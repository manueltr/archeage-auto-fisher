from pyautogui import locateOnScreen as LoS

from directKeys import PressKey, ReleaseKey

# keys here
j = 0x24
y = 0x15
u = 0x16
g = 0x22
h = 0x23

# set pixel coordinates 
skill_bar = (0, 0, 500, 500)

while True:
    
    BIG_REEL = LoS('img\BigReel.png', confidence=.8, region=skill_bar)
    if BIG_REEL:
        print('big reel')
        PressKey(j)
        ReleaseKey(j)

        endBig = None
        while endBig == None:
            endBig = LoS('img\endBig.png', confidence=.8, region=skill_bar)

    REEL_IN = LoS('img\Reel_In.png', confidence=.8, region=skill_bar)
    if REEL_IN:
        print('reel in')
        PressKey(h)
        ReleaseKey(h)

        endReel = None
        while(endReel == None):
            endReel = LoS('img\endReel.png', confidence=.8, region=skill_bar)

    STAND_RIGHT = LoS('img\standRight.png', confidence=.8, region=skill_bar)
    if STAND_RIGHT:
        print('stand right')
        PressKey(u)
        ReleaseKey(u)

        endRight = None
        while endRight == None:
            endRight = LoS('img\endRight.png', confidence=.8, region=skill_bar)


    STAND_LEFT = LoS('img\standLeft.png', confidence=.8, region=skill_bar)
    if STAND_LEFT:
        print('stand left')
        PressKey(y)
        ReleaseKey(y)

        endLeft = None
        while endLeft == None:
            endLeft = LoS('img\endLeft.png', confidence=.8, region=skill_bar)

    SLACK = LoS('img\slack.png', confidence=.8, region=skill_bar)
    if SLACK:
        print('slack')
        PressKey(g)
        ReleaseKey(g)

        endSlack = None
        while endSlack == None:
            endSlack = LoS('img\endSlack.png', confidence=.8, region=skill_bar)