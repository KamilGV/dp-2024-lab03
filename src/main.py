from src.message import CommonMessage, MessageWithDate, MessageWithFooter, MessageWithHeader, MessageInBase64

if __name__ == "__main__":
    text = 'С наступающим Новым годом!'

    common_message = CommonMessage(text)
    common_message.print()
    print('-' * 10)

    message_with_header = MessageWithHeader(common_message)
    message_with_header.print()
    print('-' * 10)

    message_with_header_and_footer = MessageWithFooter(message_with_header)
    message_with_header_and_footer.print()
    print('-' * 10)

    message_with_header_footer_and_date = MessageWithDate(message_with_header_and_footer)
    message_with_header_footer_and_date.print()
    print('-' * 10)

    message_with_header_footer_date_in_base64 = MessageInBase64(message_with_header_footer_and_date)
    message_with_header_footer_date_in_base64.print()
    print('-' * 10)
