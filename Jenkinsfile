pipeline {
 node
 stages {
  stage('Checkout code') {
   steps {
    echo "yotam"
   }
  }
  stage('Build') {
   steps {
    sh ''' docker build -t wogImage .'''
   }
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
    echo "yotam"
  }
 }
}