pipeline {
    agent any

    stages {
        stage('docker build') {
            steps {
                bat 'docker build -t mlopsapi .'
                bat 'docker run -d -p 5000:5000 mlopsapi'
            }
        }

    }
}
