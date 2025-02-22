# OOP Exercises

This repository contains simple C++ programs that demonstrate basic concepts of Object-Oriented Programming (OOP).

## Files

### 1. ex1.cpp

#### Description

The `ex1.cpp` file contains a basic C++ program that prints "Hello, World!" to the console.

#### Code

```cpp
#include <iostream>  
using namespace std; 

int main() {  
    cout << "Hello, World!";  
    return 0;  
}
```

#### How to Compile and Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing `ex1.cpp`.
3. Compile the program using a C++ compiler, for example:
   ```sh
   g++ ex1.cpp -o ex1
   ```
4. Run the compiled program:
   ```sh
   ./ex1
   ```

#### Expected Output

```
Hello, World!
```

### 2. ex2.cpp

#### Description

The `ex2.cpp` file contains a C++ program that demonstrates the use of different variable types and prints their values to the console.

#### Code

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 20;  // Integer variable
    double price = 19.99;  // Double variable
    char grade = 'A';  // Character variable
    string name = "Alice";  // String variable

    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Price: $" << price << endl;
    cout << "Grade: " << grade << endl;
    
    return 0;
}
```

#### How to Compile and Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing `ex2.cpp`.
3. Compile the program using a C++ compiler, for example:
   ```sh
   g++ ex2.cpp -o ex2
   ```
4. Run the compiled program:
   ```sh
   ./ex2
   ```

#### Expected Output

```
Name: Alice
Age: 20
Price: $19.99
Grade: A
```

### 3. ex3.cpp

#### Description

The `ex3.cpp` file contains a C++ program that prompts the user to enter their name and age, and then prints a greeting message with the entered information.

#### Code

```cpp
#include <iostream>
using namespace std;

int main() {
    string name;
    int age;

    cout << "Enter your name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Hello, " << name << "! You are " << age << " years old." << endl;

    return 0;
}
```

#### How to Compile and Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing `ex3.cpp`.
3. Compile the program using a C++ compiler, for example:
   ```sh
   g++ ex3.cpp -o ex3
   ```
4. Run the compiled program:
   ```sh
   ./ex3
   ```

#### Expected Output

```
Enter your name: Alice
Enter your age: 20
Hello, Alice! You are 20 years old.
```

### 4. ex4.cpp

#### Description

The `ex4.cpp` file contains a C++ program that performs basic arithmetic operations (addition, subtraction, multiplication, division, and modulus) on two integers and prints the results.

#### Code

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;
    cout << "Sum: " << a + b << endl;
    cout << "Difference: " << a - b << endl;
    cout << "Product: " << a * b << endl;
    cout << "Quotient: " << a / b << endl;
    cout << "Remainder: " << a % b << endl;
    return 0;
}
```

#### How to Compile and Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing `ex4.cpp`.
3. Compile the program using a C++ compiler, for example:
   ```sh
   g++ ex4.cpp -o ex4
   ```
4. Run the compiled program:
   ```sh
   ./ex4
   ```

#### Expected Output

```
Sum: 13
Difference: 7
Product: 30
Quotient: 3
Remainder: 1
```

