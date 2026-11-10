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

# 퀴즈 풀기 함수
def play_quiz():
    score = 0
    print("\n===== 퀴즈 시작! =====")

    for i, quiz in enumerate(quiz_list):
        print(f"\nQ{i+1}. {quiz.question}")
        for j, choice in enumerate(quiz.choices):
            print(f"  {j+1}. {choice}")

        answer = input("정답 번호를 입력하세요: ").strip()

        if answer == str(quiz.answer):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 오답입니다! 정답은 {quiz.answer}번이에요.")

    print(f"\n===== 결과 =====")
    print(f"총 {len(quiz_list)}문제 중 {score}개 정답!")

    # 최고 점수 갱신
    if score > state["best_score"]:
        state["best_score"] = score
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        print(f"🏆 최고 점수 갱신! {score}점")
    else:
        print(f"현재 최고 점수: {state['best_score']}점")

def add_quiz():
    print("\n===== 퀴즈 추가 =====")
    question = input("문제를 입력하세요: ").strip()

    choices = []
    for i in range(4):
        choice = input(f"보기 {i+1}번을 입력하세요: ").strip()
        choices.append(choice)

    while True:
        answer = input("정답 번호를 입력하세요 (1~4): ").strip()
        if answer in ["1", "2", "3", "4"]:
            answer = int(answer)
            break
        print("⚠️ 1~4 중에서 입력하세요!")

    # 새 퀴즈 추가
    new_quiz = {
        "question": question,
        "choices": choices,
        "answer": answer
    }
    state["quizzes"].append(new_quiz)
    quiz_list.append(Quiz(question, choices, answer))

    # state.json 저장
    with open("state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print("✅ 퀴즈가 추가되었습니다!")

def list_quiz():
    print("\n===== 퀴즈 목록 =====")
    if not quiz_list:
        print("등록된 퀴즈가 없습니다.")
        return
    for i, quiz in enumerate(quiz_list):
        print(f"\nQ{i+1}. {quiz.question}")
        for j, choice in enumerate(quiz.choices):
            print(f"  {j+1}. {choice}")
        print(f"  정답: {quiz.answer}번")
    print(f"\n총 {len(quiz_list)}개의 퀴즈가 있습니다.")

# 메뉴 출력 함수
def show_menu():
    print("\n===== 퀴즈 게임 =====")
    print("1. 퀴즈 시작")
    print("2. 최고 점수 확인")
    print("3. 퀴즈 목록 보기")   # ← 새로 추가
    print("4. 퀴즈 추가")        # ← 3에서 4로
    print("5. 종료")             # ← 4에서 5로
    print("====================")
    
# 메인 루프
while True:
    show_menu()
    choice = input("메뉴를 선택하세요: ").strip()

    if choice == "1":
        play_quiz()
    elif choice == "2":
        print(f"\n최고 점수: {state['best_score']}점")
    elif choice == "3":
        list_quiz()          # ← 새로 추가
    elif choice == "4":
        add_quiz()           # ← 3에서 4로
    elif choice == "5":      # ← 4에서 5로
        print("\n게임을 종료합니다. 안녕히 가세요!")
        break
    else:
        print("\n잘못된 입력입니다. 1~5 중에서 선택하세요.")