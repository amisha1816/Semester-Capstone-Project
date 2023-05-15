### How to code a pop up screen 🌷 AM

📎 https://www.youtube.com/watch?v=j9yMFG3D7fg by Clear Code  
 
In the video, Clear Code creates a ```GameState class``` within ```main.py``` for the different screens. We would have three (maybe 4) screens for our game: main page, inventory, farmer's market and log in screen (❓).  

The ```GameState class``` pulls code from the while loop below for each of it's different methods:
![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/9142ad11-615a-46c9-ad5e-bd6cd602050b)  
*We should move everything inside the loop except I think the clock which is ok to stay*

To make the method an object we just need to add the line ```game_state = GameState()``` somewhere within these lines of code:
![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/5122fe93-59c7-44cc-86f5-89e1b239a2c3)

Also, we need to add game_state.main_game() to our original while loop so we can change the screens.

🎉 Other content in the video: uploading text files to display, how to create a statemanger (❗)
![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/8ad0b99d-f9bc-4301-bb38-fcbe4d8622df)

#### collision
![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/334fbdec-ffe3-4b7c-9c61-69b7a2b88df4)
*this is how the tutorial did it, we're going to have to adjust it with our ```farmet's market button```
