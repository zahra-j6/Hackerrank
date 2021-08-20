#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr=sorted(arr)
    #print(len(arr))
    print(arr[len(arr)-2])
