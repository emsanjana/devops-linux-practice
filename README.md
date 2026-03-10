# Learning DevOps

This repository contains DevOps practice work.

## Week 1 
- Navigated the Linux filesystem using cd, ls, pwd, and tree
- Created, renamed, deleted, and copied files and directories
- Viewed file contents using cat, less, more, head, and tail
- Managed permissions using chmod and ownership concepts
- Monitored processes using ps, top, and htop
- Checked system resources using df, du, and free
- Wrote basic Bash scripts
- Set up Git, GitHub, and SSH authentication

## Week 2

### Assignment1
- Created and worked with branches:
	feature/login-page
	feature/signup-page
	bugfix/css-align
- Performed basic commits on each branch using git add and git commit
- Merged feature and bugfix branches into main using git merge
- Added a remote GitHub repository and pushed all branches using git remote add and git push
- Documented all Git commands used in a GIT_COMMANDS.md file

### Assignment2
- Created a new branch (aws) and managed branch-specific changes
- Added an aws-services.md file documenting 5 commonly used AWS services
- Added an aws-usecase.md file describing a basic app deployment workflow.
- Installed Ansible and wrote a playbook to create a user, install nginx, and start the service.
- Installed Terraform and created a basic configuration defining a provider and a sample resource.

## Week 3

### Assignment1
- Installed JFrog Artifactory OSS locally.
- Accessed the Artifactory web interface and configured the system.
- Created repositories:
	Generic Local Repository.
	Maven Local Repository.
- Uploaded sample test files into the Generic repository.
- Documented the installation and configuration steps with screenshots in Markdown.

### Assignment2
- Installed Docker and verified the installation.
- Created a simple Dockerfile for a sample application.
- Built the Docker image locally.
- Ran the container locally.
- Implemented a multi-stage Docker build to reduce image size and improve efficiency.
- Documented all Docker commands used and explained the reasoning behind each step.

## Week 4 

### Assignment1
- Built a multi-container application using Docker Compose.
- Created an application consisting of:
	A Flask web application
	A PostgreSQL database
- The Flask application performs the following:
	Connects to the PostgreSQL database
	Creates a simple table
	Inserts a sample record into the table
	Retrieves and displays database data on the homepage (/)
	Created a proper project structure including:
	Application source code
	Dockerfile
	docker-compose.yml
- Configured docker-compose.yml.
- Documented it.

### Assignment2

- Set up a local Kubernetes cluster using Minikube.
- Deployed the same Flask + PostgreSQL application using Kubernetes.
- Created Kubernetes YAML configuration files for:
	PostgreSQL Deployment
	PostgreSQL Service
	Flask Application Deployment
	Flask Application Service
- Configured Kubernetes resources with:
	Proper labels and selectors
	Service discovery between application and database
	Network communication between pods
- Documented it.



## Tools Used

- Linux (Ubuntu)
- Bash scripting
- Git & GitHub
- Ansible
- Terraform
- JFrog Artifactory
- Docker
- DockerHub
- Maven
- Markdown Documentation
- Kubernetes
- Minikube
- Flask
- PostgreSQL
