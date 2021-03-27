# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:30:16 2021

@author: liadb
"""

def revword(word:str) -> str:
    word = word.lower() #מעביר לאותיות קטנות
    return(word[::-1]) #עוברת על המילה ומחזירה אותה בסדר הפוך

def countword()->int:
    count = 0 #סופר כמה פעמים מופיעה המילה שבשורה הראשונה בשאר הקובץ
    forstart=0 #על מנת רק בפעם (שורה) הראשונה לקרוא את המילה
    worde = 'x' #המילה שאצטרך למצוא בשאר הקובץ
    handle=open('text.txt','r')
    for line in handle:
        for word in line.split():
            forstart = forstart + 1
            if forstart == 1:
                worde = line.strip()
                count = count + 1
                continue
            word = revword(word)
            if word == worde:
                count = count + 1
    return(count)


'''
bob=open('text.txt','r')
for line in bob:
    line = line.upper().rstrip()
    print(line)
    
file =open('text.txt','r')
savecount=0
count=0
for line in file:
        # reading each word        
    for word in line.split():
        word =revword(word)
        print(word) 
        if word == 'you':
            count = count + 1
print(count)
'''