s=set(map(int,input().split()))
s1=set(map(int,input().split()))
if s.isdisjoint(s1):
    print("disjoint")
else:
    print("not disjoint")