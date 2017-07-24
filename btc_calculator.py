import time
print('''
#~########################################################
#~ Wellcome to BTC Calculator V0.5                        #
#~ Every input is manual for now And till v1 Update       #
#~ Made By ShardX ~                                       #
#~        V.5 (Manual Input)    Final Update : V1#        #
#~########################################################
''')

def start():
    print('''
$~  Type test for default values,
$~  Type Tinfo To Check the Test Defualt Values
$~  Type Manual for Manual Inputs
$~  Type README for Readme xP
''')
    Choice = str(input())
    if Choice == ('test'):
        test()
    elif Choice == ('Tinfo'):
            print('''
~ Price = 600$
~ GH/S = 100000GH = 10TH
~ Time = 10 Week
~ Diff = 225832872179
~ Coins Per Block 12.5
-- HardWare Cost 100000$
''')
            time.sleep(4)
            start()
    elif Choice == ('Manual'):
        inputs()
    elif Choice == ('README'):
        print('''
-- Since There is no Diff Live Source in v.5 Every Week will have Give the Same Amount of BTC !
-- This is Not 100% Because Again there is not Live Diff Source
''')
        time.sleep(1)
        start()
    else:
        print('Not A Valid Option')
        time.sleep(1)
        start()
def inputs():
    global Price, GH, TimeR, Diff, CPB, HWC
    print('BTC Price, ex 600')
    Price = int(input())
    print('Mining Speed in GH/S')
    GH = int(input())
    print('How long will you mine ? 0 for 1Year')
    Time = int(input())
    if Time == 0:
        Time = Time + 48
    TimeR = Time + 1
    print('Diff , 0 for 1250M')
    Diff = int(input())
    if Diff == 0:
        Diff = Diff + 12500000000
    print('Coins Per Block ? Defualt is 12')
    CPB = int(input())
    print('HardWare Cost 0 For none')
    HWC = int(input())
    Calc()

def test():
    global Price, GH, TimeR, Diff, CPB, HWC
    Price = 600
    GH = 100000
    TimeR = 10
    Diff = 225832872179
    CoinPerBlock = 12.5
    CPB = CoinPerBlock
    HWC = 100000
    #Seconds Weekly = 605800 $~Fixed 
    Calc()

def Calc():
    global Price, GH, Diff
    for x in range(1, TimeR):
        global TimeR, CPB
        Profit =  CPB * GH * 2000000 / Diff * 2 / 32
        BTC2USD = int(Profit * Price)
        print('In the %sth Week Profit %s BTC Translates inTo %s$'% (x, Profit, BTC2USD) )
    global TimeR, Profit
    Total = Profit * TimeR
    TotalUSD = Profit * TimeR * Price
    global HWC
    TAH = TotalUSD - HWC        #Total After Hardware Cost
    print('''

Total Profit in {} Weeks is {} BTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Which Translates to {}$
With a {} As Hardware Cost The Final Profit
Will be {}
'''.format(TimeR, Total, TotalUSD, HWC, TAH))
    time.sleep(2)
    print('Type 1 To Do another Calculation 2 To Exit')
    Choice2 = int(input())
    if Choice2 == 1:
        start()
    elif Choice2 == 2:
        quit()
start()
