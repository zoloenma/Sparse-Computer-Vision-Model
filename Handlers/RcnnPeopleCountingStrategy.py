from Core.PeopleCountingStrategy import PeopleCountingStrategy
import cv2
import numpy as np

class RcnnPeopleCountingStrategy(PeopleCountingStrategy):

    def __init__(self):
        self.net = cv2.dnn.readNetFromTensorflow("Models/frozen_inference_graph_coco.pb",
                                            "Models/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt")

    def CountPeople(self, image) -> int:
        # Input image/video/camera source
        img = image
        height, width, _ = img.shape
        people_count = 0

        # DETECT OBJECTS

        # Swap BGR to RGB, put the image(blob) into the network
        blob = cv2.dnn.blobFromImage(img, swapRB=True)
        self.net.setInput(blob)
        boxes, masks = self.net.forward(['detection_out_final', 'detection_masks'])

        detection_count = boxes.shape[2]

        for x in range(detection_count):
            # Create boxes for each detected object
            box = boxes[0,0,x]
            x = int(box[3] * width)
            y = int(box[4] * height)
            x2 = int(box[5] * width)
            y2 = int(box[6] * height)

            # Count 'person' objects
            # NOTE: [1] index is associated with the name of the class
            # (e.g. IF: index value is 0 == 'person')
            if box[1] == 0 and box[2] > 0:
                people_count = people_count + 1
                cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)

        # Show image
        cv2.imshow('Image', img)
        print('People count:', people_count)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return people_count