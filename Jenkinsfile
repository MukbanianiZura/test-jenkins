pipeline{
    agent any 
    environment{
        RELEASE = '20.04'
    }

    stages{
        stage('Build') {
            agent any
            environment {
                LOGLEVEL = 'INFO'
            }
            steps{
                echo "Building release ${RELEASE} with level ${LOGLEVEL}"
            }
        }
        stage('Test') {
            steps{
                echo "Testing release ${RELEASE} with log level ${LOGLEVEL}"
            }
        }
    }
}