from AccelBrainBeat.brainbeat.binaural_beat import BinauralBeat



frequencies = [
    {'left': 666, 'right': 706},
]


for freq_par in frequencies:
    left = freq_par.get('left')
    right = freq_par.get('right')
    output_file_name = f'./output/Binaural sound - {right-left}Hz - Left {left}, Right {right}.wav'

    print(f'Starting generating noise: {output_file_name}')

    brain_beat = BinauralBeat()  # for binaural beats.
    brain_beat.save_beat(
        output_file_name=output_file_name,
        frequencys=(left, right),
        play_time=3600,
        volume=0.5
    )
