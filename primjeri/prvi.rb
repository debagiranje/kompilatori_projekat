class Person
  attr_accessor :name, :age

  def initialize(name, age, id)
    @name = name
    @age = age
    @id = id
  end

  def greet
    puts "Hello, my name is #{@name}."
  end
end

class Student < Person
  attr_accessor :university, :student_id
  
  def initialize(name, age, id, university, student_id)
    @university = university
    @student_id = student_id
  end

  def greet
    puts "Hi, I'm #{@name}, a student at #{@university}."
  end

  def show_student_info
    puts "Student ID: #{@student_id}"
  end
end
