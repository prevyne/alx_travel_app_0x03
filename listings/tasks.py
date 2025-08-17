from celery import shared_task
from django.core.mail import send_mail
from .models import Payment

@shared_task
def send_payment_confirmation_email(payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        booking = payment.booking

        subject = 'Your Booking is Confirmed!'
        message = f"""
        Dear {booking.customer_name},

        Thank you for your payment! Your booking is confirmed.

        Booking ID: {booking.id}
        Amount Paid: {payment.amount} ETB
        Transaction Reference: {payment.tx_ref}

        We look forward to serving you.

        Best regards,
        ALX Travel App
        """
        from_email = 'noreply@alxtravel.com'
        recipient_list = [booking.customer_email]

        send_mail(subject, message, from_email, recipient_list)
        return f"Confirmation email sent for payment {payment_id}"
    except Payment.DoesNotExist:
        return f"Payment with ID {payment_id} not found."