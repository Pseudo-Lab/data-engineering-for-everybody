# 파티션과 프로듀서 & 컨슈머

## 파티션과 프로듀서

![alt text](./images/9_1_3_0.png)

- 프로듀서는 어떤 Partition에 메시지를 저장할지 결정해야합니다.
  1. 메시지 키가 제공되지 않은 경우 RoundRobin 방식으로 돌아가면서 저장할 수 있습니다.
  2. Key를 이용해 특정 Partition을 선택할 수 있습니다.
    - Key가 지정된 경우 Kafka는 키의 해시값을 이용해 메시지를 특정 파티션에 저장합니다.
    - 같은 키를 갖는 메시지는 항상 같은 Partition에 저장되기 때문에 메시지 순서가 보장됩니다.

## 파티션과 컨슈머

![alt text](./images/9_1_3_1.png)

- 컨슈머는 **컨슈머 그룹**에 속하게 됩니다.
- 한개의 파티션은 컨슈머 그룹에서 한개 컨슈머만 연결 가능합니다.
  - 컨슈머 그룹에 속한 컨슈머들은 하나의 파티션을 공유 할 수 없습니다.
  - 한 컨슈머 그룹 기준으로 파티션의 메시지를 순서대로 처리하게 됩니다.

- 그림 예시를 살펴보면 Consumer Group A에서 각 컨슈머는 Partition0과 Partition1을 공유할 수 없습니다.
- 다른 Consumer Group B는 Consumer Group A에서 읽고있는 Partition0과 Partition1을 읽을 수 있습니다.

<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>