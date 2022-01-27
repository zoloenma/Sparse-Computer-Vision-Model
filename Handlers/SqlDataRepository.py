import textwrap
import datetime
import pyodbc as pyo
from Core.DataRepository import DataRepository

class SqlDataRepository(DataRepository):
    def SavePeopleCount(self, peopleCount: int):
        # ============================== CONNECTION STRING SECTION ==============================

        # Specify the driver
        driver = '{ODBC Driver 17 for SQL Server}'

        # Specify the Server Name and Database Name
        server_name = 'sparseserver'
        database_name = 'sparse'

        # Create Server
        server = f'{server_name}.database.windows.net,1433;'

        # Define Username & Password
        username = 'cliradmin'
        password = 'Admin@123'

        # Create Connection String
        connection_string = textwrap.dedent(f''' 
            Driver={driver};
            Server={server};
            Database={database_name};
            Uid={username};
            Pwd={password};
            Encrypt=yes;
            TrustServerCertificate=no;
            Connection Timeout=30;
        ''')

        # ============================== CONNECTING TO THE DATABASE AND EXECUTING QUERIES ==============================

        # Open Connection
        cnxn: pyo.Connection = pyo.connect(connection_string)
        crsr: pyo.Cursor = cnxn.cursor()

        # List of Queries
        select_query = 'SELECT * FROM RoomOccupancy'
        insert_query = 'INSERT INTO [RoomOccupancy] ([Room Occupancy], [Timestamp]) VALUES (?, ?)'

        # NOTE: The format for INSERT query is shown above The two (2) question marks are considered placeholders.
        #       In order to insert the values needed, the 'records' variable is created below. 
        records = [
            (peopleCount, datetime.datetime.now()),
        ]

        # Execute INSERT Query
        # NOTE: When executing INSERT query, commit() must be used in order for the insertion to work
        crsr.executemany(insert_query, records)
        crsr.commit()

        # Execute SELECT Query
        crsr.execute(select_query)

        # Gets the data from the current cursor
        print(crsr.fetchall())

        # Close Connection
        cnxn.close()