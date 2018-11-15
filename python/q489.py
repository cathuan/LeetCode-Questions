# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class RobotWrapper(object):
    def __init__(self, robot):

        self.robot = robot
        self.pos = (0, 0)
        self.ori = 0  # 0=up, 1=right, 2=down, 3=left
        self.orientation = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

    def addCell(self, ori):
        move = self.orientation[ori]
        return (self.pos[0] + move[0], self.pos[1] + move[1])

    def nextCell(self):
        return self.addCell(self.ori)

    def move(self):
        if self.robot.move():
            self.pos = self.nextCell()
            return True
        return False

    def turnRight(self):
        self.ori = (self.ori + 1) % 4
        self.robot.turnRight()

    def turnLeft(self):
        self.ori = (self.ori - 1) % 4
        self.robot.turnLeft()

    def clean(self):
        self.robot.clean()

    # move back. No matter whether it's successful, always face to the
    # same orientation as current.
    def back(self):
        self.turnRight()
        self.turnRight()
        if self.move():
            self.turnRight()
            self.turnRight()
            return True
        else:
            self.turnRight()
            self.turnRight()
            return False


# Use DFS to solve the problem.
# - keep track of the current locations, and record all cleaned cell.
# - for each cell, clean it's right/below/left/up cells. One problem is the robot needs to go back.
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        robot = RobotWrapper(robot)
        visited = set([(0, 0)])
        self.dfs(robot, visited)

    def dfs(self, robot, visited):
        robot.clean()
        for _ in range(4):
            robot.turnRight()
            cell = robot.nextCell()
            if cell not in visited and robot.move():
                visited.add(cell)
                self.dfs(robot, visited)
                robot.back()