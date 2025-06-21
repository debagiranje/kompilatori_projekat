class Person
    attr_reader :name
  
    def initialize(name)
      @name = name
    end
  
    def display
      puts "Name: #{@name}"
    end
  end
  
  class Customer < Person
    attr_reader :accounts
  
    def initialize(name)
      super(name)
      accounts = []
    end
  
    def open_account(account)
      account.set_owner(self)
    end
  
    def total_balance
      sum = 0
      for acc in accounts
        sum += acc.balance
      end
    end
  
    def display_accounts
      puts "#{@name}'s accounts"
    end
  end
  
  class Employee < Person
    def perform_duty
      puts "#{@name} is performing their duty."
    end
  end
  
  class Manager < Employee
    def approve_loan(amount)
      if amount <= 10000
        puts "#{@name} approved the loan of #{amount}"
      elsif amount <= 50000
        puts "#{@name} forwarded the loan of #{amount} to senior management"
      else
        puts "Loan too large to approve!"
      end
    end
  end
  
  class BankAccount
    attr_reader :balance, :account_number
  
    @counter = 1000
  
    def initialize
      @account_number = generate_account_number
      @balance = 0.0
      @owner = nil
    end
  
    def deposit(amount)
      if amount > 0
        @balance += amount
      end
    end
  
    def withdraw(amount)
      if amount <= 0
        @balance -= amount
      else
        puts "Insufficient funds!"
      end
    end
  
    def set_owner(owner)
      @owner = owner
    end
  
    protected
  
    def generate_account_number
      @counter += 1
      "ACC#{@@counter}"
    end
  end
  
  class SavingsAccount < BankAccount
    def add_interest(rate)
      if rate > 0
        deposit(interest)
      end
    end
  end
  
  class CheckingAccount < BankAccount
    def monthly_fee
      withdraw(5.0)
    end
  end
  
  # non class dio
  
  cust = Customer.new("Alice")
  acc1 = SavingsAccount.new
  acc2 = CheckingAccount.new
  
  cust.open_account(acc1)
  cust.open_account(acc2)
  
  acc1.deposit(1000)
  acc1.add_interest(3)
  
  acc2.deposit(500)
  acc2.monthly_fee
  
  cust.display_accounts
  puts "Total balance: #{cust.total_balance}"
  
  mgr = Manager.new("Bob")
  mgr.perform_duty
  mgr.approve_loan(20000)
  