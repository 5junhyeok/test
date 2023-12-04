# print('파이썬')
# import streamlit as st

# st.write('hhgtj')
# a=2+3+8
# a
# st.image("호날두.jfif") 

import streamlit as st
# import random
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
  
x = []
y = []
ysin = []
for i in range(-20, 21, 1):
    x.append(i)
    y.append(3*i*i - 5*i + 2)
    # ysin.append(1200*np.sin(i))



plt.plot(x, y, 'rs-', label = '2nd Equation')
# plt.piot(x, ysin, 'go--', label = 'sin')
plt.legend()
st.pyplot(fig)












