**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drag and Draw over the Canvas with Mouse 

**Primary Actor**: User

**Goal in Context**: To drag and draw things over the canvas with the mouse acting as a pencil on a piece of paper by left-click, hold, and drag the mouse to draw on the canvas.

**Preconditions**: (1) The program must be running and in a responsive state. (2) The canvas must be present on the screen for drawing. (3) the color has been selected for drawing

**Trigger**: (1) User left-clicking the pixel to make the pixel change color (2) Keep drag the mouse without releasing it for drawing on the canvas
  
**Scenario 1**: A user will left click, hold the left click and draw a heart shape on the canvas. 

**Scenario 2**: A user will left-click a pixel and see a color change of that pixel

**Scenario 3**: A user will hold a left click and keep dragging the mouse and move the cursor without release it and they will see the pixels that the cursor hovered changes color just like drawing with a pencil on a piece of paper
 
**Exceptions**: The drawing is not present. In this case, (1) user should check whether the pixel is left-clicked. (2) the user should check whether the pixel is dead or not. (3) the user should make sure that they do not release the press event and keep pressing during the entire drawring.

**Priority**: High-priority

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the mouse. The system is responsible for maintaining focus of the window when the user clicks. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: N/A

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
