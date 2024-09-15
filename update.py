from googleapiclient.discovery import build
import database  # Import database functions
from google.oauth2 import service_account

# Load your service account credentials
creds = service_account.Credentials.from_service_account_file('credentials.json')

# Initialize the Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Define your spreadsheet and range
SPREADSHEET_ID = '1oFDdIz-zg1gZ5tGVO3Mesjqn39nT_ouWiYf4l_toqCI'

# Update data in Google Sheets
def update_in_sheets(range_name, values):
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

# Update data in Database
def update_in_database(id, values):
    database.update_data(id, values)
