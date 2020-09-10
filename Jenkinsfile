pipeline {
  agent any
  stages {
    stage('Checkout code') {
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