#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    '''Prime Game'''
    if x > len(nums):
        x == len(nums)
    e_cache_primes = {}
    wins = {"Maria": 0, "Ben": 0}
    for i in range(x):
        single_wins = {"Maria": 0, "Ben": 0}
        query_num = nums[i]
        if query_num in e_cache_primes:
            primes = e_cache_primes[query_num]
        else:
            primes = []
            if query_num > 1:
                for j in range(2, query_num + 1):
                    for z in range(2, j + 1):
                        if j % z == 0 and j != z:
                            break
                        if z >= (j / 2):
                            primes.append(j)
                            break
            e_cache_primes[query_num] = primes
        print(primes)
        if len(primes) == 0:
            wins['Ben'] += 1
            continue
        turn = 'Maria'
        v = 0
        num_set = [x for x in range(2, query_num + 1)]
        for k in range(len(primes)):
            if k != 0:
                if turn == 'Maria':
                    turn = 'Ben'
                else:
                    turn = 'Maria'
            k += 1
            chosen_num = primes[0]
            primes.remove(chosen_num)
            for num in num_set:
                if num % chosen_num == 0:
                    num_set.remove(num)
            single_wins[turn] += 1
            if len(num_set) == 0:
                single_wins[turn] += 1
                break
        if single_wins['Maria'] == single_wins['Ben']:
            continue
        winner = 'Maria' if single_wins['Maria'] >\
            single_wins['Ben'] else 'Ben'
        wins[winner] += 1
    if wins['Maria'] == wins['Ben']:
        return None
    return 'Maria' if wins['Maria'] > wins['Ben'] else 'Ben'
