def send_email(mail, recipient, *, sender = 'university.help@gmail.com'):
    if "@" not in recipient or (
            not recipient.endswith(".com") and not recipient.endswith(".ru") and not recipient.endswith(
        ".net")) or "@" not in sender or (
            not sender.endswith(".com") and not sender.endswith(".ru") and not sender.endswith(".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print('Нельзя отправить самому себе!')
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


