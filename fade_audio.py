"""
Fade in and fade out an audio file.
Required:
    - `pydub`

Usage:
    `python fade_audio.py ./sample.mp3`
"""

import sys
from datetime import datetime

from pydub import AudioSegment


def fade_audio(audio_path):
    """
    Fade in and fade out an audio file.
    """

    extension = audio_path.split(".")[-1].lower()
    if extension == "wav" or extension == "mp3" or extension == "m4a":
        sound = AudioSegment.from_file(audio_path)
        sound = sound.fade_in(3000)  # fade in 3 seconds
        sound = sound.fade_out(1500)
        current_time = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        sound.export(f"{current_time}.{extension}")
        return True
    return False


if __name__ == "__main__":
    if fade_audio(sys.argv[1]):
        sys.exit(0)
    sys.exit(1)
