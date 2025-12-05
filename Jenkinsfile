pipeline {
    agent any

    environment {
        // We use a local tag so we don't need to push to DockerHub for this lab
        IMAGE_NAME = "devsolutions-app"
        TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    // This builds the image on your Mac's Docker daemon
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ./app"
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo "Updating Kubernetes..."
                    // Updates the running deployment with the new image tag
                    // "devsolutions-deployment" must match your YAML file name from Phase 2
                    // "devsolutions-app" must match the container name in your YAML
                    sh "kubectl set image deployment/devsolutions-deployment devsolutions-app=${IMAGE_NAME}:${TAG}"
                }
            }
        }

        stage('Verify') {
            steps {
                script {
                    sh "kubectl rollout status deployment/devsolutions-deployment"
                    echo "Deployment Successful!"
                }
            }
        }
    }
}