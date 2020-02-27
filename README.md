# archeage-auto-fisher

Setting location regions help improve code run time and therefore it has to be personalized.

Easiest way find your tab locations is to take a screenshot <br />
and use a software such as 3d paint(crop) to find pixel distances.

If the script is not performing a task, try changing the confidence level, 1 being the most precise and 0 none. You will probably have to lower it.

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
 
 
