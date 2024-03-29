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


    def SavePeopleCount(self, roomOccupancy: float):
        with pyo.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            
            get_room_capacity_query = "SELECT [Capacity] From [EffectiveCapacity]"
            cursor.execute(get_room_capacity_query)
            effective_capacity = cursor.fetchone().Capacity

            room_occupancy_percentage = roomOccupancy / effective_capacity

            insert_query = 'INSERT INTO [RoomOccupancy] ([Room Occupancy], [Timestamp]) VALUES (?, ?)'
            records = [
                (room_occupancy_percentage, datetime.datetime.now()),
            ]
            
            cursor.executemany(insert_query, records)
            cursor.commit()
    