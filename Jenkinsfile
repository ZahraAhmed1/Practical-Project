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
                sh "docker-compose build"       
            }
        }
        stage('Test') {
            steps {
                sh "pip3 install pytest flask flask_testing flask_sqlalchemy requests_mock"
                sh "python3 -m pytest ./server"
                sh "python3 -m pytest ./animal_api"
                sh "python3 -m pytest ./country_api"
                sh "python3 -m pytest ./winner_api"                        
            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy --compose-file docker-compose.yaml A"                
            }
        }
    }    
}
