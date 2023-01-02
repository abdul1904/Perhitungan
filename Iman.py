import streamlit as st
from streamlit_option_menu import option_menu
import math

with st.sidebar :
    selected = option_menu ("Perhitungan Impedansi Karakteristik dan Konstanta Propagasi",
    ["Perhitungan Impedansi Karakteristik",
    "Perhitungan Konstanta Propagasi"],
    default_index=0)

if(selected == "Perhitungan Impedansi Karakteristik") :
    st.title("Perhitungan Impedansi Karakteristik")

    r = st.number_input ("masukan nilai Resistor", 0)
    l= st.number_input ("masukan nilai Induktor", 0)
    c= st.number_input ("masukan nilai Kapasitor", 0)
    g= st.number_input ("masukan nilai Konduktansi", 0)
    f= st.number_input ("masukan nilai frekuensi", 0)
    hitung = st.button ("hitung Konstanta Progagasi")

    if hitung : 
        Z_Propagasi=(((r+complex(0,2*math.pi*f*l))/(g+complex(0,2*math.pi*f*c)))**0.5)
        st.write("nilai Impedansi Karakteristik adalah = ", Z_Propagasi)
        st.success(f"nilai Impedansi Karakteristik adalah = {Z_Propagasi} ohm")
    
if(selected == "Perhitungan Konstanta Propagasi") :
    st.title("Perhitungan Konstanta Propagasi")

    r = st.number_input ("masukan nilai Resistor", 0)
    l= st.number_input ("masukan nilai Induktor", 0)
    c= st.number_input ("masukan nilai Kapasitor", 0)
    g= st.number_input ("masukan nilai Konduktansi", 0)
    f= st.number_input ("masukan nilai frekuensi", 0)
    hitung = st.button ("hitung Konstanta Progagasi")

    if hitung : 
        K_Propagasi=(((r+complex(0,2*math.pi*f*l))*(g+complex(0,2*math.pi*f*c)))**0.5)
        st.write("nilai konstanta propagasi adalah = ", K_Propagasi)
        st.success(f"nilai konstanta propagasi adalah = {K_Propagasi}")