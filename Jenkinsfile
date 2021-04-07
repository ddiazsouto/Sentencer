pipeline {
    agent any
    stages{

        // stage('Stage 0: Test'){
        //     steps{

        //         //sh "pytest"

        //     }
        // }

        stage('Stage 1: Build'){
            steps{

                sh "docker-compose build"
                sh "docker-compose up -d"
                // docker-compose push   <<-need to look into it

            }
        }

        stage('Stage 2: Check'){
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