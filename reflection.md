# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The game had already marked an attempt before I even did anything and this happens each time the app is reloaded
  - The hints were messed up when entering a number lower than the secret number the hints show that you should go lower
  and if it is higher than the number it tells you to go higher seems like they are flipped.
  - The "new game" botton also glitches out when the correct number is guest and only changes the secret number and not the
  attemps or score the message telling you that you won and start the game also doesnot disappear. it seems like the states of the
  game are all not changed or affected when someone wins.
  - when the right number is guessed again the game doesnot update anything and the animations dont happen. it is like the 
  game is frozeen this happens when the secret number was guessed right and the user is trying to play again
  - the submit guess button seems off had to press it more than once for my guess to be submitted and checked 
  - the attempts counter didnt count the first attempt after fixing the glitch where it reduced the attempts before the player did anything/ made a guess. the attempts number changes
  after you click the button again with a differet guess. so the first guess is not added to the list utill the button is press again. seems like this is what is affect how the subimt works
  - when changing the levels of difficulty the attempts left update but the range does not update
  - There is also no warning for out of range forexample when someone enters a number like 1000 or -100 and the range is 0 - 100 the game conutinues with no warning to the player
  - the difficult ranges also seem off. It seems like a design mistake where the higher range 
  is considered not more and the median ranges is considered hard. Same thing with attempts left at each level. The invalid inputs also trigger and reduce the number of attempts left. Attempts left should only be triggered but vaild guesses.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|r | not a number,attempts change | not a number,attempts didnt change| that is not a number| 
|2 | hints telling me to go lower | hints telling me to go lower | Go lower! |
| 80 | hints telling me to go higher | hints telling me to go higher | Go Higher!|
| 15 | correct number | correct number  | correct! you won! The secret was 15. Final score: 45|
| 0 | out of ranges error | error message and update number of attempts | please enter number between a given range
|
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  AI suggest that i add the low and high perimiters  to the parse_guess function and a condition check for out of bounds. I verified by reading the suggested code and understand what it was doing and also tested it fixing the out of range bug.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  
  I didnt get any correct suggestion all suggestion suggest we based on fix the bugs that found and i read them and test them to make sure that they didnt create another bug

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I determined that the bug was fix by testing the same case and other different cases that had cause or triggered the bug.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  Tested if the hint messages where still flipped and made sure that the out of range where caught and handled. used number that where above and below the secert number to make sure that the hints where fixed and not flipped any more.


- Did AI help you design or understand any tests? How?

  yes it used Claude to make the test and i had a couple errors after runing the pytests. Claude AI explained to me what was causing the error, what the error was and how it can be fixed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I learnt that streamlit runs the code from top to bottom so states update in that form which was causing a delay in the game. it also lets oyu srore and keep values between those reruns for easy access.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    Questioning and understanding what is going on in the code and what AI is doing and why it is doing it that way and not following it blindly.

- What is one thing you would do differently next time you work with AI on a coding task?

  Finding all the bugs and having AI explain them one by one

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project showed me that AI generated code is not going to be always right and following it blindly might lead to creation of expected out puts and bugs. 
