import simpleaudio as sa

for i in range(100):
    wave_obj = sa.WaveObject.from_wave_file("boom.wav")
    play_obj = wave_obj.play()
