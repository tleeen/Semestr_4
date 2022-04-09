class BigBell:
    a = 'ding'

    def sound(self):
        print(self.a)
        if self.a == 'ding':
            self.a = 'dong'
        else:
            self.a = 'ding'


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
