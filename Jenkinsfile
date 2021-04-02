pipeline {
    agent any
    stages{

        stage('Stage 1: Build/search'){
            steps{
                sh "docker build -t service1 ./Service1"
                sh "docker build -t service2 ./Service2"
                sh "docker build -t service3 ./Service3"
                sh "docker build -t service4 ./Service4"
            }
        }

        stage('Stage 2: Test/show'){
            steps{
                sh "docker ps && docker images"
            }
        }

        stage('Stage 3: Deploy/do'){
            steps{
                sh "docker run -d -p 5500:5500 --name ser1 service1 "
                sh "docker ps"
            }
        }
    }
}