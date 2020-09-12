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
        sh ''' python ./e2e.py '''
      }
    }
    stage('Finalize') {
      steps {
        echo "yotam"
      }
    }
  }
}
