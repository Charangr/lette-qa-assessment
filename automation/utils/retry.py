import time

def retry(func, retries=3):
    # retry request if it fails
    for _ in range(retries):
        res = func()
        if res.status_code in [200, 201]:
            return res
        time.sleep(1)
    return res