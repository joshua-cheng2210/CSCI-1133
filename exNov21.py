class House:
    def __init__(self, beds, baths, haunted):
        self.beds = beds
        self.baths = baths
        self.haunted = haunted
    def remove_ghosts(self):
        self.haunted = False
    def estimate_price(self):
        value = self.beds*3000+self.baths*2000
        if self.haunted:
            return value//2
        else:
            return value

class Mansion(House):
    def __init__(self, beds, baths, haunted=True):
        House.__init__(self, beds, baths, haunted)
        # self.beds = beds
        # self.baths = baths
        self.haunted = True
    
    def remove_ghosts(self):
        print("Too spooky, call an expert")

    def estimate_price(self):
        return House.estimate_price(self) * 5

place = Mansion(10,5)
print(place.beds)
print(place.baths)
print(place.haunted)
place.remove_ghosts()
print(place.haunted)
print(place.estimate_price())
