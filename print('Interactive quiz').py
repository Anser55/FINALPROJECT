print('Interactive quiz')

def run_quiz():
    questions = {
        "Who is the National Hero of the Philippines": "Jose Rizal",
        "Where is USM located at(town)?": "4",
        "What is my nickname?": "Anser"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + answer)

    print("Quiz completed! You scored {} out of {}.".format(score, len(questions)))

if __name__ == "__main__":
    run_quiz()
