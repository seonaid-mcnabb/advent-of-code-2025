52
53
54
55 X
56
57
58
59
60
61
62
63
64
65
66 X
67
68
69
70
71
72
73
74
75

75 - 52
7 - 5 = 2


Case 2
11 X
12
13
14
15
16
17
18
19
20
21
22 X


CASE 3
1112 - 1200 , there is no invalid number possible
1200-1300 , 1212 would be invalid 
1300-1400, 1313 would be invalid
1400-1500, 1414 would be invalid
1500 - 1600, 1515 would be invalid
1600-1700, 1616 would be invalid

1649 - 1112 ... 16 - 11 = 5


89451761-89,562,523

89,451,761 x
89,458,945 1
89,468,946 2
89,478,947 3
89,488,948 4
89,498,949 5
89,508,950 6
89,518,951 7
89,528,952 8
89,538,953 9
89,548,954 10
89,558,955 11

8956 - 8945 = 11

89,562,523 - 110,7262


CASE 4
6631446-6694349
none, odd number of digits


CASE 5
8,664,371,543–8,664,413,195
86644 - 86643

Im seeing some patterns here that might be useful.
** No odd-number-of-digis number will ever meet the condition

I can:
splice my string in half to get the first half of the first number in the range.
8945, in the example above
if there are 4 characters, I know the total number is 8 characters
I know that to get to the original number, I can raise the current 4-digi number to the 3rd power(half digits-1)


if I examine the first splice of the second half I'll see:
1761
8945 x= 1761


5168-7482

STARTING POINT 51|68 - 74|82

74-51 = I should expect 23 steps between the two + 1 if starting point is in range

Formula to determine if first number will be  in range:
x = 51
y = 68

if x >= y:
add + 1 to total pairs expected
 --> no, keep at 23

x = 74
y = 82

if x <= y 
 maintain count
otherwise subtract
--> were good to maintain at 23

steps = 23

To find our first pair, I know that I cant start at 5151 because my current is higher
x+=1
x=52 
(52 * 10 ^ 2) + x

for i in range(steps -1):
    additional = (10 ** 2) +1
    x += additional
    array.append(x)

5252
5353
    



Say for example in the above case 
range start


EDGE CASES TO HAVE IN MIND
1) Starting range might report an additional invalid number through subtraction, but not truly (ie. in case of 1213 start)
2) The same applies to the ending range --> it may be below the number required to reach for invalidity

5168-7482

section start -  51
section end - 74
number of digits - 4
can an invalid id exist here - yes
first possible repeated-half number - 5252
last possible repeated half number - 7474


1. Calculate bounds before entering loop
2. loop for the established bounds