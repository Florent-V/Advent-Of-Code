from collections import deque

InputList = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

OpenSet = set()
Part2OpenSet = set()

SlopeCharDict = {">": 3, "<": 2, "^": 0, "v": 1}
#Up, Down, Left, Right
SlopeSetsList = [set(),set(),set(),set()]
for y, f in enumerate(InputList):
    for x, c in enumerate(f):
        if c == ".":
            OpenSet.add((x,y))
            Part2OpenSet.add((x,y))
            if y == 0:
                StartPoint = (x,y)
            elif y == len(InputList) - 1:
                EndPoint = (x,y)
        elif c in SlopeCharDict:
            Index = SlopeCharDict[c]
            SlopeSetsList[Index].add((x,y))
            Part2OpenSet.add((x,y))
Directions = [(0,-1),(0,1),(-1,0),(1,0)]

def Path(StartPoint, PrevVisitTuple, EndPoint, InDistance, Part):
    if PrevVisitTuple != None:
        ImperialCore = set(PrevVisitTuple)
    else:
        ImperialCore = set()
    ImperialFrontier = deque()
    NewTuple = (StartPoint, InDistance)
    ImperialFrontier.append(NewTuple)

    while ImperialFrontier:
        (X,Y),Distance = ImperialFrontier.popleft()
        if (X,Y) == EndPoint:
            return Distance
        ImperialCore.add((X,Y))

        ValidDirections = []
        for n, d in enumerate(Directions):
            DX, DY = d
            NX, NY = X+DX,Y+DY
            NewLocation = (NX,NY)
            if Part == 1:
                if (NewLocation not in OpenSet and NewLocation not in SlopeSetsList[n]) or NewLocation in ImperialCore:
                    continue
            elif Part == 2:
                if NewLocation not in Part2OpenSet or NewLocation in ImperialCore:
                    continue
            ValidDirections.append(n)
        
        if len(ValidDirections) == 0:
            return 0
        elif len(ValidDirections) == 1:
            Index = ValidDirections.pop()
            DX, DY = Directions[Index]
            NX, NY = X+DX,Y+DY
            NewLocation = (NX,NY)
            NewDistance = Distance+1
            ImperialFrontier.append((NewLocation,NewDistance))
        else:
            BranchList = []
            NewDistance = Distance+1
            ImperialCoreTuple = tuple(ImperialCore)
            for n in ValidDirections:
                DX, DY = Directions[n]
                NX, NY = X+DX,Y+DY
                NewLocation = (NX,NY)
                NewValue = Path(NewLocation, ImperialCoreTuple, EndPoint, NewDistance, Part)
                BranchList.append(NewValue)
            return max(BranchList)
                
Part1Answer = Path(StartPoint, None, EndPoint, 0, 1)   




JunctionList = []
for (X, Y) in Part2OpenSet:
    Count = 0
    for DX, DY in Directions:
        NX,NY = X+DX,Y+DY
        if (NX,NY) in Part2OpenSet:
            Count += 1
    if Count >= 3:
        JunctionList.append((X,Y))
JunctionList.sort()
JunctionSet = set(JunctionList)
JunctionDistancesDict = {}
JunctionNeighborsDict = {}
for t in range(len(JunctionList)):
    JunctionNeighborsDict[t] = set()

StartJunction = []
EndJunction = []

def BFS(JuctionStart, ProgramStart, ProgramEnd):
    ImperialCore = set()
    ImperialFrontier = deque()
    ImperialFrontier.append((JuctionStart,0))
    JunctionIndex = JunctionList.index(JuctionStart)

    while ImperialFrontier:
        (X,Y),Distance = ImperialFrontier.popleft()
        if (X,Y) == ProgramStart:
            StartJunction.append(JunctionIndex)
            StartJunction.append(Distance)
            continue
        elif (X,Y) == ProgramEnd:
            EndJunction.append(JunctionIndex)
            EndJunction.append(Distance)
            continue
        ImperialCore.add((X,Y))

        for n, d in enumerate(Directions):
            DX, DY = d
            NX, NY = X+DX,Y+DY
            NewLocation = (NX,NY)
            NewDistance = Distance+1
            if NewLocation in ImperialCore or NewLocation not in Part2OpenSet:
                continue
            if NewLocation in JunctionSet:
                NewJunctIndex = JunctionList.index(NewLocation)
                JunctionNeighborsDict[JunctionIndex].add(NewJunctIndex)
                JunctionDistancesDict[(JunctionIndex,NewJunctIndex)] = NewDistance
                continue
            ImperialFrontier.append((NewLocation,NewDistance))

for t in JunctionList:
    BFS(t, StartPoint, EndPoint)

JunctionQueue = deque()
StartJunc, StartDist = StartJunction
EndJunct, EndDist = EndJunction
StartJunc = tuple([StartJunc])
print(StartJunc)
JunctionQueue.append((StartJunc, StartDist))
CurrentAnswer = 0
while JunctionQueue:
    HistoryTuple, CurrentDist = JunctionQueue.pop()
    CurrentJunct = HistoryTuple[-1]
    HistoryList = list(HistoryTuple)
    for g in JunctionNeighborsDict[CurrentJunct]:
        if g in HistoryTuple:
            continue
        NewDistance = CurrentDist + JunctionDistancesDict[(CurrentJunct,g)]
        if g == EndJunct:
            CurrentAnswer = max(CurrentAnswer, NewDistance)
            continue
        HistoryList.append(g)
        NewHistoryTuple = tuple(HistoryList)
        HistoryList.pop()
        JunctionQueue.append((NewHistoryTuple,NewDistance))

Part2Answer = CurrentAnswer + EndDist

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")