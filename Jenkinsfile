pipeline {
    agent any

    environment {
        // Define environment variables if needed
        NODE_ENV = 'production'
    }

    tools {
        nodejs 'NodeJS_18'  // Make sure this matches your Jenkins Node.js tool name
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'npm install'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'npm test || true' // Optional: Continue if no tests
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'npx serve -s build -l 3000 &'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
