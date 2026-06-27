\# Automated Data Pipeline using Terraform, Docker, LocalStack \& GitHub Actions



\## Project Overview



This project demonstrates a complete DataOps workflow by provisioning AWS infrastructure with Terraform, running a Python ETL application inside Docker, emulating AWS services using LocalStack, and automating everything through GitHub Actions.



\---



\## Architecture



GitHub Actions



↓



Terraform



↓



LocalStack (S3 Bucket)



↓



Python ETL (Docker)



↓



Processed CSV stored in S3



\---



\## Folder Structure



```

.

├── .github/

│   └── workflows/

│       └── main.yml

├── infrastructure/

│   ├── main.tf

│   ├── variables.tf

│   └── outputs.tf

├── src/

│   ├── etl\_script.py

│   └── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── .dockerignore

├── .env.example

└── README.md

```



\---



\## Local Setup



```bash

docker compose up -d

```



Initialize Terraform



```bash

cd infrastructure

terraform init

terraform apply -auto-approve

```



Build Docker image



```bash

docker build -t etl-app .

```



Run ETL



```bash

docker run --network host \\

\-e AWS\_ENDPOINT\_URL=http://localhost:4566 \\

\-e S3\_BUCKET\_NAME=etl-pipeline-bucket \\

etl-app

```



\---



\## CI/CD



On every push to the main branch GitHub Actions:



\- Initializes Terraform

\- Creates the S3 bucket

\- Uploads sample data

\- Builds Docker image

\- Runs the ETL

\- Verifies processed/output.csv exists



\---



\## Technologies



\- Terraform

\- Docker

\- LocalStack

\- Python

\- Pandas

\- Boto3

\- GitHub Actions



\---

