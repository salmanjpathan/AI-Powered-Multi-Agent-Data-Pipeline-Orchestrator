# 🚀 Enterprise Agentic AI Data Engineering Platform

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-121212?style=for-the-badge)](https://www.langchain.com/langgraph)
[![Azure Databricks](https://img.shields.io/badge/Azure%20Databricks-EF3E42?style=for-the-badge&logo=databricks&logoColor=white)](https://www.databricks.com/)
[![PySpark](https://img.shields.io/badge/PySpark-F8991D?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/docs/latest/api/python/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD8?style=for-the-badge)](https://delta.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama%203.2-000000?style=for-the-badge)](https://ollama.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/salmanjpathan)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)

> **Enterprise AI-powered Data Engineering Platform built with Azure Databricks, LangGraph, FastAPI, PySpark, Delta Lake, and Ollama (Llama 3.2).**

> An enterprise-style AI-powered Data Engineering platform that orchestrates end-to-end data pipelines using **LangGraph**, **Azure Databricks**, **FastAPI**, **PySpark**, and **Delta Lake**.

The platform follows the **Medallion Architecture (Bronze → Silver → Gold)** and leverages **AI-powered Data Quality Analysis** using **Ollama (Llama 3.2)**.

---

## ✨ Features

- 🤖 Multi-Agent Orchestration using LangGraph
- ⚡ Azure Databricks Job Automation
- 🥉 Bronze Layer Data Ingestion
- 🥈 Silver Layer Data Cleaning & Transformation
- 🥇 Gold Layer Business Aggregation
- 📊 Delta Lake Storage
- 🧠 AI-powered Data Quality Report using Ollama (Llama 3.2)
- 🌐 REST APIs using FastAPI
- 📋 Pipeline Execution Reporting
- 🔄 Modular & Scalable Architecture

---

## ⚡ Quick Start (30 seconds)

```bash
# 1. Clone
git clone https://github.com/salmanjpathan/AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator.git
cd AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator

# 2. Install
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

# 3. Configure Databricks
echo DATABRICKS_HOST=your-workspace-url > .env
echo DATABRICKS_TOKEN=your-token >> .env

# 4. Start Services (in separate terminals)
ollama serve              # Terminal 1: Ollama LLM
uvicorn app.main:app --reload  # Terminal 2: FastAPI

# 5. Open Browser
# http://127.0.0.1:8000/docs
```

👉 **Full Setup Guide**: See [SETUP_AND_RUNBOOK.md](SETUP_AND_RUNBOOK.md) for detailed installation & troubleshooting

---

## 🏗️ Architecture

<p align="center">
  <img src="./images/architecture.png" alt="Architecture Diagram" width="100%">
</p>

The platform orchestrates an end-to-end AI-powered data engineering workflow using FastAPI, LangGraph, Azure Databricks, Delta Lake, and Ollama (Llama 3.2).

---

# 🛠️ Tech Stack

| Category        | Technology         |
| --------------- | ------------------ |
| Language        | Python             |
| Framework       | FastAPI            |
| AI Framework    | LangGraph          |
| LLM             | Ollama (Llama 3.2) |
| Data Processing | PySpark            |
| Data Platform   | Azure Databricks   |
| Storage         | Delta Lake         |
| APIs            | FastAPI            |
| Version Control | Git & GitHub       |

---

# 📂 Project Structure

```text
AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator
│
├── app
│   ├── agents
│   ├── api
│   ├── databricks
│   ├── graph
│   ├── llm
│   ├── schemas
│   ├── services
│   ├── utils
│   └── main.py
│
├── data
│   └── raw
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🤖 AI Agents

### 📥 Ingest Agent

- Collects metadata
- Calculates file hash
- Tracks dataset information

---

### 🥉 Bronze Agent

Triggers the Bronze Databricks Job.

Responsibilities

- Raw Data Ingestion
- Bronze Delta Table Creation

---

### ✅ Validator Agent

Performs initial dataset validation before processing.

Current validation includes

- Dataset verification
- Basic quality checks

---

### 🥈 Silver Agent

Triggers the Silver Databricks Job.

Responsibilities

- Data Cleaning
- Standardization
- Transformation

---

### 🥇 Gold Agent

Triggers the Gold Databricks Job.

Responsibilities

- Business Aggregations
- Analytics-ready Data
- KPI Generation

---

### 📋 Reporter Agent

Creates pipeline execution summary.

Includes

- Pipeline Status
- Execution Time
- Recommendations

---

### 🤖 AI Data Quality Agent

Uses **Ollama (Llama 3.2)** to generate AI-powered Data Quality insights.

Generates

- Data Quality Summary
- Severity Assessment
- Business Impact
- Recommendations

---

# 📊 Medallion Architecture

```text
Raw Dataset
      │
      ▼
 Bronze Layer
      │
      ▼
 Silver Layer
      │
      ▼
 Gold Layer
```

---

# 🚀 API Endpoints

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open Swagger

```text
http://127.0.0.1:8000/docs
```

Available APIs

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | /health       | Health Check              |
| POST   | /run-pipeline | Execute Complete Pipeline |

---

# ⚙️ Pipeline Workflow

```text
Ingest
   │
Bronze
   │
Validate
   │
Silver
   │
Gold
   │
Reporter
   │
AI Data Quality
```

---

# 🎬 Demo & Example

## API Documentation (Interactive)

Once the FastAPI server is running, visit:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive endpoint testing with real request/response examples.

## Example: Run Pipeline

**POST Request:**

```bash
curl -X POST "http://127.0.0.1:8000/run-pipeline" \
  -H "Content-Type: application/json" \
  -d '{
    "pipeline_id": "DEMO_001",
    "source_file": "data/raw/sales.csv",
    "source_type": "csv"
  }'
```

**Expected Response (Success):**

```json
{
  "pipeline_id": "DEMO_001",
  "status": "SUCCESS",
  "execution_time_seconds": 45.23,
  "ingest_status": "SUCCESS",
  "bronze_status": "SUCCESS",
  "validation_status": "SUCCESS",
  "transform_status": "SUCCESS",
  "gold_status": "SUCCESS",
  "ai_insights": {
    "data_quality_summary": "Dataset contains high-quality transactional data",
    "data_quality_score": 95,
    "issues_detected": 0,
    "recommendations": "Data is ready for analytics"
  }
}
```

## Test Datasets Included

The project comes with 4 pre-configured test datasets:

| Dataset                | Size     | Purpose         | Location                          |
| ---------------------- | -------- | --------------- | --------------------------------- |
| sales.csv              | 5 rows   | Quick demo      | `data/raw/sales.csv`              |
| sales_large.csv        | 1M rows  | Stress test     | `data/raw/sales_large.csv`        |
| sales_quality_test.csv | 1K rows  | Error detection | `data/raw/sales_quality_test.csv` |
| sales_mixed_test.csv   | 100 rows | Multi-type data | `data/raw/sales_mixed_test.csv`   |

## Health Check

**GET Request:**

```bash
curl http://127.0.0.1:8000/health
```

**Expected Response:**

```json
{
  "status": "healthy",
  "timestamp": "2026-08-30T10:30:45"
}
```

---

# 📷 Screenshots

Screenshots coming soon:

- FastAPI Swagger UI (/docs)
- Databricks Jobs Dashboard
- Bronze Layer Data
- Silver Layer Transformations
- Gold Layer Aggregations
- AI Quality Report Generation

---

# 📦 Dataset

This project uses the **DataCo Smart Supply Chain Dataset**.

Download it from Kaggle and place it in:

```text
data/raw/DataCoSupplyChainDataset.csv
```

The dataset is excluded from GitHub because of its size.

---

# 🔮 Roadmap

## ✅ Version 1.0

- FastAPI
- LangGraph
- Azure Databricks Integration
- Bronze Layer
- Silver Layer
- Gold Layer
- AI Data Quality Report

### 🚧 Upcoming Features

- Databricks-based Validation
- Metadata Logging
- Audit Tables
- AI Root Cause Analysis
- Business Insights Agent
- Streamlit Dashboard
- GitHub Actions CI/CD
- Notification System

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/salmanjpathan/AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator.git
```

Navigate to the project

```bash
cd AI-Powered-Multi-Agent-Data-Pipeline-Orchestrator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

# 👨‍💻 Author

**Salman Pathan**

Azure Data Engineer | Databricks | PySpark | FastAPI | LangGraph | AI Engineering

GitHub

https://github.com/salmanjpathan

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
