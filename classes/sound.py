import simpleaudio as sa
import threading


class Sound:
    LIBRARY = {
        "pew": sa.WaveObject.from_wave_file("resources/sounds/pew.wav"),
        # add more sounds here
    }

    @classmethod
    def play_sound(cls, sound_key):
        wave_obj = cls.LIBRARY.get(sound_key)
        if wave_obj is None:
            return
        t = threading.Thread(target=wave_obj.play)
        t.start()

    @staticmethod
    def set_volume(volume):
        sa.default_volume = volume
