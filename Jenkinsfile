pipeline {
  agent any
  stages {   
    stage('Run') {
      steps {
        sh ''' docker-compose up '''
      }
    }
    stage('Test') {
      steps {
        sh ''' python3 ./e2e.py '''
      }
    }
    stage('Finalize') {
      steps {
        echo 'yotam'
      }
    }
  }
}
