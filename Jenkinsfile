pipeline {
    agent any

    environment {
        // REPLACE THIS WITH YOUR USERNAME
        DOCKER_IMAGE = 'YOUR_DOCKERHUB_USERNAME/devops-assessment'
        // You must create this ID in Jenkins credentials
        DOCKER_CREDS_ID = 'docker-hub-login' 
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push to Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDS_ID, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh "docker login -u $USER -p $PASS"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    // This assumes kubectl is set up on the Jenkins machine
                    sh 'kubectl apply -f kubernetes/'
                    // Force a restart to pick up the new image
                    sh 'kubectl rollout restart deployment/web-app-deployment'
                }
            }
        }
    }
}