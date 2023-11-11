## Hot News DashBoard

> 네이버 많이 본 뉴스 제목 키워드 기반 대시보드

네이버에서 많이 본 뉴스 섹션에서 제목을 크롤링하여, 엘라스틱서치에 저장 후 키바나로 시각화했습니다. 


![news_dashboard.png](img%2Fnews_dashboard.png)
<br/><br>

### 개발환경
- Airflow
- ElasticSearch
- Kibana
- Python
<br/><br>


### 프로젝트 아키텍처
![architecture.png](img%2Farchitecture.png)
<br/><br>

### 설명
```
1. Python 으로 네이버 뉴스를 api 로 가져옵니다.
2. 토크나이징해서 엘라스틱서치에 저장합니다.
3. 키바나를 이용해 대시보드를 생성합니다.
4. Airflow 를 활용해 주기적으로 데이터를 가져옵니다.
(프로젝트 파이썬 코드를 Docker image 화해서 
 Airflow KubernetesPodOperator를 활용해 실행시킵니다.)
```
<br/><br>
### Airflow 는 Kubernetes Cluster 위에 구축했습니다.
**spec**
- CPU 2, MEM 8GB
- node 3개 (worker 3개)
- CeleryExecutor

Helm Chart: https://artifacthub.io/packages/helm/airflow-helm/airflow