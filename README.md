DevOps Monitoring & Automation Suite

📌 Project Overview

This repository contains a suite of Python-based utilities designed to demonstrate core DevOps principles: Monitoring, Automation, and Containerization. 

🛠 Project Components

1. Infrastructure Health Sentinel (monitor.py)

Purpose: A resource tracking simulation that monitors system load across various servers.

Logic: Uses lists and conditional thresholds to trigger alerts when simulated CPU/Memory usage exceeds safety limits.

2. LogInsight Sentinel (log_analyzer.py)

Purpose: An automated log parsing tool that scans server.log files for error signatures.

DevOps Value: Demonstrates the ability to transform raw log data into actionable alerts, a critical skill for Site Reliability Engineering (SRE).

🚀 DevOps Integration

GitHub Actions (Continuous Integration)

The project is integrated with GitHub Actions via .github/workflows/python-ci.yml.

Function: Automatically performs a syntax check and linting on every code push to ensure repository health.

How to view: Click the "Actions" tab in this GitHub repository to see the automation history.

Docker (Containerization)

The application is containerized to ensure "run-anywhere" consistency.

Build the Image: docker build -t monitoring-suite .

Run the Container: docker run monitoring-suite

Infrastructure as Code (Terraform)

The main.tf file demonstrates the ability to provision cloud infrastructure (AWS S3) for secure log storage, following the principle of Security Compliance by blocking public access.

📊 Technical Skills Demonstrated

Python: Automation scripting, file I/O, and data structure management.

CI/CD: Automated workflows using GitHub Actions.

Cloud Security: IAM and S3 bucket policy management via Terraform.

Linux: Command-line proficiency and environment configuration.
