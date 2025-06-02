import os
import gspread
from google.oauth2.service_account import Credentials

# Define the scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_gsheet_client():
    creds_path = os.environ.get("GOOGLE_SHEET_CREDS_JSON")
    credentials = Credentials.from_service_account_file(creds_path, scopes=SCOPE)
    return gspread.authorize(credentials)

def append_lead_to_sheet(name, email, business, description, package, style):
    try:
        client = get_gsheet_client()
        sheet = client.open("90ProofStudios_Leads").sheet1
        sheet.append_row([name, email, business, package, style, description])
        print("🟢 Lead synced to Google Sheet.")
    except Exception as e:
        print(f"❌ Error syncing to Google Sheet: {e}")
