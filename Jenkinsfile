pipeline {
    agent any

    stages {
        stage('repo check') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('git info') {
            steps {
                sh 'git log --oneline -5'
            }
        }

        stage('build') {
            steps {
                sh 'echo "Building project..."'
            }
        }

        stage('testing') {
            steps {
                sh 'echo "Testing project"'
            }
        }
    }
}
