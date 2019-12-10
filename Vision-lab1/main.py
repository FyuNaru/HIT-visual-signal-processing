from ReadBmp import ReadBmp
from Noise import Noise
from WaveFilter import WaveFilter
from EdgeDetection import EdgeDetection

# 创建高斯噪声图像
noise = Noise()
noise.GaussianNoise("1.bmp", "2.bmp")
# 创建椒盐噪声图片
noise.SaltAndPepperNoise("1.bmp", "3.bmp")

# 对椒盐噪声图像进行均值滤波
filter = WaveFilter()
filter.MeanFilter("3.bmp", "4.bmp")
# 对椒盐噪声图像进行中值滤波
filter.MedianFilter("3.bmp", "5.bmp")

# Sobel算子边缘检测
detection = EdgeDetection()
detection.Sobel("1.bmp", "6.bmp")
# Roberts算子边缘检测
detection.Roberts("1.bmp", "7.bmp")