
import json


class DataHandler:
    
    items_filename = "items.json"
    users_filename = "users.json"
    schedule_filename = "schedules.json"

    items : dict = None
    """
     {
         "item_id": {
             "item": "Item Name",
             "place": "Item Location"
         },
         #...
     }
    """
    
    user : dict = None
    """
     {
        "master": "Makie Tech",
        "assistant": "Odilon" 
     }
    """
    
    schedules : dict = None
    """
    {
        "schedule_id": {
            "schedule": "2023-05-10 12:00:00",
            "activity": "read a book"
        },
        #...
    }
    """
    
    def __init__(self):
        self.load_items()
        self.load_users()
        self.load_schedules()
        
    
    def load_items(self):
        with open(self.items_filename, "r") as file:
            self.items = json.load(file)
    
    def load_users(self):
        with open(self.users_filename, "r") as file:
            self.user = json.load(file)
    
    def load_schedules(self):
        with open(self.schedule_filename, "r") as file:
            self.schedules = json.load(file)
    
    def save_items(self):
        with open(self.items_filename, "w") as file:
            json.dump(self.items, file)
    
    def save_users(self):
        with open(self.users_filename, "w") as file:
            json.dump(self.user, file)
    
    def save_schedules(self):
        with open(self.schedule_filename, "w") as file:
            json.dump(self.schedules, file)






