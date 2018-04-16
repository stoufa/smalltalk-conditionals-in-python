from Condition import *

def ifTrueLogic():
    print("true")

def ifFalseLogic():
    print("false")

trueCondition = Condition(1 == 1)
#trueCondition.ifTrue(lambda : print("true")).ifFalse(lambda : print("false"))
trueCondition.ifTrue(ifTrueLogic).ifFalse(ifFalseLogic)

falseCondition = Condition(1 == 2)
#falseCondition.ifTrue(lambda : print("true")).ifFalse(lambda : print("false"))
falseCondition.ifTrue(ifTrueLogic).ifFalse(ifFalseLogic)
