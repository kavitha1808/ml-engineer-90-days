class Fan:
    def __init__(self):
        self.is_on = False
        self.speed = 0

    def turn_on(self):
        self.is_on = True
        self.speed = 1
        print("Fan turned ON")

    def increase_speed(self):
        if self.is_on:
            self.speed += 1
            print("Speed increased to", self.speed)
        else:
            print("Fan is OFF")

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        print("Fan turned OFF")

    def status(self):
        print("\nFan Status")
        print("ON :", self.is_on)
        print("Speed :", self.speed)


fan = Fan()
fan.turn_on()
fan.increase_speed()
fan.increase_speed()
fan.status()
fan.turn_off()
fan.status()
