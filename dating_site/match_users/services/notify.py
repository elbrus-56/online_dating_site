from config.settings import SENDER
from django.core.mail import EmailMessage


class Notify:

    @classmethod
    def send_email(cls,
                   subject: str = '',
                   message: str = '',
                   attachments: tuple = None,
                   emails: list = None
                   ) -> int:
        """
            Функция отправляет уведомления на электронную почту

            Args:
                subject (str): тема письма
                message (str): сообщение для отправки
                attachments (tuple): вложения
                emails (list): email получателей

            Returns:
                int: 1 if True else 0
        """

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=SENDER,
            to=emails,
        )

        if attachments:
            filename, content, mimetype = attachments
            try:
                with open(content, "rb") as file:
                    content = file.read()
            except FileNotFoundError:
                print(f"Файл {content} не найден")
            email.attach(filename, content, mimetype)

        return email.send(fail_silently=False)
