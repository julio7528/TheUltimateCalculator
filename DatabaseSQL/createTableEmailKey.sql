IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'vaultGmail')
    CREATE TABLE dbo.vaultGmail 
        (
            id INT IDENTITY(1,1) NOT NULL,
            waKey nvarchar(250),
            waUser nvarchar(250)
            PRIMARY KEY (id)
        );
