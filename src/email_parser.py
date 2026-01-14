import base64
from bs4 import BeautifulSoup
from datetime import datetime


def parse_email(msg):
    headers = msg["payload"]["headers"]

    sender = subject = date = ""

    for h in headers:
        if h["name"] == "From":
            sender = h["value"]
        elif h["name"] == "Subject":
            subject = h["value"]
        elif h["name"] == "Date":
            date = h["value"]

    body = ""

    if "parts" in msg["payload"]:
        for part in msg["payload"]["parts"]:
            if part["mimeType"] == "text/plain":
                body = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode("utf-8")
                break
            elif part["mimeType"] == "text/html":
                html = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")
                body = soup.get_text()
    else:
        body = base64.urlsafe_b64decode(
            msg["payload"]["body"]["data"]
        ).decode("utf-8")

    MAX_CONTENT_LENGTH = 49000  # Google Sheets limit is 50k

    return {
    "from": sender,
    "subject": subject,
    "date": date,
    "content": body.strip()[:MAX_CONTENT_LENGTH]
}

