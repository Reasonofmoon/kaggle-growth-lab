# ARC-AGI-3에 도전해보려 합니다

## LinkedIn draft

Kaggle에서 ARC Prize 2026 - ARC-AGI-3 대회를 살펴봤습니다.

처음에는 상금 규모가 먼저 눈에 들어왔습니다.

하지만 규칙과 설명을 읽어보니, 이 대회는 일반적인 Kaggle competition과는 성격이 많이 달랐습니다.

보통의 Kaggle 대회는 데이터를 받고, feature를 만들고, model을 학습시키고, 예측 파일을 제출하는 흐름이 익숙합니다.

그런데 ARC-AGI-3는 그런 문제라기보다, agent가 새로운 환경 안에서 직접 관찰하고, 규칙을 추론하고, 행동해야 하는 interactive reasoning benchmark에 가깝습니다.

즉, 단순히 좋은 모델을 고르는 문제가 아니라 이런 질문에 가까워 보였습니다.

- agent가 처음 보는 환경에서 무엇을 관찰해야 할까?
- 명시적인 지시가 없을 때 목표를 어떻게 세워야 할까?
- 행동의 결과를 보고 내부 모델을 어떻게 수정해야 할까?
- 평가 중 인터넷이나 외부 API 없이 어떤 방식으로 reasoning해야 할까?

솔직히 말하면, 이건 지금 제 기준에서 쉬운 대회는 아닙니다.

상위권이나 상금권을 목표로 하기에는 연구 난이도도 높고, 강한 팀들도 많이 참여할 가능성이 큽니다.

그래도 한 번 도전해보려고 합니다.

목표를 낮고 명확하게 잡았습니다.

이번 목표는 우승이 아니라, 다음 과정을 직접 경험해보는 것입니다.

1. Competition join
2. Rules 핵심 정리
3. Starter notebook 또는 public notebook 1-2개 실행
4. Submission format 이해
5. Baseline 하나 제출
6. GitHub에 실험 로그 남기기
7. LinkedIn에 왜 어려운 문제인지 정리하기

제가 이 대회를 해보려는 이유는 점수보다 문제의 성격 때문입니다.

AI agent를 이야기할 때는 "무엇을 할 수 있다"는 주장보다, 어떤 환경에서 실패하고 왜 실패하는지를 보는 것이 더 중요하다고 생각합니다.

ARC-AGI-3는 그 실패를 관찰하기 좋은 문제처럼 보입니다.

그래서 이번에는 "잘했다"를 증명하기보다, "왜 어려운지 이해했다"를 기록해보려고 합니다.

이 실험도 Kaggle Growth Lab에 남깁니다.

Kaggle은 실험장.
GitHub는 근거 저장소.
LinkedIn은 배운 점을 공유하는 공간.

이번 ARC-AGI-3 도전은 그 구조 안에서 진행하는 작은 연구 관찰 트랙이 될 것 같습니다.

GitHub: https://github.com/Reasonofmoon/kaggle-growth-lab
Competition: https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3

## Optional hashtags

#Kaggle
#ARCPrize
#ARCAGI
#AIAgents
#MachineLearning
#LearningInPublic

## Source notes

- ARC-AGI-3 is an interactive reasoning benchmark.
- Agents must explore, model, set goals, plan, and execute in novel environments.
- Kaggle evaluation does not allow internet access.
- Prize-eligible solutions require open-source, reproducible methods.
- My scope is learning and baseline submission, not leaderboard competition.
