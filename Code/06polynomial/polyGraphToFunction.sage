from sympy.abc import x
from sympy import *
import random
import matplotlib.pyplot as plt
import numpy

# OBJECTIVE 1 - Convert between a polynomial function and its graph.
# Types of problems
    # Type 1 - Function to graph
    # Type 2 - Graph to function

# We only need one type for this test. It might be easier to do
    # Graph to function

# In the future: Plot zeros and where derivative is zero.

# Type 2 - Graph to function
    # Students should be able to determine the graph based on
        # the end behavior and degree of the polynomial.

checkMax = 1000
checkMin = 1000
while checkMax > 100 or checkMin < -100:
    aCoeff = (-1)**random.randint(0, 1)
    degree = random.randint(3, 6)
    listRandomZeros = range(-4, 4)
    randomZeros = random.sample(listRandomZeros, 3)
    xMinimum = min(randomZeros)-0.5
    xMaximum = max(randomZeros)+0.5
    randomEvenPower = [random.randint(1, 5)*2, random.randint(1, 5)*2, random.randint(1, 5)*2]
    randomOddPower = [random.randint(1, 5)*2+1, random.randint(1, 5)*2+1, random.randint(1, 5)*2+1]
    if degree == 6:
        equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])**2
    elif degree ==5:
        equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    elif degree ==4:
        equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    else:
        equationOfGraph = aCoeff*(x-randomZeros[0]) * (x-randomZeros[1]) * (x-randomZeros[2])
    checkMax = equationOfGraph.subs(x, xMaximum)
    checkMin = equationOfGraph.subs(x, xMinimum)

def displayFactor(a):
    if a == 0:
        factor = "x"
    elif a < 0:
        factor = "(x + %d)" %-a
    else:
        factor = "(x - %d)" %a
    return factor

def displayEquation(a, z1, e1, z2, e2, z3, e3):
    if z2 == 0:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z2), e2, displayFactor(z1), e1, displayFactor(z3), e3)
    elif z3 == 0:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z3), e3, displayFactor(z1), e1, displayFactor(z2), e2)
    else:
        equation = "%d%s^{%s} %s^{%s} %s^{%s}" %(a*random.randint(2, 20), displayFactor(z1), e1, displayFactor(z2), e2, displayFactor(z3), e3)
    return equation

def randomPower(type):
    if type == 1:
        power = random.randint(2, 5)*2+1
    elif type == 2:
        power = random.randint(2, 5)*2
    else:
        power=0
        print("You input an invalid type. Use 1 for odd power and 2 for even power.")
    return power

if degree == 6:
    equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])**2
    displayEquationOfGraph = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(2))
    #
    xPlot = numpy.arange(xMinimum, xMaximum, 0.05)
    solutionGraph = aCoeff*(xPlot-randomZeros[0])**2 * (xPlot-randomZeros[1])**2 * (xPlot-randomZeros[2])**2
    plt.rcParams.update({'font.size': 36})
    showPlot = plt.plot(xPlot, solutionGraph, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/polyGraphToFunction' + str(version) + '.png', bbox_inches='tight')
    plt.close()
    # Distractors #
    negativeEquation = -aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])**2
    displayNegativeEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(2))
    #
    oneZeroOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayOneZeroOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    d4comment = "The factor $%s$ should have an even power." %displayFactor(randomZeros[2])
    #
    twoZerosOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayTwoZerosOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    d1comment = "The factors $%s$ and $%s$ should both have even powers." %(displayFactor(randomZeros[1]), displayFactor(randomZeros[2]))
    #
    negativeOneZeroOffEquation = - aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayNegativeOneZeroOffEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    d2comment = "The factor $%s$ should have an even power and the leading coefficient should be the opposite sign." %displayFactor(randomZeros[2])
    #####

elif degree ==5:
    equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayEquationOfGraph = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    #
    xPlot = numpy.arange(xMinimum, xMaximum, 0.05)
    solutionGraph = aCoeff*(xPlot-randomZeros[0])**2 * (xPlot-randomZeros[1])**2 * (xPlot-randomZeros[2])
    plt.rcParams.update({'font.size': 36})
    showPlot = plt.plot(xPlot, solutionGraph, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/polyGraphToFunction' + str(version) + '.png', bbox_inches='tight')
    plt.close()
    # Distractors #
    negativeEquation = -aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayNegativeEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    #
    oneZeroOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayOneZeroOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    d4comment = "The factor $%s$ should have an even power." %displayFactor(randomZeros[1])
    #
    twoZerosOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])**2
    displayTwoZerosOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(2))
    d1comment = "The factor $%s$ should have an even power and the factor $%s$ should have an odd power." %(displayFactor(randomZeros[1]), displayFactor(randomZeros[2]))
    #
    negativeOneZeroOffEquation = - aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])**2
    displayNegativeOneZeroOffEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(2))
    d2comment = "The factor $%s$ should have an odd power and the leading coefficient should be the opposite sign." %displayFactor(randomZeros[2])
    #####

elif degree ==4:
    equationOfGraph = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayEquationOfGraph = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    #
    xPlot = numpy.arange(xMinimum, xMaximum, 0.05)
    solutionGraph = aCoeff*(xPlot-randomZeros[0])**2 * (xPlot-randomZeros[1]) * (xPlot-randomZeros[2])
    plt.rcParams.update({'font.size': 36})
    showPlot = plt.plot(xPlot, solutionGraph, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/polyGraphToFunction' + str(version) + '.png', bbox_inches='tight')
    plt.close()
    # Distractors #
    negativeEquation = -aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayNegativeEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    #
    oneZeroOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayOneZeroOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    d4comment = "The factor $%s$ should have an odd power." %displayFactor(randomZeros[1])
    #
    twoZerosOffEquation = aCoeff*(x-randomZeros[0]) * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayTwoZerosOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(1), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    d1comment = "The factor $%s$ should have an even power and the factor $%s$ should have an odd power." %(randomZeros[0], randomZeros[1])
    #
    negativeOneZeroOffEquation = - aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])**2
    displayNegativeOneZeroOffEquation= displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(2))
    d2comment = "The factor $%s$ should have an odd power and the leading coefficient should be the opposite sign." %displayFactor(randomZeros[2])
    #####

else:
    equationOfGraph = aCoeff*(x-randomZeros[0]) * (x-randomZeros[1]) * (x-randomZeros[2])
    displayEquationOfGraph = displayEquation(aCoeff, randomZeros[0],  randomPower(1), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    #
    xPlot = numpy.arange(xMinimum, xMaximum, 0.05)
    solutionGraph = aCoeff*(xPlot-randomZeros[0]) * (xPlot-randomZeros[1]) * (xPlot-randomZeros[2])
    plt.rcParams.update({'font.size': 36})
    showPlot = plt.plot(xPlot, solutionGraph, linewidth = 5, color = 	'#02325f')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.savefig('../Figures/polyGraphToFunction' + str(version) + '.png', bbox_inches='tight')
    plt.close()
    # Distractors #
    negativeEquation = -aCoeff*(x-randomZeros[0]) * (x-randomZeros[1]) * (x-randomZeros[2])
    displayNegativeEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(1), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    #
    oneZeroOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayOneZeroOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    d4comment = "The factor $%s$ should have been an odd power." %randomZeros[0]
    #
    twoZerosOffEquation = aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1])**2 * (x-randomZeros[2])
    displayTwoZerosOffEquation = displayEquation(aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(2), randomZeros[2], randomPower(1))
    d1comment = "The factors $%s$ and $%s$ have have been odd power." %(randomZeros[0], randomZeros[1])
    #
    negativeOneZeroOffEquation = -aCoeff*(x-randomZeros[0])**2 * (x-randomZeros[1]) * (x-randomZeros[2])
    displayNegativeOneZeroOffEquation = displayEquation(-aCoeff, randomZeros[0],  randomPower(2), randomZeros[1], randomPower(1), randomZeros[2], randomPower(1))
    d2comment = "The factor $%s$ should have an odd power and the leading coefficient should be the opposite sign." %displayFactor(randomZeros[0])
    #####

displayStem = 'Which of the following equations \\textit{could} be of the graph presented below?'
displayProblem = "polyGraphToFunction%s" %version
displaySolution = displayEquationOfGraph
generalComment = "General Comments: Draw the x-axis to determine which zeros are touching (and so have even multiplicity) or cross (and have odd multiplicity)."

answerList = [equationOfGraph]

dc0 = displayNegativeEquation
dc1 = displayTwoZerosOffEquation
dc2 = displayNegativeOneZeroOffEquation
dc3 = displayEquationOfGraph
dc4 = displayOneZeroOffEquation

correctComment = "* This is the correct option."
d0comment = "This corresponds to the leading coefficient being the opposite value than it should be."

choicesAndDisplayChoices = [[dc0, d0comment, 0], [dc1, d1comment, 0], [dc2, d2comment, 0], [dc3, correctComment, 1], [dc4, d4comment, 0]]
random.shuffle(choicesAndDisplayChoices)
choices = [choicesAndDisplayChoices[0][0], choicesAndDisplayChoices[1][0], choicesAndDisplayChoices[2][0], choicesAndDisplayChoices[3][0], choicesAndDisplayChoices[4][0]]
choiceComments = [choicesAndDisplayChoices[0][1], choicesAndDisplayChoices[1][1], choicesAndDisplayChoices[2][1], choicesAndDisplayChoices[3][1], choicesAndDisplayChoices[4][1]]
answerIndex = 0
letters = ["A", "B", "C", "D", "E"]
for checkLetter in letters:
    if choicesAndDisplayChoices[answerIndex][2] == 1:
        answerLetter = letters[answerIndex]
        break
    answerIndex = answerIndex+1

writeToKey(keyFileName, version, problemNumber, displayStem, "Graph", displayProblem, "MathMode", displaySolution, answerLetter, choices, choiceComments, generalComment)
