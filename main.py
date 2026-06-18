
import os
import json
import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# -----------------------------

# Read GitHub Secrets

# -----------------------------

DISCORD_WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
GOOGLE_SHEET_ID = os.environ["GOOGLE_SHEET_ID"]
GOOGLE_SERVICE_ACCOUNT_JSON = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]

# -----------------------------

# Connect to Google Sheets

# -----------------------------

creds_dict = json.loads(GOOGLE_SERVICE_ACCOUNT_JSON)

scopes = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
creds_dict,
scopes=scopes
)

gc = gspread.authorize(creds)
sheet = gc.open_by_key(GOOGLE_SHEET_ID).sheet1

# -----------------------------

# Test Data

# -----------------------------

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
name = "Test User"
profile_link = "https://example.com/profile"
message = "GitHub Actions is working successfully!"
post_link = "https://example.com/post"

# -----------------------------

# Send to Discord

# -----------------------------

discord_message = f"""
🔔 Automation Test

👤 Name: {name}

📝 Message:
{message}

🔗 Profile:
{profile_link}

🔗 Post:
{post_link}
"""

requests.post(
DISCORD_WEBHOOK_URL,
json={"content": discord_message}
)

# -----------------------------

# Save to Google Sheets

# -----------------------------

sheet.append_row([
date,
name,
profile_link,
message,
post_link
])

print("Success! Message sent to Discord and Google Sheets.")
