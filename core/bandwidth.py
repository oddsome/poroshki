import time

def run_limited(cmd, freq = 3):

    delay = 1.0 / freq

    t_start = time.time()
    result = cmd()
    t_elapsed = time.time() - t_start

    if delay > t_elapsed:
        time.sleep(delay - t_elapsed)

    return result
