import matplotlib.pyplot as plt
import numpy as np

data2 = np.loadtxt('train (copy).txt', delimiter=' ', dtype='str')
[row2, col2] = data2.shape
print('row2 {},col2 {}'.format(row2, col2))


angle2 = data2[:, 1].astype('float')
name = data2[:, 0]
max_angle = max(angle2)
min_angle = min(angle2)



threshold = 0.5

j = 0
angle2 = angle2.tolist()
name = name.tolist()
for element in angle2:
    if angle2[j] > 0:
        if angle2[j]/max_angle >= threshold:
            del angle2[j]
            del name[j]
    if angle2[j] < 0:
        if angle2[j]/min_angle >= threshold:
            del angle2[j]
            del name[j]
    j = j + 1
