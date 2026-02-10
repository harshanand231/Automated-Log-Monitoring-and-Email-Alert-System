import smtplib
from email.message import EmailMessage

log_file = "app_log.txt"
report_file = "error_report.txt"

errors = []

# Read log file
with open(log_file, "r") as file:
    lines = file.readlines()

for line in lines:
    if "ERROR" in line:
        errors.append(line)

# Write error report
with open(report_file, "w") as report:
    for error in errors:
        report.write(error)

print(f"Total errors found: {len(errors)}")

# Send email only if errors exist
if len(errors) > 0:

    EMAIL_ADDRESS = "*** your email@gmail.com"
    APP_PASSWORD = "zkyfkldtuutjiema"
    TO_EMAIL = "harshanand@gmail.com"   # you can send to yourself

    msg = EmailMessage()
    msg["Subject"] = "🚨 ALERT: Errors Found in System Logs"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    body = "Errors detected in system logs:\n\n"
    body += "".join(errors)

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)

    print("Email alert sent successfully!")

else:
    print("No errors found. No email sent.")
