# MCalm
# Capstone Project DSN-4099

## INTRODUCTION

Our project “MCalm” would detect people’s mood by using their facial expressions as well as by
asking a few questions on a scale of 5, which would help people get a wider picture of their mood.
Next comes the task to enlighten their mood by playing games , listening to jokes by bot and at last
listening to soothing music.

Seeing people busy in the regular hustle and bustle of life and not having enough time to focus on
one’s mental health was one of the major reasons that motivated us to come up with an idea to build
a website that could help people to lighten their mood.


## Techniques used in project modules:

We have used following techniques in given modules:-
Module 1: HTML5, flask, python
Module 2: opencv, tensorflow, python, FER
Module 3: subprocess, random, os
Module 4: numpy, nltk, random, json, torch, tkinter
Module 5: sklearn, joblib, numpy, matplotlib

## Project Organisation

![Project Organisation](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/project_organisation.png)

In today’s hectic world where people just focus to excel in their lives and that too at the cost of
losing their peace of mind. Either that excel is their wealth or their position in offices and other
aspects of life. In order to overcome this lost peace of mind we have come up with a solution.


## Objective

Our main objective here is to decrease the stress or lost piece of mind of people by making an
integrated website that would tell people about their mood/sentiments either it is happy, sad and
many more by detecting their faces as well as taking answers from the people of some questions on a
scale of 5, our next objective is to improve people’s mood by playing a relaxing game of 21 and to
let people have an interaction with a chatbot that would try to lighten people’s mood by telling some
jokes to them and at last to play some soothing music for the person using the website.

## Architecture Diagram

![Architecture Diagram](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/capstone_review3_arch_diag.JPG)

## Design Diagram

![Design Diagram](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/design_diag.JPG)


#### Home Page

This is the home page of our project, it contains crisp information on what the project is about.

![Home Page](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_home.JPG)
![Home Page](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_home2.JPG)
![Home Page](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_home3.JPG)

## Methodology and Goal :

#### Game of 21 (Module 1)

![Module 1](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_game_of_21.JPG)

Module 1 (Game of 21) is a two player game built on logic. Rules are simple, a player can enter one,
two or three numbers at once. Numbers should be in a sequence. The catch is that the player who
gets 21 loses. This game is deployed using Flask.

#### Sentiment Recognition (Module 2)

Module 2 (Sentiment Recognition using facial features) uses FER, which is a package which was
developed in 2013. It had around 28000 labeled images and facial expressions.

Facial Emotion Recognition (FER)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/detected_baby1.JPG)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/detected_ishan.JPG)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/detected_johncena1.JPG)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/detected_kevin.JPG)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/detected_south_actor.JPG)

So the camera takes a
snip of the user and then processes it further to detect the sentiment. There are seven sentiments
which are detected [Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral].

Sentiment Recognised (with scores)

![Module 2](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_emotion.JPG)

#### Soothing songs (Module 3)

Module 3 (Playing soothing music using sentiment detected from Module 2) gets the emotion value
from module 2. There are seven sentiments detected and whichever has the highest score is returned
from module 2 and is further used to play soothing music. Directories are there for each sentiment
and music is stored in those paths. So with the help of a subprocess package and a music player,
songs are played.

![Module 3](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_song.JPG)

#### Doudou's Chatbot (Module 4)

Module 4 (Doudou’s chatbot) module was made to make the user feel good by allowing him to chat
with our chatbot. This is the first time I applied Natural Language Processing into one of my college
projects and I learned new things. Also I recalled the learnings of my 6th semester from Soft
Computing about Neural Networks. Like the math behind it, where the purpose was to reduce the
error and the error is the difference between actual and desired output. It was trained on some
responses which were in an intents json file. Pytorch was used to build a three layer model. ReLU
activation function was used after the layers to make the output zero if it gets a negative input else it
returns the same value. This module works well and was deployed using Flask.

![Module 4](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_chatbot.JPG)

#### Psychometric Test (Module 5)

This is an implementation of the Big Five Personality test. This test gives you more insight into how
you react in different situations, which can help you choose an occupation. HTML5, CSS3,
JavaScript was used to make the web application and the model was trained using keras package.

![Module 5](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_psychometric_test.JPG)

We used K-Means Clustering as the final layer has five outputs i.e five different kinds of personalities
(open mindedness, conscientiousness, extraversion, agreeableness, neuroticism). K-Means was used
as it is a centroid-based algorithm, or a distance-based algorithm, where we calculate the distances to
assign a point to a cluster. In K-Means, each cluster is associated with a centroid.

![Module 5](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_psychometric_test2.JPG)

## RESULTS

#### Game of 21 (Module 1)

This is the case in which the user is losing because currently the computer has entered numbers till
20 and now the user has to enter 21, i.e just after entering 21 he/she will lose.

![Module 1](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_game_of_21_result.JPG)

And you can see that after hitting the GO button, Result is displayed as ‘You Lose’.

![Module 1](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_game_of_21_result2.JPG)

This is the case in which the user is winning because the user entered 15, 16 and now there is no way
a computer can win this game unless the user does not comprehend the game pretty well. And now
the user has to enter the numbers in a way that the computer gets to put 21, i.e just enter numbers till 20.

![Module 1](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_game_of_21_result3.JPG)

And you can see that after hitting the GO button, Result is displayed as ‘You Win!’.

![Module 1](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_game_of_21_result4.JPG)

Now it's time to discuss the next segment of this project, which is not necessary to display on UI, but
is a deciding factor in selecting the song for the soothing song recommendation.
Sentiment is detected automatically during the execution of the code and out of the seven emotions,
the emotion having the highest score is awarded the opportunity to select the category of the songs,
i.e from which directory the song is going to be played.

#### Soothing Songs (Module 3)
![Module 3](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_songResult.JPG)

This is the case where neutral emotion is the top emotion out of all seven emotions (highlighted in
yellow font color) with 95% score (marked in a red box). So a song starts playing randomly from a
neutral directory.

#### Doudou's Chatbot (Module 4)

![Module 4](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_chatbotResult.JPG)

#### Psychometric Test (Module 5)

![Module 5](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_psychometricResult.JPG)

#### Fragrance Blog (Additional)

This is an article on effects fragrance on sentiments

![Blog](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_frag.JPG)

![Blog](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_frag2.JPG)

![Blog](https://github.com/sarthakmishraa/Capstone-Project-MCalm/blob/main/static/images/snip_frag3.JPG)

## Project Outcome and Applicability

#### Outline

The idea behind M-calm helps to get an understanding for the need of mental health awareness as
well as the need for an environment where people can come forward and talk about it . M-calm will
not only burst the bubble of taboo but create a safe ground where people can discuss their mental
health. The implementation chosen for going down this path is simple and via chatbot and games
which will help users to ease around and not go through a lot of technicalities.

#### Key implementations outline of the System

M-Calm is developed as a web-application with an idea of allowing each user to access it with ease
of any device they wish and is available to the respective user. What the team has aimed to achieve is
an application tested and stands on the idea fulfillment for giving a space to open up to get the
knowledge as well as to understand the awareness regarding mental health. The gamification of the
whole method is developed to achieve an interaction with the user, the perspective behind the feature
of game in the application allows user to go through change of emotions and experience the stages
one can go through while faces challenges in real time. Proceeding to our first stage and game named
“the game of 21”, allows user to enter values on alternative turns while playing with computer and
the one whoever ends on the number of 21 will be achieving win, the outline of implementation for
this game is to allowing the user to experience the hardship emotional value which is required for
people who chose not to give up and the mental health they go through to win in situations they face
in real life.

The next stage of our application is sentiment analysis using computer vision, this is the place where
computer vision and intelligence go hand-in hand to give out the message of possibilities we can
achieve in today’s time. This module not only will detect the sentiment with analysis will also
contribute to the next module and stage an example of how things can turn around, so the outline for
implementation is keeping the track of user’s sentiment state and pass the next module the
information for suggesting the helping hand they can go with to lighten their mood and experience
the technology advancement there is.

The Modules were achieved by continuous planning of the team and the research for integrating the
modules with each other. The Team planned for divide and sum-up technique by picking the modules
for each expertise field for development and fulfilling the project requirements. The guidance from
our reviewer regarding the human behavior taught us the actual help that we can provide with
providing awareness.

#### Significant project outcomes

The project’s outcomes most importantly contributed to our learnings, as well as understanding the
need of awareness about mental health, the very idea with which we started our project. The project
was like a rainbow for us which we thought of as a ray light only. The project is developed and
capable of rolling out the even more new integrations for implementations inside the project to add
features which can help the end users as much as they want to explore. There were challenges and
questions on accuracy of analysis, delivery of desired results and many like these, but each of these
was overcome by the team planning and communication with the guides and reviewer.

#### Project implementation on real world application

# (MCalm)
