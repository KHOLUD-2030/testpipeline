pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your GitHub repository
                git branch: 'main', url: 'https://github.com/KHOLUD-2030/testpipeline.git'
            }
        }
        stage('Build and Test') {
            steps {
                // Run the Python script
                sh 'python3 car_parts.py'
            }
        }
    }
}
