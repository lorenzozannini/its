from room import Room

class Building:
    def __init__(self,name,address,floors) -> None:
        self.name=name
        self.address=address
        self.floors=floors
        self.rooms=[]
    
    def add_room(self,room):
        if room not in self.get_rooms() and room.floors <= self.get_floors():
            pass
    
    def get_name(self):
        return self.name
    
    def get_addreess(self):
        return self.address
    
    def get_floors(self):
        return self.floors