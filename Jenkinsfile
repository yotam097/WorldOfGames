pipeline {
 node
 stages {
  stage('Checkout code') {
    echo "yotam"
  }
  stage('Build') {
    sh ''' docker build -t wogImage .'''
  }
  stage('Run') {
   steps {
   sh ''' docker-compose up '''
   }
  }
  stage('Test') {
   steps {
    sh ''' python ./e2e.py '''
   }
  }
  stage('Finalize') {
    sh ''' docker-compose down '''
  }
 }
}