# C# Arrays

Arrays are used in C# to store multiple values in a single variable, instead of declaring separate variables for each value. They provide a way to efficiently manage and manipulate collections of data.

```csharp
string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
int[] myNum = { 10, 20, 30, 40 };
Console.WriteLine(cars[0]);   // Output: Volvo
Console.WriteLine(myNum[0]);  // Output: 10

```

# C# Methods

> A method is a block of code which only runs when it is called.

> You can pass data, known as parameters, into a method.

> Methods are used to perform certain actions, and they are also known as functions.

> Why use methods? To reuse code: define the code once, and use it many times.

## Create a Method

> A method is defined with the name of the method, followed by parentheses (). C# provides some pre-defined methods, which you already are familiar with, such as Main(), but you can also create your own methods to perform certain actions:

Example

Create a method inside the Program class:

```csharp
class Program
{
  static void MyMethod() 
  {
    // code to be executed
  }
}
```

> - `MyMethod()` is the name of the method

> - `static` means that the method belongs to the Program class and not an object of the Program class. You will learn more about objects and how to access methods through objects later in this tutorial.

> - `void` means that this method does not have a return value. You will learn more about return values later in this chapter

> `Note:` In C#, it is good practice to start with an uppercase letter when naming methods, as it makes the code easier to read.

## Call a Method

> To call (execute) a method, write the method's name followed by two parentheses () and a semicolon;

In the following example, MyMethod() is used to print a text (the action), when it is called:

Example

Inside Main(), call the myMethod() method:

```csharp
static void MyMethod() 
{
  Console.WriteLine("I just got executed!");
}

static void Main(string[] args)
{
  MyMethod();
}

// Outputs "I just got executed!"
```

> A method can be called multiple times:

Example
```csharp
static void MyMethod() 
{
  Console.WriteLine("I just got executed!");
}

static void Main(string[] args)
{
  MyMethod();
  MyMethod();
  MyMethod();
}

// I just got executed!
// I just got executed!
// I just got executed!
```

## C# Method Parameters

> Parameters and Arguments

> Information can be passed to methods as parameter. Parameters act as variables inside the method.

> They are specified after the method name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

The following example has a method that takes a string called `fname` as parameter. 

When the method is called, we pass along a first name, which is used inside the method to print the full name:

Example
```csharp
static void MyMethod(string fname) 
{
  Console.WriteLine(fname + " Refsnes");
}

static void Main(string[] args)
{
  MyMethod("Liam");
  MyMethod("Jenny");
  MyMethod("Anja");
}

// Liam Refsnes
// Jenny Refsnes
// Anja Refsnes
```

> When a parameter is passed to the method, it is called an argument. So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.

## Multiple Parameters

You can have as many parameters as you like, just separate them with commas:

Example
```csharp
static void MyMethod(string fname, int age) 
{
  Console.WriteLine(fname + " is " + age);
}

static void Main(string[] args)
{
  MyMethod("Liam", 5);
  MyMethod("Jenny", 8);
  MyMethod("Anja", 31);
}

// Liam is 5
// Jenny is 8
// Anja is 31
```

> `Note:` when you are working with multiple parameters, the method call must have the same number of arguments as there are parameters, and the arguments must be passed in the same order.

## C# Method Overloading

> With method overloading, multiple methods can have the same name with different parameters:

Example
```csharp
int MyMethod(int x)
float MyMethod(float x)
double MyMethod(double x, double y)
```

Consider the following example, which have two methods that add numbers of different type:

```csharp
static int PlusMethodInt(int x, int y)
{
  return x + y;
}

static double PlusMethodDouble(double x, double y)
{
  return x + y;
}

static void Main(string[] args)
{
  int myNum1 = PlusMethodInt(8, 5);
  double myNum2 = PlusMethodDouble(4.3, 6.26);
  Console.WriteLine("Int: " + myNum1);
  Console.WriteLine("Double: " + myNum2);
}
```

> Instead of defining two methods that should do the same thing, it is better to overload one.

In the example below, we overload the PlusMethod method to work for both int and double:

Example
```csharp
static int PlusMethod(int x, int y)
{
  return x + y;
}

static double PlusMethod(double x, double y)
{
  return x + y;
}

static void Main(string[] args)
{
  int myNum1 = PlusMethod(8, 5);
  double myNum2 = PlusMethod(4.3, 6.26);
  Console.WriteLine("Int: " + myNum1);
  Console.WriteLine("Double: " + myNum2);
}
```

> `Note:` Multiple methods can have the same name as long as the number and/or type of parameters are different.

## C# Default Parameter Value

> You can also use a default parameter value, by using the equals sign (=).

If we call the method without an argument, it uses the default value ("Norway"):

Example
```csharp
static void MyMethod(string country = "Norway") 
{
  Console.WriteLine(country);
}

static void Main(string[] args)
{
  MyMethod("Sweden");
  MyMethod("India");
  MyMethod();
  MyMethod("USA");
}

// Sweden
// India
// Norway
// USA
```

> `Note:` A parameter with a default value, is often known as an "optional parameter". From the example above, country is an optional parameter and "Norway" is the default value.

## C# Return Values

> In the previous page, we used the void keyword in all examples, which indicates that the method should not return a value.

If you want the method to return a value, you can use a primitive data type (such as int or double) instead of void, and use the return keyword inside the method:

Example
```csharp
static int MyMethod(int x) 
{
  return 5 + x;
}

static void Main(string[] args)
{
  Console.WriteLine(MyMethod(3));
}

// Outputs 8 (5 + 3)
```

This example returns the sum of a method's two parameters:

Example
```csharp
static int MyMethod(int x, int y) 
{
  return x + y;
}

static void Main(string[] args)
{
  Console.WriteLine(MyMethod(5, 3));
}

// Outputs 8 (5 + 3)
```

You can also store the result in a variable (recommended, as it is easier to read and maintain):

Example
```csharp
static int MyMethod(int x, int y) 
{
  return x + y;
}

static void Main(string[] args)
{
  int z = MyMethod(5, 3);
  Console.WriteLine(z);
}

// Outputs 8 (5 + 3)
```

## C# Named Arguments

> It is also possible to send arguments with the key: value syntax.

> That way, the order of the arguments does not matter:

Example
```csharp
static void MyMethod(string child1, string child2, string child3) 
{
  Console.WriteLine("The youngest child is: " + child3);
}

static void Main(string[] args)
{
  MyMethod(child3: "John", child1: "Liam", child2: "Liam");
}

// The youngest child is: John
```



<br>

# C# OOP

### What is OOP?

> OOP stands for `Object-Oriented Programming.`

> Procedural programming is about writing procedures or methods that perform operations on the data, while object-oriented programming is about creating objects that contain both data and methods.

Object-oriented programming has several advantages over procedural programming:

> - OOP is faster and easier to execute
> - OOP provides a clear structure for the programs
> - OOP helps to keep the C# code DRY "Don't Repeat Yourself", and makes the code easier to maintain, modify and debug
> - OOP makes it possible to create full reusable applications with less code and shorter development time

> `Tip:` Tip: The "Don't Repeat Yourself" (DRY) principle is about reducing the repetition of code. You should extract out the codes that are common for the application, and place them at a single place and reuse them instead of repeating it.

## C# - What are Classes and Objects?

> Classes and objects are the two main aspects of object-oriented programming.

Look at the following illustration to see the difference between class and objects:

| Class    | Objects |
| -------- | ------- |
|  Fruit | Apple    |
|  | Banana |
|    | Mango |

Another Example

| Class    | Objects |
| -------- | ------- |
|  Car | Volvo    |
|  | Audi |
|    | Toyota |

> So, a class is a template for objects, and an object is an instance of a class.

> When the individual objects are created, they inherit all the variables and methods from the class.

## C# Classes and Objects

> You learned from the previous chapter that C# is an object-oriented programming language.

> Everything in C# is associated with classes and objects, along with its attributes and methods.

> For example: in real life, a car is an object.

> The car has attributes, such as weight and color, and methods, such as drive and brake.

> A Class is like an object constructor, or a "blueprint" for creating objects.

## Create a Class

To create a class, use the class keyword:

```csharp
class Car 
{
  string color = "red";
}
```

> When a variable is declared directly in a class, it is often referred to as a field (or attribute).

It is not required, but it is a good practice to start with an uppercase first letter when naming classes. Also, it is common that the name of the C# file and the class matches, as it makes our code organized. However it is not required (like in Java).

## Create an Object

> An object is created from a class. We have already created the class named Car, so now we can use this to create objects.

To create an object of Car, specify the class name, followed by the object name, and use the keyword new:

Example

Create an object called "myObj" and use it to print the value of color:
```csharp
class Car 
{
  string color = "red";

  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.color);
  }
}
```

> `Note:` we use the dot syntax (.) to access variables/fields inside a class (myObj.color).

## C# Multiple Classes and Objects

> Multiple Objects

You can create multiple objects of one class:

Example

Create two objects of Car:

```csharp
class Car
{
  string color = "red";
  static void Main(string[] args)
  {
    Car myObj1 = new Car();
    Car myObj2 = new Car();
    Console.WriteLine(myObj1.color);
    Console.WriteLine(myObj2.color);
  }
}
```

> Using Multiple Classes

You can also create an object of a class and access it in another class.

> This is often used for better organization of classes (one class has all the fields and methods, while the other class holds the Main() method (code to be executed)).

- prog2.cs

```csharp
class Car 
{
  public string color = "red";
}
```

- prog.cs
```csharp
class Program
{
  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.color);
  }
}
```

> Did you notice the public keyword? It is called an access modifier, which specifies that the color variable/field of Car is accessible for other classes as well, such as Program.

## C# Class Members

> Class Members

> Fields and methods inside classes are often referred to as "Class Members":

Example

Create a Car class with three class members: two fields and one method.
```csharp
// The class
class MyClass
{
  // Class members
  string color = "red";        // field
  int maxSpeed = 200;          // field
  public void fullThrottle()   // method
  {
    Console.WriteLine("The car is going as fast as it can!");
  }
}
```

## Fields

> In the previous chapter, you learned that variables inside a class are called fields, and that you can access them by creating an object of the class, and by using the dot syntax (.).

The following example will create an object of the Car class, with the name myObj. Then we print the value of the fields color and maxSpeed:

Example
```csharp
class Car 
{
  string color = "red";
  int maxSpeed = 200;

  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.color);
    Console.WriteLine(myObj.maxSpeed);
  }
}
```

You can also leave the fields blank, and modify them when creating the object:

Example
```csharp
class Car 
{
  string color;
  int maxSpeed;

  static void Main(string[] args)
  {
    Car myObj = new Car();
    myObj.color = "red";
    myObj.maxSpeed = 200;
    Console.WriteLine(myObj.color);
    Console.WriteLine(myObj.maxSpeed);
  }
}
```

This is especially useful when creating multiple objects of one class:

Example
```csharp
class Car 
{
  string model;
  string color;
  int year;

  static void Main(string[] args)
  {
    Car Ford = new Car();
    Ford.model = "Mustang";
    Ford.color = "red";
    Ford.year = 1969;

    Car Opel = new Car();
    Opel.model = "Astra";
    Opel.color = "white";
    Opel.year = 2005;

    Console.WriteLine(Ford.model);
    Console.WriteLine(Opel.model);
  }
}
```

## Object Methods

> You learned from the C# Methods chapter that methods are used to perform certain actions.

> Methods normally belong to a class, and they define how an object of a class behaves.

> Just like with fields, you can access methods with the dot syntax. However, note that the method must be public. And remember that we use the name of the method followed by two parentheses () and a semicolon ; to call (execute) the method:

Example
```csharp
class Car 
{
  string color;                 // field
  int maxSpeed;                 // field
  public void fullThrottle()    // method
  {
    Console.WriteLine("The car is going as fast as it can!"); 
  }

  static void Main(string[] args)
  {
    Car myObj = new Car();
    myObj.fullThrottle();  // Call the method
  }
}
```

Why did we declare the method as public, and not static, like in the examples from the C# Methods Chapter?

> The reason is simple: a static method can be accessed without creating an object of the class, while public methods can only be accessed by objects.

## Use Multiple Classes

> Remember from the last chapter, that we can use multiple classes for better organization (one for fields and methods, and another one for execution). This is recommended:

prog2.cs
```csharp
class Car 
{
  public string model;
  public string color;
  public int year;
  public void fullThrottle()
  {
    Console.WriteLine("The car is going as fast as it can!"); 
  }
}
```

prog.cs
```csharp
class Program
{
  static void Main(string[] args)
  {
    Car Ford = new Car();
    Ford.model = "Mustang";
    Ford.color = "red";
    Ford.year = 1969;

    Car Opel = new Car();
    Opel.model = "Astra";
    Opel.color = "white";
    Opel.year = 2005;

    Console.WriteLine(Ford.model);
    Console.WriteLine(Opel.model);
  }
}
```

> The public keyword is called an access modifier, which specifies that the fields of Car are accessible for other classes as well, such as Program.


# C# Constructors

> Constructors

> A constructor is a `special method` that is used to initialize objects. The advantage of a constructor, is that it is called when an object of a class is created. It can be used to set initial values for fields:

Example

Create a constructor:
```csharp
// Create a Car class
class Car
{
  public string model;  // Create a field

  // Create a class constructor for the Car class
  public Car()
  {
    model = "Mustang"; // Set the initial value for model
  }

  static void Main(string[] args)
  {
    Car Ford = new Car();  // Create an object of the Car Class (this will call the constructor)
    Console.WriteLine(Ford.model);  // Print the value of model
  }
}

// Outputs "Mustang"
```

> `Note:` the constructor name must match the class name, and it cannot have a return type (like void or int).

> Also note that the constructor is called when the object is created.

> All classes have constructors by default: if you do not create a class constructor yourself, C# creates one for you. However, then you are not able to set initial values for fields.

Constructors save time! Take a look at the last example on this page to really understand why.

## Constructor Parameters

> Constructors can also take parameters, which is used to initialize fields.

> The following example adds a `string modelName` parameter to the constructor. 

> Inside the constructor we set `model` to `modelName` (`model=modelName`).

> When we call the constructor, we pass a parameter to the constructor ("`Mustang"`), which will set the value of `model` to `"Mustang"`:

Example
```csharp
class Car
{
  public string model;

  // Create a class constructor with a parameter
  public Car(string modelName)
  {
    model = modelName;
  }

  static void Main(string[] args)
  {
    Car Ford = new Car("Mustang");
    Console.WriteLine(Ford.model);
  }
}

// Outputs "Mustang"
```

You can have as many parameters as you want:

Example
```csharp
class Car
{
  public string model;
  public string color;
  public int year;

  // Create a class constructor with multiple parameters
  public Car(string modelName, string modelColor, int modelYear)
  {
    model = modelName;
    color = modelColor;
    year = modelYear;
  }

  static void Main(string[] args)
  {
    Car Ford = new Car("Mustang", "Red", 1969);
    Console.WriteLine(Ford.color + " " + Ford.year + " " + Ford.model);
  }
}


// Outputs Red 1969 Mustang
```

> `Tip:` Just like other methods, constructors can be overloaded by using different numbers of parameters.

## Constructors Save Time

> When you consider the example from the previous chapter, you will notice that constructors are very useful, as they help reducing the amount of code:

> Without constructor:

prog.cs
```csharp
class Program
{
  static void Main(string[] args)
  {
    Car Ford = new Car();
    Ford.model = "Mustang";
    Ford.color = "red";
    Ford.year = 1969;

    Car Opel = new Car();
    Opel.model = "Astra";
    Opel.color = "white";
    Opel.year = 2005;

    Console.WriteLine(Ford.model);
    Console.WriteLine(Opel.model);
  }
}
```

> With constructor:

prog.cs
```csharp
class Program
{
  static void Main(string[] args)
  {
    Car Ford = new Car("Mustang", "Red", 1969);
    Car Opel = new Car("Astra", "White", 2005);

    Console.WriteLine(Ford.model);
    Console.WriteLine(Opel.model);
  }
}
```

# C# Access Modifiers

> Access Modifiers

> By now, you are quite familiar with the public keyword that appears in many of our examples:

```
public string color;
```

> The public keyword is an access modifier, which is used to set the access level/visibility for classes, fields, methods and properties.

C# has the following access modifiers:

| Modifier | Description |
| -------- | ------- |
|  `public` |  The code is accessible for all classes  |
| `private` | The code is only accessible within the same class |
|  `protected` | The code is accessible within the same class, or in a class that is inherited from that class. You will learn more about inheritance in a later chapter |
| `internal` | The code is only accessible within its own assembly, but not from another assembly. You will learn more about this in a later chapter |

> There's also two combinations: `protected internal` and `private protected.`

> For now, lets focus on public and private modifiers.

## Private Modifier

> If you declare a field with a private access modifier, it can only be accessed within the same class:

Example
```csharp
class Car
{
  private string model = "Mustang";

  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.model);
  }
}
```
The output will be:
```
Mustang
```

If you try to access it outside the class, an error will occur:

Example: Error
```csharp
class Car
{
  private string model = "Mustang";
}

class Program
{
  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.model);
  }
}
```
The output will be:
```
'Car.model' is inaccessible due to its protection level
The field 'Car.model' is assigned but its value is never used
```

## Public Modifier

> If you declare a field with a public access modifier, it is accessible for all classes:

Example
```csharp
class Car
{
  public string model = "Mustang";
}

class Program
{
  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.model);
  }
}
```

The output will be:
```
Mustang
```

### Why Access Modifiers?

> To control the visibility of class members (the security level of each individual class and class member).

> To achieve "`Encapsulation"` - which is the process of making sure that "sensitive" data is hidden from users. This is done by declaring fields as private. You will learn more about this in the next chapter.

> `Note:` By default, all members of a class are private if you don't specify an access modifier:

Example
```csharp
class Car
{
  string model;  // private
  string year;   // private
}
```
# C# Properties
>You learned from the previous chapter that private variables can only be accessed within the same class (an outside class has no access to it). However, sometimes we need to access them - and it can be done with properties.

>A property is like a combination of a variable and a method, and it has two methods: a get and a set method:

Example

```csharp
class Person
{
  private string name; // field

  public string Name   // property
  {
    get { return name; }   // get method
    set { name = value; }  // set method
  }
}
```
Example explained
The Name property is associated with the name field. It is a good practice to use the same name for both the property and the private field, but with an uppercase first letter.

The get method returns the value of the variable name.

The set method assigns a value to the name variable. The value keyword represents the value we assign to the property.

>Now we can use the Name property to access and update the private field of the Person class:

Example

```csharp
class Person
{
  private string name; // field
  public string Name   // property
  {
    get { return name; }
    set { name = value; }
  }
}

class Program
{
  static void Main(string[] args)
  {
    Person myObj = new Person();
    myObj.Name = "Liam";
    Console.WriteLine(myObj.Name);
  }
}
#Output: Liam
```

## Automatic Properties (Short Hand)
>C# also provides a way to use short-hand / automatic properties, where you do not have to define the field for the property, and you only have to write get; and set; inside the property.

>The following example will produce the same result as the example above. The only difference is that there is less code:

Example

```csharp
class Person
{
  public string Name  // property
  { get; set; }
}

class Program
{
  static void Main(string[] args)
  {
    Person myObj = new Person();
    myObj.Name = "Liam";
    Console.WriteLine(myObj.Name);
  }
}
#Output: Liam
```
# OOP: 02 Inheritance

> Inheritance (Derived and Base Class)

> In C#, it is possible to inherit fields and methods from one class to another. We group the "inheritance concept" into two categories:

> - `Derived Class` (child) - the class that inherits from another
> - `Base Class`(parent) - the class being inherited from

> To inherit from a class, use the : symbol.

In the example below, the `Car` class (child) inherits the fields and methods from the `Vehicle` class (parent):

Example

```csharp
class Vehicle  // base class (parent) 
{
  public string brand = "Ford";  // Vehicle field
  public void honk()             // Vehicle method 
  {                    
    Console.WriteLine("Tuut, tuut!");
  }
}

class Car : Vehicle  // derived class (child)
{
  public string modelName = "Mustang";  // Car field
}

class Program
{
  static void Main(string[] args)
  {
    // Create a myCar object
    Car myCar = new Car();

    // Call the honk() method (From the Vehicle class) on the myCar object
    myCar.honk();

    // Display the value of the brand field (from the Vehicle class) and the value of the modelName from the Car class
    Console.WriteLine(myCar.brand + " " + myCar.modelName);
  }
}
```

## Why And When To Use "Inheritance"?

> It is useful for code reusability: reuse fields and methods of an existing class when you create a new class.

## The sealed Keyword

> If you don't want other classes to inherit from a class, use the sealed keyword:

If you try to access a sealed class, C# will generate an error:

```csharp
sealed class Vehicle 
{
  ...
}

class Car : Vehicle 
{
  ...
}
```

The error message will be something like this:

```
'Car': cannot derive from sealed type 'Vehicle'
```


# OOP: 03 Polymorphism

> Polymorphism and Overriding Methods

> Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.

> Like we specified in the previous chapter; `Inheritance` lets us inherit fields and methods from another class. 

> `Polymorphism` uses those methods to perform different tasks.

> This allows us to perform a single action in different ways.

> For example, think of a base class called `Animal` that has a method called `animalSound()`. 

Derived classes of Animals could be Pigs, Cats, Dogs, Birds - And they also have their own implementation of an animal sound (the pig oinks, and the cat meows, etc.):

Example
```csharp
class Animal  // Base class (parent) 
{
  public void animalSound() 
  {
    Console.WriteLine("The animal makes a sound");
  }
}

class Pig : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The pig says: wee wee");
  }
}

class Dog : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The dog says: bow wow");
  }
}
```

> `Note:` Remember from the Inheritance chapter that we use the `:` symbol to inherit from a class.

> Now we can create Pig and Dog objects and call the animalSound() method on both of them:

Example
```csharp
class Animal  // Base class (parent) 
{
  public void animalSound() 
  {
    Console.WriteLine("The animal makes a sound");
  }
}

class Pig : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The pig says: wee wee");
  }
}

class Dog : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The dog says: bow wow");
  }
}

class Program 
{
  static void Main(string[] args) 
  {
    Animal myAnimal = new Animal();  // Create a Animal object
    Animal myPig = new Pig();  // Create a Pig object
    Animal myDog = new Dog();  // Create a Dog object

    myAnimal.animalSound();
    myPig.animalSound();
    myDog.animalSound();
  }
}
```
The output will be:
```
The animal makes a sound
The animal makes a sound
The animal makes a sound
```


## Not The Output I Was Looking For

> The output from the example above was probably not what you expected. That is because the base class method overrides the derived class method, when they share the same name.

> However, C# provides an option to override the base class method, by adding the virtual keyword to the method inside the base class, and by using the override keyword for each derived class methods:

Example
```csharp
class Animal  // Base class (parent) 
{
  public virtual void animalSound() 
  {
    Console.WriteLine("The animal makes a sound");
  }
}

class Pig : Animal  // Derived class (child) 
{
  public override void animalSound() 
  {
    Console.WriteLine("The pig says: wee wee");
  }
}

class Dog : Animal  // Derived class (child) 
{
  public override void animalSound() 
  {
    Console.WriteLine("The dog says: bow wow");
  }
}

class Program 
{
  static void Main(string[] args) 
  {
    Animal myAnimal = new Animal();  // Create a Animal object
    Animal myPig = new Pig();  // Create a Pig object
    Animal myDog = new Dog();  // Create a Dog object

    myAnimal.animalSound();
    myPig.animalSound();
    myDog.animalSound();
  }
}
```

The output will be:
```
The animal makes a sound
The pig says: wee wee
The dog says: bow wow
```

## Why And When To Use "Inheritance" and "Polymorphism"?

> It is useful for code reusability: reuse fields and methods of an existing class when you create a new class.

# OOP: 04 Abstraction

> Abstract Classes and Methods

> Data `abstraction` is the process of hiding certain details and showing only essential information to the user.

> Abstraction can be achieved with either `abstract classes` or `interfaces` (which you will learn more about in the next chapter).

The abstract keyword is used for classes and methods:

> - `Abstract class`: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).

> - `Abstract method`: can only be used in an abstract class, and it does not have a body. The body is provided by the derived class (inherited from).

An abstract class can have both abstract and regular methods:

```csharp
abstract class Animal 
{
  public abstract void animalSound();
  public void sleep() 
  {
    Console.WriteLine("Zzz");
  }
}
```

From the example above, it is not possible to create an object of the Animal class:

```
Animal myObj = new Animal(); // Will generate an error (Cannot create an instance of the abstract class or interface 'Animal')
```

> To access the abstract class, it must be inherited from another class. Let's convert the Animal class we used in the Polymorphism chapter to an abstract class.

> `Note:` Remember from the Inheritance chapter that we use the : symbol to inherit from a class, and that we use the override keyword to override the base class method.

Example
```csharp
// Abstract class
abstract class Animal
{
  // Abstract method (does not have a body)
  public abstract void animalSound();
  // Regular method
  public void sleep()
  {
    Console.WriteLine("Zzz");
  }
}

// Derived class (inherit from Animal)
class Pig : Animal
{
  public override void animalSound()
  {
    // The body of animalSound() is provided here
    Console.WriteLine("The pig says: wee wee");
  }
}

class Program
{
  static void Main(string[] args)
  {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();  // Call the abstract method
    myPig.sleep();  // Call the regular method
  }
}
```

## Why And When To Use Abstract Classes and Methods?

> To achieve security - hide certain details and only show the important details of an object.


# C# Interface

> Interfaces

Another way to achieve abstraction in C#, is with interfaces.

> An interface is a completely `"abstract class"`, which can only contain abstract methods and properties (with empty bodies):

Example
```csharp
// interface
interface Animal 
{
  void animalSound(); // interface method (does not have a body)
  void run(); // interface method (does not have a body)
}
```

> It is considered good practice to start with the letter "I" at the beginning of an interface, as it makes it easier for yourself and others to remember that it is an interface and not a class.

> By default, members of an interface are `abstract` and `public`.

> `Note:` Interfaces can contain properties and methods, but not fields.

- To access the interface methods, the interface must be "implemented" (kinda like inherited) by another class.

- To implement an interface, use the : symbol (just like with inheritance).

The body of the interface method is provided by the "implement" class. Note that you do not have to use the override keyword when implementing an interface:

Example
```csharp
// Interface
interface IAnimal 
{
  void animalSound(); // interface method (does not have a body)
}

// Pig "implements" the IAnimal interface
class Pig : IAnimal 
{
  public void animalSound() 
  {
    // The body of animalSound() is provided here
    Console.WriteLine("The pig says: wee wee");
  }
}

class Program 
{
  static void Main(string[] args) 
  {
    Pig myPig = new Pig();  // Create a Pig object
    myPig.animalSound();
  }
}
```
Notes on Interfaces:

> - Like `abstract classes`, interfaces `cannot` be used to create objects (in the example above, it is not possible to create an "IAnimal" object in the Program class)
> - Interface methods do not have a body - the body is provided by the "implement" class
> - On implementation of an interface, you must override all of its methods
> - Interfaces can contain properties and methods, but not fields/variables
> - Interface members are by default `abstract` and `public`
> - An interface cannot contain a constructor (as it cannot be used to create objects)

## Why And When To Use Interfaces?

> 1. To achieve security - hide certain details and only show the important details of an object (interface).

> 2. C# does not support "multiple inheritance" (a class can only inherit from one base class). However, it can be achieved with interfaces, because the class can implement multiple interfaces. Note: To implement multiple interfaces, separate them with a comma (see example below).

## C# Multiple Interfaces

> Multiple Interfaces

o implement multiple interfaces, separate them with a comma:

Example
```csharp
interface IFirstInterface 
{
  void myMethod(); // interface method
}

interface ISecondInterface 
{
  void myOtherMethod(); // interface method
}

// Implement multiple interfaces
class DemoClass : IFirstInterface, ISecondInterface 
{
  public void myMethod() 
  {
    Console.WriteLine("Some text..");
  }
  public void myOtherMethod() 
  {
    Console.WriteLine("Some other text...");
  }
}

class Program 
{
  static void Main(string[] args)
  {
    DemoClass myObj = new DemoClass();
    myObj.myMethod();
    myObj.myOtherMethod();
  }
}
```

# C# Enum

> Enums

> An enum is a special "class" that represents a group of `constants` (unchangeable/read-only variables).

To create an enum, use the enum keyword (instead of class or interface), and separate the enum items with a comma:

Example
```csharp
enum Level 
{
  Low,
  Medium,
  High
}
```

You can access enum items with the dot syntax:

```csharp
Level myVar = Level.Medium;
Console.WriteLine(myVar);
```

> Enum is short for "enumerations", which means "specifically listed".

## Enum inside a Class

> You can also have an `enum` inside a class:

Example
```csharp
class Program
{
  enum Level
  {
    Low,
    Medium,
    High
  }
  static void Main(string[] args)
  {
    Level myVar = Level.Medium;
    Console.WriteLine(myVar);
  }
}
```
The output will be:
```
Medium
```

## Enum Values

> By default, the first item of an enum has the value 0. The second has the value 1, and so on.

> To get the integer value from an item, you must explicitly convert the item to an `int`:

Example
```csharp
enum Months
{
  January,    // 0
  February,   // 1
  March,      // 2
  April,      // 3
  May,        // 4
  June,       // 5
  July        // 6
}

static void Main(string[] args)
{
  int myNum = (int) Months.April;
  Console.WriteLine(myNum);
}
```

The output will be:
```
3
```

You can also assign your own enum values, and the next items will update their numbers accordingly:

Example
```csharp
enum Months
{
  January,    // 0
  February,   // 1
  March=6,    // 6
  April,      // 7
  May,        // 8
  June,       // 9
  July        // 10
}

static void Main(string[] args)
{
  int myNum = (int) Months.April;
  Console.WriteLine(myNum);
}
```

The output will be:
```
7
```

## Enum in a Switch Statement

> Enums are often used in `switch` statements to check for corresponding values:

Example
```csharp
enum Level 
{
  Low,
  Medium,
  High
}

static void Main(string[] args) 
{
  Level myVar = Level.Medium;
  switch(myVar) 
  {
    case Level.Low:
      Console.WriteLine("Low level");
      break;
    case Level.Medium:
       Console.WriteLine("Medium level");
      break;
    case Level.High:
      Console.WriteLine("High level");
      break;
  }
}
```
The output will be:
```
Medium level
```

## Why And When To Use Enums?

> Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.


# C# Files

> Working With Files

> The `File` class from the `System.IO` namespace, allows us to work with files:

Example
```
using System.IO;  // include the System.IO namespace

File.SomeFileMethod();  // use the file class with methods
```

The `File` class has many useful methods for creating and getting information about files. For example:

| Method | Description |
| -------- | ------- |
| `AppendText()`  | Appends text at the end of an existing file |
| `Copy()` | Copies a file |
| `Create()` | Creates or overwrites a file | 
Delete() | Deletes a file |
| `Exists()` | Tests whether the file exists |
|`ReadAllText()` | Reads the contents of a file |
| `Replace()` | Replaces the contents of a file with the contents of another file |
| `WriteAllText()` | Creates a new file and writes the contents to it. If the file already exists, it will be overwritten. |

## Write To a File and Read It

> In the following example, we use the `WriteAllText()` method to create a file named "filename.txt" and write some content to it. Then we use the `ReadAllText()` method to read the contents of the file:

Example
```csharp
using System.IO;  // include the System.IO namespace

string writeText = "Hello World!";  // Create a text string
File.WriteAllText("filename.txt", writeText);  // Create a file and write the content of writeText to it

string readText = File.ReadAllText("filename.txt");  // Read the contents of the file
Console.WriteLine(readText);  // Output the content
```

The output will be:
```
Hello  World!
```

# C# Exceptions - Try..Catch

> Exceptions

> When executing C# code, different errors can occur: coding errors made by the programmer, errors due to wrong input, or other unforeseeable things.

> When an error occurs, C# will normally stop and generate an error message. 

> The technical term for this is: C# will throw an `exception` (throw an error).

## C# try and catch

> The `try` statement allows you to define a block of code to be tested for errors while it is being executed.

> The `catch` statement allows you to define a block of code to be executed, if an error occurs in the try block.

The `try` and `catch` keywords come in pairs:

Syntax
```csharp
try 
{
  //  Block of code to try
}
catch (Exception e)
{
  //  Block of code to handle errors
}
```

Consider the following example, where we create an array of three integers:

> This will generate an error, because myNumbers`[10]` does not exist.

```
int[] myNumbers = {1, 2, 3};
Console.WriteLine(myNumbers[10]); // error!
```
The error message will be something like this:
```
System.IndexOutOfRangeException: 'Index was outside the bounds of the array.'
```

> If an error occurs, we can use `try...catch` to catch the error and execute some code to handle it.

> In the following example, we use the variable inside the catch block `(e)` together with the built-in `Message` property, which outputs a message that describes the exception:

Example
```csharp
try
{
  int[] myNumbers = {1, 2, 3};
  Console.WriteLine(myNumbers[10]);
}
catch (Exception e)
{
  Console.WriteLine(e.Message);
}
```

The output will be:
```
Index was outside the bounds of the array.
```
You can also output your own error message:

Example
```csharp
try
{
  int[] myNumbers = {1, 2, 3};
  Console.WriteLine(myNumbers[10]);
}
catch (Exception e)
{
  Console.WriteLine("Something went wrong.");
}
```
The output will be:
```
Something went wrong.
```

## Finally

> The `finally` statement lets you execute code, after `try...catch`, regardless of the result:

Example
```csharp
try
{
  int[] myNumbers = {1, 2, 3};
  Console.WriteLine(myNumbers[10]);
}
catch (Exception e)
{
  Console.WriteLine("Something went wrong.");
}
finally
{
  Console.WriteLine("The 'try catch' is finished.");
}
```
The output will be:
```
Something went wrong.
The 'try catch' is finished.
```

## The throw keyword

> The throw statement allows you to create a custom error.

> The throw statement is used together with an `exception class`.

> There are many exception classes available in C#:

> - `ArithmeticException`
> - `FileNotFoundException`
> - `IndexOutOfRangeException`
> - `TimeOutException`
> - `etc:`

Example
```csharp
static void checkAge(int age)
{
  if (age < 18)
  {
    throw new ArithmeticException("Access denied - You must be at least 18 years old.");
  }
  else
  {
    Console.WriteLine("Access granted - You are old enough!");
  }
}

static void Main(string[] args)
{
  checkAge(15);
}
```
The error message displayed in the program will be:
```
System.ArithmeticException: 'Access denied - You must be at least 18 years old.'
```
If age was 20, you would not get an exception:

Example
```
checkAge(20);
```

The output will be:
```
Access granted - You are old enough!
```

# UML DIAGRAM

```csharp
using System.Security.Cryptography.X509Certificates;
 
public class Shape
{
    protected Location c;
 
    public string ToString()
    {
        return string.Empty;
    }
 
    public double Area()
    {
        return 0.000;
    }
 
    public double Perimeter()
    {
        return 0.000;
    }
}
 
public class Location
{
    private double x, y;
    public double X { get { return x; } set { x = value; } }
    public double Y
    {
        get { return y; }
        set { y = value; }
    }
}
 
    public class Rectangle : Shape
    {
        protected double side1, side2;
 
        public Rectangle(double side1, double side2)
        {
            this.side1 = side1;
            this.side2 = side2;
        }
        public double Side1 { get { return side1; } set { side1 = value; } }
        public double Side2 { get { return side2; } set { side2 = value; } }
        public double Area()
        {
            return this.side1 * this.side2;
        }
        public double Perimeter()
        {
            return 2 + (this.side1 + this.side2);
        }
        public void ToString()
        {
        Console.WriteLine("RECTANGLE PROPERTIES");
            Console.WriteLine($"Area is {Area()}");
            Console.WriteLine($"Perimeter is {Perimeter()}");
        }
 
    }
 
    public class Circle : Shape
    {
        protected double radius;
        public Circle(double radius)
        {
            this.radius = radius;
 
        }
        public double Radius { get { return radius; } set { radius = value; } }
 
        public double Area()
        {
            return Math.PI * (radius * radius);
        }
        public double Perimeter()
        {
            return 2 * Math.PI * radius;
        }
        public void ToString()
        {
        Console.WriteLine("CIRCLE PROPERTIES:");
            Console.WriteLine($"Area is {Area()}");
            Console.WriteLine($"Perimeter is {Perimeter()}");
        }
    }
 
    public class ShapeTest
    {
        public static void Main(string[] args)
        {
            Circle c1 = new Circle(3.45);
            c1.ToString();
            Rectangle r1 = new Rectangle(5.67, 10.5);
            r1.ToString();
        Console.ReadKey();
        }
    }
    
    ```