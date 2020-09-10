pipeline {
  agent any
  stages {
    stage('Checkout code') {
     stage('Validate this is working') {
      steps {
        echo "Hello I'm alive"
        sh ''' echo "Hello I'm alive or not" '''
      }
    }
      steps {
        sh ''' git checkout scm '''
      }
    }
    stage('Build') {
      steps {
        sh ''' docker build -t wogImage . '''
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
      steps {
        echo 'yotam'
      }
    }
  }
}
