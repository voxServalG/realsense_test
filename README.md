# realsense_test
获取camera某一帧，并保存其rgb帧，将depth数据保存于txt文件。
运行环境: python 3.9,需要的包见requirements.txt

使用方法：

 1. 切换到你的python环境（建议用anaconda为每个项目配置独立的环境）或在代码路径下打开命令行，运行
~~~
pip install -r requirements.txt
~~~
以安装相关package

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

 4.根据弹出提示操作，通过按y或其他键选择是否保存当前depth数据(.txt格式)及rgb图象(.jpeg格式)。默认保存在与
~~~
main.py
~~~
相同路径的Data上。
