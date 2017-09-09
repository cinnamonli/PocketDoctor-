import urllib.request as get
'''
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

    def printer(self):
        print(1)

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

name = 'headache'
treatments = [Medication('name', ['a', 'b'], ['c', 'd'], ['e', 'f']), Medication('name', ['a', 'b'], ['c', 'd'], ['e', 'f'])]

x = Condition(name, treatments)
x.printer()
'''

'''
URL = 'http://www.rxlist.com/drugs/alpha_a.htm'
page = get.urlopen(URL)
xs = str(page.read())
page.close()

print(xs.find('A-Methapred (Methylprednisolone Sodium Succinate)'))

URL2 = 'http://www.rxlist.com/drugs/alpha_b.htm'
page2 = get.urlopen(URL2)
xs2 = str(page2.read())
page2.close()

print(xs.find('B12 (Liver-Stomach Concentrate With Intrinsic Factor)'))
'''


conditionList = ["alzheimer's", 'diabetes', 'hypertension',
                 'leukemia',
                 'arthritis', 'depression',
                 'high cholesterol', 'osteoporosis',
                 'bronchitis', 'hyperthyroidism',
                 "Parkinson's", 'pneumonia',
                 'epilepsy', 'headaches',
                 'multiple sclerosis', 'endometriosis',
                 'sickle-cell anemia',
                 'lymphoma', 'schizophrenia',
                 'bipolar disorder', 'anxiety disorder',
                 'appendicitis']

for condition in conditionList:
    page = open('C://Users//kimbe//Desktop//Conditions//' + condition + '.txt', 'r')
    xs = str(page.readlines())
    page.close()

    print(xs)
    for element in xs:
        print(element)

'''
    newDoc = open('C://Users//kimbe//Desktop//Conditions//' + condition + '.txt', 'w')
    fullDoc = ''
    for line in xs:
        print(line)
        if (line.find("Rx\t") != -1 or line.find("Rx/") != -1):
            print(line.find("Rx\t"))
            print(line.find("Rx/"))
            newLine = line.split('Rx')[0]
            newLine = newLine[:len(newLine)-1] + '\n'
            print(newLine)
            fullDoc += newLine
    newDoc.write(fullDoc)
    newDoc.close()
''' 
