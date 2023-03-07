# Copy content of one file to another using file handling
with open('data.text','r') as prefile:
    data = prefile.read()

with open('copydata.txt','w+') as f:
    f.write(f"\n{data}")