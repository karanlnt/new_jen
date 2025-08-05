pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/karanlnt/new_jen.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-docker .'
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                script {
                    // Stop and remove any container using port 4000
                    sh '''
                        CONTAINER_ID=$(docker ps -q --filter "publish=4000")
                        if [ ! -z "$CONTAINER_ID" ]; then
                            docker stop $CONTAINER_ID
                            docker rm $CONTAINER_ID
                        fi
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 4000:4000 --name flask-container flask-docker'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
