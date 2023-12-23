

import os
import nextpy as xt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import EmailStr
from pydantic import validator


# Set Up the App State
class EmailFormState(xt.State):
    sender_email: EmailStr = ""
    api_key: str = os.environ.get('SENDGRID_API_KEY', '')
    receiver_email: EmailStr = ""
    message: str = ""

    @validator("sender_email")
    def validate_sender_email(cls, v):
        try:
            EmailStr.validate(v)
        except ValueError as e:
            print(f"Validation error for sender_email: {v}. Error: {str(e)}")
            raise e
        return v

    async def send_email(self, sender_email: EmailStr, api_key: str, receiver_email: EmailStr, message: str):
        conf = ConnectionConfig(
            MAIL_USERNAME="apikey",
            MAIL_PASSWORD=api_key,
            MAIL_FROM=sender_email,
            MAIL_PORT=587,
            MAIL_SERVER="smtp.sendgrid.net",
            MAIL_TLS=True,
            MAIL_SSL=False,
            USE_CREDENTIALS=True,
        )

        message = MessageSchema(
            subject="Email from NextPy App",
            recipients=[receiver_email],
            body=message,
            subtype="html",
        )

        fm = FastMail(conf)
        await fm.send_message(message)

# Basic styling
style = {
    "input": {
        "padding": "8px",
        "margin": "8px",
        "border": "1px solid #ccc",
        "border_radius": "4px",
        "width": "300px",
    },
    "button": {
        "padding": "10px",
        "margin": "8px",
        "background": "#4CAF50",
        "color": "white",
        "border": "none",
        "border_radius": "4px",
        "cursor": "pointer",
    },
    "container": {
        "spacing": "1em",
        "align_items": "center",
        "justify_content": "center",
        "height": "100vh",
    }
}

# Design the Main Page
def index():
    sender_email_input = xt.input(placeholder="Sender's Email", name="sender_email", type_="email", bind=EmailFormState.sender_email, **style["input"])
    api_key_input = xt.input(placeholder="SendGrid API Key", name="api_key", type_="password", bind=EmailFormState.api_key, **style["input"])
    receiver_email_input = xt.input(placeholder="Receiver's Email", name="receiver_email", type_="email", bind=EmailFormState.receiver_email, **style["input"])
    message_input = xt.input(placeholder="Message", name="message", multiline=True, bind=EmailFormState.message, **style["input"])

    submit_button = xt.button("Submit", type_="submit", on_click=lambda: EmailFormState.send_email(EmailFormState.sender_email, EmailFormState.api_key, EmailFormState.receiver_email, EmailFormState.message), **style["button"])

    return xt.vstack(sender_email_input, api_key_input, receiver_email_input, message_input, submit_button, **style["container"])

# Build and Run the App
app = xt.App()
app.add_page(index)
app.compile()
