# DevOps Kubernetes Challenge

A small DevOps project demonstrating containerization and deployment of a Flask API on Kubernetes using Docker and Kind.

## Project Overview

The goal of this project was to containerize a Flask API and deploy it on a local Kubernetes cluster.

The application exposes a `/health` endpoint that returns:

```json
{"status":"healthy"}

## Architecture

```text
                    Kind Kubernetes Cluster
                           |
                           |
                    ClusterIP Service
                  devops-challenge-api
                       Port 80
                           |
              +------------+------------+
              |                         |
              v                         v
        API Pod 1                   API Pod 2
        Flask :5000                Flask :5000