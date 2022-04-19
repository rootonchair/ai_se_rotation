from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from mpmath import mp

celery = Celery("tasks", broker='amqp://guest:guest@127.0.0.1:5672//')

celery_logger = get_task_logger(__name__)


def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield str(n)
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


@celery.task
def main_task(n_prescision):
    celery_logger.info("Order Complete")

    pi_generator = calcPi(n_prescision)

    pi_number = "".join(i for i in pi_generator)

    return pi_number

