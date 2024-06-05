import pandas as pd

def str2list(sIn):
    lsOut=[]
    if "[[" in sIn and "]]" in sIn:
        if "]," in sIn:
            _ls=sIn.split("],")
            for s in _ls:
                lsOut.append(s.replace("[","").replace("]",""))
        else:
                lsOut.append(sIn.replace("[","").replace("]",""))
            
    return lsOut


df=pd.DataFrame({"id":['111','222','333','444','555','666']})

df["compat"]=[
    "[['222','D',123],['333','B',234],['555','A',999]]",
    "[['333','B',234],['444','C',134]]",
    "[['666','D',123],['333','B',234],['555','A',999],['444','F',97]]",
    "[['666','G',5],['555','A',999]]",
    "[['444','D',123]]",
    "[['111','D',123],['333','B',234],['555','A',999]]"
]


df["expand"]=df["compat"].apply(lambda x: str2list(x))

df_ex=df[['expand']].explode("expand")

df_ex[['id','cat','amt']]=df_ex['expand'].str.split(',', expand=True)

