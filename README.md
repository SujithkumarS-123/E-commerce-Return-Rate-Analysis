# E-commerce Return Rate Reduction Analysis

## Project Overview

This project analyzes e-commerce product returns to identify the major factors affecting return rates and understand the reasons behind customer returns.

The project combines **SQL, Python, Machine Learning, and Power BI** to perform data analysis, identify return patterns, predict high-risk return orders, and present the findings through an interactive dashboard.

## Objectives

* Analyze the overall e-commerce return rate
* Identify product categories with high return rates
* Analyze return patterns by location, gender, age, shipping method, and payment method
* Analyze the impact of discounts, product price, and order value on returns
* Identify major return reasons
* Analyze the business impact of product returns
* Predict high-risk return orders using Machine Learning
* Create an interactive Power BI dashboard
* Generate a list of high-risk products

## Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **SQL / MySQL**
* **Power BI**
* **Excel / CSV**
* **Logistic Regression**

## Dataset

The dataset contains **5,000 e-commerce order records** with information about:

* Order details
* Product details
* Customer information
* Product category
* Product price
* Order quantity
* Discount
* Shipping method
* Payment method
* Location
* Return status
* Return reason
* Return cost
* Profit/Loss
* Sustainability metrics

## Key Analysis

The project analyzes:

* Return Rate
* Return Cost
* Return Reasons
* Product Category
* Product Price
* Discount
* Order Quantity
* Order Value
* Customer Age
* Customer Gender
* Location
* Shipping Method
* Payment Method
* Profit/Loss
* CO₂ Emissions
* Packaging Waste

## SQL Analysis

SQL was used to perform:

* Data validation and exploration
* Overall return-rate calculation
* Return-rate analysis by product category
* Location-wise return analysis
* Return-reason analysis
* Shipping and payment method analysis
* Gender and age-group analysis
* Price-group and order-value analysis
* Discount analysis
* Return-cost and profit/loss analysis
* Sustainability analysis

SQL file:

`SQL/ecommerce_return_analysis.sql`

## Python & Machine Learning

Python was used for data analysis, exploratory data analysis, feature preparation, and Machine Learning.

A **Logistic Regression** model was used to predict the likelihood of product returns.

### Model Features

* Product Price
* Order Quantity
* Discount Applied
* User Age
* Order Value
* Order Year
* Order Month

### Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

The Python notebook is available in:

`Python/ecommerce_return_analysis.ipynb`

## Power BI Dashboard

An interactive Power BI dashboard was created to visualize return patterns, costs, product risks, and other important business metrics.

### Page 1 – Return Overview

![Power BI Dashboard Page 1](PowerBI/Page_1_Return_Overview.png)

### Page 2 – Return Risk & Business Analysis

![Power BI Dashboard Page 2](PowerBI/Page_2_Return_Risk_Analysis.png)

Power BI file:

`PowerBI/Ecommerce_Return_Rate_Analysis.pbix`

## Key Findings

* Total orders analyzed: **5,000**
* Returned orders: **1,450**
* Not returned orders: **3,550**
* Overall return rate: **29%**
* **Clothing** recorded the highest return rate among the major product categories analyzed.
* Return rates varied across customer locations.
* Discount levels showed differences in return rates.
* Return reasons such as defective products, changed mind, wrong item, and size-related issues were analyzed.
* Return status was also analyzed in relation to return cost, profit/loss, and sustainability metrics.

## Project Outputs

The project includes:

* Interactive Power BI Dashboard
* Power BI `.pbix` file
* SQL Analysis `.sql` file
* Python `.ipynb` notebook
* High-Risk Products CSV
* Power BI dashboard screenshots

## Project Structure

```text
E-commerce Return Rate Reduction Analysis/
│
├── README.md
│
├── SQL/
│   └── ecommerce_return_analysis.sql
│
├── Python/
│   └── ecommerce_return_analysis.ipynb
│
├──  Ecommerce_Return_Rate_Analysis.pbix
│──  Page_1_Return_Overview.png
│──  Page_2_Return_Risk_Analysis.png
│
└── Dataset/
    ├── ecommerce_return_powerbi.csv
    └── high_risk_products.csv
```

## Conclusion

This project provides a data-driven analysis of e-commerce product returns. By combining SQL analysis, Python-based Machine Learning, and Power BI visualization, the project identifies important return patterns and high-risk orders.

The insights can help businesses understand return behavior, monitor return costs, identify potential high-risk products, and support strategies for reducing product returns.
