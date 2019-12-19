from FENCE.fence_chrisjune import counter

assert counter([7,1,5,9,6,7,3]) == 20
assert counter([1,4,4,4,4,1,1]) == 16
assert counter([1,8,2,2]) == 8
assert counter([2,2]) == 4
assert counter([1,3]) == 3
assert counter([1,4,1,5,4,4,4]) == 16