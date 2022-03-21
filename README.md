# realsense_test
获取camera某一帧，并保存其rgb帧，将depth数据保存于txt文件。运行环境: python 3.9

使用方法：

 1. 运行
~~~
pip install -r requirements.txt
~~~
安装相关package

 2. 连接相机，并运行
~~~
python main.py
~~~

 3.如无意外，应弹出
~~~
depth frame
~~~
及
~~~
rgb frame
~~~
两窗口，显示同一时刻的rgb帧与depth帧。

 4.根据弹出提示操作，通过按y或其他键选择是否保存当前depth数据(.txt格式)及rgb图象(.jpeg格式)。保存路径默认与
~~~
main.py
~~~
相同。
