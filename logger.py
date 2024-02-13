import os
import datetime
import logging

# Configure logging
LOG_FILENAME = "./data/error.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

LOG_FILE_PATH = "./data/log.log"

def _write_to_file(text):
    with open(LOG_FILE_PATH, "a+") as F:
        F.writelines(text)

def log(func):
    def wrapper(*args, **kwargs):
        _write_to_file(str(datetime.datetime.now())+os.linesep)
        _write_to_file(f"Entering {func.__name__} with arguments: {args}, {kwargs}"+os.linesep)
        result = func(*args, **kwargs)
        _write_to_file(f"Exiting {func.__name__} with result: {result}"+os.linesep)
        _write_to_file("*"*30+os.linesep)
        return result
    return wrapper

@log
def __test_log(name):
    return "000"

if __name__ == "__main__":
    __test_log("manish")
