weight=[40,56,75,746,54,45,63,25,53,35]
v=0
normalizedata=[]
for i in weight:
    v=i-min(weight)
    v1=max(weight)-min(weight)
    v=v/v1
    normalizedata.append(v)

normalizedata