def fibonaci_prime_generator(limit=None):
    """
    Genrator liczb fibonacciego, które sa liczbami pierwszymi.


    :param limit: Opcjonalny limit ilości generowanych liczb.
    :type limit: int or None
    :yield: Kolejna liczba Fibonaciego będąca liczbą pierwszą
    : rtype: int
    :return:
    """

    a, b = 0, 1
    count = 0

    def is_prime(n):

        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        a, b = b, a + b  #
        if is_prime(a):
            yield a  # zwróc liczbę, jesli jest liczbą pierwszą
            count += 1
            if limit is not None and count >= limit:
                break
