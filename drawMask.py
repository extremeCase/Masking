import cv2
import numpy as np

drawing = False
rectangles = []
current_rectangle = {'start': (-1, -1), 'end': (-1, -1)}
larger_img = None  # Initialize with None
drawing_enabled = True  # Enable drawing by default

def draw_rectangle(event, x, y, flags, param):
    global drawing, rectangles, current_rectangle

    if drawing_enabled:
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            current_rectangle['start'] = (x, y)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            current_rectangle['end'] = (x, y)
            rectangles.append(dict(current_rectangle))
            cv2.rectangle(larger_img, current_rectangle['start'], current_rectangle['end'], (0, 255, 0), 2)
            cv2.imshow('img', larger_img)


def kernelFunc(img, count):
    kernel = np.ones((7, 7), np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((15, 15), np.uint8)
    dilation = cv2.dilate(opening, kernel, iterations=1)
    return dilation

def subBack(path):
    cap = cv2.VideoCapture(path)
    fgbg = cv2.createBackgroundSubtractorKNN()
    ret, frame = cap.read()
    count = 0
    width = (int)(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = (int)(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    number_of_color_channels = 3
    color = (255, 255, 255)
    img = np.full((height, width, number_of_color_channels), color, dtype=np.uint8)

    global larger_img
    while ret:
        count += 1
        fgMask = fgbg.apply(frame)
        fgMask = kernelFunc(fgMask, count)
        ret, frame = cap.read()
        if not ret:
            break
        print(count)
        img = fgbg.getBackgroundImage()
        cv2.imwrite("C:/Users/User/Desktop/lama2try/lama/LaMa_test_images/img-M.png", img)

    larger_img = img
        # cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    cv2.namedWindow('img')
    cv2.setMouseCallback('img', draw_rectangle)

    while True:
        cv2.imshow('img', larger_img)
        k = cv2.waitKey(1) & 0xFF

        if k == 13:  # Press 'enter' key to exit the loop
            break

    mask = np.zeros_like(larger_img[:, :, 0])

    for rect in rectangles:
        cv2.rectangle(mask, rect['start'], rect['end'], 255, thickness=cv2.FILLED)

    cv2.imshow('Binary Mask', mask)
    mask_resized = cv2.resize(mask, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite("C:/Users/User/Desktop/lama2try/lama/LaMa_test_images/img-M_mask.png",  mask_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def disable_drawing():
    global drawing_enabled
    drawing_enabled = False

# Example usage
# show_image("path/to/image.jpg")  # Uncomment this line to test the show_image function
