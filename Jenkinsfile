pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat 'python -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'python -m pytest --junitxml=reports\\junit.xml --html=reports\\pytest-report.html --self-contained-html --alluredir=reports\\allure-results --output=reports\\test-results --screenshot=only-on-failure --video=retain-on-failure --tracing=retain-on-failure'
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml', allowEmptyResults: true
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'pytest-report.html',
                reportName: 'Pytest HTML Report'
            ])
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
            allure([
                commandline: 'Allure',
                includeProperties: false,
                reportBuildPolicy: 'ALWAYS',
                reportName: 'Allure Report',
                results: [[path: 'reports/allure-results']]
            ])
        }
    }
}