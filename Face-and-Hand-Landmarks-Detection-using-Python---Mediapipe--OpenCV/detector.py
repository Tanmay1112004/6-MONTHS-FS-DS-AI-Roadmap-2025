# detector.py
import time
import numpy as np
import cv2
import mediapipe as mp

class FaceHandDetector:
    """Simple wrapper around MediaPipe Holistic for face + hand landmarks."""

    def __init__(self, min_detection_confidence: float = 0.5, min_tracking_confidence: float = 0.5):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.prev_time = 0.0

    def _draw(self, image, results, draw_face: bool, draw_hands: bool):
        if draw_face and results.face_landmarks:
            self.mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                self.mp_holistic.FACEMESH_CONTOURS,
                self.mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1, circle_radius=1),
                self.mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
            )

        if draw_hands:
            if results.right_hand_landmarks:
                self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
            if results.left_hand_landmarks:
                self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)

        return image

    def process_frame(self, frame: np.ndarray, draw_face: bool = True, draw_hands: bool = True) -> np.ndarray:
        """
        Input: BGR OpenCV frame (numpy array)
        Output: processed BGR frame with landmarks + FPS overlay
        """
        if frame is None:
            return frame

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False
        results = self.holistic.process(rgb)
        rgb.flags.writeable = True
        bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        bgr = self._draw(bgr, results, draw_face, draw_hands)

        # FPS
        now = time.time()
        fps = 1.0 / (now - self.prev_time) if self.prev_time else 0.0
        self.prev_time = now
        cv2.putText(bgr, f"{int(fps)} FPS", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return bgr

    def process_bytes(self, file_bytes: bytes, draw_face: bool = True, draw_hands: bool = True) -> np.ndarray:
        """Decode bytes (from upload/camera_input) and run processing."""
        arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        return self.process_frame(img, draw_face, draw_hands)
