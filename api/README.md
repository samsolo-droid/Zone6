## PIZZA DELIVERY API

This is a REST API for a Pizza delivery service built for fun and learning with FastAPI, SQLAlchemy and PostgreSQL. The video playlist is
[here](https://www.youtube.com/playlist?list=PLEt8Tae2spYnLMAf8RGCNYhovIFZHVsPP)

## ROUTES TO IMPLEMENT

| METHOD   | ROUTE                              | FUNCTIONALITY               | ACCESS      |
| -------- | ---------------------------------- | --------------------------- | ----------- |
| _POST_   | `/auth/signup/`                    | _Register new user_         | _All users_ |
| _POST_   | `/auth/login/`                     | _Login user_                | _All users_ |
| _POST_   | `/orders/order/`                   | _Place an order_            | _All users_ |
| _PUT_    | `/orders/order/update/{order_id}/` | _Update an order_           | _All users_ |
| _PUT_    | `/orders/order/status/{order_id}/` | _Update order status_       | _Superuser_ |
| _DELETE_ | `/orders/order/delete/{order_id}/` | _Delete/Remove an order_    | _All users_ |
| _GET_    | `/orders/user/orders/`             | _Get user's orders_         | _All users_ |
| _GET_    | `/orders/orders/`                  | _List all orders made_      | _Superuser_ |
| _GET_    | `/orders/orders/{order_id}/`       | _Retrieve an order_         | _Superuser_ |
| _GET_    | `/orders/user/order/{order_id}/`   | _Get user's specific order_ |
| _GET_    | `/docs/`                           | _View API documentation_    | _All users_ |

## How to run the Project

- Install Postgreql
- Install Python
- Git clone the project with ` git clone https://github.com/jod35/Pizza-Delivery-API.git`
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Set Up your PostgreSQL database and set its URI in your `database.py`

```
engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>',
    echo=True
)
```

- Create your database by running `python init_db.py`
- Finally run the API
  ``uvicorn main:app`
