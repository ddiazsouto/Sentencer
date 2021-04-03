pipeline {
    agent any
    stages{

        stage('Stage 0: Clean/Set-up'){
            steps{

                sh "docker rm -f $(docker ps -aq)"

            }
        }

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
                sh "docker run -d -p 5500:5500 --name ser1 --network mynet service1"
                sh "docker run -d -p 5000:5000 --name ser2 --network mynet service2"
                sh "docker run -d -p 5005:5005 --name ser3 --network mynet service3"
                sh "docker run -d -p 5050:5050 --name ser4 --network mynet service4"
                sh "docker ps"
            }
        }
    }
}