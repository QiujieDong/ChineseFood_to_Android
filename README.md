# ChineseFood_to_Android

创建ChineseFood项目的Android APk

# 一、将keras生成的hdf5模型转换成tensorflow的pb模型
- 使用：keras_to_tensorflow.py，输入自己的hdf5模型相应的path,然后运行即可
- 打开terminal，然后输入$ tensorboard --logdir=生成的pb文件所在的父文件夹
    - 例如：生成的pb文件位置为./model/tensor/my.pb,那么输入tensorboard --logdir=./model/tensor）；
    - 然后打开浏览器的‘127.0.1.1：6006’，即可看到自己生成的pb模型的tensorboard，记录下最开始的输入和最后的输出，一般为‘input_1’和‘output_1’
      
      如果出现：6006端口被占用：lsof -i:6006，找到占用的进程的PID; 然后杀死进程：kill -9 占用的PID
# 二、修改tensorflow给出的Android例子
- clone:[[Tensorflow]](https://github.com/tensorflow/tensorflow)
- 
