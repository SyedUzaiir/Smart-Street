import smtplib
from email.mime.text import MIMEText

# Email configuration
sender_email = "disoxygencarbonate@gmail.com"  # Your email
receiver_email = "sduzairmohiuddin@gmail.com"  # Recipient email
password = "ncoy dksa dtzx yvoi"  # Replace with your app password

# Create the email content
msg = MIMEText("Hi")
msg['Subject'] = "Test Email"
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)  # Log in to the email account
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
    print("Test email sent successfully!")  # Log successful email sending
except Exception as e:
    print(f"Failed to send email: {str(e)}")  # Log the error
