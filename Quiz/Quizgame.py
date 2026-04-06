import json, os, random
from Quiz import Quiz
from utils import get_int

STATE = "state.json" #저장파일

class QuizGame:
    def __init__(self):
        self.quizzes = []   #퀴즈 목록
        self.best_score = 0 #최고점수
        self.load()         #시작 시 데이터를 가져옴.

    def load(self):
        try:
            # 파일 없으면 초기 데이터 생성
            if not os.path.exists(STATE):
                self._init_data()
                return
            #JSON파일 생성
            with open(STATE, encoding="utf-8") as f:
                data = json.load(f)
            # JSON → 객체 변환
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", 0)

        except:
            # 파일 깨지면 초기화
            print("파일 손상 → 초기화")
            self._init_data()

    def save(self):
        # 객체 → JSON 저장        
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }

        with open(STATE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def _init_data(self):
        self.quizzes = [
            Quiz("2+2=?", ["1","2","3","4"], 4),
            Quiz("대한민국 수도는?", ["서울","부산","대구","광주"], 1),
            Quiz("파이썬 창시자는?", ["Guido","Elon","Bill","Jobs"], 1),
            Quiz("CPU는?", ["중앙처리장치","RAM","SSD","GPU"], 1),
            Quiz("HTML은?", ["마크업 언어","프로그래밍","OS","DB"], 1),
        ]
        self.best_score = 0
        self.save()

    def run(self):
        while True:
            print("========================================\n")
            print("\t 🎯 나만의 퀴즈 게임 🎯\t\n")
            print("========================================")
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수확인\n5. 종료")
            print("========================================\n")
            try:
                c = get_int("선택: ", 1, 5)
            except:
                raise

            if c == 1: self.play()
            elif c == 2: self.add()
            elif c == 3: self.show()
            elif c == 4: print("최고 점수:", self.best_score)
            elif c == 5:
                self.save()
                print("종료")
                break
# 퀴즈 진행
    def play(self):
        if not self.quizzes:
            print("퀴즈 없음")
            return

        count = get_int("몇 문제 풀래? ", 1, len(self.quizzes))
        selected = random.sample(self.quizzes, count)

        score = 0

        for q in selected:
            q.shuffle_choices() #rand%
            q.display()         #출력

            ans = get_int("답: ", 1, 4)

            if q.check(ans):
                print("정답")
                score += 1
            else:
                print(f"오답 (정답: {q.answer})")

        print(f"점수: {score}/{count}")
#현 스코어 > 최고 스코어
        if score > self.best_score:
            self.best_score = score
            print("최고 점수 갱신")
            self.save()
#문제 추가
    def add(self):
        question = input("문제: ").strip()

        choices = []
        for i in range(4):
            while True:
                c = input(f"선택지 {i+1}: ").strip()
                if c:
                    choices.append(c)
                    break
                print("빈 입력 불가")

        ans = get_int("정답 번호 (1~4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, ans))
        self.save()

        print("추가 완료")
#퀴즈 목록 출력
    def show(self):
        if not self.quizzes:
            print("퀴즈 없음")
            return

        print("\n===== 퀴즈 목록 =====")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")