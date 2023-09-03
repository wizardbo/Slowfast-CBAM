import pickle
with open('D:\\projects\\ncData\\test_sst_u_v_wind_u_v_current_pre_weekly_average_20190101-20201228.pkl',"rb+") as f2:
    data_daily_inference2=pickle.loads(f2.read())
    for i in range(0,100):
                data_daily_inference2['SST'][i] = data_daily_inference2['SST'][i] - 273.15 # 选择key为'SST'的一维数组进行更改，开尔文转换成摄氏度
                f2.write(data_daily_inference2['SST'][i])  # 将转换完的SST写入原文件
f2.close()#关闭文档

print(data_daily_inference2['SST'])#查看转换后的数据
