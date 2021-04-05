pipeline {
    agent any
    stages{

        stage('Stage 0: Set-up'){
            steps{

                sh "echo Here-we-go"

            }
        }

        stage('Stage 1: Build'){
            steps{

                sh "docker-compose build"
                sh "docker-compose up -d"

            }
        }

        stage('Stage 2: Test'){
            steps{
                sh "docker ps && docker images"
            }
        }

        // stage('Stage 3: Deploy'){
        //     steps{

                

        //     }
        // }
    }
}