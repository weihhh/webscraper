import pickle

pkl=open('恰恰恰好的.pkl','rb')
data=pickle.load(pkl)
pkl.close()
for i in data:
    print(i,len(data[i]))
print(data)