import sounddevice
from scipy.io.wavfile import write
sr = 44100 #frequencia do audio
seconds = 5 #tempo de gravação (5 segundos)
print('Recording...\n')
record_voice = sounddevice.rec(sr*seconds, samplerate = sr, channels = 2)
sounddevice.wait()
print('Salvando...\n')
write('mynewfile.wav', sr, record_voice)
print('Finished!')
