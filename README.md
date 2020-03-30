# immensity()
An encryption function built on the same math used in mathematical constants like the Fibonacci sequence, the twin prime constant and the base of the natural logarithm, to name but a few.

![](Images/immensity().png)


The idea behind the *immensity* function, was to create a strong light weight encryption function that can easily be used in future code. So the *immensity* function is designd to either encrypt existing string variables, or it can be given a file path and then read text from the file in question. Following this the function is build so it can decrypt the messages as well.

## How It Works ##

Going about encrypting text espesialy with the use of a computer is quite simple. If however you're not that fomilular with how a computer deals with the string datatype i.e. *text*. Here is a quick computer science theory lesson. 

Computers can only understand numbers. In order to represente letters and other unique characters we make use of the ASCII table. ASCII(American Standard Code for Information Interchange) is the numerical representation of a character such as 'a' or '@' or an action of some sort such as *`Esc`* or *`Tab`*. So to a computer each character is represented as a number between 0 and 255.
The way I went about encrypting a string of text, was to take the number of each character and move it *n* either in the positive or negative direction on the ASCII table.

I worked on the premiss that the ASCII table is arranged as a cyrcyle this will allow me to move the digits more than a max of 255 positions at any give time. To get a half desint encriptio each number will need to be moved a diffrent number of digets than the one before or the one after. Thus I'll need a unique series of number rotations at least the length of the message being encoded. And as we don't know what the length of the message is going to be, well lets cater for infinity just to be safe.

So create a series that is unique every single time and that stretches to infinity.

To do this I started by looking at already exsisting mathematical constants such as *pi* and the *Fibonacci sequence*. Below I listed the 13 matimatical constants used in this function. All of which stretches to infinity.

```
fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
twin_prime_constant = ['0', '6', '6', '0', '1', '6', '1', '8', '1', '5', '8', '4', '6', '8', '6', '9', '5', '7', '3', '9']
pi = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '5']
degree = ['0', '0', '1', '7', '4', '5', '3', '2', '9', '2', '5', '1', '9', '9', '4', '3', '2', '9', '5', '7']
base_of_natural_logarithm = ['2', '7', '1', '8', '2', '8', '1', '8', '2', '8', '4', '5', '9', '0', '4', '5', '2', '3', '5', '4']
golden_ratio = ['1', '6', '1', '8', '0', '3', '3', '9', '8', '8', '7', '4', '9', '8', '9', '4', '8', '4', '8', '2']
eulers_constant = ['0', '5', '7', '7', '2', '1', '5', '6', '6', '4', '9', '0', '1', '5', '3', '2', '8', '6', '0', '6']
catalans_constant = ['0', '9', '1', '5', '9', '6', '5', '5', '9', '4', '1', '7', '7', '2', '1', '9', '0', '1', '5', '0']
aperys_constant = ['1', '2', '0', '2', '0', '5', '6', '9', '0', '3', '1', '5', '9', '5', '9', '4', '2', '8', '5', '4']
khinchins_constant = ['2', '6', '8', '5', '4', '5', '2', '0', '0', '1', '0', '6', '5', '3', '0', '6', '4', '4', '5', '3']
glaishers_constant = ['1', '2', '8', '2', '4', '2', '7', '1', '2', '9', '1', '0', '0', '6', '2', '2', '6', '3', '6', '9']
mertens_constant = ['0', '2', '6', '1', '4', '9', '7', '2', '1', '2', '8', '4', '7', '6', '4', '2', '7', '8', '3', '7']
```








![](Images/pythonpoweredlengthgif.gif)
