from pyspark import pipelines as dp
from pyspark.sql.functions import col

@dp.table(
    name="trips"
)
def load():
    return (
        spark.readStream.table("samples.nyctaxi.trips")
    )