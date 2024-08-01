# 카프카 장애대응

## 리플리카를 통한 장애대응

- 리플리카는 파티션의 복제본입니다.
  - Replication Factor 만큼 파티션의 복제본이 각 Broker에 생성됩니다.
  - Replication Factor를 2로 지정하게 되면 동일한 데이터를 가지고 있는 파티션이 서로 다른 Broker에 2개가 생성됩니다. 이중 하나가 Leader, 하나가 Follower가 됩니다.

- Leader와 Follower구성
  - Producer와 Consumer는 Leader를 통해서만 메시지를 처리합니다.
  - Follower는 Leader로부터 메시지를 복제합니다.

- 장애대응
  - 리더가 속한 브로커가 장애시 다른 Follower가 Leader가 됩니다.

## Additional - Replication의 기본값은 주로 3인 이유

- 합의 알고리즘에서 사용되는 **정족수**
  - 5개의 노드로 구성할 경우 정족수를 채우기 위해 최소 3개의 노드는 동의를 해야해서 2개까지 장애를 허용합니다.
  - 4개의 노드로 구성할 경우 정족수를 채우기 위해 최소 3개의 노드는 동의를 해야해서 1개까지 장애를 허용합니다.
  - 3개의 노드로 구성할 경우 정족수를 채우기 위해 최소 2개의 노드는 동의를 해야해서 1개까지 장애를 허용합니다.
- 짝수개 노드로 클러스터를 구성한 경우 홀수개 노드로 구성했을때보다 장애허용에 있어 이득을 보기 힘들어 보통 홀수개로 구성되는데 그 중 3이라는 최소 수치를 설정한것으로 이해하였습니다.

<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>