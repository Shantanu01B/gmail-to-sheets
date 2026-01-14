import json
import os
from gmail_service import (
    get_gmail_service,
    get_unread_emails,
    get_email_details,
    mark_email_as_read,
)
from email_parser import parse_email
from sheets_service import get_sheets_service, append_row
from config import SPREADSHEET_ID


STATE_FILE = "processed_emails.json"


def load_processed_ids():
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r") as f:
        return set(json.load(f))


def save_processed_ids(ids):
    with open(STATE_FILE, "w") as f:
        json.dump(list(ids), f)


def main():
    gmail_service = get_gmail_service()
    sheets_service = get_sheets_service()

    processed_ids = load_processed_ids()
    messages = get_unread_emails(gmail_service)

    for msg in messages:
        msg_id = msg["id"]

        if msg_id in processed_ids:
            continue

        email = get_email_details(gmail_service, msg_id)
        data = parse_email(email)

        row = [
            data["from"],
            data["subject"],
            data["date"],
            data["content"],
        ]

        append_row(sheets_service, SPREADSHEET_ID, row)
        mark_email_as_read(gmail_service, msg_id)

        processed_ids.add(msg_id)

    save_processed_ids(processed_ids)
    print("✅ Emails added to Google Sheets successfully")


if __name__ == "__main__":
    main()
