/*Creating a Table if not exists for SQL Server Database*/
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'ChatGPTDatabaseApi')
    CREATE TABLE dbo.ChatGPTDatabaseApi 
        (
            id INT IDENTITY(1,1) NOT NULL,
            Api_Key nvarchar(250),
            PRIMARY KEY (id)
        );