# archeage-auto-fisher

You need to have the opencv and pyautogui installed
run:
pip install opencv-python
pip install pyautogui

my settings- res: 2560 x 1440 and ui scale: 100%

pyautogui looks for the exact image pixel by pixel. If you don't
have my settings, You will have to update all the png files with your own.
Even then, you still might have to do so.

Easiest way find your skill bar location is to take a screenshot <br />
and use a software such as 3d paint(crop) to find pixel distances.

```python
region = (left, top, width, height)

#Ex. (top left corner)
locateOnScreen('some.png', confidence =.8, region=(0,0, 300, 400))


```

need python installed <br />
run command prompt as administrator 


 
 ## run
 ```bash
 cd <path> (folder where files are located)
 python driver.py
 ```
 
 
