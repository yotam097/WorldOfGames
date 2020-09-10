pipeline {
  agent any
  stages {   
    stage('Build') {
      steps {
        sh ''' docker build -t Dockerfile . '''
      }
    }
    stage('Run') {
      steps {
        sh ''' docker run Dockerfile '''
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
