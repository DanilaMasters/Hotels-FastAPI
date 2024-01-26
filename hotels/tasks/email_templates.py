from email.message import EmailMessage
from pydantic import EmailStr
from hotels.config import SMTP_USER


def create_booking_confirmation_template(booking: dict, email_to: EmailStr):
    email = EmailMessage()

    email['Subject'] = 'Booking confirmation'
    email['From'] = SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
            <h1>Hello World!</h1>
        """,
        subtype='html'
    )
    return email