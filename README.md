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

- fibonacci_sequence 
- prime_numbers 
- twin_prime_constant 
- pi 
- degree 
- base_of_natural_logarithm 
- golden_ratio 
- eulers_constant 
- catalans_constant 
- aperys_constant 
- khinchins_constant 
- glaishers_constant 
- mertens_constant 

So the first thing the *immensity* function does is look at how long the message is that needs to be encoded. It then selects a number of the formentioned mathimatical constants in a random order and costructs a grid the same lenth as the message.

![](Images/grid.png)

We can now generat a pretty unique grid but lets make it completely uninue. To do this I added a *'step'* to each of the uneanding series. This *'step'* is basicaly just a random number that indicates at which point the series will start. Each series gets their own unique number. Forinstange the first *'pi'* series could only start at it's 78th number and then continue from there, Where as the *'twin_prime_constant '* might start at 7 followed by antother *'pi'* series that starts at 39.

Now we can create a truly uniue grid every time that stretches to infinity. But how does one gest a single series out of this grid the same lenght as the message. 

at this point I thought it a nifty idea to draw a classic *Sin* graph over this grid.

![](Images/graph.png)

After this was done it is easy to construct a new series. Just take the number in each colomb that the graph goes through.
Something like this:

![](Images/graph_and_num.png)

```
['2', '2', '1', '7', '0', '9', '5', '6', '9', '4', '1', '7', '7', '5', '3', '2', '2', '9', '5', '7', '0', '9', '2', '1', '3', '3', '6', '1', '3', '5', '8', '6', '6', '9', '9', '8', '0', '8', '3', '4']
```

You'll notice that the number graph does not match a 100%. Dis is due to switching between float and int data type in the sourse code. 

We now have a unique series of numbers the same length as our message. This can be used to indicate the number of positions each of the original characters will move on the *"ASCII cyrcle"* as it were. This is how we go abouut incrypting our originam string. The series of numbers we abtained from ouur graph can also be used as a *'key'* to decrypt the encoded string, the only diffrince is the opporatoin will just need to be done in reverse.

## The Function ##

### Multiprocessing, what is it ind why are all the cool kids talking about it? ###


![](Images/pythonpoweredlengthgif.gif)
