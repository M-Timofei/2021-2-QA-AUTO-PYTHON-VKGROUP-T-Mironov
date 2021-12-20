properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    environment {
        DOCKER_COMPOSE = "/usr/bin/docker-compose"
    }

    stages {

        stage("Testing myapp") {
            steps {
                withEnv(["PATH+EXTRA=$DOCKER_COMPOSE"]) {
                    sh "cd $WORKSPACE/testFinalProject/QA-Python-Final-Project"
                    dir ("$WORKSPACE/testFinalProject/QA-Python-Final-Project") {
                        sh "docker-compose up --abort-on-container-exit"
                    }
                }
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'alluredir']]
            ])
            script {
                withEnv(["PATH+EXTRA=$DOCKER_COMPOSE"]) {
                    sh "cd $WORKSPACE/testFinalProject/QA-Python-Final-Project"
                    dir("$WORKSPACE/testFinalProject/QA-Python-Final-Project") {
                        sh 'docker-compose down'
                    }
                }
            }
            cleanWs()
        }
    }
}