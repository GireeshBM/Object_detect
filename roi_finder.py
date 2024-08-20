import cv2

# Intialize counter for each mouse click
counter = 0
# initialize dictionary to store the coordinates for inner ROI. Initialize to empty dictionary
inner_roi = {}

# Initialize dictionary to store the coordinates for outer ROI
outer_roi = {}

class BoundingBoxWidget(object):
    def __init__(self):
        self.image = cv2.imread(input("Enter the path to the image, png/jpg: "))
        self.original_image = cv2.resize(self.image, (1280, 720), interpolation=cv2.INTER_AREA)

        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # Bounding box reference points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        global counter
        global inner_roi
        global outer_roi
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            # Increment counter
            # counter += 1
            self.image_coordinates = [(x,y)]
            # Reset coube if counter is greater than 4
            # if counter > 4:
                # counter = 0

        # Record ending (x,y) coordintes on left mouse button release
        elif event == cv2.EVENT_LBUTTONUP:
            # increment counter
            counter += 1
            # print("counter: {}".format(counter))
            # Reset counter if counter is greater than 5
            if counter > 5:
                counter = 0
            self.image_coordinates.append((x,y))
            # print('top left: {}, bottom right: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            # print('x,y,w,h : ({}, {}, {}, {})'.format(self.image_coordinates[0][0], self.image_coordinates[0][1], self.image_coordinates[1][0] - self.image_coordinates[0][0], self.image_coordinates[1][1] - self.image_coordinates[0][1]))
            x = self.image_coordinates[0][0]
            y = self.image_coordinates[0][1]
            w = self.image_coordinates[1][0] - self.image_coordinates[0][0]
            h = self.image_coordinates[1][1] - self.image_coordinates[0][1]
            # Add ROI coordinates to either inner dict or outer dict
            # If counter is less than or equal to 3, attributes belong to inner ROI. Each click will add x,y coordinates to inner_roi dictionary as x1, y1 upto x3, y3
            if counter <= 4:
                inner_roi['x' + str(counter)] = x
                inner_roi['y' + str(counter)] = y
                print('inner_roi: {}'.format(inner_roi))
            # If counter is greater than 3, attributes belong to outer ROI. Each click will add x,y coordinates to outer_roi dictionary as x4, y4 upto x5, y5
            else:
                outer_roi['x'] = x
                outer_roi['y'] = y
                outer_roi['w'] = w
                outer_roi['h'] = h
                print('outer_roi: {}'.format(outer_roi))

            # Draw rectangle
            cv2.rectangle(self.clone, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)
            cv2.imshow("image", self.clone)

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone

if __name__ == '__main__':
    boundingbox_widget = BoundingBoxWidget()
    while True:
        cv2.imshow('image', boundingbox_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)