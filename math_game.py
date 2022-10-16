import random

signs = ["+", "-", "*", "/"]
score = 0
print("MATH GAME")
print("Do you want to start?")
print("[Yes/No]")
Start_game = input()
while True:
    if Start_game == "Yes" or Start_game == "yes":
        print("Select difficulty")
        print("Easy/Normal/Hard")
        difficulty = input()
        for _ in range(10):
            while True:
                if difficulty == "Easy" or difficulty == "easy":
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    sign = random.choice(signs)
                    if sign == "/":
                        while True:
                            a = random.randint(1, 10)
                            b = random.randint(1, 10)
                            if a % b == 0:
                                break
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer != a / b:
                            score += 0
                            print(f"score = {score}")
                            break
                        else:
                            score += 1
                            print(f"score = {score}")
                            break
                    elif sign == "+":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a + b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "-":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a - b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "*":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a * b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                elif difficulty == "Normal" or difficulty == "normal":
                    a = random.randint(10, 100)
                    b = random.randint(10, 100)
                    sign = random.choice(signs)
                    if sign == "/":
                        while True:
                            a = random.randint(1, 100)
                            b = random.randint(1, 20)
                            if a % b == 0:
                                break
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer != a / b:
                            score += 0
                            print(f"score = {score}")
                            break
                        else:
                            score += 1
                            print(f"score = {score}")
                            break
                    elif sign == "+":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a + b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "-":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a - b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "*":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a * b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                elif difficulty == "Hard" or difficulty == "hard":
                    a = random.randint(100, 1000)
                    b = random.randint(100, 1000)
                    sign = random.choice(signs)
                    if sign == "/":
                        while True:
                            a = random.randint(100, 1000)
                            b = random.randint(10, 100)
                            if a % b == 0:
                                break
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer != a / b:
                            score += 0
                            print(f"score = {score}")
                            break
                        else:
                            score += 1
                            print(f"score = {score}")
                            break
                    elif sign == "+":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a + b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "-":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a - b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                    elif sign == "*":
                        print(f"{a} {sign} {b} = ?")
                        answer = input()
                        while True:
                            try:
                                answer = int(answer)
                                break
                            except:
                                print("Please enter number")
                                answer = input()
                        if answer == a * b:
                            score += 1
                            print(f"score = {score}")
                            break
                        else:
                            score += 0
                            print(f"score = {score}")
                            break
                else:
                    print("Please enter: easy or normal or hard ")
                    difficulty = input()
        if score <= 3:
            print("You lose")
            break
        elif 7 >= score >= 4:
            print("You can do better")
            break
        elif 9 >= score >= 8:
            print("Not bad")
            break
        elif score == 10:
            print("You win")
            break
        else:
            print("Skill issue")
            break
    elif Start_game == "No" or Start_game == "no":
        print("SKill issue")
        break
    else:
        print("Please enter: yes or no")
        Start_game = input()
input("Press any key to terminate the program")
