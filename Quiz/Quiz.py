import random

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(f"\nQ. {self.question}")
        for i, c in enumerate(self.choices, 1):
            print(f"{i}. {c}")

    def check(self, user):
        return self.answer == user

    def shuffle_choices(self):
        indexed = list(enumerate(self.choices))
        random.shuffle(indexed)

        self.choices = [c for _, c in indexed]

        for new_idx, (old_idx, _) in enumerate(indexed):
            if old_idx + 1 == self.answer:
                self.answer = new_idx + 1
                break

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])