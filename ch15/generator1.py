import time
def longtile_job():
    print("job start")

    time.sleep(1)
    return "done"

longtile_job()

print("---------------------------")
list_job = [longtile_job() for i in range(5)]
print(list_job[0])