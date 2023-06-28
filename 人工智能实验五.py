from sklearn import tree
import numpy as np

# 加载训练数据
train_data = np.loadtxt('traindata.txt', delimiter=' ',dtype=str)
X_train = train_data[:, :-1].astype(np.float64)  # 特征
y_train = train_data[:, -1]   # 标签

# 构建决策树模型
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
# 加载测试数据
test_data = np.loadtxt('testdata.txt', delimiter=' ',dtype=str)
X_test = test_data[:, :-1].astype(np.float64)  # 特征
y_test = test_data[:, -1]   # 标签

# 对测试数据进行分类
y_pred = clf.predict(X_test)
print("这个模型的预测结果如下")
for i in range(len(y_pred)):
    print(f"样本 {i+1} 的预测分类为: {y_pred[i]}")
# 计算分类准确率
accuracy = np.mean(y_pred == y_test)
print("与test比较")
print("分类准确率：", accuracy)
