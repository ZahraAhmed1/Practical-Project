pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        DATABASE_URI='mysql+pymysql://root:flask@10.11.112.2:3306/animalduel'
    }
    stages {        
        stage('Build') {
            steps {
                sh "docker rm -vf $(docker ps -a -q)"
                sh "docker rmi -f $(docker images -a -q)"
                sh "docker system prune"
                sh "docker-compose up -d --build"            
                sh "docker-compose push"                                      
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
