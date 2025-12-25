# Module 4: Ingestion, Streaming & Orchestration (3-5 weeks)

## Overview

This module covers modern data ingestion patterns, real-time streaming with Structured Streaming, Delta Live Tables for declarative pipelines, and workflow orchestration.

## Learning Objectives

- Use Autoloader for incremental ingestion
- Build streaming applications with Structured Streaming
- Create declarative pipelines with Delta Live Tables (DLT)
- Orchestrate workflows with Databricks Jobs
- Handle late data and watermarking

## Module Contents

### Notebooks

1. **[01-Autoloader-Incremental-Ingestion.ipynb](./01-Autoloader-Incremental-Ingestion.ipynb)**
   - Autoloader overview
   - Schema inference and evolution
   - Checkpoint management
   - Performance optimization

2. **[02-Structured-Streaming-Basics.ipynb](./02-Structured-Streaming-Basics.ipynb)**
   - Streaming concepts
   - Reading streams
   - Writing streams
   - Triggers and micro-batches

3. **[03-Structured-Streaming-Advanced.ipynb](./03-Structured-Streaming-Advanced.ipynb)**
   - Watermarking for late data
   - Stateful operations
   - Stream-stream joins
   - Exactly-once semantics

4. **[04-Delta-Live-Tables.ipynb](./04-Delta-Live-Tables.ipynb)**
   - DLT overview
   - Declarative pipelines
   - Expectations (data quality)
   - Incremental vs full refresh
   - Pipeline monitoring

5. **[05-Databricks-Workflows.ipynb](./05-Databricks-Workflows.ipynb)**
   - Job creation and configuration
   - Multi-task workflows
   - Task dependencies
   - Job clusters vs all-purpose clusters
   - Alerts and notifications

6. **[06-Change-Data-Capture.ipynb](./06-Change-Data-Capture.ipynb)**
   - CDC patterns
   - Processing database changes
   - Implementing upserts from CDC
   - Real-time replication

## Prerequisites

- Completed Module 3
- Understanding of streaming concepts
- Familiarity with Delta Lake

## Time Estimate

- **Beginner**: 5 weeks (25-30 hours)
- **Intermediate**: 4 weeks (20-24 hours)
- **Advanced**: 3 weeks (15-18 hours)

## Hands-on Labs

- Build an Autoloader ingestion pipeline
- Create a real-time streaming application
- Implement DLT with data quality checks
- Orchestrate multi-task workflow

## Key Projects

- **Project**: Real-time clickstream analytics
  - Ingest clickstream data with streaming
  - Apply transformations and aggregations
  - Create near-real-time dashboard
  - Implement data quality with DLT

## Next Steps

After completing this module, proceed to [Module 5: DevOps, CI/CD & Best Practices](../Module-5-DevOps-CICD/)
