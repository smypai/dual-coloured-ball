import random
from sql import Sqlite
from log import logger as log
class Generation:
    # red 01～33，blue 01～16
    def red(self):
        reds = []
        for i in range(6):
            while True:
                red = random.randint(1, 33)
                if red not in reds:
                    reds.append(red)
                    break
        reds.sort()
        return reds

    def blue(self):
        return random.randint(1, 16)

    def check(self):
        reds = self.red()
        blue = self.blue()
        history = Sqlite().sel(reds[0],reds[1],reds[2],reds[3],reds[4],reds[5], blue)
        generation = Sqlite().gsel(reds[0],reds[1],reds[2],reds[3],reds[4],reds[5], blue)
        if history and generation:
            Sqlite().addNew(reds[0], reds[1], reds[2], reds[3], reds[4], reds[5], blue)
            reds.append(blue)
            return reds
        else:
            return self.check()

    def main(self):
        log.info("--------------------------Generation-------------------------------")
        for x in range(5):
            log.info(self.check())
