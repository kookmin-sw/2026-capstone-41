# "Vision-Language Navigation 기반 사족 로봇 통합 자율 네비게이션 시스템"

## 프로젝트 개요

본 프로젝트는 **Unitree Go2** 사족 보행 로봇에 최신 Vision-Language Navigation 기반 모델인 **InternVLA-N1-DualVLN**을 이식하여, 사람이 말하는 자연어 명령("의자로 가", "저 사람을 따라가")만으로 로봇이 시각 정보를 해석하고 실제 환경을 자율 주행하도록 구현한 프로젝트다.

기존 Vision-Language Navigation 모델들은 대체로 사람 눈높이의 시점이나 고품질 카메라 환경을 전제로 만들어져 있어, 카메라 높이가 낮은 소형 사족 로봇 환경에 그대로 적용하면 성능이 떨어질 수 있다. 우리 팀은 이러한 **로봇 본체별 시점 차이와 실제 환경 배포 문제**를 보완하기 위해 LOVON의 일부 구조와 객체 탐지 모듈을 InternVLA 기반 파이프라인에 결합하고, ROSA 에이전트를 통해 자연어 명령을 여러 도구 호출 단위로 분해하는 시스템 레벨의 개선을 더했다.

본 프로젝트의 결과는 **대한전자공학회 2026년도 하계종합학술대회**에 “시점 변화에 강건한 시각-언어 내비게이션 모듈과 다중 도구 호출 에이전트 기반 파이프라인”이라는 제목으로 제출되어 accepted되었다.

---

## 학술 성과

본 프로젝트의 연구 결과는 **대한전자공학회 2026년도 하계종합학술대회**에 논문으로 제출되어 **Accept**되었다.

* **논문명**: 시점 변화에 강건한 시각-언어 내비게이션 모듈과 다중 도구 호출 에이전트 기반 파이프라인
* **영문명**: A Vision-Language Navigation Module Robust to Viewpoint Shifts and a Multi-Tool Invocation Agent-Based Pipeline
* **학회**: 대한전자공학회 2026년도 하계종합학술대회
* **논문번호**: SSP-0184
* **주저자**: 임민석
* **공동저자**: 성재승, 조원영, 조유빈, 정유진, 유리안, 이재권
* **교신저자**: 이재구

본 논문은 사족 보행 로봇의 낮은 카메라 시점에서 발생하는 Vision-Language Navigation 성능 저하 문제를 다루며, 기존 DualVLN 기반 구조에 객체 탐지 모듈과 ROSA 기반 다중 도구 호출 에이전트를 결합한 실제 로봇 파이프라인을 제안한다. 실험에서는 객체 탐지 모듈이 낮은 시점 조건에서 pixel goal 보정에 도움을 주었고, ROSA 기반 에이전트를 통해 Navigation, Move, Task Planning, Backtracking 기능을 통합하여 복합 자연어 지시를 수행할 수 있음을 확인하였다.

특히 실제 환경 과업 실험에서 제안 파이프라인은 평균 60.0%의 성공률을 보였으며, 낮은 카메라 시점 조건에서 객체 탐지 모듈을 추가했을 때 SR은 1.93%p, SPL은 2.46%p 향상되었다.

---

## 4가지 핵심 기능

단일 task 시연에 그치지 않고, 네 가지 기능을 하나의 파이프라인으로 통합했다.

### Navigation

자연어 명령을 받아 환경 내 목표 지점까지 자율 주행한다. InternVLA-N1-DualVLN이 카메라 이미지와 명령을 동시에 해석해 pixel goal을 출력하면, 로봇이 그에 맞춰 이동한다.

### Pointing

이미지 위 특정 객체를 지시하면 로봇이 해당 객체로 향한다. 객체 지시 정보를 pixel goal로 변환해 InternVLA에 전달하는 방식이다.

### Following

사람이나 물체를 지속적으로 추종한다. YOLO 객체 검출 결과를 pixel goal 입력으로 사용하며, LOVON의 일부 구조를 차용해 모션 블러·저속 추종 환경에서도 안정적으로 동작하도록 개선했다.

### Backtracking

LiDAR SLAM 기반 closed-loop 제어로 과거에 지나온 경로를 자동으로 되짚어 돌아온다. 이를 통해 “처음 위치로 돌아와”, “N초 전 위치로 돌아가”와 같은 복귀 명령을 수행할 수 있도록 했다.

---

## 시스템 아키텍처

* **베이스 모델 — InternVLA-N1-DualVLN**: System1(저수준 제어) + System2(고수준 의사결정)의 dual-system 구조를 가진 Vision-Language Navigation 기반 foundation model을 활용한다.
* **LOVON 부분 결합**: LOVON 모델 전체를 통째로 사용하지 않고, 일부 구조와 모델을 차용해 InternVLA 내부에 끼워 넣어 객체 중심 지시와 추종 환경에서의 성능을 개선했다.
* **객체 탐지 기반 Pixel Goal 보정**: YOLO 객체 검출 결과를 pixel goal 형태로 주입하여, 낮은 카메라 시점에서 발생하는 목표 위치 추론 오차를 완화한다.
* **LiDAR SLAM Runner**: 실시간 SLAM 기반 closed-loop 제어로 안전한 자율 백트래킹을 제공한다.
* **ROSA Agent + Qwen3.5-4B**: 자연어 명령을 tool 단위로 분해하고, 4종 기능을 상황에 맞게 호출하는 LLM 에이전트다.
* **YOLO 입력단**: VLA/VLN 모델을 통째로 재학습하지 않고도 신규 task를 추가할 수 있도록 객체 검출 결과를 pixel goal 형태로 모델에 주입한다.

---

## 진행 타임라인

### 3월 — 환경 구축 및 베이스라인 탐색

프로젝트 방향성 결정, ROS2/Zenoh 무선 통신 셋업, InternVLA·LOVON 재현, 1차 시연 발표를 진행했다.

### 4월 — 핵심 기능 구현

InternVLA에 객체 탐지 모듈과 Following 기능을 결합하는 방향성을 확정하고, LOVON 일부 구조 차용·디블러링·LiDAR SLAM 기반 자율 Backtracking을 구현했다.

### 5월 — 통합·평가·논문화

Pointing 기능 추가, 전체 코드 병합, ROSA에 Qwen3.5-4B 연결, ROS2 도구 개선, Task Planner 통합 후 정량 평가와 논문 초안 작성에 들어갔다. 이후 해당 연구 결과를 대한전자공학회 2026년도 하계종합학술대회에 제출하여 accepted되었다.

---

## 기술 스택

**하드웨어**

* Unitree Go2 (4족 보행 로봇, 내장 Jetson Orin / 내장 LiDAR)
* Intel RealSense D435 (RGB-D 카메라)
* RTX 3090

**모델·AI**

* InternVLA-N1-DualVLN (메인 VLN 모델)
* LOVON (일부 구조 차용)
* Qwen3.5-4B (vLLM 서빙, ROSA agent의 LLM)
* YOLO (객체 검출)

**소프트웨어**

* Python + PyTorch — 메인 개발 언어 및 InternVLA·LOVON 추론 프레임워크
* vLLM — Qwen3.5-4B LLM 서빙
* OpenCV / NumPy — 이미지 처리·디블러링·SLAM 후처리·좌표 연산
* ROS 2 — 로봇 미들웨어 (노드 간 토픽·서비스 통신)
* TensorRT — System1 추론 속도 향상

**미들웨어·로봇 제어**

* Zenoh-bridge ROS2 DDS (무선 통신 브릿지)
* Unitree API
* LiDAR SLAM Runner (자체 closed-loop 백트래킹)

**시뮬레이션·툴**

* NVIDIA Isaac Sim (Embodiment gap 검증)
* 3D 프린팅 (RealSense 마운트)

---

## 실험 및 평가

본 프로젝트에서는 실제 Unitree Go2 환경과 Isaac Sim 기반 실험을 통해 Vision-Language Navigation 모델의 사족 보행 로봇 배포 가능성을 평가했다.

### 1. 실제 환경 과업 실험

실제 환경에서는 Navigation, 저수준 제어, Task Planning, Backtracking을 포함한 복합 자연어 지시를 수행하도록 구성했다. 단일 VLN 모델만 사용한 경우 복합 과업 수행에 한계가 있었지만, 제안한 ROSA 기반 다중 도구 호출 파이프라인은 과업 유형별 실험에서 평균 60.0%의 성공률을 보였다.

### 2. 시점 변화에 따른 성능 저하 분석

기존 VLN 모델은 주로 사람 눈높이에 가까운 140cm 카메라 시점에서 평가된다. 그러나 Unitree Go2와 같은 소형 사족 보행 로봇은 카메라 높이가 낮아, 기존 모델을 그대로 배포하면 시점 차이로 인한 성능 저하가 발생할 수 있다.

Isaac Sim 환경에서 카메라 높이를 140cm에서 70cm로 낮추어 평가한 결과, 기존 DualVLN의 성능은 SR과 SPL에서 모두 감소했다. 이는 사족 보행 로봇의 낮은 시점이 목표 객체의 위치, 크기, 구도 변화를 유발하기 때문이다.

### 3. 객체 탐지 모듈의 보정 효과

낮은 카메라 시점 조건에서 객체 탐지 모듈을 추가하면, 객체 중심 지시에서 pixel goal을 보정할 수 있다. 실험 결과 70cm 조건에서 객체 탐지 모듈을 추가했을 때 SR은 1.93%p, SPL은 2.46%p 향상되었다. 이를 통해 객체 탐지 기반 pixel goal 보정이 일부 객체 중심 지시에서 보조 단서로 작동할 수 있음을 확인했다.

---

## 레퍼런스

본 프로젝트의 핵심 기반이 된 논문 및 기술 문서다.

[1] M. Wei, C. Wan, J. Peng, *et al.*, "Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation," *arXiv preprint* arXiv:2512.08186, 2025. [[arXiv](https://arxiv.org/abs/2512.08186)] [[HuggingFace](https://huggingface.co/InternRobotics/InternVLA-N1-DualVLN)]

[2] D. Peng, J. Cao, Q. Zhang, and J. Ma, "LOVON: Legged Open-Vocabulary Object Navigator," *arXiv preprint* arXiv:2507.06747, July 2025. [[arXiv](https://arxiv.org/abs/2507.06747)]

[3] R. Royce, M. Kaufmann, J. Becktor, *et al.*, "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent," *arXiv preprint* arXiv:2410.06472, October 2024. [[arXiv](https://arxiv.org/abs/2410.06472)] [[GitHub](https://github.com/nasa-jpl/rosa)]

[4] Qwen Team, "Qwen3.5: Towards Native Multimodal Agents," *Qwen Blog*, February 2026. [[Blog](https://qwen.ai/blog?id=qwen3.5)] [[HuggingFace](https://huggingface.co/Qwen/Qwen3.5-4B)]

---

## 프로젝트의 의의

### 1. 소형 사족 로봇 환경에 대한 VLN Foundation Model의 적응

대규모 시뮬레이션 데이터로 학습된 최신 Vision-Language Navigation Foundation Model은 일반적으로 사람 눈높이 시점이나 고품질 RGB-D 환경을 가정하기 때문에, 시점 높이가 낮고 카메라 사양이 제한된 소형 사족 로봇에 그대로 배포하면 성능이 저하되는 본질적 한계를 지닌다. 본 프로젝트는 LOVON의 일부 구조와 객체 탐지 모듈을 InternVLA-N1-DualVLN 기반 파이프라인에 선택적으로 통합함으로써, **Foundation Model을 통째로 재학습하지 않고도 소형 사족 로봇 본체에 적응시키는 실용적 경로**를 제시했다. 이는 최신 대규모 VLN 모델을 저비용 로봇 플랫폼에 이식하려는 후속 연구·개발에 직접 활용 가능한 방법론적 기여로 평가된다.

### 2. 단일 task 시연을 넘어선 멀티태스크 통합 파이프라인

오픈소스 InternVLA의 공개 시연이 단일 navigation task에 머물러 있는 것과 달리, 본 시스템은 **Navigation, Pointing, Following, Backtracking 4종 task를 ROSA 기반 LLM 에이전트 위에 단일 파이프라인으로 통합**했다. 특히 LiDAR SLAM closed-loop 기반 자율 백트래킹은 InternVLA가 본래 다루지 않는 기능을 시스템 레벨에서 확장한 사례로, foundation model을 응용 task로 확장하는 구체적 설계 예시를 제공한다.

### 3. 자연어 기반 원격 로봇 운용 인터페이스

자체 개발한 **Go2 Monitor 웹 인터페이스**와 **Zenoh-bridge 기반 무선 ROS2 통신 스택**을 결합함으로써, **인터넷 연결만 있으면 원격지에서도 로봇의 실시간 카메라 피드를 확인하고 자연어 명령을 전송·실행**시킬 수 있는 구조를 완성했다. 이는 사족 로봇의 활용 범위를 연구실 데모를 넘어 **사람의 직접 접근이 제한되는 원격지·위험 환경·무인 시설** 등 실제 운용 시나리오로 확장할 수 있는 기반을 제공하며, 비전문가도 자연어만으로 로봇을 운용할 수 있다는 점에서 HRI(Human-Robot Interaction) 측면의 진입 장벽을 크게 낮춘 기여로 평가된다.

### 4. 실제 로봇 실험 기반 학술 성과

본 프로젝트는 단순한 기능 구현이나 데모에 그치지 않고, 실제 Unitree Go2 사족 보행 로봇 환경에서 Vision-Language Navigation 모델의 배포 가능성과 한계를 정량적으로 분석했다. 특히 사람 눈높이 기반 벤치마크와 달리 낮은 카메라 시점을 가지는 사족 로봇 환경에서는 기존 VLN 모델의 성능이 저하될 수 있음을 확인하고, 객체 탐지 기반 pixel goal 보정과 ROSA 기반 도구 호출 에이전트를 통해 이를 완화하는 방향을 제안했다.

이 결과는 대한전자공학회 2026년도 하계종합학술대회에 accepted되었으며, 프로젝트가 단순 캡스톤 수준을 넘어 실제 로봇 시스템 구현, 실험 평가, 논문화까지 연결된 사례라는 점에서 의의가 있다.
