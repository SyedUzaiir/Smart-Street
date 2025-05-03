from flask import Flask, send_from_directory, request, jsonify
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'home.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    message = request.form.get('message')
    location = request.form.get('location') or "Charminar, Hyderabad, India"  # Default location

    if not message:
        return jsonify({"error": "Message is required."}), 400

    # Email configuration
    sender_email = "dioxygencarbonate@gmail.com"  # Your email
    receiver_email = "sduzairmohiuddin@gmail.com"  # Recipient email
    subject = "New Complaint Submitted"
    body = f"Complaint: {message}\nLocation: {location}"

    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email using smtplib
    try:
        print(f"Preparing to send email to {receiver_email}...")  # Log email sending attempt
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, 'hzvt mpbb qtmp rfjo')  # Replace with your app password
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")  # Log successful email sending
        return jsonify({"message": "Complaint submitted successfully!"}), 200
    except Exception as e:
        print(f"Failed to send complaint: {str(e)}")  # Log the error
        print("Error occurred while sending email.")  # Additional error logging
        return jsonify({"error": "Failed to send complaint."}), 500

if __name__ == '__main__':
    app.run(debug=True)
