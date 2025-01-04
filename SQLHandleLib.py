import sqlite3

class SQL_Lib:
    #Connect the SQL
    def Open_DB(self,Par_DBName):
        return sqlite3.connect(Par_DBName)

    #Disconnect the SQL
    def Close_DB(self,Par_DBHandle):
        return Par_DBHandle.close()

    #Get all table names in the SQL
    def Get_Table_Name(self, Par_DBHandle):
        cursor = Par_DBHandle.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        Table = cursor.fetchall()
        cursor.close()
        return Table

    #Get all contents in the table
    def Get_Table_Content(self,Par_DBHandle,Par_TableName):
        cursor = Par_DBHandle.execute(f"SELECT * FROM {Par_TableName}")
        rows = cursor.fetchall()
        cursor.close()
        return rows
