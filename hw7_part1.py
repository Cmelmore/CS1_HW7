"""
Author: Christina Elmore
RIN: 661542904
Section: 2
Assignment: Homework 7 Part 1
Purpose: Determine who the N busiest actors in IMDB are.
"""

if __name__=="__main__":
    imdb = raw_input("Enter the name of the IMDB file ==> ").strip()
    print imdb
    n = int(raw_input("Enter the number of top individuals ==> "))
    print n
    
    actors = {}
    movie_num = {}
    for line in open(imdb):
        words = line.strip().split('|')
        name = words[0].strip()
        movie = words[1].strip()
        
        #make actors dictionary
        if not name in actors:
            actors[name] = set()
        actors[name].add(movie)
    
    #make movies dictionary
    for actor in actors:
        num = len(actors[actor])
        if num in movie_num:
            movie_num[num].append(actor)
        else:
            movie_num[num] = [actor]
              
    sorted_num = sorted(movie_num.keys())
    
    #determines how many ranks have multiple actors and subtracts the multiples from n
    i = 1
    while i <= n:
        actor_list = movie_num[sorted_num[-i]]
        j = 0
        if len(actor_list) > 1:
            j += (len(actor_list)-1)
        n -= j
        i += 1
    n += len(movie_num[sorted_num[-n]])
    if n < 20:
        n -= 2
    
    #Prints N busiest actors
    i = 1
    while i <= n:
        actor_list = movie_num[sorted_num[-i]]
        if len(actor_list) > 1:
            actor_list.sort()
        print "%3d: %s" %(sorted_num[-i], '; '.join(actor_list))
        i += 1