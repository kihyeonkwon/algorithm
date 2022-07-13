beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer2={}

for i in beer :
    beer2[i] = beer[i]*1.05

print('{0}'.format(beer))
print('{0}'.format(beer2))