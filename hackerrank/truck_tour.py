def truckTour(petrolpumps):
    diffs = [gas - dist for gas, dist in petrolpumps]
    total_gas = 0
    start_idx = 0
    for idx, diff in enumerate(diffs):
        total_gas += diff
        if total_gas < 0:
            total_gas = 0
            start_idx = idx + 1
    return start_idx