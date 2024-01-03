# Configuration and Constants
MLFLOW_EXPERIMENT_NAME = "textclassification"
MLFLOW_RUN_NAME = "text-classification"
MLFLOW_MODEL_NAME = "TextClassificationModel"

ADLS_CONTAINER = "xxx" # FILL HERE YOUR STORAGE ACCOUNT
ADLS_STORAGE_ACCOUNT = "xxx" # FILL HERE YOUR STORAGE ACCOUNT

BATCH_SIZE = 32
TEST_SIZE = 0.2
SEED = 42
VOCAB_SIZE = 10000
START_PARTITION_DATE = "20230101"

STAGE = "Production"
DATE_FORMAT = "%Y%m%d"