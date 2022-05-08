s=input("Please Enter a string ")
def most_frequent(string):
    a=[]
    def lower(String):
        return s.lower()
    s1=lower(s)
    for i in range(len(s1)):
        a.append(s1[i])
    se=set(a)
    a1=[]
    for i in se:
        a1.append(a.count(i))
    se1=set(a1)
    d={}
    a2=[]
    for j in se1:
        for i in se:
            if a.count(i)==j:
                a2.append(i)
                d[i]=a.count(i)
    a2.reverse()
    for i in a2:
        print(i,"=","%.2d" % d[i])
most_frequent(s)