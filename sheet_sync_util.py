
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the Google Sheets API scope
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Get credentials from service account JSON
def get_gsheet_client():
    creds_path = os.environ.get("GOOGLE_SHEET_CREDS_JSON")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, SCOPE)
    return gspread.authorize(creds)

# Append a new row to the spreadsheet
def append_lead_to_sheet(name, email, business, description, package, style):
    try:
        client = get_gsheet_client()
        sheet = client.open("90ProofStudios_Leads").sheet1

        sheet.append_row([name, email, business, description, package, style])
        print("🟢 Lead synced to Google Sheet.")
    except Exception as e:
        print(f"❌ Error syncing to Google Sheet: {e}")
