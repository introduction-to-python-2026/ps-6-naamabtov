def create_codon_dict(file):
  
    file=open(path)
    rows=file.readlines()
    file.close()
    
    codon2aa={}
    for i in rows:
         newlist=i.strip().split('\t')
         key= newlist[0]
         value= newlist[2]
         codon2aa[key]=value
  
    return codon2aa

print(codon2aa)

