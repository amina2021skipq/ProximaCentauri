# ProximaCentauri
This is the Repo for cohort 2 trainees.

## Web Health Stack Project (Sprint1: 13Dec-17Dec)
In this project we will monitor the url resorce /website and check whether the mentioned host is avaible and measure latency. we will use lambda service. This service will measures and write the availblity and latency into cloud watch service. If the latency value rises from thresh hold then Cloud watch alarm arises alarm. 
When alarm rised , SNS Topic service will send notifications to the subscribers. Notifications may be in the form of email and msg or some other way. After notifications , one service will run named “Alarm Handler Lamda that will write these alarms in daynamoDB service
 1. Lambda Service
 2. Cloud Watch Service
 3. Cloud Watch Alrams
 4. SNS Service
 5. Dynamo DB Service

## LeetCode:
1. Array Code
2. Linked List Code
  
## User Stories 
 1. Sprint 1(Web Health Stack Project)

## Documentation
1. Sprint 1(Web Health Stack Project)



