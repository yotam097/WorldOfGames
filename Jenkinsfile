pipeline {
  agent any
  stages {   
    stage('Repo pull') {
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
        sh ''' winpty docker exec -it worldofgames_web_1 python e2e.py '''
      }
    }
    stage('Finalize') {
      steps {
        sh ''' docker-compose down '''
      }
    }
  }
}
