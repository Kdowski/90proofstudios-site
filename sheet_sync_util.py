import os
import gspread
from google.oauth2.service_account import Credentials

# Define the scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def append_lead_to_sheet(name, email, business, description, package, style, prompt):
    try:
        client = get_gsheet_client()
        sheet = client.open("90ProofStudios_Leads").sheet1

        # Append all lead details plus the generated image prompt
        sheet.append_row([name, email, business, package, style, description, prompt])
        print("🟢 Lead and prompt synced to Google Sheet.")
    except Exception as e:
        print(f"❌ Error syncing to Google Sheet: {e}")

def get_gsheet_client():
    creds_json = os.environ.get("GOOGLE_SHEET_CREDS_JSON")
    if not creds_json:
        raise Exception("Missing GOOGLE_SHEET_CREDS_JSON environment variable.")

    import json
    creds_dict = json.loads(creds_json)

    credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
    return gspread.authorize(credentials)

