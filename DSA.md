
# Variables and Primitive Data Types in Programming

>In programming, variables are used to store and manipulate data. Data types define the type of data a variable can hold. Here are some common primitive data types:

## INT (Integer)
>An int is used to store whole numbers. It can be both positive and negative.

```Python
int age = 25;
```

## FLOAT (Floating-Point)
>A float is used to store numbers with a decimal point. It represents real numbers.

```Python
float price = 19.99;
```

## DOUBLE (Double-Precision Floating-Point)
>A double is similar to a float, but it can store more significant digits with higher precision.

```python
double pi = 3.14159265359;
```

## DECIMAL
>The decimal type is used for high-precision decimal arithmetic, often used in financial calculations.

```python
decimal bankBalance = 1000000.50M;
```
## STRING
>A string is used to store a sequence of characters, such as text.

```python
string name = "John";
```
## BOOL (Boolean)
>A bool represents a binary value: true or false. It's used for logical operations.

```python
bool isStudent = true;
```

>These are some fundamental data types used in programming. The specific syntax may vary depending on the programming language you're using, but the concepts remain consistent across most languages.

# Sample Code for Variables and Primitive Data Types
```csharp
using System;

namespace VariableAndType
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 2;
            Console.WriteLine("The Value of x Variable is "+ x);

            x = 5;
            Console.WriteLine("The value of x variable is " + x);

            double double_var = 0.0;
            float float_var = 0.0f;
            decimal decimal_var = 0.0m;

            double_var = 9.8;
            float_var = 5.10f;
            decimal_var = 100.145m;

Console.WriteLine("Double Var: " + double_var + " Float Var: " + float_var + " Decimal Var: " + decimal_var);
           
            //string firstname = "John";
            //string lastname = "Wick";

            string firstname, lastname, address;
            firstname = "John";
            lastname = "Wick";
            address = "Duon lng";

//Console.WriteLine("Firstname: " + firstname + " Lastname: " + lastname);

Console.WriteLine(String.Format("Firstname: {0} Lastname: {1} Address: {2}", firstname, lastname, address));
            

            Console.ReadLine();
        }
    }
}
```

## Convert and Type Casting
```csharp
using System;

namespace VariableAndType
{
    class Program
    {
        static void Main(string[] args)
        {
            int serialNo = 150;
            string accountNo = "";
            accountNo = serialNo.ToString();
            Console.WriteLine(accountNo);

            float myFloat = 5.3f;
            accountNo = myFloat.ToString();
            //serialNo = Convert.ToInt32(myFloat); (Convert)
            serialNo = (int)myFloat;  //(Type Casting)

            decimal money1 = 45.65m;
            decimal money2 = 1001.53m;
            decimal result = Convert.ToInt32 (money1 + money2);

            Console.WriteLine(result.ToString("#,##0.00"));
            Console.ReadLine();


        }        }    }   
```

# Sample Code for Comparison Operators
```csharp
using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {

        int x = 0;
        int y = 0;

        Console.WriteLine("Enter a number: ");
        x = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter a number: ");
        y = int.Parse(Console.ReadLine());

        if(x < y)
        {
            Console.WriteLine("x Less than y");
        }
        else
        {
            Console.WriteLine("x is not Less than y");
        }

        if(x > y)
        {
            Console.WriteLine("x Greater than y");
        }
        else
        {
            Console.WriteLine("x is not Greater than y");
        }

        if(x != y)
        {
            Console.WriteLine("x is Equal to y");
        }
        else
        {
            Console.WriteLine("x is not Equal y");
        }

        if(x <= y)
        {
            Console.WriteLine("x less than y or equal to y");
        }
        else
        {
            Console.WriteLine("x is not less than y or equal to y");
        }

        Console.ReadLine();

       }
    }
}       
```

# Logical Operators in C#
>Logical operators are essential components of programming languages used for making decisions and performing conditional actions. There are three common logical operators:

* AND (&&): This operator returns true only if both operands are true. In Markdown, you can represent it as &&.

* OR (||): The OR operator returns true if at least one of the operands is true. In Markdown, it is represented as ||.

* NOT (!): The NOT operator negates the truth value of an operand. Markdown uses the exclamation mark ! to denote it.

These operators play a crucial role in controlling program flow, enabling you to create conditional statements and complex decision-making processes in your code.
```csharp
using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {

            int age = 0;
            Console.WriteLine("Enter your age: ");
            age = int.Parse(Console.ReadLine());

            if (age >= 0 && age <=2)
            {
                Console.WriteLine("Infant");
            }else if (age >= 3 && age <=5)
            {
                Console.WriteLine("Toddler");
            }
            else if (age >= 6 && age <=12)
            {
                Console.WriteLine("Kid");
            }
            else if (age >= 13 && age <= 19)
            {
                Console.WriteLine("Teen");
            }
            else if (age >= 20 )
            {
                Console.WriteLine("Adult");
            }
            Console.ReadLine();

        }
    }
}       
```
# Switch Statement in C#

A `switch` statement is a control flow statement in C# that allows you to select one of several code blocks to execute based on the value of an expression. It provides a concise way to handle multiple possible cases or conditions, making your code more readable and maintainable.
 ```csharp
 using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {

            int day = 0;
            Console.Write("Enter a day [1-7]: ");
            day = int.Parse(Console.ReadLine());

            switch (day)
            {
                case 1:
                    Console.WriteLine("Monday");
                    break;
                case 2:
                    Console.WriteLine("Tuesday");
                    break;
                case 3:
                    Console.WriteLine("Wednesday");
                    break;
                case 4:
                    Console.WriteLine("Thursday");
                    break;
                case 5:
                    Console.WriteLine("Friday");
                    break;
                case 6:
                    Console.WriteLine("Saturday");
                    break;
                case 7:
                    Console.WriteLine("Sunday");
                    break;
            }

            Console.ReadLine();

        }
    }
}       
```
## While Statement
> `while` is a loop statement that executes a block of lines of code whenever the condition is true

```csharp
using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {
            int x = 0;  
           while (x < 10)
            {
                Console.WriteLine(string.Format("{0}. I am Learning c#",x)); 
                x = x + 1;
               
            }
           Console.ReadLine();
        }
    }
}       
```
# For statement
>`for` is a loop statement that executes a block of codes in a specific number of repetition
```csharp
using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {
            for (int i = 10; i >= 1; i--)
            { 
                Console.WriteLine("{0} I am learning c#",i);
            }
            Console.ReadLine();
        }
    }
}       
```
# Do while statement
>The do while statement is written at the buttom of the code.

```csharp
using System;

namespace VariableAndType



{
    class Program
    {
        static void Main(string[] args)
       {
            //Do while loop statement
            Console.WriteLine("Do while loop");
            int n = 100;
            do
            {
                Console.WriteLine("{0} I am learning c#", n);
                n++;
            } while (n <= 10);


            //=============================
            Console.WriteLine("");
            Console.WriteLine("While Loop");
            int i = 0;
            while (i <= 10)
            {
                Console.WriteLine("");
                Console.WriteLine("{0} I am learning c#", i);
                i++;
            }
                Console.ReadLine();
        }
    }
}       
```
# Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly selecting the minimum element from an unsorted portion of the list and moving it to the sorted portion. Here's a basic implementation in C#:

```csharp
public static void SelectionSort(int[] arr)
{
    int n = arr.Length;

    for (int i = 0; i < n - 1; i++)
    {
        int minIndex = i;

        // Find the index of the minimum element in the unsorted part of the array
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }

        // Swap the found minimum element with the first element
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}
```
# Insertion Sort in C#

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the array. Here's a basic implementation in C#:

```csharp
public static void InsertionSort(int[] arr)
{
    int n = arr.Length;

    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;

        // Move elements of the sorted portion that are greater than the key
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        // Insert the key into its correct position in the sorted portion
        arr[j + 1] = key;
    }
}
```

# Data Structures and Algorithms

## Quick Sort
- A Divide and Conquer sorting algorithm.
- Partitions using a random pivot item x.
- Sorts both partitions recursively, cost is T(p) + T(n – p).
- Concatenates the two sorted partitions in O(1) time.
- Partition can be done in linear time (Θ(n)).
- Ideal pivot is the median item, but finding the true median is difficult.
- A good estimate for the true median is a sample median.
- Worst-case: Θ(n^2).
- Best-case: Θ(n log n).
- Average case with random pivot: Θ(n log n).
- Improvements: Choose median of a small sample as pivot, stop recursion earlier.

## Classification of 4 Sorting Algorithms
- Quick Sort
- Quick Select
- Lomuto Partition
- Hoare Partition

## Quick Select
- Used to find the kth smallest (or largest) element in an unordered list or array.
- Average-case time complexity: O(n).
- Worst-case time complexity: O(n^2).
- Strategies to mitigate worst-case: Choose a good pivot element, like "median-of-medians."

### Idea Behind Quick Select
- Select a "pivot" element and partition the list.
- Elements smaller than pivot on the left, larger on the right.
- If pivot's index is k, return pivot as the kth smallest element.
- If k < pivot's index, repeat on left partition; else, repeat on right.

### Algorithms for Finding a Good Pivot
- Lomuto Partition
- Hoare Partition

### Applications of Quick Select
1. Finding Medians.
2. Order Statistics.
3. Partial Sorting.

## Median-of-Medians Algorithm
- Divides array items into groups of 5.
- Partitions each group of 5 using the median.
- Further partitions using the median of these medians.
- T(n) = T(n/5) + O(n).
- MOM is greater than (0.3n+5)/10 items and less than (0.3n+5)/10 items.

## Heap Sort
- A comparison-based, in-place, unstable sorting algorithm.
- Proposed by J. W. J. Williams in 1964, refined by Robert W. Floyd in 1965.
- Uses a binary heap data structure for efficient sorting.

### Heap Sort in Action
1. Build a complete binary tree from the array.
2. Transform into a max heap (parent node >= child nodes).

# Data Structures and Algorithms

## Data Structure

A data structure is a way of organizing and storing data in a computer's memory or storage system so that it can be efficiently accessed, manipulated, and utilized. The choice of data structure can significantly impact the efficiency and effectiveness of various operations performed on the data, such as insertion, deletion, search, and sorting.

The common data structures include:

- Array
- Linked List
- Stacks
- Queues
- Trees
- Graphs
- Hash Tables
- Heaps

## Algorithms

An algorithm is a step-by-step procedure or set of rules that outline how to perform a specific task or solve a particular problem. It's a well-defined sequence of instructions designed to achieve a certain goal or produce a desired output from given inputs. Algorithms are used in various fields of study, including mathematics, computer science, engineering, and other scientific disciplines.

Key characteristics of algorithms include:

- Well-Defined Inputs and Outputs: The inputs and outputs should be clearly defined so that the algorithm's behavior is predictable.
- Clear and Unambiguous Steps: Each step of the algorithm must be unambiguous and clearly defined, leaving no room for interpretation.
- Finiteness: An algorithm must eventually terminate after a finite number of steps. It should not run indefinitely, or else it would not be useful for practical purposes.
- Effective Computability: The steps of an algorithm should be feasible to perform using available computational resources.
- Determinism: An algorithm's steps are deterministic, meaning that given the same inputs and executed under the same conditions, it will always produce the same output.

## Data Structures and Algorithms Course Topics

This course covers a wide range of topics, including:

- Design and analysis of algorithms and data structures
- Mathematical analysis of iterative and recursive algorithms
- Correctness, running time, and storage requirements of algorithms
- Algorithm design paradigms, including divide-and-conquer, dynamic programming, greedy algorithms, and more
- Linear structures like skip lists, hashing, and bloom filters
- Various search trees and priority trees, including balanced trees, multi-way search trees, and heaps
- Algorithms on graphs, multigraphs, and hypergraphs, covering spanning trees, path problems, matching, network flows, network routing, and their applications.

## Analyzing Algorithms

When analyzing algorithms, we consider various aspects:

- Correctness: Ensuring the algorithm produces the correct output with respect to the problem specifications.
- Running Time: Determining how the algorithm's performance scales with the input size.
- Storage Requirements: Assessing the amount of memory or storage space needed.
- Trade-offs: Recognizing that optimizing one aspect may impact others, such as using more time to improve accuracy or using more space to speed up execution.

## Algorithm Specification and Derivation

Formal specifications are crucial for understanding and solving problems effectively. Specifications clarify the problem's requirements and can even assist in algorithm derivation. For instance:

**Sample Problem:** Given an array of n pebbles colored RED, WHITE, and BLUE in random order, swap pairs of pebbles so that all the REDs are before the WHITES, and the WHITES before the BLUES.

- Precondition: The initial state of the array.
- Post-condition: The desired state of the array after swapping.

Deriving a correct and efficient algorithm involves studying the specifications, establishing a loop invariant, initializing variables, and implementing the necessary steps.

## Algorithm Analysis

Algorithm analysis focuses on evaluating an algorithm's performance in terms of:

- Correctness: Ensuring the algorithm produces accurate results.
- Running Time: Assessing how the running time scales with input size, often expressed in asymptotic notation (e.g., O(n)).
- Storage Requirements: Determining memory or storage needs.
- Parallelism: For parallel algorithms, evaluating processor utilization.

### Asymptotic Notations: Big O, Big Omega, Big Theta

- Big O: Describes the upper bound or worst-case scenario of an algorithm's running time.
- Big Omega: Describes the lower bound or best-case scenario.
- Big Theta: Indicates both upper and lower bounds, showing the tightest possible range of performance.

Asymptotic notations provide a simplified way to describe an algorithm's efficiency as input size grows large.

### Examples

Here are some examples of algorithms and their big O analysis:

- Algorithm A: T(n) = O(n^3)
- Algorithm B: T(n) = O(n^2)
- Algorithm C: T(n) = O(n)
- Algorithm D: T(n) = O(n^2)

## Recursive Algorithms and Recurrence Relations

Recursive algorithms solve problems by breaking them down into smaller instances of the same problem. The performance of recursive algorithms can often be described by recurrence relations.

For example, the factorial function:

```python
int factorial(int n) {
  if (n == 0) return 1;
  else return n * factorial(n-1);
}
```
