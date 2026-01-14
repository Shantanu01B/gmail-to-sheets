# Gmail to Google Sheets Automation

## 👤 Author
Shantanu Barge

---

## 📖 Project Overview

This project is a Python-based automation system that reads **unread emails** from a Gmail inbox and logs them into a **Google Sheet** using official Google APIs.

The automation extracts important email details such as sender, subject, date, and content, and appends them as rows in a Google Sheet. The system is designed to be **idempotent**, meaning re-running the script does not create duplicate entries.

---

## 🎯 Objective

For each qualifying email, the following fields are captured and stored in Google Sheets:

| Column | Description |
|------|------------|
| From | Sender email address |
| Subject | Email subject |
| Date | Date & time received |
| Content | Email body (plain text) |

---

## 🏗️ High-Level Architecture

Gmail Inbox (Unread Emails)
↓
Gmail API (OAuth 2.0)
↓
Python Script
↓
Email Parser
↓
Google Sheets API
↓
Google Sheet (Rows Appended)


---

## 🛠️ Tech Stack

- Language: **Python 3**
- APIs Used:
  - Gmail API
  - Google Sheets API
- Authentication: **OAuth 2.0**
- Data Storage: Google Sheets
- State Management: Local JSON file

---

## 📂 Project Structure

gmail-to-sheets/
│
├── src/
│ ├── main.py
│ ├── gmail_service.py
│ ├── sheets_service.py
│ ├── email_parser.py
│ └── config.py
│
├── credentials/
│ └── credentials.json (NOT committed)
│
├── proof/
│ ├── gmail_unread.png
│ ├── google_sheet.png
│ └── oauth_consent.png
│
├── processed_emails.json (NOT committed)
├── token.json (NOT committed)
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd gmail-to-sheets

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Google Cloud Setup

Create a Google Cloud Project

Enable:

Gmail API

Google Sheets API

Configure OAuth Consent Screen (External)

Add your Gmail as a Test User

Create OAuth Client ID (Desktop App)

Download credentials.json into credentials/

4️⃣ Configure Spreadsheet

Create a Google Sheet

Add headers: From | Subject | Date | Content

Copy the Spreadsheet ID

Paste it into src/config.py

5️⃣ Run the Script
python src/main.py


On first run, Google OAuth will open in the browser. Grant permissions.

🔐 OAuth Flow Explanation

This project uses OAuth 2.0 (Installed App flow):

User is redirected to Google login

User grants Gmail and Sheets access

Access token is saved locally (token.json)

Token is reused for future executions

Service accounts are not used, as required.

🔁 Duplicate Prevention Logic

Each Gmail email has a unique message ID.

Processed message IDs are stored in processed_emails.json

Before inserting a row, the script checks if the ID already exists

If found, the email is skipped

This guarantees:

No duplicate rows

Safe re-execution of the script

💾 State Persistence Method

State is persisted using a local JSON file:

processed_emails.json


Why this approach?

Gmail message IDs are globally unique

JSON is lightweight and easy to manage

No external database required

🚧 Challenges Faced

Issue:
Google Sheets has a limit of 50,000 characters per cell, causing errors for large HTML emails.

Solution:
The email content is truncated to a safe length before insertion, ensuring reliable execution without data loss.

⚠️ Limitations

Very large emails are truncated to fit Google Sheets limits

Only unread emails are processed

Attachments are not handled

📸 Proof of Execution

Screenshots included in /proof/ folder:

Gmail inbox with unread emails

Google Sheet populated with data

OAuth consent screen

A 2–3 minute demo video demonstrates:

Project flow

Gmail → Sheets data movement

Duplicate prevention

Safe re-execution

✅ Conclusion

This project demonstrates secure API integration, stateful automation, and reliable data processing using Python and Google APIs, following all assignment requirements.
