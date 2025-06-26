
class InvalidCardError(Exception):
    def __init__(self,message='Invalid Card detected'):
        self.message=message
    def __str__(self):
        return self.message
class InsufficientBalanceError(Exception):
    def __init__(self,message='Insufficient balance detected'):
        self.message=message
    def __str__(self):
        return self.message
class InvalidUPIError(Exception):
    def __init__(self,message='Invalid UPI detected'):
        self.message=message
    def __str__(self):
        return self.message
class PaymentValidationError(Exception):
    def __init__(self,message='Payment validation failure'):
        self.message=message
    def __str__(self):
        return self.message
class AuthenticationError(Exception):
    def __init__(self,message='Authentication error'):
        self.message=message
    def __str__(self):
        return self.message
class InvalidEmailError(Exception):
    def __init__(self,message='Invalid email'):
        self.message=message
    def __str__(self):
        return self.message
class PaymentModeError(Exception):
    def __init__(self,message='Payment mode error occur'):
        self.message=message
    def __str__(self):
        return self.message


from abc import *

class PaymentMethod(ABC):
    @abstractmethod
    def validate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self,card_nmber=None,cvv=None,balance=0):
        if not card_nmber or not cvv or not balance:
            raise TypeError('Provide (card number,cvv,balance)')
        else:
            self.card_number=card_nmber
            self.cvv=cvv
            self.balance=balance
            self.validate()
    
    def validate(self):
        if len(self.card_number)!=16:
            raise InvalidCardError('U have entered invalid card no')
        if len(self.cvv)!=3:
            raise InvalidCardError('U have entered Wrong CVV')
        if self.balance <0 or isinstance(self.balance,int)==False:
            raise ValueError('Balance would be in +ve and integer value')
    
    def AuthenticateCardDetail(self,card_number,cvv):
        if card_number!=self.card_number or cvv!=self.cvv:
            raise AuthenticationError('Card_no or cvv does not match')
        else:
            print('Card detail has matched')
            return True

    def pay(self,card_number=None,cvv=None,amount=None):
        if not card_number or not cvv or not amount:
            raise TypeError('U have not entered detaill for Credit card detail')
        if type(amount)!=int:
            raise ValueError('Payment amount would be in intger')
        if amount<0 or amount>self.balance:
            raise InsufficientBalanceError('Entered amount is insufficient')
        else:
            print('Validating--- stay tunesss')
            if self.AuthenticateCardDetail(card_number,cvv):
                print('Validation successful')
                self.balance-=amount
                print(f'{amount} deducted successfully')
                print(f'Total balance: {self.balance}')

class UPIPayment(PaymentMethod):
    def __init__(self,upi_id=None,pin=None,balance=0):
        self.upi_id=upi_id
        self.pin=pin
        self.balance=balance
        self.validate()
    
    def validate(self):
        if '@' not in self.upi_id:
            raise InvalidUPIError('u have entered invalid UPI id')
        if len(self.pin)!=4:
            raise InvalidUPIError('U have entered invalid PIN')
        if self.balance <0:
            raise InvalidUPIError('Balance would be in positive')
    
    def Authenticate_UPI(self,upi_id,pin):
        if upi_id!=self.upi_id or pin!=self.pin:
            raise AuthenticationError('U have entered unmatched UPI detail')
        else:
            return True
    def pay(self,upi_id=None,pin=None,amount=None):
        if not upi_id or not pin or not amount:
            raise TypeError('U have not entered detaill for UPI peyment')
        if amount>self.balance:
            raise InsufficientBalanceError('Insufficient balance in ur account')
        if amount <0:
            raise InsufficientBalanceError('payment would not be in negativee')
        else:
            print('validation is in progress.....')
            if self.Authenticate_UPI(upi_id,pin):
                print('Validation successful')
                self.balance-=amount
                print(f'{amount} deducted successfully')
                print(f'Total balance: {self.balance}')

class PayPalPayment(PaymentMethod):
    def __init__(self,email=0,password=0,balance=0):
        self.email=email
        self.password=password
        self.balance=balance
        self.validate()
    def validate(self):
        if '@' not in self.email:
            raise InvalidEmailError('u have entered invalid PayPal id')
        if len(self.password)<6:
            raise AuthenticationError('U have entered sort PIN')
    
    def authenticate_paypal(self,email,password):
        if email!=self.email or password!=self.password:
            raise AuthenticationError('U have entered wrong papal detail')
        else:
            return True
        
    def pay(self,email=None,password=None,amount=0):
        if not email or not password or not amount:
            raise TypeError('U have not entered detaill for paypalaccount')
        if type(amount)!=int:
            raise ValueError('Invalid type amount fatched ')
        if amount>self.balance:
            raise InsufficientBalanceError('Insufficient balance in ur account')
        if amount <0:
            raise InsufficientBalanceError('payment would not be in negativee')
        else:
            print('validation is in progress.....')
            if self.authenticate_paypal(email,password):
                print('Validation successful')
                self.balance-=amount
                print(f'{amount} deducted successfully')
                print(f'Total balance: {self.balance}')


class UserWallet:
    def __init__(self,name='User'):
        self.name=name
        self.mode_record={}
        self.active_mode=None
        print(f'Welcome {self.name}')
    def add_payment_method(self,mode_name=None,payment_obj=None):
        if not mode_name or not payment_obj:
            raise TypeError('u have missed to provide mode name or obj')
        if not payment_obj:
            raise AuthenticationError('please Provide method detail')
        else:
            if isinstance(mode_name,str)==False:
                raise ValueError('mode_name would be in string')
            else:
                if mode_name in self.mode_record:
                    raise PaymentModeError('Mode name is already present')
                else:
                    self.mode_record[mode_name]=payment_obj
                    print(f'Detail added {self.mode_record}')

    def switch_payment_mode(self,mode_name):
        if not mode_name:
            raise PaymentModeError('choose payment mode')
        else:
            if mode_name not in self.mode_record.keys():
                raise PaymentModeError('Payment Mode is not found in your wallet')
            else:
                self.active_mode=mode_name
    
    def make_payment(self):
        if not self.active_mode:
            raise PaymentValidationError('Payment mode not selected')
        else:
            # ''' this is for credit card payment-------'''
            if self.mode_record[self.active_mode].__class__.__name__=='CreditCardPayment':
                print('Enter Card details-----------  ')
                card_number=input('Enter card number: ')
                cvv=input('Enter cvv: ')
                amount=input('Enter amount: ')
                if amount.isdigit()==False:
                    raise TypeError('amount would be numeric')
                else:
                    amount=int(amount)
                self.mode_record[self.active_mode].pay(card_number,cvv,amount)
                # ''' this is for UPI Payment payment-------'''
            elif self.mode_record[self.active_mode].__class__.__name__=='UPIPayment':
                print('Enter UPI details----------')
                upi_id=input('Upi_ID:')
                pin=input('Pin: ')
                amount=input('Enter amount: ')
                if amount.isdigit()==False:
                    raise TypeError('amount would be numeric')
                else:
                    amount=int(amount)
                self.mode_record[self.active_mode].pay(upi_id,pin,amount)
            # ''' this is for PayPalPayment payment-------'''
            elif self.mode_record[self.active_mode].__class__.__name__=='PayPalPayment':
                print('Enter PayPal Details----------')
                email=input('Enter Email: ')
                password=input('Enter Password: ')
                amount=input('Enter amount: ')
                if amount.isdigit()==False:
                    raise TypeError('amount would be numeric')
                else:
                    amount=int(amount)
                    self.mode_record[self.active_mode].pay(email,password,amount)

try:
    ppl=PayPalPayment('sandy@paypal.com','234523',6000)
    upi=UPIPayment('chatgtp@ai','2407',111)
    myWallet=UserWallet('Sandeep')
    myWallet.add_payment_method('ppl',ppl)
    myWallet.add_payment_method('Upi',upi)
    # myWallet.switch_payment_mode('ppl')
    # myWallet.make_payment()
    myWallet.switch_payment_mode('Upi')
    myWallet.make_payment()
except ValueError as e:
    print(e)
except InvalidEmailError as e:
    print(e)
except AuthenticationError as e:
    print(e)
except PaymentValidationError as e:
    print(e)
except InvalidUPIError as e:
    print(e)
except InsufficientBalanceError as e:
    print(e)
except TypeError as e:
    print(e)
except PaymentModeError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('Transection complete')

  