total = 0.0
with open('Data/portfolio.csv', 'r') as f:
    headers = next(f)   # Skip a single of input
    for line in f:
        line = line.strip()     # Strip whitespace
        parts = line.split(',')
        parts[0] = parts[0].strip ('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2] * parts[3]

print('Total cost:', total)