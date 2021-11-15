pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "*******building app...*******"
                // sh "docker-compose build"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}