from ReadBmp import ReadBmp
import random

class Noise:
    def GaussianNoise(self, filename1, filename2):
        bmp = ReadBmp(filename1)
        # 生成均值为means，方差为sigma，噪声比为percetage的高斯噪声图像
        means = 8
        sigma = 10
        percetage = 1
        for pixel in bmp.data:
            # 图像灰度化
            gray = 0.299 * pixel[0] + 0.578 * pixel[1] + 0.114 * pixel[2]
            p = random.random()
            # 增加高斯噪声
            if p <= percetage:
                gray = gray + random.gauss(means, sigma)

            if gray < 0:
                gray = 0
            elif gray > 255:
                gray = 255

            pixel[0] = round(gray)
            pixel[1] = round(gray)
            pixel[2] = round(gray)
        # 将新图像保存到文件
        bmp.creataBmp(filename2)
        return

    def SaltAndPepperNoise(self, filename1, filename2):
        bmp = ReadBmp(filename1)
        # 生成椒盐噪声图像
        percetage = 0.05
        for pixel in bmp.data:
            # 图像灰度化
            gray = 0.299 * pixel[0] + 0.578 * pixel[1] + 0.114 * pixel[2]
            p = random.random()
            # 增加椒盐噪声
            if p <= percetage:
                if p <= percetage * 0.5:
                    gray = 0
                else:
                    gray = 255

            pixel[0] = round(gray)
            pixel[1] = round(gray)
            pixel[2] = round(gray)

        # 将新图像保存到文件
        bmp.creataBmp(filename2)
        return