## Analysis Half-Pattern / Even-Digit Ranges

For day 2 code challenge we're tasked with finding all "invalid" numbers within a range of numbers, and then summing them together to discover the password. We get a list of ranges as input and, for each range of numbers, one condition must be met for a number within that range to be considered invalid:

* It must be composed of any sequence of numbers repeated TWICE

Given this constraint, off the bat I can conclude that:

* If a number is composed of an **odd** number of digits, then it will never meet this condition, so I'll start looking for an identifiable patter in numbers with an even number of total digits

### Analyzing specific ranges for patterns in even-digited numbers

#### Range 52-75 (where invalid numbers marked with x)
```
52, 53, 54, 55 [X], 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66 [X], 67, 68, 69, 70, 71, 72, 73, 74, 75
```

**Conclusion**: 2 numbers meet the invalid condition within this range

```
75 - 52
7 - 5 = 2
```

### Range 11-22 (where invalid numbers marked with x)
```
11 [X], 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 [X]
```
**Conclusion**: 2 invalid numbers in 11-22 range

### Range 1112-1649 (where invalid numbers marked with x)
```
1112 - 1200 , no invalid number possible
1200-1300 , 1212 would be invalid 
1300-1400, 1313 would be invalid
1400-1500, 1414 would be invalid
1500 - 1600, 1515 would be invalid
1600-1700, 1616 would be invalid
```
**Conclusion**: 5 invalid numbers in 1112-1649

### Range 89451761-89,562,523 (where invalid numbers marked with x)
**Condition**: I know the length of my numbers at each end of the range is 8 digits. That being the case, to have an "invalid number" for this range, 4 digits need to repeat themselves twice.

```
89,45 | 1,761 x (start number, not invalid)
89,45 |8,945 - 1 (allowed, in range as this number is greater than starting number)
89,46 |8,946 2
89,47 |8,947 3
89,48 |8,948 4
89,49 |8,949 5
89,50 |8,950 6
89,51 |8,951 7
89,52 | 8,952 8
89,53 | 8,953 9
89,54 | 8,954 10
89,55 |8,955 11
8956  | 2,523 x (end of my provided range, we'll never reach 8956,8956)
```
**Conclusion**: there are 11 invalid numbers in range 89451761-89,562,523

8956 - 8945 = 11

## Patterns in common with first cases
* I notice that I can (more or less) determine the number of invalid numbers that will be produced within a certain range by first: taking the end range number, and taking the first half of its digits. Next, I do the same thing with the beginning range number. To determine the number of possible pairs, I subtract the latter from the former. ie:

### Case 1
```
52 to 75

Start number
5|2
End number
7|5

7 - 5 = 2 invalid numbers in range
```
** I notice that this works only because the start range number is lower than 55, and the end number is lower than 77.

### Case 2
```
Start number
1|1
End number
2|2

2 - 1 = 1 (+1)
```
** I notice, in this case, that because the start number meets conditions, we need to add an extra 1

### Case 3
```
Start number
11|12
End number
16|49

16-11 = 5
```
**I notice that this  gives us the correct final number, as the starting number will not allow us to meet the invalid num condition if increasing

### Case 4
```
89451761-89,562,523
Start number
8945|1761
End number
8956|2523

8956 - 8945 = 11
```
** I notice that this also gives us the correct number--this time because, while the start number is before the bounds (will reach invalid status while increasing), the end number will never reach invalid status. Thinking in comparisons.

Thinking of possible rules:
If I compare the FIRST half of a number to its SECOND half, then:
* For the starting number ( I know this will increase), if x < y, then it will be included in the end count of possible invalid numbers
* For the ending number (I know this cannot increase further) if x < y, then I know it will not be included in the final count


### Analyzing invalid numbers within range
Since I more or less know the "possibility" of invalid numbers within a given range, rather than examining the whole range I am thinking that I can generate the invalid numbers in a loop oncr I know a certain amount of details.

For example, in case of range **1112-1649**, the invalid numbers are: 1212, 1313, 1414, 1515, 1616. In other words, each step adds 101 to the previous number. 

If I'm taking half the number as the "value" that I need to mirror, then how can I produce it mathematically, aka get 1212 from the number 12?

ie. 12 (do-something) = 1212

I notice I need to get to 1200, then add 12.

To get to 1200, I can do 12 * 10 ** 2
To get to 1212, I simply add 12.
So, if 12 is x, a formula could be:

```
invalid_num = (x * 10 ** 2) + x
1212
```

Can I dynamically determine the correct factor? In this case it's 2, which I notice is the length of half the number.

I test for a longer number, ie in the case of 8945|8945:

```
x=8945
factor=len(x)

invalid_number = (x * 10 ** 4) + x
89458945
```

Knowing that I have a dynamic way to increment and generate invalid numbers between ranges, I see that in order to get the full list I can likely generate numbers with my increment rate in a loop that is determined by the established bounds.

* The start bound
* The end bound
* The increment rate per loop

To determine start and end bounds, I think I need reference back a former finding (sometimes the starting number will produce an invalid number, sometimes it will not, and same goes for the end number of the range). I'll make use of the mirror here as well. Using the same example:

### Establishing bounds for 1112-1649

```
Start
x | y
11|12

if:
x >= y
start = x

else:
start = x + 1

So, 11 >= 12 --> false,
I want to start my bounds at 12

```

```
End
x | y
16|49

if:
x <= y
end = x

else:
start = x -1

So, 16 <= 49 is true -->
I want to establish my end bound at 16
```

Now I know how to calculate a dynamic increase val, and I have the range of bounds I want to iterate over to generate the invalid numbers for.

In pseudo code I can do:
```
for(number in range start, end + 1):
    increment by dynamic factor
    add result to invalid ids array

```

## Edge case
Some ranges cross over lines, ie. 900 - 1300. I think in order to handle these cases I can separate my initial range inputs into sections.

If I get a range where:

```
len(start_num) == len(end_num)
```
Then, no problem. I'll send the range for processing to another method that checks the length and, if it's not even, early exits. Otherwise, it will perform the transformations and loop to gather the invalid ids from the range.

If the lengths are NOT equal, however, I need to split into sections. I'll want to do this with the left start value (section 1) and right end value (section 2)

### Range 850 - 1300
#### Split into first section
```
start = 850
start_length = len(start) 

**I know that the minimum starting point for this section will be the input start range, so:

section_1_start = 850

To determine the end, I need to know the MAX number these 3 digits can reach. I can use a factor of 10 to determine the next boundary:

next_digit_boundary = 10 ** start_length

then determine the largest possible number in the range:
section_1_end = next_digit_boundary - 1

Whereby, section 1 would be sent for processing as:
process(section_1_start, section_1_end)
```

#### Split into second section
Above, I established the first range of numbers that need to be processed, and now I need to establish the second. I can assume that the beginning of my next section is the end of section 1 + 1, since I already know that's the next_digit_boundary.

```
end = 1300
section_2_start = next_digit_boundary
section_2_end = end
process(section_2_start, section_2_end)
```
Since I plan for my processing method to exit early if the number has an odd number of digits then, by separting ranges into sections, I can make sure the whole original range is handled properly. For now, anyway, since I know my digit input will not stretch over several digit-length bounds.

### Summary of patterns / constraints:
1. An invalid number must be even
2. An invalid number is determined entirely by its first half, therefore invalid numbers can be represented by their first half
3. Range boundaries will determine which first halves are valid for generation
4. Ranges that cross digit-length boundaries need to be split