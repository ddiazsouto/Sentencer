pipeline {
    agent any
    stages{

        stage('Stage 0: Clean/Set-up'){
            steps{

                sh "echo Here-we-go"

            }
        }

        stage('Stage 1: Build/search'){
            steps{

                sh "docker-compose build"

            }
        }

        stage('Stage 2: Test/show'){
            steps{
                sh "docker ps && docker images"
            }
        }

        stage('Stage 3: Deploy/do'){
            steps{

                sh "docker-compose up -d"

            }
        }
    }
}