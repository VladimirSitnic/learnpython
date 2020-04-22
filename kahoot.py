score = 0
nextQuestion = "======================NEXT QUESTION======================"
wrong = "                          WRONG!"
goodJob = "                        GOOD JOB!"
print(nextQuestion)
answer = input("first question:2+2|| А.4   B.8   C.1   D.22: ")
if answer == "A" or answer == "a" or answer == "А" or answer == "а" or answer == "4":
    print()
    print(goodJob)
    score += 1
else:
    print()
    print(wrong)

print()
print(nextQuestion)
answer = input("next question:3/3||A.33   B.1   C.9   D.6: ")
if answer == "B" or answer == "b" or answer == "Б" or answer == "б" or answer == "1":
    print()
    print(goodJob)
    score += 1
else:
    print()
    print(wrong)

print()
print(nextQuestion)
answer = input("next question:5+5+5*0:2,5||A.4   B.5   C.10   D.0: ")
if answer == "C" or answer == "c" or answer == "С" or answer == "с" or answer == "10":
    print()
    print(goodJob)
    score+=1
else:
    print()
    print(wrong)

print()
print(nextQuestion)
answer = input("next question:100*2,5*2||A.250   B.100   C.125   D.500: ")
if answer == "D" or answer == "d" or answer == "Д" or answer == "д" or answer == "500":
    print()
    print(goodJob)
    score+=1
else:
    print()
    print(wrong)

print()
print(nextQuestion)
answer = input("next question:10/3||A.3,(33)   B.3,3   C.3   D.30: ")
if answer == "A" or answer == "a" or answer == "А" or answer == "а" or answer == "3,(33)":
    print()
    print(goodJob)
    score+=1
else:
    print()
    print(wrong)
    
print("                     YOUR SCORE IS:"+ str(score) + "\5")

