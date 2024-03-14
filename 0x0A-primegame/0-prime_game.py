#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    '''Prime Game'''
    if x is None or nums is None or x == 0 or nums == []:
        return None
    e_cache_primes = {}
    wins = {"Maria": 0, "Ben": 0}
    for i in range(x):
        single_wins = {"Maria": 0, "Ben": 0}
        query_num = nums[i]
        if query_num in e_cache_primes:
            primes = e_cache_primes[query_num]
        else:
            primes = [x for x in range(2, query_num + 1)]
            for number in primes:
                for x in primes:
                    if x % number == 0 and x >= (number * number):
                        primes.remove(x)
            e_cache_primes[query_num] = primes
        if len(primes) == 0:
            wins['Ben'] += 1
            continue
        turn = 'Maria'
        num_set = [x for x in range(2, query_num + 1)]
        for k in range(len(primes)):
            if k != 0:
                if turn == 'Maria':
                    turn = 'Ben'
                else:
                    turn = 'Maria'
            chosen_num = primes[0]
            primes.remove(chosen_num)
            for num in num_set:
                if num % chosen_num == 0:
                    num_set.remove(num)
            single_wins[turn] += 1
            if len(num_set) == 0 or len(primes) == 0:
                single_wins[turn] += 1
                break
        if single_wins['Maria'] == single_wins['Ben']:
            continue
        winner = 'Maria' if single_wins['Maria'] >\
            single_wins['Ben'] else 'Ben'
        wins[winner] += 1
        if i + 1 < x - 1 and i + 1 > len(nums):
            wins[winner] += 1
            break
    if wins['Maria'] == wins['Ben']:
        return None
    return 'Maria' if wins['Maria'] > wins['Ben'] else 'Ben'
