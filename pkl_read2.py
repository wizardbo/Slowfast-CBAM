import pickle

path = '/home/xuwenqiang/flash/SlowFast-main/configs/Charades/SLOWFAST_8x8_R50.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径
#path ='/home/xuwenqiang/flash/charades_完整模型/SLOWFAST_16x8_R50.pkl'
#path = '/home/xuwenqiang/flash/charades/预训练模型/SLOWFAST_8x8_R50.pkl'
f = open(path, 'rb')
#data = pickle.load(f)
data=pickle.load(f,encoding='latin1')

print(data)
# print(len(data))
#print(data.shape)