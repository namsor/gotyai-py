import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

DEFAULT_TRANSFORMED_VALUE = 0


class DataSet:
    def __init__(self, file_path: str, target_column_name: str) -> None:
        self._original_data = pd.read_csv(file_path)
        self._target_column_name = target_column_name
        self._target_categories = list(self._original_data[target_column_name].sort_values().unique())

        self._encoder = OrdinalEncoder(
            categories=[list(self._original_data[c].sort_values().unique()) for c in self._original_data.columns]
        )

        self._transformed_dataset = self._encoder.fit_transform(self._original_data)
        self._target_column_index = self._find_target_column(target_column_name)

        self._original_features, self._original_targets = self._separate_samples_by_features_and_targets()

        self._transformed_features = np.delete(self._transformed_dataset, self._target_column_index, axis=1)
        self._transformed_targets = self._transformed_dataset[:, self._target_column_index]

    def _separate_samples_by_features_and_targets(self) -> tuple[list[dict], list]:
        features, targets = [], []

        for sample in self._original_data.values:
            sample_of_feature = {
                feature_name: sample[column_index]
                for column_index, feature_name in enumerate(self._original_data.columns)
                if feature_name != self._target_column_name
            }
            target = sample[self._target_column_index]

            features.append(sample_of_feature)
            targets.append(target)

        return features, targets

    def _find_target_column(self, target_column: str) -> int:
        for index, column in enumerate(self._original_data.columns):
            if column == target_column:
                return index

        raise f'Column {target_column} is absent in dataset'

    @property
    def transformed_ds(self):
        return self._transformed_dataset

    @property
    def original_features(self):
        return self._original_features

    @property
    def transformed_features(self):
        return self._transformed_features

    @property
    def original_targets(self):
        return self._original_targets

    @property
    def transformed_targets(self):
        return self._transformed_targets

    @property
    def target_categories(self):
        return self._target_categories

    def prepare_row_for_predict(self, request: dict) -> np.ndarray:
        copy_request = dict(request)

        copy_request[self._target_column_name] = self._encoder.categories[self._target_column_index][0]

        for feature in request:
            copy_request[feature] = [copy_request[feature]]

        transform_df = self._encoder.transform(pd.DataFrame(copy_request))

        return np.delete(transform_df, self._target_column_index, axis=1)

    def decode_into_categorical(self, predicted):
        samples = []

        for p in predicted:
            row = []

            for index, _ in enumerate(self._original_data.columns):
                if index == self._target_column_index:
                    row.append(p)
                else:
                    row.append(DEFAULT_TRANSFORMED_VALUE)

            samples.append(row)

        return self._encoder.inverse_transform(samples)[:, self._target_column_index]
