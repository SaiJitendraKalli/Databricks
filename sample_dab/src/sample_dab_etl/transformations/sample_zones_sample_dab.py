from pyspark import pipelines as dp
from pyspark.sql.functions import col, avg

@dp.table(
    name="trips_aggregated"
)
def aggregate():
    return (
        spark.readStream.table("workspace.sample_dab.trips")
        .groupBy(
            col("pickup_zip")
        )
        .agg(
            avg("fare_amount").alias("avg_fare_amount")
        )
    )