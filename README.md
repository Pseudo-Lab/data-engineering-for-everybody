# Data Engineering for Everybody
<p align="center">
  <img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffbdaefd4-c878-42d0-85b3-6bd65934bf10%2FUntitled.png?table=block&id=a8bbbdc4-774a-4c51-b020-bf7a7c91ceba&spaceId=333f96cf-396d-45ff-8331-232d41bd4d55&width=2000&userId=824ab286-e513-46f5-9abf-8a045b001e1a&cache=v2" width="1000">
</p>

> DE4E: Data Engineering for Everybody by Pseudo-Lab

[![Pseudo-Lab](https://img.shields.io/badge/-PseudoLab-565CD8)](https://pseudo-lab.com/)
[![Data Science Fellowship](https://img.shields.io/badge/-DSF-32CD32)](https://url.kr/58h2mq)
[![DataCamp Donates](https://img.shields.io/badge/-DataCampDonates-228b22)](https://www.datacamp.com/donates)

This repository aims to give a complete picture from the fundamental data engineering landscape to advanced data engineering for Data Lover!
<br></br>

# Acknowledgement 🙏
> **DE4E: Data Engineering for Everybody**는 가짜연구소의 DFS프로그램에서 시작되었습니다. 시작에 앞서 감사의 말씀을 전합니다.

[가짜연구소](https://pseudo-lab.com/)는 DataCamp의 후원을 받아 Donates 프로그램을 진행하고 있습니다. 프로그램을 통해 구직자, 불완전 취업자, 비영리 연구 과학자, 학생분들께 DataCamp에서 제공하는 다양한 코스와 트랙을 제공합니다. 본 프로젝트는 DataCamp Donates 프로그램 중 하나인 [Data Science Fellowship](https://pseudo-lab.com/c9013228f63342b689a96e18c0db32c8)으로부터 시작되었습니다. 

DE4E는 데이터 분석가, 데이터 과학자, 데이터 엔지니어, 머신러닝 엔지니어가 함께 모여 데이터의, 데이터에 의한, 데이터를 위한 Data Engineering Repository를 만들어나가고자합니다.
<br></br>

# DE4E: Data Engineering for Everybody 
```mermaid
sequenceDiagram
Who want to know DE->>DE4E(Data Engineering for Everybody): Hello DE?
DE4E(Data Engineering for Everybody)->>Who want to know DE: Why Don't you Start from fundamentals?
Who want to know DE->>DE4E(Data Engineering for Everybody): I'm not familier with DE, any help?
loop fill the background knowledge
  DE4E(Data Engineering for Everybody)->>DE4E(Data Engineering for Everybody): we also prepared background knowledges for DE, DA, DS!
end
Who want to know DE->>DE4E(Data Engineering for Everybody): Thank u :) What's Next?
DE4E(Data Engineering for Everybody)->>Who want to know DE: Dive Into Data Engineering! like Intermediate Python, Spark, Airflow...!

loop Pseudo-Lab x Data Camp
    DFS->>DFS: We learn together, share together and grow together!
end
```

---
<br></br>

# Overview 🔎
```mermaid
flowchart LR

%% Colors %%

classDef blue fill:#66deff,stroke:#000,color:#000
classDef green fill:#6ad98b,stroke:#000,color:#000
classDef lgreen fill:#24e357,stroke:#000,color:#000

%% GENERATION 1 %%
p1(Beginner):::green --> funda(Fundamentals):::blue

%% GENERATION 2 %%	
funda --- c1(DE4E: Data Engineering for Everybody)

%% GENERATION 3 %%	
funda --> p2(Intermediate):::green ---> p3(Advanced):::blue

%% GENERATION 4 %%	
Mo(Background Knowledge):::green --- G2(Fill Your Knowledge and Experiences)
```
> We want to let you know how data is connected :)

<br></br>

## Fundamentals
```mermaid
flowchart LR
A(Beginner) -->|foot in the door!| B(Fundamentals)
B --> C{Decision}
C -->|fill the background knowledge?| D[Background Knowledge]
C -->|Go next| E[Intermediate]

style A fill:#cff09e,stroke:#3b8686,stroke-width:4px
style B fill:#79bd9a,stroke:#08182b,stroke-width:2px
style C fill:#cff09e,stroke:#3b8686,stroke-width:4px, 
style D fill:#cff09e,stroke:#3b8686,stroke-width:4px
style E fill:#cff09e,stroke:#3b8686,stroke-width:4px
```
* Introduction to DE4E: Data Engineering for Everybody
* Introduction to Data Engineering
* Introduction Shell Programming and Data Processing in Shell
* Introduction to Bash Scripting
* Python Programming
* Introduction to Relational Databases in SQL
* Pandas for data processing
* Database Design
* Introduction to Apache Airflow
* Introduction to PySpark
<br></br>

## Intermediate
```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```
* Efficient Python Code
* Writing Function in Python
* Unit Testing for Data Science in Python
* OOP(Object-Oriented Programming) in Python
* Big Data Fundamentals with PySpark 
* Data Analysis in SQL
<br></br>

## Advanced
```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```
* Cleaning Data with PySpark
<br></br>


## Background Knowledge
```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```
* About Data Engineering
* Data Analyst vs Data Engineer vs Data Science
* Data Engineer's responsibilities
* Structured Data, Semi-Structured Data and Unstructured Data
* OLTP vs OLAP
* ETL, ELT and Reverse ETL
* Change Data Capture(CDC)
* Data Lake vs Data warehouse
* Lake house
* Data engineers process
* Batch Data vs Streaming Data
* Batch processing vs Stream processing
* Scheduling
* Hadoop Ecosystem
* Parallel computing
* Introduction to Cloud Computing
<br></br>

## Summary
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'pie1': '#a8dba8', 'pie2': '#79bd9a', 'pie3': '#3b8686', 'pie4': '#cff09e', 'pie5': '#800080', 'pie6': '#ff0000', 'pie7': '#FFA500'}}}%%
pie
  "Fundamentals" : 10
  "Intermediate" : 6
  "Advanced" : 1
  "Background Knowledge" : 16
```

<br></br>

# Course Recommendation 💻
* Data Engineer with Python - DataCamp
<br></br>

# Contributors 😃
<br></br>

# About us 👋🏼
[가짜연구소](https://pseudo-lab.com/)는 머신러닝, 데이터 사이언스, 데이터 엔지니어링을 중심으로 모인 비영리단체입니다. 누구나 원하는 연구를 할 수 있는 시작점이 되는, 진짜보다 더 진짜 같은 연구소를 꿈꾸고 있습니다. 공유(Share), 동기부여(Motivation), 함께하는 즐거움(Delighted to work together)라는 핵심가치를 추구하며 약 1800여명의 연구원분들이 오늘도 함께 머신러닝, 데이터 사이언스, 데이터 엔지니어링 분야에 선한 영향력을 행사하고 있습니다. 보다 자세한 내용은 [여기](https://pseudo-lab.com/)서 살펴보실 수 있습니다.
<br></br>

# License 🗞
