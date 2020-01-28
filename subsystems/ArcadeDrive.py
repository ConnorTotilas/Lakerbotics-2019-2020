import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.drive import DifferentialDrive
from commands.throttlemixer import ThrottleMixer

class Arcade(Subsystem):
    """
    Subsystem to control the motors for ArcadeDrive
    """

    def __init__(self):
        super().__init__("Arcade")

        # motors and the channels they are connected to

        self.frontLeftMotor = wpilib.PWMVictorSPX(0)
        self.rearLeftMotor = wpilib.PWMVictorSPX(1)
        self.frontRightMotor = wpilib.PWMVictorSPX(2)
        self.rearRightMotor = wpilib.PWMVictorSPX(3)

        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.drive = DifferentialDrive(self.left, self.right)

        self.drive.setExpiration(0.1)
        self.drive.setSafetyEnabled(False)
    def speed(self, xSpeed, zRotation):
        self.drive.arcadeDrive(xSpeed, zRotation)
    
    def speed2(self, leftSpeed, rightSpeed):
        self.drive.tankDrive(leftSpeed, rightSpeed)
    
    def initDefaultCommand(self):
        self.setDefaultCommand(ThrottleMixer())