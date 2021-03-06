import sys
import random
from math import exp
from math import log

DIR=sys.argv[1]
debug=sys.argv[2]
if debug == "save":
    database_name=sys.argv[3]
    question_list=sys.argv[4]
    version=sys.argv[5]
    thisQuestion=sys.argv[6]
    OS_type=sys.argv[7]
    response_type=sys.argv[8]
else:
    version="Z"
    thisQuestion="debug_image"
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForQuestionCode")
from commonlyUsedFunctions import *
from intervalMaskingMethod import *
sys.path.insert(1, f"/{DIR}/PythonScripts/ScriptsForDatabases")
from storeQuestionData import *

k, distractork, badk, badDistractork = 0, 0, 0, 0
duplicate = True

while duplicate == True:
    initialTemp = random.randint(10, 20)*10
    bathTemp = random.randint(10, 20)
    finalTemp = initialTemp - random.randint(40, 70)
    timePassed = random.randint(10, 40)
    A = initialTemp - bathTemp
    distractorA = initialTemp
    k = math.log( float(finalTemp - bathTemp) / float(A) ) / float( timePassed*math.log(math.exp(1)) )
    k_bad_initial_good_solve = math.log( float(finalTemp - bathTemp) / float(distractorA) ) / float( timePassed*math.log(math.exp(1)) )
    k_good_initial_bad_solve = -math.log(finalTemp - bathTemp) / float( timePassed*math.log(math.exp(1)*A) )
    k_bad_initial_bad_solve = -math.log(finalTemp - bathTemp) / float( timePassed*math.log(math.exp(1)*distractorA) )
    k_very_bad_initial_bad_solve = -math.log(finalTemp - bathTemp) / float( timePassed*math.log(math.exp(1)*bathTemp) )
    ### Checks list of values for duplicates
    checkList = [round(k, 5), round(k_bad_initial_good_solve, 5), round(k_good_initial_bad_solve, 5), round(k_bad_initial_bad_solve, 5), round(k_very_bad_initial_bad_solve, 5)]
    if len(checkList) == len(set(checkList)):
        duplicate = False
    else:
        duplicate = True
###
if response_type=="Multiple-Choice":
	displayStem = "The temperature of an object, $T$, in a different surrounding temperature $T_s$ will behave according to the formula $T(t) = Ae^{kt} + T_s$, where $t$ is minutes, $A$ is a constant, and k is a constant. Use this formula and the situation below to construct a model that describes the uranium's temperature, $T$, based on the amount of time t (in minutes) that have passed. Choose the correct constant $k$ from the options below."
else:
	displayStem = "The temperature of an object, $T$, in a different surrounding temperature $T_s$ will behave according to the formula $T(t) = Ae^{kt} + T_s$, where $t$ is minutes, $A$ is a constant, and k is a constant. Use this formula and the situation below to construct a model that describes the uranium's temperature, $T$, based on the amount of time t (in minutes) that have passed."
displayProblem = "Uranium is taken out of the reactor with a temperature of $%d^{\\circ}$ C and is placed into a $%d^{\\circ}$ C bath to cool. After %d minutes, the uranium has cooled to $%d^{\\circ}$ C." %(initialTemp, bathTemp, timePassed, finalTemp)

listedOrNot = random.randint(0, 1)
if listedOrNot == 0:
    option1 = ["k = %.5f" %(k_good_initial_bad_solve), "This uses $A$ correctly and solves for $k$ incorrectly.", 0]
    option2 = ["k = %.5f" %(k_bad_initial_bad_solve), "This uses $A$ as the initial temperature and solves for $k$ incorrectly.", 0]
    option3 = ["k = %.5f" %(k_very_bad_initial_bad_solve), "This uses $A$ as the bath temperature and solves for $k$ incorrectly.", 0]
    option4 = ["k = %.5f" %(k_bad_initial_good_solve), "This uses $A$ as the initial temperature and solves for $k$ correctly.", 0]
    option5 = ["\\text{None of the above}", "* This is the correct answer as $k = %.5f$." %(k), 1]
    displaySolution = option5[0]
else:
    option1 = ["k = %.5f" %(k), "* This is the correct option.", 1]
    option2 = ["k = %.5f" %(k_good_initial_bad_solve), "This uses $A$ correctly but solves for $k$ incorrectly.", 0]
    option3 = ["k = %.5f" %(k_bad_initial_bad_solve), "This uses $A$ as the initial temperature and solves for $k$ incorrectly.", 0]
    option4 = ["k = %.5f" %(k_bad_initial_good_solve), "This uses $A$ as the initial temperature and solves for $k$ correctly.", 0]
    option5 = ["\\text{None of the above}", "If you chose this, please contact the coordinator to discuss why you believe none of the other answers are correct.", 0]
    displaySolution = option1[0]

answerList = [option1, option2, option3, option4]
random.shuffle(answerList)

choices = [answerList[0][0], answerList[1][0], answerList[2][0], answerList[3][0], option5[0]]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], option5[1]]
potentialAnswers = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], option5[2]]

generalComment = "The initial temperature is when $t = 0$. Unlike power models, that means $A$ is not the initial temperature!"

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if potentialAnswers[answerIndex] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="String"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
