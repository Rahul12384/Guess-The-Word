import pickle
fp=open('text_file.txt','rb')
b=pickle.load(fp)
fp.close()
print(b['score'])
