
# import nextpy as xt
# from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
# from pydantic import BaseModel, EmailStr

# # Set Up the App State
# class EmailFormState(xt.State):
#     sender_email: str = ""
#     receiver_email: str = ""
#     message: str = ""

#     async def send_email(self):
#         # Replace with your email server details
#         conf = ConnectionConfig(
#             MAIL_USERNAME="your_email@gmail.com",
#             MAIL_PASSWORD="your_email_password",
#             MAIL_FROM="your_email@gmail.com",
#             MAIL_PORT=587,
#             MAIL_SERVER="smtp.gmail.com",
#             MAIL_TLS=True,
#             MAIL_SSL=False,
#             USE_CREDENTIALS=True,
#             VALIDATE_CERTS=True
#         )

#         # Create a MessageSchema for sending the email
#         message = MessageSchema(
#             subject="Email from NextPy App",
#             recipients=[self.receiver_email],
#             body=self.message,
#             subtype="html"  # Specify the subtype here, e.g., "plain" or "html"
#         )

#         # Create FastMail instance and send the email
#         fm = FastMail(conf)
#         await fm.send_message(message)

# # Basic styling
# style = {
#     "input": {
#         "padding": "8px",
#         "margin": "8px",
#         "border": "1px solid #ccc",
#         "border_radius": "4px",
#         "width": "300px",
#     },
#     "button": {
#         "padding": "10px",
#         "margin": "8px",
#         "background": "#4CAF50",
#         "color": "white",
#         "border": "none",
#         "border_radius": "4px",
#         "cursor": "pointer",
#     },
#     "container": {
#         "spacing": "1em",
#         "align_items": "center",
#         "justify_content": "center",
#         "height": "100vh",
#     }
# }

# # Design the Main Page
# def index():
#     return xt.vstack(
#         xt.input(placeholder="Sender's Email", name="sender_email", type_="email", value=EmailFormState.sender_email, **style["input"]),
#         xt.input(placeholder="Receiver's Email", name="receiver_email", type_="email", value=EmailFormState.receiver_email, **style["input"]),
#         xt.input(placeholder="Message", name="message", multiline=True, value=EmailFormState.message, **style["input"]),
#         xt.button("Submit", type_="submit", on_click=EmailFormState.send_email, **style["button"]),
#         **style["container"]
#     )

# # Build and Run the App
# app = xt.App()
# app.add_page(index)
# app.compile()
# import nextpy as xt
# from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
# from pydantic import EmailStr

# # Set Up the App State
# class EmailFormState(xt.State):
#     sender_email: EmailStr = ""
#     sender_password: str = ""  # Add sender_password property
#     receiver_email: EmailStr = ""
#     message: str = ""

#     async def send_email(self):
#         # Replace with your email server details
#         conf = ConnectionConfig(
#             MAIL_USERNAME=self.sender_email,
#             MAIL_PASSWORD=self.sender_password,  # Use sender_password here
#             MAIL_FROM=self.sender_email,
#             MAIL_PORT=587,
#             MAIL_SERVER="smtp.gmail.com",
#             MAIL_TLS=True,
#             MAIL_SSL=False,
#             USE_CREDENTIALS=True,
#             VALIDATE_CERTS=True
#         )

#         # Create a MessageSchema for sending the email
#         message = MessageSchema(
#             subject="Email from NextPy App",
#             recipients=[self.receiver_email],
#             body=self.message,
#             subtype="html"  # Specify the subtype here, e.g., "plain" or "html"
#         )

#         # Create FastMail instance and send the email
#         fm = FastMail(conf)
#         await fm.send_message(message)

# # Basic styling
# style = {
#     "input": {
#         "padding": "8px",
#         "margin": "8px",
#         "border": "1px solid #ccc",
#         "border_radius": "4px",
#         "width": "300px",
#     },
#     "button": {
#         "padding": "10px",
#         "margin": "8px",
#         "background": "#4CAF50",
#         "color": "white",
#         "border": "none",
#         "border_radius": "4px",
#         "cursor": "pointer",
#     },
#     "container": {
#         "spacing": "1em",
#         "align_items": "center",
#         "justify_content": "center",
#         "height": "100vh",
#     }
# }

# # Design the Main Page
# def index():
#     return xt.vstack(
#         xt.input(placeholder="Sender's Email", name="sender_email", type_="email", bind=EmailFormState.sender_email, **style["input"]),
#         xt.input(placeholder="Sender's Password", name="sender_password", type_="password", bind=EmailFormState.sender_password, **style["input"]),  # Use type="password" for passwords
#         xt.input(placeholder="Receiver's Email", name="receiver_email", type_="email", bind=EmailFormState.receiver_email, **style["input"]),
#         xt.input(placeholder="Message", name="message", multiline=True, bind=EmailFormState.message, **style["input"]),
#         xt.button("Submit", type_="submit", on_click=EmailFormState.send_email, **style["button"]),
#         **style["container"]
#     )

# # Build and Run the App
# app = xt.App()
# app.add_page(index)
# app.compile()

import nextpy as xt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import EmailStr
import sqlalchemy
from databases import Database

# Database Configuration
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

emails = sqlalchemy.Table(
    "emails",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("sender_email", sqlalchemy.String),
    sqlalchemy.Column("receiver_email", sqlalchemy.String),
    sqlalchemy.Column("message", sqlalchemy.String),
)

# FastAPI Configuration
api_app = FastAPI()

# OAuth2 Password Bearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get the current user based on the provided token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real application, you would verify the token and retrieve user details
    # This is a simple example and doesn't provide real authentication
    if token != "fake-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return "fake-user"

# Set Up the App State
class EmailFormState(xt.State):
    sender_email: EmailStr = ""
    sender_password: str = ""
    receiver_email: EmailStr = ""
    message: str = ""

    async def send_email(self):
        # Replace with your email server details
        conf = ConnectionConfig(
            MAIL_USERNAME=self.sender_email,
            MAIL_PASSWORD=self.sender_password,
            MAIL_FROM=self.sender_email,
            MAIL_PORT=587,
            MAIL_SERVER="smtp.gmail.com",
            MAIL_TLS=True,
            MAIL_SSL=False,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
        )

        # Create a MessageSchema for sending the email
        message = MessageSchema(
            subject="Email from NextPy App",
            recipients=[self.receiver_email],
            body=self.message,
            subtype="html",
        )

        # Create FastMail instance and send the email
        fm = FastMail(conf)
        await fm.send_message(message)

        # Save the form data to the database
        query = emails.insert().values(
            sender_email=self.sender_email,
            receiver_email=self.receiver_email,
            message=self.message,
        )
        await database.execute(query)

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
    return xt.vstack(
        xt.input(placeholder="Sender's Email", name="sender_email", type_="email", bind=EmailFormState.sender_email, **style["input"]),
        xt.input(placeholder="Sender's Password", name="sender_password", type_="password", bind=EmailFormState.sender_password, **style["input"]),
        xt.input(placeholder="Receiver's Email", name="receiver_email", type_="email", bind=EmailFormState.receiver_email, **style["input"]),
        xt.input(placeholder="Message", name="message", multiline=True, bind=EmailFormState.message, **style["input"]),
        xt.button("Submit", type_="submit", on_click=EmailFormState.send_email, **style["button"]),
        **style["container"]
    )

# Build and Run the App
app = xt.App()
app.add_page(index)
app.compile()