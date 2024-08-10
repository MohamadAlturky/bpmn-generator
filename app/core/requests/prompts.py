from abc import ABC, abstractmethod

class IPromptSender(ABC):
    @abstractmethod
    def send_prompt_history(self, prompt_history):
        pass
