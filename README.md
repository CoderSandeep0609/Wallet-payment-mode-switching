# Wallet-payment-mode-switching

 Multi-Method Payment Wallet System
A Python mini-project that simulates a real-world digital wallet system supporting multiple payment methods, such as:

🏦 Credit Card

📲 UPI (Unified Payments Interface)

📧 PayPal

The system enables:

Adding and switching between payment methods

Authenticating payment credentials

Performing secure payments with balance tracking

Enforcing validation through custom exceptions

Built using Object-Oriented Programming (OOP), Abstract Base Classes (ABC), and robust Exception Handling

🚀 Features
🔐 Secure Validation
Every payment method validates details like card number, UPI ID, password, CVV, etc.

🔄 Switchable Payment Modes
Users can add multiple payment methods to a wallet and switch between them dynamically.

🧠 Abstract Base Class Enforcement
Uses abc module to define a common interface (PaymentMethod) for all payment types.

⚠️ Custom Exception Handling
Project defines and raises meaningful exceptions like:

InvalidCardError

InvalidUPIError

AuthenticationError

PaymentModeError

InsufficientBalanceError

🏷️ UserWallet Class
Central controller that:

Stores payment modes

Validates mode existence

Manages balance

Routes to appropriate payment method

🔧 Technologies Used
Python 3.x

Object-Oriented Programming (OOP)

Abstract Base Classes (abc module)

Custom Exceptions

🛠️ How It Works
Create Payment Method Objects
Define user accounts with different payment types and starting balances.

Add to Wallet
Use add_payment_method() to add these methods to a UserWallet.

Switch Payment Mode
Call switch_payment_mode() to choose which method is active.

Make Payment
Provide credentials and amount — the system verifies, deducts, and shows the updated balance.

🧪 Example Use
python
Copy
Edit
my_wallet = UserWallet('Sandeep')
ppl = PayPalPayment('sandy@paypal.com', '123456', 5000)
upi = UPIPayment('sandeep@upi', '4321', 2000)

my_wallet.add_payment_method('paypal', ppl)
my_wallet.add_payment_method('upi', upi)

my_wallet.switch_payment_mode('upi')
my_wallet.make_payment()  # prompts for UPI ID, PIN, amount
 Learning Outcomes
Interface design using ABC

Practical usage of custom exceptions

Real-world wallet logic with mode switching

Strong OOP architecture with encapsulation and modularity

Error-proof user interactions

🧠 Future Improvements (Optional Ideas)
Transaction history log

File/database storage

OTP/email simulation

