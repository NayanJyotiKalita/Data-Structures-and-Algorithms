# OOPs Basics - 4

## Consider the following code

### Java
```java
class Student {
   int age;
   String name;

   void display(){
       System.out.println("My name is " + this.name + ". I am "  + this.age + " years old");
   }
}

public class Client {
   public static void main(String[] args) {
       Student s1 = new Student();
       s1.age = 10;

       Student s2 = s1;

       s2.display();
   }
}
```

### Python
```python
class Student:
    def __init__(self):
        self.age = 0
        self.name = none

    def display(self):
        print("My name is", self.name + ". I am", self.age, "years old")


# Main code
s1 = Student()
s1.age = 10

s2 = s1

s2.display()
```

### JS
```javascript
class Student {
    constructor() {
        this.age = 0;
        this.name = null;
    }

    display() {
        console.log(`My name is ${this.name}. I am ${this.age} years old`);
    }
}

const s1 = new Student();
s1.age = 10;

const s2 = s1;

s2.display();
```

## What is the output of the final call to display function?

### Choose the correct answer from below:

  - My name is A. I am 10 years old.

  - My name is null. I am 0 years old.

  - My name is null. I am 10 years old.

  - My name is A. I am 0 years old.

---

# Answer
*My name is null. I am 10 years old.*
