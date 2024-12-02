# Fabric notebook source

# METADATA ********************

# META {
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b141c37a-5d09-455a-a056-a3efc9176bc5",
# META       "default_lakehouse_name": "data_storage",
# META       "default_lakehouse_workspace_id": "cfed32f0-9c4a-467a-9e23-07af9d893908",
# META       "known_lakehouses": [
# META         {
# META           "id": "b141c37a-5d09-455a-a056-a3efc9176bc5",
# META           "name": "data_storage"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Run the below script or schedule it to run regularly to optimize your Lakehouse table 'stg_table'

from delta.tables import *
deltaTable = DeltaTable.forName(spark, "stg_table")
deltaTable.optimize().executeCompaction()

# If you only want to optimize a subset of your data, you can specify an optional partition predicate. For example:
#
#     from datetime import datetime, timedelta
#     startDate = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
#     deltaTable.optimize().where("date > '{}'".format(startDate)).executeCompaction()

