import cv2
import os
import copy


dataColor = (0,250,0)
font = cv2.FONT_HERSHEY_PLAIN
storeData = 0
className = 'NONE'
count = 0
fx , fy, fh = 10,50,45

def storeClass(name):
	global className , count
	className = name
	os.system('mkdir -p data/%s' % name)
	count = len(os.listdir('data/%s' % name))

def main():

    global storeData , font , dataColor
    global className , count
    global fx , fy, fh
    cam = cv2.VideoCapture(0)
    cv2.namedWindow('Original' , cv2.WINDOW_NORMAL)
    x0 , y0 , width = 100 , 100 , 299
    while True:
        
        ret , frame = cam.read()
        frame = cv2.flip(frame,1)
        window = copy.deepcopy(frame)
        cv2.rectangle(window,(x0,y0),(x0+width,y0+width),dataColor, 12)
        roi = frame[y0:y0+width,x0:x0+width]  
        
        if storeData:
            dataColor = (0,250,0)
            cv2.putText(window, 'Pic storing : ON' ,(fx,fy),font,1.2, dataColor,  2,1)
            cv2.imwrite('data/{0}/{0}_{1}.png'.format(className,count),roi)
            count+=1
        else:
            dataColor = (0,0,250)
            cv2.putText(window, 'Pic storing : ON' ,(fx,fy),font,1.2, dataColor,  2,1)
        cv2.putText(window, 'Class Name: %s (%d)'%(className,count),(fx,fy+fh),font,1.0,(245,210,65),2,1)
        
        
        cv2.imshow('Original', window)
        
        key = cv2.waitKey(10) & 0xff
        
        
        if key == ord('q'):
            break
        
        elif key == ord('s'):
            storeData = not storeData
            
        elif key == ord('0'): storeClass('NONE')
        elif key == ord('1'): storeClass('ONE')
        elif key == ord('2'): storeClass('TWO')
        elif key == ord('3'): storeClass('THREE')
        elif key == ord('4'): storeClass('FOUR')
        elif key == ord('5'): storeClass('FIVE')
        elif key == ord('6'): storeClass('OK')
                
        elif key == ord('i'):
            y0 = max((y0 - 5, 0))
        elif key == ord('k'):
            y0 = min((y0 + 5, window.shape[0]-width))
        elif key == ord('j'):
            x0 = max((x0 - 5, 0))
        elif key == ord('l'):
            x0 = min((x0 + 5, window.shape[1]-width))
            
    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    storeClass('NONE')
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
