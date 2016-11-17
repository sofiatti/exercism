import operator

NORTH, WEST, SOUTH, EAST = 'NORTH', 'WEST', 'SOUTH', 'EAST'

class Robot:
   
    directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
  
    def __init__(self, bearing=NORTH, x_coord=0, y_coord=0):
        self.bearing = bearing    
        self.coordinates = (x_coord, y_coord) 
    def turn_right(self):
        new_direction = (self.directions.index(self.bearing) + 1) % 4
        self.bearing = self.directions[new_direction]
    def turn_left(self):
        new_direction = (self.directions.index(self.bearing) - 1) % 4
        self.bearing = self.directions[new_direction]
    def advance(self):
        advancing = {NORTH:(0,1), SOUTH:(0,-1), EAST:(1,0), WEST:(-1,0)}
        move = advancing[self.bearing] 
        self.coordinates = tuple(map(operator.add, self.coordinates, move))
    def simulate(self, command):
        switcher = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance
            }         
        for letter in command: 
            func = switcher.get(letter)
            func()

if __name__ == '__main__':
    robot = Robot(NORTH, 7, 3)
    robot.simulate("RAALAL")
    print('FINAL', robot.coordinates)
    print('EXPECTED', (9,4))

