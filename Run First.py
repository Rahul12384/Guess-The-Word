import pickle
high={'score':0,'naam':''}
fp=open('text_file.txt','wb')
pickle.dump(high,fp)
fp.close()
