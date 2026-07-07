pipeline {
    agent any

    stages {
        stage('env check') {
            steps {
                sh 'which python3 || true'
                sh 'which pip3 || true'
            }
        }

        stage('repo check') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('install dependencies') {
            steps{
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('testing') {
            steps {
                sh 'echo "========Testing Start========"'
                sh 'pytest'
            }
        }
    }
}
