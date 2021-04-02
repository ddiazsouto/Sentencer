pipeline {
    agent any
    stages{

        stage('Stage 1: Build/search'){
            steps{
                sh "cd Service1"
                sh "docker build -t Service1 ."
                sh "cd .."
            }
        }

        stage('Stage 2: Test/show'){
            steps{
                sh "docker ps"
            }
        }

        stage('Stage 3: Deploy/do'){
            steps{
                sh "docker run -d -p 5500:5500 --name ser1 service1 "
            }
        }
    }
}