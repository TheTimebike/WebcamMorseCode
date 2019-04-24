import cv2
import time

class WebcamHandler:
    def __init__(self, webcamEnum=0):
        self._webcam_number = webcamEnum
        self.conversion = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            " ": " "
        }

    def _on(self):
        self.webcam = cv2.VideoCapture(self._webcam_number)

    def _off(self):
        self.webcam.release()

    def _flash(self):
        self._on()
        time.sleep(1)
        self._off()

    def _hold(self, delay):
        self._on()
        time.sleep(delay)
        self._off()
    
    def _convert(self, to_conv):
        _converted = []
        for letter in to_conv:
            _converted.append(self.conversion[letter])
        return _converted

    def morse(self, to_conv):
        _converted = self._convert(to_conv.lower())
        for pattern in _converted:
            for character in pattern:
                if character == ".":
                    self._flash()
                elif character == "-":
                    self._hold(3)

web = WebcamHandler()
web.morse("AbCd")
