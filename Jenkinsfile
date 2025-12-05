pipeline {
    agent any
    
    environment {
        // Change this to your DockerHub username
        DOCKER_IMAGE = "codesraza/devsolutions-app" 
        TAG = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // Building from the app directory
                    sh "docker build -t ${DOCKER_IMAGE}:${TAG} ./app"
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    echo 'Pushing to Registry...'
                    // Assumes you are logged in to docker on the agent
                    // sh "docker push ${DOCKER_IMAGE}:${TAG}" 
                    echo "Skipping push for local lab speed, simulating push..."
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    // Updates the image tag in deployment on the fly
                    sh """
                    kubectl set image deployment/devsolutions-deployment devsolutions-app=${DOCKER_IMAGE}:${TAG} --record
                    """
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                sh "kubectl rollout status deployment/devsolutions-deployment"
            }
        }
    }
}