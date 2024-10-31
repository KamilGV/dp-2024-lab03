import base64
import datetime

from src.message import CommonMessage, MessageWithDate, MessageWithFooter, MessageWithHeader, MessageInBase64


def test_common_message():
    test_message = 'Тестовое сообщение'
    message = CommonMessage(test_message)
    return_message = message.get_message()
    assert test_message == return_message


def test_message_with_date():
    """ Проверка корректности декоратора с хедером"""
    test_message = 'Тестовое сообщение'
    message = MessageWithDate(CommonMessage(test_message))
    return_message = message.get_message()
    assert test_message + "\n" + datetime.datetime.now().strftime("%d.%m.%Y") == return_message


def test_message_with_footer():
    """ Проверка корректности декоратора с футером"""
    test_message = 'Тестовое сообщение'
    message = MessageWithFooter(CommonMessage(test_message))
    return_message = message.get_message()
    assert test_message + "\nДед Мороз" == return_message


def test_message_with_header():
    """ Проверка корректности декоратора с датой"""
    test_message = 'Тестовое сообщение'
    message = MessageWithHeader(CommonMessage(test_message))
    return_message = message.get_message()
    assert "Добрый день,\n" + test_message == return_message


def test_message_in_base64():
    """ Проверка корректности декоратора с преобразованием в base64"""
    test_message = 'Тестовое сообщение'
    message = MessageInBase64(CommonMessage(test_message))
    return_message = message.get_message()

    decoded_data = base64.b64decode(return_message)
    decoded_string = decoded_data.decode('utf-8')

    assert test_message == decoded_string
