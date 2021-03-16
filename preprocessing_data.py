import os
import glob
import cv2  

def del_pdf(directory_name):
    print("已删除pdf扫面件:")
    for directory in os.walk(r"./"+directory_name):
        for file in glob.glob(os.path.join(directory[0], 'RPT*.jpg')):
            os.remove(file)
            print(file)

def crop_picture(directory_name):
    # 裁剪图片并保存。也可以不保存。
    for directory in os.walk(r"./" + directory_name):
        for i in directory[1]:
            for filename in os.listdir(r"./"+directory[0] + '/' + i):
                img = cv2.imread(directory[0] + '/' + i + '/' + filename) # 以numpy.ndarray的形式存着
                crop_img = img[:, 587:1817] # 这个区域是内镜图片，其他区域没有作用
                cv2.imwrite(directory[0] + '/' + i + '/' + filename, crop_img) # 其第三个参数是指定图片质量


del_pdf('data')
crop_picture('data')