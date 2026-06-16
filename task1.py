def task1():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    reversed_arr = arr[::-1]
    print(' '.join(map(str, reversed_arr)))

if __name__ == "__main__":
    task1()
