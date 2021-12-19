# ProximaCentauri
This is the Repo for cohort 2 trainees.

### Web Health Stack Project (Sprint1: 13Dec-17Dec)
In this project we will monitor the url resorce /website and check whether the mentioned host is avaible and measure latency. we will use lambda service. This service will measures and write the availblity and latency into cloud watch service. If the latency value rises from thresh hold then Cloud watch alarm arises alarm. 
When alarm rised , SNS Topic service will send notifications to the subscribers. Notifications may be in the form of email and msg or some other way. After notifications , one service will run named “Alarm Handler Lamda that will write these alarms in daynamoDB service
 1. Lambda Service
 2. Cloud Watch Service
 3. Cloud Watch Alrams
 4. SNS Service
 5. Dynamo DB Service

### Commands used to set Environment
1. python --version
2. sudo apt-get install python3.7
3. alias python=python3
4. python --version
5. aws --version
6. curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
7. unzip awscliv2.zip
8. sudo ./aws/install
9. aws --version
10. git clone _________
11. cd ProximaCentauri
12. mkdir AminaArshad
13. cd AminaArshad
14. mkdir Sprint1
15. mkdir LeetCode
16. cd Sprint1

### Commands used to create & run project
1. cdk init app --language python
2. python -m pip install -r requirements.txt
3. source .venv/bin/activate
4. python -m pip install -r requirements.txt
5. nvm install v16.3.0 && nvm use v16.3.0 && nvm alias v16.3.0
6. npm install -g aws-cdk
7. export PATH=$PATH:$(npm get prefix)/bin
8. python -m pip install aws-cdk.aws-s3 aws-cdk.aws-lambda
9. cdk synth
10. cdk deploy
11. deactivate

### Commands used to push on GitHub
1. git add ______________
2. git commit -m "First Commit"
3. git push

### LeetCode
1. Array Code
2. Linked List Code
  
### User Stories 
 1. Sprint 1(Web Health Stack Project)

### Documentation
1. Sprint 1(Web Health Stack Project)
