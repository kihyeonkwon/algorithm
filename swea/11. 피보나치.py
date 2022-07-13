
# nazi = [1, 1]
# for i in range (8):
#     newnazi = (nazi[-1] + nazi[-2])
#     nazi = nazi +[newnazi]



nazi = [1, 1]
nazi2 = [nazi.append(nazi[-1] + nazi[-2]) for i in range (8)]
print(nazi)
