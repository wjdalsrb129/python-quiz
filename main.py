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

# 메뉴 출력 함수
def show_menu():
    print("\n===== 퀴즈 게임 =====")
    print("1. 퀴즈 시작")
    print("2. 최고 점수 확인")
    print("3. 종료")
    print("====================")

# 메인 루프
while True:
    show_menu()
    choice = input("메뉴를 선택하세요: ").strip()

    if choice == "1":
        print("\n퀴즈를 시작합니다!")  # 5단계에서 구현 예정
    elif choice == "2":
        print(f"\n최고 점수: {state['best_score']}점")
    elif choice == "3":
        print("\n게임을 종료합니다. 안녕히 가세요!")
        break
    else:
        print("\n잘못된 입력입니다. 1~3 중에서 선택하세요.")