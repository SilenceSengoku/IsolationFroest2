import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import MinMaxScaler

#read data
dataset = pd.read_csv('customers_nums.csv',engine='python')
#set variable
rs = np.random.RandomState(169);
outliers_fraction = 0.05;lendata = dataset.shape[0]
#label
anomaly = [];test_data = []
#sit normalize limited
nmlz_a = -1;nmlz_b = 1;

#some function is useful
def normalize(dataset,a,b):
    scaler = MinMaxScaler(feature_range=(a, b))
    normalize_data = scaler.fit_transform(dataset)
    return normalize_data

#read dataset x,y
x = normalize(pd.DataFrame(dataset, columns=['cr']), nmlz_a, nmlz_b)
y = normalize(pd.DataFrame(dataset, columns=['7wr']), nmlz_a, nmlz_b)
#
ifm = IsolationForest(n_estimators=100, verbose=2, n_jobs=2,
                      max_samples=lendata, random_state=rs, max_features=2)

if __name__ == '__main__':
    Iso_train_dt = np.column_stack((x, y))
    ifm.fit(Iso_train_dt)
    scores_pred = ifm.decision_function(Iso_train_dt)

    threshold = stats.scoreatpercentile(scores_pred, 100 * outliers_fraction)
    # 使用预测值取5%分位数来定义阈值（基于小概率事件5%）
    # 根据训练样本中异常样本比例，得到阈值，用于绘图

    # matplotlib
    # plot the line, the samples, and the nearest vectors to the plane
    xx, yy = np.meshgrid(np.linspace(nmlz_a, nmlz_b, 50), np.linspace(nmlz_a, nmlz_b, 50))  # 画格子
    Z = ifm.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.title("IsolationForest ")# plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)
    otl_proportion = int(outliers_fraction * len(dataset['Date']))
    plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, otl_proportion), cmap=plt.cm.hot)# 绘制异常点区域，值从最小的到阈值的那部分
    a = plt.contour(xx, yy, Z, levels=[threshold], linewidths=2, colors='red')# 绘制异常点区域和正常点区域的边界
    plt.contourf(xx, yy, Z, levels=[threshold, Z.max()], colors='palevioletred')
    # palevioletred 紫罗兰
    # 绘制正常点区域，值从阈值到最大的那部分

    for i in scores_pred:
        if i <= threshold:
            #print(i)
            test_data.append(1)
            anomaly.append(i)
        else:
            test_data.append(0)

    ano_lable = np.column_stack(((dataset['Date'],dataset['data'],x,y,scores_pred, test_data)))
    df = pd.DataFrame(data=ano_lable, columns=['Date','data','x', 'y', 'IsoFst_Score','label'])

    b = plt.scatter(df['x'][df['label'] == 0], df['y'][df['label'] == 0], s=20, edgecolor='k',c='white')
    c = plt.scatter(df['x'][df['label'] == 1], df['y'][df['label'] == 1], s=20, edgecolor='k',c='black')
    plotlist = df.to_csv('Iso_list.csv')

    plt.axis('tight')
    plt.xlim((nmlz_a, nmlz_b))
    plt.ylim((nmlz_a, nmlz_b))
    plt.legend([a.collections[0], b, c],
               ['learned decision function', 'true inliers', 'true outliers'],
               loc="upper left")
    print("孤立森林阈值  ：",threshold)
    print("全量数据样本数：",len(dataset),"个")
    print("检测异常样本数：",len(anomaly),"个")
    plt.show()

