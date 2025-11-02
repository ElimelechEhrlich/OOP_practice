class Timer:
    def __init__(self, seconds = 0):
        self.seconds = seconds

    def set_time(self, sec):
        self.sec = sec
        self.seconds += self.sec

    def get_time(self):
        mm = int(self.seconds / 60)
        ss = self.seconds % 60
        return f'{mm}:{ss}'
t1 = Timer()
t1.set_time(188)
print(t1.get_time())


