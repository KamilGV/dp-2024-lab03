from abc import ABC, abstractmethod


class IMessage(ABC):
    """
    Интерфейс для сообщений

        Методы:
        get_message(): Возвращает сообщение
        print(): Выводит сообщение в консоль
    """

    @abstractmethod
    def get_message(self) -> str:
        """
        Метод для получение сообщения.

        :return: Сообщение.
        """
        pass

    @abstractmethod
    def print(self):
        """
        Метод для вывода сообщения в консоль.
        :return: None.
        """
        pass
