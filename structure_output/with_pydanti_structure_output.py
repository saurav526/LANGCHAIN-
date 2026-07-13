from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict ,Annotated , Optional
from pydantic import BaseModel , EmailStr ,field


load_dotenv()
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

class Review(BaseModel):
    key_themes : list[str] = field(..., description="A list of key points from the review")
    summary: str = field(..., description="A brief summary of the review")
    pros: Optional[list[str]] = field(default=None, description="A list of positive aspects mentioned in the review")
    cons: Optional[list[str]] = field(default=None, description="A list of negative aspects mentioned in the review")
    name : Optional[str] = field(default=None, description="Name of the reviewer")

structured_llm = model.with_structured_output(Review)

result = structured_llm.invoke("""I've been using these wireless Bluetooth headphones for a few weeks, and they've been a great everyday companion. The sound quality is clear, with balanced bass and crisp vocals, making them suitable for music, podcasts, and video calls.

The battery life is impressive, lasting around 25–30 hours on a single charge under normal use. Pairing with devices is quick and stable, and the Bluetooth connection remains reliable even when moving around the house or office.

The headphones are lightweight and comfortable enough to wear for long periods without causing discomfort. The controls are intuitive, allowing easy adjustment of volume, playback, and calls. Additionally, the built-in microphone provides clear voice quality during calls. Overall, these headphones offer excellent value for their price, combining good sound quality, long battery life, and user-friendly features. I would recommend them to anyone looking for a reliable pair of wireless headphones.""")
print(result)
print(result.name)
print(result["summary"])
print(result["summary"])
print(result["key_themes"])
print(result["pros"])
print(result["cons"])
