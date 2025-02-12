#todo
#revamp menu to vertical list instead of horizontal (90% done, double check)
#add dynamic discord intergration

#shortcut: 
# sp = skill heal% 
# sf = skill heal flat 
# a = alternate, b = alt 2 
# hm = outgoing healing (healing multiplier)
# sk = skill level
inthp = 'Input HP: '
intch = 'Input the number corresponding to the character: '
intsk = 'Input skill level: '
intak = 'Input Atk: '
intsl = 'Input Superimposition level: '
intype = 'Input the corresponding number for your desired calculation(s)'
intcdmg = 'Input Crit Damage: '
typeint = '1.skill 2.ult 3.talent 4.summon'
skheal = 'Skill healing is: '
lc404 = 'Invalid lightcone'
sl404 = 'Invalid superimposition level, assuming highest level...'
ult404 = 'This character does not have heal scaling on ultimate, defaulting to skill.'
char404 = 'Character does not exist on database/invalid number, returning to main menu...'
skill404 = 'Unobtainable skill level, returning to menu...'
type404 = 'Invalid skill type, returning to main menu'
choice404 = 'Invalid number, defaulting to no'
enterstart = 'Press Enter without any input to go back'

#imports
import math
import os
import random
import webbrowser
from pypresence import *
import time

#1313762516945342494 #application key

#equations
#num = ((((hp*sp)+sf)*hm)//1)+1
#numa = ((((hp*spa)+sfa)*hm)//1)+1
#numb = ((((hp*spb)+sfb)*hm)//1 )+1
#numc = (((atk*sp)+sf)*hm)+1  atk scaling skill
#ATK Total = (Character Base ATK + LC Base ATK) * (1 + ATK%) + Flat ATK

#math process
#stat calculation uses math.ceil
#hp heal uses round
#atk heal uses math.floor

#hp 
def calc(hp, sp, sf, hm): #skill heal calculation(hp)
     sf = float(sf)
     x = ((((hp*sp)+sf)*hm))+1
     x = round(x)
     print('Skill healing is '+str(x))
     
def acalc(hp, spa, sfa, hm): #ult heal calculation(hp)
     sfa = float(sfa)
     y = ((((hp*spa)+sfa)*hm))+1
     y = round(y)
     print('Ult healing is: '+ str(y))
     
def aacalc(hp, spa, sfa, uhm): #post op heal calculation for ult(hp) 
    sfa = float(sfa)
    yy = ((((hp*spa)+sfa)*uhm))+1
    yy = round(yy)
    print('Ult healing is '+str(yy))
    
def aaacalc(hp, spa, sfa, hm): #adjacent heal calculation(hp)
     sfa = float(sfa)
     y = ((((hp*spa)+sfa)*hm))+1
     y = round(y)
     print('Skill adjacent healing is: '+ str(y))
       
def bcalc(hp, spb, sfb, hm): #talent heal calculation(hp)
    sfb = float(sfb)
    z = ((((hp * spb) + sfb) * hm))+1
    z = round(z)
    print('Talent healing is: '+ str(z))
    
#atk
def ccalc(atk, sp, sf, hm): #skill heal calculation(atk)
     sf = float(sf)
     a = ((((atk*sp)+sf)*hm))
     a = round(a)
     print('Skill healing is '+ str(a))
     
def cccalc(atk, spa, sfa, hm): #ult heal calculation(atk)
     sfa = float(sfa)
     y = ((((atk*spa)+sfa)*hm))
     y = round(y)
     print('Ult healing is: '+ str(y))

#crit dmg advance
def critcalc(critdmg, sp, sf):
    print()
    x = round((critdmg*sp)+sf,2)
    print('Crit Dmg buffed is: '+str(x))
    sparklecalculator()

def critcalc2(critdmg, sp, sf):
    print()
    x = round((critdmg*sp)+sf,2)
    print('Crit Dmg buffed is: '+str(x))


#typecast
def fc(x,y,z):
     x = float(x)
     y = float(y)
     z = float(z)

#the main calculator
def calculator1():
    hm = 1
    print()
    print('[Healing Calculator]')
    print()

    print('Are you using Outgoing Healing Boost on your body piece?')
    try:
        outgoinghealing = int(input('0.Back 1.Yes 2.No: '))
        if outgoinghealing == 1:
            hm = 1.345
        elif outgoinghealing ==2:
            hm = hm 
        elif outgoinghealing == 0:
            startmenu()
        else:
            print(choice404)
            hm = hm
        print()
        print('10% = 0.1, 33.5% = 0.335, 5% = 0.05 etc...')
        rhm = float(input('Input any additional Outgoing Healing Boost from relics: '))
        print()
        print('Input the number corresponding to your current Light Cone.')
        print('Note that the code assumes the chosen Light Cone buff is active and at max stacks.')
        print(enterstart)
        print()
        print('0. None of them')
        print('1. Hey, Over Here')
        print('2. Perfect Timing')
        print('3. Shared Feeling')
        print('4. Post-Op Conversation')
        print('5. Time Waits for No One')
        lc = input('Input number: ')
        if lc == '':
            calculator1()
        elif lc == '0':
            nhm = 0
        elif lc == '1':
            sl = int(input(intsl))
            if sl == 1:
                nhm = 0.16
            elif sl == 2:
                nhm = 0.19
            elif sl == 3:
                nhm = 0.22
            elif sl == 4:
                nhm = 0.25
            elif sl == 5:
                nhm = 0.28
            else:
                print(sl404)
                nhm = 0.28
        elif lc == '2':
            sl = int(input(intsl))
            if sl == 1:
                nhm = 0.15
            elif sl == 2:
                nhm = 0.18
            elif sl ==3:
                nhm = 0.21
            elif sl == 4:
                nhm =0.24
            elif sl ==5:
                nhm = 0.27
            else:
                print(sl404)
                nhm = 0.27
        elif lc == '3':
            sl = int(input(intsl))
            if sl == 1:
                nhm = 0.1
            elif sl == 2:
                nhm = 0.12
            elif sl ==3:
                nhm = 0.15
            elif sl ==4:
                nhm = 0.17
            elif sl ==5:
                nhm = 0.2
            else:
                print(sl404)
                nhm = 0.2
        elif lc == '4':
            sl = int(input(intsl))
            if sl == 1:
                uhm = 0.12
                nhm = 0
            elif sl ==2:
                uhm = 0.15
                nhm = 0
            elif sl ==3:
                uhm = 0.18
                nhm = 0
            elif sl ==4:
                uhm = 0.21
                nhm = 0
            elif sl ==5:
                uhm = 0.24
                nhm =0
            else:
                print(sl404)
                uhm = 0.24
                nhm = 0
            uhm = hm + uhm
        elif lc == '5':
            sl = int(input(intsl))
            if sl == 1:
                nhm = 0.12
            if sl == 2:
                nhm = 0.14
            if sl == 3:
                nhm = 0.16
            if sl == 4:
                nhm = 0.18
            if sl== 5:
                print('LMAOOOO IMAGINEEEE')
                nhm = 0.2
            else:
                print(sl404)
                nhm = 0.2
        else: 
            print(lc404)
            calculator1()
        hm = hm + nhm
        hm = rhm + hm
        print()
        print('Current Total Outgoing Healing Boost: ' + str(hm))
        print()
        print('1 for 4*, 2 for 5* ')
        starclass = int(input(intch))
        if starclass == 1:
            print()
            print('1.Lynx ')
            char4 = int(input(intch))
            if char4 == 1:
                hp = float(input(inthp))
                Stype = int(input('1 for E skill, 2 for Ultimate skill'))
                if Stype == 1:
                    sk = int(input(intsk))
                    if sk == 1:
                        sp = 0.05
                        sf = 50
                        spa = 0.08
                        sfa = 80
                        sf = float(sf)
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 2:
                        sp = 0.053
                        sf = 80
                        spa = 0.085
                        sfa = 128
                        sf = float(sf)
                        sfa = float(sfa)
                        num = (((hp*sp)+sf)*hm)//1
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 3:
                        sp = 0.055
                        sf = 103
                        spa = 0.09
                        sfa = 164
                        sf = float(sf)
                        sfa = float(sfa)
                        num = (((hp*sp)+sf)*hm)//1
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 4: 
                        sp = 0.057
                        sf = 125
                        spa = 0.095
                        sfa = 200
                        sf = float(sf)
                        sfa = float(sfa)
                        num = (((hp*sp)+sf)*hm)//1
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 5: 
                        sp = 0.06
                        sf = 140
                        spa = 0.1
                        sfa = 224
                        sf = float(sf)
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 6: 
                        sp = 0.063
                        sf = 155
                        spa = 0.104
                        sfa = 248
                        sf = float(sf)
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 7:
                        sp = 0.066
                        sf = 166
                        spa = 0.108
                        sfa = 266
                        sf = float(sf)
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 8: 
                        sp = 0.069
                        sf = 178
                        spa = 0.112
                        sfa = 284
                        sf = float(sf)
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 9: 
                        spa = 0.116
                        sfa = 302
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 10: 
                        spa = 0.12
                        sfa = 320
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 11: 
                        spa = 0.124
                        sfa = 338
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    elif sk == 12: 
                        spa = 0.128
                        sfa = 356
                        sfa = float(sfa)
                        numa = (((hp*spa)+sfa)*hm)//1
                        print('skill healing is: '+str(numa))
                    else:
                        print(skill404)
                        calculator1()
                elif Stype == 2: #ult
                    sk = int(input(intsk))
                    if sk == 1:
                        spa = 0.09
                        sfa = 90
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 2:
                        spa = 0.096
                        sfa =144
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 3:
                        spa = 0.101
                        sfa = 185
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 4:
                        spa = 0.107
                        sfa = 225
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 5:
                        spa = 0.113
                        sfa = 252
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 6:
                        spa = 0.117
                        sfa = 279
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 7:
                        spa = 0.122
                        sfa = 299
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 8:
                        spa = 0.126
                        sfa = 320
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 9:
                        spa = 0.131
                        sfa = 340
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 10:
                        spa = 0.135
                        sfa = 360
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 11:
                        spa = 0.319
                        sfa = 380
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    elif sk == 12:
                        spa = 0.144
                        sfa = 401
                        if lc == 4:
                            aacalc(hp,spa,sfa,uhm)
                        else:
                            acalc(hp,spa,sfa,hm)
                    else:
                        print(skill404)
                        calculator1()
                else: print(type404)
                calculator1()
            else: 
                print(char404)
                calculator1()
        elif starclass == 2:
            print()
            print('0. Fu Xuan')
            print('1. Huohuo')
            print('2. Luocha')
            print('3. Lingsha')
            print()
            char5 = int(input(intch))
            if char5 == 1:
                hp = float(input(inthp))
                print(ult404)
                sk = int(input(intsk))
                if sk == 1:
                    sp = 0.14
                    sf = 140
                    spa = 0.112
                    sfa = 112
                    spb = 0.03
                    sfb = 30
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 2:
                    sp = 0.149
                    sf = 224
                    spa = 0.119
                    sfa = 179
                    spb = 0.032
                    sfb = 48
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 3:
                    sp = 0.157
                    sf = 287
                    spa = 0.126
                    sfa = 230
                    spb = 0.034
                    sfb = 62
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 4:
                    sp = 0.166
                    sf = 350
                    spa = 0.133
                    sfa = 280
                    spb = 0.036
                    sfb = 75
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 5:
                    sp = 0.175
                    sf = 392
                    spa = 0.14
                    sfa = 314
                    spb = 0.037
                    sfb =84
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 6:
                    sp = 0.182
                    sf = 434
                    spa = 0.146
                    sfa = 347
                    spb = 0.039
                    sfb = 93
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 7:
                    sp = 0.189
                    sf = 466
                    spa = 0.151
                    sfa = 372
                    spb = 0.041
                    sfb = 100
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 8:
                    sp = 0.196
                    sf = 497
                    spa = 0.157
                    sfa = 398
                    spb = 0.042
                    sfb = 107
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 9:
                    sp = 0.203
                    sf = 529
                    spa = 0.162
                    sfa = 423
                    spb = 0.044
                    sfb = 113
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 10:
                    sp = 0.21
                    sf = 560
                    spa = 0.168
                    sfa = 448
                    spb = 0.045
                    sfb =120
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 11:
                    sp = 0.217
                    sf = 592
                    spa = 0.174
                    sfa = 473
                    spb = 0.046
                    sfb =127
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                elif sk == 12:
                    sp = 0.224
                    sf = 623
                    spa = 0.179
                    sfa = 498
                    spb = 0.048
                    sfb =134
                    calc(hp,sp,sf,hm)
                    aaacalc(hp,spa,sfa,hm)
                    bcalc(hp,spb,sfb,hm)
                    calculator1()
                else:
                    print(skill404)
                    calculator1()
            elif char5 == 2:
                atk = float(input(intak))
                print(ult404)
                sk = int(input(intsk))
                if sk == 1:
                    sp = 0.4
                    sf = 200
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 2:
                    sp = 0.43
                    sf = 320
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 3:
                    sp = 0.45
                    sf = 410
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 4:
                    sp = 0.48
                    sf =500
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 5:
                    sp =0.5
                    sf =560
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 6:
                    sp =0.52
                    sf =620
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 7:
                    sp =0.54
                    sf =665
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 8:
                    sp =0.56
                    sf =710
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 9:
                    sp =0.58
                    sf =755
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 10:
                    sp = 0.6
                    sf = 800
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 11:
                    sp =0.62
                    sf =845
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                elif sk == 12:
                    sp =0.64
                    sf =890
                    ccalc(atk,sp,sf,hm)
                    calculator1()
                else:
                    print(skill404)
                    calculator1
            elif char5 == 0: 
                hp = float(input(inthp))
                num = ((hp*0.05)+133)//1
                print('Ult healing is '+str(num))
                calculator1()
            elif char5 == 3:
                print()
                print('Use built in stat calculator?')
                usecalc = int(input('1.Yes 2.No: '))
                if usecalc == 1:
                    atk,hm = lingsha(hm)
                elif usecalc == 2:
                    print()
                    atk = float(input(intak))
                    print()
                    print('does your break effect equal to or exceed 200%?')
                    BEbonus = int(input('1.yes 2.no :'))
                    if BEbonus == 1:
                        hm +=0.2
                    elif BEbonus ==2:
                        hm = hm
                    else:
                        print(choice404)
                        hm = hm
                else:
                    print(choice404)
                    print()
                    atk = float(input(intak))
                print('current healing bonus is ' + str(hm))
                print(intype)
                print('lingshas heal scaling with her ult and summon is the same so it will be in the same category')
                Stype = int(input('1.skill 2.ult+talent(summon): '))
                if Stype == 1:
                    sk = int(input(intsk))
                    if sk == 1:
                        sp = 0.1
                        sf = 105
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 2:
                        sp = 0.105
                        sf = 168
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 3:
                        sp = 0.11
                        sf = 215
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 4:
                        sp = 0.115
                        sf = 262
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 5:
                        sp = 0.12
                        sf = 294
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 6:
                        sp = 0.124
                        sf = 325
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 7:
                        sp = 0.128
                        sf = 349
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 8:
                        sp = 0.132
                        sf = 372.75
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 9:
                        sp = 0.136
                        sf = 396.375
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 10:
                        sp = 0.14
                        sf = 420
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 11:
                        sp = 0.144
                        sf = 433.625
                        ccalc(atk,sp,sf,hm)
                        calculator1()
                    elif sk == 12:
                        sp = 0.148
                        sf = 467.25
                        ccalc(atk,sp,sf,hm)
                        calculator1()                
                elif Stype == 2:
                    sk = int(input(intsk))
                    if sk == 1:
                        spa = 0.08
                        sfa = 90
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 2:
                        spa = 0.085
                        sfa = 144
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 3:
                        spa = 0.09
                        sfa = 184
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 4:
                        spa = 0.095
                        sfa = 225
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 5:
                        spa = 0.1
                        sfa = 252
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 6:
                        spa = 0.104
                        sfa = 279
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 7:
                        spa = 0.108
                        sfa = 299
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 8:
                        spa = 0.112
                        sfa = 319
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 9:
                        spa = 0.116
                        sfa = 339
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 10:
                        spa = 0.12
                        sfa = 360
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 11:
                        spa = 0.124
                        sfa = 380
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    elif sk == 12:
                        spa = 0.128
                        sfa = 400
                        ccalc(atk,spa,sfa,hm)
                        calculator1()
                    else:
                        print(type404)
                        calculator1
            else:
                print(char404)
                calculator1()
        else:
            print(char404) 
            calculator1()
    except ValueError:
        print('ValueError, Please input a number. Returning to calculator')
        calculator1()

#lingsha attack calculator 
#0, 33, 0.038, 0.432, 40, 0.159, 0, 0.432, 0, 0, 0
def lingsha(hm): #1 is %, 2 is flat
    try:
        print()
        print('Input Atk% values and flat A tk values')
        print('For percentages, 10% = 0.1, 15% = 0.15, 3% = 0.03 etc, and for flat numbers, input them as is.')
        baseatk = 679.0
        print()
        print('gallagher 4* and QPQ is 423, 5* sig is 529')
        baseatk2 = int(input('input atk on lightcone: '))
        baseatk = baseatk + baseatk2
        print()
        atkhead1 = float(input('input the atk% on your headpiece: '))
        atkhead2 = float(input('input the flat atk on your headpiece: '))
        atkhand1 = float(input('input the atk% on your hand piece: '))
        atkhand2 = 352.0
        atkbody1 = float(input('input the atk% on your body piece: '))
        atkbody2 = float(input('input the flat atk on your body piece: '))
        atkboots1 = float(input('input the atk% on your boots: '))
        atkboots2 = float(input('input the flat atk on your boots: '))
        atkorb1 = float(input('input the atk% on your orb: '))
        atkorb2 = float(input('input the flat atk on your orb: '))
        atkrope1 = float(input('input the atk% on your rope: '))
        atkrope2 = float(input('input the flat atk on your rope: '))
        print()
        print('Are your atk traces maxed?')
        tracemax = int(input('1.Yes  2.No : '))
        if tracemax == 1:
            trace = 0.1
        elif tracemax == 2:
            trace = 0
        else:
            print(choice404)
            trace = 0
        print()
        print('Does your break effect equal to or exceed 200%?')
        BEbonus = int(input('1.Yes 2.No :'))
        if BEbonus == 1:
            thm = 0.2
            LStrace = 0.5
        elif BEbonus == 2:
            thm = 0
            LStrace = 0
        else:
            print(choice404)
            thm = 0
            LStrace = 0
        atkhead1 = baseatk*atkhead1
        atkhead1 = math.ceil(atkhead1)
        atkhand1 = baseatk*atkhand1
        atkhand1 = math.ceil(atkhand1)
        atkbody1 = baseatk*atkbody1
        atkbody1 = math.ceil(atkbody1)
        atkboots1 = baseatk*atkboots1
        atkboots1 = math.ceil(atkboots1)
        atkorb1 = baseatk*atkorb1
        atkorb1 = math.ceil(atkorb1)
        atkrope1 = baseatk*atkrope1
        atkrope1 = math.ceil(atkrope1)
        trace = baseatk*trace
        trace = math.ceil(trace)
        LStrace = baseatk*LStrace
        LStrace = math.ceil(LStrace)

        percent = atkhead1 + atkhand1 + atkbody1 + atkboots1 +atkorb1 +atkrope1 + trace + LStrace + 1
        flat = atkhead2 + atkhand2 + atkbody2 + atkboots2 + atkorb2 + atkrope2
        hm = thm+hm
        atk = baseatk+percent+flat #new formula
        additionalatk = percent+flat
        print()
        print('[testing purposes]')
        print('['+'percent is: '+str(percent)+']')
        print('['+'flat is: '+ str(flat)+']')
        print('['+'total atk is: '+str(atk)+']') 
        print('['+ str(baseatk)+'+'+str(additionalatk)+']')
        print()
        return atk, hm
    except ValueError:
        print('I actually wrote the entire thing in a way that i cant just like loop you back to the start of this part, so like yea')
        print()
        calculator1()
    
#menus
def startmenu():
    print()
    print('[Welcome to the Main Menu]')
    print('1. Main Features')
    print('2. Additional Features')
    print('3. Should I pull today?')
    try:
        choice = int(input('Input Number: '))
        if choice == 1:
            firstmenu()
        elif choice == 2:
            secondmenu()
        elif choice == 3:
            gamble()
        else:
            print('Input a valid number')
            startmenu()
    except ValueError:
        print('Input a fucking number')
        print()
        startmenu()

def firstmenu():
    print()
    print('[Main features]')
    print('Press Enter without any input to go back')
    print('1. Heal Calculator')
    print('2. Crit-Score Calculator')
    print('3. Crit Dmg Buff Calculator')
    choice = input('Input Number: ')
    if choice == '':
        startmenu()
    elif choice == '1':
        calculator1()
    elif choice =='2':
        critcalculator()
    elif choice == '3':
        sparklecalculator()
    else:
        print('Input a valid number')

def secondmenu():
    print()
    print('Other Features')
    print('Press Enter without any input to go back')
    print('1. Print One Billion Numbers')
    print('2. Super Idol')
    print()
    try:
        choice = input('Input Number')
        if choice == "":
            startmenu()
        elif choice =='1':
            onebillion()
        elif choice == '2':
            superidol()
            secondmenu()
        else:
            print('Input a valid number')
            secondmenu()
    except ValueError:
        print('Input a fucking number')
        secondmenu()

#additional features
def onebillion():
    x=0
    while x<1000000000:
        print(x)
        x += 1

def critcalculator():
    print()
    print('Welcome to Damage Score Calculator, the higher your Damage Score the more well balanced your Crit ratios are!')
    print('Do take note that this is mostly an estimation. Actual data may differentiate from calculations')
    print()
    print('Input 0 to go back')
    try:
        atk = float(input('Input your Atk: ')) #3200
        print()
        if atk == 0:
            startmenu()
        critchance = float(input('Input your Crit Rate: ')) #42
        critmultiplier = float(input('Input your Crit Damage: ')) #248
        critmultiplier /= 100 #2.48
        print()
        print('Do you want to use default multiplier (200%) or Custom multiplier?')
        x = int(input('1.Default 2.Custom: '))
        if x == 1:
            Multiplier = 2.0
        elif x == 2:
            print()
            print('Input multiplier in decimal format. Example: 200% = 2, 350% = 3.5 etc')
            Multiplier = float(input('Input Multiplier: '))
        else:
            print('Using Default Multipliers')
            Multiplier = 2.0
        print()
        print('Multiplier is '+ str(Multiplier))
        print()
        notcritchance = 100.0-critchance #58
        normaldamage = atk*Multiplier #6400
        critdmg = normaldamage*critmultiplier #15872
        critavrg = critdmg*critchance #666624
        noncritavrg = normaldamage*notcritchance # 371200
        averagedmg =round((critavrg+noncritavrg)/100,1)
        print('Your Damage Score is '+ '['+str(averagedmg)+']')
        print()
        choice2 = input('1.Back 2.Calculate again: ')
        if choice2 == '1':
            startmenu()
        elif choice2 == '2':
            critcalculator()
        else:
            print('?? ok.')
            startmenu()
    except ValueError:
        print('Input a fucking number')
        critcalculator()

def superidol():
    videourl = 'https://youtube.com/shorts/aCgP8BFjrw4?si=sYPwYies_lOSg4Ig'
    webbrowser.open_new(videourl)

def gamble():
    print()
    numbers = random.sample(range(1, 1001), 6)
    a, b, c, d, e, f = numbers
    print('(Press Enter without input to go back to the menu)')
    try:
        odds_input = input('Input a random number from 1 to 1000: ')
        if odds_input == "":
            startmenu()
            return  
        odds = int(odds_input)       
        if not 1 <= odds <= 1000:
            print('Please input a number between 1 and 1000')
            gamble()
            return       
        print()
        print('Your number: ' + str(odds))
        print('Digital lottery: ', a, b, c, d, e, f) 
        if odds in (a, b, c, d, e, f):
            print()
            print('Youve just won a 0.6% chance lottery! Congratulations!')
            startmenu()
        else:
            print('Unfortunate, better luck next time!')
            startmenu()
    except ValueError:
        startmenu()

def sparklecalculator():
    print()
    print('[Crit Damage Calculator]')
    print()
    print('Press Enter Without input to go back')
    print('1. Bronya')
    print('2. Sparkle')
    print('3. Sunday')
    print('4. Remembrance MC')
    print()
    char = input('Input Number: ')
    if char == '':
        firstmenu()
    elif char == '1':
        print()
        critdmg = float(input(intcdmg))
        print()
        print('(Bronyas Crit increase comes fom her ult)')
        sk = int(input(intsk))
        if sk == 1:
            sp = 0.12
            sf = 12
            critcalc(critdmg, sp, sf)
        elif sk == 2:
            sp = 0.124
            sf = 12.8
            critcalc(critdmg,sp,sf)
        elif sk == 3:
            sp = 0.128
            sf = 0.136
            critcalc(critdmg,sp,sf)
        elif sk == 4:
            sp = 0.132
            sf = 0.144
            critcalc(critdmg,sp,sf)
        elif sk == 5:
            sp = 0.136
            sf = 0.152
            critcalc(critdmg,sp,sf)
        elif sk == 6:
            sp = 0.14
            sf = 0.16
            critcalc(critdmg,sp,sf)
        elif sk == 7:
            sp = 0.145
            sf = 17
            critcalc(critdmg,sp,sf)
        elif sk == 8:
            sp = 0.15
            sf = 18
            critcalc(critdmg,sp,sf)
        elif sk == 9:
            sp = 0.155
            sf = 19
            critcalc(critdmg,sp,sf)
        elif sk == 10:
            sp = 0.16
            sf = 20
            critcalc(critdmg,sp,sf)
        elif sk == 11:
            sp = 0.164
            sf = 20.8
            critcalc(critdmg,sp,sf)
        elif sk == 12:
            sp = 0.168
            sf = 21.6
            critcalc(critdmg,sp,sf)
        else:
            print(skill404)
            sparklecalculator()
    elif char == '2':
        print()
        critdmg = float(input(intcdmg))
        print()
        sk = int(input(intsk))
        if sk == 1:
            sp = 0.12
            sf = 27
            critcalc(critdmg,sp,sf)
        elif sk == 2:
            sp = 0.132
            sf = 28.8
            critcalc(critdmg,sp,sf)
        elif sk == 3:
            sp = 0.144
            sf = 20.6
            critcalc(critdmg,sp,sf)
        elif sk == 4:
            sp = 0.156
            sf = 32.4
            critcalc(critdmg,sp,sf)
        elif sk == 5:
            sp = 0.168
            sf = 34.2
            critcalc(critdmg,sp,sf)
        elif sk == 6:
            sp = 0.18
            sf = 36
            critcalc(critdmg,sp,sf)
        elif sk == 7:
            sp = 0.195
            sf = 38.3
            critcalc(critdmg,sp,sf)
        elif sk == 8:
            sp = 0.21
            sf = 40.5
            critcalc(critdmg,sp,sf)
        elif sk == 9:
            sp = 0.225
            sf = 42.8
            critcalc(critdmg,sp,sf)
        elif sk == 10:
            sp = 0.24
            sf = 45
            critcalc(critdmg,sp,sf)
        elif sk == 11:
            sp = 0.252
            sf = 46.8
            critcalc(critdmg,sp,sf)
        elif sk == 12:
            sp = 0.264
            sf = 48.6
            critcalc(critdmg,sp,sf)
        else:
            print(skill404)
            sparklecalculator()
    elif char == '3':
        print()
        critdmg = float(input(intcdmg))
        print()
        print('(Sundays Crit increase comes fom his ult)')
        sk = int(input(intsk))
        if sk == 1:
            sp = 0.12
            sf = 8
            critcalc(critdmg,sp,sf)
        elif sk == 2:
            sp = 0.138
            sf = 8.4
            critcalc(critdmg,sp,sf)
        elif sk == 3:
            sp = 0.156
            sf = 8.8
            critcalc(critdmg,sp,sf)
        elif sk == 4:
            sp = 0.174
            sf = 9.2
            critcalc(critdmg,sp,sf)
        elif sk == 5:
            sp = 0.192
            sf = 9.6
            critcalc(critdmg,sp,sf)
        elif sk == 6:
            sp = 0.21
            sf = 10
            critcalc(critdmg,sp,sf)
        elif sk == 7:
            sp = 0.233
            sf = 10.5
            critcalc(critdmg,sp,sf)
        elif sk == 8:
            sp = 0.255
            sf = 11
            critcalc(critdmg,sp,sf)
        elif sk == 9:
            sp = 0.278
            sf = 11.5
            critcalc(critdmg,sp,sf)
        elif sk == 10:
            sp = 0.3
            sf = 12
            critcalc(critdmg,sp,sf)
        elif sk == 11:
            sp = 0.318
            sf = 12.4
            critcalc(critdmg,sp,sf)
        elif sk == 12:
            sp = 0.336
            sf = 12.8
            critcalc(critdmg,sp,sf)
        else:
            print(skill404)
            sparklecalculator()
    elif char == '4':
        RMC()
    else:
        print('Input a valid number')
        sparklecalculator()

#Discord prescence
def setup_rich_presence():
    try:
        CLIENT_ID = '1313762516945342494'  # Replace with your Application ID
        rpc = Presence(CLIENT_ID)  # Initialize the client
        rpc.connect()  # Connect to Discord

        # Update Rich Presence with details
        rpc.update(
            state="Calculating",  # Small text
            details="Let him cook",  # Large text
            large_image="night_of_fright_800",  # Key from the assets in Developer Portal
            large_text="Huohuo omg",  # Tooltip for the large image
            small_image="night_of_fright_small",  # Key for a smaller icon (optional)
            small_text="Small Huohuo omg",  # Tooltip for the small image (optional)
            start=time.time(),  # Start time for elapsed timer
        )

        print("[Testing Purposes: Discord is open.]")
        return rpc
    except DiscordNotFound:
        print("[Testing Purposes: Discord is not open.]")
    except InvalidID:
        print("Invalid CLIENT_ID. Check your Application ID in the Developer Portal.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

#Crit Dmg buff Calculator Character Specific functions
def RMC():
    print()
    critdmg = str(input(intcdmg))
    if critdmg == '':
        sparklecalculator()
    else:
        critdmg = float(critdmg)
    print()
    print("(RMC's Crit increase comes from Mem)")
    sk = int(input('Input Memosprite Talent Level: '))
    if sk == 1:
        sp = 0.06
        sf = 12
        critcalc(critdmg, sp, sf)
    elif sk == 2:
        sp = 0.072
        sf = 14.4
        critcalc(critdmg, sp, sf)
    elif sk == 3:
        sp = 0.084
        sf = 16.8
        critcalc(critdmg, sp, sf)
    elif sk == 4:
        sp = 0.096
        sf = 19.2
        critcalc(critdmg, sp, sf)
    elif sk == 5:
        sp = 0.108
        sf = 21.6
        critcalc(critdmg, sp, sf)
    elif sk == 6:
        sp = 0.12
        sf = 24
        critcalc2(critdmg, sp, sf)
        RMC()
    elif sk == 7:
        sp = 0.132
        sf = 26.4
        critcalc2(critdmg, sp, sf)
        RMC()
    elif sk == 8:
        sp = 0.144
        sf = 28.8
        critcalc(critdmg, sp, sf)
    elif sk == 9:
        sp = 0.156
        sf = 31.2
        critcalc(critdmg, sp, sf)
    elif sk == 10:
        sp = 0.168
        sf = 33.6
        critcalc(critdmg, sp, sf)
    else:
        print(skill404)
        RMC()



#startcommand and program name
os.system("title Healing Calculator")
print('Loading...')
setup_rich_presence()
startmenu()

#pyinstaller --onefile --icon=NightofFright.ico HSRCalc.py