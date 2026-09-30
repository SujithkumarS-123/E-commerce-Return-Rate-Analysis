-- ============================================================
-- PROJECT: E-COMMERCE RETURN RATE REDUCTION ANALYSIS
-- DATABASE: ecommerce_returns
-- TABLE: returns_sustainability_dataset
-- TOOL: MySQL
--
-- TASK 1: Data Understanding & Overall Return Analysis
-- TASK 2: Return Pattern & Customer Analysis
-- TASK 3: Business Impact & Sustainability Analysis
-- ============================================================


USE ecommerce_returns;


-- ============================================================
-- TASK 1: DATA UNDERSTANDING & OVERALL RETURN ANALYSIS
-- ============================================================


-- 1.1 Display sample records

SELECT *
FROM returns_sustainability_dataset
LIMIT 10;


-- 1.2 Check total number of records

SELECT COUNT(*) AS total_records
FROM returns_sustainability_dataset;


-- 1.3 Check table structure

DESCRIBE returns_sustainability_dataset;


-- 1.4 Check return status distribution

SELECT
    Return_Status,
    COUNT(*) AS total_orders
FROM returns_sustainability_dataset
GROUP BY Return_Status
ORDER BY total_orders DESC;


-- 1.5 Calculate overall return rate

SELECT
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset;


-- ============================================================
-- TASK 2: RETURN PATTERN & CUSTOMER ANALYSIS
-- ============================================================


-- 2.1 Return rate by product category

SELECT
    Product_Category,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Product_Category

ORDER BY return_rate_percentage DESC;


-- 2.2 Return rate by user location

SELECT
    User_Location,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY User_Location

ORDER BY return_rate_percentage DESC;


-- 2.3 Return reasons

SELECT
    Return_Reason,
    COUNT(*) AS return_count

FROM returns_sustainability_dataset

WHERE Return_Status = 'Returned'

GROUP BY Return_Reason

ORDER BY return_count DESC;


-- 2.4 Return reasons as percentage of total returns

SELECT
    Return_Reason,

    COUNT(*) AS returned_orders,

    ROUND(
        COUNT(*) * 100.0 /
        (
            SELECT COUNT(*)
            FROM returns_sustainability_dataset
            WHERE Return_Status = 'Returned'
        ),
        2
    ) AS percentage_of_returns

FROM returns_sustainability_dataset

WHERE Return_Status = 'Returned'

GROUP BY Return_Reason

ORDER BY returned_orders DESC;


-- 2.5 Return rate by shipping method

SELECT
    Shipping_Method,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Shipping_Method

ORDER BY return_rate_percentage DESC;


-- 2.6 Return rate by payment method

SELECT
    Payment_Method,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Payment_Method

ORDER BY return_rate_percentage DESC;


-- 2.7 Return rate by gender

SELECT
    User_Gender,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY User_Gender

ORDER BY return_rate_percentage DESC;


-- 2.8 Return rate by existing age group

SELECT
    Age_Group,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Age_Group

ORDER BY return_rate_percentage DESC;


-- 2.9 Return rate by existing price group

SELECT
    Price_Group,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Price_Group

ORDER BY return_rate_percentage DESC;


-- 2.10 Return rate by existing order value group

SELECT
    Order_Value_Group,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY Order_Value_Group

ORDER BY return_rate_percentage DESC;


-- 2.11 Return rate by high-discount status

SELECT
    High_Discount,
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS return_rate_percentage

FROM returns_sustainability_dataset

GROUP BY High_Discount

ORDER BY return_rate_percentage DESC;


-- ============================================================
-- TASK 3: BUSINESS IMPACT & SUSTAINABILITY ANALYSIS
-- ============================================================


-- 3.1 Return cost by return status

SELECT
    Return_Status,
    COUNT(*) AS total_orders,
    ROUND(SUM(Return_Cost), 2) AS total_return_cost,
    ROUND(AVG(Return_Cost), 2) AS average_return_cost

FROM returns_sustainability_dataset

GROUP BY Return_Status;


-- 3.2 Profit/Loss by return status

SELECT
    Return_Status,
    COUNT(*) AS total_orders,
    ROUND(SUM(Profit_Loss), 2) AS total_profit_loss,
    ROUND(AVG(Profit_Loss), 2) AS average_profit_loss

FROM returns_sustainability_dataset

GROUP BY Return_Status;


-- 3.3 CO2 emissions and packaging waste by return status

SELECT
    Return_Status,
    COUNT(*) AS total_orders,

    ROUND(AVG(CO2_Emissions), 2) AS avg_co2_emissions,

    ROUND(AVG(Packaging_Waste), 2) AS avg_packaging_waste,

    ROUND(AVG(CO2_Saved), 2) AS avg_co2_saved,

    ROUND(AVG(Waste_Avoided), 2) AS avg_waste_avoided

FROM returns_sustainability_dataset

GROUP BY Return_Status;


-- 3.4 Final overall business summary

SELECT
    COUNT(*) AS total_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Returned' THEN 1
            ELSE 0
        END
    ) AS returned_orders,

    SUM(
        CASE
            WHEN Return_Status = 'Not Returned' THEN 1
            ELSE 0
        END
    ) AS not_returned_orders,

    ROUND(
        SUM(
            CASE
                WHEN Return_Status = 'Returned' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS overall_return_rate,

    ROUND(SUM(Return_Cost), 2) AS total_return_cost,

    ROUND(SUM(Profit_Loss), 2) AS total_profit_loss

FROM returns_sustainability_dataset;


-- ============================================================
-- END OF SQL ANALYSIS
-- ============================================================
