from typing import Dict, List
import uuid

import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.classifier_out import ClassifierOut
from gotyai_client.model.classifier_spec_in import ClassifierSpecIn
from gotyai_client.model.batch_fit_in import BatchFitIn
from gotyai_client.model.fit_in import FitIn
from gotyai_client.model.predict_in import PredictIn
from gotyai_client.model.predict_out import PredictOut

BASE_URL = 'http://ns3044521.ip-91-121-222.eu:8080/gotyai'
X_API_KEY = '12c87b63238c65f334ac61788903cd75'


class GotyaiNB:
    def __init__(self, categories: List[str]):
        self._configuration = gotyai_client.Configuration(
            host=BASE_URL
        )
        self._configuration.api_key['api_key'] = X_API_KEY

        with gotyai_client.ApiClient(self._configuration) as api_client:
            api_instance = classify_api.ClassifyApi(api_client)

            api_response: ClassifierOut = api_instance.multinomial_create(
                body=ClassifierSpecIn(
                    classifierName=str(uuid.uuid4()),
                    categories=categories,
                )
            )

            self._uuid_model = api_response.body['uuid']

    @staticmethod
    def _batching(iterable_1, iterable_2, size=100):
        length = len(iterable_1)

        for dx in range(0, length, size):
            yield iterable_1[dx:min(dx + size, length)], iterable_2[dx:min(dx + size, length)]

    def fit(self, features: List[Dict], targets: List[str]) -> None:
        if len(features) != len(targets):
            raise 'dimensions of features and targets are not equal'

        with gotyai_client.ApiClient(self._configuration) as api_client:
            api_instance = classify_api.FitMany(api_client)

            for features_batch, targets_batch in self._batching(features, targets, size=100):
                api_instance.fit_many(
                    path_params={
                        'classifierUuid': self._uuid_model,
                    },
                    body=BatchFitIn(
                        rows=[
                            FitIn(
                                x=features_batch[index],
                                y=targets_batch[index],
                            ) for index, _ in enumerate(features_batch)
                        ],
                    ),
                )

    def predict(self, x) -> str:
        with gotyai_client.ApiClient(self._configuration) as api_client:
            api_instance = classify_api.PredictOne(api_client)

            api_response: PredictOut = api_instance.predict_one(
                path_params={
                    'classifierUuid': self._uuid_model,
                },
                body=PredictIn(
                    x=x
                )
            )

        return api_response.body['y']
