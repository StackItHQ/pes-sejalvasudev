from google.oauth2 import service_account
from googleapiclient.discovery import build
import database  # Import your database functions

# Load your service account credentials
creds = service_account.Credentials.from_service_account_file('credentials.json')

# Initialize the Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

SPREADSHEET_ID = '1oFDdIz-zg1gZ5tGVO3Mesjqn39nT_ouWiYf4l_toqCI'
CRUD_RANGE_NAME = 'Sheet1!A1:E'

def read_data(spreadsheet_id, range_name):
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

def write_data(spreadsheet_id, range_name, values):
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    return result


def sync_data():
    # Read data from Google Sheets
    sheet_data = read_data(SPREADSHEET_ID, CRUD_RANGE_NAME)

    # Create or update database records
    for row in sheet_data:
        if len(row) == 4:  # Assuming the sheet has 4 columns
            values = (row[0], int(row[1]), row[2], row[3])
            database.create_data([values])  # Adjust this based on your database function

    # Read data from database
    db_data = database.read_all_data()  # Adjust this based on your database function

    # Write data back to Google Sheets if needed
    write_data(SPREADSHEET_ID, CRUD_RANGE_NAME, db_data)

if __name__ == '__main__':
    sync_data()