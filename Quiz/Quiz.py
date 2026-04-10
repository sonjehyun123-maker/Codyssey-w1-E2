import random

class Quiz:
# 문제, 선택지, 정답 저장
    def __init__(self, question, choices, answer):

        self.question = question # 퀴즈 데이터 저장 //play, show
        self.choices = choices # 최고점수 비교 갱신
        self.answer = answer 
#문제 출력
    def display(self):
        print(f"\nQ. {self.question}")
        for i, c in enumerate(self.choices, 1):
            print(f"{i}. {c}") #선택지 번호와 함꼐 출력

#정답 확인
    def check(self, user):
        return self.answer == user

#정답 ,선택지 rand%
    def shuffle_choices(self): #
        indexed = list(enumerate(self.choices)) #각 선택지 섞은 번호 리스트
        random.shuffle(indexed) #번호 붙은 선택지를 섞음.

        self.choices = [c for _, c in indexed]  #섞은 선택지를 다시 self.choices로 만듬.
        #정답위치 다시 계산
        for new_idx, (old_idx, _) in enumerate(indexed):
            if old_idx + 1 == self.answer: # 이 선택지가 원래 정답이었는지 확인
                self.answer = new_idx + 1 #새로운 정답 저장
                break

# JSON 저장용 변환
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @staticmethod
    def from_dict(data):
        #정답, 선택지, 답 JSON->객체
        return Quiz(data["question"], data["choices"], data["answer"])