from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    def __init__(self, scopes, creds_JSON_path, sheetID):
        """
        This class is used to read and write to the spreadsheet

        Parameters
        ----------
        scopes : list
            All the scopes used when accessing the google drive API
            and the google sheets API.

        creds_JSON : str
            The path of the credentials JSON file.

        sheetID : str
            The name of the sheet that the program will read and write to.
        """
        self.scopes = scopes
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(creds_JSON_path, self.scopes)
        
        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open_by_key(sheetID)

    def read_worksheet(self, worksheet_number):
        """
        Returns a dictionary of all contents of the worksheet.
        This returns all the methods in alphabetical order of the columns.

        Examples
        --------
        For the examples "sheet" will represent an instance of Sheet.

        >>> from pprint import pprint
        >>> pprint(sheet.read_worksheet(0))
        [{'Five': 1, 'Four': 1, 'One': 1, 'Three': 1, 'Two': 1},
         {'Five': 2, 'Four': 2, 'One': 2, 'Three': 2, 'Two': 2},
         {'Five': 3, 'Four': 3, 'One': 3, 'Three': 3, 'Two': 3},
         {'Five': 4, 'Four': 4, 'One': 4, 'Three': 4, 'Two': 4},
         {'Five': 5, 'Four': 5, 'One': 5, 'Three': 5, 'Two': 5},
         {'Five': 6, 'Four': 6, 'One': 6, 'Three': 6, 'Two': 6}]

        Parameters
        ----------
        worksheet_number : int
            The worksheet that the program will read.

        Returns
        -------
        dict
            A dictionary of all contents in the given worksheet.

        str
            In the event that the sheet isn't found, this method will return a string saying "WorkSheet isn't found".
        """

        try:
            return self.sheet.get_worksheet(worksheet_number).get_all_records()

        except gspread.exceptions.WorksheetNotFound:
            return "WorkSheet isn't exist"


numberSheet = Sheet(['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive'],
                     'creds.json',
                     '1HJj_OZSDDCnppiqkLzdyKt2Nd62YKsqUNBQ_-igLV4M')

pprint(numberSheet.read_worksheet(0))