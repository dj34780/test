import wpilib
import wpilib.drive
import time
import ctre

class MyRobot(wpilib.TimedRobot): 
    def robotInit(self):
        print("init")
        self.motor ctre.WPI_TalonSRX(15)
        self.motor.set(.5)
        print("motor on right")
        time.sleep(3)
        self.motor.set(0)
        print("motor stop")

if __name__ == "__main__":
    wpilib.run(MyRobot)