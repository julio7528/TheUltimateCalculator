/*Creating a Table if not exists for SQL Server Database*/
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'TwitterDatabaseApi')
    CREATE TABLE dbo.TwitterDatabaseApi 
        (
            id INT IDENTITY(1,1) NOT NULL,
            Api_Key nvarchar(250),
            Api_Secret_Key nvarchar(250),
            Bearer_Token nvarchar(250),
            Access_Token nvarchar(250),
            Access_Token_Secret nvarchar(250),
            Client_Id nvarchar(250),
            Client_Secret nvarchar(250)
            PRIMARY KEY (id)
        );