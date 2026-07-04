username = input("Enter your name: ")
questions = ["What is the closest planet to the Sun?","Which mammal is known to have the most powerful bite?","What is the smallest ocean in the world?"]
all_options = [["Venus","Mars","Mercury","Earth"],["Grizzly Bear","Hippopotamus","Lion","Alligator"],["Indian Ocean","Pacific Ocean","Arctic Ocean","Atlantic Ocean"]]
letters = ["a","b","c","d"]
answers_list = ["c","b","c"]
# score = 0
is_continue = True

choice = input("Are you ready to attempt the quiz? y/n: ").lower()

while is_continue:
    if choice == "y" or choice == "":
        score = 0
        for i in range (len(questions)):
                print(f"\nQ{i+1}. {questions[i]}")
                current = all_options[i]
                for j in range (len(current)):
                     print(f"{letters[j].upper()}. {current[j]}")
                while True:
                    answer = input("Enter correct option: ").lower()
                    if answer in letters:
                         if answer == answers_list[i]:
                              score +=1
                         else:
                              pass
                         break
                    else:
                         print("Invalid choice!!!, Please enter choice A,B,C or D")
        print("\n\n")
        print("="*40)
        print(f"Thanks {username} for attempting the quiz!\n")
        print(f"Your score is {score}/{len(questions)} and Percentage is {(score/(len(questions)))*100}")
        continue_ = input("\nDo you want to try again? y/n: ")
        if continue_.lower() == "y":
             is_continue = True
        else:
             print("Okay, Good Bye!")
             is_continue = False
    elif choice == "n":
        print("Okay, Good Bye!")
        break
    else:
        print("Enter correct choice")
        break
