# 2.5 Index 실험

- 데이터 엔지니어가 작업을 수행할 때 적절한 Index를 설정함으로써 데이터 엑세스 성능을 최적화 하고 쿼리 실행시간을 단축시킬 수 있습니다.
- 이번 실험에서는 Postgresql을 사용하여 간단히 B-Tree Index와 Brin Index를 비교해봄으로써 상황에따른 Index선택에 대해 알아보고자 합니다.
- 자신의 컴퓨팅 리소스, 데이터 크기, 검색조건, 데이터 특성 등 다양한 요소를 고려하여 Index를 설정하여야 합니다.

## B-Tree Index (Balanced Tree Index)

- B-Tree 인덱스는 키 기반으로 정렬된 데이터 구조를 사용하기 때문에, 컬럼의 값이 다양하고 중복되지 않는 경우 인덱스의 효과를 최대화할 수 있습니다.
- 일반적인 데이터 구조에서 균등한 속도를 내기 때문에 기본적인 알고리즘이라고 할 수 있습니다.

## BRIN Index (Block Range Index)

- BRIN 인덱스는 페이지의 메타데이터를 뽑아서 인덱스를 구성하게 됩니다.
- 대량의 정렬된 데이터나 시계열 데이터와 같이 연속적인 특성을 가진 데이터에서 뛰어난 성능을 발휘합니다.

## 실험

- [실습 Repository](https://github.com/ehddnr301/Index)를 Clone하여 직접 실습해보도록 합니다.
- 준비된 실습환경은 PK설정이 되어있지 않고, 병렬처리에 대한 고려가 되어있지 않습니다.

`준비한 실습1`: 126,269,471건의 row에 대해 실험 (날짜에 대해서 인덱스)

- 인덱스가 없는 경우: 15868.808 ms
- B Tree Index가 있는 경우: 738.754 ms **(2705 MB)**
- Brin Index가 있는 경우: 1085.056 ms **(192 kB)**
- Index를 설정함으로써 성능이 개선되는 정도는 비슷하지만 Index 크기는 Brin Index가 훨씬 작습니다.

`준비한 실습2`: 126,269,471건의 row에 대해 실험 (Alphabet에 대해서 인덱스)

- 인덱스가 없는 경우: 17285.917 ms
- B Tree Index가 있는 경우: 15827.413 ms **(835 MB)**
- Brin Index가 있는 경우: 17893.296 ms **(152 kB)**
- 인덱스가 없는 경우에 비해서 성능이 크게 나아지지 않았음을 볼 수 있습니다.
- Brin Index의 경우엔 인덱스가 없는경우보다 오히려 느려졌음을 볼 수 있습니다.


<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>