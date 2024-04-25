# Inventory Optimization

## Step 1: Requirements Analysis and Product Discovery
We need to ensure that our AI-driven system can effectively manage and predict inventory needs based on dynamic market conditions. Here are key aspects to consider:

### Business Objectives:
* **Reduce excess inventory:** Minimize costs associated with overstocking.
* **Increase capital efficiency:** Optimize stock levels to ensure liquidity and reduce capital tied up in inventory.
* **Enhance customer satisfaction:** Ensure product availability aligns with customer demand to prevent stockouts.

### Integration Requirements:
* **Real-time data processing:** The system must integrate real-time sales data, supply chain logistics, and external market trends.
* **Cross-functional planning integration:** Connect with sales, finance, and operations plans to align inventory levels with broader business goals.

## Step 2: Creating User Stories
These user stories should reflect the specific goals and functionalities needed from the inventory optimization system:

### 1. Dynamic Inventory Adjustment Based on Sales Forecast
**As an inventory manager,**
* I want the system to automatically adjust inventory orders
* So that inventory levels are optimized weekly based on real-time sales forecasting and external market trends.
#### Acceptance Criteria:
* Given the latest sales forecast and supplier lead times,
* When the inventory optimization model runs,
* Then it should adjust the order quantities to ensure optimal stock levels are maintained.
* And notify the manager if adjustments exceed predefined thresholds.

### 2. View Demand Forecast Accuracy
**As a business analyst,**
* I want to view reports on the accuracy of demand forecasts,
* So that I can evaluate the performance of the forecasting model and make adjustments if necessary.
#### Acceptance Criteria:
* The system should generate reports on demand forecast accuracy for specified time periods.
* Reports should include metrics such as forecasted demand, actual demand, variance, and percentage accuracy.
* Users should be able to select different time periods (e.g., daily, weekly, monthly) for viewing accuracy reports.
* The accuracy calculation should consider both overestimations and underestimations.
* Reports should be accessible through a user-friendly interface, allowing easy navigation and filtering options.

### 3. Demand Forecast Visualization
**As a data analyst,**
* I want the system to visualize demand forecasts,
* So that I can gain insights into future inventory needs and make informed decisions.

### 4. Supplier Performance Tracking
As a procurement manager,
* I want the system to track supplier performance metrics,
* So that I can evaluate supplier reliability and make informed decisions regarding supplier partnerships.

### 5. Real-time Inventory Monitoring and Alerts
As an inventory manager,
* I want the system to provide real-time monitoring of inventory levels,
* So that I can receive immediate alerts for low stock or excess inventory situations.

## Step 3: ATDD, BDD, and TDD
Develop detailed test scenarios that will validate the functionality of the inventory optimization system.

### For [User Story 1](https://github.com/prakashvadrevu/oxford-ai-capstone-group-3/blob/main/abstract.md#1-dynamic-inventory-adjustment-based-on-sales-forecast)

#### Scenario: Ensuring Inventory Levels Meet Forecasted Demand
* Given that the system has current and historical sales data,
* And has access to real-time external market data,
* When the monthly inventory optimization process is triggered,
* Then inventory levels should automatically adjust to match the forecasted demand for the next month.

#### ATDD for Inventory Optimization
ATDD focuses on defining acceptance criteria from the user's perspective before writing code. For inventory optimization, acceptance tests could include:
* Given a low stock level, when an order is placed, then the inventory is replenished to the desired level.
* Given a high stock level, when no orders are received, then no new inventory is ordered.
* Given a perishable item nearing expiration, when stock remains, then a discount is applied to clear inventory.
 
#### BDD for Inventory Optimization
BDD extends ATDD by defining expected behaviors in a ubiquitous language understood by all stakeholders. Behavior scenarios for inventory optimization could be:
* **Scenario: Reorder stock when inventory is low**
  - Given the current stock level is below the reorder threshold
  - When an order is received
  - Then a purchase order should be generated to replenish stock
* **Scenario: Avoid overstocking non-perishable items  **
  - Given the current stock level exceeds the maximum threshold
  - And the item is non-perishable
  - When no orders are received
  - Then no new inventory should be ordered

#### TDD for Inventory Optimization
TDD involves writing unit tests before production code to drive the implementation. Unit tests for an inventory optimization module could verify:
* That the reorder quantity is calculated correctly based on current stock and desired levels
* That expiration dates are properly tracked, and discounts are applied when items are nearing expiration
* That ordering costs and constraints (e.g., supplier lead times) are considered in reorder decisions

### For [User Story 2](https://github.com/prakashvadrevu/oxford-ai-capstone-group-3/blob/main/abstract.md#2-view-demand-forecast-accuracy)

#### ATDD Test Cases:
* Given that the system has historical demand data and forecasted demand for a specific time period,
* When I request a demand forecast accuracy report,
* Then the report should display the actual demand, forecasted demand, variance, and percentage accuracy for each product.

#### BDD Scenarios:
* **Scenario: Viewing demand forecast accuracy report**
  - Given the system has historical demand data and forecasted demand for a specific time period
  - When the user requests a demand forecast accuracy report
  - Then the report should display actual demand, forecasted demand, variance, and percentage accuracy for each product
* **Scenario: Changing time period for accuracy report**
  - Given the system generates forecast accuracy reports
  - When the user selects a different time period
  - Then the report should update to display accuracy metrics for the selected period

#### TDD Test Cases:
* Test Case: Verify that the system calculates percentage accuracy correctly
  - Input: Actual demand = 100, Forecasted demand = 90
  - Expected Output: Percentage accuracy = 90%
* Test Case: Verify that the system handles negative variances appropriately
  - Input: Actual demand = 80, Forecasted demand = 100
  - Expected Output: Variance = -20
* Test Case: Verify that the report updates correctly when selecting different time periods
  - Input: Request weekly accuracy report instead of monthly
  - Expected Output: Updated report showing accuracy metrics for the selected week.
* Test Case: Verify that the interface allows filtering by product and time period
  - Input: Filter report by a specific product and time period
  - Expected Output: Display accuracy metrics only for the selected product and time period.
* Test Case: Verify that the report layout is visually clear and organized
  - Input: Access the accuracy report
  - Expected Output: Clear presentation of actual demand, forecasted demand, variance, and percentage accuracy for easy interpretation.

By following ATDD, BDD, and TDD practices, the inventory optimization system can be developed in an iterative and test-driven manner, ensuring it meets user requirements and expected behaviors while maintaining a comprehensive suite of automated tests

## Step 4: Synthetic Data Generation
Can we use the already provided Kelly's Dataset instead of generating Synthetic data?

## Step 5: Code Generation and Validation
Develop AI models and algorithms to predict and manage inventory:
* Model training: Use Kelly's dataset and synthetic test cases to train models.

## Step 6: Validation
Continuously test and refine the system using both synthetic and actual data, focusing on:
* Accuracy of inventory forecasts
* Response time to changing market conditions
* Effectiveness of automated inventory adjustments




