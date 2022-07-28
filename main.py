import cv2
from realsense_camera import *
import os
import sys
import time


# 将数组arr写入位置dest
def write_into_text(arr, dest):
    with open(os.path.join(os.path.dirname(sys.argv[0]), 'data', dest), 'w', encoding='UTF-8') as f:
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
        cv2.imshow("depth frame", depth_frame)
        cv2.imshow("rgb frame", rgb_frame)  # depth frame 和 rgb_frame是相機獲取到的一幀的rgb圖像和深度圖像，imshow将其以窗口形式展现
        # obtain current time for filenames
        current_time = time.strftime('%Y%m%d_%H%M%S')  # 获取当前时间，精确到秒，用于给文件命名

        print("Save current depth data and RGB frame? [y/others]")  # 获取两个图像后，提示是否保存深度数据及rgb图象
        # 121 = 'y' in ASCII
        # （点一下rgb frame的窗口让他在最上方，然后按y就会进入下面的if代码）
        # 如果按了其他，就会重新开始while段获取新的两帧图像）
        if cv2.waitKey(1000000) == 121:
            depth_output_file = 'depth_{}.txt'.format(current_time)
            # save depth as .txt
            write_into_text(depth_frame, depth_output_file)  # 深度数据的本质还是1280*720的数组，这个方法将数组写到txt文件上
            # Notice when succeed
            print("Depth data saved as {}!".format(os.path.join(os.path.dirname(sys.argv[0]), depth_output_file)))

            # save current rgb frame as .jpeg
            frame_output_path = os.path.join(os.path.dirname(sys.argv[0]), 'data', 'rgb_{}.jpeg'.format(current_time))
            cv2.imwrite(frame_output_path, rgb_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            # notice when succeed
            print("Frame saved as {}!".format(frame_output_path))
