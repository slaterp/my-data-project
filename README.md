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

Due to my previous experience with the Pandas library, I selected it for this project. Beyond that, Pandas is a very useful option for low volume data processing. Pandas' Dataframe data structure are highly functional with many useful methods to access specific columns, labels and/or rows, and also perform calculations (dot products, aggregates, cumulative min/max). Pandas is also very simple for someone with Python experience to pick up due to its straightforward syntax and extensive API documentaiton and community.

Pandas falls short on large datasets. Pandas exclusively operates on a single core/machine which inhibits its ability to process large volumes of data. A common option for large volumes of data is Spark, which has similar benefits to Pandas (extensive community support and documentation, easy to pick up with Python experience). Spark however has the added bonus of being distributed in nature - having the ability to use multiple cores or machines to perform operations. [Analysis by blogger and developer Steven Levine](https://stevenlevine.dev/2022/01/pandas-on-spark-vs-plain-pandas/) found that there was a nearly 50% difference in runtime between Spark and Pandas for just 7.3 GB of data. 

### 4.2 PostgreSQL vs Other Storage Options

Again, like with Pandas, I selected Postgres firstly because I had prior experience with the database. Postgres is however an excellent option - a widely used open source database with great community support and documentation. Postgres is used by AWS in their relational database service Redshift, Postgres is available on Azure servers and GCP has a Cloud SQL service for Postgres. PostgreSQL in itself provides support for foreign keys, sub queries and has better CSV support than most SQL options (such as `copy to` and `copy from` functions).

- What other options are there? Snowflake? MySQL? Cloud? Redshift? BigQuery? NoSQL?
- How would it go about integrating with BI tools?

## 5. Conclusion
