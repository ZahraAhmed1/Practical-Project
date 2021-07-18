pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {
        stage('Install Docker/Docker Compose') {
            steps {
                sh "curl https://get.docker.com/ | sudo bash"
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose up -d --build"
                sh "docker exec animal_duel_server python3 create.py"
                sh "docker swarm init"                
            }
        }
        stage('Test') {
            steps {
                sh "cd server && pytest"
                sh "cd animal_api && pytest"
                sh "cd country_api && pytest"
                sh "cd winner_api && pytest"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy --compose-file docker-compose.yaml A"
            }
        }
    }
}