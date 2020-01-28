from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from commands.targeting import Targeting

def getJoystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    button1 = JoystickButton(joystick, 1)

    button1.whileHeld(Targeting())
    
    return Joystick


