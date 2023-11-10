import time
from src.save_data import save_to_es

if __name__ == '__main__':
    start = time.time()
    save_to_es()
    end = time.time()
