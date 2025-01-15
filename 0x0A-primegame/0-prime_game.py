#!/usr/bin/python3

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_game(n):
    """Simulate a single round of the prime game."""
    nums = list(range(1, n + 1))
    primes = [p for p in nums if is_prime(p)]
    
    turn = 0  # 0 for Maria, 1 for Ben
    while primes:
        # Pick the smallest prime and remove all its multiples
        prime = primes[0]
        nums = [x for x in nums if x % prime != 0]
        primes = [p for p in nums if is_prime(p)]
        
        # Switch turns
        turn = 1 - turn
    
    # If turn is 0, Maria wins (because it was Ben's turn and couldn't play)
    return 'Maria' if turn == 1 else 'Ben'

def isWinner(x, nums):
    """Determine who won the most rounds."""
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
