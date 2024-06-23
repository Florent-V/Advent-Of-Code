import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re
from copy import deepcopy

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    # Trouver l'indice de l'élément vide
    separator = lines.index('')
    # Diviser la liste en deux parties
    work_flow = lines[:separator]
    print('work_flow', work_flow)
    parts = lines[separator + 1:]
    print('parts', parts)
    dico_work_flow = {}
    for flow in work_flow:
        temp = flow.strip('}').split('{')
        dico_work_flow[temp[0]] = temp[1].split(',')
    print('dico_work_flow', dico_work_flow)

    list_parts = []
    for part in parts:
        temp = part.strip('{}').split(',')
        dico_parts = {}
        for i in temp:
            temp = i.split('=')
            dico_parts[temp[0]] = int(temp[1])
        list_parts.append(dico_parts)
    print('list_parts', list_parts)



    
    return dico_work_flow, list_parts


def part_1(dico_work_flow, list_parts):
    liste= []
    for part in list_parts:
        result_part = handle_part(part, dico_work_flow)
        if result_part == 'A':
            liste.append(sum(part.values()))
    print('liste', liste)
    print('part 1', sum(liste))
        
    return

def handle_part(part, dico_work_flow):
    flow = 'in'
    print('part', part)
    operateurs = ['<', '>']
    flag = True
    while flag:
        steps = dico_work_flow[flow]
        print('steps', steps)
        for step in steps:
            print('step', step)
            result = evaluer_condition(part, step)
            print('result', result)
            if result == False:
                print('coucou1')
                continue
            if result == True:
                print('coucou2')
                flow = step.split(':')[1]
                if flow == 'A' or flow == 'R':
                    flag = False
                    return flow
                print('flow', flow)
                break
            if result == step and step != 'A' and step != 'R':
                print('coucou3')
                flow = step
                break
            if result == step and (step == 'A' or step == 'R'):
                print('coucou4')
                flag = False
                return step        
    return

# Exemple d'utilisation de match (à partir de Python 3.10)
def evaluer_condition(objet, step):
    operateurs = ['<', '>']
    operateur = None
    for op in operateurs:
      if op in step:
          operateur = op
          break
    if not operateur:
        return step
    
    if ':' not in step:
        print('#####################WARNING#####################')
        return step

    splitted_step = step.split(':')

    condition = splitted_step[0].split(operateur)
    cle = condition[0]
    value = int(condition[1])
    
    match operateur:
        case '<':
            return objet.get(cle, 0) < value
        case '>':
            return objet.get(cle, 0) > value
        # case '<=':
        #     return objet.get(cle, 0) <= value
        # case '>=':
        #     return objet.get(cle, 0) >= value
        # case '==':
        #     return objet.get(cle, 0) == value
        # case '!=':
        #     return objet.get(cle, 0) != value
        case _:
            raise ValueError("Opérateur de comparaison non pris en charge.")

def part_2():
    ps = open("input_light.txt").read().split("\n\n")

    rules = {}

    for l in ps[0].splitlines():
        p = l.split("{")
        rules[p[0]] = p[1][:-1]
    print('rules', rules)

    print(get_combs("in", rules))

def get_combs(state, rules, ranges={"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}):
    if state == "R":
        return 0
    elif state == "A":
        x_s = ranges["x"]
        m_s = ranges["m"]
        a_s = ranges["a"]
        s_s = ranges["s"]

        return (x_s[1] - x_s[0] + 1) * (m_s[1] - m_s[0] + 1) * (a_s[1] - a_s[0] + 1) * (s_s[1] - s_s[0] + 1)

    total = 0
    print('state', state)
    for pred in rules[state].split(","):
        print('pred', pred)
        if not ":" in pred:
            total += get_combs(pred, rules, ranges)
        else:
            p = pred.split(":")
            print('p', p)
            new_range = deepcopy(ranges)

            new_val = int(p[0][2:])
            c_range = ranges[p[0][0]]

            if c_range[0] < new_val < c_range[1]:
                if p[0][1] == "<":
                    new_range[p[0][0]] = (c_range[0], new_val - 1)
                    ranges[p[0][0]] = (new_val, c_range[1])
                else:
                    new_range[p[0][0]] = (new_val + 1, c_range[1])
                    ranges[p[0][0]] = (c_range[0], new_val)
                total += get_combs(p[1], rules, new_range)
    return total





def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    #dico_work_flow, list_parts = format_data(lines)
    #part_1(dico_work_flow, list_parts)
    part_2()



    print('script execution time', time.time() - now)
    

    



if __name__ == "__main__":
    main()
   