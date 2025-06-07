import os
import gspread
import json
from google.oauth2.service_account import Credentials

# Define the scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_gsheet_client():
    try:
        json_path = os.environ.get("GOOGLE_SHEET_CREDS_JSON")
        if not json_path:
            raise Exception("GOOGLE_SHEET_CREDS_JSON is not set or is empty")

        with open(json_path) as f:
            service_account_info = json.load(f)

        creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPE)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        print(f"❌ Failed to authorize Google Sheets client: {e}")
        raise

def append_lead_to_sheet(name, email, business, description, package, style, prompt):
    try:
        client = get_gsheet_client()
        sheet = client.open("90ProofStudios_Leads").sheet1

        # Append all lead details plus the generated image prompt
        sheet.append_row([name, email, business, package, style, description, prompt])
        print("🟢 Lead and prompt synced to Google Sheet.")
    except Exception as e:
        print(f"❌ Error syncing to Google Sheet: {e}")
