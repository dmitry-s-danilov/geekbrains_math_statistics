def statistics(x: list) -> dict:
    n = len(x)

    # expected value
    Ex = sum(x) / n

    # biased

    # variance
    Dx = sum([(_ - Ex) ** 2 for _ in x]) / n
    # standard deviation
    Sx = Dx ** .5

    # unbiased

    # variance
    D0x = n / (n - 1) * Dx
    # standard deviation
    S0x = D0x ** .5

    return {
        'mean': Ex,
        'var': Dx,
        'std': Sx,
        'var_unbiased': D0x,
        'std_unbiased': S0x
    }
