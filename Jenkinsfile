pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-ci-demo'   // Change to your DockerHub repo
        CONTAINER_PORT = '4000'
        CONTAINER_NAME = 'exciting_meitner'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/karanlnt/new_jen.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Build Project') {
            steps {
                sh 'npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Push Docker Image') {
            when {
                expression { return env.DOCKER_USERNAME != null && env.DOCKER_PASSWORD != null }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                sh '''
                    CONTAINER_ID=$(docker ps -q --filter "name=$CONTAINER_NAME")
                    if [ ! -z "$CONTAINER_ID" ]; then
                        echo "Stopping old container $CONTAINER_NAME"
                        docker stop $CONTAINER_NAME
                        docker rm $CONTAINER_NAME
                    fi
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker run -d -p ${CONTAINER_PORT}:3500 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}
