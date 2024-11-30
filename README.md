"# raspberry_ai" 

# Raspberry pi can be used as a home assistant
1. task automation [ lights and electric fan ]
2. voice recognition
3. answer question
4. remember something where i put the item
5. play music
6. schedule manage


# Generate a text dictionary that will be converted into json format
1. message : represent the response of the assistant
2. action : represent the action that the assistant will execute
3. close : represent if the voice sound should be stopped or just do it silently
# Optional arguments based on the action that the assistant
- play music :
    1. music : repsent the music that will be played 
- remember something where i put the item :
    1. item : represent what item to be saved in the database
    2. place : represent where to place the item putted.
    3. item_id : represent the id of the item that will be saved in the database
- schedule manage :
    1. schedule : represent the day and time when the schedule be setted.
    2. activity : represent the activity that will be done in the schedule.
    3. schedule_id : represent the id of the schedule that will be saved in the database
- task automation [ lights and electric fan ] :
    1. light : represent the light that will be turned on or off
    2. fan : represent the fan that will be turned on or off


# Data type of each text dictionary
1. message : string
2. action : string
3. close : boolean
4. music : string
5. item : string
6. place : string
7. item_id : string
8. schedule : string
9. schedule_id : string
10. activity : string
11. light : string
12. fan : string


# Example of the data type of each text dictionary
1. message : "Hello world!"
2. action : "answer" | "music" | "remember" | "schedule" | "automate"
3. close : true | false
# Optional arguments based on the action that the assistant
- play music :
    1. music : "music.mp3"
- remember something where i put the item :
    1. item : "phone"
    2. place : "desk"
    3. item_id : "1"
- schedule manage :
    1. schedule : "2023-05-10 12:00:00"
    2. activity : "read a book"
    3. schedule_id : "1"
- task automation [ lights and electric fan ] :
    1. light : "on" | "off"
    2. fan : "on" | "off"



# Components also needed for the project
1. SD card & ffmusicplayer
2. Bluetooth components Arduino








