import json
import os

import Calc

listData = 'ControllerData'
nameList = ["VirtualButtons","Dice","GrabAndPlace","LightSwitch","Hanoi","ThrowObject"]
virtualButtonsTime = []
diceTime = []
grabAndPlace = []
lightSwitchTime = []
hanoiTime = []
throwObjectTime = []

minControllerTime = []
maxControllerTime = []
avgControllerTime = []

minHandTrackingTime = []
maxHandTrackingTime = []
avgHandTrackingTime = []

a = 0

while a < 2:
    if(a == 1):
        listData = 'HandTrackingData'

    virtualButtonsTime.clear()
    diceTime.clear()
    grabAndPlace.clear()
    lightSwitchTime.clear()
    hanoiTime.clear()
    throwObjectTime.clear()

    for path in os.listdir(listData):
        f = open(listData + '/' + path)
        data = json.load(f)
        for i in data['list']:
            if(i['_interactionName'] == 'VirtualButtons'):
                virtualButtonsTime.append(i['_seconds'])
            if (i['_interactionName'] == 'Dice'):
                diceTime.append(i['_seconds'])
            if (i['_interactionName'] == 'GrabAndPlace'):
                grabAndPlace.append(i['_seconds'])
            if (i['_interactionName'] == 'LightSwitch'):
                lightSwitchTime.append(i['_seconds'])
            if (i['_interactionName'] == 'Hanoi'):
                hanoiTime.append(i['_seconds'])
            if (i['_interactionName'] == 'ThrowObject'):
                throwObjectTime.append(i['_seconds'])

    virtualButtonsTime.sort()
    diceTime.sort()
    grabAndPlace.sort()
    lightSwitchTime.sort()
    hanoiTime.sort()
    throwObjectTime.sort()

    if(a == 0):
        minControllerTime.extend([virtualButtonsTime[0],diceTime[0],grabAndPlace[0],lightSwitchTime[0],hanoiTime[0],throwObjectTime[0]])
        maxControllerTime.extend([virtualButtonsTime[len(virtualButtonsTime)-1],diceTime[len(diceTime)-1],grabAndPlace[len(grabAndPlace)-1],lightSwitchTime[len(lightSwitchTime)-1],hanoiTime[len(hanoiTime)-1],throwObjectTime[len(throwObjectTime)-1]])
        avgControllerTime.extend([sum(virtualButtonsTime) / len(virtualButtonsTime),sum(diceTime) / len(diceTime),sum(grabAndPlace) / len(grabAndPlace),sum(lightSwitchTime) / len(lightSwitchTime),sum(hanoiTime) / len(hanoiTime),sum(throwObjectTime) / len(throwObjectTime)])
    else:
        minHandTrackingTime.extend([virtualButtonsTime[0],diceTime[0],grabAndPlace[0],lightSwitchTime[0],hanoiTime[0],throwObjectTime[0]])
        maxHandTrackingTime.extend([virtualButtonsTime[len(virtualButtonsTime)-1],diceTime[len(diceTime)-1],grabAndPlace[len(grabAndPlace)-1],lightSwitchTime[len(lightSwitchTime)-1],hanoiTime[len(hanoiTime)-1],throwObjectTime[len(throwObjectTime)-1]])
        avgHandTrackingTime.extend([sum(virtualButtonsTime) / len(virtualButtonsTime),sum(diceTime) / len(diceTime),sum(grabAndPlace) / len(grabAndPlace),sum(lightSwitchTime) / len(lightSwitchTime),sum(hanoiTime) / len(hanoiTime),sum(throwObjectTime) / len(throwObjectTime)])

    # Standardabweichung
    print('\n')
    print("Standardabweichung: ", listData)
    print("VirtualButtons: ", Calc.stdAbweichung(virtualButtonsTime))
    print("Dice: ", Calc.stdAbweichung(diceTime))
    print("GrabAndPlace: ", Calc.stdAbweichung(grabAndPlace))
    print("LightSwitch: ", Calc.stdAbweichung(lightSwitchTime))
    print("Hanoi: ", Calc.stdAbweichung(hanoiTime))
    print("ThrowObject: ", Calc.stdAbweichung(throwObjectTime))

    f.close()
    a += 1

b = 0
print('\n')
print('Type ', "Controller")
while b < (len(nameList)):
    print('Minimum: ',nameList[b], minControllerTime[b])
    print('Maximum: ',nameList[b], maxControllerTime[b])
    print('Average: ',nameList[b], avgControllerTime[b])
    b += 1

b = 0
print('\n')
print('Type ', "HandTracking")
while b < (len(nameList)):
    print('Minimum: ', nameList[b], minHandTrackingTime[b])
    print('Maximum: ', nameList[b], maxHandTrackingTime[b])
    print('Average: ', nameList[b], avgHandTrackingTime[b])
    b += 1

# AvgDifferenz
b = 0
print('\n')
print('Type ', "AvgDifferenz")
while b < (len(nameList)):
    print('Differenz: ', nameList[b], abs(avgHandTrackingTime[b] - avgControllerTime[b]))
    b += 1