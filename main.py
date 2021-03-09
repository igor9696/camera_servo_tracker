import RPi.GPIO as GPIO
import cv2 as cv
import time
from movement import ServoControl
from flask import Flask
from flask import Response
from utilis import process_img

app = Flask(__name__)


@app.route('/')
def index():
    return "Main page"


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen():
    cap = cv.VideoCapture(0)

    while True:
        ret, img = cap.read()

        if ret:
            processed_img = process_img(img)
            output = cv.imencode('.jpg', processed_img)[1].tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + output + b'\r\n'
        else:
            break


# servo_1 = ServoControl(GPIO.BOARD, frequency=50, pin_number=16)
# servo_2 = ServoControl(GPIO.BOARD, frequency=50, pin_number=18)

# some tests

# servo_1.set_angle(90)
# servo_2.set_angle(90)

# print('Done')

# GPIO.cleanup()

if __name__ == '__main__':
    app.run(host='192.168.8.103', port=6060, debug=True)