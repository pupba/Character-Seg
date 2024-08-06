#!/bin/bash

# 가상환경 이름 설정
VENV_NAME="venv"

# 가상환경이 존재하는지 확인
if [ ! -d "$VENV_NAME" ]; then
    # 가상환경 생성
    python3 -m venv $VENV_NAME
fi

# 가상환경 활성화
source $VENV_NAME/bin/activate

# requirements.txt 설치
pip install --upgrade pip
if [[ "$1" == "--gpu" ]]; then
    # GPU용 requirements.txt가 있는지 확인
    if [ -f requirements_gpu.txt ]; then
        echo "Installing GPU requirements..."
        pip install -r requirements_gpu.txt
    else
        echo "requirements_gpu.txt 파일이 없습니다."
    fi
else
    # 기본 requirements.txt 설치
    echo "Installing regular requirements..."
    pip install -r requirements.txt
fi

# 파라미터를 전달하여 Python 스크립트 실행
python3 app.py

# 가상환경 비활성화
deactivate