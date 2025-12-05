pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsolutions-app"
        TAG = "${BUILD_NUMBER}"
        // Define a temp path for the modified config
        KUBECONFIG_FIX = "${WORKSPACE}/kube_config_fixed" 
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ./app"
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo "Fixing Kubeconfig for Mac Docker..."
                    
                    // 1. Copy the mounted config to workspace so we don't break the original
                    sh "cp /root/.kube/config ${KUBECONFIG_FIX}"
                    
                    // 2. Replace localhost/127.0.0.1 with host.docker.internal
                    sh "sed -i 's/127.0.0.1/host.docker.internal/g' ${KUBECONFIG_FIX}"
                    sh "sed -i 's/localhost/host.docker.internal/g' ${KUBECONFIG_FIX}"
                    
                    // 3. Disable TLS verification (Certificate usually doesn't match host.docker.internal)
                    sh "kubectl --kubeconfig=${KUBECONFIG_FIX} config set-cluster docker-desktop --insecure-skip-tls-verify=true"

                    echo "Deploying..."
                    // 4. Run the deploy command using the FIXED config
                    sh "kubectl --kubeconfig=${KUBECONFIG_FIX} set image deployment/devsolutions-deployment devsolutions-app=${IMAGE_NAME}:${TAG}"
                }
            }
        }

        stage('Verify') {
            steps {
                script {
                    // Use the fixed config for verification too
                    sh "kubectl --kubeconfig=${KUBECONFIG_FIX} rollout status deployment/devsolutions-deployment"
                    echo "Deployment Successful!"
                }
            }
        }
    }
}