import os
import smtplib
from flask import Flask, request, jsonify, send_from_directory
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'login.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/test-complaint', methods=['POST'])
def test_complaint():

    # Log incoming request data
    print("Test complaint submitted.")

    
    # Get data from form or JSON request

    data = request.get_json() or request.form
    message = data.get("message")
    location = data.get("location", "Charminar, Hyderabad, India")  # Default location
    report = data.get("report")  # Get the report from the request

    if not message:
        print("❌ No message received in the request.")
        return jsonify({"error": "Message is required."}), 400

    # Email configuration
    sender_email = "disoxygencarbonate@gmail.com"  # Your email
    receiver_email = "sduzairmohiuddin@gmail.com"  # Recipient email
    email_password = os.getenv("EMAIL_PASSWORD")  # Secure way to store password

    # Create the email content
    subject = "New Complaint Submitted"
    body = f"Complaint: {message}\nLocation: {location}\nReport: {report}"  # Include report in the email body

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, email_password)  # Log in to the email account
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
        return jsonify({"message": "Your complaint has been submitted successfully!"}), 200  # Update success message

    except Exception as e:
        print(f"Failed to send complaint: {str(e)}")
        print("Error occurred while sending email.")  # Additional error logging
        return jsonify({"error": "Failed to send complaint."}), 500

if __name__ == "__main__":
    app.run(debug=True)
