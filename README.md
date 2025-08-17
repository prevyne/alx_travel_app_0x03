# ALX Travel App 0x02 - Chapa Payment Integration

This project integrates the Chapa payment gateway into a Django-based travel booking application. It provides a complete workflow for initiating payments, verifying transactions, and sending automated email confirmations.

## Features

- Secure payment processing via Chapa API.
- Database models for tracking payment transactions.
- API endpoints for payment initiation and verification.
- Asynchronous email notifications for successful payments using Celery.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/alx_travel_app_0x02.git](https://github.com/your-username/alx_travel_app_0x02.git)
    cd alx_travel_app_0x02
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your Chapa API key:
    ```ini
    CHAPA_SECRET_KEY="YOUR_CHAPA_SECRET_KEY"
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server and Celery worker:**
    ```bash
    # In one terminal
    python manage.py runserver

    # In another terminal (ensure Redis is running)
    celery -A alx_travel_app worker -l info
    ```

## API Endpoints

### 1. Initiate Payment

-   **URL:** `/api/initiate-payment/`
-   **Method:** `POST`
-   **Body:** `{ "booking_id": <your_booking_id> }`
-   **Success Response:** Returns a Chapa checkout URL.
    ```json
    {
        "message": "Hosted Link",
        "status": "success",
        "data": {
            "checkout_url": "[https://checkout.chapa.co/checkout/payment/](https://checkout.chapa.co/checkout/payment/)..."
        }
    }
    ```

### 2. Verify Payment (Callback)

-   **URL:** `/api/verify-payment/<tx_ref>/`
-   **Method:** `GET`
-   **Description:** This URL is used by Chapa as a callback to verify the transaction status. Upon successful verification, the payment status is updated in the database and a confirmation email is sent.