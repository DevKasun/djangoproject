import requests

MAILGUN_API_KEY = ""
MAILGUN_API_URL = ""
FROM_EMAIL_ADDRESS = ""

def send_email(to_address: str, subject: str, message: str):
    resp = requests.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,
            "text": message
        }
    )
    
    if resp.status_code == 200:
        print("Email sent successfully!")
    else:
        print("Failed to send email. Status code: ", resp.status_code)
        

send_email("devkasunlakshitha@gmail.com", "Test Email", "This is a test email sent using Mailgun API")