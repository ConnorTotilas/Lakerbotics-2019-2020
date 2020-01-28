from wpilib.command import Command
from networktables import NetworkTables


class Targeting(Command):
    '''
    Reads inputs from camera to get in range and aim at target
    '''

    def __init__(self):
        super().__init__("Targeting")

        self.requires(self.getRobot().drive)

    def execute(self):
        KpAim = -0.1
        KpDistance = -0.1
        min_aim_command = 0.05

        table = NetworkTables.getTable("limelight")
        tx = table.getNumber('tx',None)
        ty = table.getNumber('ty',None)
       

        heading_error = -tx
        distance_error = -ty
        steering_adjust = 0.0
        left_command = 0.0
        right_command = 0.0

        if (tx > 1.0):
        
                steering_adjust = KpAim*heading_error - min_aim_command
        
        elif (tx < 1.0):
        
                steering_adjust = KpAim*heading_error + min_aim_command
        

        distance_adjust = KpDistance * distance_error

        left_command += steering_adjust + distance_adjust
        right_command -= steering_adjust + distance_adjust

        self.getRobot().drive.speed2(left_command, right_command)

