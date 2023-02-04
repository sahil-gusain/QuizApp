import face_recognition
from os import remove
from onlinequiz.settings import BASE_DIR
import cv2

def recognizeFace(faceid):
         cam = cv2.VideoCapture(0)
         ret, frame = cam.read()
         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
         rgb_small_frame = small_frame[:, :, ::-1]
    
         cv2.imwrite(BASE_DIR+'/student/face/Image.jpg',rgb_small_frame)
    
         unknown = face_recognition.load_image_file(BASE_DIR + '/student/face/Image.jpg')
         try:
           unknown_encode = face_recognition.face_encodings(unknown)[0]
         except IndexError as e:
            ProperExit1(cam)
            recognizeFace(faceid)
   
         
         known = face_recognition.load_image_file(BASE_DIR + '/student/face/Image'+str(faceid)+'.jpg')
         known_encode = face_recognition.face_encodings(known)[0]
         
         
         
         matches = face_recognition.compare_faces([known_encode], unknown_encode)
         if matches[0]==True:
            
            return True
    
         ProperExit1(cam)
         return False
   
def ProperExit1(cam):
    remove(BASE_DIR + '/student/face/Image.jpg')
    cam.release()
    cv2.destroyAllWindows()

def ProperExit2(cam,faceid):
    remove(BASE_DIR + '/student/face/Image'+str(faceid)+'.jpg')
    cam.release()
    cv2.destroyAllWindows()

def registerface(faceid):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    cv2.imwrite('C:\\Users\\sahil\\Desktop\\Quizapp\\Quiz\\QuizApp\\Quiz\\student\\face\\Image'+str(faceid)+'.jpg',rgb_small_frame)

    known = face_recognition.load_image_file(BASE_DIR + '/student/face/Image'+str(faceid)+'.jpg')
    known_encode = face_recognition.face_encodings(known)[0]
    try:
        known_encode = face_recognition.face_encodings(known)[0]
    except:
        ProperExit2(cam,faceid)
        registerface(faceid)