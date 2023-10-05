**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear Canvas with Space Key

**Primary Actor**: User

**Goal in Context**: To clear the entire canvas and return to the canvas entirely filled with the last color the user has selected

**Preconditions**: The program must be running and in a responsive state. There is a pre-selected or default color before doing this step

**Trigger**: (1) Pressing the space key.
  
**Scenario**: A user will press the space key and the entire canvas is filled with a color after the key pressing action.
 
**Exceptions**: The canvas may not be responding (i.e. not changed the state and filled entirely with a certain color). In this case, (1) the user need to double check whether the space key is working properly and are responsive when pressing from the user's end.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices. This includes the keyboard. The system should respond within 1 second of any keyboard event.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement "clearing" functionality in the future, and revise this use case to pprompt a user with a clear dialog before clearing to double check whether the user really want to cover the entire canvas with just one selected color or the space key is pressed by accident.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
