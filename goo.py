from logger import logging
from alarm import Alarm

if __name__ == "__main__":
    try:
        alarm = Alarm(alarm_json_path="./data/alarm.json", notes_json_path="./data/notes.json")
        alarm.check()
    except Exception as e:
        print(e)
        logging.exception("An unexpected error occurred")