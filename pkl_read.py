import pickle
# inf = pickle.load(open('/home/xuwenqiang/flash/SlowFast-main/configs/Charades/SLOWFAST_8x8_R50.pkl',"rb+"))
inf = pickle.load(open('/home/xuwenqiang/flash/charades_完整模型/SLOWFAST_16x8_R50.pkl',"rb+"))
print(inf.keys())#查看pkl文件中的键值
print(inf)#读取数据
for var in inf.keys():
     data3=inf[var][:]
     print(var,data3.shape)
     #查看各键值对应的shape
