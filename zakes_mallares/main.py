while True:

 print("==== ACT MAJOR ====")
 print("[1] = FUNDAMENTALS TO PROGRAMMING")
 print("[2] = FUNDAMENTALS OF PROBLEM SOLVING")
 subj = int(input("Enter your Subj: "))

 print("==== FUNDAMENTALS OF PROGRAMMING ====")
 if subj == 1:
     print("\n[1] = CONDITIONAL STATEMENTS IN PYTHON")
     print("[2] = LOGICAL OPERATOR")
     print("[3] = INTRODUCTION TO ITERATION AND LOOPS")
     print("[4] = INTRODUCTION TO PROGRAMMING")
     print("[5] = BASIC SYNTAX")
     print("[6] = ARITHMETIC OPERATORS")

     topics = int(input("Choose your lesson: "))
     if topics == 1:
       print("===== CONDITIONCAL STATEMENTS IN PYTHON =====")
       print("[1] = INTRODUCTION to Conditional Statement")
       print("[2] = Relational Operators")
       print("[3] = The IF Statement")
       print("[4] = The if-else Statement")
       print("[5] = The if-elif-else Statement")
       print("")
       answer = int(input("Choose Topic: "))
       if answer == 1:
           print("===== INTRODUCTION to Conditional Statement ====")
           print("it allows a program to make decisions based on whether a condition is True or False.")
           print("EXAMPLE!")
           age = int(input("Enter Your Age: "))
           if age >= 18:
            print    ("You are an adult.")
           elif age <=18:
               print("BATA KAPA BOI!")
           else:
               print("INVALID ID")
           print("")
       elif answer == 2:
           print("==== RELATIONAL OPERATOR =====")
           print ("Relational operators also called comparison operators, are used to compare two values. The Result is always either True or False.")
           print ("EXAMPLE!")
           score = int(input("Enter your Score: "))
           if score == 75:
               print("SALAMAT SA AWA MO SIR!")
           elif score != 75:
               print("ARAY FONSO DANUM NALANG")
           elif score >= 75:
               print("PASANG UMAWA PA")
           elif score <= 75:
               print("BAKA PWEDE PANG I-TAMA ANG LAHAT, SIR.")
           else:
               print("BAWI NALANG NEXT YEAR")
               print("")
       elif answer == 3:
           print("==== The IF Statement ====")
           print("The IF Statement executes a block of code only when a condition is true.")
           print("HALIMBAWA:")
           edad = int(input("Enter your Edad: "))
           if edad >= 18:
            print    ("KATWA MUNA JO!")
           elif edad <=18:
               print("BATA KAPA BOI!")
           else:
               print("INVALID ID")
               print("")
       elif answer == 4:
           print("==== The IF-ELSE Statement =====")
           print("The else statement provides an alternative when the if condition is false.")
           print("EXAMPLE!")
           grades = int(input("Enter your Grades: "))
           if grades >= 75:
               print("PASADO KA!")
           else:
               print("BAWI NEXT YEAR!")
       elif answer == 5:
           print("==== The IF-ELIF-ELSE Statement ====")
           print("The ELIF statement is used when there are multiple conditions to evaluate.")
           print("EXAMPLE!")
           category = int(input("Enter your age: "))
           if category <= 0-12:
               print("CHILD")
           elif category >= 13-19:
               print("TEENAGER")
           elif category >= 20-59:
               print("ADULT")
           elif category >= 60:
               print("SENIOR CITIZEN")
           else:
               print("INVALID INPUT")
       else:
           print("PUMASOK KA KASI!")
     elif topics == 2:
       print("==== LOGICAL OPERATOR ====")
       print("[1] = The and Operator")
       print("[2] = The or Operator")
       print("[3] = The not Operator")
       answer = int(input("Choose Topic: "))
       if answer == 1:
           print("==== The AND Operator ====")
           print("The AND operator returns True only when ALL conditions are True.")
           print("EXAMPLE!")
           ages = int(input("Enter age: "))
           if ages >= 18 and ages <= 60:
               print("ALLOWED")
           else:
               print("NOT ALLOWED")
       if answer == 2:
           print("==== The OR Operator ====")
           print("The OR operator returns True when at least ONE condition is True.")
           print("EXAMPLE!")
           day = input("Enter your Day: ")
           if day == "Saturday" or day == "Sunday":
            print("It's ShoterDay!")
           else:
            print("It's a Regular School Day")
       if answer == 3:
           print("==== The not Operator ====")
           print("The NOT operator reverses the result of a condition.")
           print("EXAMPLE!")
           is_shoting = input("IS SHOTING?: ")
           if not is_shoting:
               print("Bring ALAK")
           else:
               print("You come here!")

     elif topics == 3:
       print("==== INTRODUCTION TO ITERATION AND LOOPS ====")
       print("[1] = Types of Loops in Phyton")
       print("[2] = Python for Loop")
       print("[3] = for Loop: Print Number 1 to 5")
       print("[4] = Counting Downward with range(): 5 to 1")
       print("[5] = Repeating a Program with while True")
       answer = int(input("Choose Topic: "))
       if answer == 1:
           print("==== Types of Loops in Phyton ====")
           print("Python has two main types of loops: for and while.")
           print("[1] = for loop")
           print("[2] = while loop")
           types = int(input("Choose types of loops: "))
           if types == 1:
               print("==== for loop ====")
               print("EXAMPLE!")
               for number in range(3):
                   print("CCST!")
           elif types == 2:
               print("==== while loop ====")
               print("EXAMPLE!")
               count = 2
               while count <= 3:
                   print("I LOVE CCST!")
                   count += 2
           else:
               print("UNAVAILABLE LOOP!")
       elif answer == 2:
           print("==== Python for Loop ====")
           print("EXAMPLE!")
           for number in range(4):
               print("Study Wells")
       elif answer == 3:
           print("==== Python while Loop ====")
           print("When count becomes 6, the condition is False and the loop stops.")
           print("Example:")
           count = 10
           while count <= 20:
               print(count)
               count += 10
       elif answer == 4:
           print("==== Counting Downward with range(): 5 to 1 ====")
           print("It counts backward.")
           print("Example:")
           number = 10
           while number >= 1:
               print(number)
               number -= 1
       elif answer == 5:
           print("==== Repeating a Program with while True ====")
           print("The program repeats until the user chooses to exit.")
           print("Example:")
           while True:
               name = input("Enter your name (X to exit): ")
               if name.upper() == "X":
                   print("Program stopped.")
                   break
               print("Hello,", name)
       else:
        print("Invalid lesson!")
     elif topics == 4:
         print("==== INTRODUCTION TO PROGRAMMING ====")
         print("[1] = PROGRAMMING LANGUAGE")
         print("[2] = PYTHON PROGRAMMING")
         print("[3] = ABOUT PYTHON")
         answer = int(input("Choose Lesson: "))
         if answer == 1:
             print("==== PROGRAMMING LANGUAGE ====")
             print("A programming language is a special language that computers understand and use to perform tasks.")
         elif answer == 2:
             print("==== PYTHON PROGRAMMING ====")
             print("Python is a widely-used programming language that was a created by Guido van Rossum in 1991.")
             print("Python is a high-level, interpreted, and general-purpose programming language designed to be simple, readable, and easy to learn")
         elif answer == 3:
             print("==== ABOUT PYTHON ====")
             print("[1] = Simple and easy to learn")
             print("[2] = Readable syntax")
             print("[3] = Versatile")
             print("[4] = Huge community")
             definition = int(input("Why learn python?: "))
             if definition == 1:
                 print("Great for beginners")
             elif definition == 2:
                print("Code looks almost like English")
             elif definition == 3:
                 print("Used in many fields (AI, web, automation, games, etc.")
         else:
                 print("LOOK TO ANOTHER SUBJECT")
     elif topics == 5:
         print("==== BASIC SYNTAX ====")
         print("Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
         print("Example:")
         sir = "YOOHOOO!DITO ANG TINGIN SIRR."
         print(sir)
     elif topics == 6:
         print("==== ARITHMETIC OPERATORS ====")
         print("Arithmetic operators are symbols used to perform mathematical calculations on numbers.")
         print("Example:")
         print("Addition:", 5 - 3)
         print("Multiplication:", 5 * 3)
         print("Division:", 5 / 3)
         print("Floor Division:", 5 // 3)
         print("Modulus:", 5 % 3)
         print("Exponentiation", 5 ** 3)

 elif subj == 2:
     print("\n[1] INTRODUCTION TO PROBLEM SOLVING")
     print("[2] ALGORITHM")
     print("[3] PSEUDOCODE")
     print("[4] FLOWCHART")
     print("[5] PROGRAM LOGIC")
     print("[6] CONDITION")
     print("[7] IF-ELSE STATEMENT")
     print("[8] IF-ELSE IF-ELSE STATEMENT")

     topics = int(input("Choose your lesson: "))

     if topics == 1:
       print("==== INTRODUCTION TO PROBLEM SOLVING ====")
       print("Problem solving is the process of analyzing a problem and finding the best solution before writing a computer program.")
     elif topics == 2:
       print("==== ALGORITHM ====")
       print("An Algorithm is a step-by-step procedure used to solve a problem or accomplish a task.")
     elif topics == 3:
       print("==== PSEUDOCODE ====")
       print("Pseudocode is an informal way of writing program logic using simple English statements.")
       print("Example:")
       print("START")
       print("DECLARE")
       print("INPUT")
       print("OUTPUT")
       print("END")
     elif topics == 4:
       print("==== FLOWCHART ====")
       print("A flowchart is a diagram representing the logical sequence in which a combination of steps or operations is to be performed.")
     elif topics == 5:
       print("==== PROGRAM LOGIC ====")
       print("Program Logic is the sequence of instruction that tells a computer how to solve problem.")
     elif topics == 6:
       print("==== CONDITION ====")
       print("A condition is an expression that evaluates to either: TRUE OR FALSE")
     elif topics == 7:
       print("==== IF-ELSE STATEMENT ====")
       print("A decision structure allows a program  to choose between two or more actions.")
     elif topics == 8:
       print("==== IF-ELSE IF-ELSE STATEMENT ====")
       print("What is an If-Else Statement?")
       print("An if-else statement is a conditional statement in Python ")
       print("that allows a program to make decisions.It checks whether a condition is True or False.")
       print("Example:")
       print("age = 18")

       print( "age >= 18:")
       print("You are  an adult")
       print("else:")
       print("You are a minor")
       print("else:")
       print("Invalid Lesson!")

 else:
    print("Invalid Subject!")