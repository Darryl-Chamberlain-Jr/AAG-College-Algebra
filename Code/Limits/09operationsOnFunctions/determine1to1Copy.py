import sys
import random
from sympy.abc import x

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

intervalRange = 5
precision = 1

def generateFunctionAndSolution():
    type = random.randint(0, 3)
    if (type==0):
        # Radical Function
        function, displayFunction = generateRadicalFunction()
        return [function, "yes", displayFunction]
    elif (type==1):
        # Poly with 1 unique zero, even degree
        function, displayFunction = generate1ZeroEvenDegree()
        return [function, "no", displayFunction]
    elif (type==2):
        # Poly with 1 unique zero, odd degree
        function, displayFunction = generate1ZeroOddDegree()
        return [function, "yes", displayFunction]
    else:
        # Poly with 2+ unique zeros
        function, displayFunction = generate2Zeros()
        return [function, "no", displayFunction]

def generateRadicalFunction():
    a = maybeMakeNegative(random.randint(3, 6))
    b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
    term = a*x+b
    function = sqrt(term)
    if b < 0:
        displayFunction = "\\sqrt{%d x - %d}" %(a, -b)
    else:
        displayFunction = "\\sqrt{%d x + %d}" %(a, b)
    return [function, displayFunction]

def generate1ZeroEvenDegree():
    a = maybeMakeNegative(random.randint(3, 6))
    b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
    term = a*x+b
    function = term**2
    if a*b < 0:
        displayFunction = "%d x^2 - %d x + %d" %(a**2, -2*a*b, b**2)
    else:
        displayFunction = "%d x^2 + %d x + %d" %(a**2, 2*a*b, b**2)
    return [function, displayFunction]

def generate1ZeroOddDegree():
    a = random.randint(3, 6)
    b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
    term = a*x+b
    function = term**3
    if b < 0:
        displayFunction = "(%d x - %d)^3" %(a, -b)
    else:
        displayFunction = "(%d x + %d)^3" %(a, b)
    return [function, displayFunction]

def generate2Zeros():
    a = maybeMakeNegative(random.randint(3, 6))
    b = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
    c = maybeMakeNegative(random.randint(3, 6))
    d = maybeMakeNegative(a*random.randint(3, 6) + random.randint(1, 6))
    term1 = a*x+b
    term2 = c*x+d
    function = term1*term2
    if (b*c+a*d) < 0 and b*d < 0:
        displayFunction = "%d x^2 - %d x - %d" %(a*c, -b*c-a*d, -b*d)
    elif (b*c+a*d) < 0 and b*d > 0:
        displayFunction = "%d x^2 - %d x + %d" %(a*c, -b*c-a*d, b*d)
    elif (b*c+a*d) > 0 and b*d < 0:
        displayFunction = "%d x^2 + %d x - %d" %(a*c, b*c+a*d, -b*d)
    else:
        displayFunction = "%d x^2 + %d x + %d" %(a*c, b*c+a*d, b*d)
    return [function, displayFunction]

functionAndSolution = generateFunctionAndSolution()

response1 = ["\\text{Yes, the function is 1-1.}"]
response2 = ["\\text{No, because there is an $x$-value that goes to 2 different $y$-values.}"]
response3 = ["\\text{No, because there is a $y$-value that goes to 2 different $x$-values.}"]
response4 = ["\\text{No, because the domain of the function is not $(-\\infty, \\infty)$.}"]
response5 = ["\\text{No, because the range of the function is not $(-\\infty, \\infty)$.}"]

if (functionAndSolution[1]=="yes"):
    response1.append("* This is the solution.")
    response2.append("Corresponds to the Vertical Line test, which checks if an expression is a function.")
    response3.append("Corresponds to the Horizontal Line test, which this function passes.")
    response4.append("Corresponds to believing 1-1 means the domain is all Real numbers.")
    response5.append("Corresponds to believing 1-1 means the range is all Real numbers.")
    response1.append(1)
    response2.append(0)
    response3.append(0)
    response4.append(0)
    response5.append(0)
else:
    response3.append("* This is the solution.")
    response1.append("Corresponds to believing the function passes the Horizontal Line test.")
    response2.append("Corresponds to the Vertical Line test, which checks if an expression is a function.")
    response4.append("Corresponds to believing 1-1 means the domain is all Real numbers.")
    response5.append("Corresponds to believing 1-1 means the range is all Real numbers.")
    response3.append(1)
    response2.append(0)
    response1.append(0)
    response4.append(0)
    response5.append(0)

answerList =  [response1, response2, response3, response4, response5]

if response_type=="Multiple-Choice":
	displayStem = "Determine whether the function below is 1-1."
else:
	displayStem="Determine whether the function below is 1-1. Provide reasoning for your response."
displayProblem = "f(x) = %s" %functionAndSolution[2]
displaySolution = "\\text{%s}" %functionAndSolution[1]
generalComment = "There are only two valid options: The function is 1-1 OR No because there is a $y$-value that goes to 2 different $x$-values."
random.shuffle(answerList)

c0 = "%s" %answerList[0][0]
c1 = "%s" %answerList[1][0]
c2 = "%s" %answerList[2][0]
c3 = "%s" %answerList[3][0]
c4 = "%s" %answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][1], answerList[1][1], answerList[2][1], answerList[3][1], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

# String, Math Mode, or Graph
displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
