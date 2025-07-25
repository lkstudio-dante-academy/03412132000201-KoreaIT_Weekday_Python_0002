import os
import sys

import random

"""
Python 연습 문제 13
- 바위/가위/보 게임 제작하기
- 사용자로부터 바위/가위/보 중 하나를 입력받는다
- 컴퓨터는 바위/가위/보 중 랜덤하게 선택한다
- 결과를 계산해서 승리 or 무승부 일 경우 게임을 다시 진행한다
- 패배 일 경우 전적을 출력하고 게임을 종료한다

Ex)
정수 (1. 바위, 2. 가위, 3. 보) 입력 : 1
결과 : 승리 (나 - 바위, 컴퓨터 - 가위)

정수 (1. 바위, 2. 가위, 3. 보) 입력 : 2
결과 : 무승부 (나 - 가위, 컴퓨터 - 가위)

정수 (1. 바위, 2. 가위, 3. 보) 입력 : 1
결과 : 패배 (나 - 바위, 컴퓨터 - 보)

전적 : 1 승 1 무 1 패
프로그램을 종료합니다.
"""


# Training 13
def start(args):
	nCount_Win = 0
	nCount_Draw = 0
	
	while True:
		nSelect_My = int(input("정수 (1. 바위, 2. 가위, 3. 보) 입력 : "))
		nSelect_Computer = random.randrange(0, 3) + 1
		
		nResult = getResultA(nSelect_My, nSelect_Computer)
		oStr_Result = resultToStr(nResult)
		
		oStr_MySelect = selectToStr(nSelect_My)
		oStr_ComputerSelect = selectToStr(nSelect_Computer)
		
		print(f"결과 : {oStr_Result} (나 - {oStr_MySelect}, 컴퓨터 - {oStr_ComputerSelect})\n")
		
		# 패배했을 경우
		if nResult == RESULT_LOSE:
			break
	
		nCount_Win += 1 if nResult == RESULT_WIN else 0
		nCount_Draw += 1 if nResult == RESULT_DRAW else 0

	print(f"전적 : {nCount_Win} 승 {nCount_Draw} 무 1 패")
	print("프로그램을 종료합니다.")


RESULT_WIN = 1
RESULT_DRAW = 2
RESULT_LOSE = 3

# 결과를 반환한다
def getResultA(a_nSelect_My, a_nSelect_Computer):
	oListResults = [
		[RESULT_DRAW, RESULT_WIN, RESULT_LOSE],
		[RESULT_LOSE, RESULT_DRAW, RESULT_WIN],
		[RESULT_WIN, RESULT_LOSE, RESULT_DRAW]
	]
	
	return oListResults[a_nSelect_My - 1][a_nSelect_Computer - 1]
	
	
# 결과를 반환한다
def getResultB(a_nSelect_My, a_nSelect_Computer):
	# 무승부 일 경우
	if a_nSelect_My == a_nSelect_Computer:
		return RESULT_DRAW
	
	nSelect_MyNext = (a_nSelect_My % 3) + 1
	return RESULT_WIN if nSelect_MyNext == a_nSelect_Computer else RESULT_LOSE


# 선택 -> 문자열로 변환한다
def selectToStr(a_nSelect):
	oListStrings = [
		"", "바위", "가위", "보"
	]
	
	return oListStrings[a_nSelect]


# 결과 -> 문자열로 변환한다
def resultToStr(a_nResult):
	oListStrings = [
		"", "승리", "무승부", "패배"
	]
	
	return oListStrings[a_nResult]
