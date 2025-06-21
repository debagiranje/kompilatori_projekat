class Animal
    attr_accessor :name, :age
    attr_reader :species
    attr_writer :weight
  
    def initialize(name, age, species)
      @name = name
      @age = age
      @species = species
      @weight = 0
    end
  
    def speak
      puts "#{@name} is making a sound."
    end
  
    protected
    def sleep
      puts "#{@name} is sleeping."
    end
  
    private
    def secret
      puts "This is a secret method."
    end
  end
  
  class Mammal < Animal
    attr_accessor :fur_color
  
    def initialize(name, age, species, fur_color)
      super(name, age, species)
      @fur_color = fur_color
    end
  
    def speak
      puts "#{@name} the mammal is making a mammal sound."
    end
  end
  
  class Dog < Mammal
    def initialize(name, age, fur_color, breed)
      super(name, age, "Dog", fur_color)
      @breed = breed
    end
  
    def speak
      puts "#{@name} barks: Woof!"
    end
  
    def display_breed
      puts "#{@name} is a #{@breed}."
    end
  
    private
    def wag_tail
      puts "#{@name} is wagging its tail."
    end
  end
  
  class Cat < Mammal
    def speak
      puts "#{@name} meows: Meow!"
    end
  
    def call_secret
    end
  end
  
  class Bird < Animal
    attr_accessor :wing_span
  
    def initialize(name, age, species, wing_span)
      super(name, age, species)
      @wing_span = wing_span
    end
  
    def speak
      puts "#{@name} chirps."
    end
  
    protected
    def fly
      puts "#{@name} is flying."
    end
  end
  
  # ovaj dio se ne generise u dijagramu, ali je analiziran
  
  dog = Dog.new("Rex", 5, "Brown", "Labrador")
  dog.speak
  dog.call_sleep
  dog.display_breed
  
  cat = Cat.new("Whiskers", 3, "Cat", "Black")
  cat.speak
  
  bird = Bird.new("Tweety", 2, "Canary", 25)
  bird.speak
  
  