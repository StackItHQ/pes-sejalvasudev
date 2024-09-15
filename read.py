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

# Read data from Google Sheets
def read_from_sheets():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=CRUD_RANGE_NAME).execute()
    return result.get('values', [])

# Read data from Database
def read_from_database():
    return database.read_all_data()
