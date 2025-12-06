# Module 3: Lakehouse Core - Delta, Medallion, Unity Catalog (3-5 weeks)

## Overview

This module covers the core of Databricks lakehouse: Delta Lake for ACID transactions, Medallion architecture for data organization, and Unity Catalog for governance.

## Learning Objectives

- Master Delta Lake features and operations
- Implement Medallion architecture patterns
- Use Unity Catalog for data governance
- Manage schemas, tables, and permissions
- Apply schema evolution and time travel

## Module Contents

### Notebooks

1. **[01-Delta-Lake-Fundamentals.ipynb](./01-Delta-Lake-Fundamentals.ipynb)**
   - What is Delta Lake?
   - ACID transactions
   - Creating Delta tables
   - Basic operations (read, write, update, delete)

2. **[02-Delta-Lake-Advanced-Features.ipynb](./02-Delta-Lake-Advanced-Features.ipynb)**
   - Time travel and versioning
   - Schema evolution
   - OPTIMIZE and Z-ORDER
   - VACUUM for cleanup
   - Change Data Feed (CDF)

3. **[03-MERGE-Operations.ipynb](./03-MERGE-Operations.ipynb)**
   - MERGE syntax (Upserts)
   - SCD Type 2 implementation
   - Handling duplicates
   - Performance tuning

4. **[04-Medallion-Architecture-Implementation.ipynb](./04-Medallion-Architecture-Implementation.ipynb)**
   - Bronze layer: Raw data ingestion
   - Silver layer: Cleaning and validation
   - Gold layer: Business aggregates
   - End-to-end pipeline example

5. **[05-Unity-Catalog-Basics.ipynb](./05-Unity-Catalog-Basics.ipynb)**
   - Unity Catalog overview
   - Three-level namespace (catalog.schema.table)
   - Creating catalogs and schemas
   - Managed vs external tables

6. **[06-Unity-Catalog-Governance.ipynb](./06-Unity-Catalog-Governance.ipynb)**
   - Access control and permissions
   - Row and column-level security
   - Data lineage
   - Data sharing
   - Audit logs

7. **[07-Schema-Management.ipynb](./07-Schema-Management.ipynb)**
   - Schema enforcement
   - Schema evolution strategies
   - Data types and constraints
   - Schema migration patterns

## Prerequisites

- Completed Module 2
- Understanding of data modeling
- Access to Databricks workspace with Unity Catalog

## Time Estimate

- **Beginner**: 5 weeks (25-30 hours)
- **Intermediate**: 4 weeks (20-24 hours)
- **Advanced**: 3 weeks (15-18 hours)

## Hands-on Labs

- Create Bronze-Silver-Gold pipeline
- Implement SCD Type 2 with MERGE
- Set up Unity Catalog with proper governance
- Practice time travel and schema evolution

## Key Projects

- **Project**: Build a retail analytics pipeline
  - Ingest raw transaction data (Bronze)
  - Clean and validate (Silver)
  - Create business metrics (Gold)
  - Apply Unity Catalog governance

## Next Steps

After completing this module, proceed to [Module 4: Ingestion, Streaming & Orchestration](../Module-4-Ingestion-Streaming-Orchestration/)
