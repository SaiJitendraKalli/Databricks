# Datasets for Databricks Course

This directory contains Parquet datasets used throughout the course. **All datasets are in Parquet format** for optimal performance and compatibility with Databricks and Spark.

## Dataset Options

### Option 1: Built-in Databricks Datasets (Recommended)
If you're using Databricks Community Edition or a Databricks workspace, you can access built-in sample datasets:

```python
# List available datasets
display(dbutils.fs.ls("/databricks-datasets/"))

# Common datasets used in this course:
# - /databricks-datasets/flights/
# - /databricks-datasets/retail-org/
# - /databricks-datasets/songs/
# - /databricks-datasets/structured-streaming/events/
# - /databricks-datasets/COVID/
```

### Option 2: Sample Parquet Files (Included)
Small sample Parquet files are provided in this directory for local testing and exercises:

1. **customers.parquet** - Customer information (20 records)
2. **orders.parquet** - Order transactions (30 records)
3. **products.parquet** - Product catalog (20 records)
4. **sales.parquet** - Sales data (30 records)
5. **employees.parquet** - Employee data (20 records)

### Option 3: External Public Datasets
Links to public datasets for advanced projects:

#### NYC Taxi Data
- **Source**: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- **Use Cases**: Streaming, large-scale processing, time series analysis
- **Format**: Parquet, CSV

#### Kaggle Datasets
- **Source**: https://www.kaggle.com/datasets
- **Popular Datasets**:
  - E-commerce datasets
  - Retail analytics
  - Customer churn
  - Time series forecasting

#### UCI Machine Learning Repository
- **Source**: https://archive.ics.uci.edu/ml/index.php
- **Use Cases**: Classification, regression, clustering

## Datasets by Module

### Module 1: Prerequisites
- **customers.parquet** - For SQL practice (joins, aggregations)
- **orders.parquet** - For SQL practice (window functions, CTEs)
- **sales.parquet** - For Python data manipulation

### Module 2: Databricks & Spark Fundamentals
- **Built-in datasets**: `/databricks-datasets/flights/`
- **products.parquet** - For DataFrame operations
- **orders.parquet** - For RDD operations and transformations

### Module 3: Lakehouse Core (Delta Lake)
- **sales.parquet** - For Delta table creation and MERGE operations
- **customers.parquet** - For schema evolution examples
- **orders.parquet** - For time travel and versioning demos

### Module 4: Ingestion & Streaming
- **Built-in datasets**: `/databricks-datasets/structured-streaming/events/`
- **orders.parquet** - For Auto Loader examples
- **sales.parquet** - For streaming simulations

### Module 6: Certification Prep
- All sample datasets for practice scenarios

### Module 7: End-to-End Projects

#### Project 1: Retail Analytics
**Datasets needed**:
- customers.parquet
- orders.parquet
- products.parquet
- sales.parquet

#### Project 2: Streaming Analytics
**Datasets needed**:
- `/databricks-datasets/structured-streaming/events/`
- Or generate streaming data using provided scripts

#### Project 3: E-commerce Pipeline
**Datasets needed**:
- Kaggle e-commerce dataset (download separately)
- Or use provided sample Parquet data

## Loading Datasets in Your Notebooks

### Loading Parquet Files

```python
# For local Parquet files (if uploaded to Databricks)
df = spark.read.format("parquet") \
    .load("/FileStore/tables/customers.parquet")

# For GitHub raw files (public access)
parquet_url = "https://github.com/SaiJitendraKalli/Databricks/raw/main/Databricks-Course/Datasets/customers.parquet"
df = spark.read.format("parquet").load(parquet_url)

# Or use pandas to read first, then convert to Spark DataFrame
import pandas as pd
pdf = pd.read_parquet("customers.parquet")
df = spark.createDataFrame(pdf)
```

### Loading Built-in Datasets

```python
# Read built-in flights dataset (already in Parquet)
flights_df = spark.read.format("parquet") \
    .load("/databricks-datasets/flights/departuredelays.parquet")

# Read retail org dataset (Delta format)
retail_df = spark.read.format("delta") \
    .load("/databricks-datasets/retail-org/customers/")
```

### Generating Sample Data

If you need to generate your own sample data for testing:

```python
from pyspark.sql import Row
from datetime import datetime, timedelta
import random

# Generate sample orders
def generate_orders(num_records=1000):
    orders = []
    for i in range(num_records):
        order = Row(
            order_id=i+1,
            customer_id=random.randint(1, 1000),
            product_id=random.randint(1, 500),
            order_date=(datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
            quantity=random.randint(1, 10),
            amount=round(random.uniform(10, 1000), 2),
            status=random.choice(["pending", "completed", "cancelled"])
        )
        orders.append(order)
    return spark.createDataFrame(orders)

# Create sample orders DataFrame
orders_df = generate_orders(5000)

# Save as Parquet for reuse
orders_df.write.format("parquet") \
    .mode("overwrite") \
    .save("/tmp/generated_orders.parquet")

display(orders_df)
```

## Dataset Schemas

### customers.parquet
```
customer_id: integer
first_name: string
last_name: string
email: string
phone: string
address: string
city: string
state: string
zip_code: string
country: string
registration_date: date
```

### orders.parquet
```
order_id: integer
customer_id: integer
product_id: integer
order_date: date
quantity: integer
amount: decimal(10,2)
status: string
shipping_address: string
payment_method: string
```

### products.parquet
```
product_id: integer
product_name: string
category: string
subcategory: string
price: decimal(10,2)
cost: decimal(10,2)
brand: string
description: string
```

### sales.parquet
```
sale_id: integer
order_id: integer
product_id: integer
customer_id: integer
sale_date: timestamp
quantity: integer
unit_price: decimal(10,2)
total_amount: decimal(10,2)
discount: decimal(10,2)
region: string
```

### employees.parquet
```
employee_id: integer
first_name: string
last_name: string
email: string
department: string
position: string
hire_date: date
salary: decimal(10,2)
manager_id: integer
```

## Uploading Datasets to Databricks

### Method 1: Using Databricks UI
1. Click on "Data" in the left sidebar
2. Click "Add Data" → "Upload File"
3. Select your Parquet files
4. Files will be stored in `/FileStore/tables/`

### Method 2: Using dbutils
```python
# Upload from your local machine using Databricks UI
# Then access with:
dbutils.fs.ls("/FileStore/tables/")

# Read the uploaded Parquet file
df = spark.read.format("parquet").load("/FileStore/tables/customers.parquet")
```

### Method 3: Using Git Integration
1. Clone this repository in Databricks
2. Datasets will be available in the repo folder
3. Access them using relative paths

## Data Generation Scripts

For projects requiring larger datasets, use the provided generation script:

- **create_parquet_datasets.py** - Creates all sample Parquet datasets with realistic data

This script is available in the `Datasets/scripts/` folder.

To generate larger datasets, modify the script parameters:

```python
# Edit the script to generate more records
create_customers_parquet(num_records=1000)  # Instead of 20
create_orders_parquet(num_records=5000)      # Instead of 30
```

## External Dataset Setup

### NYC Taxi Data (for advanced projects)
```python
# Download and process NYC taxi data (Parquet format)
taxi_df = spark.read.format("parquet") \
    .load("s3://nyc-tlc/trip data/yellow_tripdata_2023-01.parquet")

# Or use public URLs
taxi_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
taxi_df = spark.read.format("parquet").load(taxi_url)
```

### COVID-19 Data
```python
# Built-in COVID dataset in Databricks (CSV format - can convert to Parquet)
covid_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/databricks-datasets/COVID/coronavirusdataset/")

# Save as Parquet for better performance
covid_df.write.format("parquet") \
    .mode("overwrite") \
    .save("/tmp/covid_data.parquet")
```

## Best Practices

1. **Use Parquet Format**: Parquet is columnar, compressed, and optimized for Spark/Databricks
2. **Start Small**: Use sample Parquet files for learning and testing
3. **Scale Up**: Move to built-in datasets for realistic scenarios
4. **Production-Like**: Use external datasets for portfolio projects
5. **Documentation**: Always document your data sources
6. **Partitioning**: For large datasets, partition Parquet files by key columns

## Troubleshooting

### Issue: Cannot access /databricks-datasets/
**Solution**: This path only works in Databricks workspaces. Use sample Parquet files for local testing.

### Issue: File not found error
**Solution**: Verify the file path and ensure the Parquet file is uploaded to Databricks.

### Issue: Schema mismatch
**Solution**: Parquet files include schema information. Use `df.printSchema()` to inspect the schema.

### Issue: Need to convert CSV to Parquet
**Solution**: Read CSV and write as Parquet:
```python
# Read CSV
csv_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("data.csv")

# Write as Parquet
csv_df.write.format("parquet") \
    .mode("overwrite") \
    .save("data.parquet")
```

## Additional Resources

- [Databricks Datasets Documentation](https://docs.databricks.com/data/databricks-datasets.html)
- [Kaggle API for Dataset Download](https://github.com/Kaggle/kaggle-api)
- [Public Dataset Collections](https://github.com/awesomedata/awesome-public-datasets)

---

**Need help with datasets?** Check Module 8: Additional Resources for more data sources and tutorials.
