# 🚀 Project - MovieFlix

- date : 2023-10-09 ~ 2023-11-11
- author
  * [이동욱](https://github.com/ehddnr301)
- 본 프로젝트는 [방태모](https://www.linkedin.com/in/taemo)님의 데이터야 놀자 발표에 영감을 받아 제작하였습니다.
- 최대한 리얼하게 구성하려 하였으나 [타협점 및 잔존이슈](https://github.com/ehddnr301/MovieRecommend/issues/5) 들이 존재합니다. 자유로운 기여로 프로젝트를 발전 시킬 수 있으면 좋겠습니다.

## Scenario

- 당신은 MovieFlix 의 하나뿐인 개발자가 되었습니다.
- 유저들의 원활한 영화관람을 위해 백엔드 개발과 추천시스템 개발을 진행하여야합니다.
- 우리는 A/B Test에만 집중할뿐 A/A Test는 놓치기 쉽다고 합니다.
- MovieFlix는 A/B Test를 통해 대조 실험을 하기전 A/A Test를 통해 두그룹을 먼저 살펴보려 합니다.

## Architecture

<img src="./images/9_0_1.png" align="center">


## Final Visualization

<img src="./images/9_0_2.png" align="center">

- `그룹별 평균 만족도 점수` 차트 혹은 `유저 만족도 현황` 차트를 보았을 때 A/B Test에서 B그룹 만족도가 개선
- 우리의 추천시스템이, 서비스가 잘 작동하고 있구나를 모니터링하는것이 목표입니다.

## Data

- [MovieLens](https://grouplens.org/datasets/movielens/)

<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>