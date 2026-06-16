def task2():
    N = int(input())
    arr = list(map(int, input().split()))
    
    result = [arr[-1]] + arr[:-1]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    task2()
