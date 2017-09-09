# This program is used to read in user input, whether it be conditions or medications
    # However, the program as it is can only expect either conditions or medications, not both

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

d = {} # dictionary of classes

d['abilify'] = Medication('abilify', ['fentora', 'morphine'], ['difficulty with speaking', 'uncontrolled movements'])
d['cymbalta'] = Medication('cymbalta', ['zoloft', 'sustol', 'lithium', 'tamofen', 'prozac', 'fentora', 'ranexa'], ['cold sweats', 'weakness', 'blindness'])
d['fentora'] = Medication('fentora', ['prozac', 'sustol', 'zoloft', 'morphine', 'abilify', 'cymbalta', 'haldol'], ['convulsions', 'light-headedness', 'nervousness'])
d['sustol'] = Medication('sustol', ['lithium', 'zoloft', 'cymbalta', 'fentora', 'prozac', 'haldol'], ['blurred vision', 'fever', 'pounding in the ears'])
d['zoloft'] = Medication('zoloft', ['lithium', 'cymbalta', 'fentora', 'sustol', 'tamofen', 'haldol'], ['diarrhea', 'sweating', 'inability to sit still'])
d['ibuprofen'] = Medication('ibuprofen', ['lithium'], ['heartburn', 'shortness of breath'])
d['tamofen'] = Medication('tamofen', ['ibuprofen', 'prozac', 'zoloft', 'ranexa', 'haldol'], ['anxiety', 'confusion', 'dizziness'])
d['prozac'] = Medication('prozac', ['abilify', 'ibuprofen', 'lithium', 'tamofen', 'sustol'], ['suicidal thoughts and behaviors', 'seizures', 'abnormal bleeding'])
d['lithium'] = Medication('lithium', ['ibuprofen', 'zoloft', 'sustol', 'prozac', 'cymbalta', 'haldol'], ['fainting', 'irregular heartbeat', 'troubled breathing'])
d['morphine'] = Medication('morphine', ['abilify', 'fentora', 'haldol'], ['stomache pain', 'headache'])
d['ranexa'] = Medication('ranexa', ['tamofen', 'cymbalta', 'haldol'], ['dizziness', 'constipation', 'nausea', 'sensation of spinning'])
d['haldol'] = Medication('haldol', ['sustol', 'ranexa', 'zoloft', 'morphine', 'fentora', 'lithium', 'tamofen'], ['insomnia', 'agitation', 'difficulty speaking', 'troubled swallowing'])

# Suppose there was a search query and you were processing the command line
# Suppose the command line was taken in as a string that is comma separated
def processLine(commandLine):
    processedLine = commandLine
    tokens = []
  
    commaLocator = processedLine.find(',')
    while commaLocator != -1:
        newToken = processedLine[:commaLocator]     # things must be separated by commas
        tokens.append(newToken)
        processedLine = processedLine[commaLocator+1:]
  
        while processedLine[0] == ' ':
            processedLine = processedLine[1:]       # in the case that the user uses spaces after commas
        
        commaLocator = processedLine.find(',')
        
    if len(processedLine) > 0:
        newToken = processedLine[:commaLocator]
        tokens.append(newToken)
    
    return tokens

def tokens(tokens, infoDict, medOrCondition):
    ''' Retrieves good tokens '''
    goodTokens = []

    print('  List of Tokens:')
    for token in tokens:
        if token not in infoDict.keys():
            print(token + ': this ' + medOrCondition + ' does not exist')
        else:
            print(token + ': this ' + medOrCondition + ' exists')
            goodTokens.append(token)
    
    return goodTokens

def goodMedTokens(goodTokens):
    ''' Prints the value in parts '''
    for token in goodTokens:
        val = d[token]
        print(val.name, val.contraMeds, val.sideEffects)

def goodConditionTokens(goodTokens):
    ''' Prints the value in parts '''
    for token in goodTokens:
        val = d[token]
        print(val.name, val.treatments)

x = processLine('prozac, zoloft, iweviweuvb') # example
y = tokens(x, d, 'medicine')
goodMedTokens(y)
