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

# Acknowledgement π
> **DE4E: Data Engineering for Everybody**λ κ°μ§μ°κ΅¬μμ DFSνλ‘κ·Έλ¨μμ μμλμμ΅λλ€. μμμ μμ κ°μ¬μ λ§μμ μ ν©λλ€.

[κ°μ§μ°κ΅¬μ](https://pseudo-lab.com/)λ DataCampμ νμμ λ°μ Donates νλ‘κ·Έλ¨μ μ§ννκ³  μμ΅λλ€. νλ‘κ·Έλ¨μ ν΅ν΄ κ΅¬μ§μ, λΆμμ  μ·¨μμ, λΉμλ¦¬ μ°κ΅¬ κ³Όνμ, νμλΆλ€κ» DataCampμμ μ κ³΅νλ λ€μν μ½μ€μ νΈλμ μ κ³΅ν©λλ€. λ³Έ νλ‘μ νΈλ DataCamp Donates νλ‘κ·Έλ¨ μ€ νλμΈ [Data Science Fellowship](https://pseudo-lab.com/c9013228f63342b689a96e18c0db32c8)μΌλ‘λΆν° μμλμμ΅λλ€. 

DE4Eλ λ°μ΄ν° λΆμκ°, λ°μ΄ν° κ³Όνμ, λ°μ΄ν° μμ§λμ΄, λ¨Έμ λ¬λ μμ§λμ΄κ° ν¨κ» λͺ¨μ¬ λ°μ΄ν°μ, λ°μ΄ν°μ μν, λ°μ΄ν°λ₯Ό μν Data Engineering Repositoryλ₯Ό λ§λ€μ΄λκ°κ³ μν©λλ€.
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

# Overview π
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

# Course Recommendation π»
* Data Engineer with Python - DataCamp
<br></br>

# Contributors π
<br></br>

# About us ππΌ
[κ°μ§μ°κ΅¬μ](https://pseudo-lab.com/)λ λ¨Έμ λ¬λ, λ°μ΄ν° μ¬μ΄μΈμ€, λ°μ΄ν° μμ§λμ΄λ§μ μ€μ¬μΌλ‘ λͺ¨μΈ λΉμλ¦¬λ¨μ²΄μλλ€. λκ΅¬λ μνλ μ°κ΅¬λ₯Ό ν  μ μλ μμμ μ΄ λλ, μ§μ§λ³΄λ€ λ μ§μ§ κ°μ μ°κ΅¬μλ₯Ό κΏκΎΈκ³  μμ΅λλ€. κ³΅μ (Share), λκΈ°λΆμ¬(Motivation), ν¨κ»νλ μ¦κ±°μ(Delighted to work together)λΌλ ν΅μ¬κ°μΉλ₯Ό μΆκ΅¬νλ©° μ½ 1800μ¬λͺμ μ°κ΅¬μλΆλ€μ΄ μ€λλ ν¨κ» λ¨Έμ λ¬λ, λ°μ΄ν° μ¬μ΄μΈμ€, λ°μ΄ν° μμ§λμ΄λ§ λΆμΌμ μ ν μν₯λ ₯μ νμ¬νκ³  μμ΅λλ€. λ³΄λ€ μμΈν λ΄μ©μ [μ¬κΈ°](https://pseudo-lab.com/)μ μ΄ν΄λ³΄μ€ μ μμ΅λλ€.
<br></br>

# License π
