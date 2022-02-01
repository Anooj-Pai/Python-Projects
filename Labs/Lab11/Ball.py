class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color): #creats the initalizing function
        self.radius = radius
        self.color = color
        self.start_x = x # reset function
        self.start_y = y
        self.start_dx = dx
        self.start_dy = dy
        self.ball_x,self.ball_y = x,y   # initial location
        self.ball_radius = radius
        self.ball_dx,self.ball_dy = dx,dy   # the movement of the ball object
        self.ball_color = color
    def position(self):
        return (self.ball_x,self.ball_y) #returns the cordinates initalized
    def move(self):
        self.ball_x += self.ball_dx #moves it by the value of dx and dy
        self.ball_y += self.ball_dy
    def move(self):
        self.ball_x += self.ball_dx #moves it by the value of dx and dy
        self.ball_y += self.ball_dy
    def bounding_box(self):
        self.ball_box_x0 = self.ball_x - self.radius #creats a box around it based off radius of circle
        self.ball_box_y0 = self.ball_y - self.radius
        self.ball_box_x1 = self.ball_x + self.radius
        self.ball_box_y1 = self.ball_y + self.radius
        return (self.ball_box_x0, self.ball_box_y0, self.ball_box_x1, self.ball_box_y1)
    def get_color(self):
        return self.color
    def some_inside(self, maxx, maxy):
        return ((self.ball_y + self.radius) > 0 and (self.ball_y - self.radius) < maxy and (self.ball_x + self.radius) > 0 and (self.ball_x - self.radius) < maxx) #if its x0 cord of box is less then maxx and so on its in the frame
    def reset(self):
        self.ball_x = self.start_x # makes reset work
        self.ball_y = self.start_y #reset position and velocity direction
        self.ball_dx,self.ball_dy = self.start_dx, self.start_dy
    def check_and_reverse(self, maxx, maxy):
        if(self.ball_x + self.radius >= maxx): # change to negative if its greater then furthest x bound
            self.ball_dx *= -1
        elif(self.ball_x - self.radius <= 0): # change to negative if its less then lowest y bound
            self.ball_dx *= -1
        elif(self.ball_y + self.radius >= maxy):  # change to negative if its greater then furthest y bound
            self.ball_dy *= -1
        elif(self.ball_y - self.radius <= 0): # change to negative if its less then lowest x bound
            self.ball_dy *= -1