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
                sh "pip3 install pytest"
                sh "pytest ./server/tests/test_server.py"
                sh "pytest ./animal_api/tests/test_animal.py"
                sh "pytest ./country_api/tests/test_country.py"
                sh "pytest ./winner_api/tests/test_winner.py"                        
            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy --compose-file docker-compose.yaml A"                
            }
        }
    }    
}
