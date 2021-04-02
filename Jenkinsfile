pipeline {
    agent any
    stages{

        stage('Stage 1: Build/search'){
            steps{
                sh "docker build -t service1 ./Service1"
                sh "docker build -t service2 ./Service2"
                sh "docker build -t service3 ./Service3"
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
                sh "docker run -d -p 5000:5000 --name ser2 service2"
                sh "docker run -d -p 5005:5005 --name ser3 service3"
                sh "docker ps"
            }
        }
    }
}