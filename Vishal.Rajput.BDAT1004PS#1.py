#!/usr/bin/env python
# coding: utf-8

# # Question 1 C# What data type is each of the following?

# In[ ]:


#answer 1

5         integer
5.0       double
5 > 1     Relational/comparison operator 
'5'       Character
5 * 2     Arithmatic operator 
'5' * 2   Arithmatic operator 
'5' + '2' Arithmatic operator
5 / 2     Arithmatic operator
5 % 2     Arithmatic operator
{5, 2, 1} Array
5 == 3    Assignment operator
Pi(the number) math operator


# # Question 2 C#
# 
# Write (and evaluate) C# expressions that answer these questions: a. How many letters are there in 'Supercalifragilisticexpialidocious'? b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? c. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn? d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
# 

# In[ ]:


#answer 2a

string word ="Supercalifragilisticexpialidocious";
int countofletters = word.Length;
Console.WriteLine(countofletters);


# In[ ]:


# output : 34


# In[ ]:


#answer 2b

string word ="Supercalifragilisticexpialidocious";
string substring ="ice";
bool containsubstring = word.Contains(substring);
Console.WriteLine(containsubstring);


# In[ ]:


# output : True


# In[ ]:


#answer 2c


string wordone = "Supercalifragilisticexpialidocious";
string wordtwo = "Honorificabilitudinitatibus";
string wordthree = "Bababadalgharaghtakamminarronnkonn";

                   if (wordone.Length>wordtwo.Length)
                   {
                        if (wordone.Length>wordthree.Length)
                        {
                              Console.WriteLine("{0} is the largest", wordone);
                        }
                        else
                        {
                               Console.WriteLine("{0} is the largest", wordthree);
                        }
                   }
                   else
                   {
                        if (wordtwo.Length>wordthree.Length)
                        {
                              Console.WriteLine("{0} is the largest", wordtwo);
                        }
                        else
                       {
                               Console.WriteLine("{0} is the largest", wordthree);
                       }
                   }


# In[ ]:


# output : Bababadalgharaghtakamminarronnkonn is the largest


# In[ ]:


#answer 2d

SortedDictionary<string, string> names = new SortedDictionary<string, string>(); 
           names.Add("3", "Berlioz"); 
           names.Add("5", "Borodin");
           names.Add("6", "Brian");
           names.Add("1", "Bartok"); 
           names.Add("2", "Bellini");
           names.Add("7", "Buxtehude");
           names.Add("4", "Bernstein");
           foreach (KeyValuePair<string, string> kv in names)
           {
                 Console.WriteLine(kv.Key + " " + kv.Value);
                 
           }


# In[ ]:


# output :

1 Bartok
2 Bellini
3 Berlioz
4 Bernstein
5 Borodin
6 Brian
7 Buxtehude


# # Question 3 C#
# 
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b, and c iss(s - a)(s - b)(s - c) , wheres = (a + b + c)/2 .
# 
#             triangleArea(2,2,2) 1.7320508075688772
# 
# 

# In[ ]:


using System;

class Triangle
{
    public double a;
    public double b;
    public double c;

    public double GetArea()
    {
        double s = (a + b + c) / 2;
        return Math.Sqrt(s * (s - a) * (s - b) * (s - c));
    }

    public void Display()
    {
        Console.WriteLine("Side 1: {0}", a);
        Console.WriteLine("Side 2: {0}", b);
        Console.WriteLine("Side 3: {0}", c);
        Console.WriteLine("Area: {0}", GetArea());
    }
}

class ExecuteTriangle
{
    static void Main(string[] args)
    {
        Triangle t = new Triangle();
        t.a = 2;
        t.b = 2;
        t.c = 2;
        t.Display();
        Console.ReadLine();
    }
}


# In[ ]:


# output : 
Side 1: 2
Side 2: 2
Side 3: 2
Area: 1.7320508075688772


# # Question 4 C#
# 
# Write a program in C# Sharp to separate odd and even integers in separate arrays. Go to the editor Test Data : Input the number of elements to be stored in the array :5 Input 5 elements in the array : element - 0 : 25 element - 1 : 47 element - 2 : 42 element - 3 : 56 element - 4 : 32 Expected Output: The Even elements are: 42 56 32 The Odd elements are : 25 47
# 

# In[ ]:


using System;

public class Program
{
    public static void Main()
    {
        Console.WriteLine("Input the number of elements to be stored in the array: ");
        int count = Convert.ToInt32(Console.ReadLine());

        int[] numbers = new int[count];
        int[] evenNumbers = new int[count];
        int[] oddNumbers = new int[count];
        int evenIndex = 0;
        int oddIndex = 0;

        Console.WriteLine($"Input {count} elements in the array:");
        for (int i = 0; i < count; i++)
        {
            Console.Write($"element - {i}: ");
            numbers[i] = Convert.ToInt32(Console.ReadLine());

            if (numbers[i] % 2 == 0)
            {
                evenNumbers[evenIndex] = numbers[i];
                evenIndex++;
            }
            else
            {
                oddNumbers[oddIndex] = numbers[i];
                oddIndex++;
            }
        }

        Console.Write("The Even elements are: ");
        for (int i = 0; i < evenIndex; i++)
        {
            Console.Write(evenNumbers[i] + " ");
        }

        Console.WriteLine();

        Console.Write("The Odd elements are: ");
        for (int i = 0; i < oddIndex; i++)
        {
            Console.Write(oddNumbers[i] + " ");
        }

        Console.WriteLine();
    }
}


# In[ ]:


# output :

Input the number of elements to be stored in the array:
5
Input 5 elements in the array:
element - 0: 12
element - 1: 11
element - 2: 10
element - 3: 6
element - 4: 4
The Even elements are: 12 10 6 4
The Odd elements are: 11


# # Question 5 C#
# 
# a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).
# 
#             inside(1,1,0,0,2,3) True inside(-1,-1,0,0,2,3) False 
# 
#     b. Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).
# 
# 

# In[2]:


#answer 5a

using System;

public class MainClass
{
    // Main method
    public static void Main(string[] args)
    {
        // Declared variables and initialized bottom-left corner coordinates
        int x1 = 0, y1 = 0;

        // Declared variables and initialized top-right corner coordinates
        int x2 = 2, y2 = 3;

        // Declared variables and initialized point value which needs to be checked
        int x = 1, y = 1;

        // Calling the Inside function by passing all the point values as parameters
        if (Inside(x, y, x1, y1, x2, y2))
            Console.WriteLine("True");
        else
            Console.WriteLine("False");
    }

    // Function to check whether a given point lies inside a rectangle or not
    static bool Inside(int x, int y, int x1, int y1, int x2, int y2)
    {
        // If it satisfies the condition
        if (x > x1 && x < x2 && y > y1 && y < y2)
        {
            // Then return true
            return true;
        }

        // Else return false
        return false;
    }
}


# In[ ]:


# output : True


# In[ ]:


#answer 5b

using System;

public class MainClass
{
    // Main method
    public static void Main(string[] args)
    {
        // Rectangle 1
        double x1Rect1 = 0.3, y1Rect1 = 0.5;
        double x2Rect1 = 1.1, y2Rect1 = 0.7;

        // Rectangle 2
        double x1Rect2 = 0.5, y1Rect2 = 0.2;
        double x2Rect2 = 1.1, y2Rect2 = 2;

        // Point
        double x = 1, y = 1;

        // Check if the point lies in both rectangles
        bool isInsideBothRectangles = Inside(x, y, x1Rect1, y1Rect1, x2Rect1, y2Rect1) &&
                                      Inside(x, y, x1Rect2, y1Rect2, x2Rect2, y2Rect2);

        // Print the result
        if (isInsideBothRectangles)
            Console.WriteLine("The point (1, 1) lies in both rectangles");
        else
            Console.WriteLine("The point (1, 1) does not lie in both rectangles");
    }

    // Function to check whether a given point lies inside a rectangle or not
    static bool Inside(double x, double y, double x1, double y1, double x2, double y2)
    {
        // If it satisfies the condition
        if (x >= x1 && x <= x2 && y >= y1 && y <= y2)
        {
            // Then return true
            return true;
        }

        // Else return false
        return false;
    }
}


# In[ ]:


# output : The point (1, 1) does not lie in both rectangles


# # Question 6 Python
# 16. You can turn a word into pig-Latin using the following two rules (simplified):
# • If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pig-
# Latin form. Your function should still work if the input word contains upper case
# characters. Your output should always be lower case however.
# >>> pig('happy')
# 'appyhay'
# >>> pig('Enter')
# 'enterway'

# In[2]:


def pig(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Convert the word to lowercase
    word = word.lower()

    # Check if the word starts with a vowel
    if word[0] in vowels:
        return word + 'way'

    # Move the first consonant to the end and append 'ay'
    for i in range(len(word)):
        if word[i] not in vowels:
            return word[i:] + word[:i] + 'ay'

        
        print(pig('happy')) 
        print(pig('Enter')) 




# # Question 7 Python
# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.
# Write a function bldcount() that reads the file with name name and reports (i.e.,
# prints) how many patients there are in each bloodtype.
# >>> bldcount('bloodtype.txt')
# There are 10 patients of blood type A.
# There is one patient of blood type B.
# There are 10 patients of blood type AB.
# There are 12 patients of blood type O.
# There are no patients of blood type OO.

# In[18]:


def bldcount(filename):
    blood_types = {'A': 0, 'B': 0, 'AB': 0, 'O': 0, 'OO': 0}

    with open(filename, 'r') as file:
        for line in file:
            blood_type_list = line.strip().split()
            for blood_type in blood_type_list:
                blood_types[blood_type] += 1

    for blood_type, count in blood_types.items():
        if count == 1:
            print(f"There is one patient of blood type {blood_type}.")
        elif count == 0:
            print(f"There is no patient of blood type {blood_type}.")
        else:
            print(f"There are {count} patients of blood type {blood_type}.")

bldcount('C:\\Users\\Gurpreet singh sethi\\OneDrive\\Desktop\\bloodtype1.txt')


# # Question 8 Python
# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or
# 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.
# >>> curconv('EUR', 100)
# 122.96544
# >>> curconv('JPY', 100)
# 1.241401
# The currency rates you will need are stored in file currencies.txt
# 
# 

# In[19]:


def curconv(currency, amount):
    with open('C:\\Users\\Gurpreet singh sethi\\OneDrive\\Desktop\\currencies.txt', 'r') as file:
        for line in file:
            parts = line.split()
            if parts[0] == currency:
                rate = float(parts[1])
                usd_amount = amount * rate
                return usd_amount

    return None

usd_amount = curconv('EUR', 100)
if usd_amount is not None:
    print(usd_amount)
else:
    print("Currency not found")

usd_amount = curconv('JPY', 100)
if usd_amount is not None:
    print(usd_amount)
else:
    print("Currency not found")


# # Question 9
# 
# Each of the following will cause an exception (an error). Identify what type of
# exception each will cause.
# Trying to add incompatible variables, as in
# adding 6 + ‘a’
# Referring to the 12th item of a list that has only 10
# items
# Using a value that is out of range for a function’s
# input, such as calling math.sqrt(-1.0)
# Using an undeclared variable, such as print(x)
# when x has not been defined
# Trying to open a file that does not exist, such as
# mistyping the file name or looking in the wrong
# directory.

# In[ ]:


#Answer a : Trying to add incompatible variables, as in adding 6 + 'a':
This will cause a TypeError.The interpreter will raise an error because it is not possible to add an integer (6) and
a string ('a') together.
    
#Answer b : Referring to the 12th item of a list that has only 10 items:    
This will cause an IndexError. The interpreter will raise an error because the index provided (12) is out of range for
the given list. Since the list has only 10 items, valid indices range from 0 to 9.


#Answer c : Using a value that is out of range for a function's input, such as calling math.sqrt(-1.0):
This will cause a ValueError. The math.sqrt() function expects a non-negative number as its input, so passing a negative 
value (-1.0) will raise an exception. Square roots of negative numbers are not defined in real numbers, hence the ValueError.

#Answer d : Using an undeclared variable, such as print(x) when x has not been defined:
This will cause a NameError. The interpreter will raise an exception because the variable 'x' has not been declared or assigned 
any value. Trying to use an undefined variable will result in a NameError.

#Answer e : Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory:
This will cause a FileNotFoundError (or IOError in some cases). If the file specified in the code does not exist or if there is
an error in the file name or directory path, attempting to open the file will raise an exception indicating that the file was
not found.


# # Question 10 Python
# Encryption is the process of hiding the meaning of a text by substituting letters in the
# message with other letters, according to some system. If the process is successful, no
# one but the intended recipient can understand the encrypted message. Cryptanalysis
# refers to attempts to undo the encryption, even if some details of the encryption are
# unknown (for example, if an encrypted message has been intercepted). The first step
# of cryptanalysis is often to build up a table of letter frequencies in the encrypted text.
# Assume that the string letters is already defined as
# 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()
# that takes a string as its only parameter, and returns a list of integers, showing the
# number of times each character appears in the text. Your function may ignore any
# characters that are not in letters.
# >>> frequencies('The quick red fox got bored and went home.')
# [1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2,
# 1, 0, 1, 1, 0, 0]
# >>> frequencies('apple')

# In[1]:


def frequencies(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    frequency_list = [0] * len(letters)  # Initialize a list of zeros with the length of letters

    # Iterate over each character in the text
    for char in text.lower():
        if char in letters:
            # Increment the count for the corresponding character in the frequency list
            index = letters.index(char)
            frequency_list[index] += 1

    return frequency_list

print(frequencies('The quick red fox got bored and went home.'))
# Output: [1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0]

print(frequencies('apple'))
# Output: [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

