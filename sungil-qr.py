import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner
from camera_input_live import camera_input_live

step1, step2, step3 = st.tabs(["STEP1", "STEP2", "STEP3"])

with step1:
    st.write("s1")
    spread_id = st.text_input('insert google spreadsheet id')


with step2:
    # c = camera_input_live()
    # if c:
    #     st.image(c)
    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        st.write(qr_code)
    st.write('s2')