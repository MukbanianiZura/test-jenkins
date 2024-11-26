pipeline {
    agent any

    environment {
        def MY_ENV_VAR = 'some_value'
    }

    stages{
        stage('Checkout'){
            steps{
                script {
                    def GIT_REPO_URL = 'https://github.com/MukbanianiZura/test-jenkins'

                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[$url: GIT_REPO_URL]],
                        extentions: [[$class: 'CleanBeforeCheckout'], [$class: 'CloneOption', noTags: false, shallow: true, depth: 1]]
                    ])
                }
            }
        }

        stage('Build'){
            steps{
                sh '''
                    ls
                    echo "In a Build Step"
                '''
            }
        }

        stage('Test'){
            steps{
                sh 'echo "In Test Step"'
            }
        }

        stage ('Deploy'){
            steps{
                sh 'echo "Value of ENV variable is $"""'
            }
        }
    }

    post {
        success {
            echo "Pipeline success"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}