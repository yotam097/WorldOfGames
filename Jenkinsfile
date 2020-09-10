pipeline {
 node
 stages {
  stage('Checkout code') {
    sh ''' checkout scm '''
  }
  stage('Build') {
    sh ''' docker build -t wogImage .'''
  }
  stage('Run') {
   sh ''' docker-compose up '''
  }
  stage('Test') {
    sh ''' python ./e2e.py '''
  }
  stage('Finalize') {
    sh ''' docker-compose down '''
  }
 }
}
