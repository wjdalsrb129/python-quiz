# main.py

import json
import random  # ← 추가
from quiz import Quiz

class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self, filepath="state.json"):
        self.filepath = filepath
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.state = json.load(f)

        self.quiz_list = []
        for q in self.state["quizzes"]:
            self.quiz_list.append(
                Quiz(q["question"], q["choices"], q["answer"], q.get("hint", ""))  # ← hint 추가
            )

    def save(self):
        """state.json 저장"""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)

    def play_quiz(self):
        score = 0

        # ── 문제 수 선택 ──────────────────────────────
        total = len(self.quiz_list)
        print(f"\n현재 퀴즈 수: {total}개")

        while True:
            count = input(f"몇 문제를 풀까요? (1~{total}): ").strip()
            if count.isdigit() and 1 <= int(count) <= total:
                count = int(count)
                break
            print(f"⚠️  1~{total} 사이의 숫자를 입력하세요!")

        # ── 랜덤 출제 ─────────────────────────────────
        selected = random.sample(self.quiz_list, count)  # ← 랜덤으로 count개 선택

        print("\n===== 퀴즈 시작! =====")

        for i, quiz in enumerate(selected):
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
        print(f"총 {count}문제 중 {score}개 정답!")

        if score > self.state["best_score"]:
            self.state["best_score"] = score
            self.save()
            print(f"🏆 최고 점수 갱신! {score}점")
        else:
            print(f"현재 최고 점수: {self.state['best_score']}점")

    def add_quiz(self):
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

        new_quiz = {"question": question, "choices": choices, "answer": answer, "hint": ""}  # ← hint 추가
        self.state["quizzes"].append(new_quiz)
        self.quiz_list.append(Quiz(question, choices, answer))
        self.save()
        print("✅ 퀴즈가 추가되었습니다!")

    def list_quiz(self):
        print("\n===== 퀴즈 목록 =====")
        if not self.quiz_list:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quiz_list):
            print(f"\nQ{i+1}. {quiz.question}")
            for j, choice in enumerate(quiz.choices):
                print(f"  {j+1}. {choice}")
            print(f"  정답: {quiz.answer}번")
        print(f"\n총 {len(self.quiz_list)}개의 퀴즈가 있습니다.")

    def show_menu(self):
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 시작")
        print("2. 최고 점수 확인")
        print("3. 퀴즈 목록 보기")
        print("4. 퀴즈 추가")
        print("5. 종료")
        print("====================")

    def run(self):
        """메인 루프"""
        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                print(f"\n최고 점수: {self.state['best_score']}점")
            elif choice == "3":
                self.list_quiz()
            elif choice == "4":
                self.add_quiz()
            elif choice == "5":
                print("\n게임을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("\n잘못된 입력입니다. 1~5 중에서 선택하세요.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()