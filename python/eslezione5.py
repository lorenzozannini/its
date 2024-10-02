def create_playlist(name,*song):
    d={}
    d[name]=set(song)
    return d
dict=create_playlist("Road Trip", "Song 1", "Song 2")

def add_like(d,name,liked):
    d[name]=d[name],liked
    return d
print(add_like(dict,"Road Trip" ,liked=True))

def add_book(name,*book):
    d={}
    d[name]=list(book)
    return d
dict=add_book("Mark Twain", "The Adventures of Tom Sawyer", "Life on the Mississippi")
print(dict)
def delete_book(d,name):
    d.__delitem__(name)
print(delete_book(dict, "Mark Twain"))

def build_profile(name,surname,occupation=None,location=None,age=None):
    d={}
    d[surname]=name,occupation,location,age
    return d
print(build_profile("John", "Doe", occupation="Developer", location="USA", age=30))

def plan_event(name,l,hour):
    d={}
    d[name]=l,hour
    return d
dict=plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
def modify_event(d,name,*all):
    d[name]=all
    return d
print(modify_event(dict, "Code Workshop", ["Alice", "Bob", "Charlie"], "4pm"))

def create_shopping_list(name,*items):
    d={}
    d[name]=items
    return d
dict=create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
def print_shopping_list(d,name):
    print(d[name])
print_shopping_list(dict,"Grocery Store")
