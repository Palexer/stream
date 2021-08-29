import cv2, sys
from flask import Flask, send_from_directory, Response, jsonify, request

def gen_frames():

    # get video capture device with correct ID
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


app = Flask(__name__)

# routing
# video stream
@app.route("/video_stream")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

# sensor data API
@app.route("/sensor_data_api", methods=["GET"])
def sensor_data():
    if request.method != "GET":
        return

    # test values for now
    response = jsonify({
        "temperature": "20°",
        "humidity": "50%",
        "sensor3": "123"
    })

    response.headers.add("Access-Control-Allow-Origin", "*") # CORS support
    return response


if __name__ == "__main__":
    # start server
    app.run(debug=True, threaded=True, host="0.0.0.0", port=8080)
    # app.run(threaded=True)

