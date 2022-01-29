import textwrap
import datetime
import pyodbc as pyo
from Core.DataRepository import DataRepository

class SqlDataRepository(DataRepository):
    def __init__(self) -> None:
        super().__init__()
        
        # Driver
        driver = '{ODBC Driver 17 for SQL Server}'

        # Server Name and Database Name
        server_name = 'sparseserver'
        database_name = 'sparse'

        # Host
        server = f'{server_name}.database.windows.net,1433;'

        # Username & Password
        username = 'cliradmin'
        password = 'Admin@123'

        # Connection String
        self.connection_string = textwrap.dedent(f''' 
            Driver={driver};
            Server={server};
            Database={database_name};
            Uid={username};
            Pwd={password};
            Encrypt=yes;
            TrustServerCertificate=no;
            Connection Timeout=30;
        ''')


    def SavePeopleCount(self, peopleCount: int):
        with pyo.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            
            insert_query = 'INSERT INTO [RoomOccupancy] ([Room Occupancy], [Timestamp]) VALUES (?, ?)'
            records = [
                (peopleCount, datetime.datetime.now()),
            ]
            
            cursor.executemany(insert_query, records)
            cursor.commit()