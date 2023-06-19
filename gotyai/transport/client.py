import uuid

import httpx
from httpx_auth import HeaderApiKey

from gotyai.transport.const import APP_JSON_HEADER
from gotyai.transport.errors import HttpError
from gotyai.transport.requests import CreateClassifierRequest, FitModelByOneRequest, PredictByOneRequest, FitModelByManyRequest
from gotyai.transport.responses import CreateClassifierResponse, PredictResponse


class HTTPClient:
    def __init__(self, host: str, api_key: str):
        """
        :param host: base url.
        :param api_key: X_API_KEY for http requests.
        """
        self._host = host
        self._api_key = api_key

    def create_classifier(self, target_categories: list[str]) -> str:
        """
        Creating classifier.
        :param target_categories: Unique categories without duplicates of dataset's target.
        :return: UUID of classifier
        """
        request = CreateClassifierRequest(classifierName=str(uuid.uuid4()), categories=target_categories)

        with httpx.Client() as client:
            origin_response = client.post(
                f'{self._host}/api2/json/multinomialCreate',
                headers=APP_JSON_HEADER, auth=HeaderApiKey(self._api_key),
                data=request.json(by_alias=True), timeout=None
            )

        if origin_response.status_code >= 300:
            raise HttpError(
                f'Create classifier endpoint. Status code = {origin_response.status_code}. Message = {origin_response.content.decode("utf-8")}.')

        response = CreateClassifierResponse(**origin_response.json())

        return response.uuid

    def fit_model_with_one_row(self, classifier_uuid: str, features: dict, target: str) -> None:
        """
        Fit model by one sample.
        :param classifier_uuid: UUID of classifier.
        :param features: Map of features. For example: {'Outlook': 'sunny', 'Temperature': 'hight', ...}
        :param target: Value of target. For example: 'yes' or 'not'.
        :return:
        """
        request = FitModelByOneRequest(x=features, y=target)

        with httpx.Client() as client:
            origin_response = client.post(
                f'{self._host}/api2/json/fitOne/{classifier_uuid}',
                headers=APP_JSON_HEADER, auth=HeaderApiKey(self._api_key),
                data=request.json(by_alias=True), timeout=None
            )

        if origin_response.status_code >= 300:
            raise HttpError(
                f'Fit model by one row endpoint. Status code = {origin_response.status_code}. Message = {origin_response.content.decode("utf-8")}.')

    def fit_model_with_several_rows(self, classifier_uuid: str, features: list[dict], targets: list[str]) -> None:
        """
        Fit model by several samples.
        :param classifier_uuid: UUID of classifier.
        :param features: List of features map. For example: [{'Outlook': 'sunny', 'Temperature': 'hight', ...},]
        :param targets: List of target values. For example: ['yes', ..., 'no'].
        :return:
        """
        if len(features) != len(targets):
            raise 'dimensions of features and targets are not equal'

        # Using batching because there is a limit of consumption on the server side
        for features_batch, targets_batch in self._batching(features, targets, size=100):
            request = FitModelByManyRequest(rows=[
                FitModelByOneRequest(x=features_batch[index], y=targets_batch[index])
                for index, _ in enumerate(features_batch)
            ])

            with httpx.Client() as client:
                origin_response = client.post(
                    f'{self._host}/api2/json/fitMany/{classifier_uuid}',
                    headers=APP_JSON_HEADER, auth=HeaderApiKey(self._api_key),
                    data=request.json(by_alias=True), timeout=None
                )

            if origin_response.status_code >= 300:
                raise HttpError(
                    f'Fit model by several rows endpoint. Status code = {origin_response.status_code}. Message = {origin_response.content.decode("utf-8")}.')

    def predict_with_one_row(self, classifier_uuid: str, features: dict) -> tuple[str, float, float]:
        """
        Make a predict target value by features.
        :param classifier_uuid: UUID of classifier.
        :param features: List of features map. For example: [{'Outlook': 'sunny', 'Temperature': 'hight', ...},]
        :return: Answer , score and probability.
        """
        request = PredictByOneRequest(x=features)

        with httpx.Client() as client:
            origin_response = client.post(
                f'{self._host}/api2/json/predictOne/{classifier_uuid}',
                headers=APP_JSON_HEADER, auth=HeaderApiKey(self._api_key),
                data=request.json(by_alias=True), timeout=None
            )

        if origin_response.status_code >= 300:
            raise HttpError(
                f'Predict by one sample endpoint. Status code = {origin_response.status_code}. Message = {origin_response.content.decode("utf-8")}.')

        response = PredictResponse(**origin_response.json())

        return response.y, response.score, response.proba

    @staticmethod
    def _batching(iterable_1, iterable_2, size=100):
        length = len(iterable_1)

        for dx in range(0, length, size):
            yield iterable_1[dx:min(dx + size, length)], iterable_2[dx:min(dx + size, length)]

