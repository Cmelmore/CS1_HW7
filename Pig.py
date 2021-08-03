"""
Author: Christina Elmore
RIN: 661542904
Section: 2
Assignment: Homework 7 Part 2
Purpose: Class for the pigs from the above assignment
"""
class Pig(object):
    def __init__( self, n, x0, y0, r0 ):
        self.name = n
        self.x = x0
        self.y = y0
        self.radius = r0
        
    def __str__(self):
        return self.name