# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b141c37a-5d09-455a-a056-a3efc9176bc5",
# META       "default_lakehouse_name": "data_storage",
# META       "default_lakehouse_workspace_id": "cfed32f0-9c4a-467a-9e23-07af9d893908"
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT orderid,itemid,orderunits,address,EventProcessedUtcTime FROM data_storage.stg_table")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("WriteToADLSGen2") \
    .getOrCreate()

# Set up the configurations for ADLS Gen2
spark.conf.set("fs.azure.account.key.streamingstoragelake1234.dfs.core.windows.net", "oCsSK0NO9Et5LwphlT3nweti9NUvka5obHc9hO4r8NnFgZNC2bJVVv8BEirrhWk/fO3MjVl3LWW8+AStnap9RA==")

# Write the DataFrame to ADLS Gen2
df.write.format('parquet').mode('overwrite').save('abfss://stgfolder@streamingstoragelake1234.dfs.core.windows.net/stream_data')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

