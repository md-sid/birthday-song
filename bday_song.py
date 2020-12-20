import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from playsound import playsound


samp_freq = 1046
note_freq = [262, 262, 294, 262, 349, 330, 262, 262, 294, 262, 392, 349,
             262, 262, 523, 440, 349, 330, 294, 466, 466, 440, 349, 392, 349]
note_dur = [0.5, 0.5, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 2, 0.5, 0.5, 1, 1,
            1, 1, 3, 0.5, 0.5, 1, 1, 1, 2]

y = []
x = []
for i in range(len(note_freq)):
    t = np.arange(0, note_dur[i], 1/samp_freq)
    tmp = np.cos(2*np.pi*note_freq[i]*t)
    y.append(np.array(tmp).tolist())
    if i == 0:
        x = y[i]
    else:
        x = x + y[i]

sf.write('bday_song.wav', x, samp_freq)
playsound('bday_song.wav')
time = np.linspace(0, len(x)/samp_freq, len(x))
plt.plot(time, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Plot of Birthday Song')
plt.show()
