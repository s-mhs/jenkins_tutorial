pipeline {
    agent any

    stages {
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