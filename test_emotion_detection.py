from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_dominant_emotion(self):
        # Test 1
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

        # Test 2
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")
        
        # Test 3
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")
        
        # Test 4
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")
        
        # Test 5
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")
        

unittest.main()