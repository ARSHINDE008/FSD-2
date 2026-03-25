# Experiment 11: Microservice-based backend module

This repository contains two microservices: **Customer Service** and **Order Service**.

## Project Structure

```
micro-services-lab/
├── customer-service/
│   ├── customer_app.py
│   └── requirements.txt
└── order_service/
    ├── order_app.py
    └── requirements.txt
```

## Running the Services Locally

1. **Start Order Service (runs on port 5002):**
   ```bash
   cd order_service
   pip install -r requirements.txt
   python order_app.py
   ```

2. **Start Customer Service (runs on port 5001):**
   ```bash
   cd customer-service
   pip install -r requirements.txt
   python customer_app.py
   ```

## API Endpoints

### Order Service (`http://localhost:5002`)
- `GET /orders/user/<user_id>`: Fetches all orders for a specific user ID.
- `PUT /orders/<order_id>/status`: Updates the status of an order.
  - **Body (JSON):** `{"order_status": "New Status"}`

### Customer Service (`http://localhost:5001`)
- `GET /customers/<user_id>/orders`: Fetches customer details along with their orders (communicates with Order Service).

## Testing with POSTMAN
1. **GET Customer Orders:** Send a `GET` request to `http://localhost:5001/customers/101/orders`
2. **Update Order Status:** Send a `PUT` request to `http://localhost:5002/orders/1/status` with JSON body `{"order_status": "Delivered"}`.

## Deployment (Render)
To deploy these to Render:
1. Create a GitHub repository and push this code.
2. In Render, create two separate "Web Services".
3. Point both Web Services to the same GitHub repository, but set different **Root Directories**:
   - For Customer Service: Root Directory `customer-service`, Command `gunicorn customer_app:app`
   - For Order Service: Root Directory `order_service`, Command `gunicorn order_app:app`
4. Update the `Customer Service` code (in Render Environment Variables or by editing the file before pushing) to point to the deployed Order Service URL instead of `localhost:5002`.
