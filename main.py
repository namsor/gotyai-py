from sklearn.naive_bayes import GaussianNB
from loguru import logger

from gotyai.dataset import DataSet
from gotyai.transport.client import HTTPClient


DATASET_FILE_PATH = 'datasets/golf_df.csv'
TARGET_COLUMN_NAME = 'Play'
ROW_FOR_PREDICT = {
    'Outlook': 'rainy',
    'Temperature': 'cool',
    'Humidity': 'high',
    'Windy': False,
}
NAMSOR_BASE_URL = 'http://ns3044521.ip-91-121-222.eu:8080/gotyai'
X_API_KEY = '<GotyAI API KEY>'


if __name__ == '__main__':
    ds = DataSet(DATASET_FILE_PATH, TARGET_COLUMN_NAME)

    # Begin Python Version ---------------------------------------------------------------------------------------------
    logger.info('Beginning of minimalist Naive Bayes Classifier implementation in Python')
    model = GaussianNB()
    model.fit(ds.transformed_features, ds.transformed_targets)

    request = ds.prepare_row_for_predict(ROW_FOR_PREDICT)

    predicted = model.predict(request)
    logger.info(f'Predicted result is = {ds.decode_into_categorical(predicted)[0]}')
    logger.info('Finish of minimalist Naive Bayes Classifier implementation in Python\n')
    # End Python Version -----------------------------------------------------------------------------------------------

    # Begin GotyAI Version ---------------------------------------------------------------------------------------------
    logger.info('Beginning usage of GotyAI API Client')
    client = HTTPClient(NAMSOR_BASE_URL, X_API_KEY)

    try:
        classifier_id = client.create_classifier(ds.target_categories)
        logger.info(f'Classifier was created with UUID = {classifier_id}')

        client.fit_model_with_several_rows(classifier_id, ds.original_features, ds.original_targets)
        logger.info(f'Model was fitted by {len(ds.original_targets)} samples')

        result, score, probability = client.predict_with_one_row(classifier_id, ROW_FOR_PREDICT)
        logger.info(f'Predicted result is = {result}, score = {score}, probability = {probability}')
        logger.info('Finish usage of GotyAI API Client')
    except Exception as e:
        logger.error(e)
    # End GotyAI Version -----------------------------------------------------------------------------------------------
