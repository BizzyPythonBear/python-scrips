import simpleaudio as sa

for i in range(1):
    wave_obj = sa.WaveObject.from_wave_file("boom.wav")
    #wave_obj2 = sa.WaveObject.from_wave_file("yay.wav")
    #wave_obj3 = sa.WaveObject.from_wave_file("ya.wav")
    play_obj = wave_obj.play()
    #play_obj = wave_obj2.play()
    #play_obj = wave_obj3.play()
    
