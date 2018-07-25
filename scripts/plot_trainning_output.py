import matplotlib.pyplot as plt
import numpy as np

def plot_data(data, label):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)    
    ax.set_title(label)
    ax.set_xlabel('epochs')
    ax.plot(data)
    plt.show()

def extract_log(log, key_word):
    validation_dice_coeffs = []
    losses = []

    for line in log:        
        if 'Validation Dice Coeff' in line:
            bidx = line.find('Dice Coeff:')
            coeff = float(line[bidx+len('Dice Coeff:'):].strip())
            validation_dice_coeffs.append(coeff)
        if '--- loss:' in line:
            bidx = line.find('--- loss:')
            loss = float(line[bidx+len('--- loss:'):].strip())
            losses.append(loss)

    return validation_dice_coeffs, losses

import sys

def main():    
    log_file = sys.argv[1]
    log = open(log_file,'r')
   
    coeffs, losses = extract_log(log, 'Dice Coeff')
    plot_data(coeffs, 'Dice Coeff')
    plot_data(losses, 'losses')
    log.close()

if __name__ == '__main__':
    main()

