import mediapipe as mp #step2 is to detect the face with the help of mediapipe package
import cv2 # for image processing
import pyautogui # for mouse
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) # we will go to mediapipe solutions inside that we will call the facemesh solutions
#refine_landmarks is the specific location in which we  need the landmarks
screen_w,screen_h=pyautogui.size()
cam=cv2.VideoCapture(0)
while True:
    _,frame = cam.read()
    frame=cv2.flip(frame,1) # by default the frame is flipped so we have to flip it again for the real image and 1 is to flip vertically
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) # to easy to detect the face
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks # to make the points on the face which will detect the face coordinates
    print(landmark_points)# this will give the result of x and y coordinates of the landmarks points on the face , if face is not detected then it will print none
    frame_h,frame_w,_ = frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark # this is to detect the only single face
        for id,landmark in enumerate(landmarks[474:478]): # to detect the iris we only want 4 landmarks which are 474,475,476,477
            #enumerate is to get the index of the coordinates
            x = int(landmark.x * frame_w) # int will be required to print the circle
            y= int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255)) # this is the point that we point to draw on the face which have yellow color and has the radius of 3
            if id==1:
                screen_x =screen_w/frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x,screen_y) # to move the cursor any where in the screen
        left=[landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w) # int will be required to print the circle
            y= int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
        #print(left[0].y-left[1].y)
        if(left[0].y-left[1].y)<0.004:# it will give the vertical points of the eyeslid
            pyautogui.click()
            pyautogui.sleep(2)
            # we need to know the width and height  of the frame
    cv2.imshow("Moueyes",frame) # to show the captured image 
    cv2.waitKey(1) # to wait for a key if I press it.




