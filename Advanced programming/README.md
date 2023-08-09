# Advanced programming
  - question #1
    1. Write a program that takes a string and counts and displays the number of English vowels ( English vowels : a,e,i,o,u )
    2. Write a program that takes the name of the month of the year and determines the number of days
    3. Write a program that takes and displays a list of 5 marks
       - guidance : Implement in two ways
          1. Implement bubble sort yourself
          2. Use Python's lists method to sort
    
  - question #2
    1. Write a function that takes a list of numbers and returns the unique digits of that list (remove duplicates)
       - Sample List : [1,2,3,3,3,3,4,5]
       - Uniqe List : [1,2,3,4,5]
    2. Write a function that displays n rows of Pascal's triangle after receiving n
    3. Write a function that takes a string whose words are separated by dashes and returns a string whose words are sorted alphabetically.
       - Sample items : green-red-yellow-black-white
       - Expected Result : black-green-red-white-yellow

  - question #3
     - Convert the members of the following list to a dictionary in such a way that the words in list be the key and the value of each member shows the count of words.
       
        words = [ 'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes', 'white', 'black', 'orange', 'pink' , 'pink', 'red', 'red', 'white', 'orange',                       'white', "black", 'pink', 'green', 'green', 'pink', 'green', ' pink', 'white', 'orange', 'orange', 'red']
       
        Then find and display the word that has the most and least repetition.
  
  - question #4

    questions are in the jupyter notebook

  - question #5
    
    Define and call functions for each of the data types and data structures and specify which parameters are pass by reference and which are pass by value.
    List of items to be tested:
      - integer and float variable
      - dictionary
      - tuple
      - set
      - list
      - string
        
  - question #6

    - Encoder program on string: <br>
        write a program that takes a string from the user and turns it into a password; Also, if it receives a password, convert it to a string. <br>
        
        Example:
        `nima`'s string input should be: <br>
        Password: ojnb <br>
        Algorithm: Every character in the English alphabet is changed from `n` to `o` or `i` to `j` <br>
        
        Second example: <br>
        
        Input: nima <br>
        Password: a:d/fcojnb <br>
        Algorithm: First, a:d/fc string is added for each type of string that we understand is a secret string, then the same ojnb password

- question #7

  - Write a function that takes a string and prints it as a banner
   
- question #8
    
  - The problem of 8 queens <br>
              The problem of 8 queens is an old and famous question in computer science.
              The question is how to place 8 queens on an 8 x 8 chessboard so that they do not threaten each other?

- question #9
    
    - Hanoi towers problem:
      
        As in the figure, we have three bars. One of the bars is the origin bar (A), the other is the auxiliary bar (B) and the other is the destination bar (C). The            goal is to transfer all disks from the origin bar to the destination bar with the following conditions:
          - Only one disk can be moved at a time
          - A disc should never be placed on top of a smaller sized disc.
         
        Write a program that works for n disks.
        It means that, there are n disks inside the rod A
        Show the transfer steps from A to C.
        ![Watch the video](https://preview.redd.it/c8fyjo37cwr21.gif?width=1021&auto=webp&s=b58f91e5482bb4086acd3b729ac11d4fab52e971)

- question #10
  
  - A class implementation for rational numbers <br>
      -  Attributes of the class include numerator and denominator of the rational number
      
      Implement a method for: <br>
        🎗 Adding two numbers <br>
        🎗 Dividing two numbers <br>
        🎗 Multiplication of two numbers <br>
        🎗 Subtraction of two numbers <br>
      
      Also, a class attribute that keeps the number of created objects

- question #11

  - New exercise for subject of multiple inheritance
        
    🎗 Define a class called triangle to implement the example, which has attributes such as the size of the sides and height, and methods to calculate the                     perimeter and area.
        
    🎗 A class called square to implement the square which has the attribute of side size and methods to calculate perimeter and area
            
    🎗 A class called pyramid is used to implement the pyramid, which inherits its attributes and methods from the previous two classes, and it has a method to                  calculate the area and volume of the pyramid, but it does this by calling the methods inherited from the base classes.
            
    - Note that the constructor of the pyramid class receives all the inherited attributes and sets them by calling the constructor of the base classes.

- question #12

  🎗 class of two numbers

  Create a class with two numeric members a and b Member functions required for:
     
  - Initialization,
  - Reading values ​​from input for a , b ,
  - Calculate a+b,
  - Calculate a^b,
  - determine the larger number,
  - Factorial calculation b
         
- question #13

  The goal is to implement large integers using arrays: <br>
  
    * 1 - Initializing the numbers, and overloading the necessary constructors <br>
    * 2 - Necessary methods for calculating factorial, calculating absolute value (abs) and power. Exponent contains an input, which can be an `int` or `long int`,              that sets the calling object to its exponent. <br>
    * 3 - A function to perform addition between two Huge_int <br>
    * 4 - A function to compare between two Huge_int

- question #14

  🎗 Define a class with its member functions to hold the grades of the candidates (each student has his own grades and a maximum of 10 grades).
  
    * Write a member function that displays the code of students who have passed all courses.
    * Write a member function that displays the code of conditional students.
      
   Note : The constructor must be used in this class.

- question #15
  🎗 Exercise: Sparse matrix class
  
  Define a class for an n*3 matrix. The constructor of the class must specify n when creating the matrix object so that the matrix is ​​created dynamically. Then          perform the necessary member functions to fill the matrix, display the matrix information, reconstruct the initial matrix from the sparse matrix.
  
  ![figure 1](https://github.com/nimarasi/Undergraduate_projects/assets/80810639/b100ec0e-06ac-4b0f-8d3f-6368027bd7b2)
  ![figure 2](https://github.com/nimarasi/Undergraduate_projects/assets/80810639/e9c87980-c252-4458-bf1d-5cf284a238ed)


- final project
  
  🎯 End of semester project 🎯
  
  Language: Python or cpp <br>
  Goal: Implementation of the space shooter game <br>
  Basic limitation: 100% object oriented

  Mandatory items:
  
  🎯 Implementing the movement of the ship with WASD keys and not leaving the ship from the game box and shooting with X
  
  🎯 Display score and elapsed time of the game On the side of the page
  
  🎯 Implementation of background movement and time passage
  
  🎯 Each obstacle has 3 lives(It means that it won't explode until it is shot twice)
  
  🎯 The ship loses lives due to collision with obstacles
  
  🎯 Over time, the obstacles come down and the user has to shoot to advance the game

  Optional items:

  🎯 By increasing the user's score (destroying most of the obstacles), the bullets fired by the ship will be doubled, that is, first, one bullet will be fired for
      every 10 points; 2 bullets for 20 points; 4 bullets and until the end
    
  🎯 Changing colors of obstacles and using colors correctly

  🎯 Change the shape of the obstacles in each stage

  🎯 Shoot the obstacles towards the ship
  
  Note: It is possible to use any Python module
  
  ![figure 3](https://github.com/nimarasi/Undergraduate_projects/assets/80810639/81481344-2079-4001-a9aa-aad31d38dec1)
