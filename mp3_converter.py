#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert wav to mp3 in Python.

@author: mrroo5
"""
from pydub import AudioSegment


def convert_wav_to_mp3(wav_path='data/twinkle_star.wav', mp3_path='data/twinkle_star.mp3'):
    AudioSegment.from_wav(wav_path).export(mp3_path, format="mp3")


if __name__ == '__main__':
    convert_wav_to_mp3()
