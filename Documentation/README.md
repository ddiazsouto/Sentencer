# Sentencer
Sentencer is an ice breaker

## --Requirements
The modules used by python are

flask       - to render the main frame of the app
requests    - for services to interact through GET and POST requests
pymysql     - personal choice to interact with the database

The following modules have been using for testing:

mock        
flask_testing 
pytest
pytest-cov


## --Test Analysis
<br>
I have followed a TDD approach in building my aplication, which saved plenty of time in finding errors without having to manually load the app. Testing has been done in the following areas:

### <b>We started testing that the pages could load and thus we would get a return statement with a status of 200 from the get request.</b>
### <b>This covers Service 1 Service 2 Service 3 and Service 4</b>
<br>
This was very helpful particularly in the late stages as I could test the aplication before pushing it to GitHub and thus avoided waiting to see the problem through Jenkins.

### <br> <b>Service 4 Has used mock in the testing, this helps to check that the json is parsed propperly by the page and that is can be used propperly by the page logic.</b>
<br>

We are missing more thorough testing mainly in the classes and functions that were created for the module



## --Tech Stack used
<br>
<p>
A MySQL database running in GCP for the app to connect <br>
Infrastructure of the app will be in Python<br>
Git as VSC<br>
A fully integrated pipeline using Jenkins<br>
Ansible as Configuration Manager<br>
The cloud provider of choice was GCP<br>
The containerization tool used was Docker, orchestrated with Docker Swarm<br>
Further automation was achieved with docker-compose<br>
nginx has served both as a reverse proxy and a load balancer<br>
</p>

## --Trello Board



## --Database


## --Software Architeceture


# Risk Analysis
<hr>

The readme must be exhaustive, the main structure will be written.
-Requirements
-Test analysis
-Technologies used
-Database

This needs to be done
-Architecture

## Issues

I run into issues trying to put Jenkins in a container, it was solver by installing it in the machine

The pipeline was given preference over the app, to align with Devops practices and improve CI


Second step was to build the app, I can't seem to be able to use json requests

Worked out the tests after a while



| Description |Evaluation| Likelihood  | Impact Level | Responsability |  Response  |  Control Measures  
| :---        | :----:   |  :----:     |  :----:      |  :----:        |  :----:    |---:
| The project is missing basic functionality on the day of the project | I had issues with connecting containers, machines or deploying| Medium  | Critical | Mine |    |  Work on the basic foundation of the app early on and build on top 
|The app behaves differntly after integration than in development environment |	The project gives new problems| Medium/high |	Very High | me	| Undo last changes and detect the issue before deploying |	There should be a CI pipeline before the app has any new features or any features at all so we can integrate frequently with Jenkins and be able to detect problematic changes as they happen rather than a bunch at the time
|The aplication code has bugs when pushed|	The developer didn't realise mistakes in coding and has pushed to a CD pipeline| Moderate |	Very High | me or collaborators	| Propper response should be as automated as possible |	The first stage in the Jenkins Pipeline perform tests wo we find the issues early on and way before building any changes or deploying them
| The connection between elements of the app falls down | the configuration that previously worked is no longer holding the app together | Medium/Low  | High | VM/Docker images/Jenkins pipelina |  Use a redundant Microservices aplication allocated for this purpose  |  Create a Redundant application as a back up
|The Microserviced app is not finished on time|	Issues when deploying at the end| Moderate |	Very High | me/project manager	| Show the finished bits |	Have a working pipeline and infrastructure early on so we can test as we deploy (CI)
|There are problems in a local network i.e. US west|	GCP network system is down| Extremely low |	Very High | GCP	| Make sure load balancers are redirecting traffic to other regions |	Create part of the Swarm in different zones
|Last changes in the source code make app unstable| Source code has changed	| Moderate |    Very High | Me and/or collaborators	| Git Revert to last stable release|	Make sure CVS has been used propperly during development


## Acknowledgements and contributions

<br>
I aknowledge QA community as my main source of reference for the technologies and methodologies used. The same goes for Dara Oladapo and Harry Volker who provided the knowledge necessary to build this aplication
<br><br>
<p>A special mention must be made to all the colleagues of my cohort who have shown a truly Open Source mentality providing support at any time online to those who needed, and sharing their experience and knowledge for the community to benefit from it. </p>