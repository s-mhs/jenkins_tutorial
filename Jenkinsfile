pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/s-mhs/jenkins_tutorial'
            }
        }

        stage('compile') {
            steps {
                sh 'cc -o main hello.c'
            }
        }
    }

    post {
        success {
            echo 'compiled main successfully.'
        }

        failure {
            echo 'compilation failed.'
        }
    }
}