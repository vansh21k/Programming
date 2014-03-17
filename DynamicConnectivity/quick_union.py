'''Sample Script illustrating union find with path compression optimization'''
def findRoot(i, inp):
    temp = i[0]
    while i[1] != i[0]:
        i = inp[i[1]]
    print "root of " + str(temp) + " is " + str(i[1])
    return i[1]
def find(p, q, inp):
    parent1 = findRoot(p, inp)
    parent2 = findRoot(q, inp)
    p[1] = parent1
    q[1] = parent2
    if parent1 == parent2:
        print "Connected"
    else:
        print "Not Connected"
    
def union(p,q):
    if p[2] > q[2]:
        p[2] = p[2] + q[2]
        q[1] = p[1]
    else:
        q[2] = p[2] + q[2]
        p[1] = q[1]
    print "Connected " + str(p[0]) + " and " + str(q[0])
def initialize():
    inp = [[x,x,0] for x in range(10)]
    return inp
    
inp =  initialize()
print inp
union(inp[1], inp[3])
union(inp[1], inp[6])
find(inp[1], inp[3], inp)
union(inp[2], inp[9])
union(inp[3], inp[5])
union(inp[1], inp[6])
find(inp[1], inp[9], inp)
find(inp[3], inp[7], inp)
