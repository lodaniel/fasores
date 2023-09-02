# Python 3.11.4
# numpy==1.25.1
# matplotlib==3.7.2

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

print('\n***Código fasor2.py foi iniciado***\n')
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line1, = ax.plot([], [], lw=2, label='Fasor girante no sentido Anti-Horário')
line2, = ax.plot([], [], lw=2, label='Fasor girante no sentido Horário')
ax.set_xlabel('Eixo Real')
ax.set_ylabel('Eixo Imaginário')
ax.legend()

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    vector1 = np.exp(1j * frame * np.pi)  
    vector2 = np.exp(-1j * frame * np.pi)
    x1, y1 = np.real(vector1), np.imag(vector1)
    x2, y2 = np.real(vector2), np.imag(vector2)
    line1.set_data([0, x1], [0, y1])
    line2.set_data([0, x2], [0, y2])
    return line1, line2

num_frames = 200 
interval = 10     
ani = FuncAnimation(fig,update,frames=np.linspace(0,2,num_frames),init_func=init,blit=True,interval=interval)
plt.show()
print('\n***Código fasor2.py executado com sucesso***\n')
time.sleep(1)
plt.close()