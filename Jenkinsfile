pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        DATABASE_URI=credentials('DATABASE_URI')
    }
    stages {        
        stage('Build') {
            steps {
                sh "docker-compose build"       
            }
        }
        stage('Test') {
            steps {
                sh "pip3 install pytest flask flask_testing flask_sqlalchemy requests_mock pymysql"
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
