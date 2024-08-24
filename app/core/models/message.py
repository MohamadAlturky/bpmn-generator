from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role: str
    content: str

class MessageHistory(BaseModel):
    messages: List[Message]
    
    
def add_message_to_history(message_history: MessageHistory, role: str, content: str) -> None:
    new_message = Message(role=role, content=content)
    message_history.messages.append(new_message)
