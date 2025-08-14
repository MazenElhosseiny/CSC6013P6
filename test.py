import random

def findKthSmallest(nums, k):
    k = k-1

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quickSelect(1, p-1)
        elif p < k:
            return quickSelect(p+1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)

def main():
    randomList = []
    for i in range(1000):
        randomList.append(random.randint(0,1000))

    print(randomList)
    while True:
        choice = input("Enter an integer value for the kth Smallest element to find in an unsorted array: ")
        if not choice:
            print("No input received.")
        else:
            try:
                choice_int = int(choice)
                if 1 <= choice_int:
                    break
                else:
                    print("Please enter a value greater than or equal to 1.")
            except ValueError:
                print("Please enter an integer value.")
    
    
    print(f"The {choice}th smallest element in the array is:", findKthSmallest(randomList, choice_int))
    randomList.sort()
    print(randomList)
main()
