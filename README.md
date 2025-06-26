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

🎯 Project Objective
To design a system that:

Registers students with age and roll number validation

Stores exam metadata like subject, date, and total marks

Evaluates quiz performance against valid constraints

Raises clear and meaningful errors using custom exceptions

🔧 Features
👦 Student Registration
Ensures age is numeric and at least 10 years

Prevents duplicate roll numbers across students

Validates roll number uniqueness using a class-level registry

🧾 Exam Creation
Accepts subject name, exam date, and total marks

Validates that maximum marks are non-negative integers




Quiz mini project


📊 Quiz Evaluation
Accepts student and exam as inputs

Validates scored marks within allowed limits

Calculates and prints percentage

Passes students scoring 40% or more

⚠️ Custom Exceptions Used
Exception Name	Trigger Condition
UnderageStudentError	If student's age is below 10
DuplicateRollError	If roll number is already registered
InvalidMarksError	If quiz marks are out of valid range (negative or too high)
InvalidExamDataError	If maximum exam marks are negative or not integer

🧠 Learning Outcomes
Use of exception classes to model real-world validation problems

Proper object-oriented design, including encapsulation and class-level data

Realistic simulation of a student evaluation workflow

Understanding of constructor-level validation

🚀 Code Flow (Non-Technical)
Student Creation
The system checks:

Age must be numeric and ≥ 10

Roll number must not already exist

Exam Creation
Exam is initialized with:

Subject name

Exam date (treated as a string here)

Maximum allowed marks

Quiz Submission

The student’s score is validated against the exam’s max marks

A result (Pass/Fail) is printed based on a 40% threshold

Errors
If anything goes wrong during student registration, exam setup, or quiz scoring, appropriate custom errors are raised and shown.

✅ Example Output
cpp
Copy
Edit
Pass::Sandeep score 80.0
Exam over
Or, if an error:

pgsql
Copy
Edit
Roll no already exists
Exam over
📦 Future Enhancements (Suggestions)
Add subject-wise history or transcript tracking

Use datetime module to validate exam dates

Store results in CSV or JSON format
