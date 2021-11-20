pipeline {
    agent any

    stages {
        stage('Pull') {
            steps {
                sh 'rm -r *'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t portfolio-flask-image .'
                script {
                    dockerImage = docker.build "046432083464.dkr.ecr.eu-west-2.amazonaws.com/portfolio" + ":$BUILD_NUMBER"
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Testing.'
            }
        }

        stage('Deploy') {
            steps {
                script{
                docker.withRegistry("https://" + "046432083464.dkr.ecr.eu-west-2.amazonaws.com/portfolio", "ecr:eu-west-2:" + "portfoliocredentials") {
                    dockerImage.push()
                }
            }
            }
        }

    }
}
