import pandas as pd
import pyodbc
from Products.Five.browser import BrowserView

class SQLView(BrowserView):
    """ The default view for talks"""

    def head(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server=10.1.10.49\ITEVA;'
                              'Database=NALR060111;'
                              'Port=15555;'
                              'UID=sa;'
                              'PWD=Thermo-123;')

        cursor = conn.cursor()

        sql = pd.read_sql_query('SELECT top 500 * FROM ElementLines order by 1 desc',conn)
        headers = []
        for i in sql.columns:
            headers.append(i)
        # html = sql_query.to_html()
        return headers

    def body(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                              'Server=10.1.10.49\ITEVA;'
                              'Database=NALR060111;'
                              'Port=15555;'
                              'UID=sa;'
                              'PWD=Thermo-123;')

        cursor = conn.cursor()

        sql = pd.read_sql_query('SELECT top 500 * FROM ElementLines order by 1 desc',conn)
        body = []
        for i, row in sql.iterrows():
            body.append(row)
        # html = sql_query.to_html()
        return body
