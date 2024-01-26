from pathlib import Path
import smtplib

from pydantic import EmailStr
from hotels.tasks.celery import celery
from PIL import Image

from hotels.tasks.email_templates import create_booking_confirmation_template
from hotels.config import SMTP_HOST, SMTP_PASS, SMTP_PORT, SMTP_USER

@celery.task
def process_pic(
    path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized = im.resize((1000, 500))
    im_resized.save(f'hotels/static/images/resized_{im_path.name}')


@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg_content)
    