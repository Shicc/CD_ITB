import torch.utils.data as data
import os
import cv2
import pandas as pd

class myDataset(data.Dataset):
    def __init__(self, path, label_path):
        self.path = path
        self.labels = pd.read_csv(label_path)
    
    def __getitem__(self, index):
        """返回图片(numpy.ndarray)，[诊断类型,诊断结果](list)，镜下所见(str)"""
        # 每个病人都有28张图片
        p = os.listdir(r"./" + self.path)
        f = os.listdir(r"./" + self.path + '/' + p[index//28-1])
        img = cv2.imread(self.path + '/' + p[index//28-1] + '/' + f[index%28-1])
        details = self.labels.loc[self.labels['id'] == p[index//28-1]]
        # 描述需要转化成词向量，据说之后会提供，待更改
        return img, [details['诊断类型'].to_string(), details['诊断结果'].to_string()], [details['镜下所见'].to_string()]

    def __len__(self):
        num = 0
        for directory in os.walk(r"./" + self.path):
            for i in directory[1]:
                num += len(os.listdir("./" + directory[0] + '/' + i))
        return num


# def collate_fn(data):
#     pass

def get_data_loader(path, label_path, batch_size, shuffle, num_workers):
    myData = myDataset(path, label_path)
    data_loader = data.DataLoader(dataset=myData,
                                  batch_size=batch_size, 
                                  shuffle=shuffle,
                                  num_workers=num_workers)
    return data_loader
