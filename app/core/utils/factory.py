from abc import ABC, abstractmethod

"""
base class for connect to llms.
"""
class LLMFactory(ABC):
    
    @abstractmethod
    def create(self, model_name : str = None):
        pass        