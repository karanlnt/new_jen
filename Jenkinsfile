pipeline {
    agent any
    properties([pipelineTriggers([githubPush()])])

  stages {
    stage('Pull Code') {
      steps {
        git url: 'https://github.com/karanlnt/new_jen.git', branch: 'main'
      }
    }
    // Add more stages as needed
  }
}

    environment {
        IMAGE_NAME = "flask-ci-demo"
        CONTAINER_PORT = "1000"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/karanlnt/new_jen.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 1000:1000 $IMAGE_NAME'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
