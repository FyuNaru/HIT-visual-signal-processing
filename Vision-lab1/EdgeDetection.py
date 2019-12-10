from ReadBmp import ReadBmp
import math

class EdgeDetection:
    def Sobel(self, filename1, filename2):
        bmp = ReadBmp(filename1)
        # 阈值，根据实验结果大致调整的
        Gmax = 140
        for i in range(bmp.biHeight*bmp.biWidth):
            # 图像灰度化
            gray = round(0.299 * bmp.data[i][0] + 0.578 * bmp.data[i][1] + 0.114 * bmp.data[i][2])
            bmp.data[i][0] = gray
            bmp.data[i][1] = gray
            bmp.data[i][2] = gray

        new_data = []
        for j in range(bmp.biHeight):
            for i in range(bmp.biWidth):
                if i == 0 or j == 0 or i == bmp.biWidth - 1 or j == bmp.biHeight - 1:
                    new_data.append(0)
                    continue

                Gx = (-1)*bmp.data[(j + 1) * bmp.biWidth + i - 1][0] + bmp.data[(j + 1) * bmp.biWidth + i + 1][0] \
                + (-1)*bmp.data[(j - 1) * bmp.biWidth + i - 1][0] + bmp.data[(j - 1) * bmp.biWidth + i + 1][0] \
                + (-2)*bmp.data[j * bmp.biWidth + i - 1][0] + 2*bmp.data[j * bmp.biWidth + i + 1][0]

                Gy = (-1)*bmp.data[(j - 1) * bmp.biWidth + i - 1][0] + bmp.data[(j + 1) * bmp.biWidth + i - 1][0] \
                + (-1)*bmp.data[(j - 1) * bmp.biWidth + i + 1][0] + bmp.data[(j + 1) * bmp.biWidth + i + 1][0] \
                + (-2)*bmp.data[(j - 1) * bmp.biWidth + i][0] + 2*bmp.data[(j + 1) * bmp.biWidth + i][0]

                G = math.sqrt(Gx ** 2 + Gy ** 2)

                if G >= Gmax:
                    new_data.append(255)
                else:
                    new_data.append(0)

        for i in range(len(new_data)):
            bmp.data[i][0] = new_data[i]
            bmp.data[i][1] = new_data[i]
            bmp.data[i][2] = new_data[i]
        # 将新图像保存到文件
        bmp.creataBmp(filename2)

        return

    def Roberts(self, filename1, filename2):
        bmp = ReadBmp(filename1)
        # 阈值，根据实验结果大致调整的
        Gmax = 60
        for i in range(bmp.biHeight*bmp.biWidth):
            # 图像灰度化
            gray = round(0.299 * bmp.data[i][0] + 0.578 * bmp.data[i][1] + 0.114 * bmp.data[i][2])
            bmp.data[i][0] = gray
            bmp.data[i][1] = gray
            bmp.data[i][2] = gray

        new_data = []
        for j in range(bmp.biHeight):
            for i in range(bmp.biWidth):
                if j == 0 or i == bmp.biWidth - 1:
                    new_data.append(0)
                    continue
                Gx = bmp.data[(j - 1) * bmp.biWidth + i + 1][0] - bmp.data[j * bmp.biWidth + i][0]
                Gy = bmp.data[(j - 1) * bmp.biWidth + i][0] - bmp.data[j * bmp.biWidth + i + 1][0]

                G = math.sqrt(Gx ** 2 + Gy ** 2)
                if G >= Gmax:
                    new_data.append(255)
                else:
                    new_data.append(0)


        for i in range(len(new_data)):
            bmp.data[i][0] = new_data[i]
            bmp.data[i][1] = new_data[i]
            bmp.data[i][2] = new_data[i]
        # 将新图像保存到文件
        bmp.creataBmp(filename2)
        return