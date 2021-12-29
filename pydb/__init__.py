import pyodbc

class DBBroker:

    def __init__(self, dbb_path, driver = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};") -> None:
        self.path = dbb_path
        self.__init_connection__(driver + r"Dbq=" + self.path + r";")

    def __init_connection__(self, connection_string) -> None:
        conn = pyodbc.connect(connection_string)
        self.cursor = conn.cursor()

    def Read(self, sql):
        return self.cursor.execute(sql)

    def Insert(self, sql):
        _ = self.cursor.execute(sql).rowcount
        self.cursor.commit()
        return _

    def Delete(self, sql):
        _ = self.cursor.execute(sql).rowcount
        self.cursor.commit()
        return _

    def Update(self, sql):
        _ = self.cursor.execute(sql).rowcount
        self.cursor.commit()
        return _
