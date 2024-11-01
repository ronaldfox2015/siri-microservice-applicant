from app.notification.domain.items import ItemsEntity, MailBody
from app.notification.domain.mail_repository import MailRepository
from flask import Flask, render_template, current_app, abort
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class MailRepositoryImpl(MailRepository):
    def __init__(self, config):
        self.config = config

    def send(self, itemsEntity: ItemsEntity):
        global server
        try:
            # Crear el mensaje
            msg = MIMEMultipart('alternative')
            msg['From'] = itemsEntity.addressee.From
            msg['To'] = itemsEntity.addressee.To
            msg['Subject'] = itemsEntity.addressee.Subject
            # Adjuntar el contenido HTML al correo
            html_part = MIMEText(itemsEntity.mailBody.html, 'html')
            current_app.logger.info(itemsEntity.mailBody.html)

            msg.attach(html_part)

            # Conectar al servidor SMTP
            server = smtplib.SMTP(self.config['smtp_server'] , self.config['smtp_port'])
            server.starttls()  # Iniciar el cifrado TLS
            server.login(self.config['username'], self.config['password'])  # Autenticarse

            # Enviar el correo
            server.sendmail(itemsEntity.addressee.From, itemsEntity.addressee.To, msg.as_string())

            print("Correo enviado con éxito")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
        # finally:
            # Cerrar la conexión al servidor
            # server.quit()

    def html(self, itemsEntity: MailBody):
        template_name = '{}.html'.format(itemsEntity.slug)
        template_path = os.path.join('templates', template_name)
        if not os.path.exists("/app/notification/infrastructure/{}".format(template_path)):
            abort(404)

        return render_template(template_name, user_name=itemsEntity.recipient_data.get("user_name", "Invitado"))

