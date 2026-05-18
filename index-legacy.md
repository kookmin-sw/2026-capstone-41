# VLA 기반 사족 로봇 통합 자율 시스템

## 프로젝트 개요

본 프로젝트는 **Unitree Go2** 사족 보행 로봇에 최신 Vision-Language-Action(VLA) 모델인 **InternVLA-N1-DualVLN**을 이식하여, 사람이 말하는 자연어 명령("의자로 가", "저 사람을 따라가")만으로 로봇이 시각 정보를 해석하고 실제 환경을 자율 주행하도록 구현한 프로젝트다.

기존 VLA 모델들은 대체로 휴머노이드급 시점이나 고품질 카메라 환경을 전제로 만들어져 있어, 작은 사족 로봇처럼 본체가 다른 환경에 그대로 옮기면 성능이 떨어진다. 우리 팀은 이러한 **로봇 본체별 환경 차이**를 보정하기 위해 LOVON의 일부 구조를 InternVLA에 결합하고, ROSA 에이전트로 명령을 분해하는 등 시스템 레벨의 개선을 더했다.

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
LiDAR SLAM 기반 closed-loop 제어로 과거에 지나온 경로를 자동으로 되짚어 돌아온다. 

---

## 시스템 아키텍처

- **베이스 모델 — InternVLA-N1-DualVLN**: System1(저수준 제어) + System2(고수준 의사결정)의 dual-system 구조를 가진 VLA foundation model을 그대로 활용한다.
- **LOVON 부분 결합**: LOVON 모델 전체를 통째로 사용하지 않고, 일부 구조와 모델만 차용해 InternVLA 내부에 끼워 넣어 모션 블러·저속 환경에서의 추종 성능을 개선했다.
- **LiDAR SLAM Runner**: 실시간 SLAM 기반 closed-loop 제어로 안전한 자율 백트래킹을 제공한다.
- **ROSA Agent + Qwen3.5-4B**: 자연어 명령을 tool 단위로 분해하고, 4종 기능을 상황에 맞게 호출하는 LLM 에이전트다.
- **YOLO 입력단**: VLA를 통째로 재학습하지 않고도 신규 task를 추가할 수 있도록 객체 검출 결과를 pixel goal 형태로 모델에 주입한다.

---

## 팀 구성과 역할

| 팀원 | 담당 영역 |
|---|---|
| **임민석** | TODO |
| **조원영** | TODO |
| **정유진** | TODO |
| **성재승** | TODO |
| **유리안** | TODO |
| **조유빈** | TODO |

---

## 진행 타임라인

### 3월 — 환경 구축 및 베이스라인 탐색
프로젝트 방향성 결정, ROS2/Zenoh 무선 통신 셋업, InternVLA·LOVON 재현, 1차 시연 발표를 진행했다.

### 4월 — 핵심 기능 구현
InternVLA에 Following을 결합하는 방향성을 확정하고, LOVON 일부 구조 차용·디블러링·LiDAR SLAM 기반 자율 Backtracking을 구현했다.

### 5월 — 통합·평가·논문화
Pointing 기능 추가, 전체 코드 병합, ROSA에 Qwen3.5-4B 연결, ROS2 도구 개선, Task Planner 통합 후 정량 평가와 논문 초안 작성에 들어갔다.

---

## 기술 스택

**하드웨어**
- Unitree Go2 (4족 보행 로봇, 내장 Jetson Orin / 내장 LiDAR)
- Intel RealSense D435 (RGB-D 카메라)
- RTX 3090

**모델·AI**
- InternVLA-N1-DualVLN (메인 VLA)
- LOVON (일부 구조 차용)
- Qwen3.5-4B (vLLM 서빙, ROSA agent의 LLM)
- YOLO (객체 검출)

**소프트웨어**
- Python + PyTorch — 메인 개발 언어 및 InternVLA·LOVON 추론 프레임워크
- vLLM — Qwen3.5-4B LLM 서빙
- OpenCV / NumPy — 이미지 처리·디블러링·SLAM 후처리·좌표 연산
- ROS 2 — 로봇 미들웨어 (노드 간 토픽·서비스 통신)
- TensorRT — System1 추론 속도(주기) 향상

**미들웨어·로봇 제어**
- Zenoh-bridge ROS2 DDS (무선 통신 브릿지)
- Unitree API
- LiDAR SLAM Runner (자체 closed-loop 백트래킹)

**시뮬레이션·툴**
- NVIDIA Isaac Sim (Embodiment gap 검증)
- 3D 프린팅 (RealSense 마운트)

---

## 레퍼런스

본 프로젝트의 핵심 기반이 된 4개의 논문 및 기술 문서다.

[1] M. Wei, C. Wan, J. Peng, *et al.*, "Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation," *arXiv preprint* arXiv:2512.08186, 2025. \[[arXiv](https://arxiv.org/abs/2512.08186)\] \[[HuggingFace](https://huggingface.co/InternRobotics/InternVLA-N1-DualVLN)\]

[2] D. Peng, J. Cao, Q. Zhang, and J. Ma, "LOVON: Legged Open-Vocabulary Object Navigator," *arXiv preprint* arXiv:2507.06747, July 2025. \[[arXiv](https://arxiv.org/abs/2507.06747)\]

[3] R. Royce, M. Kaufmann, J. Becktor, *et al.*, "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent," *arXiv preprint* arXiv:2410.06472, October 2024. \[[arXiv](https://arxiv.org/abs/2410.06472)\] \[[GitHub](https://github.com/nasa-jpl/rosa)\]

[4] Qwen Team, "Qwen3.5: Towards Native Multimodal Agents," *Qwen Blog*, February 2026. \[[Blog](https://qwen.ai/blog?id=qwen3.5)\] \[[HuggingFace](https://huggingface.co/Qwen/Qwen3.5-4B)\]

---

## Project Significance

### 1. 소형 사족 로봇 환경에 대한 VLA Foundation Model의 적응
대규모 시뮬레이션 데이터로 학습된 최신 VLA Foundation Model은 일반적으로 휴머노이드급 시점이나 고품질 RGB-D 환경을 가정하기 때문에, 시점 높이가 낮고 카메라 사양이 제한된 소형 사족 로봇에 그대로 배포하면 성능이 저하되는 본질적 한계를 지닌다. 본 프로젝트는 LOVON의 핵심 모듈을 InternVLA-N1-DualVLN 내부에 선택적으로 통합함으로써, **Foundation Model을 통째로 재학습하지 않고도 소형 사족 로봇 본체에 적응(domain adaptation)시키는 실용적 경로**를 제시했다. 이는 최신 대규모 VLA 모델을 저비용 로봇 플랫폼에 이식하려는 후속 연구·개발에 직접 활용 가능한 방법론적 기여로 평가된다.

### 2. 단일 task 시연을 넘어선 멀티태스크 통합 파이프라인
오픈소스 InternVLA의 공개 시연이 단일 navigation task에 머물러 있는 것과 달리, 본 시스템은 **Navigation, Pointing, Following, Backtracking 4종 task를 ROSA 기반 LLM 에이전트 위에 단일 파이프라인으로 통합**했다. 특히 LiDAR SLAM closed-loop 기반 자율 백트래킹은 InternVLA가 본래 다루지 않는 기능을 시스템 레벨에서 확장한 사례로, foundation model을 응용 task로 확장하는 구체적 설계 예시를 제공한다.

### 3. 자연어 기반 원격 로봇 운용 인터페이스
자체 개발한 **Go2 Monitor 웹 인터페이스**와 **Zenoh-bridge 기반 무선 ROS2 통신 스택**을 결합함으로써, **인터넷 연결만 있으면 원격지에서도 로봇의 실시간 카메라 피드를 확인하고 자연어 명령을 전송·실행**시킬 수 있는 구조를 완성했다. 이는 사족 로봇의 활용 범위를 연구실 데모를 넘어 **사람의 직접 접근이 제한되는 원격지·위험 환경·무인 시설** 등 실제 운용 시나리오로 확장할 수 있는 기반을 제공하며, 비전문가도 자연어만으로 로봇을 운용할 수 있다는 점에서 HRI(Human-Robot Interaction) 측면의 진입 장벽을 크게 낮춘 기여로 평가된다.
