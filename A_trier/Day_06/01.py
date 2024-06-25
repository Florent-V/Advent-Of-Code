import sys
import math
from string import punctuation

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    data = {}
    for line in lines:
        info = line.split()
        data[info[0]] = info[1:]
    return data
    
def find_way_to_win(time, distance):
    number_of_way = 0
    for i in range(0, time+1):
        dist = (time - i) * i
        if dist > distance:
            number_of_way += 1
    return number_of_way

def part_1(data):
    ways = []
    for i in range(len(data['Time:'])):
        ways.append(find_way_to_win(int(data['Time:'][i]), int(data['Distance:'][i])))
    print(math.prod(ways))

def part_2(data):
    data['Time:'] = ''.join(data['Time:'])
    data['Distance:'] = ''.join(data['Distance:'])
    print(find_way_to_win(int(data['Time:']), int(data['Distance:'])))
    
    


def main():
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    data = format_data(lines)
    #part_1(data)
    part_2(data)
    

    


    



if __name__ == "__main__":
    main()
   