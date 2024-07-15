# OOP

# learn about Object Oriented Programming by answering these questions


<details>
<summary>
1. Basic Class and Object
</summary>
Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
</details>


<details>
<summary>
2. Class Method and Self
</summary>
Problem: Add a method to the Car class that displays the full name of the car (brand and model).
</details>


<details>
<summary>
3. Inheritance
</summary>
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
</details>



<details>
<summary>
4. Encapsulation
</summary>
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
</details>

<details>
<summary>
5. Polymorphism
</summary>
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
</details>



<details>
<summary>
6. Class Variables
</summary>
Problem: Add a class variable to Car that keeps track of the number of cars created.
</details>




<details>
<summary>
7. Static Method
</summary>
Problem: Add a static method to the Car class that returns a general description of a car.
</details>



<details>
<summary>
8. Property Decorators
</summary>
Problem: Use a property decorator in the Car class to make the model attribute read-only.
</details>



<details>
<summary>
9. Class Inheritance and isinstance() Function
</summary>
Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
</details>



<details>
<summary>
10. Multiple Inheritance
</summary>
Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
</details>

---

<details>
<summary>
1. Basic Class and Object
</summary>
Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
</details>

---



```python
class Car:
  brand = None
  model = None

my_car = Car()
print(my_car)
```

    <__main__.Car object at 0x7f5b0d53d0f0>
    


```python
class Car:
  def __init__(self, brand,model):
    self.brand = brand
    self.model = model

my_car = Car("Toyota","Corolla")
print(my_car)
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
```

    <__main__.Car object at 0x7f5b0e18b2b0>
    Toyota
    Corolla
    Tata
    Safari
    
---

<details>
<summary>
2. Class Method and Self
</summary>
Problem: Add a method to the Car class that displays the full name of the car (brand and model).
</details>

---


```python
class Car:
  def __init__(self, brand,model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"

my_car = Car("Toyota","Corolla")
print(my_car)
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
```

    <__main__.Car object at 0x7a487cf42470>
    Toyota
    Corolla
    Toyota Corolla
    
---

<details>
<summary>
3. Inheritance
</summary>
Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
</details>

---

```python
class Car:
  def __init__(self, brand,model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
print(my_tesla.brand)
print(my_tesla.full_name())
```

    Tesla
    Tesla Model S
    
---

<details>
<summary>
4. Encapsulation
</summary>
Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
</details>

---

```python
class Car:
  def __init__(self, brand,model):
    self.__brand = brand
    self.model = model

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.model}"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85Kwh")

print(my_tesla.get_brand())
# print(my_tesla.__brand)

```

    Tesla
    
---

<details>
<summary>
5. Polymorphism
</summary>
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
</details>

---

```python
class Car:
  def __init__(self, brand,model):
    self.__brand = brand
    self.model = model

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.model}"

  def fuel_type(self):
    return "Petrol or Diesel"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
safari = Car("Tata","Safari")

print(safari.fuel_type())
print(my_tesla.fuel_type())
```

    Petrol or Diesel
    Electric Charge
    
---

<details>
<summary>
6. Class Variables
</summary>
Problem: Add a class variable to Car that keeps track of the number of cars created.
</details>

---

```python
class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.__brand = brand
    self.model = model
    Car.total_car+=1
    #self.total_car+=1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.model}"

  def fuel_type(self):
    return "Petrol or Diesel"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
safari = Car("Tata","Safari")

print(safari.fuel_type())
print(my_tesla.fuel_type())
print(Car.total_car)
```

    Petrol or Diesel
    Electric Charge
    2
    
---

<details>
<summary>
7. Static Method
</summary>
Problem: Add a static method to the Car class that returns a general description of a car.
</details>

---

```python
class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.__brand = brand
    self.model = model
    Car.total_car+=1
    #self.total_car+=1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def gen_desc():
    return "Cars are means of transport"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
safari = Car("Tata","Safari")

print(Car.gen_desc())
```

    Cars are means of transport
    
---

<details>
<summary>
8. Property Decorators
</summary>
Problem: Use a property decorator in the Car class to make the model attribute read-only.
</details>

---

```python
class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.__brand = brand
    self.__model = model
    Car.total_car+=1
    #self.total_car+=1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def gen_desc():
    return "Cars are means of transport"

  @property
  def model(self):
    return self.__model

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
safari = Car("Tata","Safari")
# safari.model = "city"
print(safari.model)
```

    Safari
    
---

<details>
<summary>
9. Class Inheritance and isinstance() Function
</summary>
Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
</details>

---

```python
class Car:
  total_car = 0
  def __init__(self, brand,model):
    self.__brand = brand
    self.__model = model
    Car.total_car+=1
    #self.total_car+=1

  def get_brand(self):
    return self.__brand

  def full_name(self):
    return f"{self.__brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def gen_desc():
    return "Cars are means of transport"

  @property
  def model(self):
    return self.__model

class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85Kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
```

    True
    True
    
---

<details>
<summary>
10. Multiple Inheritance
</summary>
Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
</details>

---

```python
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
```
