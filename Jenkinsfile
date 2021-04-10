pipeline {
    agent any

    environment{
            SOME = 'AA'
            PASSWD = credentials('DOCKER_HUB_PASSWD')
            
    }

    stages{

        stage('Stage 0: Test'){
            steps{
               
                sh "bash testing.sh"

            }
        }

        stage('Stage 1: Build'){
            steps{

                sh "docker-compose build"
                sh "docker-compose up -d"

            }
        }

        stage('Stage 2: Push'){
            steps{
                sh "docker login -u 'ddiazsouto' -p 'Buddhassister22' docker.io"   //   
                sh "docker ps && docker images"         // Here we push to DockerHub or Nexus so in the Deployment phase we can pull from there
                sh "docker-compose push "               // as it is best practice
              
            }                                            
        }
        stage('Stage 3: Config'){
            steps{                          

                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml "
            }
        }


        stage('Stage 4: Deploy'){                        //     And here we pull from Dockerhub instead of using local images
            steps{

                sh "docker stack deploy --compose-file docker-compose.yaml Sentencer"
                
            }
        }
    }
}