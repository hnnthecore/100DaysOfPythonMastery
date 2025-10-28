# Day 13 - Invoice Generator (Swiss Edition)
# Project: Generate professional invoices with Swiss VAT & CHF currency.

import datetime
import random

VAT_RATE = 0.077  # 7.7% Swiss VAT

def generate_invoice_number():
    """Generate a random invoice number."""
    return f"CH-{random.randint(1000, 9999)}"

def input_items():
    """Collects items from user input."""
    items = []
    print("Enter item details (type 'done' when finished):\n")
    while True:
        name = input("Item name: ").strip()
        if name.lower() == "done":
            break
        try:
            qty = int(input("Quantity: "))
            price = float(input("Price per unit (CHF): "))
            items.append({"name": name, "qty": qty, "price": price})
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.\n")
    return items

def calculate_total(items):
    """Calculate subtotal, VAT, and total."""
    subtotal = sum(item["qty"] * item["price"] for item in items)
    vat = subtotal * VAT_RATE
    total = subtotal + vat
    return subtotal, vat, total

def print_invoice(company_name, customer_name, items, subtotal, vat, total, invoice_number):
    """Print a formatted Swiss-style invoice."""
    print("\n" + "=" * 55)
    print(f"{company_name:^55}")
    print("=" * 55)
    print(f"Zürich Invoice No: {invoice_number}")
    print(f"Customer: {customer_name}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)
    print(f"{'Item':<25}{'Qty':<10}{'Price (CHF)':<12}{'Total (CHF)'}")
    print("-" * 55)

    for item in items:
        total_price = item["qty"] * item["price"]
        print(f"{item['name']:<25}{item['qty']:<10}{item['price']:<12.2f}{total_price:.2f}")

    print("-" * 55)
    print(f"{'Subtotal':<40}CHF {subtotal:.2f}")
    print(f"{'VAT (7.7%)':<40}CHF {vat:.2f}")
    print(f"{'Grand Total':<40}CHF {total:.2f}")
    print("=" * 55)
    print("Vielen Dank für Ihren Einkauf! 🇨🇭\n")

def save_invoice(company_name, customer_name, items, subtotal, vat, total, invoice_number):
    """Save the invoice as a text file."""
    filename = f"invoice_{invoice_number}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{company_name}\n")
        f.write("=" * 55 + "\n")
        f.write(f"Zürich Invoice No: {invoice_number}\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'Item':<25}{'Qty':<10}{'Price (CHF)':<12}{'Total (CHF)'}\n")
        f.write("-" * 55 + "\n")
        for item in items:
            total_price = item["qty"] * item["price"]
            f.write(f"{item['name']:<25}{item['qty']:<10}{item['price']:<12.2f}{total_price:.2f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'Subtotal':<40}CHF {subtotal:.2f}\n")
        f.write(f"{'VAT (7.7%)':<40}CHF {vat:.2f}\n")
        f.write(f"{'Grand Total':<40}CHF {total:.2f}\n")
        f.write("=" * 55 + "\n")
        f.write("Vielen Dank für Ihren Einkauf! 🇨🇭\n")

    print(f"📄 Invoice saved successfully as {filename}")

def main():
    print("=" * 55)
    print("💼 SWISS INVOICE GENERATOR 💼")
    print("=" * 55)

    company_name = input("Enter your company name: ") or "Helvetic Python GmbH"
    customer_name = input("Enter customer name: ") or "Guest"
    invoice_number = generate_invoice_number()

    items = input_items()
    if not items:
        print("No items entered. Exiting.")
        return

    subtotal, vat, total = calculate_total(items)
    print_invoice(company_name, customer_name, items, subtotal, vat, total, invoice_number)

    save_choice = input("Would you like to save this invoice as a text file? (y/n): ").lower()
    if save_choice == "y":
        save_invoice(company_name, customer_name, items, subtotal, vat, total, invoice_number)

    print("\n✅ Swiss Invoice Generation Complete!\n")

if __name__ == "__main__":
    main()
