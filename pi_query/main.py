from fastapi import FastAPI
from celery_worker import main_task
from model import Order

app = FastAPI()


@app.post('/order')
def add_order(order: Order):
    main_task.delay(order.precision)

    return {"message": "Order Received! Thank you for your patience."}
