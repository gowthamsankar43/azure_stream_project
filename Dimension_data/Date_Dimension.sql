
-- Create the DateDimension table
CREATE TABLE DateDimension (
    DateKey INT PRIMARY KEY,
    Date DATE NOT NULL,
    Year INT NOT NULL,
    Quarter INT NOT NULL,
    Month INT NOT NULL,
    Day INT NOT NULL,
    Weekday INT NOT NULL,
    WeekOfYear INT NOT NULL,
    DayName VARCHAR(10) NOT NULL,
    IsHoliday BOOLEAN NOT NULL
);


CREATE INDEX idx_date ON DateDimension(Date);
CREATE INDEX idx_year_month ON DateDimension(Year, Month);
CREATE INDEX idx_weekofyear ON DateDimension(WeekOfYear);
CREATE INDEX idx_isholiday ON DateDimension(IsHoliday);



DELIMITER $$

CREATE PROCEDURE DATE_DIMENSION(In initial_date Date,In last_date Date,OUT OUTPUT CHAR(1))
BEGIN
    DECLARE StartDate DATE;
    DECLARE EndDate DATE;
    SET StartDate = initial_date;
    SET EndDate = last_date;

    WHILE StartDate <= EndDate DO
        INSERT INTO DateDimension (DateKey, Date, Year, Quarter, Month, Day, Weekday, WeekOfYear, DayName, IsHoliday)
        VALUES (
            DATE_FORMAT(StartDate, '%Y%m%d'),
            StartDate,
            YEAR(StartDate),
            QUARTER(StartDate),
            MONTH(StartDate),
            DAY(StartDate),
            DAYOFWEEK(StartDate),
            WEEK(StartDate),
            DAYNAME(StartDate),
            CASE
                WHEN DAYOFWEEK(StartDate) IN (1, 7) THEN TRUE
                ELSE FALSE
            END
        );

        SET StartDate = DATE_ADD(StartDate, INTERVAL 1 DAY);
    END WHILE;

    SET OUTPUT = 'S';
END $$

DELIMITER ;

CALL DATE_DIMENSION('2020-01-01','2024-12-31',@OUT);
SELECT @OUT;
