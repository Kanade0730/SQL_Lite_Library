import sqlite3

class SQL_Lib:
    #Connect the SQL
    def Open_DB(self, Str_DBName):
        return sqlite3.connect(Str_DBName)

    #Disconnect the SQL
    def Close_DB(self,DBHandle):
        return DBHandle.close()

    #Get all table names in the SQL
    def Get_Table_Name(self, DBHandle):
        cursor = DBHandle.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        Table = cursor.fetchall()
        cursor.close()
        return Table
    #Get column name
    def Get_Column_Name(self,DBHandle,Str_TableName):
        cursor = DBHandle.execute(f"PRAGMA table_info({Str_TableName})")
        column_names = [column[1] for column in cursor.fetchall()]
        cursor.close()
        return column_names

    #Get all contents in the table
    def Get_Table_Data(self,DBHandle,Str_TableName):
        cursor = DBHandle.execute(f"SELECT * FROM {Str_TableName}")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def Creat_Table(self,DBHandle,Str_TableName):
        cursor = DBHandle.execute(f"CREATE TABLE IF NOT EXISTS {Str_TableName}(ID INTEGER PRIMARY KEY AUTOINCREMENT)")
        cursor.close()

    def Creat_Column_Not_NULL(self,DBHandle,Str_Table_Name,Str_ColumnName):
        cursor = DBHandle.execute(f"ALTER TABLE {Str_Table_Name} ADD COLUMN {Str_ColumnName} TEXT NOT NULL")
        cursor.close()


