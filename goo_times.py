import random
import logger

class GooTimes():
    times = ["05:03", "05:33", "07:03", "07:33", "08:03", "08:33", "12:03", "12:33", "12:37", "13:03", "13:33", "13:37",\
        "15:03", "15:33", "15:37", "17:03", "17:33", "17:37", "19:03", "19:33", "19:37", "20:03", "20:33", "20:37", "21:03",\
        "21:33", "21:37", "22:03", "22:33", "22:37"]
    
    def __init__(self) -> None:
        random.shuffle(self.times)

    @logger.log
    def get_todays_sporadic_times(self):
        return sorted(self.times[0:17])
    
if __name__ == "__main__":
    t = GooTimes()
    print(t.get_todays_sporadic_times())
