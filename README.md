# Intelligent-Chat-Box:
The main functionality of Intelligent Chat Box is it help users accomplish specific tasks by identifying user intent from text or voice conversations using artificial intelligence. It is a desktop application that communicates with users in natural language via auditory or textual methods.

# Modules description:
The project have three layers, In the first layer, I have to make a bot with the help chatterbot package, First of all, I have to pip 
Chatterbot package from this import ChatBot package to make a bot after this we have made a data set for train the Bot with the help
of ListTrainer package and this is an import from Chatterbot. trainers package for communicates with users in natural language via auditory or textual methods.
In the second layer, I have to create a window with the help of the Tkinter GUI package for taking queries of users in the form of auditory or textual methods. In this we have to create tk class for creating a window of the bot after this I have made a frame to show the text or
auditory msg.
In the third layer, finally, I have to show a conversation between users and bot through the ask_from_bot function which is a user-defined function
working of this is that get the text or auditory queries from get() and the response of these queries with the help of 
bot.get_responce(query) and after this insert the conversations on the frame of Tkinter with the help of msg.insert().
And further, I modify my project with the help of the pptxs3 package working on this package is to deliver audio of queries response.
In this firstly initialize engine from init() of pptxs3 and this engine has a set of two voice one is a male version or the second one is female version then set the engine voice with the help of engine.setProerty().

# Advantages and the main functionality of your application:
Advantage of this application is:
-- Available of 24 hrs.
-- Getting an instant responce.
-- A good customer experience.
-- Higher Customer Satisfaction.
-- Complaints resolve quickly.
-- Benfits of companies in terms of cost saving.

Main functionality of Intelligent Bots is it help users accomplish specific tasks by identifying user intent from text or voice conversations using artificial intelligence. They extract key pieces of information using a process called entity extraction leveraging natural language understanding
	
# Tools/Technologies used:
With the help of Python, Tkinter, Chatterbot and pptxs3 technologies helped me to developed Intelligent ChatBot.

# Challenges in the project:
I had faced a lot of difficulties like how to solve bugs in the code and sometimes my code was correct but my system or package configuration was not suitable.
Those errors took a lot of time to solve, and StackOverflow helped me a lot to solve the errors even it is of package installation or code related error.

# The number of people in the project:
In this project three members and this is my acadmic project and my role in this project is developer.
'''Role: The skills of developers that should be involved depends a bit on your case. If you don’t want to integrate any external services you might even create a bot with a developer. If you’re planning to connect with other service it is recommended to have at least someone that is familiar with JavaScript.

Skill: The Developer is able to use the extracted entities to push that data into other systems and the other way around. When you want your bot to be future-proof you will need someone that can work with JavaScript. As most chatbot pilots start small you might want to look for a developer that is able to work in small and flexible teams.'''

# Amount of time it took for the project:
We took approx one month to complete this project.

# Improvements in the future for the present system:
I'll try to improve my application in the future like in present it is a desktop application and  with the help of flask or django
try to convert in web application.

# Drawbacks:
One of the greatest drawbacks of Chat Box is that they have been designed to handle first-level questions only. They may not be able to solve complex queries. You need to train them to converse with your customers in the right way. You also need to structure and optimize your knowledge base in a bot-friendly way.
