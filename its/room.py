class Room:
    def __init__(self,name,floor,num_seats) -> None:
        self.set_name(name)
        self.set_floor(floor)
        self.set_num_seats(num_seats)

    def set_name(self,name):
        self.name=name

    def set_floor(self,floor):
        self.floor=floor
    
    def set_num_seats(self,num_seats):
        self.num_seats=num_seats
    
    def get_name(self):
        return self.name
    
    def get_floor(self):
        return self.floor
    
    def get_num_seats(self):
        return self.num_seats