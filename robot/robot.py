from datetime import datetime
import json
class Robot:
    """A class to repersent a robot."""

    def __init__(self, robot_dict):
        """Initialize attributes of a robot."""
        self.name = robot_dict['name']
        self.date_created = robot_dict['date_created']
        self.owner = robot_dict['owner']
        self.password = robot_dict['password']

def set_up_robot():
    """Set up a new robot."""
    print("Enter 'q' in any of the inputs(leaving the password) if you don't want to create a robot.")
    # Get information about the robot.
    name = input("Robot name: ")
    if name == 'q':
        return
    owner = input("Robot owner name: ")
    if owner == 'q':
        return
    password = input(f"Password for accessing robot(tip: {name]}123): ")
    date_created = str(datetime.now())
    # Create a dict about the robot and store it in a file.
    robot_dict = {
        'name': name,
        'owner': owner,
        'date_created': date_created,
        'password': password,
    }
    filename = '/home/ishaan/Documents/Ishaan\'s-Coding/robot/robots.json'
    with open(filename) as f:
        robot_list = json.load(f)
        robot_list.append(robot_dict)
    with open(filename, 'w') as f:
        json.dump(robot_list, f, indent=4)
    launch = input("The robot is created sucessfully!\n \
    do you want to launch it now?(Y/n): ")
    if launch == 'Y':
        robot = Robot(robot_dict)
set_up_robot()