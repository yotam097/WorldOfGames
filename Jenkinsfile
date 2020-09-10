pipeline {
  agent any
  stages {   
    stage('Validate this is working') {
      steps {
        echo "Hello I'm alive"
        sh ''' echo "Hello I'm alive or not" '''
      }
    }
    stage('Run') {
      steps {
        sh ''' docker-compose up --build -d '''
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
