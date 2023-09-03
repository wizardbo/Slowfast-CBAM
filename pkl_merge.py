import pickle
import numpy as np
import pandas as pd

with open("D:\\projects\\ncData\\weekly1.pkl", 'rb+') as f:
    a = pickle.load(f)  # 待合并的pkl文件a
with open("D:\\projects\\ncData\\weekly2.pkl", 'rb+') as f:
    b = pickle.load(f)  # 待合并的pkl文件b

# 根据所需数组维度和空间使用numpy.zeros建立好zero数组，本案例中有7个key
# a文件各数组shape为[104,20,100;；b文件各数组shape为[2087,20,100];故合并后的新文件数组shape为[2191,20,100]
dates_weekly = pd.date_range(start='1979-01-01', end='2020-12-31', freq="w")
m_tem = np.zeros((2191, 20, 100), dtype=np.float32)
m_P_SURF = np.zeros((2191, 20, 100), dtype=np.float32)
m_U_WIND = np.zeros((2191, 20, 100), dtype=np.float32)
m_V_WIND = np.zeros((2191, 20, 100), dtype=np.float32)
m_U_CURRENT = np.zeros((2191, 20, 100), dtype=np.float32)
m_V_CURRENT = np.zeros((2191, 20, 100), dtype=np.float32)

# 使用numpy.append对同维度数组进行延伸，本案例将a中变量加到b文件中，键值一一对应保持不变，沿x轴进行延伸
m_tem = np.append(b['SST'], a['SST'], axis=0)
m_P_SURF = np.append(b['P_SURF'], a['P_SURF'], axis=0)
m_U_WIND = np.append(b['U_WIND'], a['U_WIND'], axis=0)
m_V_WIND = np.append(b['V_WIND'], a['V_WIND'], axis=0)
m_U_CURRENT = np.append(b['U_CURRENT'], a['U_CURRENT'], axis=0)
m_V_CURRENT = np.append(b['V_CURRENT'], a['V_CURRENT'], axis=0)
dataset_weekly = {"LAT": a['LAT'], "LON": a['LON'], "DATE": dates_weekly, "SST": m_tem, "U_WIND": m_U_WIND,
                  "V_WIND": m_V_WIND,
                  "U_CURRENT": m_U_CURRENT, "V_CURRENT": m_V_CURRENT, "P_SURF": m_P_SURF}
with open("D:\\projects\\ncData\\concat.pkl",
          'wb') as f:
    pickle.dump(dataset_weekly, f, protocol=4)  # 写入新的pkl文件
f.close()
