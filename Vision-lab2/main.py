from ReadBmp import ReadBmp
import matplotlib.pyplot as plt
import  numpy as np

filename1 = "1.bmp"
bmp = ReadBmp(filename1)
bmp.gray()

# 统计各像素点数
h = np.array([0 for i in range(256)])
h1 = []
for pixel in bmp.data:
    h[pixel[0]] = h[pixel[0]] + 1
    h1.append(pixel[0])
# 画出原先的直方图
plt.subplot(1,2,1)
plt.hist(h1, bins = 256)

# 归一化
hs = h / len(bmp.data)
# 计算累计分布
hp = np.array([0.0 for i in range(256)])
for i in range(256):
    hp[i] = np.round(np.sum(hs[0:i+1]) * 255)
T = hp.astype('uint8')

# 创建新图像，并统计新图像的各个像素点的个数
hn = np.array([0 for i in range(256)])
h2 = []
for pixel in bmp.data:
    s = T[pixel[0]]
    pixel[0] = s
    pixel[1] = s
    pixel[2] = s
    hn[pixel[0]] = hn[pixel[0]] + 1
    h2.append(s)
bmp.creataBmp("2.bmp")
# 画出新图像的直方图
plt.subplot(1,2,2)
plt.hist(h2, bins = 256)
plt.show()