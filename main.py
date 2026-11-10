import json
from quiz import Quiz

# state.json 읽기
with open("state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# Quiz 객체 리스트 생성
quiz_list = []
for q in state["quizzes"]:
    quiz = Quiz(q["question"], q["choices"], q["answer"])
    quiz_list.append(quiz)