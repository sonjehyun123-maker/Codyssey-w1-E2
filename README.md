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
## 게임 흐름
    (1) main.py -> Quizgame() 객체 생성 -> __init__ -> load()호출 
        ```
        game = QuizGame()
        game.run()
        ```

    (2) 데이터 로드 QuizGame.load() -> JSON파일 여부 확인 -> JSON을 Quiz 객체로 변환
        ```
        state.json 있음? -> JSON 읽어서 Quiz 객체 리스트로 변환
        state.json 없음? -> _init_data() 호출 -> 기본 퀴즈 5개 + best_score=0 생성 후 저장
        파일 깨짐?      -> 초기화
        ```

    (3) QuizGame.run() - 게임 시작 - get_int()로 1~5 입력 받고 아닐 시 재입력 요구
    ```
    ==========================================
                🎯 나만의 퀴즈 게임 🎯
    ==========================================
    1. 퀴즈 풀기
    2. 퀴즈 추가
    3. 퀴즈 목록
    4. 점수확인
    5. 종료
    입력>>
    ```
    (4) QuizGame.play() - 풀 문제수 입력 -> random.sample()로 n개 선택 ->
                            - shuffle_choices() → 보기 순서 섞기 + 정답 번호 재계산
                            - display()         → 문제 + 보기 출력
                            - get_int()         → 1~4 답 입력
                            - check()           → 정답 여부 확인, score++
                            -> 최고 점수 출력 (if score > best_score){best_score 갱신 json,self.best score 저장}
    (5) QuizGame.add() - 퀴즈 문제, 선택지, 정답 입력 -> Quiz객체 생성 -> quizzes리스트에 추가 -> json에 저장
    (6) QuizGame.show() - 퀴즈 목록을 메모리 리스트에서 불러와 출력
    (7) 점수 확인 -> self.best_score 출력
    (8) 종료 - 1. 5입력 / 2. ctul+c ctul+d -> 안전종료
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
    - 문제:
        1. 버그의 유래는? : 컴퓨터에 벌레가 끼어서
        2. 파이썬의 유래는? : 영국 코미드 그룹
        3. 파이썬의 창시자는? : Guido
        4. 자바와 자바스크립트의 관계는? : 관계 없음
        5. 1GB의 크기는? : 1024MB
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
```main.py
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
    - int: 소수점이 없는 숫자 = 정수
    - str: 글자들의 묶음 = 문자열
    - bool: 참과 거짓 판별 = 판별기
    - list: 여러개의 값을 순서대로 저장 = 묶음
    - dict: list에서 진화 / 여러가지 이름표 + 값 
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

## 파일입출력
 - 파일을 열고, 읽고, 쓰는 기본 과정
    - 열기: content = f.read()
    - 읽기: f = open("파일명", "명령")
        - r: 읽기 / w : 쓰기 / a : 추가
    - 쓰기: f = open("data.txt", "w")
            f.write("hello")
 - JSON 형식이 무엇이고, 왜 데이터 저장에 사용
    - JSON: 데이터를 구조화해서 저장하는 텍스트
    - 사용 이유 1. 구조유지 / 2. 파일로 저장 가능 / 3. 다양한언어에서 사용 가능
 - try/except 필요 이유
    - 오류로 인한 프로그램 중단 방지 및 흐름 유지, 데이터 손상 방지
    - 발생 가능한 실패 케이스: 

## Git기초
 - Git이란? : 파일 변경내용 관리도구
 - Git명령어
    - init : git 저장소 초기화
    - add : 새롭게 업데이트된 파일을 스테이징 영역에 올림
    - commit : 스테이징 파일을 로컬 저장소에 저장함 (+꼬리표)
    - push: github에 commit 한 내용을 올림
    - pull: github에서 commit 한 내용을 내려받음
    - checkout: 다른 브랜치로 이동하거나 특정 시점 파일 복구시 사용
    - clone: github에서 프로그램을 불러옴 git clone github주소 
 - 브랜치 : 작업 흐름을 분리하는 독립된 작업라인.
 ![브랜치 생성/병합](./images/git%20log%20--oneline%20--graph.png)
    - main안정 but 새로운 기능 추가 할 때 사용.
    -   main:     A --- B --- C
                         \
        feature:          D --- E
        
    - 브랜치 사용 순서
        1) git branch feature / 생성
        2) git switch feature / main->feature로 변경
        3) git switch main / feature->main으로 변경
        4) git merge feature / main + faeture해서 새로운 커밋 생성.
 - 원격저장소를 clone하고 pull로 변경사항 적용(스크린샷)

 ## 체크리스트
    []GitHub에 코드가 업로드되어 있고 10개 이상의 의미 있는 커밋이 존재
        - https://github.com/sonjehyun123-maker/Codyssey-w1-E2
        - 
    []커밋을 어떤 단위로 나누었고, 커밋 메시지 규칙
        - 초반 : 커밋을 규칙 없이 시간에 따라 적성하거나 신경 안씀
        - 후반 : 커밋을 하나의 작업을 끝난 후 하고 메세지에는 어떤 작업을 하였는지 작성.

    []Quiz와 QuizGame 등 클래스들의 책임을 어떻게 나눴는지 설명할 수 있는가?
        - Quiz: 데이터 관리, 보관
        - QuizGames: 게임흐름 진행 
            - Quiz 객체 리스트 배열
            - Quiz데이터를 활용하여 실제로 게임이 동작하게 함
            - json파일 없을시 기초데이터로 생성

    []state.json 데이터 구조(필드/중첩 구조)를 현재 형태로 설계한  + json으로 데잍 저장 이유/특징
        - 사람이 직접 읽고 수정 가능
        - Python 내장 json 모듈로 별도 설치 없이 사용 가능
        - to_dict() / from_dict()로 객체 ↔ JSON 변환이 단순함

    []퀴즈 데이터가 1000개 이상으로 늘어난다면 현재 JSON 저장 방식에 어떤 한계
        load()시 전체를 한 번에 메모리에 올림 → 데이터가 클수록 느려짐
        save()도 전체를 덮어씀 → 퀴즈 1개 추가해도 1000개 전부 다시 씀
        검색/필터 기능이 없어서 특정 퀴즈 찾으려면 전체 순회

    []만약 state.json이 손상되어 JSON 파싱에 실패한다면, 사용자가 데이터를 잃지 않도록 어떤 대응(복구/백업/초기화)이 가능한지 설명
        ① 백업 파일 유지
        save() 호출 시 state.json → state_backup.json 복사 후 저장
        손상 감지 시 백업에서 복구

        ② 임시 파일로 안전 저장
        state_tmp.json에 먼저 쓰고
        성공하면 state.json으로 이름 변경 (덮어쓰기 실패 방지)

        ③ 손상 감지 시 사용자에게 선택권 부여
        "파일 손상 - 1.백업복구 2.초기화" 선택하게 함

    []“정답 채점 방식(점수 계산)”이나 “퀴즈 구조(선택지 개수 등)” 요구사항이 바뀐다면, 어떤 파일/클래스/메서드를 수정
        -----------------------------------------------------
        변경 내용           |      수정 파일/메서드점수
        -----------------------------------------------------
        계산 방식           |      QuizGame.play()
        선택지 수 변경       |      Quiz.__init__, display(), get_int() 범위, _init_data()
        정답 채점 기준 변경   |      Quiz.check()
        -----------------------------------------------------

    []clone/pull 스크린샷 필요.
        - git clone (github주소)

    [] “입력 처리”, “게임 진행”, “데이터 저장/불러오기” 로직을 어떤 기준으로 분리했는지 설명할 수 있는가?
        - 분리 기준: 하나의 파일/클래스가 하나의 역할만 갖도록 함
        - main.py       : 게임 진입점 / 실행
        - Quiz.py       : 퀴즈 데이터 구조 
        - QuizGame.py   : 게임 진행+저장+불러오기 
        - utils.py      : 입력처리/안전 종료

    [] 클래스를 사용한 이유는 무엇이며, 함수만으로 구현할 때와 어떤 차이가 있는지 설명할 수 있는가?
        - 클래스 = 데이터 + 동작 : 객체를 생성하여 데이터, 동작을 한번에 동작하게 함.
        - 함수만으로 했을 때: 데이터와 동작이 묶여있지 않아 매번 return값을 넘기고 받아야함. + 함수 추적의 어려움.