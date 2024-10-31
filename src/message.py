import base64
import datetime

from src.interfaces import IMessage


class CommonMessage(IMessage):
    """
    Класс для сообщений

        Методы:
        get_message(): Возвращает сообщение
        print(): Выводит сообщение в консоль
    """
    def __init__(self, message: str):
        self._message = message

    def get_message(self):
        """
        Метод для получение сообщения.

        :return: Сообщение.
        """
        return self._message

    def print(self):
        """
        Метод для вывода сообщения в консоль.
        :return: None.
        """
        print(self._message)


class MessageDecorator(IMessage):
    """
    Базовый декоратор для сообщений

        Методы:
        get_message(): Возвращает сообщение
        print(): Выводит сообщение в консоль
    """
    def __init__(self, message: IMessage):
        self._message = message

    def get_message(self):
        """
        Метод для получение сообщения.

        :return: Сообщение.
        """
        return self._message.get_message()

    def print(self):
        print(self.get_message())


class MessageWithHeader(MessageDecorator):
    """
     Декоратор добавлющий заголовок к сообщению

        Методы:
        get_message(): Возвращает сообщение с заголовком
        print(): Выводит сообщение с заголовком в консоль
    """
    def get_message(self):
        """
        Метод для получение сообщения c хедером.

        :return: Сообщение.
        """
        return "Добрый день,\n" + self._message.get_message()


class MessageWithFooter(MessageDecorator):
    """
     Декоратор добавлющий футер к сообщению

        Методы:
        get_message(): Возвращает сообщение с футером
        print(): Выводит сообщение с футером в консоль
    """
    def get_message(self):
        """
        Метод для получение сообщения с футером.

        :return: Сообщение.
        """
        return self._message.get_message() + "\nДед Мороз"


class MessageWithDate(MessageDecorator):
    """
     Декоратор добавлющий дату к сообщению

        Методы:
        get_message(): Возвращает сообщение с датой
        print(): Выводит сообщение с датой в консоль
    """
    def get_message(self):
        """
        Метод для получение сообщения с датой.

        :return: Сообщение.
        """
        return self._message.get_message() + "\n" + self._get_date_str()

    @staticmethod
    def _get_date_str():
        return datetime.datetime.now().strftime("%d.%m.%Y")


class MessageInBase64(MessageDecorator):
    """
     Декоратор преобразующий сообщение в base64

        Методы:
        get_message(): Возвращает сообщение в base64
        print(): Выводит сообщение в base64 в консоль
    """
    def get_message(self):
        """
        Метод для получение сообщения в base64.

        :return: Сообщение.
        """
        return self._convert_in_base64(self._message.get_message())

    @staticmethod
    def _convert_in_base64(message):
        """
        Метод для преобразования строки.

        :param message: Строка.
        :return: Строка в base64.
        """
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('utf-8')

        return base64_message

