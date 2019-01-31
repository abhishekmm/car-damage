import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 50,
    'threshold': 0.002,
}
print("1")
tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
##for video if req
##capture = cv2.VideoCapture(0)
##capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
##capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
##Read img in rbg
##srcBGR= cv2.imread('C:\\Users\\abhis\\Desktop\\car damage\\darkflow\\test\\000000.jpg')
srcBGR= cv2.imread('C:\\Users\\abhis\\Desktop\\car damage\\darkflow\\test\\000006.jpg')
frame = cv2.cvtColor(srcBGR, cv2.COLOR_BGR2RGB)
results = tfnet.return_predict(frame)
for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('frame', frame)
##print('FPS {:.1f}'.format(1 / (time.time() - stime)))
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
