pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {        
        }
        stage('Build') {
            steps {
                sh "docker-compose up -d --build"                                        
            }
        }
        stage('Test') {
            steps {
                sh "pip3 install pytest"
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