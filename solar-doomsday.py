import math

def solution(area):
    panelArray = []
    findPanels(panelArray, area)
    return panelArray

def findPanels(panels, area):
    if area >= 1:
        nextPanel = getPanelArea(area)
        panels.append(nextPanel)
        newArea = area - nextPanel
        findPanels(panels, newArea)


def getPanelArea(area):
    rootOfArea = math.sqrt(area)
    intRoot = int(rootOfArea)
    return intRoot * intRoot