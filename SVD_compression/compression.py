import caffe
import numpy as np


net = caffe.Net('/home/roy/end-to-end-car-caffe/SVD_compression/pilotnet_train(0-2,no_compression).prototxt', '/home/roy/end-to-end-car-caffe/SVD_compression/pilotnet_iter_10000(0-4,no_compression).caffemodel', caffe.TEST)
fc6_weight_matrix = net.params['fc9'][0].data[...]
fc6_biaos_matrix = net.params['fc9'][1].data[...]

print('fc6_weight_matrix is\n {}\n shape is {}'.format(fc6_weight_matrix,fc6_weight_matrix.shape))
print('fc6_biaos_matrix is\n {}\n shape is {}'.format(fc6_biaos_matrix,fc6_biaos_matrix.shape))

# u, s, vh = np.linalg.svd(fc6_weight_matrix)
# print('u is\n {}\n shape is {}'.format(u,u.shape))
# print('s is\n {}\n shape is {}'.format(s,s.shape))
# print('vh is\n {}\n shape is {}'.format(vh,vh.shape))
