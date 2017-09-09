# dictionary d contains all of the conditions 
# contains all of the information on the conditions 

# @requires args is however many conditions: string 
# @ensures returns a 2d list containing the lists of medications required
def getMedications(*args):
	n = len(args)
	medicationsList = []
	for i in range(0,n):
		# condition is a string
		condition = args[i]
		medications = d[condition]
		medicationsList[i] = medications
	return medicationsList 

def isSafe(m1, m2):
	contraMeds1 = m1.contraMeds; 
	contraMeds2 = m2.contraMeds; 
	for med in contraMeds1:
		if med == m2:
			return False
	for med in contraMeds2:
		if med == m1:
			return False 
	return True

# @requires takes in a 2d list containing the lists of medications required  
# @ensures returns a list containing all the possible solutions to the conditions 
def getValidPrescriptions(medicationsList):
    prescription = []; 
    def isLegal(curMed, curSolution):
        # a position is legal if the med doesn't contradict with the previous
        for med in curSolution:
        	if not(isSafe(curMed,med)):
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
    