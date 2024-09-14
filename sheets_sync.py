from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load your service account credentials
creds = service_account.Credentials.from_service_account_file('credentials.json')

# Initialize the Sheets API
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Example: Reading data from the sheet
SPREADSHEET_ID = '1oFDdIz-zg1gZ5tGVO3Mesjqn39nT_ouWiYf4l_toqCI'  # Replace with your Google Sheet ID
RANGE_NAME = 'Sheet1!A1:C10'  # Adjust the range as needed

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Data from the sheet:')
    for row in values:
        print(row)
