import time
import datetime

from config import PROGRESS_BAR

class ProgressBar:

    def __init__(self, length):
        self.length = length
        self.i = 0
        self.init_time = time.time()
        self.done = False
        self.show()

    def show(self):
        progress = int(self.i / self.length * PROGRESS_BAR['width'])
        t = int(time.time() - self.init_time)
        r = int(t * (self.length / max(1, self.i) - 1))
        print('[' + PROGRESS_BAR['positive'] * progress + PROGRESS_BAR['negative'] * (PROGRESS_BAR['width'] - progress) + ']', str(self.i), '/', str(self.length), 'Time Elapsed:', str(datetime.timedelta(seconds=t)), 'Estimated Time Remaining:', str(datetime.timedelta(seconds=r)), end='\r')

    def increment(self):
        if self.done: return
        self.i += 1
        self.show()
        if self.i >= self.length:
            self.done = True
            print("\nFinished in", str(datetime.timedelta(seconds=int(time.time() - self.init_time))))