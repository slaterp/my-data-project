# my-data-project
Basic data engineering project to explore end-to-end ETL data pipelines .

## 1. Introduction

This is a basic data engineering project I used to familiarise myself with different data engineering tools. For a first project, I wanted to keep complexity low by using elements I was already familiar with: tools I had prior knowledge and experience with, data I knew well and open-source platforms with low barriers for entry. In this project I also wanted to use a small volume of data as I would be using a local Postgres instance. The end result was this simple pipeline that uses API calls, JSON data, Pandas for data processing and Postgres for storage.

## 2. Architecture

![image](https://user-images.githubusercontent.com/49575091/214498912-5ebf2e9d-c889-4e84-b5b2-a09138e2cf68.png)

## 3. ETL

### 3.1 Extract

The data for this project was extracted from the Squiggle AFL analytics API (https://api.squiggle.com.au/). Data was extracted in JSON format through a number of API calls - one for each AFL season beginning in 1990 and ending in 2022.

![image](https://user-images.githubusercontent.com/49575091/215917031-0fd4ddb5-474a-4ff3-bd20-310858565c33.png)
*Code responsible in data_request.py for API calls*

Data is stored locally in JSON format.

![image](https://user-images.githubusercontent.com/49575091/215917352-a6dd6baf-9278-410e-b1cd-86fa09057ed8.png)
![image](https://user-images.githubusercontent.com/49575091/215917504-1b7f81ac-d6cf-4e54-8423-bd9cc35514e3.png)

*Snapshot of data extracted from API*

### 3.2 Transform

Python's JSON library and Pandas' Dataframes provide a simple way to transform the extracted data. Using these we generate an array of dataframes containing all AFL seasons' data.

![image](https://user-images.githubusercontent.com/49575091/215918977-cc2f4f03-1182-4e23-8b13-9cefb077f22d.png)
*An array of Dataframes containing our extracted data*

Now that our data is in stored in dataframes, we have access to many different tools to transform and process the data (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). For this project, the transformation is simply removing the goals for/against and behinds for/against columns - generally in AFL statistics the total points for/against give enough resolution in terms of a teams offensive and defensive quality for the goals and behinds columns to be redundant.

![image](https://user-images.githubusercontent.com/49575091/215919655-99434908-2c97-4b7b-b612-57cfff458eee.png)
*Removing the redundant goals and behinds columns*

### 3.3 Load

To estbalish connection to the database, SQLAlchemy's create_engine() function is used. We can then use the Dataframe method to_sql() to load the data into Postgres.

![image](https://user-images.githubusercontent.com/49575091/215920776-0ab4ef4f-2e37-4fdb-bf3a-5c1102227161.png)
*Establishing DB connection and loading data*

## 4. Discussion 
### 4.1 Pandas vs Other Data Processing Options
- Dataframes are very functional
- Very effective for low volume data such as this project
- Pandas easy to pick up for anyone with Python experience

- Pandas probably not scalable (explain why - dataframes are operationally inefficient I think)
- Talk abt other options (eg Spark - distributed processing)

### 4.2 PostgreSQL vs Other Storage Options
- Why is Postgres good? Why did I pick it?
- What other options are there? Snowflake? MySQL? Cloud? Redshift? BigQuery?
- How would it go about integrating with BI tools?

## 5. Conclusion
