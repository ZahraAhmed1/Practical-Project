# Practical Project


## Contents 

* [Overview](#overview)
* [Trello Board](#Trello-Board)
* [The Application](#The-Application)
* [Pipeline and ERD Diagram](#Pipeline-and-ERD-Diagram)
* [Jenkins](#Jenkins)
* [Risk Assessment](#Risk-Assessment)
* [Future Improvements](#Future-Improvements)


## Overview

I created an application where you can determine if an animal will win or lose while fighting in a different country.

## Trello Board

Here is a [Trello Board](https://trello.com/b/xgvGz3X6/practical-project) which is my choice of the equivalent of a Kanban board. This is a good method as it makes everything like a message.

<img width="900" alt="2021-07-19 (15)" src="https://user-images.githubusercontent.com/84967213/126112513-935eb68e-2a06-42ba-9f46-e43d5b2ea2a7.png">



## The Application

Here is the front page of the app. It is very basic but can easily be adapted and changed on the servers.

<img width="314" alt="2021-07-19 (17)" src="https://user-images.githubusercontent.com/84967213/126113148-e04f46df-4af1-414a-939d-abf3843ee7f7.png">

### The Architecture 

__SERVICE 1 (server):__ This will be communicating with the other servers and persisting data from the database based on the ERD diagram.

__SERVICE 2 + 3 (animal_api and country_api):__ Both these servers randomly produce an animal and country from a list.

__SERVICE 4 (winner_api):__ This server produces an outcome of 'lose' or 'win'. The outcome is based on service 2 and 3 and is determined by the length the animals type.

## Pipeline and ERD Diagram

This is the Entity Relation Diagram database created in SQL. 

<img width="300" alt="2021-07-18 (22)" src="https://user-images.githubusercontent.com/84967213/126079914-4a86cd38-f722-41d0-ad2d-d9c0ae691f41.png">


## Jenkins

I ran some stages on the CI server Jenkins that would build, test and deploy the application

<img width="596" alt="2021-07-19 (10)" src="https://user-images.githubusercontent.com/84967213/126105363-83258f5c-c3cc-4115-8ad5-153f9c2c81f6.png">

## Risk Assessment

Before starting this project I had detemined some risks that might occur and their likelihood.


<img width="828" alt="2021-07-19 (13)" src="https://user-images.githubusercontent.com/84967213/126111981-65df737b-f9c6-4799-bdd8-bda52df1c361.png">


## Future Improvements

Rather than displaying the last five animals I would display only one of the animals and create a short story where the get and post request could stay the same.

I would create more servers so that a lot of peopke can be on the site without waiting. As well as that I would also create more about the animals on SQL (e.g. their fur, diet, sleep pattern)


