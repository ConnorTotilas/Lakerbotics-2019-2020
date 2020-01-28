from wpilib.command import TimedCommand
from wpilib.drive import DifferentialDrive


class Drive(TimedCommand):
    '''
    Drive command that can be used for autonomous.
    '''
    def __init__(self, xSpeed, zRotation, timeoutInSeconds):
        super().__init__("Drive", timeoutInSeconds)

        self.requires(self.getRobot().drive)
        self.xSpeed = xSpeed
        self.zRotation = zRotation

    def initialize(self):
        self.getRobot().drive.speed(self.xSpeed, self.zRotation)

    def end(self):
        self.getRobot().drive.speed(0, 0)