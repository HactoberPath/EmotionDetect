import cv2
import os
 
 
 # Set resolution for the video capture
    # Function adapted from https://kirr.co/0l6qmh
    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
          return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']
