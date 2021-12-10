import os
from datetime import datetime

def getthing():
    thing = []
    with open("./4/example.txt", "r") as f:
        for line in f.readlines():
            thing.append((line.strip()))
    return thing


def getNumbers(thing):
    return thing[0].split(",")
    
def getCards(thing):
    cards=[]
    for x in range(2,len(thing),6):
        if len(thing[x]) > 1:
            card=[]
            for i in range(5):
                row = thing[x+i].split()
                card.append(row)
            cards.append(card)
    return cards



def checkRows(card,row):
    for i in card[row]:
        if i[-1] != "x":
            return False
    return True
def checkCols(card,col):
    for row in card:
        if row[col][-1] != "x":
            return False
    return True

def checkBingo(card,row,col):
    if checkRows(card,row):
        print("Bingo, Row:{}".format(card[row]))
        return True
    elif checkCols(card,col):
        print("Bingo, Col:")
        return True
    else:
        return False

def getResult(card,num):
    result =0
    for row in card:
        for col in row:
            if col[-1]!="x":
                result += int(col)
    return result * int(num)


def Scorecard(card,nums):
    for i in range(0,len(nums)):

        for row in range(0,len(card)):
            for col in range(0,len(card[0])):
                if card[row][col] == nums[i]:
                    card[row][col] += "x"
                    if checkBingo(card,row,col):
                        return getResult(card,nums[i]), i





def PartOne():
    cards = getCards(getthing())
    result = 0
    time = 999999

    for card in cards:
        
        r,t = Scorecard(card,getNumbers(getthing()))
        if t < time:
            time = t
            result = r
    print("PartOne")
    print("Card {} is the winner with result {} and the winning num {}".format(card,result,getNumbers(getthing())[time]))


def PartTwo():
    cards = getCards(getthing())
    result = 0
    time = 0

    for card in cards:
        
        r,t = Scorecard(card,getNumbers(getthing()))
        if t > time:
            time = t
            result = r
    print("PartTwo")
    print("Card {} is the loser with result {} and the winning num {}".format(card,result,getNumbers(getthing())[time]))
            

PartOne()
PartTwo()

            

