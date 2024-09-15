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

# Delete data in Google Sheets (clear cell values)
def delete_in_sheets(range_name):
    body = {
        'values': [[''] * 5]  # Adjust the number of columns as needed
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

# Delete data in Database
def delete_in_database(id):
    database.delete_data(id)
