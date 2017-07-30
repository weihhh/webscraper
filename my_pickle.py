import pickle

data=[1,2,3,4,5,6]
output=open('data.pkl','wb')
pickle.dump(data,output)
output.close()