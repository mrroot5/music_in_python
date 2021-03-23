#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write `Happy Birthday` from sine waves.

@author: mrroot5
"""
import numpy as np
from scipy.io import wavfile
import utils

if __name__ == '__main__':
    right_hand_notes = ['D2', 'C1',
                        'G5', 'E3', 'C1',
                        'F4', 'F4', 'E3', 'C1', 'D2', 'C1']
    right_hand_duration = [1, 1,
                           1, 1, 1,
                           1, 1, 1, 1, 1, 1]

    left_hand_notes = ['G4', 'G4', 'A3', 'G4', 'C1', 'B2',
                       'G4', 'G4', 'A3', 'G4',
                       'G4', 'G4', 'B2', 'A3']
    left_hand_duration = [1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1,
                          1, 1, 1, 1]

    factor = [0.68, 0.26, 0.03, 0. , 0.03]
    length = [0.01, 0.6, 0.29, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    sustain_level = 0.1
    right_hand = utils.get_song_data(right_hand_notes, right_hand_duration,
                                     factor, length, decay, sustain_level)
    factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01, 0.01]
    length = [0.01, 0.29, 0.6, 0.1]
    decay = [0.05, 0.02, 0.005, 0.1]
    left_hand = utils.get_song_data(left_hand_notes, left_hand_duration,
                                    factor, length, decay, sustain_level)
    data = left_hand + right_hand
    data = data * (4096 / np.max(data))
    wavfile.write('data/twinkle_star.wav', 44100, data.astype(np.int16))
