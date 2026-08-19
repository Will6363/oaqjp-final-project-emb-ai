from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        tests = []
        tests.append(("I am glad this happened","joy"))
        tests.append(("I am really mad about this","anger"))
        tests.append(("I feel disgusted just hearing about this","disgust"))
        tests.append(("I am so sad about this", "sadness"))
        tests.append(("I am really afraid that this will happen", "fear"))

        for i in tests:
            self.assertEqual(emotion_detector(i[0])['dominant_emotion'], i[1])

    
unittest.main()