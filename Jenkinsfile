pipeline {
    agent{
        lable'windows'
    }

    parameters{
        choice(
            name:"browser",
            choices:['chrom','edge','firefox'],
            description:"done"

        )
        choice(
            name:"tags",
            choices:["smoke","regression"]
        )
        string(
            name:"environment",
            defaultValue: 'test',
        )
        booleanParam(
            name: 'RUN_TESTS',
            defaultValue: true,
        )
    }
    stages{
        stage('checkout'){
            checkout sm
        }
        stage('Install dependencies'){
            steps{
                bat 'python -m pip install'
                sh 'python -m pip install -r requirements.txt'
            }

        }
        stage('playwright'){
            bat 'python -m playwright install chromium '

        }
        stage('test run'){
            when {
                expression{params.tags}
            }
            steps{
                bat 'pytest e2e/ --browser chromium ${params.tags}'
            }
            
        }
        stage('deploy'){
            echo 'Deploying application'
        }
    }
    post{
        always{
            publishHTML(target:[
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Playwright Test Report',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }
    }
}