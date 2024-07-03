from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_receipt(filename, transaction_details):
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Title
        c.setFont("Helvetica-Bold", 24)
        c.drawString(200, 750, "Payment Receipt")

        # Transaction details
        c.setFont("Helvetica", 12)
        y_position = 700
        for key, value in transaction_details.items():
            c.drawString(100, y_position, f"{key}: {value}")
            y_position -= 20

        # Signature line
        c.line(100, 150, 300, 150)
        c.drawString(100, 135, "Signature")

        c.save()
        print(f"Receipt successfully created as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_transaction_details():
    transaction_id = input("Enter Transaction ID: ")
    date = input("Enter Date: ")
    amount = input("Enter Amount: ")
    payment_method = input("Cash/ Card/ UPI: ")
    customer_name = input("Enter Customer Name: ")
    customer_email = input("Enter Customer Email: ")

    return {
        "Transaction ID": transaction_id,
        "Date": date,
        "Amount": amount,
        "Payment Method": payment_method,
        "Customer Name": customer_name,
        "Customer Email": customer_email
    }


# Main code
transaction_details = get_transaction_details()
create_receipt("receipt2.pdf", transaction_details)
