class Animal
    def speak(name, cow, name) # duplikat parametra
      puts "Animal says something"
    end
  end
  
  class Dog < Pet  # nasljedjivanje nedef klase Pet
    def bark
      puts "Woof"
    end
  
    def bark  # duplikat metode u istoj klasi
      puts "WOOF"
    end
  end
  
  def global_method(x, x)  # dupl param globalne metode
    puts x
  end
  
  def global_method(y)  # duplikat globalne metode
    puts y
  end

  # Poziv metode sa pogrešnim brojem argumenata
  class Cow < Animal
    def moo
      speak()         # ocekuje 3 parametra
      global_method() # ocekuje 1 parametar
    end
  end
  
  