from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    personality = "Unknown"

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        # Detect nose
        nose = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (nx,ny,nw,nh) in nose:
            cv2.rectangle(roi_color, (nx,ny), (nx+nw, ny+nh), (0,0,255), 2)

        # Detect mouth
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.3, 10)
        for (mx,my,mw,mh) in mouth:
            cv2.rectangle(roi_color, (mx,my), (mx+mw, my+mh), (255,255,0), 2)

        # Rough personality logic
        if len(eyes) >= 2 and w > h:
            personality = "Extrovert Type"
        else:
            personality = "Introvert Type"

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], "output_" + file.filename)
    cv2.imwrite(output_path, img)

    return render_template("result.html", personality=personality, user_image=output_path)

if __name__ == "__main__":
    app.run(debug=True)