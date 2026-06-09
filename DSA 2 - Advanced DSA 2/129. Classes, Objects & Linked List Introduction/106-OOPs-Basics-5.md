# OOPs Basics - 5

## Consider the following class Student

### Java
```java
class Student {
   int age;
   String name;

   void display(){
       System.out.println("My name is " + this.name + ". I am "  + this.age + " years old");
   }

   void sayHello(String name){
       System.out.println(this.name + " says hello to " + name);
   }
}

public class Client {
   public static void main(String[] args) {
       Student s1 = new Student();
       s1.age = 10;
       s1.name = "A";

       Student s2 = new Student();
       s2.age = 20;
       s2.name = "B";

       swap(s1, s2);

       s1.display();
   }

   private static void swap(Student s1, Student s2) {
       int tage = s1.age;
       s1.age = s2.age;
       s2.age = tage;

       String tname = s1.name;
       s1.name = s2.name;
       s2.name = tname;
   }
}
```

### Python
```python
class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", str(self.age), "years old")

    def sayHello(self, name):
        print(self.name, "says hello to", name)

def swap(s1, s2):
    tage = s1.age
    s1.age = s2.age
    s2.age = tage

    tname = s1.name
    s1.name = s2.name
    s2.name = tname

if __name__ == "__main__":
    s1 = Student()
    s1.age = 10
    s1.name = "A"

    s2 = Student()
    s2.age = 20
    s2.name = "B"

    swap(s1, s2)

    s1.display()
```

### What is the output of the final call to display function?

## Choose the correct answer from below:

  - My name is A. I am 10 years old.

  - My name is B. I am 20 years old.

  - My name is A. I am 20 years old.

  - My name is B. I am 10 years old.

---

# Answer
*My name is B. I am 20 years old*





