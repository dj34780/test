import wpilib
import ctre
import time

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor = ctre.WPI_TalonSRX(15)
        self.motor.set(.5)
        time.sleep(3)
        self.motor.set(0)
        time.sleep(5)
        self.motor.set(-1)
        time.sleep(7)