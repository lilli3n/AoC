#make 2dig number from each line

#PART ONE
import pandas as pd
import os
os.listdir(os.curdir)
f1 = open("dayone.txt", "r")
#split into list by '\'
words = f1.read().split()

#Take 1st & last digit
def get_tens(words):
    grand_total = 0
    total = []
    for line in words:
        first_dig = 0
        last_dig = 0
        nums = []  #append to array
        for c in line:
            if c.isdigit():
                nums.append(c)
        first_dig = nums[0]
        last_dig = nums[-1]
#         print(first_dig, last_dig)
        #join for 1 digit
        total.append(int(first_dig + last_dig))
    
    grand_total = sum(total)
    return(grand_total)

print(get_tens(words))

#P2 ***
def alpha_to_dig(arr):
    spelling = ['one','two','three','four','five',
           'six','seven','eight','nine']
    dig = [1,2,3,4,5,6,7,8,9]
    
    return(dig[spelling.index(arr)])  #return digit in same pos

def new_calibration_func(current_word):
#     print(current_word)
    digits = []
    pos = []  #combine word position
    spelling = ['one','two','three','four','five',
               'six','seven','eight','nine']
    for num in spelling:  #letters
        if (num in current_word):
            if num in pos:
                pos.append(current_word.rfind(num))   #multiple, find last
            else:
                pos.append(current_word.find(num))
            digits.append(alpha_to_dig(num))

    for c in current_word:
        if c.isdigit():
    #         if c in digits:  
    #             pos.append(words[2].rfind(c))  #multiple, find last
    #         else:
            char_pos = current_word.find(c)
            if char_pos in pos:
                pos.append(current_word.rfind(c))
            else:
                pos.append(current_word.find(c))
            digits.append(int(c))

    out = [pos,digits]
#     print(out)

    #Find the max & min positions from 1st row of out
    #first digit
    pos_min = out[0].index(min(out[0]))
    pos_max = out[0].index(max(out[0]))
    first_dig = out[1][pos_min]
    last_dig = out[1][pos_max]
    total = first_dig*10+last_dig
    return total

#Usage
total=[]
for line in words:
    total.append(new_calibration_func(line))
grand_total = sum(total)
print(grand_total)