import time
import datetime
import json

import player
import speak
import goo_times

class Alarm():
    _instance = None

    audio_player = player.Player()
    text_to_speech = speak.TextToSpeech()
    alarm_times = goo_times.GooTimes()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self, alarm_json_path, notes_json_path) -> None:
        super().__init__()
    
        try:
            self.alarms = json.loads(open(alarm_json_path).read())
            self.notes = json.loads(open(notes_json_path).read())
        except:
            raise ValueError("Inappropriate value for given json file. Check its correct formatting...")

        #in current design for all sporadic alarms, same times and frequency applies
        self.todays_sporadic_times = self.alarm_times.get_todays_sporadic_times()

    def check(self):
        """
        every 37 seconds poll if some alarm time has arrived #may 57 would be fine to just run once in a minute

        :param nothing:
            none

        :returns: nothing
            nothing
        """

        while True:
            alarm_content_ids = []

            #regular alarms
            for alarm in self.alarms:
                if alarm["type"] == "regular-reminder":
                    hour, minutes, sec = alarm["time"].split(":")
                    
                    if datetime.datetime.now().hour == int(hour) and datetime.datetime.now().minute == int(minutes):
                        alarm_content_ids.append(alarm["alarm-content-id"])

            #sporadic alarms
            for sporadic_time in self.todays_sporadic_times:
                hour, minutes = sporadic_time.split(":")

                if datetime.datetime.now().hour == int(hour) and datetime.datetime.now().minute == int(minutes):
                    for alarm in self.alarms:
                        if alarm["type"] == "sporadic-reminder":
                            alarm_content_ids.append(alarm["alarm-content-id"])

            for alarm_content_id in alarm_content_ids:
                if self.notes[alarm_content_id]["type"] == "audio":
                    self.audio_player.play(self.notes[alarm_content_id]["content"])
                elif self.notes[alarm_content_id]["type"] == "text":
                    self.text_to_speech.speak(self.notes[alarm_content_id]["content"])

            print("...")
            time.sleep(37)

    def __iter__(self):
        return iter(self.alarms)

if __name__ == "__main__":
    alarm = Alarm(alarm_json_path="./data/alarm.json", notes_json_path="./data/notes.json")
    # alarm.check()
    for a in alarm:
        print(a)