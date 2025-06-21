class Person
    attr_accessor :name, :age
  
    def initialize(name, age)
      @name = name
      @age  = age.to_i
    end
  
    proteced
    def inspect
      "#{name} (#{age})"
    end
  end
