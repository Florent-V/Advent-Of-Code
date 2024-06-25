import sys
from itertools import combinations, permutations, combinations_with_replacement
import time
import re
import copy

def read_file(file):
    with open(file, "r") as f:
        return f.read().split("\n")

def format_data(lines):
    flip_flops = {}
    conjunctions = {}
    dico_line = {}
    for line in lines:
        if line.startswith('broadcaster'):
            dico_line['broadcaster'] = [i.strip() for i in line.split('->')[1].strip().split(',')]
        else:
            if line.startswith('%'):
                flip_flops[line.split('->')[0].strip()[1:]] = {'state':0, 'pulse':0}
            elif line.startswith('&'):
                conjunctions[line.split('->')[0].strip()[1:]] = {}
            dico_line[line.split('->')[0].strip()[1:]] = [i.strip() for i in line.split('->')[1].strip().split(',')]
    for line in lines:
        for j in [i.strip() for i in line.split('->')[1].strip().split(',')] :
            if j in conjunctions.keys() and line.split('->')[0].strip()[1:] not in conjunctions.keys():
                conjunctions[j][line.split('->')[0].strip()[1:]] = {'state':0, 'pulse':0}
    print('conjunction', conjunctions)
    print('flip_flop', flip_flops)
    print('dico_line', dico_line)
    print('count flip_flop', len(flip_flops))
    print('count conjunction', len(conjunctions))
    print('count dico_line', len(dico_line))
    return flip_flops, conjunctions, dico_line

def handle_flip_flop(flip_flop, pulse):
    if pulse == 1:
        return flip_flop
    flip_flop['pulse'] = 1 - flip_flop['pulse']
    flip_flop['state'] = 1 - flip_flop['state']
    return flip_flop

def handle_conjunction(conjunction):
    print('handle_conjunction', conjunction)
    if all(conjunction[i]['state'] == 1 for i in conjunction):
        return 0
    return 1

def init_queue(queue, flip_flops):
    for i in queue:
        flip_flops[i] = handle_flip_flop(flip_flops[i], 0)
    return flip_flops

def press_button(dico_line, flip_flops, conjunctions):
    queue = dico_line['broadcaster'][:]
    nb_low_pulse = 1
    nb_high_pulse = 0
    nb_low_pulse += len(queue)
    print('nb_low_pulse', nb_low_pulse)
    flip_flops = init_queue(queue, flip_flops)
    print('start')
    print('flip_flop', flip_flops)
    print('queue', queue)
    while len(queue) > 0:
        emitter = queue.pop(0)
        if emitter in flip_flops.keys():
            receivers = dico_line[emitter]
            print('emitter flip_flop', emitter, "pulse", flip_flops[emitter]['pulse'], 'to', receivers)
            if flip_flops[emitter]['pulse'] == 0:
                nb_low_pulse += len(receivers)
            else:
                nb_high_pulse += len(receivers)
            for i in receivers:
                if i in flip_flops.keys():
                    flip_flops[i] = handle_flip_flop(flip_flops[i], flip_flops[emitter]['pulse'])
                    queue.append(i) if i not in queue and flip_flops[emitter]['pulse'] != 1 else None
                    continue
                else:
                    conjunctions[i][emitter]['state'] = flip_flops[emitter]['state']
                    conjunctions[i][emitter]['pulse'] = flip_flops[emitter]['pulse']
                    
                queue.append(i) if i not in queue else None
        elif emitter in conjunctions.keys():
            print('conjunctions emitter', emitter)
            pulse = handle_conjunction(conjunctions[emitter])
            receivers = dico_line[emitter]
            if pulse == 0:
                nb_low_pulse += len(receivers)
            else:
                nb_high_pulse += len(receivers)
            print('conjunctions emitter', emitter,"pulse", pulse, 'to', receivers)
            for i in receivers:
                if i in flip_flops.keys():
                    flip_flops[i] = handle_flip_flop(flip_flops[i], pulse)
                    #print('flip_flop', i, flip_flops[i])
                    if i not in queue and pulse != 1:
                        queue.append(i)
                    continue
                queue.append(i) if i not in queue else None
        else:
            continue
        #print('flip_flop', flip_flops)
        #print('queue', queue)
    print('fin')
    print('flip_flop', flip_flops)
    #print('conjunction', conjunctions)
    #print('nb_low_pulse', nb_low_pulse)
    #print('nb_high_pulse', nb_high_pulse)
    return nb_low_pulse, nb_high_pulse, flip_flops
    

def part_1(dico_line, flip_flops, conjunctions):
    print(dico_line)
    nb_low_pulse_total = 0
    nb_high_pulse_total = 0

    deep_copy_flip_flops = copy.deepcopy(flip_flops)
    for i in range(1000):
      nb_low_pulse, nb_high_pulse, flip_flops = press_button(dico_line, flip_flops, conjunctions)
      nb_low_pulse_total += nb_low_pulse
      nb_high_pulse_total += nb_high_pulse
      print('nb_low_pulse_total', nb_low_pulse_total)
      print('nb_high_pulse_total', nb_high_pulse_total)
      print('conjunction', conjunctions)
      print('produit', nb_low_pulse_total * nb_high_pulse_total)
        

    
      


                
  
#def part_2(matrice):

def main():
    now = time.time()
    lines = read_file(sys.argv[1]) if len(sys.argv) > 1 else read_file('input_light.txt')
    flip_flops, conjunctions, dico_line = format_data(lines)
    part_1(dico_line, flip_flops, conjunctions)


    print('script execution time', time.time() - now)
    

    


if __name__ == "__main__":
    main()
   