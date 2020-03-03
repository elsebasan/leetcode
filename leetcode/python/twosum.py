

def twoSum(nums, target: int):
    middle = target// 2
    hash_size = middle + 1
    hash_array = [None] * hash_size
    i = 0
    for elem in nums:
        if elem <= middle:
            print("directo")
        #Direct
            if hash_array[elem] == None:
                hash_array[elem] = i
                print("elem")
                print(elem)
                print("i")
                print(i)
            else:
                print("elem")
                print(elem)
                print("i")
                print(i)
                return ([hash_array[elem], i])
        elif elem < target:
        #complement
            print("complemento")
            if hash_array[target - elem] == None:
                hash_array[target - elem] = i
                print("elem")
                print(elem)
                print("i")
                print(i)
            else:
                print("elem")
                print(elem)
                print("i")
                print(i)
                return ([hash_array[target - elem], i])
        i = i + 1


def main():
#    nums = [2,7,11,15]
    nums = [0,4,3,0]
    target = 0
    salida = twoSum(nums,target)
    print(salida) 
   
  
if __name__ == "__main__":
  main()

    
