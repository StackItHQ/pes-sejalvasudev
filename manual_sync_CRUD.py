import create
import read
import update
import delete

def manual_sync():
    # Create data in Sheets and Database
    create.create_in_sheets([['Alice', 25, 'University X', 'CS']])
    create.create_in_database([('Alice', 25, 'University X', 'CS')])
    
    # Read data from Sheets and Database
    sheet_data = read.read_from_sheets()
    db_data = read.read_from_database()
    print(f"Sheet Data: {sheet_data}")
    print(f"DB Data: {db_data}")
    
    # Update data in Sheets and Database (Example: Update first row with new data)
    update.update_in_sheets('Sheet1!A1:E1', [['Alice', 26, 'University Y', 'Physics']])
    update.update_in_database(1, ['Alice', 26, 'University Y', 'Physics'])
    
    # Delete data from Sheets and Database (Example: Delete first row)
    delete.delete_in_sheets('Sheet1!A1:E1')
    delete.delete_in_database(1)

if __name__ == '__main__':
    manual_sync()
