# Orbit Wars에서 첫 strategy bot을 제출해보려 합니다

## LinkedIn draft

Kaggle에서 Orbit Wars라는 simulation competition을 살펴봤습니다.

이 대회는 일반적인 prediction competition이 아니라, 2D 공간에서 planet을 점령하는 strategy bot을 만드는 대회입니다.

Agent는 매 turn마다 현재 board 상태를 관찰하고, 어느 planet에서 어느 각도로 몇 척의 ship을 보낼지 결정해야 합니다.

처음 봤을 때 흥미로웠던 점은 이 대회가 AI agent를 꽤 현실적인 방식으로 연습하게 만든다는 점이었습니다.

단순히 정답 label을 맞히는 문제가 아닙니다.

- 관찰해야 하고
- 행동해야 하고
- 상대 agent와 경쟁해야 하고
- replay를 보면서 실패 원인을 찾아야 하고
- 다음 version에서 전략을 개선해야 합니다

특히 마음에 든 부분은 첫 제출 난이도가 비교적 낮다는 점입니다.

Nemotron challenge처럼 큰 모델을 fine-tuning해야 하는 것도 아니고, ARC-AGI-3처럼 submission gateway 구조부터 낯선 것도 아닙니다.

Orbit Wars는 `main.py` 안에 `agent(obs)` 함수를 작성해서 제출할 수 있습니다.

그래서 이번에는 아주 작은 목표로 시작하려고 합니다.

목표는 상위권이 아닙니다.

첫 목표는 다음 흐름을 끝까지 경험하는 것입니다.

1. Competition join
2. Rules 읽고 핵심 정리
3. 간단한 nearest-target baseline bot 작성
4. local validation 실행
5. Kaggle에 첫 bot 제출
6. replay와 logs 확인
7. 실패한 행동을 GitHub에 기록
8. 다음 version에서 전략 하나만 개선

제가 처음 만들 baseline은 단순합니다.

내 planet 중 ship이 충분한 곳에서, 가까우면서 production이 괜찮은 target으로 일부 ship을 보내는 방식입니다.

강한 bot은 아니겠지만, 시작점으로는 충분하다고 생각합니다.

이번 실험에서 보고 싶은 것은 점수보다 이 과정입니다.

- sun을 가로지르는 fleet이 얼마나 자주 죽는지
- nearest target 전략이 언제 실패하는지
- 공격보다 방어가 필요한 순간이 언제인지
- replay를 보고 strategy를 어떻게 수정할 수 있는지

이 실험도 Kaggle Growth Lab에 기록합니다.

Kaggle은 실험장.
GitHub는 근거 저장소.
LinkedIn은 배운 점을 공유하는 공간.

Orbit Wars는 agent를 "말로 설명하는 것"에서 벗어나, 실제 환경에서 행동하게 만들어볼 좋은 연습장이 될 것 같습니다.

GitHub: https://github.com/Reasonofmoon/kaggle-growth-lab
Competition: https://www.kaggle.com/competitions/orbit-wars

## Optional hashtags

#Kaggle
#OrbitWars
#AIAgents
#MultiAgentSystems
#ReinforcementLearning
#LearningInPublic
