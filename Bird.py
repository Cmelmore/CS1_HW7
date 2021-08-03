"""
Author: Christina Elmore
RIN: 661542904
Section: 2
Assignment: Homework 7 Part 2
Purpose: Class for the birds from the above assignment
"""
import math
from Pig import *

class Bird(object):
    def __init__( self, n, x0, y0, r, dx, dy): #initilize bird class
        self.name = n
        self.x = float(x0)
        self.y = float(y0)
        self.radius = float(r)
        self.dx = float(dx)
        self.dy = float(dy)
        
    def __str__(self): #returns name and position of bird
        return '%s (%.1f,%.1f)' %(self.name, self.x, self.y)
    
    def print_name(self): #returns name of bird
        return '%s' %(self.name)
    
    def position(self): #returns position of bird
        return '(%.1f,%.1f)' %(self.x, self.y)
    
    def bird_speed(self): #returns speed of bird
        return ((self.dx)**2 + (self.dy)**2)**0.5
        
    def speed_reduction(self): #reduces dx by 50% when bird hits a pig
        self.dx /= 2
        self.speed = ((self.dx)**2 + (self.dy)**2)**0.5
        return '(%.1f,%.1f)' %(self.dx, self.dy)
        
    def move_bird(self): #move the bird for one time step
        self.x += self.dx
        self.y += self.dy
        
    def collision_check(self, pig): #check if bird has colided with a pig
        center_dist = ((self.x-float(pig.x))**2 + (self.y-float(pig.y))**2)**0.5
        radii_sum = self.radius + float(pig.radius)
        if center_dist <= radii_sum:
            return True
        else:
            return False

    def exit_screen(self): #check if the bird has gone off the board
        if (self.y-self.radius) < 0 or (self.y+self.radius) > 1000:
            return True
        if self.x-self.radius < 0 or self.x+self.radius > 1000:
            return True
        return False