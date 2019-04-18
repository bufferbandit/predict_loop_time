from time import time,sleep

def predict_loop_time(counter,loop_max,start_time):
    try:
        current_time = time()
        elapsed_time = current_time - start_time
        time_left = loop_max * elapsed_time / counter - elapsed_time
        minst_left = float(str([int(time_left)/100 if int(time_left / 60) < 1 else (time_left)/60][0])[:4])
        return minst_left
    except ZeroDivisionError:
        return 99999999999


if __name__ == "__main__":
    max_loop = 60
    start_time = time()
    for x in range(max_loop):
        sleep(1)
        time_left = predict_loop_time(x,max_loop,start_time)
        print(time_left)
   
