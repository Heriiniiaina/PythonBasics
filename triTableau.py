def permute(i1:int,i2:int):
    tmp = tab[i1]
    tab[i1] = tab[i2]
    tab[i2] = tmp
def compare(v1:int,v2:int,type):
    if type==0:
        return v1-v2
    elif type ==1:
        return v2-v1
def triTab(tab:list[int],type) -> list[int]:
    for i in range(len(tab) ):
        for j in range (i+1,len(tab)):
            if compare(tab[i],tab[j],type) < 0:
                permute(i,j)

    return tab


tab = [0,2,6,1,9,6,3,9]
type = 0 # 0 for decroissant and 1 for croissant
tri = triTab(tab,type)
print(tri)