pipeline {
    agent any
    // environment {
    //     AWS_ACCOUNT_ID="046432083464"
    //     AWS_DEFAULT_REGION="eu-west-2"
    //     IMAGE_REPO_NAME="portfolio"
    //     IMAGE_TAG="latest"
    //     REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    // }

    // AKIAQVT4RLYEE3VX6BUV
    // l5d7fAgL4OollqSJfhnEsoc2qMaJ72xets6RuquJ
   
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
