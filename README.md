# exercise-uno
Create a simple and fun game of Uno in Python. It should be easy for a user to clone your repository and start your game.

What you will program
A computer game resembling the card game Uno, with the following features:

A deck of cards

A hand of cards for each player

A discard pile

A draw pile

Two kinds of players: human and computer

The flow of turns between players

The end of the game

What you will learn
Overcome the fear of the blank canvas

Managing scope and complexity

Applying programming concepts to a real-world problem

Instructions
This exercise must be completed and submitted for review.
This may seem like a complicated undertaking for a first project. It is. But it’s also a great opportunity to learn how to break down a problem into manageable pieces. It’s likely that you might have to submit your project earlier than you expect, so it’s a good idea to work in small steps that leave you "incomplete, but ready to present" in between.

Online guides will likely add a lot of unnecessary complexity to the project. Part of your job as an engineer is to invent simplicity. To get you started in thinking about this, here are some questions to consider:

Is there a more specific version of this project that you could start with? For example, Uno with only 2 human players and only numerical cards.

Is it possible to program and test some of the features listed above independently of the others? For example, the user interface for selecting a card from your hand could just be a function that takes a list of cards and returns one of them.

What’s the simplest version of each feature? For example, a computer player whose only strategy is to play a random legal card.

What functions would make this project easy? Why not start with those?

Uno famously has a lot of variability in how people interpret the rules. I suggest you leave fun and complex house rules for when you’ve already got a working version of the basic rules.

A game should be fun to play. Ultimately, software only exists to be used by people; the user experience is the chief concern of an experienced programmer. Keep this in mind.

Finally, a big part of programming is psychology. Always be searching for ways to make the project easier and more enjoyable for yourself.

Python
Sometimes two pieces of code behave the same, but we still consider one to be better than the other. This is because code has lots of jobs besides just running correctly. It also has to be easy to understand and maintain.

Python has the notion of "Pythonic" code, which essentially means that you’re using the features of Python in the way they were intended. This makes it easier for other programmers to understand the choices you’ve made. It also makes it easier for you to understand the code you wrote six months ago.

You might have noticed that I haven’t mentioned efficiency. This project is not computationally intensive, so it’s not a concern. Right now, reasoning about which code is more "efficient" is unlikely to be helpful. We’ll learn more about this later in the program.

I only link two resources here, but they are both very important. The first is the official rules of Uno, which you should read. The second is the Zen of Python, which is a set of aphorisms that guide Python programmers in their work. It’s a good idea to read them and think about how they apply to your project.

You’re welcome to search for other resources, though I’d emphasize that the best way to learn is through programming a lot and through discourse with your peers.

Self Study
The Rules of Uno

The Zen of Python

Your Peers
Throughout the project, you will have access to a rich network of your fellow students. This is an incredible resource, but it’s also a responsibility. Don’t allow someone to do your work for you. A much better way to utilize your peers is to discuss programming concepts and strategies in general terms.

If you need help, try to isolate the problem from the rest of your work before presenting it to someone. Show them the simplest, smallest piece of code where you still encounter the same problem. This will help them answer you, but it’ll also help you apply the lesson more readily to future projects.

Review Guidelines
You are expected to review other students' submitted work. For each exercise submitted, you will be given guidelines to do a meaningful review.
Completeness
We’d like to know:

Does the game run?

Which of the listed features work properly?

Code style
Like we discussed, code serves many purposes besides just running. We’d also like to know:

Does the code take advantage of variable names and function names to make the code easier to understand?

Is the code neatly formatted? Did the programmer follow a common Python style, like PEP-8?

Is the code neatly separated into sections, such as imports, function definitions, and main code?

Software design
A well designed codebase is made up of simple, reusable components. We’d like to know:

Are the components of the codebase well separated? For example, are the user interface and game logic separate?

Do you think it would be easy to implement new features in this codebase?

User experience
A game should be fun to play. We’d like to know:

Is the game easy to understand and play?

Is the interface pleasant to use?

Are there any bugs or unexpected behaviors?