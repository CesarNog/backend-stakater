# Stakater Hiring Task - Backend Repository

## Requirements

 - [minikube](https://minikube.sigs.k8s.io/docs/start/)
 - [docker](https://docs.docker.com/get-docker/)
 - [kubernetes CLI](https://kubernetes.io/docs/tasks/tools/)

## Setup

 1. Start docker desktop (in case you are using Windows)
 2. Run `minikube start` to start minikube locally 
 3. Run `kubectl get ingresses,services,pods -A` to get the list of services running locally on minikube

## Run Commands

 1.  Build docker image: 
`docker build -f Dockerfile -t hello-python-frontend:latest .`
 2.  Apply Kubernetes Deployment file: 
`kubectl apply -f ./kubernetes/backend-deployment.yaml`
 3. Expose the port 8080 of backend API to be reachable by the frontend
  `kubectl expose deployment hello-python-backend --type=NodePort --port=8080`
 4. Run the command below to open the hello-python-backend on minikube
  `minikube service hello-python-backend-service`

