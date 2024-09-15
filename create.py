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
CRUD_RANGE_NAME = 'Sheet1!A1:E'

# Create data in Google Sheets
def create_in_sheets(values):
    body = {
        'values': values
    }
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=CRUD_RANGE_NAME,
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()

# Create data in Database
def create_in_database(values):
    database.create_data(values)
