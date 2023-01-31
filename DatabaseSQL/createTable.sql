IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'LogCalculations')
    CREATE TABLE LogCalculations (
        id INT IDENTITY(1,1) NOT NULL,
        [date] DATETIME NOT NULL,
        n1 FLOAT NOT NULL,
        n2 FLOAT NOT NULL,
        result FLOAT NOT NULL,
        [comment] VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    );