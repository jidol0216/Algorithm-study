# xor.py

from sklearn import svm
from sklearn import metrics
import pandas as pd

xor_data=[
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
          
          ]

xor_df =pd.DataFrame(xor_data)
data = xor_df.loc[:,0:1]
label = xor_df.loc[:,2]


clf =svm.SVC()
clf.fit(data,label)

# clf =svm.SVC()
# clf.fit([                           #학습
#     [0,0],
#     [0,1],
#     [1,0],
#     [1,1]
# ],[0,1,1,0]     #레이블(정답)

# )   

pre = clf.predict(data)
print(pre)

ac_score =metrics.accuracy_score([1,0],pre)
print(f"정답률:{ac_score}")