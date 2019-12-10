from ReadBmp import ReadBmp

class WaveFilter:
    def MeanFilter(self, filename1, filename2):
        # 均值滤波， 这里对边界填充采用不做边界处理的方式
        bmp = ReadBmp(filename1)
        new_data = []
        for j in range(bmp.biHeight):
            for i in range(bmp.biWidth):
                if i == 0 or j == 0 or i == bmp.biWidth-1 or j == bmp.biHeight-1:
                    new_data.append(bmp.data[j * bmp.biWidth + i][0])
                    continue

                sum = bmp.data[j * bmp.biWidth + i + 1][0] + bmp.data[j * bmp.biWidth + i - 1][0] \
                + bmp.data[(j + 1) * bmp.biWidth + i][0] + bmp.data[(j - 1) * bmp.biWidth + i][0] \
                + bmp.data[(j + 1) * bmp.biWidth + i + 1][0] + bmp.data[(j + 1) * bmp.biWidth + i - 1][0] \
                + bmp.data[(j - 1) * bmp.biWidth + i + 1][0] + bmp.data[(j - 1) * bmp.biWidth + i - 1][0]

                new_data.append(round(sum/8))

        for i in range(len(new_data)):
            bmp.data[i][0] = new_data[i]
            bmp.data[i][1] = new_data[i]
            bmp.data[i][2] = new_data[i]
        # 将新图像保存到文件
        bmp.creataBmp(filename2)
        return

    def MedianFilter(self, filename1, filename2):
        # 中值滤波，这里对边界填充采用不做边界处理的方式
        bmp = ReadBmp(filename1)
        new_data = []
        for j in range(bmp.biHeight):
            for i in range(bmp.biWidth):
                if i == 0 or j == 0 or i == bmp.biWidth-1 or j == bmp.biHeight-1:
                    new_data.append(bmp.data[j * bmp.biWidth + i][0])
                    continue

                list = [bmp.data[j * bmp.biWidth + i + 1][0], bmp.data[j * bmp.biWidth + i - 1][0] \
                , bmp.data[(j + 1) * bmp.biWidth + i][0], bmp.data[(j - 1) * bmp.biWidth + i][0] \
                , bmp.data[(j + 1) * bmp.biWidth + i + 1][0], bmp.data[(j + 1) * bmp.biWidth + i - 1][0] \
                , bmp.data[(j - 1) * bmp.biWidth + i + 1][0], bmp.data[(j - 1) * bmp.biWidth + i - 1][0]]
                list.sort()
                median = round((list[3] + list[4])/2)
                new_data.append(median)

        for i in range(len(new_data)):
            bmp.data[i][0] = new_data[i]
            bmp.data[i][1] = new_data[i]
            bmp.data[i][2] = new_data[i]

        # 将新图像保存到文件
        bmp.creataBmp(filename2)
        return