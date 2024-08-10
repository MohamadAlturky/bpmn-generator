import os
from ..prompts import IPromptSender
from ...models.message import MessageHistory
import openai

class OpenAIPromptSender(IPromptSender):
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def send_prompt_history(self, prompt_history: MessageHistory):
        messages = [{"role": message.role, "content": message.content} for message in prompt_history.messages]
        
        completion = self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL_NAME"),
            messages=messages)
        
        return completion.choices[0].message
