pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "*************************building app...*************************"
                sh "cd ./jenkins"
                sh "pwd"
                sh "docker-compose build"
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