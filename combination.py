# dictionary d contains all of the conditions 
# contains all of the information on the conditions 

####################DATA_STRUCTURE#####################
# import urllib.request as get

d = {} # conditions dictionary

class Medication():

    def __init__(self, name, contraMeds, sideEffects, cautions):
        self.name = name
        self.contraMeds = contraMeds
        self.sideEffects = sideEffects
        self.cautions = cautions

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, A) and (self.name == other.name))

class Condition():

    def __init__(self, name, treatments):
        self.name = name
        self.treatments = treatments

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, A) and (self.name == other.name))

    def printer(self):
        print(2)

name1 = 'headache'
med1 = Medication('med1', ['med3', 'b'], "causes insomnia", "don't drink alchohol")
med2 = Medication('med2', ['med4', 'b'], "causes insomnia", "don't drink alchohol")
treatments1 = [med1, med2]

name2 = 'toothache'
med3 = Medication('med3', ['med2', 'b'], "causes insomnia", "don't drink alchohol")
med4 = Medication('med4', ['med1', 'b'], "causes insomnia", "don't drink alchohol")
treatments2 = [med3, med4]


headache = Condition(name1, treatments1)
toothache = Condition(name2, treatments2)
d[name1] = headache
d[name2] = toothache 
####################SOLVE##############################
# @requires args is however many conditions: string 
# @ensures returns a 2d list containing the lists of medications required
def getMedications(*args):
	n = len(args)
	medicationsList = []
	for c in args:
		# condition is a string
		condition = d[c]
		medications = condition.treatments
		medicationsList.append(medications)
	return medicationsList 

def isSafe(m1, m2):
	contraMeds1 = m1.contraMeds; 
	for med in contraMeds1:
		if med == m2:
			return False
	return True
# turns a list of meds into a list of strings
def display(resL):
	for med in resL:
		print(med.name + ":\n")
		print(med.sideEffects + "\n")
		print(med.cautions + "\n")
   

# @requires takes in a 2d list containing the lists of medications required  
# @ensures returns a list containing all the possible solutions to the conditions 
def getValidPrescriptions(medicationsList):
    prescription = []; 
    def isLegal(curMed, curSolution):
        # a position is legal if the med doesn't contradict with the previous
        for med in curSolution:
        	if not(isSafe(curMed,med.name)):
        		return False
        return True
    def solve(medicationsList,resL):
        if (medicationsList == []):
            return resL
        else:
            # try to place the med in solutions,
            # and then recursively solve the rest of the conditions
            for i in range(len(medicationsList)):
            	medsForCondition = medicationsList[i]
                for j in range(len(medsForCondition)):
                	curMed = medsForCondition[j]
	                if isLegal(curMed,resL):
	                    resL.append(curMed)  # place the med and hope it works
	                    backup = medicationsList.pop(0)
	                    solution = solve(medicationsList,resL)
	                    if (solution != None):
	                        # ta da! it did work
	                        return solution
	                    medicationsList.insert(0,backup);
	                    resL.pop();
            # shoot, can't place the queen anywhere
            return None
    return solve(medicationsList,[])
meds = getMedications(name1, name2)
# display(meds[0])
# display(meds[1])
result = getValidPrescriptions(meds)
display(result)
