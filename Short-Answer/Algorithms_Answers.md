#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)this is an O(1) because after the calculations are done a is always going to be greater than n^3 meaning the while loop would have only been executed once.

b)this one is O(n^2) because there are nested for loops. and a for loop is O(n) or linear because the bigger n is the more loops it has to go through. and because there is a nested for loop it becomes O(n^2)

c)This is O(n). this is because the amount of times the recursion gets called is dependant on the amount of bunnies there are. so the more bunnies there are the more times the function will be called and the longer it will take

## Exercise II

if the amount of floors is unorganized i would sort that first to resemble the actual building. i would use the middle of the building as the starting point and drop the egg. if it breaks, we know we have to go lower so we halve the list again and test until the egg doesnt break and we can find our safe for throwing floor and return that. This was actually a project i had to do in middle school.

Since this is technically a binary search because we are cutting the number of floors in half, the runtime of this algorithm is O(log N).
