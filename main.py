import cv2
import pyautogui

# haar cascade used
hand_cascade = cv2.CascadeClassifier("hand.xml")

cap = cv2.VideoCapture(0)

# Camera width and height
cam_width  = cap.get(3) 
cam_height = cap.get(4)

# Screen width and height
width, height = pyautogui.size()



# Mapping camera position to screen position and moving mouse
def moveMouse(x, y):
    move_x = (x * width) / cam_width
    move_y = (y * height) / cam_height
    
    pyautogui.moveTo(move_x, move_y)



while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detection
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Placing rectangle and calling moveMouse-function
    for (x,y,w,h) in hands:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        moveMouse(cam_width - x, y)
    
    # Reflect the image
    frame = cv2.flip(frame, 1)
    
    # Display output to screen
    cv2.imshow('Move Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Exit Cleanly
cap.release()
cv2.destroyAllWindows()