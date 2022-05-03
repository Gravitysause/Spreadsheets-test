from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    def __init__(self, scopes, creds_JSON, sheetID):
        self.scopes = scopes
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(creds_JSON, self.scopes)
        
        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open_by_key(sheetID)

    def read_worksheet(self, worksheet_number):
        try:
            return self.sheet.get_worksheet(worksheet_number).get_all_records()

        except gspread.exceptions.WorksheetNotFound:
            return "WorkSheet doesn't exist"


numberSheet = Sheet(['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive'],
                     'creds.json',
                     '1HJj_OZSDDCnppiqkLzdyKt2Nd62YKsqUNBQ_-igLV4M')

pprint(numberSheet.read_worksheet(0))