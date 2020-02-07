str1="The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n."
str2="Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term."
str3="If the previous term is odd, the next term is 3 times the previous term plus 1."
str4="The conjecture is that no matter what value of n, the sequence will always reach 1."
print(str1)
print(str2)
print(str3)
print(str4)
print("Enter a natural number:")
n=int(input())
color="white"
A=0
steps=0
def collatz(A):
    global n
    if n%2==0:
        n/=2
        return n
        if n==1:
            n="1:choose new number"
    elif n%2==1:
        n=3*n+1
        return n
        if n==1:
            n="1:Choose new number"
    else:
        print("Error not a real number")
while(n>1):
    steps+=1
    print(collatz(A))
print("Total steps:",steps)