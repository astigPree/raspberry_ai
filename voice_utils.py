

# Import the required module for text 
# to speech conversion
from gtts import gTTS

from playsound import playsound

# This module is imported so that we can 
# play the converted audio
import os
import time

class VoiceUtils:
    
    # The text that you want to convert to audio
    text = None
    
    # Language in which you want to convert
    language = 'en'

    save_path = "speech.mp3"
    
    def update_text(self, text : str):
        self.text = text
    
    def update_language(self, language : str):
        self.language = language
    
    def speak(self , text : str):
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        if self.text or text:
            myobj = gTTS(text=self.text if text is None else text, lang=self.language, slow=False)

            
            # Saving the converted audio in a mp3 file named
            # welcome 
            myobj.save(self.save_path)
             
            # Playing the converted file
            os.system(f"start {self.save_path}")
            
            
            
    def speak_with_duration(self, text : str):
        
        if self.text or text:
            myobj = gTTS(text=self.text if text is None else text, lang=self.language, slow=False)
 
            # Saving the converted audio in a mp3 file named
            # welcome 
            myobj.save(self.save_path)
             
            # Play the audio file using playsound 
            playsound(self.save_path) 
            # Calculate the duration of the audio file using gTTS estimate 
            duration = len(text.split()) / 2 
            # Rough estimate: 2 words per second 
            print(f"Audio estimated length: {duration} seconds") 
            # Add delay to ensure the audio file is played completely before proceeding 
            # time.sleep(duration + 1) 
            # Add a small buffer to ensure it completes





