# Machine Learning Prediction API with Azure DevOps CI/CD

## Overview

This project demonstrates an end-to-end Machine Learning deployment workflow using FastAPI, Scikit-Learn, Azure DevOps, and Azure App Service.

A Linear Regression model is trained on a sample housing dataset and exposed through a REST API. The application is automatically built, tested, packaged, and deployed using a multi-stage Azure DevOps YAML pipeline.

## Features

- Linear Regression model using Scikit-Learn
- REST API built with FastAPI
- Automated model training
- Unit testing with Pytest
- Multi-stage Azure DevOps CI/CD pipeline
- Deployment to Azure App Service
- Development and Production deployment stages
- Swagger UI documentation

## Architecture

GitHub Repository
↓
Azure DevOps Pipeline
↓
Install Dependencies
↓
Train ML Model
↓
Run Unit Tests
↓
Create Deployment Artifact
↓
Deploy to Azure App Service
↓
Prediction API Available

## Technology Stack

- Python 3.11
- FastAPI
- Scikit-Learn
- Pandas
- Joblib
- Pytest
- Azure DevOps
- Azure App Service
- GitHub

## Project Structure

```
.
├── main.py
├── train.py
├── test_main.py
├── requirements.txt
├── azure-pipelines.yml
└── README.md
```

## Model Training

The model is trained using a simple housing dataset.

Input Feature:
- Area (sq.ft)

Target:
- House Price

Training is automated within the Azure DevOps pipeline.

## API Endpoints

### Health Check

GET /

Response:

```json
{
  "status": "healthy"
}
```

### Price Prediction

POST /predict

Request:

```json
{
  "area": 1200
}
```

Response:

```json
{
  "area": 1200,
  "predicted_price": 6276382
}
```

## CI/CD Pipeline

The Azure DevOps pipeline performs:

1. Dependency Installation
2. Model Training
3. Unit Testing
4. Artifact Packaging
5. Deployment to Development Environment
6. Deployment to Production Environment

## Testing

Run tests locally:

```bash
pytest
```

## Deployment

The application is deployed to Azure App Service using Azure DevOps YAML pipelines.

## Future Enhancements

- Replace synthetic dataset with a real-world housing dataset
- Add model performance metrics
- Containerize using Docker
- Implement approval gates before production deployment
- Add monitoring and logging

## Author

Sanjeev Sreedhar
