pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Saikumarbadham/playwright-python-framework/blob/main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}