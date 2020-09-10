pipeline {
  agent any
  stages {   
    stage('Build') {
      steps {
        sh ''' docker build -t dockerfiletest . '''
      }
    }
    stage('Run') {
      steps {
        sh ''' docker run dockerfiletest '''
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
