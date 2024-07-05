s = "25 26 19"
k = int(s.split(" ")[0]) #homo
m = int(s.split(" ")[1]) #hetero
n = int(s.split(" ")[2]) #homozygous recessive
sum_kmn = k+m+n

two_recess=n/sum_kmn*((n-1)/(sum_kmn-1))
two_hetero=m/sum_kmn*((m-1)/(sum_kmn-1))
hetero_recess = (n/sum_kmn)*(m/(sum_kmn-1)) + (m/sum_kmn)*(n/(sum_kmn-1))
prob_recess = two_recess + two_hetero*1/4 + hetero_recess*1/2
print(1-prob_recess)
