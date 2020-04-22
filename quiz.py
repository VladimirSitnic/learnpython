score = 0
nextQuestion = "\n====================== \033[1;33;40mAnswer Question\033[0;37;40m ======================"
wrong = "\n                        \033[1;31;40mWrong answer!\033[0;37;40m"
goodJob = "\n                        \033[1;32;40mGOOD JOB!\033[0;37;40m"

question_answer = [
    ['\033[1;33;40m Q:\033[0;37;40m 2+2 || А.4   B.8   C.1   D.22: ', ['A', 'a', 'А', 'а', '4'] ],
    ['\033[1;33;40m Q:\033[0;37;40m 3/3 || A.33   B.1   C.9   D.6: ', ['B', 'b', 'Б', 'б', '1'] ],
    ['\033[1;33;40m Q:\033[0;37;40m 5+5+5*0:2,5 || A.4   B.5   C.10   D.0: ', ['C', 'c', 'С', 'с', '10'] ],
    ['\033[1;33;40m Q:\033[0;37;40m 100*2,5*2 || A.250   B.100   C.125   D.500: ', ['D', 'd', 'Д', 'д', '500'] ],
    ['\033[1;33;40m Q:\033[0;37;40m 10/3 || A.3,(33)   B.3,3   C.3   D.30: ', ['A', 'a', 'А', 'а', '3,(33)'] ],
    ['\033[1;33;40m Q:\033[0;37;40m 3^2 || A.3,(33)   B.3,3   C.9   D.30: ', ['C', 'c', 'С', 'с', '9'] ]
]

counter=0
for element in question_answer:
  print(nextQuestion)
  answer = input(question_answer[counter][0])
  answers = question_answer[counter][1]
  if answer in answers :
    print(goodJob)
    score += 1
  else:
    print(wrong)
  counter += 1

print('                     \033[1;34;40mYOUR SCORE IS:\033[0;37;40m'+ str(score) + '\\' + str(counter))




