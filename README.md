Supply Chain Performance Analysis (End-to-End Data Analyst Project)

Overview

Welcome to my end-to-end Supply Chain Analysis Project, focused on identifying inefficiencies in delivery performance and uncovering the root causes of delays.

This project was built to simulate a real-world business scenario where a company is facing high late delivery rates and wants to understand:

Why deliveries are delayed
Whether the issue is operational or systemic
What actions can improve performance

Using a structured analytical approach, I explored delivery behavior, logistics efficiency, planning accuracy, and business impact to derive actionable insights.

The Business Questions

Below are the key questions I answered in this project:

Why is the late delivery rate so high?
Does shipping mode impact delivery performance?
Do delivery delays affect profitability?
Are certain regions responsible for delays?
Do product categories influence delivery time?
Is poor planning (scheduling) causing delays?
Are customer segments treated differently?
What are the key drivers of inefficiency and how can they be fixed?

 Tools I Used

This project was built using industry-relevant tools:

Python – Core analysis
Pandas → data cleaning & transformation
Plotly → interactive visualizations
Jupyter Notebook (VS Code)
Used for analysis, storytelling, and combining code with insights
Git & GitHub
Version control and project sharing

Data Preparation & Cleaning

Before analysis, I built a reusable data cleaning pipeline (data_cleaning.py) to ensure consistency and scalability.

Key Cleaning Steps:
Standardized column names (lowercase, underscores)
Converted date columns into datetime format
Removed irrelevant columns (PII, redundant fields)
Handled missing values
Created new features:
order_processing_time
delay (Actual vs Scheduled difference)
schedule_gap (Planning accuracy)

The Analysis

Each section of the analysis focuses on a specific business problem.

High Late Delivery Rate
Insight:
Over 57% of orders are delivered late
Most delays are 1–2 days

 Indicates a system-wide inefficiency

Shipping Mode Efficiency
Insight:
Premium shipping (First Class, Second Class) performs worse than expected
Standard shipping is the most stable

 Faster shipping ≠ better delivery

Impact on Profitability
Insight:
Delays have minor impact on profit
Profit variation is influenced more by other factors

 Delay is an operational issue, not a major financial driver

Regional Performance
Insight:
Very small variation across regions (~0.57–0.65 days)

 Problem is not geographic, it's systemic

Product Category Impact
Insight:
Minor variation across categories
High-volume categories show stable performance

 Category is not a major driver

Root Cause: Scheduling Accuracy
Insight:
Only ~18.7% orders are on-time as planned
~57% deliveries are underestimated
Average gap = +0.56 days

 Planning is the main problem

Customer Segment Analysis
Insight:
All segments show almost identical performance

 No service bias — issue affects all customers equally

Key Insights
High late delivery rate is a system-wide issue
The biggest root cause is inaccurate scheduling
Logistics execution is not the main problem — planning is
Region, category, and segment have minimal impact
Premium shipping is inefficient and unreliable

Business Risks
Unrealistic delivery promises reduce customer trust
High delay rate damages brand reputation
Inefficient premium services waste resources

Recommendations
1. Fix Planning (Highest Priority)
Use historical data for accurate delivery estimates
Add buffer time in scheduling
2. Reevaluate Shipping Strategy
Align premium shipping promises with actual performance
3. Focus on System-Level Improvements
Optimize overall logistics instead of isolated areas
4. Improve Customer Experience
Provide realistic delivery timelines
Increase transparency

What I Learned
Real-world data rarely gives perfect answers — interpretation matters
Not every pattern is meaningful (avoid overanalysis)
Root cause analysis is more valuable than surface insights
Clean structure and storytelling are critical in data projects

Challenges I Faced
Synthetic dataset patterns required careful interpretation
Avoiding misleading conclusions from small differences
Designing clear and readable visualizations
Separating signal vs noise in analysis

Conclusion

This project demonstrates a complete data analysis workflow — from data cleaning to business insights.

The key takeaway:

The supply chain is not failing due to logistics execution, but due to inaccurate planning and unrealistic scheduling.
