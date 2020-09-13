pipeline {
  agent any
  stages {   
    stage('Git clone') {
      steps {
        git 'https://github.com/yotam097/WorldOfGames.git'
      }
    }
    stage('Run') {
      steps {
        sh ''' docker-compose up -d '''
      }
    }
    stage('Test') {
      steps {
        sh ''' python ./e2e.py '''
      }
    }
    stage('Finalize') {
      steps {
        sh ''' docker-compose down '''
      }
    }
  }
}
