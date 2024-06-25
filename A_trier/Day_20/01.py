from collections import defaultdict
from collections import deque
import math

InputList = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

PulseSendDict = defaultdict()
FlipDict = defaultdict()
ConjunctionDict = defaultdict()
CyclesDict = {}

for i in InputList:
    Name, Dests = i.split(" -> ")
    #Addition for Part 2
    if Dests == "rx":
        Part2WatchName = Name[1:]
    DestsTuple = tuple(Dests.split(", "))
    if Name.startswith("%"):
        Name = Name[1:]
        FlipDict[Name] = "Off"
        PulseSendDict[Name] = DestsTuple
    elif Name.startswith("&"):
        Name = Name[1:]
        ConjunctionDict[Name] = {}
        PulseSendDict[Name] = DestsTuple
    else:
        Name = "Broad"
        PulseSendDict[Name] = DestsTuple

for i in InputList:
    Name, Dests = i.split(" -> ")
    DestsTuple = tuple(Dests.split(", "))
    if Name.startswith("b"):
        Name = "Broad"
    else:
        Name = Name[1:]
    for d in DestsTuple:
        if d in ConjunctionDict:
            ConjunctionDict[d][Name] = "L"

LowCount = 0
HighCount = 0

Part2Cycle = True
Cycles = 0
while Part2Cycle:
    Cycles += 1
    PulseQueue = deque()
    PulseQueue.append(("Button", "Broad", "L"))
    if Cycles == 10000:
        break
    while PulseQueue:
        From, To, Pulse = PulseQueue.popleft()
        if Cycles <= 1000:
            if Pulse == "L":
                LowCount += 1
            else:
                HighCount += 1
        if To == "rx" and Pulse == "L":
            Part2Answer = Cycles
            Part2Cycle = False
            break
        if To == "Broad":
            for d in PulseSendDict[To]:
                NewTuple = (To, d, Pulse)
                PulseQueue.append(NewTuple)
        elif To in FlipDict:
            if Pulse == "L" and FlipDict[To] == "Off":
                FlipDict[To] = "On"
                NewPulse = "H"
            elif Pulse == "L" and FlipDict[To] == "On":
                FlipDict[To] = "Off"
                NewPulse = "L"
            else:
                continue
            for d in PulseSendDict[To]:
                NewTuple = (To, d, NewPulse)
                PulseQueue.append(NewTuple)
        elif To in ConjunctionDict:
            ConjunctionDict[To][From] = Pulse
            if "L" in ConjunctionDict[To].values():
                NewPulse = "H"
            else:
                NewPulse = "L"
            for d in PulseSendDict[To]:
                NewTuple = (To, d, NewPulse)
                PulseQueue.append(NewTuple)
        if To == Part2WatchName and Pulse == "H":
            if From in CyclesDict:
                OldValue, OldDistance = CyclesDict[From]
                Distance = Cycles - OldValue
                print(From, OldValue, Distance)
                CyclesDict[From] = (Cycles, Distance)
            else:
                CyclesDict[From] = (Cycles, Cycles)
                print(From, 0, Cycles)


Part1Answer = LowCount*HighCount
Part2Answer = 1
for t in CyclesDict.values():
    _, t = t
    Part2Answer = math.lcm(Part2Answer, t)

print(LowCount, HighCount)
print(f"{Part1Answer = }")
print(f"{Part2Answer = }")