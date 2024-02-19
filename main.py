# pylint: disable=import-error
import streamlit as st
import time
import beepy as beep
from threading import Thread
import os
def play1():
  beep.beep(1)
def play3():
  beep.beep(3)
def count_down(ts):
  while ts:
    st.write(ts)
    if ts<4:
      s_task=Thread(target=play3)
    else:
      s_task=Thread(target=play1)
    s_task.start()
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
