# AWS Data Pipeline for YouTube Trending videos Dataset
## Overview
This project objectve is to build a data pipeline using AWS services to cleanse YouTube trending videos dataset from Kaggle by converting semi-structured data to structured format and perform analysis based on the video categories and the trending metrics.
## AWS Services Used
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.  
2. AWS IAM: Identity and access management which enables us to manage access to AWS services and resources securely.  
3. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.  
4. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.  
5. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.  
6. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
## Datasets Used
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

https://www.kaggle.com/datasets/datasnaek/youtube-new
## Data Pipeline Architecture
<img width="953" alt="Pipeline_Architecture_Diagram" src="https://github.com/devallasaitej/Youtube_Data_Engineering/assets/64268620/97192c34-2e37-4a5e-b631-1a40444f089e">
