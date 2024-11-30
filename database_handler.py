
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
        "assistant": "Odilon",
        "password": "makietech"
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

    def add_item(self, name : str, place : str):
        item_id = list(self.items.keys())[-1]
        self.items[item_id] = {
            "item": name,
            "place": place
        }
    
    def remove_item(self, item_id : int):
        if item_id in self.items:
            del self.items[item_id]
    
    def update_item(self, name : str, place : str, item_id : int):
        self.items[item_id] = {
            "item": name,
            "place": place
        }

    def add_schedule(self, schedule : str, activity : str):
        schedule_id = list(self.schedules.keys())[-1]
        self.schedules[schedule_id] = {
            "schedule": schedule,
            "activity": activity
        }
        
    def remove_schedule(self, schedule_id : int):
        if schedule_id in self.schedules:
            del self.schedules[schedule_id]

    def update_schedule(self, schedule : str, activity : str, schedule_id : int):
        self.schedules[schedule_id] = {
            "schedule": schedule,
            "activity": activity
        }

    def get_item(self, item_id : int):
        return self.items[item_id]

    def get_schedule(self, schedule_id : int):
        return self.schedules[schedule_id]

    def get_items(self):
        return self.items

    def get_schedules(self):
        return self.schedules

    def get_user(self):
        return self.user

    def get_master(self):
        return self.user["master"]

    def get_assistant(self):
        return self.user["assistant"]

    def get_password(self):
        return self.user["password"]

    def get_schedule_by_date(self, date : str):
        schedules = []
        for schedule_id, schedule in self.schedules.items():
            if schedule["schedule"].startswith(date):
                schedules.append(schedule)
        return schedules

    def get_schedule_by_activity(self, activity : str):
        schedules = []
        for schedule_id, schedule in self.schedules.items():
            if schedule["activity"] == activity:
                schedules.append(schedule)
        return schedules
