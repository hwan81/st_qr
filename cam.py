import cv2
import pyzbar.pyzbar as pyzbar
import time
import streamlit as st


try:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        result, frame = cap.read()
        if result:
            #cv2.rectangle(img=frame, pt1=(100, 100), pt2=(300, 300), color=(255, 255, 255), thickness=3)
            cv2.imshow("window", frame)
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                #print(frame)
                x, y, w, h = barcode.rect
                frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 3)
                cv2.putText(frame, barcode.data.decode('utf-8'), (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255, 0, 255), 1)

                cv2.imshow("window", frame)
                #cv2.rectangle(img = frame, pt1 = (100,100), pt2 = (300,300), color = (255,255,255), thickness = 3)
                #
                #print(barcode)

            if cv2.waitKey(1) == 27:
                break

        else:
            print('error')
            break
except Exception as e:
    print(e, 'errorTT')
finally:
    cap.release()
    cv2.destroyAllWindows()

