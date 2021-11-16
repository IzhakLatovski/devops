pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="046432083464"
        AWS_DEFAULT_REGION="eu-west-2"
        IMAGE_REPO_NAME="portfolio"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {
        
         stage('Logging into AWS ECR') {
            steps {
                echo "-----------Started----------------------------------------------------------------------------------------------------"
                sh "docker login -u AWS --password-stdin \$(aws ecr get-login-password --region eu-west-2) 046432083464.dkr.ecr.eu-west-2.amazonaws.com"

                echo "-----------Ended----------------------------------------------------------------------------------------------------"                 
            }
        }
        
    //     stage('Cloning Git') {
    //         steps {
    //             checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/sd031/aws_codebuild_codedeploy_nodeJs_demo.git']]])     
    //         }
    //     }
  
    // // Building Docker images
    // stage('Building image') {
    //   steps{
    //     script {
    //       dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
    //     }
    //   }
    // }
   
    // // Uploading Docker images into AWS ECR
    // stage('Pushing to ECR') {
    //  steps{  
    //      script {
    //             sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
    //             sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
    //      }
    //     }
    //   }
    }
}
