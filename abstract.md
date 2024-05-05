# Inventory Optimization
Ref: [Original Design Doc](https://docs.google.com/document/d/18MHqb7a5KHHf6vB_BQLhsSnf34q80WtZfH57aItrs4Y/edit?pli=1)
## Requirements Analysis and Product Discovery
### Executive Summary
#### Purpose
The goal of this AI system is to provide an inventory optimization solution that addresses the key problem of inefficient inventory management. Its intended impact is to streamline operations, thereby helping businesses reduce excess costs and enhance customer satisfaction through reliable stock availability.
#### Business Objective
The primary goal of the AI system is to revolutionize inventory management by utilizing machine learning and generative AI technologies.
This system aims to enhance business operations by providing precise demand forecasting, optimizing inventory levels, and automating replenishment processes, thereby ensuring efficient stock management and improved customer satisfaction.
### Business View
#### Business Case
Excess inventory not only locks up valuable capital but also escalates storage costs, thereby straining financial liquidity. Deploying this AI system aligns with our strategic goals to streamline inventory management and enhance fiscal efficiency. By reducing excess inventory by 30%, the company is poised to significantly improve profit margins and operational efficiency. This initiative is underpinned by a thorough market analysis, indicating a strong demand for advanced inventory solutions, and a cost-benefit analysis confirms that the savings from reduced inventory levels will substantially outweigh the system implementation costs.

#### Stakeholder Analysis
The primary stakeholders for this project are inventory managers, financial officers, and logistics coordinators. Inventory managers will benefit from predictive insights that enable more accurate stock management. Financial officers will utilize the system's outputs to optimize budget allocations and reduce unnecessary expenditure on excess inventory. Logistics coordinators will leverage actionable recommendations to streamline supply chain processes, thereby enhancing overall operational efficiency. This system is designed to meet the specific needs of each stakeholder group, ensuring that their respective objectives are aligned and supported.

#### ROI and Success Metrics
The success of this project will be quantitatively measured through several key performance indicators: a reduction in overstock levels, decreased storage and handling costs, and an improvement in the inventory turnover ratio. 

The return on investment will be evaluated by the increased cash flow and reduction in operational expenses. Additional metrics such as customer satisfaction due to better product availability and the rate of inventory obsolescence reduction will also be considered to assess the overall impact and effectiveness of the implemented system.

### Project Overview
#### Scope
The project is focused on the development and implementation of predictive models specifically tailored for demand forecasting. This includes the collection and preprocessing of relevant data, model training, testing, and deployment. The project will also involve the integration of these models into the existing inventory management system to enhance decision-making processes. Out of Scope: This project will not cover the redevelopment of the entire inventory management system, nor will it address changes in supply chain logistics unrelated to demand forecasting.

#### Timeline
**For Real-time:**
* Month 1-2: Data collection and preprocessing.
* Month 3-4: Model development and initial testing.
* Month 5: Integration with existing systems and pilot testing.
* Month 6: Full deployment and final adjustments based on feedback.
* Month 7: Project review and closure.

**For the scope of this project:**
* Week 1-2: Data collection and preprocessing.
* Week 3: Model development and initial testing.
* Week 4: Integration with existing systems and pilot testing.
* Week 5: Full deployment and final adjustments based on feedback.
* Week 6: Project review and closure.

#### Constraints and Assumptions
**Constraints**
* Technical: Requires integration with existing inventory management systems without disrupting ongoing operations.
* Financial: Budget limitations may restrict the scope of advanced analytics tools and technologies available.
* Operational: The project must be completed within a six-month window to align with financial planning cycles.

**Assumptions**
* Sufficient historical sales and inventory data is available and accessible for model training.
* The existing IT infrastructure is adequate to support the deployment of new AI models without significant upgrades.
* The staff will be available and capable of managing the transition to the new system.

### System Scope and Requirements 
#### Integration Requirements
The AI system will be designed to seamlessly integrate with existing business systems and workflows, particularly the enterprise resource planning (ERP) and supply chain management (SCM) systems. Integration will involve:
* Establishing data pipelines for real-time data exchange between the AI system and existing databases to ensure that inventory forecasts are based on the latest data.
* Configuring APIs to enable communication between the AI system and other business applications to facilitate automated actions based on predictive insights, such as replenishment orders and inventory adjustments.
* Ensuring compatibility with current hardware and software platforms to avoid disruptions in current operations.
* Implementing security protocols to safeguard data integrity and confidentiality during data exchanges.

#### User Roles and Permissions
User roles within the AI system will be clearly defined to maintain data security and ensure functional usability:
* Managers: Will have access to comprehensive dashboards that provide an overview of inventory metrics, predictive insights, and performance indicators. This access allows managers to make informed strategic decisions and monitor overall system effectiveness.
* Operational Staff: Will receive alerts and reports that are directly relevant to their specific workflows. This targeted information helps in managing day-to-day operations more effectively and responding swiftly to any inventory-related issues.
* IT Support Staff: Will have permissions to manage system settings, update configurations, and perform system maintenance to ensure operational continuity and address any technical issues.

These roles and permissions are structured to maintain an efficient workflow while protecting sensitive data and providing all stakeholders with the tools they need to perform their roles effectively.

### Risk Management
#### Business Risks
The risks associated with the deployment of the AI system extend beyond technical challenges to include:
* Market Changes: The volatility in market demand can affect the accuracy of demand forecasts produced by the AI system, leading to inventory discrepancies.
* Regulatory Developments: Changes in data protection regulations could impact the way data is handled and processed within the system, requiring updates to compliance protocols.
* Stakeholder Acceptance: Resistance from employees and management due to unfamiliarity with AI technology or concerns over job displacement could hinder system integration and effectiveness.

#### Risk Response Planning
To address these risks, the project will implement several strategic measures:
* For Market Changes: Regular updates and recalibrations of predictive models will be scheduled to align with shifting market trends and maintain forecasting accuracy.
* For Regulatory Developments: A compliance officer will be appointed to monitor regulatory changes and ensure that the AI system adheres to all legal requirements. The system design will incorporate flexible data management capabilities to quickly adapt to new regulations.
* For Stakeholder Acceptance: A comprehensive change management strategy will be executed, which includes training programs to educate all users on the benefits and operations of the AI system, and internal marketing to address concerns and highlight the positive impacts on workflow and job quality.
* Technical and Data Security: The project will include a detailed testing phase to validate the reliability and accuracy of predictive models. Robust data security protocols will be implemented to safeguard sensitive information, addressing potential data privacy issues.

These planned responses aim to ensure the project’s continuity and resilience by effectively managing both technical and business risks, thereby supporting successful integration and operational stability of the AI system.

### Product View
This product perspective given below outlines the roles, features, benefits, and pain points addressed by the AI system, demonstrating how it serves as a comprehensive solution to key inventory management challenges.
#### Features
* AI-driven Demand Forecasting Tools: Utilizes advanced machine learning algorithms to predict future demand based on historical data, trends, and external factors.
* Real-Time Inventory Tracking: Monitors inventory levels continuously to provide up-to-the-minute accuracy.
* Automated Recommendations for Inventory Adjustment: Generates suggestions for inventory replenishment or reduction based on current demand forecasts and stock levels.
#### Benefits
* Reduced Inventory Carrying Costs: Optimizes inventory levels to decrease the capital tied up in excess stock.
* Minimized Risk of Overstock and Stockouts: Ensures optimal stock levels are maintained, reducing the instances of unsold goods and missed sales.
* Enhanced Ability to Respond to Market Changes Swiftly: Provides agility in operations, allowing businesses to quickly adapt to market dynamics and consumer demands.
#### Pain Points Addressed:
* Inefficiency of Manual Inventory Predictions: Replaces guesswork and manual processes with precise, data-driven forecasting.
* Frequent Overstock Scenarios: Reduces financial losses by preventing situations where excess stock accumulates.
* Financial Drain Associated with Excess Inventory Storage and Markdowns: Lowers costs related to storing surplus items and discounts needed to move outdated stock.

## User Stories for Inventory Optimization
Below are the user stories that reflect the specific goals and functionalities needed from the inventory optimization system:
### User Story 1:
**Title:** Dynamic Inventory Adjustment Based on Sales Forecast

As an inventory manager,
I want the system to automatically adjust inventory orders,
So that inventory levels are optimized weekly based on real-time sales forecasting and external market trends.

#### Acceptance Criteria:
* Given the latest sales forecast and supplier lead times
* When the inventory optimization model runs,
* Then it should adjust the order quantities to ensure optimal stock levels are maintained,
* And notify the manager if adjustments exceed predefined thresholds.
* The system should also factor in upcoming promotions and seasonal demand changes when making adjustments.

#### Notes
* Assumes access to up-to-date sales data and accurate supplier lead times.
* Dependency on the sales forecasting system for real-time data.
* No specific UI/UX requirements mentioned; system notifications may require basic UI elements for alert display.

**Priority:** High
**Estimation:** 8 story points

#### Definition of Done
* All acceptance criteria are met.
* Code is reviewed and meets quality standards.
* All unit and acceptance tests are written and passed.
* Documentation is updated.

### User Story 2

**Title:** Inventory Analytics and Reporting

As a Finance Analyst,
I want to have access to comprehensive reports and analytics on the company's inventory performance,
So that I can track the financial impact of inventory management decisions.

#### Acceptance Criteria
* The system shall provide reports on key inventory metrics such as inventory turnover, days of supply, stockout rates, and inventory-related costs.
* The reports shall allow for filtering and segmentation by product, product category, warehouse, or other relevant dimensions.
* The system shall generate alerts and notifications for any inventory-related issues or KPI thresholds that are breached.
* Reports should be accessible in real-time with options to export data for offline analysis and presentations.

#### Notes
* Assumes integration with existing financial and inventory management systems for data accuracy.
* Dependency on real-time data availability and system performance for timely reporting.
* UI/UX requirements include a dashboard interface for interactive data exploration and report customization.

**Priority:** Medium
**Estimation:** 5 story points

#### Definition of Done
* All acceptance criteria are met.
* Code is reviewed and meets quality standards.
* All unit and acceptance tests are written and passed.
* Documentation is updated.

### User Story 3

**Title:** Demand Forecast Visualization
As a data analyst,
I want the system to visualize demand forecasts,
So that I can gain insights into future inventory needs and make informed decisions.

#### Acceptance Criteria
* Given access to the demand forecasting module,
* When generating demand forecasts for different product categories,
* Then the system should provide visualizations such as charts and graphs to represent forecasted demand trends.
* Given the demand forecast visualizations,
* When analyzing historical data alongside forecasts,
* Then the system should enable comparison and identification of demand patterns.

#### Notes
* Assumes availability of a robust data processing framework to support visualization capabilities.
* Dependency on the data quality and granularity provided by the demand forecasting module.
* UI/UX requirements include a sophisticated graphical interface for visualization tools.

**Priority:** Medium
**Estimation:** 6 story points

#### Definition of Done
* All acceptance criteria are met.
* Code is reviewed and meets quality standards.
* All unit and acceptance tests are written and passed.
* Documentation is updated.

## ATDD, BDD, TDD Development
**User Story: Dynamic Inventory Adjustment Based on Sales Forecast**

### Acceptance Test-Driven Development (ATDD) Scenario
**Scenario Title:** Ensuring Inventory Levels Meet Forecasted Demand
* And the forecast algorithm has been updated to the latest market trends,
* When the monthly inventory optimization process is triggered,
* Then the system should adjust inventory levels to match the forecasted demand for the next month,
* And notify the inventory manager if adjustments exceed predefined thresholds.

### Behavior-Driven Development (BDD) Scenario
* Given the system has current and accurate sales data,
* When a significant change in sales trends is detected,
* Then the system should automatically propose adjustments to inventory orders,
* And provide a detailed report to the inventory manager explaining the reason for adjustments.

### Test-Driven Development (TDD) Test Cases
#### Test Case: Validate forecast accuracy with historical data
* **Setup:** Load 6 months of sales data.
* **Action:** Run forecast model.
* **Assertion:** Forecast error margin is within acceptable limits (e.g., +/- 10%).

#### Test Case: Verify inventory adjustment notification
* **Setup:** Set inventory adjustments to exceed thresholds.
* **Action:** Trigger inventory optimization.
* **Assertion:** System sends a notification to the inventory manager.

## Synthetic Data Generation
* Utilize the current Kelly dataset and supplement it with synthetic data points.
* **Code Generation:** Develop AI models and algorithms to predict and manage inventory:
* **Model training:** Use historical sales data and synthetic test cases to train models.
* **Integration testing:** Ensure the system integrates seamlessly with existing ERP and supply chain management systems.
* **Validation:** Continuously test and refine the system using both synthetic and actual data, focusing on 
  - Accuracy of inventory forecasts
  - Effectiveness of automated inventory adjustments

## Implementation Process
### Step 1: Data Preprocessing
We'll begin by loading the dataset, performing initial cleaning, and checking for any missing values or outliers that need to be addressed.

Let's start by loading the dataset and taking a preliminary look at its structure and any potential issues it may have.

The dataset has been successfully loaded, and here's a summary of its characteristics:
* Total entries: 5000
* Columns: Store ID, Country, Product ID, Product Category, Units Sold, Date of Sale, GDP Growth Rate, Inflation Rate, Price Sold.
* The data types and range of values appear to be appropriate for each field.
* No immediate signs of missing values from the initial check.

#### Data Preprocessing Steps
* Convert 'Date of Sale' from string to date time format for better manipulation and time-series analysis.
* Check for outliers especially in 'Units Sold', 'Price Sold', 'GDP Growth Rate', and 'Inflation Rate' which could affect predictive modeling.
* Feature Engineering: We could derive additional features such as month, year, or quarter from 'Date of Sale' to analyze seasonal trends.

#### Let's execute these preprocessing steps
* Output image:The boxplots show the distribution of 'Units Sold' and 'Price Sold':
* Units Sold: The distribution appears fairly even without extreme outliers, which is good for modeling purposes.
* Price Sold: Similar to 'Units Sold', there are no significant outliers. The spread is consistent, indicating that price data is stable.

### Step 2: Exploratory Data Analysis (EDA)
We will now perform EDA to uncover trends, patterns, and anomalies in the dataset. This involves analyzing sales trends over time, relationships between variables, and how external economic factors (like GDP growth rate and inflation) influence sales. This insight will guide the development of predictive models for inventory optimization.

#### Let’s proceed with the EDA
The Exploratory Data Analysis (EDA) provides the following insights:
* Total Units Sold Over Time: The trend indicates seasonality in sales, which is crucial for forecasting inventory needs.
* Units Sold vs. GDP Growth Rate: There seems to be a weak correlation, suggesting that higher GDP growth might not directly lead to higher sales across all scenarios.
* Units Sold vs. Inflation Rate: Similarly, inflation doesn't show a strong direct correlation with units sold. However, certain patterns could be further explored with more detailed analysis.
* Units Sold by Product Category: Sales vary significantly between different product categories, indicating the need for category-specific inventory strategies.

### Step 3: Developing Predictive Models
With the insights from EDA, we can proceed to develop predictive models. These models will predict inventory needs based on sales trends, economic indicators, and product categories.
#### Model Considerations
* Time Series Forecasting: For overall and category-specific sales predictions.
* Regression Models: To understand the impact of economic indicators on sales.

#### Machine Learning Models
Advanced models like Random Forest or Gradient Boosting could be used to incorporate multiple features effectively.

Let’s start with setting up a simple time series forecast model to predict future sales based on historical data. We'll also prepare models to explore the impact of GDP and inflation on sales predictions. ​​

#### Output image
The decomposition of the time series data reveals the following components:
* **Trend:** There is a noticeable trend component in the sales data, which could be either increasing or decreasing over time. This is critical for understanding long-term changes in demand.
* **Seasonality:** Clear seasonal patterns suggest that sales fluctuate during specific times of the year. This cyclical behavior is essential for planning inventory levels seasonally.
* **Residuals:** The residuals show the randomness or noise in the data after accounting for trend and seasonality, indicating any anomalies or irregular patterns.
* **Developing Predictive Models:** Given the observed trend and seasonality, a forecasting model such as SARIMA (Seasonal ARIMA) can be particularly useful. This model will allow us to incorporate both non-seasonal and seasonal factors into our predictions.

#### Steps to build the SARIMA model:
* **Parameter Selection:** Use grid search to find the optimal parameters for the SARIMA model based on AIC/BIC criteria.
* **Model Fitting:** Fit the SARIMA model to historical sales data.
* **Validation:** Split the data into training and test sets to validate the model's forecasting accuracy.
* **Forecasting:** Use the model to forecast future sales, which will guide inventory decisions.

Let's set up and train a simple SARIMA model to start making forecasts. ​​

The SARIMA model has been successfully fitted to the time series data of units sold. Here's a summary of the model's performance:
* **Parameters:** The coefficients for the model indicate the relationships in the data. For example, the MA part has a significant coefficient, suggesting that the moving average component is influential in the model.

AIC and BIC: The Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) values are used to compare models; lower values generally indicate a better model fit with fewer extraneous parameters.

* **Diagnostic Statistics:** The Ljung-Box test and other statistics provide information about the residuals of the model, suggesting whether the model fit is adequate.

* **Forecasting Future Sales:**
Now, let’s use the model to forecast future sales, which will be crucial for planning inventory levels. We will forecast sales for the next 12 months and plot these predictions to visualize the forecast against the historical data.
Utilizing Forecasts for Inventory Optimization

* **Demand Forecasting:**
Use the SARIMA model's forecasts to estimate future demand for each product category at each store location.

Analyze forecast confidence intervals to understand potential demand volatility.

### Step 4: Testing and Validation
* **System Testing:** Run simulations using historical sales data to test the system's responsiveness to past demand fluctuations.
* **Steps to Implement and Utilize the SARIMA Model:**
 - **Model Setup:** Since we've already determined the parameters for the SARIMA model and have initial forecasts, we'll formalize this into a systematic forecasting process.
 - **Model Validation:** Before fully integrating the model into the inventory management system, it's crucial to validate it with historical data to assess its accuracy and reliability.
 - **Forecast Generation:** Use the SARIMA model to generate sales forecasts for the upcoming periods. This will serve as the basis for setting inventory levels.
* **Monitoring and Adjustment:** Establish a monitoring system to regularly assess the performance of the forecasting model and make necessary adjustments to the model parameters based on observed sales trends and forecast errors.

### Here's how we'll do it:
1. Split the historical sales data into training and testing sets.
2. Use the training set to fit the model.
3. Predict sales on the testing set.
4. Compare the predicted sales to the actual sales in the testing set to evaluate the model's performance.

```python
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from google.colab import files
import io

# Step 1: Upload the CSV file
uploaded = files.upload()

# Step 2: Load the dataset
data = pd.read_csv(io.BytesIO(uploaded['Dataset.csv']))

# Step 3: Prepare the data
# Convert 'Date of Sale' to datetime and set it as the index
data['Date of Sale'] = pd.to_datetime(data['Date of Sale'])
data.set_index('Date of Sale', inplace=True)

# Prepare time series data from 'Units Sold' column
time_series_data = data['Units Sold']

# Step 4: Prepare data for SARIMA modeling
# Use 80% of data for training, 20% for testing
split_point = int(len(time_series_data) * 0.8)
train_data, test_data = time_series_data[:split_point], time_series_data[split_point:]

# Step 5: Fit SARIMA model on training data
sarima_model_train = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                             enforce_stationarity=False, enforce_invertibility=False)
sarima_results_train = sarima_model_train.fit(disp=False)

# Step 6: Predict on test data
sarima_predictions = sarima_results_train.get_forecast(steps=len(test_data))
predicted_means = sarima_predictions.predicted_mean

# Step 7: Calculate RMSE for the predictions
rmse = np.sqrt(mean_squared_error(test_data, predicted_means))

# Step 8: Plot the actual vs predicted values for visualization
plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data, label='Train Data')
plt.plot(test_data.index, test_data, label='Actual Test Data')
plt.plot(test_data.index, predicted_means, label='Predicted Test Data', color='red')
plt.fill_between(predicted_means.index, sarima_predictions.conf_int().iloc[:, 0],
                 sarima_predictions.conf_int().iloc[:, 1], color='pink', alpha=0.3)
plt.title('SARIMA Forecast vs Actuals')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.legend()
plt.show()

# Step 9: Output RMSE
print("RMSE:", rmse)


Output: 
RMSE: 2.909572558234653
```
