pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps { cleanWs() }
        }
        stage('Checkout Code') {
            steps { checkout scm }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t flask-docker .'
            }
        }
        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f flask-container || true
                    docker run -d -p 4000:4000 --name flask-container flask-docker
                '''
            }
        }
    }

    post {
        always { cleanWs() }
    }
}
