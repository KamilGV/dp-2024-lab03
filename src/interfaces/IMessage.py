from abc import ABC, abstractmethod


class IMessage(ABC):
    @abstractmethod
    def get_message(self):
        pass

    @abstractmethod
    def print(self):
        pass
