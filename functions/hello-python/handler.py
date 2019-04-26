# Hello World Example
#
#
# def handle(req):
#     print("Hello! You said: " + req)
import requests
import cv2 as cv


def handle(req):
    url = req
    filename = url.split("/")[-1]
    try:
        r = requests.get(url, timeout=0.5)
    except:
        print("This Link didnt work")

    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)

    # Read image from your local file system
    try:
        original_image = cv.imread(filename)
    except:
        print("cannot find image")

    # Convert color image to grayscale for Viola-Jones
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

    # Load the classifier and create a cascade object for face detection
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt.xml")

    detected_faces = face_cascade.detectMultiScale(grayscale_image)

    if len(detected_faces) <= 0:
        print("No faces Detected")
    else:
        print("Yes, faces detected")
    # for (column, row, width, height) in detected_faces:
    #     cv.rectangle(
    #         original_image,
    #         (column, row),
    #         (column + width, row + height),
    #         (0, 255, 0),
    #         2
    #     )

    # Display the image

    # cv.imshow('Image', original_image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()