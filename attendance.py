import math

A,T,P = map(float, input().split())

D = 0
tP = 0
#print (tP)
def num_class(a,t,p,D,tP):

    tp2 = a
    while tP < p:
        tP = 100 * (a / t)
        math.ceil(tP)
        D = a
        #print (a,t,D,tP)
        a+=1
        t+=1 
    print(math.ceil(D - tp2))

num_class(A,T,P,D,tP)


#print(a,t,p,D,tP)
'''Attendance Calculation

Problem Statement :

 

Deepak hates going to class. He’s always concerned about his low attendance and he tries to calculate the number of classes he needs to attend from now on continuously without skipping any classes so that he can maintain the minimum attendance percentage proposed by his college. 

 

Since Deepak is bad at maths he’s asking for your help. You are given the number of classes Deepak attended till date as A, the total number of classes till date as T and the required percentage to be achieved as P.

 

You need to calculate the minimum number of classes he should attend without skipping any so that his attendance satisfies the required attendance percentage.

 

Since the answer can be a decimal, print the ceil of the answer.

 

(Note: The ceil function returns the smallest integer that is greater than or equal to x)  

 

(Example: ceil(93.1) = 94)

 

 


Constraints :

 

1 <= A <= T <= 10^9
1 <= P <= 100 
 

 

 

Input Format :

 

First-line contains three spaced integers A (attended classes),  T(Total classes),  P(Required percentage).
 

 


Output Format :

 

Print the number of classes that should attend without skipping to achieve the required percentage.
 

 

Sample Input :

 

100 200 75

 

 

Sample Output :

 

200

 

 


Explanation :

 

After attending 200 classes continuously 
Classes attended = 100 + 200 = 300
Total classes = 200 + 200 = 400
So the attendance percentage = (300/400) * 100 => 75
 

 

 

 

Things to Note for the Candidate :

 

You can use your own IDE like Visual Studio Code, Eclipse, or any other IDE that you are comfortable with to build your solution code.
The IDE provided on the platform is purely for submission. Avoid using the IDE for coding out the solution.
Test against any custom input in your own IDE. In the IDE provided on the platform, you cannot pass custom test cases and see the output. 
Use standard input and standard output in your program for the IDE to run the test cases smoothly against your code. We are giving a sample problem statement along with a solution that will pass the test cases in the IDE. - Sample Problem Statement  (Right Click and Open in New Tab to view.)'''
