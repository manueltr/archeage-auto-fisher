import pyautogui as ag
from directKeys import PressKey, ReleaseKey



fishDead = False

j = 0x24
y = 0x15
u = 0x16
g = 0x22
h = 0x23

print('starting test')

# look for when fish is caught
image = ag.locateOnScreen('img\startFight.png', confidence=.7, region =(800,0,1500,200))
print('starting...')

while image == None:
    image = ag.locateOnScreen('img\startFight.png', confidence=.7, region =(800,0,1500,200))


print('FISH ON!')


while True:
    if(fishDead):
        break
    BIG_REEL = ag.locateOnScreen('img\BigReel.png', confidence=.8, region = (500, 0, 1000, 250))
    if(BIG_REEL != None):
        print('big reel')
        PressKey(j)
        ReleaseKey(j)
        endBig = ag.locateOnScreen('img\endBig.png', confidence=.8, region = (500, 0, 1000, 250))
        while(endBig == None):
            endBig = ag.locateOnScreen('img\endBig.png', confidence=.8, region=(500, 0, 1000, 250))
        continue

    REEL_IN = ag.locateOnScreen('img\Reel_In.png', confidence=.8, region = (500, 0, 1000, 250))
    if (REEL_IN != None):
        print('reel in')
        PressKey(h)
        ReleaseKey(h)
        endReel = ag.locateOnScreen('img\endReel.png', confidence=.8, region = (500, 0, 1000, 250))
        while(endReel == None):
            endReel = ag.locateOnScreen('img\endReel.png', confidence=.8, region=(500, 0, 1000, 250))
        continue

    STAND_RIGHT = ag.locateOnScreen('img\standRight.png', confidence=.8, region = (500, 0, 1000, 250))
    if (STAND_RIGHT != None):
        print('stand right')
        PressKey(u)
        ReleaseKey(u)
        endRight = ag.locateOnScreen('img\endRight.png', confidence=.8, region = (500, 0, 1000, 250))
        while (endRight == None):
            endRight = ag.locateOnScreen('img\endRight.png', confidence=.8, region=(500, 0, 1000, 250))
        continue


    STAND_LEFT = ag.locateOnScreen('img\standLeft.png', confidence=.8, region = (500, 0, 1000, 250))
    if (STAND_LEFT != None):
        print('stand left')
        PressKey(y)
        ReleaseKey(y)
        endLeft = ag.locateOnScreen('img\endLeft.png', confidence=.8, region=(500, 0, 1000, 250))
        while (endLeft == None):
            endLeft = ag.locateOnScreen('img\endLeft.png', confidence=.8, region=(500, 0, 1000, 250))
        continue

    SLACK = ag.locateOnScreen('img\slack.png', confidence=.8, region = (500, 0, 1000, 250))
    if (SLACK != None):
        print('slack')
        PressKey(g)
        ReleaseKey(g)
        endSlack = ag.locateOnScreen('img\endSlack.png', confidence=.8, region=(500, 0, 1000, 250))
        while (endSlack == None):
            endSlack = ag.locateOnScreen('img\endSlack.png', confidence=.8, region=(500, 0, 1000, 250))
        continue
    FISH_DEAD = ag.locateOnScreen('img\deadFish.png', confidence=.8, region=(800,0,1500,200))
    if(FISH_DEAD != None):
        fishDead = True



print('ded Fish')










