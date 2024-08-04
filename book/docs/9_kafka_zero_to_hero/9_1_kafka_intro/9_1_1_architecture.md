# 카프카 기본 구조

![alt text](./images/9_1_1.png)

## 카프카란

> 카프카(Kafka)는 아파치 소프트웨어 재단에서 개발한 오픈 소스 분산 스트리밍 플랫폼입니다. 대규모 데이터 처리와 실시간 데이터 스트리밍을 목적으로 설계되었습니다. 카프카는 여러 애플리케이션 간에 데이터를 효율적으로 교환할 수 있게 합니다.[MSA(MicroService Arcitecture)에 적합하다고 평가]

- 카프카는 4개의 구성요소로 이루어져 있습니다. (Zookeeper, Kafka Cluster, Producer, Consumer)
- 카프카는 주로 대용량의 실시간 데이터 스트리밍을 처리하기 위해 사용되는 분산 스트리밍 플랫폼입니다.

## Zookeeper

- 카프카 클러스터를 관리하는 용도로 Zookeeper가 필요합니다.
- 브로커 메타데이터 관리, 파티션 리더 선출 등의 관리 역할을 수행합니다.
- 주키퍼를 제거한 **KRaft 모드**를 사용하여 주키퍼 의존성을 제거하는 방법도 존재합니다.

## Kafka Cluster

- 카프카 클러스터는 메시지를 저장하는 저장소 입니다.
- 하나의 카프카 클러스터는 여러개의 브로커(각각의 서버)로 구성이 됩니다.

## Producer

- 카프카 클러스터에 메시지를 넣는 역할

## Consumer

- 카프카 클러스터에서 메시지를 읽어오는 역할

<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>