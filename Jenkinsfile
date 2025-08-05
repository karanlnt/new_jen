pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/karanlnt/new_jen.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-docker .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                  docker rm -f flask-container || true
                  docker run -d -p 4000:4000 --name flask-container flask-docker
                '''
            }
        }
    }
}
