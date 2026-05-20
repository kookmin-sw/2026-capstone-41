# InternNav

InternNav는 내비게이션 태스크를 위한 벤치마크 평가 프레임워크다.
이 저장소에는 Python 패키지, 학습/평가 스크립트, Go2 실로봇 보조 도구, ROS 2 모니터링 코드가 함께 들어 있다.

## 구성

- `internnav/`: 핵심 Python 패키지. agent, model, dataset, env, evaluator, trainer, config를 포함한다.
- `scripts/`: 학습, 평가, 데이터 변환, real-world 실행, IROS challenge 관련 스크립트.
- `requirements/`: 설치 목적별 의존성 목록.
- `go2_agent/`: ROSA 기반 Go2 agent와 도구 연동 코드.
- `go2_monitor/`: ROS 2 Humble 기반 C++ 웹 모니터링 서버. 자세한 내용은 `go2_monitor/README.md` 참고.
- `rosa/`: 로컬 ROSA 패키지 소스.
- `tests/`: unit/function 테스트.
- `docs/`: 변경 이력과 호환성 문서.
- `assets/`, `utils/`, `third_party/`: 샘플 데이터, 보조 유틸리티, 외부 코드.

## 설치

지원 Python 버전은 `3.8`부터 `3.12`까지다.

```bash
pip install -e .
```

목적별 추가 의존성:

```bash
pip install -e ".[habitat]"
pip install -e ".[isaac]"
pip install -e ".[model]"
pip install -e ".[internvla_n1]"
```

## 자주 쓰는 명령

```bash
pytest
python scripts/eval/eval.py
bash scripts/train/base_train/start_train.sh
```

Go2 monitor는 별도 ROS 2 빌드가 필요하다.

```bash
cd go2_monitor
# 자세한 빌드/실행 방법은 go2_monitor/README.md 참고
```

## 참고

- 패키지 이름: `internnav`
- 현재 버전: `0.3.1`
- 라이선스: Apache 2.0
- InternData-N1 변환 로직은 `v0.5` 데이터 구조를 기준으로 한다. 자세한 내용은 `docs/compatibility.md` 참고.
