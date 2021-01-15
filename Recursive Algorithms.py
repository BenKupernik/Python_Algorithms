##Ben Kupernik
##7/16/2020
##
############################################################################################################################################################################################
##
##README
##
##This program has 5 total functions. The function in order of appearance count how many substrings in a string start with the same character,
##how many charters there are in a string, finds the maximum and minimum vales of an array, prints a pattern of * and $ based of a number, and
##mutuplys two positive integers together. They all use recursion to do this. After the function definitions is a short program that will ask the user for some
##information and run through each of the functions to demonstrate them. 
##
##
############################################################################################################################################################################################
##
##Test one
##
##Input
##
##Run through all the functions and check that the expected output is produced
##
##Output
##
##Program complies correctly and runs the user through all the function. The output from the function match the expected value.
##
##Test two
##
##Input
##
##Run through the program again but throw some curve balls and weird cases in for the input. For the first and second function enter an empty string. For the 3ed
##enter an empty array for the 4th enter 0 and for the 5th enter 0 and 0.
##
##Output
##
##The first two functions handle the empty sting fine but the maxMinArray function crashed so I add an
##if statement to handle that case. The pattern function did produce a pattern with 0 as the starting number and
##The multiply function went into an infinite loop. So, I adjusted the special case criteria to account for
##a starting number of 0. After these additional all functions performed smoothly.
##
##Test three
##
##Input
##
##Try some special characters for the first and second functions like $. Try a large array for the third function
##and value with a decimal for the fourth. For the last function try a large number.
##
##Output
##
##The first two functions handle special characters fine and the pattern function can handle an floating point number. It is possible to crash
##the arrayMaxMin function and multiplier function by using a large enough number. The error produced is a maximum recursion depth error.
##After some googleing it seems the limit is typical 1000 recursions before the program crashes and it is possible to increase this value.
##However, given the scope of these functions I don't really feel this is necessary as they can handle any reasonable request.
##
##
##############################################################################################################################################################################################

import random
import array as arr


##############################################################################################################################################################################################

##Function definitions

##This function counts how many substrings in a string start with the same character
def subStringCounter (aString, numSubstrings = 0):
    
    shorterString =""

     ##Specal case when the string has one or zero characters remaining
    if (len(aString) <= 1):
        return numSubstrings

    ##otherwise shorten the string by removing the first and last characters
    else:
        shorterString = aString[1 : len(aString) - 1]
        numSubstrings = subStringCounter(shorterString, numSubstrings)##Pass the shorter string back in to the function

       ##Check if the string has the same start and end functions 
    if(aString[0] == aString [-1]):
        numSubstrings = numSubstrings + 1
       
    return numSubstrings

#######################################################################################################

##This function takes a string and returns the length of the string
def stringLengthCounter (aString, length = 0):
    
    shorterString = ""

    ##Specal case when the string is empty
    if (aString == ""): 
        pass

    ##shorten the string by one then pass it back to the function
    else:
        shorterString = aString[0 :- 1]
        length = stringLengthCounter(shorterString, length)
        length += 1 ##for every time the function is called this will increase by 1
    
    return length

#######################################################################################################

## This function takes an array of positive integers and returns the min and max values in the array

def arrayMinMax (anArray):
    
    theMax = 0
    theMin = 0
    short = arr.array('i', [])
    
    if len(anArray) <=1:##specal case for when the array has one of fewer elements in it.

        if len(anArray) == 0:
           print("This array is empty!")
           return 0, 0
        else:
            theMax = anArray[0] ##in a list of one the one element is both the min and max
            theMin = anArray[0]
            return theMax, theMin

    ##Shortens the array by removing the last element and passes it back to the function
    else:
        short = anArray[0 : (len(anArray) - 1)]
        theMax, theMin = arrayMinMax(short)

   ##Checks the current min/max value against every value as they are added back to the array and
   ##updates the min/max values as needed
    if theMax < anArray[-1]:
        theMax = anArray[-1]

    if theMin > anArray[-1]:
        theMin = anArray[-1]

    return theMax, theMin

#######################################################################################################

##This function takes a user provided number and generates a random pattern based off the value of that number

def pattern (aNumber):
    
    newNumber = 0
    thePattern = ""
    evenString = "$"
    oddString = "*"

    ##Specal case where the number = 1
    if aNumber <= 1:
        thePattern = "*"
        return thePattern

    ##takes the user number and uses floor division to divide it by 1, 2 or 3 and then
    ##passes it back in to the function. Eventually this has to equal 1
    else:
        newNumber = aNumber // random.randint(1,3)
        thePattern = pattern(newNumber)

    ##Checks if the number after floor division is odd or even and assigns a * or $ to create a pattern
    if (newNumber % 2) == 0:
        thePattern = thePattern + evenString
    else:
        thePattern = thePattern + oddString

    return thePattern

#######################################################################################################

##This function takes two positive integers and multiplies them.

def multiplier(x, y):

    answer = 0
    newY = 0

    ##Specal case if y = 1 then assigns the value of x to answer
    if y <= 1:
        answer = x
        return answer

    ##If y is not 1 this subtracts one from y and then feeds it back into the function
    else:
        newY = y - 1
        answer = multiplier(x, newY)

    ##Mutuplacation is really just repeated addition so this just keeps adding x to the answer y - 1 times
    answer += x

    return answer

#######################################################################################################

##Test Program

##Varables

numSubstrings = 0
length = 0
randNum = 0
numInArray = 0
startNum = 0
answer = 0
aString = ""
listOfNumInArray =[]
anArray = arr.array('i', [])




##Tests the subStringCounter function, asks the user for a string and then passes it through the function and prints the results
aString = input("Please enter a string. For this function whitespace and special characters do count as characters")
numSubstrings = subStringCounter(aString)
print("There are",numSubstrings,"substrings that start with the same charter in that string!")

##Tests the stringLength function. Takes the string previously entered by the user and passes it through
##the function. Then prints the result
length = stringLengthCounter(aString)
print("That string had",length,"charcters in it!")


##asks for a positive integer
numInArray = int(input("How many numbers would you like in your array??"))

##uses that integer to randomly fill out an array with numbers between 1 and 100 (including both 1 and 100)
for i in range (numInArray):
    
    randNum = random.randint(1,100)
    anArray.append(randNum)
    listOfNumInArray.append(randNum)

print("Here's the numbers in your array!\n",listOfNumInArray)

##Runs the array through the arrayMinMax function and prints the result
theMax, theMin = arrayMinMax(anArray)
print("looks like the maximum is ",theMax,"and the minimum is",theMin,".")

##Asks the user for a number then passes that number to the pattern function and prints the pattern
startNum = float(input("Pick a number to print a pattern! (Hint pick a large number for a better pattern ex. 2000000000 \n"))
aString = pattern(startNum)
print(aString)


##Asks the user for two positive integers
x = int(input("What’s the first number you would like to multiply? (Positive integers only please)"))
y = int(input("And what’s the next?"))


##Runs the two numbers through the multiplier function and prints the result
answer = multiplier(x, y)
print(x,"times",y,"is",answer)


                
           

            
############################################################################################################################################################################################

    



##If you’re wondering what happened to the permutations function its here. Its here because despite
##my best efforts I can’t quite get this one to work. I suspect it has something to do with where I
##should put the return statement. It does give a partial list though so I though I’d include it anyway, just uncomment it and check it out.

####This function returns a list of all possible permutationsof a word
##def listCombanations(aList):
##
##    length = len(aList)
##    masterList = []
##    shortList = []
##
##    ##specal case if there is only one letter left in the list
##    if (len(aList) == 1): ##specal case for when there are two items
##        masterList.append(aList)
##        #i = input("")
##        return masterList
##
##    ##If there’s more than one letter left cycle through the list removing each item once and passing the resulting list back to the function 
##    else:
##        for i in range (len(aList)):
##            shortList = aList[ : i]  + aList[i + 1 :]            
##            masterList = listCombanations(shortList)
##
##            ##Add the removed letter back to the end of the word after all permutations of the shorter word have been found
##            if masterList != None: ##I keep getting a type none returned and I don't know why but this fixed it.
##                masterList. append(aList[i])
##                print(masterList)
##        return masterList

##aList =['a', 'n', 'd']
##answer = listCombanations(aList)
