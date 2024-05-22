pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your GitHub repository
                git branch: 'main', url: 'https://github.com/KHOLUD-2030/testpipeline.git'
            }
        }
        stage('Build') {
            steps {
                // Run the Python script (Build step can be more complex in real scenarios)
                sh 'python3 car_parts.py'
            }
        }
        stage('Test') {
            steps {
                // Run unit tests
                sh 'python3 -m unittest discover -s . -p "test_*.py"'
            }
        }
    }
    post {
        always {
            // Specify the correct path to your test report files
            junit '**/test-reports/*.xml'
        }
    }
}
