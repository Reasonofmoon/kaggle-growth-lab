# ROGII Wellbore Geology Prediction을 정석 ML 트랙으로 진행해보려 합니다

## LinkedIn draft

최근 Kaggle에서 ROGII - Wellbore Geology Prediction 대회를 살펴봤습니다.

이 대회는 horizontal wellbore를 따라 `tvt`를 예측하는 회귀 문제입니다.

지금까지 제가 살펴본 대회들은 꽤 다양했습니다.

- ARC-AGI-3는 interactive reasoning benchmark
- Orbit Wars는 multi-agent simulation bot
- AI Agents Intensive는 agent/capstone 중심

반면 ROGII는 훨씬 더 정석적인 머신러닝 competition에 가깝습니다.

데이터를 이해하고, validation을 설계하고, baseline을 만들고, feature를 개선하고, RMSE로 실험을 비교하는 흐름이 명확합니다.

그래서 이 대회는 제 Kaggle Growth Lab에서 "정석 ML workflow"를 연습하는 트랙으로 잡아보려고 합니다.

첫 목표는 상위권이 아닙니다.

첫 목표는 다음 과정을 깔끔하게 남기는 것입니다.

1. 데이터 구조 이해
2. well 단위 EDA
3. target인 `tvt`와 `TVT_input` 관계 확인
4. leakage 위험 정리
5. 단순 interpolation baseline 만들기
6. well-level validation 설계
7. 첫 `submission.csv` 제출

특히 이 대회에서 가장 중요해 보이는 것은 validation입니다.

wellbore 데이터는 같은 well 안의 row들이 강하게 연결되어 있을 가능성이 큽니다.

그래서 단순 random row split을 하면 모델이 실제보다 좋아 보일 수 있습니다.

이번에는 점수만 올리는 것보다, "왜 이 validation이 타당한가"를 설명할 수 있는 방식으로 진행해보려고 합니다.

제가 먼저 만들 baseline은 단순합니다.

`TVT_input`이 존재하는 구간을 이용해 evaluation zone의 missing 값을 well 내부에서 interpolation하고, 부족한 부분은 median으로 채우는 방식입니다.

강한 모델은 아니지만, 문제 구조를 이해하기에는 좋은 시작점이라고 생각합니다.

이 실험도 Kaggle Growth Lab에 기록합니다.

Kaggle은 실험장.
GitHub는 근거 저장소.
LinkedIn은 배운 점을 공유하는 공간.

ROGII 트랙에서는 "모델 성능"뿐 아니라 "데이터 이해와 validation 습관"을 보여주는 데 집중해보겠습니다.

GitHub: https://github.com/Reasonofmoon/kaggle-growth-lab
Competition: https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction

## Optional hashtags

#Kaggle
#MachineLearning
#Regression
#Geoscience
#DataScience
#LearningInPublic
