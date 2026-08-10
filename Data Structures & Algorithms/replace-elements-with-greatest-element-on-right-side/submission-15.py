class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp_max = -1
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            for j in range (i+1, len(arr)):
                if temp_max < arr[j]:
                    temp_max = arr[j]
            arr[i] = temp_max
            temp_max = -1
        return arr