#Write a program to create a class with name Student and perform the following tasks -
 #Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them

class student:
    grade=11
    name="Anaysha"


    def intro(self):
       print("Hi I am a student")
   
    def show(self):
     print("my name is",self.name, "and I study in grade",self.grade)
          
st=student()
st.intro()
st.show()

       
