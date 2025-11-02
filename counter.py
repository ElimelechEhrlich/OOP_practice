class Counter:
    def __init__(self, count=0):
        self.count = count

    def increase(self):
        self.count += 1

    def decrease(self):
        self.count -= 1

    def reset(self):
        self.count = 0
    
    def get_value(self):
        return (f'{self.count}')
    

c1 = Counter()
print(c1.get_value())
c1.increase()
c1.increase()
c1.increase()
c1.increase()
print(c1.get_value())
c1.decrease()
c1.decrease()
print(c1.get_value())
c1.reset()
print(c1.get_value())
