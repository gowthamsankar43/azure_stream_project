# azure_stream_project
Azure streaming etl pipeline with Kafka , ADF, Datalake, and Databricks
![Screenshot (16)](https://github.com/user-attachments/assets/f9b0a9ee-e295-4afa-a156-c8e0e6341944)

 An simulated e-commerce platform that processing of customer orders in real-time.
The system has three main parts
	1. Data Producing system
	2. Kafka streaming system
	3. Processing and Storing data in Onelake 
	
**Data Producing System**
		Real-time order data has been produced by python code with use of python faker package , fake data has been produced and streamed to kafka with essential kafka libraries.
** Kafka Streaming System**
		Confluent Kafka cluster has been configured to get data and send to consumer.
**Microsoft Fabric System**
		Fabric work space has been configured with Fabric Lake house, Fabric Event stream, the streaming data has been captured with eventstream platform and stored in Lakehouse in raw format.
		Realtime powerBI dashboard displays the current data from lakehouse with some key points.
