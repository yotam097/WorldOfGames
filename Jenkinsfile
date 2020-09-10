pipeline {
    agent any
    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        stage('Build') {
            steps {
                docker build -t wogImage .
            }
        }
        stage('Run') {
            steps {
                docker-compose up
            }
        }
        stage('Test') {
            steps {
                python ./e2e.py
            }
        stage('Finalize') {
            steps {
                docker-compose down
            }
        }
    }
}
