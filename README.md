# Codyssey-w1-E2
Codyssey 1주차 E2 문제

## 프로젝트 개요
    - 동작하는 퀴즈 게임 프로그램을 개발
    - python 기초 공부

## 퀴즈 주제 선정 이유
  - 주제: 프로그래밍에 관련된 알아도 그만 몰라도 그만 지식
    - 선정이유: 프로그래밍을 하며 알면 재미있는지식을 알리고 싶었습니다.

## 실행방법 및 기능
1) main.py 실행
2) 숫자입력에 따른 기능
    (1) 퀴즈풀기
        - 저장된 문제 출력/실행 // 점수 누적 및 점수 기억 
    (2) 퀴즈추가
        - 저장된 문제 이외에 사용자가 문제를 낼 수 있도록 함
    (3) 퀴즈목록
        - 저장된 문제 출력
    (4) 점수확인
        - 퀴즈 풀기(1)에서 저장된 최고 점수를 출력
    (5) 종료
        - eixt
    etc. 예외처리(숫자가 아닌 잘못된 입력 처리)
         데이터 저장(종료 후에도 데이터 유지)
         랜덤 문제/선택지 출력

## 파일 구조
 Quiz/
 ├── main.py        # 실행 진입점
 ├── Quizgame.py    # 게임 전체 로직
 ├── Quiz.py        # Quiz 클래스 (데이터)
 ├── utils.py       # 입력 처리 함수
 └── state.json     # 데이터 저장/불러오기 파일

## 데이터 파일 설명
### state.json
    - 위치: Qize 디렉토리
    - 역할: 퀴즈 데이터 및 최고 점수 함수 저장
```JSON
{ "quizzes": [ //저장된 퀴즈 목록
    {
      "question": "문제 내용",
      "choices": ["보기1", "보기2", "보기3", "보기4"],
      "answer": 1 //정답 번호
    }
  ],
  "best_score": 3 //최고점수 저장
}
```

### main.py
    - 위치: Qize 디렉토리
    - 역할: 퀴즈 게임 실행 및 종료
```M
from Quizgame import QuizGame

def main():
    game = QuizGame()

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n안전 종료")
        game.save()

if __name__ == "__main__":
    main()
```

## Python 기초
 - 변수란? : 값이 들어가있는 공간. (변경 가능)
 - int, str, bool, list, dict의 차이
 - if/elif/else로 조건
    - if : 만약이라는 뜻으로 조건을 달아 아래 명령 실행
    - elif : if가 아닌 다른 조건으로 명령 실행
    - else : if도 elif도 아닌 나머지 가능성 모두
 - for와 while의 차이
    - for : 정해진 횟수까지 반복
    - while : 정해진 조건까지 반복
 - 함수를 정의하고, 매개변수와 반환값을 활용
    - 함수 정의 
        - def main():dsply(self): save(self): load(self) run(self), play(self), add(self), show(self) etc...
    - 매개변수와 반환값 활용
        - Quiz생성: Quiz(question, choices, answer)

## 클래스와 객체
 - 클래스란? : 데어터 속성 + 데이터를 다루는 매서드
 - __init__ 메서드와 self의 역할
    - __init__역할 : 생성된 객체 초기화, 초기 값 설정.
    - self역할 : QizeGame내 속성과 메서드에 접근할수 있게함.
    ```QuizGame
        def __init__(self):
        self.quizzes = []   #퀴즈 목록
        self.best_score = 0 #최고점수
        self.load()         #시작 시 데이터를 가져옴.
    ```

