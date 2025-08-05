pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        // your build steps here
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}
