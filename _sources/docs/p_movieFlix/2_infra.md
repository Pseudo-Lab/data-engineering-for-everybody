# 2. Infra

- MovieFlix 서비스는 Kubernetes환경에서 운영됩니다.
- 추가적으로 Terraform과 Ansible을 통해 개발 외적으로 신경쓰는 부분을 최소화 하려합니다.

## Infra 관리

- [MovieRecommend-Infra](https://github.com/ehddnr301/MovieRecommend-Infra)
- 위 Repository를 통해 GCP VM 생성, 관리 및 프로젝트 환경설정을 진행합니다.

## K8s 관리

- [MovieRecommend-K8s](https://github.com/ehddnr301/MovieRecommend-K8s)
- 위 Repository를 통해 서비스에 활용되는 모든 요소들이 Container로 관리될 수 있도록 합니다.

## Flow

- Infra부분의 README를 참고하여 진행합니다. 
    - Terraform 부분의 README를 참고하여 GCP e2-standard-2 VM 3대를 생성합니다.
    - Ansible 부분의 README를 참고하여 쿠버네티스 환경을 GCP VM에 구성합니다.
- MovieRecommend-K8s Repository를 Clone하여 쿠버네티스 환경에서 필요한 프로젝트를 배포합니다.

<script src="https://utteranc.es/client.js"
        repo="Pseudo-Lab/data-engineering-for-everybody"
        issue-term="pathname"
        label="comments"
        theme="preferred-color-scheme"
        crossorigin="anonymous"
        async>
</script>