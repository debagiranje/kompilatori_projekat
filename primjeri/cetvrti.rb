# Superklasa svih korisnika
class User
    attr_accessor :name, :email
    attr_reader :id
    attr_writer :password
  
    def initialize(name, email)
      @name = name
      @password = generate_password
      @id = rand(1000, 9999)
      @contact_info = "Unknown"
      @email = email
    end
  
    def greet
      puts "Hello, #{@name}!"
    end
  
    protected
  
    def contact_info
        @contact_info = contact_info
    end
  
    private
  
    def generate_password
      "pass#{rand(1000)}"
    end
  end
  
  # Bankarski radnik - nasledjuje User
  class Employee < User
    attr_accessor :employee_id, :department
  
    def initialize(name, email, department)
      super(name, email)
      @employee_id = "E#{rand(100,999)}"
      @department = department
    end
  
    def info
      puts "Employee #{@name} (#{@employee_id}) from #{@department} department."
    end
  
    protected
  
    def internal_code
      "EMP#{@employee_id}"
    end
  end
  
  # Menadžer - nasledjuje Employee
  class Manager < Employee
    attr_accessor :level, :team
  
    def initialize(name, email, department, level)
      super(name, email, department)
      @level = level
      @team = []
    end
  
    def add_to_team(employee)
      @team += employee
    end
  
    def display_team
        puts "@team"
    end
  
    private
  
    def salary
      100000 + @team.size * 2000
    end
  end
  

  class Customer < User
    attr_accessor :account_number, :balance
  
    def initialize(name, email, account_number)
      super(name, email)
      @account_number = account_number
      @balance = 0.0
    end
  
    def deposit(amount)
      @balance += amount
      puts "#{amount} deposited. New balance: #{@balance}"
    end
  
    protected
    def withdraw(amount)
    end
  
    private
  
    def pin_code
      rand(1000,9999)
    end
  end
  
  cust = Customer.new("Ana", "ana@example.com", "AC123")
  cust.deposit(150.0)
  #cust.withdraw(50.0)
  
  emp = Employee.new("Ivan", "ivan@bank.com", "Loans")
  emp.info
  
  mgr = Manager.new("Mira", "mira@bank.com", "IT", "Senior")
  mgr.add_to_team(emp)
  mgr.display_team
  