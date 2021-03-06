import sys
import numpy
import random

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

def createAllCoefficients():
    c0 = maybeMakeNegative(random.randint(3, 9))
    c1 = maybeMakeNegative(random.randint(3, 9))
    c2 = abs(c1) + random.randint(1, 3)
    c3 = maybeMakeNegative(random.randint(3, 9))
    c4 = maybeMakeNegative(random.randint(3, 9))
    c5 = abs(c4) + random.randint(1, 3)
    coefficients = [c0, c1, c2, c3, c4, c5]
    smallerEndpoint = float(-c0/(c1-c2))
    largerEndpoint = float(-c3/(c4-c5))
    while (largerEndpoint <= smallerEndpoint):
        c0 = maybeMakeNegative(random.randint(3, 9))
        c1 = maybeMakeNegative(random.randint(3, 9))
        c2 = abs(c1) + random.randint(1, 3)
        c3 = maybeMakeNegative(random.randint(3, 9))
        c4 = maybeMakeNegative(random.randint(3, 9))
        c5 = abs(c4) + random.randint(1, 3)
        coefficients = [c0, c1, c2, c3, c4, c5]
        smallerEndpoint = float(-c0/(c1-c2))
        largerEndpoint = float(-c3/(c4-c5))
    return coefficients

def createIntervalFromGreaterThanInequality(coefficients):
    a, b, c = coefficients
    left = numpy.poly1d([b, a])
    right = numpy.poly1d([c, 0])
    diff_of_left_right= left-right
    endpoint = diff_of_left_right.r
    return [0, endpoint[0]]

def createIntervalFromLessThanInequality(coefficients):
    a, b, c = coefficients
    left = numpy.poly1d([b, a])
    right = numpy.poly1d([c, 0])
    diff_of_left_right= left-right
    endpoint = diff_of_left_right.r
    return [endpoint[0], 0]

def distractorNegateAndInverseDomain(intervalPresentation):
    a, b = intervalPresentation
    return [-b, -a]

def intervalCupInclusive(solutionInterval):
    a, b = solutionInterval
    return "(-\\infty, a] \\cup [b, \\infty)"

def intervalCupExclusive(solutionInterval):
    a, b = solutionInterval
    return "(-\\infty, a) \\cup (b, \\infty)"

def extractValue(solutionInterval):
    a, b = solutionInterval
    if(a == 0):
        return b
    else:
        return a

# Type 1 - "or"
# block[0] + block[1]*x > block[2]*x "or" block[3] + block[4]*x < block[5]*x

allCoefficients = createAllCoefficients()
factor1Coefficients = [allCoefficients[0], allCoefficients[1], allCoefficients[2]]
factor2Coefficients = [allCoefficients[3], allCoefficients[4], allCoefficients[5]]
intervalLeft = createIntervalFromGreaterThanInequality(factor1Coefficients)
intervalRight = createIntervalFromLessThanInequality(factor2Coefficients)
endpointLeft = extractValue(intervalLeft)
endpointRight = extractValue(intervalRight)
solution = [float(endpointLeft), float(endpointRight)]

while (abs(solution[0])==abs(solution[1]) or abs(solution[0])<1 or abs(solution[1])<1 or abs(abs(solution[0])-abs(solution[1])) < 1 ):
    allCoefficients = createAllCoefficients()
    factor1Coefficients = [allCoefficients[0], allCoefficients[1], allCoefficients[2]]
    factor2Coefficients = [allCoefficients[3], allCoefficients[4], allCoefficients[5]]
    intervalLeft = createIntervalFromGreaterThanInequality(factor1Coefficients)
    intervalRight = createIntervalFromLessThanInequality(factor2Coefficients)
    endpointLeft = extractValue(intervalLeft)
    endpointRight = extractValue(intervalRight)
    solution = [float(endpointLeft), float(endpointRight)]

if factor1Coefficients[1] < 0:
    displayLeftFactor = "%s - %s x > %s x" %(factor1Coefficients[0], -factor1Coefficients[1], factor1Coefficients[2])
else:
    displayLeftFactor = "%s + %s x > %s x" %(factor1Coefficients[0], factor1Coefficients[1], factor1Coefficients[2])

if factor2Coefficients[1] < 0:
    displayRightFactor = "%s - %s x < %s x" %(factor2Coefficients[0], -factor2Coefficients[1], factor2Coefficients[2])
else:
    displayRightFactor = "%s + %s x < %s x" %(factor2Coefficients[0], factor2Coefficients[1], factor2Coefficients[2])

distractor1 = distractorNegateAndInverseDomain(solution)
distractor2 = solution
distractor3 = distractorNegateAndInverseDomain(solution)

solutionListA = [solution, distractor1]
solutionListB = [distractor2, distractor3]
intervalOptionsA = createIntervalOptions(solutionListA, 4, 0.75)
intervalOptionsB = createIntervalOptions(solutionListB, 4, 0.75)

solutionInterval = [intervalCupExclusive(solution), intervalOptionsA[0], ' * Correct option.', 1]
distractor1Interval = [intervalCupExclusive(solution), intervalOptionsA[1], "Corresponds to inverting the inequality and negating the solution.", 0]
distractor2Interval = [intervalCupInclusive(solution), intervalOptionsB[0], "Corresponds to including the endpoints (when they should be excluded).", 0]
distractor3Interval = [intervalCupInclusive(solution), intervalOptionsB[1], "Corresponds to including the endpoints AND negating.", 0]
# Distractor4Interval is all real numbers. "(-\\infty, \\infty)"
if response_type=="Multiple-Choice":
    displayStem = 'Solve the linear inequality below. Then, choose the constant and interval combination that describes the solution set.'
else:
    displayStem = 'Solve the linear inequality below.'
displayProblem = '%s \\text{ or } %s' %(displayLeftFactor, displayRightFactor)
displaySolution = "(-\\infty, %s) \\text{ or } (%s, \\infty)" %(round(solution[0], 3), round(solution[1], 3))
generalComment = "When multiplying or dividing by a negative, flip the sign."

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval]
random.shuffle(answerList)
answerList.append(["(-\\infty, \\infty)", "Corresponds to the variable canceling, which does not happen in this instance.", 0, 0])

c0 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[0][0], answerList[0][1][0][0], answerList[0][1][0][1], answerList[0][1][1][0], answerList[0][1][1][1])
c1 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[1][0], answerList[1][1][0][0], answerList[1][1][0][1], answerList[1][1][1][0], answerList[1][1][1][1])
c2 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[2][0], answerList[2][1][0][0], answerList[2][1][0][1], answerList[2][1][1][0], answerList[2][1][1][1])
c3 = "%s, \\text{ where } a \\in [%s, %s] \\text{ and } b \\in [%s, %s]" %(answerList[3][0], answerList[3][1][0][0], answerList[3][1][0][1], answerList[3][1][1][0], answerList[3][1][1][1])
c4 = "%s" %answerList[4][0]
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][1]]

answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if answerList[answerIndex][3] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

displayStemType="String"
displayProblemType="Math Mode"
displayOptionsType="Math Mode"
if debug=="save":
    writeToDatabase(OS_type, DIR, database_name, question_list, thisQuestion, displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
else:
    print_for_debugger(displayStemType, displayStem, displayProblemType, displayProblem, displayOptionsType, choices, choiceComments, displaySolution, answerLetter, generalComment)
