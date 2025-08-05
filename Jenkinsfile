pipeline {
  agent any

  stages {
    stage('Clean Workspace') {
      steps { cleanWs() }
    }
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build --no-cache -t flask-ci-demo .'
      }
    }
    stage('Run Container') {
      steps {
        sh 'docker run --rm -d -p 4000:4000 flask-ci-demo'
      }
    }
  }
  post { always { cleanWs() } }
}
