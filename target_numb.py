def prime_gen(i=0):
    if i == 0:
        return [2]
    else:
        primes_ = prime_gen(i - 1)
        last_prime = primes_[-1]
        next_prime = last_prime + 1
        bool_list = [(bool(next_prime % prime)) for prime in primes_]

        print(f'i : {i}')
        print(f'  last_prime : {last_prime}')
        print(f'  primes_ : {primes_}')
        print(f'  bool_list : {bool_list}')

        count = 0
        while (not all(bool_list)) and count < 10:
            next_prime += 1
            bool_list = [(bool(next_prime % prime)) for prime in primes_]
            print(f'  bool_list : {bool_list}')

            count += 1
        primes_.append(next_prime)
        return primes_


def solution(numbers):
    answer = 0
    return answer


print(prime_gen(3))