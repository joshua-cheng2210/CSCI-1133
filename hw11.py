import random

class Boat:
    '''
Purpose: information about the boat
Instance variables: 
    self.boat_name = a string of the name of the boat 
    self.top_speed = an integer of the top speed of the boat
    self.current_progress = distance moved
Methods:
    __str__: to display the boat name and its top speed
    move: generate a random speed lower than it's top speed and add it to its self.current progress
'''

    def __init__(self, boat_name, top_speed = 3):
        self.boat_name = str(boat_name)
        self.top_speed = int(top_speed)
        self.current_progress = 0
    
    def set_boat_name(self, other):
        self.boat_name = str(other)
    
    def set_top_speed(self, other):
        self.top_speed = int(other)
        
    def set_current_progress(self, other):
        self.current_progress = int(other)

    def get_boat_name(self):
        return self.boat_name

    def get_top_speed(self):
        return self.top_speed
    
    def get_current_progress(self):
        return self.current_progress

    def __str__(self):
        return f"{self.boat_name}: {self.current_progress}"
    
    def move(self):
        increment = random.randint(0, self.top_speed)
        self.current_progress = self.current_progress + increment
        return increment

class BoatRace:
    '''
Purpose: information about the race and racers
Instance variables: 
    self.race_name = name of race
    self.race_id = race's id
    self.distance = race's distance
    self.racers = a list of racers objects
Methods:
    add_racers: add more boats object into the self.racers lists
    print_racers: prints all the racers and it's current progress
    count: returns the amount of racers
    race: calls the move() method on every boat until at least one boat reaches the distance of the race
'''
    def __init__(self, fname):
        with open(fname) as f:
            fp = f.readlines()
            self.race_name = fp[0].split(",")[1].strip()
            self.race_id = int(fp[1].split(",")[1])
            self.distance = int(fp[2].split(",")[1])
            self.racers = []
            for boats in range(len(fp[3:])):
                fp[3 + boats] = fp[3 + boats].strip().split(",")
                try:
                    self.racers.append(Boat(fp[3 + boats][0], int(fp[3 + boats][1])))
                except:
                    self.racers.append(Boat(fp[3 + boats][0]))

    def get_race_name(self):
        return self.race_name
    
    def get_race_id(self):
        return self.race_id
    
    def get_distance(self):
        return self.distance
    
    def get_racers(self):
        return self.racers

    def add_racer(self, other):
        self.racers.append(other)

    def print_racers(self):
        for x in self.racers:
            print(x)

    def count(self):
        return len(self.racers)

    def race(self):
        winners = []
        while len(winners) == 0:
            for xx in self.racers:
                xx.move()
            self.print_racers() # how to call other ethods in another method?
            winners = []
            for xxx in self.racers:
                if xxx.current_progress >= self.distance:
                    winners.append(xxx)
            if len(winners) > 0:
                return winners