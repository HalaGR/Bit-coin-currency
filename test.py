import time
start_time = time.time()
if __name__ == "__main__":
    i = (time.time() - start_time)
    print(i)
    if (time.time() - start_time) > 1:
        print("true")