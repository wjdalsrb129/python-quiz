# quiz.py

class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        """
        question : 질문 문자열
        choices  : 보기 4개 리스트  ex) ["Python", "Java", "C", "Ruby"]
        answer   : 정답 번호 (1~4)  ex) 1
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """퀴즈 문제와 보기를 출력"""
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        """
        user_answer : 사용자가 입력한 번호 (int)
        정답이면 True, 오답이면 False 반환
        """
        return self.answer == user_answer