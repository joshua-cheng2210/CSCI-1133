class Item():
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"Item size: {self.size}"

    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False

def Warehouse(Item):
    # def __init__(self, address, lst):
    #     # Item.__init__(self)
    #     self.address = address
    #     self.list = lst

    def __init__(self, address, lst):
        self.address = address
        self.list = lst

    def normalize(self):
        self.list.sort()

    def __add__(self, other):
        for stuff in self.list:
            other.list.append(stuff)
        other.list.sort()
        return Warehouse(self.address, other.list)

    def __repr__(self):
        return str(self.list)

    def add_item(self, other):
        self.list.append(other)


f = Warehouse("abc", [Item(4)])
print(f.address)
