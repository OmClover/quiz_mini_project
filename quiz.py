username = input("Enter your name: ")
choice = input("Are you ready to attempt the quiz? y/n: ")
questions = ["What is the closest planet to the Sun?","Which mammal is known to have the most powerful bite?","What is the smallest ocean in the world?"]
all_options = [["Venus","Mars","Mercury","Earth"],["Grizzly Bear","Hippopotamus","Lion","Alligator"],["Indian Ocean","Pacific Ocean","Arctic Ocean","Atlantic Ocean"]]
letters = ["A","B","C","D"]
# score = 0
is_continue = True

while is_continue:
    if choice == "y" or "":
        score = 0
        for i in range (3):
                print(f"\nQ{i+1}. {questions[i]}")
                current = all_options[i]
                for j in range (4):
                     print(f"{letters[j]}. {current[j]}")
                answer = input("Enter correct option: ")
                if answer.lower() == "a":
                     score +=1
                else:
                     score = score
        print("\n\n")
        print("="*40)
        print(f"Thanks {username} for attempting the quiz!\n")
        print(f"Your score is {score}/3 and Percentage is {(score/3)*100}")
        continue_ = input("\nDo you want to try again? y/n: ")
        if continue_.lower() == "y":
             is_continue = True
        elif continue_.lower() == "n":
             is_continue = False
        else:
             is_continue = False
    elif choice == "n":
        print("Okay, Good Bye!")
        break
    else:
        print("Enter correct choice")
        break
