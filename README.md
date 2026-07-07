# 🏠 PropertyIntelAI

**AI-Powered Property Listing Quality & SEO Analyzer Using a Structured Real Estate Knowledge Base**

## Overview

PropertyIntelAI is an end-to-end AI application that evaluates the quality and SEO readiness of real estate listings. The project combines **data engineering**, a **structured knowledge base**, and **Large Language Models (LLMs)** to provide explainable, actionable feedback for property listings.

Unlike traditional AI applications that only generate text, PropertyIntelAI first analyzes a listing against a structured real estate knowledge base built from historical housing data. The AI then uses this structured analysis to generate quality scores, SEO recommendations, and listing improvements.

---

# Problem Statement

Many real estate listings fail to attract buyers because they:

* Omit important property details
* Have poor or incomplete descriptions
* Are not optimized for search engines
* Lack consistency and readability
* Miss key selling points

PropertyIntelAI helps improve listing quality by identifying missing information and providing AI-powered recommendations.

---

# Objectives

* Build a structured real estate knowledge base from historical housing data.
* Evaluate new property listings against the knowledge base.
* Generate explainable listing quality and SEO scores.
* Recommend improvements using AI.
* Provide an easy-to-use web interface for users.

---

# Features

## Data Collection

The application uses the **Ames Housing Dataset** as the primary data source.

The dataset includes:

* Property details
* Neighborhood information
* Property quality
* Lot size
* Living area
* Bedrooms
* Bathrooms
* Garage information
* Basement information
* Sale prices
* Amenities

---

## Data Engineering

The raw dataset is cleaned and transformed into a structured knowledge base.

### Data Cleaning

* Standardize column names
* Handle missing values
* Normalize categorical values
* Remove inconsistencies

### Feature Engineering

The preprocessing pipeline creates features such as:

* Property type
* Living area
* Number of bedrooms
* Number of bathrooms
* Garage capacity
* Amenity count
* Property quality label
* Completeness score
* Recommended SEO keywords

The processed knowledge base is stored as:

```text
data/processed/property_knowledge_base.csv
```

---

# Knowledge Base

Instead of analyzing listings directly with an LLM, PropertyIntelAI first compares user listings against a structured knowledge base.

The knowledge base contains information about:

* Property characteristics
* Amenities
* Property quality
* Neighborhoods
* Listing completeness
* Common SEO keywords

This enables explainable and consistent evaluations.

---

# AI Workflow

### Step 1 – User Input

The user submits a property listing.

### Step 2 – Feature Extraction

The system extracts information such as:

* Price
* Bedrooms
* Bathrooms
* Square footage
* Garage
* Basement
* Amenities
* Location

### Step 3 – Knowledge Base Comparison

The listing is compared against the structured knowledge base.

The application identifies:

* Missing fields
* Completeness score
* Typical characteristics of high-quality listings

### Step 4 – AI Analysis

The knowledge base analysis is sent to an LLM.

The LLM generates:

* Listing Quality Score
* SEO Score
* Explanation of the scores
* Missing information
* SEO keyword recommendations
* Improvement suggestions
* Optimized listing description

---

# System Architecture

```text
Raw Housing Dataset
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Property Knowledge Base
(CSV + SQLite)
        │
        ▼
Knowledge Base Analyzer
        │
        ▼
OpenAI LLM
        │
        ▼
FastAPI Backend
        │
        ▼
Streamlit User Interface
```

---

# Technology Stack

### Programming Language

* Python

### Data Engineering

* Pandas
* NumPy

### Database

* SQLite

### Backend

* FastAPI

### Frontend

* Streamlit

### AI

* OpenAI API

### Version Control

* Git
* GitHub

---

# Project Structure

```text
PropertyIntelAI/
│
├── backend/
│   ├── ai_engine.py
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── database.py
│   ├── knowledge_base.py
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── properties.csv
│   ├── processed/
│   │   └── property_knowledge_base.csv
│   └── realestate.db
│
├── docs/
├── notebooks/
├── tests/
├── screenshots/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# API Endpoints

### GET /

Returns the API status.

### GET /health

Checks whether the API is running.

### POST /analyze

Accepts a property listing and returns:

* Quality Score
* SEO Score
* Completeness Score
* Missing Fields
* AI Explanation
* SEO Keywords
* Improvement Suggestions
* Optimized Listing

Example request:

```json
{
  "listing_text": "Beautiful 3-bedroom home in Ames with updated kitchen and attached garage."
}
```

---

# User Interface

The Streamlit application allows users to:

* Paste a property listing
* Analyze listing quality
* View completeness score
* View SEO score
* Identify missing information
* Read AI explanations
* View suggested SEO keywords
* Generate an optimized listing

---

# Installation

## Clone the repository

```bash
git clone https://github.com/<your-username>/PropertyIntelAI.git
cd PropertyIntelAI
```

## Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Application

## Build the knowledge base

```bash
python backend/data_preprocessing.py
```

## Start the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

## Launch the Streamlit application

```bash
streamlit run frontend/app.py
```

---

# Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Vector database for semantic property search
* Image quality analysis
* Duplicate listing detection
* Property price estimation
* Similar property recommendations
* Cloud deployment
* User authentication
* PDF report generation
* Interactive analytics dashboard

---

# Skills Demonstrated

* Data Collection
* Data Cleaning
* Feature Engineering
* Knowledge Base Construction
* AI Prompt Engineering
* LLM Integration
* FastAPI Development
* Streamlit Development
* SQLite Database Design
* Git & GitHub
* End-to-End AI Application Development

---

# License

This project was developed for educational purposes and as part of an AI-powered real estate application portfolio.
