# dictionary d contains all of the conditions 
# contains all of the information on the conditions 

####################DATA_STRUCTURE#####################
# import urllib.request as get

d = {} # conditions dictionary

class Medication():

    def __init__(self, name, contraMeds, sideEffects):
        self.name = name
        # a list of med names that cause adverse drug reactions 
        self.contraMeds = contraMeds
        # a list of side effects 
        self.sideEffects = sideEffects

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, Medication)and(self.name == other.name))

class Condition():

    def __init__(self, name, treatments):
        self.name = name
        # a list of medications classes 
        self.treatments = treatments

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (isinstance(other, Condition)and(self.name == other.name))

    def printer(self):
        print(2)

def loadConditions():
    L = []
    abilify = Medication('abilify', ['fentora', 'morphine'], ['difficulty with speaking', 'uncontrolled movements'])
    cymbalta = Medication('cymbalta', ['zoloft', 'sustol', 'lithium', 'tamofen', 'prozac', 'fentora', 'ranexa'], ['cold sweats', 'weakness', 'blindness'])
    fentora = Medication('fentora', ['prozac', 'sustol', 'zoloft', 'morphine', 'abilify', 'cymbalta', 'haldol'], ['convulsions', 'light-headedness', 'nervousness'])
    sustol = Medication('sustol', ['lithium', 'zoloft', 'cymbalta', 'fentora', 'prozac', 'haldol'], ['blurred vision', 'fever', 'pounding in the ears'])
    zoloft = Medication('zoloft', ['lithium', 'cymbalta', 'fentora', 'sustol', 'tamofen', 'haldol'], ['diarrhea', 'sweating', 'inability to sit still'])
    ibuprofen = Medication('ibuprofen', ['lithium'], ['heartburn', 'shortness of breath'])
    tamofen = Medication('tamofen', ['ibuprofen', 'prozac', 'zoloft', 'ranexa', 'haldol'], ['anxiety', 'confusion', 'dizziness'])
    prozac= Medication('prozac', ['abilify', 'ibuprofen', 'lithium', 'tamofen', 'sustol'], ['suicidal thoughts and behaviors', 'seizures', 'abnormal bleeding'])
    lithium = Medication('lithium', ['ibuprofen', 'zoloft', 'sustol', 'prozac', 'cymbalta', 'haldol'], ['fainting', 'irregular heartbeat', 'troubled breathing'])
    morphine = Medication('morphine', ['abilify', 'fentora', 'haldol'], ['stomache pain', 'headache'])
    ranexa = Medication('ranexa', ['tamofen', 'cymbalta', 'haldol'], ['dizziness', 'constipation', 'nausea', 'sensation of spinning'])
    haldol = Medication('haldol', ['sustol', 'ranexa', 'zoloft', 'morphine', 'fentora', 'lithium', 'tamofen'], ['insomnia', 'agitation', 'difficulty speaking', 'troubled swallowing'])
    L.append([abilify,cymbalta,fentora])
    L.append([sustol,zoloft,ibuprofen])
    L.append([prozac,lithium,morphine])
    return L 
def loadDictionary(d):
    conditionsL = loadConditions()
    for condition in conditionsL:
        d[condition.name] = condition


# name1 = 'headache'
# med1 = Medication('med1', ['med3', 'b'], "causes insomnia", "don't drink alchohol")
# med2 = Medication('med2', ['med4', 'b'], "causes insomnia", "don't drink alchohol")
# treatments1 = [med1, med2]

# name2 = 'toothache'
# med3 = Medication('med3', ['med2', 'b'], "causes insomnia", "don't drink alchohol")
# med4 = Medication('med4', ['med1', 'b'], "causes insomnia", "don't drink alchohol")
# treatments2 = [med3, med4]


# headache = Condition(name1, treatments1)
# toothache = Condition(name2, treatments2)
# d[name1] = headache
# d[name2] = toothache 
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
    contraMeds1 = m1.contraMeds
    contraMeds2 = m2.contraMeds
    for med in contraMeds1:
        if med == m2.name:
            return False
    for med in contraMeds2:
        if med == m1.name:
            return False
    return True
# turns a list of meds into a list of strings
def display(resL):
    for med in resL:
        print(med.name + ":\n")
        print("contrameds")
        for name in med.contraMeds:
            print(name)
		    # print(med.sideEffects + "\n")
		# print(med.cautions + "\n")
        print("\n")
   

# @requires takes in a 2d list containing the lists of medications required  
# @ensures returns a list containing all the possible solutions to the conditions 
def getValidPrescriptions(medicationsList): 
    def isLegal(curMed, curSolution):
        # a position is legal if the med doesn't contradict with the previous
        for med in curSolution:
        	if not(isSafe(med,curMed)):
        		return False
        return True
    def solve(medicationsList,resL):
        # print(resL)
        # display(resL)

        if (medicationsList == []):
            return resL
        else:
            # try to place the med in solutions,
            # and then recursively solve the rest of the conditions
            # for i in range(len(medicationsList)):
            medsForCondition = medicationsList.pop(0)
            for j in range(len(medsForCondition)):
                curMed = medsForCondition[j]
                if isLegal(curMed,resL):
                    resL.append(curMed)  # place the med and hope it works
                    solution = solve(medicationsList,resL)
                    if (solution != None):
	                    # ta da! it did work
                        return solution
                    resL.pop()
            medicationsList.insert(0,medsForCondition)
            # shoot, can't place the queen anywhere
            return None
    return solve(medicationsList,[])
# meds = getMedications(name1, name2)
meds = loadConditions()
# display(meds[0])
# display(meds[1])
result = getValidPrescriptions(meds)
display(result)
