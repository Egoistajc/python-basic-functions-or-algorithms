elements=[90,90,80,85,85,84,83,81]
weights=[1,3,3,4,5,6,8,9]
print(round(sum([j[0]*j[1] for j in zip(elements, weights)])/sum(weights), 1))
