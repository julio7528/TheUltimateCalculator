IF OBJECT_ID('LogCalculations', 'U') IS NULL
BEGIN
    CREATE TABLE LogCalculations (
        id INT IDENTITY(1,1) NOT NULL,
        [date] DATETIME NOT NULL,
        n1 FLOAT NOT NULL,
        n2 FLOAT NOT NULL,
        result FLOAT NOT NULL,
        [comment] VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    );
END;