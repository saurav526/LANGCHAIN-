from langchanin_anthropic import ChatAnthropic 
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file

model = ChatAnthropic(model="claude-v1", temperature=0.9)
result = model.invoke("Write a tagline for an ice cream shop.") 

print(result.content)
