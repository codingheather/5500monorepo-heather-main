**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Color Selection by Key Pressing

**Primary Actor**: User

**Goal in Context**: To select the color for drawing on canvas by pressing the number keys 1 through 8 to select the following color:
1 = Black
2 = White
3 = Red
4 = Green
5 = Blue
6 = Yellow
7 = Magenta
8 = Cyan

**Preconditions**: (1) The program must be running and in a responsive state. (2) The canvas must be present on the screen for drawing. (3) The default color is Black and the corresponding color related to the specific number key need to be given in the instruction (below).
1 = Black
2 = White
3 = Red
4 = Green
5 = Blue
6 = Yellow
7 = Magenta
8 = Cyan

**Trigger**: (1) Pressing the number key in the range in 1 to 8.

**Scenario 1**: A user will choose and press a number key 2 to select the White color.

**Scenario 1**: A user will choose and press a number key 5 to select the Blue color.
 
**Exceptions**: The color may not be changed or change as expected. In this case, (1) the user need to be double checked to see whether the user pressed the number keys in the range of 1-8; (2) the user need to double check whether the number keys 1 through 8 are working properly and are responsive when pressing from the user's end. 

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard. The system should respond within 1 second of any keyboard event. The user is responsible for all other input after selecting the color.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement 'color_change' functionalities in the future to prompt a user with a dialog to double check whether the user is sure about changing color before selecting the new color.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
