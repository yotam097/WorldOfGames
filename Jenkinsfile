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
        bat ''' docker-compose up --build -d '''
      }
    }
    stage('Test') {
      steps {
        bat ''' python ./e2e.py '''
      }
    }
    stage('Finalize') {
      steps {
        bat ''' docker-compose down '''
      }
    }
  }
}
