from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB
from loguru import logger

from gotyai.dataset import DataSet
from gotyai.model import GotyaiNB


DATASET_FILE_PATH = 'datasets/golf_df.csv'
TARGET_COLUMN_NAME = 'Play'
ROW_FOR_PREDICT = {
    'Outlook': 'rainy',
    'Temperature': 'cool',
    'Humidity': 'high',
    'Windy': 'no',
}
# Available models: GotyaiNB, GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB
PREDICTION_MODEL = 'GotyaiNB'


if __name__ == '__main__':
    ds = DataSet(DATASET_FILE_PATH, TARGET_COLUMN_NAME)
    transformed_row_for_predict = ds.prepare_row_for_predict(ROW_FOR_PREDICT)

    sklearn_models = {
        'GaussianNB':    GaussianNB(),
        'MultinomialNB': MultinomialNB(),
        'ComplementNB':  ComplementNB(),
        'BernoulliNB':   BernoulliNB(),
        'CategoricalNB': CategoricalNB(),
    }

    if PREDICTION_MODEL in sklearn_models:
        # Begin one of sklearn model version ---------------------------------------------------------------------------
        logger.info(f'Beginning of sklearn {PREDICTION_MODEL} Naive Bayes Classifier')
        try:
            model = sklearn_models[PREDICTION_MODEL]
            model.fit(ds.transformed_features, ds.transformed_targets)

            predicted = model.predict(transformed_row_for_predict)

            logger.info(f'Predicted result is = {ds.decode_into_categorical(predicted)[0]}')
            logger.info(f'Finish of sklearn {PREDICTION_MODEL} Naive Bayes Classifier')
        except Exception as e:
            logger.error(e)
        # End sone of sklearn model version ----------------------------------------------------------------------------
    elif PREDICTION_MODEL == 'GotyaiNB':
        # Begin of GotyAI Version --------------------------------------------------------------------------------------
        logger.info('Beginning usage of Naive Bayes Classifier based on GotyAI API')
        try:
            model = GotyaiNB(ds.target_categories)
            model.fit(ds.original_features, ds.original_targets)

            predicted = model.predict(ROW_FOR_PREDICT)

            logger.info(f'Predicted result is = {predicted}')
            logger.info('Finish usage of Naive Bayes Classifier based on GotyAI API\n')
        except Exception as e:
            logger.error(e)
        # End of GotyAI Version ----------------------------------------------------------------------------------------
    else:
        logger.error(f'Unknown <{PREDICTION_MODEL}> prediction model')
