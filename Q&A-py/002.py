from string import ascii_lowercase
import random
import tomli
NUM_QUESTIONS_PER_QUIZ = 5
with open("D:/_python_/_ask Q_/Q2.toml", mode="rb") as toml_file:
    
    questions = tomli.load(toml_file)
    
name = input("What is your name? \n")
print(f'''
      ⭐Hello, this game is made for you, dear {name}⭐
          The rules of this game are very simple:
1- There are 4 topics in each stage, you choose one topic
2- Choose the correct option among the 4 options that are given to you
3- If your answer is correct, 1 point will be given to you and if it is wrong, 
    0.5 points will be deducted from you
                have fun ;)
      ''') 
print()
print('''
for:
    History -> H
    Movie -> M
    python -> P
      
      ''')
mark = 0
list_1 = ["M","H","P"]
topic = input('select your topic:\n')

t = None
qu = None
a = None
def check_topic(topic):
    global qu
    global t
    global a
    if topic == 'P':
        qu = questions.get('python')
        t = 'python'
        a = len(qu)
        print(f'''
              ***In this game, you have to get {a} points,
                      otherwise you are a loser***
              ''')
    elif topic == 'H':
        qu = questions.get('History')
        t = 'History'
        a = len(qu)
        print(f'''
              ***In this game, you have to get {a} points,
                      otherwise you are a loser***
              ''')
    elif topic == 'M':
        qu = questions.get('Movie')
        t = 'Movie'
        a = len(qu)
        print(f'''
              ***In this game, you have to get {a} points,
                      otherwise you are a loser***
              ''')
    else:
        while topic not in list_1:
            print(f"What you typed is not correct. Please choose from {list_1}")
            topic = input('select your topic:\n')
        check_topic(topic)
    
check_topic(topic)





num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(qu))

questions1 = random.sample(list(qu.items()), k=num_questions)

point = 0
for num, (question, alternatives) in enumerate(questions1, start=1):
    
    print(f"⭐{t}⭐ \n Question {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
    zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
)
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        point += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        point -= 0.5
print(f"\nYou got {point} point of {num} questions")