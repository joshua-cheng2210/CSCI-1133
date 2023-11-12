import random

class Crew:
    '''
Purpose: normal member of the crewship
Instance variables: 
    self.name = name of member
    self.status = Active by default, Injured otherwise
    self.location = Sleep Pods by default, location of the member
Methods: 
    move: move the member from one part of the ship to another
    repair: unknown step for normal crew
    first_aid: unknown step for normal crew
    fire_lasers: unknown step for knormal crew
'''

    def __init__(self, name):
        self.name = name
        self.status = "Active"
        self.location = "Sleep Pods"

    def __repr__(self):
        return f"{self.name} : {self.status}, at {self.location}"

    def move(self, location):
        if location in ["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]:
            self.location = location
        else:
            print("Not a valid location.")

    def repair(self, ship):
        print(f"{self.name} doesn't know how to do that.")
    def first_aid(self, ship):
        print(f"{self.name} doesn't know how to do that.")
    def fire_lasers(self, ship, target_ship, target_location):
        print(f"{self.name} doesn't know how to do that.")

class Starship():
    '''
Purpose: the crewship
Instance variables: 
    self.name = name of ship
    self.crew_list = list of the members of the crews on the crewship
Methods: 
    encounter: for every member of the crewship that has Active status will move to a random spot on the ship. and then the same for the enemy_ship
'''
    def __init__(self, name, crew_list):
        self.name = name
        self.crew_list = crew_list
        self.damaged = {'Bridge':False, 'Medbay':False, 'Engine':False, 'Lasers':False, 'Sleep Pods':False}

    def encounter(self, enemy_ship):
        for ppl in self.crew_list:
            ppl.move(random.choice(["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]))
        for ppl in enemy_ship.crew_list:
            ppl.move(random.choice(["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]))

class Engineer(Crew):
    '''
Purpose: repair the part of the ship if it is damaged
Instance variables: 
    None
Methods: 
    repair: repair the part of the ship if it is damaged
'''
    def repair(self, ship):
        if ship.damaged[self.location] == True:
            ship.damaged[self.location] = False
            print(f"{self.name} fixed the damage to {self.location}.")
        else:
            print(f"{self.location} isn't damaged.")

class Captain(Crew):
    '''
Purpose: damaged the enemy's part of the ship and change the status of whoever in the part of the ship to Injured
Instance variables: 
    None
Methods: 
    fire_lasers: damaged the enemy's part of the ship and change the status of whoever in the part of the ship to Injured
'''
    def fire_lasers(self, ship, target_ship, target_location):
        if target_location not in ["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]:
            print("Not a valid location.")
        elif self.location != "Bridge":
            print(f"{self.name} must be in the Bridge to fire lasers.")
        elif ship.damaged["Bridge"] == True:
            print("Bridge is too damaged to order lasers to be fired.")
        elif ship.damaged["Lasers"] == True:
            print("Lasers are too damaged to fire.")
        else:
            target_ship.damaged[target_location] = True
            print(f"{ship.name} fires lasers at {target_ship}'s {target_location}.")
            for ppl in target_ship.crew_list:
                if ppl.location == target_location:
                    ppl.status = "Injured"

class Doctor(Crew):
    '''
Purpose: change crew member status from Injured to Active
Instance variables: 
    self.medpacs = 3 by default, minus one everytime used
Methods: 
    first_aid: spend one medpac to change everybody's status from Injured to Active at the same location of the Doctor
'''
    def __init__(self, name):
        Crew.__init__(self, name)
        self.medpacs = 3

    def first_aid(self, ship):
        if self.location == "Medbay" and ship.damaged["Medbay"] == False:
            self.medpacs = 3
            print(f"{self.name}'s supply of medpacs has been replenished.")
            for ppl in ship.crew_list:
                if ppl.location == "Medbay" and ppl.status == "Injured":
                    ppl.status = "Active"
                    print(f"{self.name} healed {ppl.name}'s injuries.")
        elif self.medpacs == 0:
            print(f"{self.name} has no medpacs left.")
        else:
            self.medpacs -= 1
            for ppl in ship.crew_list:
                if self.location == ppl.location and ppl.status == "Injured":
                    ppl.status = "Active"
                    print(f"{self.name} healed {ppl.name}'s injuries.")
 
