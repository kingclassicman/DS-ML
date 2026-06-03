import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning (Chanakan) ")
st.markdown(''':rainbow[Chanakan Punnuwong] ''')
st.info("7 Day Intensive Hands-on Workshop")
st.info(" ******************************** Hello ชาวโลก ******************************** ")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานแล")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("💰 ทำความสะอาดข้อมูล ไฟล์แก้ไขด้วย AI"):
    st.switch_page("pages/clean_app_KingClassicMan.py")
elif st.button("💰 ทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_app.py")
elif st.button("💰 ทำความสะอาดข้อมูล Customer"):
    st.switch_page("pages/clean_customers.py")
elif st.button("💰 แปลงข้อมูล"):
    st.switch_page("pages/transform_app.py")
elif st.button("💰 การวิเคราะห์ข้อมูลเชิงสำรวจ"):
    st.switch_page("pages/EDA_app.py")


