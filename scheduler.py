import json
from jsonschema import validate, ValidationError
import logging


# Setup logging
logging.basicConfig(
    filename="config_error.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define jsonschema for config file
config_schema = {
    "type": "object",
    "properties": {
        "datasets": {
            "type": "object",
            "additionalProperties": {"type": "string"}
            },
        "models": {
            "type": "object",
            "additionalProperties": {"type": "string"}
            },
        "metrics": {
            "type": "array",
            "items": {"type": "string"}
            },
        },
    "required": ["datasets", "models", "metrics"]
}


def load_file(file_path):
    """Return a string"""

    with open(file_path, 'r') as file:
        return file.read()


def parse_json(file, display_json=False):
    """Return a dictionary"""

    parse_file = json.loads(file)
    if display_json == True:
        print(json.dumps(parse_file, indent=4))
    return parse_file


def validate_config(config_data):
    """Return True if config file has a correct structure"""

    try:
        validate(instance=config_data, schema=config_schema)
    except ValidationError as err:        
        log_and_print(f"Config validation error: {err.message}")
        raise ValueError(f"Config validation error: {err.message}")
    return True


# def schedule_tasks(tasks):
#     # Добавить логику планирования задач
#     return tasks


# def execute_task(task):
#     # Добавить логику выполнения задачи
#     print("Executing task:", task)


def log_and_print(message):
    """Wrapper for print() and logging messages"""

    print(message)
    logging.info(message)


def run_scheduler():
    """
    Main module of the scheduler.
    Reads the config file.
    Schedule and execute tasks.
    """

    config_data = load_file("config.json")
    parsed_config = parse_json(config_data, display_json=True)
    if validate_config(parsed_config):
        log_and_print("Valid configuration")
        # parsed_tasks = parse_tasks(tasks)
        # scheduled_tasks = schedule_tasks(tasks)
        # execute_task(task)
        # for task in scheduled_tasks:
        #     execute_task(task)
        #     time.sleep(1)  # Имитация задержки между задачами
    else:
        log_and_print("Invalid configuration")
    

if __name__ == "__main__":

    run_scheduler()
    log_and_print("The program has completed execution")
