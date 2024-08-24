import os
from groq import Groq

from ..prompts import IPromptSender
from ...models.message import MessageHistory


class GroqPromptSender(IPromptSender):
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def send_prompt_history(self, prompt_history: MessageHistory):
        messages = [{"role": message.role, "content": message.content} for message in prompt_history.messages]
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=os.getenv("GROQ_MODEL_NAME_70B")
        )
        return chat_completion.choices[0].message.content
