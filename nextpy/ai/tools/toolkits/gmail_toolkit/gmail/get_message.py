import base64
import email
from typing import Dict, Type

from pydantic import BaseModel, Field

from nextpy.ai.tools.toolkits.gmail_toolkit.gmail.base import GmailBaseTool
from nextpy.ai.tools.toolkits.gmail_toolkit.gmail.utils import clean_email_body


class SearchArgsSchema(BaseModel):
    message_id: str = Field(
        ...,
        description="The unique ID of the email message, retrieved from a search.",
    )


class GmailGetMessage(GmailBaseTool):
    name: str = "get_gmail_message"
    description: str = (
        "Use this tool to fetch an email by message ID."
        " Returns the thread ID, snipet, body, subject, and sender."
    )
    args_schema: Type[SearchArgsSchema] = SearchArgsSchema

    def run(
        self,
        message_id: str,
    ) -> Dict:
        """Run the tool."""
        query = (
            self.api_resource.users()
            .messages()
            .get(userId="me", format="raw", id=message_id)
        )
        message_data = query.execute()
        raw_message = base64.urlsafe_b64decode(message_data["raw"])

        email_msg = email.message_from_bytes(raw_message)

        subject = email_msg["Subject"]
        sender = email_msg["From"]

        message_body = email_msg.get_payload()

        body = clean_email_body(message_body)

        return {
            "id": message_id,
            "threadId": message_data["threadId"],
            "snippet": message_data["snippet"],
            "body": body,
            "subject": subject,
            "sender": sender,
        }

    async def _arun(
        self,
        message_id: str,
    ) -> Dict:
        """Run the tool."""
        raise NotImplementedError
