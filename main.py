import pyautogui 
import numpy as np
import cv2, mss
import time

pyautogui.PAUSE = 0.1

#icon cordinates
icon_loc ={'left': 260,'top':1345 , 'width':170, 'height':195}
button_left = [921,1698]
button_right = [173,1698]

#이미지의 rgb 평균 계산하여 어떤 이미지인지 판별
def compute_icon_type(img):
    mean =np.mean(img, axis=(0, 1))
    result = 0

    if 40 < mean[0] < 60 and 40< mean[1] < 65 and 40 < mean[2] < 60:
        result = 'BOMB'
    elif 240 < mean[0]  and 75< mean[1] < 120 and 240 < mean[2] :
        result = 'SWORD'
    elif 100 < mean[0] < 130 and 150 < mean[1] < 200 and 90 < mean[2] < 110:
        result = 'POISON'
    elif 21 < mean[0] < 230 and 200 < mean[1] < 255 and 120 < mean[2] < 135:
        result = 'JEWEL'
    
    return result

def click(coords):
    pyautogui.moveTo(coords)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


while True:
    
   #capture left
    with mss.mss() as sct:
        sct_img = np.array(sct.grab(icon_loc))[:,:,:3]
        icon = compute_icon_type(sct_img)

        ##attack left
        if icon == 'SWORD' :
            print('attack left')
            click(button_left)
            
        ##fiver
        elif icon == 'JEWEL':
            print('fiver')
            click(button_left)

        ##attack right
        elif icon != 'SWORD':#icon == 'BOMB' or icon == "POISON":
            print('attack right')
            click(button_right)
        else:
            print('err',icon)
            break
        