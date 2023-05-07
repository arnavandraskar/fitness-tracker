# Personalized Health Monitoring

Personalized Health Monitoring is a project aimed at providing elderly individuals (age group 65+) with a holistic approach to tracking and managing their health. It utilizes technology to gather health data from various sources and presents it in an easy-to-understand format, allowing users to monitor their health parameters and make informed decisions about their well-being.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technology Used](#technology-used)
- [Prototype Description](#prototype-description)
- [API Simulation](#api-simulation)
- [ETL Process](#etl-process)
- [Data Visualization](#data-visualization)
- [Deployment](#deployment)


## Introduction

The Personalized Health Monitoring project aims to empower users (age group 65+) to take control of their health by providing them with a comprehensive platform to track and monitor their vital health parameters. By utilizing wearable devices and manual input, the system gathers data such as heart rate, daily steps, sleep patterns, and additional health information. It then presents this information through a user-friendly interface, offering visualizations and trends over time.

## Features

- Real-time tracking of health parameters, including heart rate, steps, sleep patterns, and more.
- Integration with wearable devices for automatic data collection.
- User-friendly dashboard for visualizing and analyzing health data.
- Continuous data monitoring and updates.

## Technology Used

The Personalized Health Monitoring project utilizes the following technologies:

- **Apache Kafka**: For stream processing and real-time data ingestion.
- **PostgreSQL**: A powerful and open-source relational database management system.
- **Google Looker Studio**: A data visualization and reporting tool for creating interactive dashboards.

## Prototype Description

The prototype of the Personalized Health Monitoring project consists of several components that work together to provide an enhanced health tracking experience:

1. **API Simulation:** The `smartwatch_api.py` script simulates the functionality of a smartwatch API. It generates random health data and sends it to the system at regular intervals.

2. **ETL Process:** The `ETL.py` script performs the Extract, Transform, and Load (ETL) process. It consumes the health data sent by the API simulation script, transforms it into a structured format, and loads it into a PostgreSQL database for further analysis.

3. **Data Visualization:** The project includes a Google Data Studio dashboard ([link](https://lookerstudio.google.com/reporting/b3895062-ea5d-4b8f-9f58-cb7c2232bef0)) that provides an intuitive visualization of the health data. The dashboard offers various charts, graphs, and insights to help users monitor their health parameters and progress towards their goals.


## Deployment
The Personalized Health Monitoring project is deployed on an AWS EC2 instance, ensuring continuous availability. The scripts are running continuously to capture and process real-time health data.

## Data Visualization
The Personalized Health Monitoring project includes a Google Data Studio dashboard that provides intuitive visualizations of the health data. You can access the dashboard using the following link:([Google Data Studio Dashboard](https://lookerstudio.google.com/reporting/b3895062-ea5d-4b8f-9f58-cb7c2232bef0)).

