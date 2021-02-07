import random


if __name__ == '__main__':
    for i in range(100):
        with open(f'testdata/data{i}.dat', 'wb') as f:
            for j in range(10000):
                num = int(random.uniform(0, 1024))
                f.write(num.to_bytes(2, byteorder='little'))
