from AccelBrainBeat.brainbeat.binaural_beat import BinauralBeat



frequencies = [
    {'left': 420, 'right': 460},
    {'left': 421, 'right': 461},
    {'left': 422, 'right': 462},
    {'left': 423, 'right': 463},
    {'left': 424, 'right': 464},
    {'left': 425, 'right': 465},
    {'left': 426, 'right': 466},
    {'left': 427, 'right': 467},
    {'left': 428, 'right': 468},
    {'left': 429, 'right': 469},
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
