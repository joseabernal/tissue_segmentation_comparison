from configuration import general_configuration, training_configuration
from workflow.evaluate import run_evaluation_in_dataset

run_evaluation_in_dataset(general_configuration, training_configuration)