import time
import sched

schedule = sched.scheduler(time.time, time.sleep)


def func():
    print("now is", time.time())


print(time.time())
schedule.enter(2, 0, func)
schedule.run()
print(time.time())