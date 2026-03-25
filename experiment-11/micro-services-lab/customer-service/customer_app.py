from flask import Flask, jsonify
import requests

app = Flask(__name__)

customers = {
    101: {"id": 101, "name": "Customer-1", "email": "customer-1@example.com"},
    102: {"id": 102, "name": "Customer-2", "email": "customer-2@example.com"}
}

@app.route("/")
def home():
    return jsonify({"message": "Customer Service is running"})

@app.route("/customers/<int:user_id>/orders")
def get_account_details(user_id):
    customer = customers.get(user_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    # Call Order Service
    try:
        response = requests.get(
            f"http://localhost:5002/orders/user/{user_id}",
            timeout=3
        )

        if response.status_code == 200:
            orders = response.json()
        else:
            orders = []
    except requests.exceptions.RequestException:
        orders = {"error": "Order service unavailable"}
        
    return jsonify({
        "customer": customer,
        "orders": orders
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
