pipeline {
  agent any

  environment {
    REGISTRY         = "docker.io/your‑dockerhub‑username"
    IMAGE_NAME       = "${REGISTRY}/simple‑flask‑ci"
    DOCKERHUB_CRED  = credentials('dockerhub‑creds')
    GIT_CRED        = credentials('github‑creds')
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    disableConcurrentBuilds()
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/your‑username/simple‑flask‑ci.git', credentialsId: GIT_CRED
      }
    }

    stage('Build & Test Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
        script {
          dockerImage.inside {
            sh 'python -m pip install pytest'
            writeFile file: 'test_app.py', text: '''
import pytest
from app import app

def test_root():
    resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert b"Hello from Flask" in resp.data
'''
            sh 'pytest --maxfail=1 --disable-warnings -q'
          }
        }
      }
      post {
        failure {
          error "Tests failed – aborting CI"
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry("", DOCKERHUB_CRED) {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          sh '''#!/bin/bash
            docker pull ${IMAGE_NAME}:latest
            docker stop flask-ci-demo || true
            docker rm flask-ci-demo || true
            docker run -d --name flask-ci-demo -p 5000:5000 ${IMAGE_NAME}:latest
          '''
        }
      }
    }
  }

  post {
    success {
      echo "✅ Build #${env.BUILD_NUMBER} deployed successfully"
    }
    cleanup {
      cleanWs()
      script {
        try {
          sh "docker image prune -f"
        } catch (err) { }
      }
    }
}
