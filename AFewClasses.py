# Classes

abilify = Medication('abilify', ['fentora', 'morphine'], ['difficulty with speaking', 'uncontrolled movements'])
cymbalta = Medication('cymbalta', ['zoloft', 'sustol', 'lithium', 'tamofen', 'prozac', 'fentora'], ['cold sweats', 'weakness', 'blindness'])
fentora = Medication('fentora', ['prozac', 'sustol', 'zoloft', 'morphine', 'abilify', 'cymbalta'], ['convulsions', 'light-headedness', 'nervousness'])
sustol = Medication('sustol', ['lithium', 'zoloft', 'cymbalta', 'fentora', 'prozac'], ['blurred vision', 'fever', 'pounding in the ears'])
zoloft = Medication('zoloft', ['lithium', 'cymbalta', 'fentora', 'sustol', 'tamofen'], ['diarrhea', 'sweating', 'inability to sit still'])
ibuprofen = Medication('ibuprofen', ['lithium'], ['heartburn', 'shortness of breath'])
tamofen = Medication('tamofen', ['ibuprofen', 'prozac', 'zoloft'], ['anxiety', 'confusion', 'dizziness'])
prozac = Medication('prozac', ['abilify', 'ibuprofen', 'lithium', 'tamofen', 'sustol'], ['suicidal thoughts and behaviors', 'seizures', 'abnormal bleeding'])
lithium = Medication('lithium', ['ibuprofen', 'zoloft', 'sustol', 'prozac', 'cymbalta'], ['fainting', 'irregular heartbeat', 'troubled breathing'])
morphine = Medication('morphine', ['abilify', 'fentora'], ['stomache pain', 'headache'])
