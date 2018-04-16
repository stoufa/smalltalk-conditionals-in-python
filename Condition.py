class TrueClass():
    def ifTrue(self, function):
        function()
        return self

    def ifFalse(self, function):
        return self

class FalseClass():
    def ifTrue(self, function):
        return self

    def ifFalse(self, function):
        function()
        return self    

class Condition():
    conditionTypeDict = {False: FalseClass, True: TrueClass}
    
    def __init__(self, condition):
        self.condition = condition
        self.classType = Condition.conditionTypeDict[self.condition]()

    def ifTrue(self, function):
        self.classType.ifTrue(function)
        return self

    def ifFalse(self, function):
        self.classType.ifFalse(function)
        return self  
