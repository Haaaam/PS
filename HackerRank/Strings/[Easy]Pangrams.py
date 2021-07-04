def sol(s):
   alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   return set(alphabet)<set(s.lower())
s=input()
if sol(s):
    print("pangram")
else:
    print("not pangram")
