# Linking other python files to allow fleunt functionility
from core.quiz_engine import generate_quiz
from core.summary_ai import generate_summary
from core.pdf_export import export_summary_to_pdf

def run_quiz():
    topic = input("Enter topic: ")
    questions = generate_quiz(topic)
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j+1}. {opt}")
        ans = int(input("Your answer (1-4): ")) - 1
        correct = q['answer'][0]
        if ans == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct: {q['options'][correct]}")
        print(" ", q['explanation'])
    print(f"\n Score: {score}/{len(questions)}")

def run_summary():
    topic = input("Enter topic to summarize: ")
    summary = generate_summary(topic)
    print("\n" + summary)
    if input("Export to PDF? (y/n): ").lower() == "y":
        export_summary_to_pdf(summary)
        print("PDF saved as summary.pdf")

def main():
    print("Study-Assistant CLI")
    print("1. Quiz\n2. Summary\n3. Exit")
    choice = input("Choose: ")
    if choice == "1": run_quiz()
    elif choice == "2": run_summary()
    else: print("Goodbye!")

if __name__ == "__main__":
    main()

