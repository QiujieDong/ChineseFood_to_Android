 
from keras.models import load_model
import tensorflow as tf
import os 
import os.path as osp
from keras import backend as K

#file path
input_path = 'model path'
weight_file = 'model name'
weight_file_path = osp.join(input_path,weight_file)
output_graph_name = weight_file[:-5] + '.pb' 

#convert function
def hdf5_to_pb(h5_model,output_dir,model_name,out_prefix = "output_",log_tensorboard = True):
    if osp.exists(output_dir) == False:
        os.mkdir(output_dir)
    out_nodes = []
    for i in range(len(h5_model.outputs)):
        out_nodes.append(out_prefix + str(i + 1))
        tf.identity(h5_model.output[i],out_prefix + str(i + 1))
    sess = K.get_session()
    from tensorflow.python.framework import graph_util,graph_io
    init_graph = sess.graph.as_graph_def()
    main_graph = graph_util.convert_variables_to_constants(sess,init_graph,out_nodes)
    graph_io.write_graph(main_graph,output_dir,name = model_name,as_text = False)
    if log_tensorboard:
        from tensorflow.python.tools import import_pb_to_tensorboard
        import_pb_to_tensorboard.import_to_tensorboard(osp.join(output_dir,model_name),output_dir)

#output path
output_dir = osp.join(os.getcwd(),"tensorflow_model")

#load Keras(hdf5) model
h5_model = load_model(weight_file_path)

#convert keras(hdf5) to tensorflow(pb) model
hdf5_to_pb(h5_model,output_dir = output_dir,model_name = output_graph_name)
print('model saved')
