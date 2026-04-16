# Valorant AI Anti-Cheat Behavior Detector

FPS 게임 플레이 데이터를 기반으로 핵 사용자를 탐지하는 AI 기반 안티치트 시스템입니다.

## Features
- FastAPI 기반 실시간 API 서버
- 플레이 로그 CSV 자동 생성
- 반응속도 분포 그래프
- 핵 비율 자동 리포트
- RandomForest 기반 머신러닝 모델
- 실시간 핵 유저 예측 API

## Detection Signals
- 비정상적으로 빠른 반응속도
- 과도한 에임 스냅
- 일정한 클릭 패턴
- 비정상적인 반동 제어

## API Endpoints
- `POST /detect`
- `GET /report`
- `POST /predict`

## Preview
reaction_graph.png

## Future Roadmap
- 실시간 웹 대시보드
- WebSocket 스트리밍
- 플레이어별 위험 점수 추적
- 딥러닝 기반 에임 패턴 분석