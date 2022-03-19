import cv2
from realsense_camera import *
import os
import sys
import time


def write_into_text(arr, dest):
    with open(os.path.join(os.path.dirname(sys.argv[0]), dest), 'w', encoding='UTF-8') as f:
        row = arr.shape[0]
        column = arr.shape[1]
        for i in range(row):
            for j in range(column):
                f.write(str(arr[i][j]))
                if j is not (column - 1):
                    f.write(' ')
            f.write('\n')


if __name__ == '__main__':
    # Load intel realsense
    rs = RealsenseCamera()
    while True:
        ret, rgb_frame, depth_frame = rs.get_frame_stream()
        cv2.imshow("dpeth frame", depth_frame)
        cv2.imshow("rgb frame", rgb_frame)
        # obtain current time for filenames
        current_time = time.strftime('%Y%m%d%H%M%S')

        print("Write depth data into txt? [y/others]")
        # 121 = 'y' in ASCII
        if cv2.waitKey(1000000) == 121:
            depth_output_file = 'depth_{}.txt'.format(current_time)
            # save depth as .txt
            write_into_text(depth_frame, depth_output_file)
            # Notice when succeed
            print("Depth data saved as {}!".format(os.path.join(os.path.dirname(sys.argv[0]), depth_output_file)))


        print("Save current RGB frame? [y/others]")
        if cv2.waitKey(1000000) == 121:
            # save current rgb frame as .jpeg
            frame_output_path = os.path.join(os.path.dirname(sys.argv[0]), 'rgb_{}.jpeg'.format(current_time))
            cv2.imwrite(frame_output_path, rgb_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            # notice when succeed
            print("Frame saved as {}!".format(frame_output_path))
