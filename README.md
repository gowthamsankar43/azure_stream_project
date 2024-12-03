# azure_stream_project
Azure streaming etl pipeline with Kafka , ADF, Datalake, and Databricks
![Screenshot (16)](https://github.com/user-attachments/assets/f9b0a9ee-e295-4afa-a156-c8e0e6341944)

 An simulated e-commerce platform that processing of customer orders in real-time.
The system must: 
1. Handle real-time communication between order, inventory, and shipping microservices. 
2. Store and transform data for analytics. 
System Overview:
 The system consists of the following components: 
1. Simulate an e-commerce scenario by generating a dummy dataset and sending it to Kafka topics. 
2. Design an ADF pipeline to read the dataset from Kafka, store it in a persistent storage or server, and trigger a Databricks job. 
3. Use Azure Databricks to read the stored data, apply data transformations, and save the processed data back to storage or the server for further analysis. 
