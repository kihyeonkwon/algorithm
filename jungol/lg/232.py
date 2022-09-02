def odd_even(N):
    if N<1:
        return
    odd_even(N-2)
    print(N, end=' ')



odd_even(int(input()))