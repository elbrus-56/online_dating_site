from django.core.mail import EmailMessage

from config.settings import SENDER


class Notify:

    @classmethod
    def send_email(cls, subject: str = None, message: str = None, attachments: tuple = None, emails: list = None) -> None:
        """
            Функция отправляет уведомления на электронную почту

            Args:
                subject (str): тема письма
                message (str): сообщение для отправки
                attachments (tuple): вложения
                emails (list): список получателей

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
            except Exception:
                print(f"Файл {content} не найден")
            email.attach(filename, content, mimetype)

        return email.send(fail_silently=False)
