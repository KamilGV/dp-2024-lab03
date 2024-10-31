import base64
import datetime

from src.interfaces import IMessage


class CommonMessage(IMessage):
    def __init__(self, message: str):
        self._message = message

    def get_message(self):
        return self._message

    def print(self):
        print(self._message)


class MessageDecorator(IMessage):
    def __init__(self, message: IMessage):
        self._message = message

    def get_message(self):
        return self._message.get_message()

    def print(self):
        print(self.get_message())


class MessageWithHeader(MessageDecorator):
    def get_message(self):
        return "Добрый день,\n" + self._message.get_message()


class MessageWithFooter(MessageDecorator):
    def get_message(self):
        return self._message.get_message() + "\nДед Мороз"


class MessageWithDate(MessageDecorator):
    def get_message(self):
        return self._message.get_message() + "\n" + self._get_date_str()

    @staticmethod
    def _get_date_str():
        return datetime.datetime.now().strftime("%d.%m.%Y")


class MessageInBase64(MessageDecorator):
    def get_message(self):
        return self._convert_in_base64(self._message.get_message())

    @staticmethod
    def _convert_in_base64(message):
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('utf-8')

        return base64_message

