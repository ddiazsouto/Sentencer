# Sentencer
Sentencer is an ice breaker

## --Requirements
flask
requests



## --Test Analysis


## --Tech Stack used


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
| The connection between elements of the app falls down | the configuration that previously worked is no longer holding the app together | Medium/Low  | High | VM/Docker images/Jenkins pipelina |  Use a redundant Microservices aplication allocated for this purpose  |  Create a Redundant application as a back up
|The Microserviced app is not finished on time|	Issues when deploying at the end| Moderate |	Very High | me/project manager	| Show the finished bits |	Have a working pipeline and infrastructure early on so we can test as we deploy (CI)
|Description|	Evaluation| Very low |	High | GCP/me	| Response |	Control Measures
