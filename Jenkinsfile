pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/MohamadAlturky/bpmn-generator.git'
        BRANCH = 'main'
        CREDENTIALS_ID = 'github'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}", credentialsId: "${CREDENTIALS_ID}"
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    sh "docker-compose up --build -d"
                }
            }
        }
    }
}