# Live Encrypted Network Traffic Classifier

## Overview

In this project, I focused on developing a machine learning model for classifying encrypted network traffic into various types, including web, streaming, and email. The model utilizes features extracted exclusively when the DNS of the packet is encrypted, such as the time between packets and packet length. The project began by using NFStream, a data analysis tool, to collect data and extract these features from a live server containing real client traffic. Data preprocessing, including cleaning, clustering, and feature selection, was performed using Pandas and NumPy. The data was visualized through Seaborn. A benchmark was established for four machine learning algorithms (Decision Tree, Random Forest, SVM, and KNN), with the results favoring the Random Forest algorithm. The model was constructed using Random Forest and deployed on the live server for predictions. These predictions were stored in an SQL database and displayed through Grafana for comprehensive monitoring and analysis.

## Technologies Used

- Capturing network traffic: NFStream (generated me the pcap file)
- Data Processing: Pandas, NumPy
- Machine Learning benchmark from scikit-learn: Decision Tree, Random Forest, SVM, KNN
- Visualization: Seaborn
- Database to store predictions: SQL
- Monitoring and Analysis: Grafana

## Features

- Capturing traffic from a network port.
- Classification of encrypted network traffic into different types.
- Feature extraction from encrypted DNS packets.
- Benchmarking of machine learning algorithms.
- Deployment of the model on a live server.
- Storage of predictions in an SQL database.
- Comprehensive monitoring and analysis through Grafana.
