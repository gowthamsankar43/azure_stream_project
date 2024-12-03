# azure_stream_project
Azure streaming etl pipeline with Kafka , ADF, Datalake, and Databricks
![image](https://github.com/user-attachments/assets/803c547c-40fd-4271-abec-7077af522e04)
 An simulated e-commerce platform that processing of customer orders in real-time.
The system must: 
1. Handle real-time communication between order, inventory, and shipping microservices. 
2. Store and transform data for analytics. 
System Overview:
 The system consists of the following components: 
1. Simulate an e-commerce scenario by generating a dummy dataset and sending it to Kafka topics. 
2. Design an ADF pipeline to read the dataset from Kafka, store it in a persistent storage or server, and trigger a Databricks job. 
3. Use Azure Databricks to read the stored data, apply data transformations, and save the processed data back to storage or the server for further analysis. 
