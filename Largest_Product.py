def find_Largest_Product(digits):
    maxVal = 0
    range_val = 13
    zero_idx = list()
    nums = [int(val) for val in ''.join(digits.split())]
    for idx, val in enumerate(nums):
        if not val:
            zero_idx.append(idx)
    
    for i in range(len(zero_idx)-1):
        if zero_idx[i+1] - zero_idx[i] > range_val:
            start = zero_idx[i] + 1 
            end = zero_idx[i+1]
            count = 0 
            multiplication = 1 
            
            for idx in range(start, end):
                count += 1
                multiplication *= nums[idx]
                
                if count == range_val:
                    maxVal = max(maxVal,multiplication)
                elif count > range_val:
                    multiplication //= nums[idx-range_val]
                    maxVal = max(maxVal,multiplication)

    return maxVal
 
 
def main():
    digits = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""   
    
    print(find_Largest_Product(digits))
    
if __name__ == "__main__":
    try:
        main()
    except:
        print("Keyboard interruption detected, quitting")
    
            


























