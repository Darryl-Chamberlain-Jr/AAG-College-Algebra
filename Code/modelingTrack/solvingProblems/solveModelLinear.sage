concentrationA = random.randint(5, 20)
concentrationB = concentrationA + random.randint(10, 30)
totalConcentration = random.randint(concentrationA, concentrationB)
if float(concentrationA+concentrationB)/2.0 == totalConcentration:
    concentrationA = random.randint(5, 20)
    concentrationB = concentrationA + random.randint(10, 30)
    totalConcentration = random.randint(concentrationA, concentrationB)
totalVolume = random.randint(15, 30)
volumeA = round(float(  float(totalConcentration*totalVolume - concentrationB*totalVolume) / float(concentrationA - concentrationB)    ), 2)
volumeB = round(float(totalVolume), 2) - volumeA
treatedEqual = round( float(totalVolume) / 2.0 , 2)
randomValue = random.uniform(   int(min(volumeA, volumeB, treatedEqual)), int(max(volumeA, volumeB, treatedEqual))   )
while (randomValue == volumeA) or (randomValue == volumeB) or (randomValue == treatedEqual):
    randomValue = random.randint(   int(min(volumeA, volumeB, treatedEqual)), int(max(volumeA, volumeB, treatedEqual))   )
test_list = [volumeA, volumeB, treatedEqual, randomValue]
while len(set(test_list)) != len(test_list):
    concentrationA = random.randint(5, 20)
    concentrationB = concentrationA + random.randint(10, 30)
    totalConcentration = random.randint(concentrationA, concentrationB)
    if float(concentrationA+concentrationB)/2.0 == totalConcentration:
        concentrationA = random.randint(5, 20)
        concentrationB = concentrationA + random.randint(10, 30)
        totalConcentration = random.randint(concentrationA, concentrationB)
    totalVolume = random.randint(15, 30)
    volumeA = round(float(  float(totalConcentration*totalVolume - concentrationB*totalVolume) / float(concentrationA - concentrationB)    ), 2)
    volumeB = round(float(totalVolume), 2) - volumeA
    treatedEqual = round( float(totalVolume) / 2.0 , 2)
    randomValue = random.randint(   int(min(volumeA, volumeB, treatedEqual)), int(max(volumeA, volumeB, treatedEqual))   )
    while (randomValue == volumeA) or (randomValue == volumeB) or (randomValue == treatedEqual):
        randomValue = random.randint(   int(min(volumeA, volumeB, treatedEqual)), int(max(volumeA, volumeB, treatedEqual))   )
    test_list = [volumeA, volumeB, treatedEqual, randomValue]
#####
chooseFocus = random.randint(0, 1)
if chooseFocus == 0:
    volumeQuestion = volumeA
    concQuestion = concentrationA
    otherVolume = volumeB
    otherConc = concentrationB
else:
    volumeQuestion = volumeB
    concQuestion = concentrationB
    otherVolume = volumeA
    otherConc = concentrationA
##
displayStem = "Solve the modeling problem below, if possible."
displayProblem = "\\begin{center} \\textit{In CHM2045L, Brittany created a %d liter %d percent solution of chemical $\\chi$ using two different solution percentages of chemical $\\chi$. When she went to write her lab report, she realized she forgot to write the amount of each solution she used! If she remembers she used %d percent and %d percent solutions, what was the amount she used of the %d percent solution?} \\end{center}" %(totalVolume, totalConcentration, concentrationA, concentrationB, concQuestion)

option1 = ["%.2f" %volumeQuestion, "*This is the correct option.", 1]
option2 = ["%.2f" %otherVolume, "This is the concentration of %d percent solution." %otherConc, 0]
option3 = ["%.2f" %treatedEqual, "This would be correct if Brittany used equal parts of each solution.", 0]
option4 = ["%.2f" %randomValue, "This was a random value. If this was not a guess, contact the coordinator to talk about how you got this value.", 0]
option5 = ["\\text{There is not enough information to solve the problem.}", "You may have chose this if you thought you needed to know how much of the second solution was used in the problem. Remember that the total minus the first solution would give you the second amount used.", 0]
displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "\\textbf{General Comments:} Build the model exactly as you did in Module 9M. Then, solve for the volume you are looking for."

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "NoMathMode", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)