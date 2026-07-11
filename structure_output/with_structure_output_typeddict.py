from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

class Review(TypedDict):
    summary: str
    sentiment: str
structured_llm = model.with_structured_output(Review)

result = structured_llm.invoke("""I've been using these wireless Bluetooth headphones for a few weeks, and they've been a great everyday companion. The sound quality is clear, with balanced bass and crisp vocals, making them suitable for music, podcasts, and video calls.

The battery life is impressive, lasting around 25–30 hours on a single charge under normal use. Pairing with devices is quick and stable, and the Bluetooth connection remains reliable even when moving around the house or office.

The headphones are lightweight and comfortable enough to wear for long periods without causing discomfort. The controls are intuitive, allowing easy adjustment of volume, playback, and calls. Additionally, the built-in microphone provides clear voice quality during calls. Overall, these headphones offer excellent value for their price, combining good sound quality, long battery life, and user-friendly features. I would recommend them to anyone looking for a reliable pair of wireless headphones.""")

print(result)
