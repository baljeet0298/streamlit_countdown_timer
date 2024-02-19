# pylint: disable=import-error
import streamlit as st
import time
# import beepy as beep

import os
def count_down(ts):
  while ts:
    st.write(ts)
    # if ts<4:
    #   beep.beep(3)
    # else:
    #   beep.beep(1)
    time.sleep(0.5)
    ts -= 1  
  st.header("Time Up!")



if st.button("Reset", key="reset"):
  st.empty()

st.title("Countdown App")
time_value = st.slider("Pick time in sec", 0, 60, key="0")

if st.button("Start", key="start"):
  st.write(f'Timer starts for {time_value} sec')
  count_down(int(time_value))
