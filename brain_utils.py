
from g4f.client import Client
import time



class BrainUtils:
    
    client = Client()
    model = "gpt-4o-mini"
    
    debounce = 2
    
    
    async def generate_response(self, text : str):
        """
        Generates a response based on the provided text.
        """
        # while True:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": text}],
            )
            self.debounce = 2 # Reset the delay
            print(f"The response is: {response.choices[0].message.content}")
            return str(response.choices[0].message.content)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(self.debounce)
            self.debounce  = self.debounce * self.debounce

    
