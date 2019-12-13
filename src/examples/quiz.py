def read_questions(filename):
    questions = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                question, answer = line.split('=')
                questions[question.strip()] = answer.strip()
    return questions


def ask_questions(questions):
    correct = []
    wrong = []

    for question, answer in questions.items():
        if input('%s = ' % question).strip() == answer:
            print("Correct!")
            correct.append(question)
        else:
            print("Wrong! The correct answer is %s." % answer)
            wrong.append(question)

    return (correct, wrong)


def stats(correct, wrong, questions):
    print("\n**** STATS ****\n")
    print("You answered", len(correct), "questions correctly and",
          len(wrong), "questions wrong.")

    if wrong:
        print("These would have been the correct answers:")
        for question in wrong:
            print(' ', question, '=', questions[question])


def main():
    filename = input("Name of the question file: ")
    questions = read_questions(filename)
    correct, wrong = ask_questions(questions)
    stats(correct, wrong, questions)


if __name__ == '__main__':
    main()
