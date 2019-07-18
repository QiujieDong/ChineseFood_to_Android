# ChineseFood_to_Android

创建ChineseFood项目的Android APk

# 一、将keras生成的hdf5模型转换成tensorflow的pb模型
- 使用：keras_to_tensorflow.py，输入自己的hdf5模型相应的path,然后运行即可
- 打开terminal，然后输入$ tensorboard --logdir=生成的pb文件所在的父文件夹
    - 例如：生成的pb文件位置为./model/tensor/my.pb,那么输入tensorboard --logdir=./model/tensor）；
    - 然后打开浏览器的‘127.0.1.1：6006’，即可看到自己生成的pb模型的tensorboard，记录下最开始的输入和最后的输出，一般为‘input_1’和‘output_1’
      
      如果出现：6006端口被占用：lsof -i:6006，找到占用的进程的PID; 然后杀死进程：kill -9 占用的PID
# 二、修改tensorflow给出的Android例子
- 下载[[android]](https://github.com/QiujieDong/ChineseFood_to_Android/tree/master/android);或者clone:[[Tensorflow]](https://github.com/tensorflow/tensorflow)
- 下载[[Android Studio]](https://developer.android.com/studio/index.html),安装是一定要保证“科学上网”，因为需要Google下载，还有后续代码run等，都要“科学上网”
- 打开Android Studio，选择 “Open an existing Android Studio project”，在“Open File or Project ”，选择在中对应的 tensorflow-master\tensorflow\examples\android 文件夹，OK。如果需要“Gradle Sync”，选择OK(保持科学上网连接)。第一次启动可能需要安装或更新很多模块，耐心等待。
- 在 build.gradle 文件中（在左侧 1:Project 面板  Android 下面 Gradle Scripts ），找到  nativeBuildSystem 这个变量，设置等于 “none”:
        
       // set to 'bazel', 'cmake', 'makefile', 'none'
       def nativeBuildSystem = 'none'
- 点击上方菜单 Run -> Run 'android'  命令， 如果不能运行，那就看在哪里出错，然后进入那个文件，就会看到需要安装什么，安装就可以了。我本来也没法运行，然后它让我安装各种包，我都安装了，就可以运行了。
- 如果可以运行，运行后，在assets文件夹下出现.pb文件和.txt文件，那就OK了。
# 三、修改对应的文件
我的是需要Classify,所以我修改了src/org/tensorflow/demo/ClassifierActivity.java
- 将自己的.pb文件和label.txt拷贝到assets文件夹下
- 将ClassifierActivity.java中的MODEL_FILE改成自己的pb名称
- 将ClassifierActivity.java中的LABEL_FILE改成自己的label文件
- 如果只需要Classify这一个软件，那么将主文件夹下的AndroidManifest.xml中的其他的不需要的注释掉，注意这里不是bin目录下的AndroidManifest.xml
- 点击run或者Debug

我遇到一个问题就是生成的apk进行分类时不输出label,在Debug时发现在ClassifierActivity.java找到TensorFlowImageClassifier.create，点击进入，然后找到final int numClasses = (int) operation.output(idx: 0).shape().size(i: 1);我Debug这里，然后Evaluate值 operation.output(0).shape().size(0)才是我的类别总数10，所以修改final int numClasses = (int) operation.output(idx: 0).shape().size(i: 0)
