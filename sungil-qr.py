import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=callback)




# import cv2
# import numpy as np
# import streamlit as st
#
# from camera_input_live import camera_input_live
#
# "# Streamlit camera input live Demo"
# "## Try holding a qr code in front of your webcam"
#
# image = camera_input_live(debounce=1000)
#
# if image is not None:
#     st.image(image)
#     bytes_data = image.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#
#     detector = cv2.QRCodeDetector()
#
#     data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
#
#     if data:
#         st.write("# Found QR code")
#         st.write(data)
#         with st.expander("Show details"):
#             st.write("BBox:", bbox)
#             st.write("Straight QR code:", straight_qrcode)
#

#import pyzbar.pyzbar as pyzbar
# import streamlit as st
# import cv2
# import numpy as np
#
# image = st.camera_input("Take a picture")
# st.write('image start')
# if image is not None:
#     image = st.camera_input("Take a picture")
#     st.write("image capturing")
#     #st.image(image)
#     bytes_data = image.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#
#     detector = cv2.QRCodeDetector()
#     st.write(detector)
#     data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
#
#     if data:
#         st.write("# Found QR code")
#         st.write(data)
#         with st.expander("Show details"):
#             st.write("BBox:", bbox)
#             st.write("Straight QR code:", straight_qrcode)