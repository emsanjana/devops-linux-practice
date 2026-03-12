pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/emsanjana/devops-linux-practice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-jenkins-build docker-compose-flask-postgres'
            }
        }

        stage('Verify Build') {
            steps {
                sh 'docker images'
            }
        }

    }
}
