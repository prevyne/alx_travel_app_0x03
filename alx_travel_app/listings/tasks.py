from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking, Hotel, Payment

#1: SEND BOOKING CONFIRMATION

@shared_task
def send_booking_confirmation_email(booking_id):
    """
    Celery task to send a confirmation email to a user after a booking is made.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
        user = booking.user
        hotel = booking.hotel
        
        subject = f"Your Booking is Confirmed: {hotel.name}"
        message = f"""
        Hi {user.first_name or user.username},

        Thank you for your booking at {hotel.name}! We're excited to host you.

        Your booking details:
        - Check-in Date: {booking.check_in_date}
        - Check-out Date: {booking.check_out_date}
        - Number of Guests: {booking.num_guests}

        Best regards,
        The ALX Travel Team
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL or 'noreply@alxtravel.com',
            [user.email],
            fail_silently=False,
        )
        return f"Booking confirmation email sent successfully to {user.email}."

    except Booking.DoesNotExist:
        return f"Error: Booking with ID {booking_id} does not exist."
    except Exception as e:
        print(f"An unexpected error occurred for booking {booking_id}: {e}")
        return f"Failed to send booking confirmation for booking ID: {booking_id}."


#2: SEND PAYMENT CONFIRMATION

@shared_task
def send_payment_confirmation_email(payment_id):
    """
    Celery task to send a confirmation email after a payment is successful.
    """
    try:
        # Retrieve the Payment object from the database.
        payment = Payment.objects.get(id=payment_id)
        
        # Use the model relationship to get the User object.
        # This assumes your Payment model is linked to your Booking model.
        user = payment.booking.user

        # Create the email subject and message.
        subject = "Payment Confirmation - Thank You!"
        message = f"""
        Hi {user.first_name or user.username},

        This is a confirmation that your payment of ${payment.amount} has been received successfully.
        Your booking for {payment.booking.hotel.name} is now fully paid.

        Thank you for your business!

        Best regards,
        The ALX Travel Team
        """
        
        #Send the email.
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL or 'noreply@alxtravel.com',
            [user.email],
            fail_silently=False,
        )
        return f"Payment confirmation email sent successfully for payment ID: {payment_id}."

    except Payment.DoesNotExist:
        return f"Error: Payment with ID {payment_id} does not exist."
    except Exception as e:
        print(f"An unexpected error occurred for payment {payment_id}: {e}")
        return f"Failed to send payment confirmation for payment ID: {payment_id}."