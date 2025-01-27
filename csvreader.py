import os
import time
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns


data = np.loadtxt('driving_log.csv', delimiter=',', dtype='str')
[row, col] = data.shape
# angle = data[1:row, 3].astype('float')
center_name = data[1:row, 0]
left_name = data[1:row, 1]
right_name = data[1:row, 2]

# l = len(angle)

train_path = '/home/roy/end-to-end-car-caffe/train'
val_path = '/home/roy/end-to-end-car-caffe/val'
data_base_dir = "/home/roy/end-to-end-car-caffe/new_img"
dir_list = os.listdir(data_base_dir)
num_of_picture = len(dir_list)

start = time.time()
n = -1
train_file = open("train.txt", 'w')
val_file = open("val.txt", 'w')
index = 0
left_offset = 0.22
right_offset = -0.22
left_zero = 0
right_zero = 0

# angle = data[1:row, 3].astype('float')
# max_index = 90
# min_index = 0
# max_angle = max(angle)
# min_angle = min(angle)
# def mapfun(x):
#     x = x.astype('float')
#     y = round(x/(max_angle-min_angle)*(max_index-min_index))
#     return (y.astype('str'))
angle = data[1:row, 3]

for pic_name in dir_list:
    n = n + 1
    file_list = os.path.join(data_base_dir, pic_name)
    index = 0
    zero_num = 0
    if n % 10 != 0:
        for index in range(row-1):
            # if os.path.isfile(file_list):
                if center_name[index].find(pic_name)>0:
                    center_angle = angle[index].astype('float')
                    if center_angle == 0:
                        zero_num = zero_num + 1
                        if zero_num % 5 == 0:
                            train_file.write(file_list + angle[index] + '\n')
                            train_pic = os.path.join(train_path, pic_name)
                            open(train_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        train_file.write(file_list + angle[index] + '\n')
                        train_pic = os.path.join(train_path, pic_name)
                        open(train_pic, "wb").write(open(file_list, "rb").read())

                if left_name[index].find(pic_name)>0:
                    left_angle = angle[index].astype('float')
                    if left_angle == 0:
                        left_zero = left_zero + 1
                        if left_zero % 5 == 0:
                            left_angle = angle[index].astype('float') + left_offset
                            left_angle = left_angle.astype('str')
                            train_file.write(file_list + ' ' + left_angle + '\n')
                            train_pic = os.path.join(train_path, pic_name)
                            open(train_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        left_angle = angle[index].astype('float') + left_offset
                        left_angle = left_angle.astype('str')
                        train_file.write(file_list + ' ' + left_angle + '\n')
                        train_pic = os.path.join(train_path, pic_name)
                        open(train_pic, "wb").write(open(file_list, "rb").read())

                if right_name[index].find(pic_name)>0:
                    right_angle = angle[index].astype('float')
                    if right_angle == 0:
                        right_zero = right_zero + 1
                        if right_zero % 5 == 0:
                            right_angle = angle[index].astype('float') + right_offset
                            right_angle = right_angle.astype('str')
                            train_file.write(file_list + ' ' + right_angle + '\n')
                            train_pic = os.path.join(train_path, pic_name)
                            open(train_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        right_angle = angle[index].astype('float') + right_offset
                        right_angle = right_angle.astype('str')
                        train_file.write(file_list + ' ' + right_angle + '\n')
                        train_pic = os.path.join(train_path, pic_name)
                        open(train_pic, "wb").write(open(file_list, "rb").read())

        # index = 0
    elif n % 10 == 0:
        for index in range(row-1):
            # if os.path.isfile(file_list):
                if center_name[index].find(pic_name)>0:
                    center_angle = angle[index].astype('float')
                    if center_angle == 0:
                        zero_num = zero_num + 1
                        if zero_num % 5 == 0:
                            val_file.write(file_list + angle[index] + '\n')
                            val_pic = os.path.join(val_path, pic_name)
                            open(val_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        val_file.write(file_list + angle[index] + '\n')
                        val_pic = os.path.join(val_path, pic_name)
                        open(val_pic, "wb").write(open(file_list, "rb").read())

                if left_name[index].find(pic_name)>0:
                    left_angle = angle[index].astype('float')
                    if left_angle == 0:
                        left_zero = left_zero + 1
                        if left_zero % 5 == 0:
                            left_angle = angle[index].astype('float') + left_offset
                            left_angle = left_angle.astype('str')
                            val_file.write(file_list + ' ' + left_angle + '\n')
                            val_pic = os.path.join(val_path, pic_name)
                            open(val_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        left_angle = angle[index].astype('float') + left_offset
                        left_angle = left_angle.astype('str')
                        val_file.write(file_list + ' ' + left_angle + '\n')
                        val_pic = os.path.join(val_path, pic_name)
                        open(val_pic, "wb").write(open(file_list, "rb").read())

                if right_name[index].find(pic_name)>0:
                    right_angle = angle[index].astype('float')
                    if right_angle == 0:
                        right_zero = right_zero + 1
                        if right_zero % 5 == 0:
                            right_angle = angle[index].astype('float') + right_offset
                            right_angle = right_angle.astype('str')
                            val_file.write(file_list + ' ' + right_angle + '\n')
                            val_pic = os.path.join(val_path, pic_name)
                            open(val_pic, "wb").write(open(file_list, "rb").read())
                    else:
                        right_angle = angle[index].astype('float') + left_offset
                        right_angle = right_angle.astype('str')
                        val_file.write(file_list + ' ' + right_angle + '\n')
                        val_pic = os.path.join(val_path, pic_name)
                        open(val_pic, "wb").write(open(file_list, "rb").read())

        # index = 0

train_file.close()
val_file.close()

t = time.time() - start
print('n is %d'%n)
print('execution time: %0.3f'%(t))


data2 = np.loadtxt('train.txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('row2 {},col2 {}'.format(row2, col2))
angle2 = data2[1:row2, 1].astype('float')
plt.hist(angle2, bins=np.arange(-1, 1, 0.02))
plt.title("angle Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

# sns.distplot(TData, rug=True)
