"""
Author: Christina Elmore
RIN: 661542904
Section: 2
Assignment: Homework 7 Part 2
Purpose: Simulate a simplified angry birds
"""
from Pig import *
from Bird import *

if __name__ == '__main__':
    bird_file = raw_input('Enter the bird file ==> ')
    print bird_file
    pig_file = raw_input('Enter the pigs file ==> ')
    print pig_file
    
    #creates list of birds in game
    bird_list = []
    for line in open(bird_file):
        bird = line.strip().split('|')
        bird = Bird(bird[0], bird[1], bird[2], bird[3], bird[4], bird[5])
        bird_list.append(bird)

    #creates list of pigs in game
    pig_list = []
    for line in open(pig_file):
        pig = tuple(line.strip().split('|'))
        pig = Pig(pig[0], pig[1], pig[2], pig[3])
        pig_list.append(pig)
    
    #prints game starting information
    print "Num birds %d:" %len(bird_list)
    for bird in bird_list:
        print "%s %s" %(bird.print_name(), bird.position())
    print "...."
    print "Num pigs %d:" %len(pig_list)
    print "Time 0: %s starts at %s" %(bird_list[0].print_name(), bird_list[0].position())
    
    time = 0
    i = 0
    
    #runs through the time steps for the simulation
    while len(pig_list) > 0 and len(bird_list) >= i+1:
        time += 1
        bird_list[i].move_bird()
        
        #checks for collisions with pigs
        for pig in pig_list:
            if bird_list[i].collision_check(pig) == True:
                print "Time %d: %s at %s pops %s"%(time, bird_list[i].print_name(), bird_list[i].position(), str(pig))
                pig_list.remove(pig)
                reduced_speed = bird_list[i].speed_reduction()
                print "Time %d: %s at %s has (dx,dy) = %s" %(time, bird_list[i].print_name(), bird_list[i].position(), reduced_speed)
                
                #when a bird passes below minimum speed
                if bird_list[i].bird_speed() < 6:
                    print "Time %d: %s at %s with speed %.1f stops" %(time, bird_list[i].print_name(), bird_list[i].position(), bird_list[i].bird_speed())
                    i += 1
                    if i == len(bird_list):
                        break                    
                    print "Time %d: %s starts at %s" %(time, bird_list[i].print_name(), bird_list[i].position())
                if len(pig_list)== 0:
                    break        
        
        #when a bird leaves the screen
        if i == len(bird_list):
            break        
        if bird_list[i].exit_screen() == True:
            
            print "Time %d: %s at %s has left the game" %(time, bird_list[i].print_name(), bird_list[i].position())
            i += 1
            if i == len(bird_list):
                break
            print "Time %d: %s starts at %s" %(time, bird_list[i].print_name(), bird_list[i].position())
            
    #if birds win
    if len(pig_list) == 0:
        print "Time %s: All pigs are popped. The birds win!" %time
        
    #if pigs win           
    elif i == len(bird_list):
        print "Time %s: No more birds. The pigs win!\nRemaining pigs:" %(time)
        for pig in pig_list:
            print str(pig)    