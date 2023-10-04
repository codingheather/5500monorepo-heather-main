# Lab 4 - SDLC

<img align="right" width="200px" src="./media/sdlc.jpg">


# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
	- However, my instructions will usually be using the command-line, and that is what I will most easily be able to assist you with.
- In the future there may be restrictions, so please review the logistics each time.

# Resources to help

Provided below are a list of curated resources to help you complete the task(s) below. Consult them (read them, or do ctrl+f for keywords) if you get stuck.

1. For Task 0
	- https://www.guru99.com/software-engineering-prototyping-model.html
	- Discusses the Prototyping Model (For task 0 we have actually already gone through the prototyping model!)
2. For Task 1
	- High level description of use cases
		- https://en.wikipedia.org/wiki/Requirements_analysis#Use_cases

# Task 0 - The SDLC

We have previously talked about the Software Development Life Cycle(SDLC) in class. Working through the entire Software Development Life Cycle(SDLC) in one lab however may not be very pragmatic. For your group project you will have to pick a style and follow it (pragmatically, in this course it is likely to be an agile methodology, though I would be open to other variants). Today you are going to get some practice on the first planning stage of the SDLC.

## Refresher

Recall that we saw several versions of SDLC's. One of them was Synopsys SDLC, a real company's Software Development Life Cycle that they follow. As a refresher, the 5 stages were:

1. Plan 	- Determine the feasibility of the project and perform a requirements analysis
2. Design	- Create interfaces, and figure out some software structures
3. Implement	- Begin writing code and end with a working prototype
4. Release	- Test the software then release to the public
5. Respond	- Perform any software maintenance after the release.

(Note: Sometimes different companies will have 6 stages--it just depends)

## Planning Stages

Assume that you have a client who wants us to build a 'paint' like program called mini-paint. In this stage we really want to focus on two things:

1. The feasibility of the project
2. The requirements of the system.

## Project feasibility

<img width="400px" src="./media/prototyping.png">

A first question we might ask when developing software is, *do we have the technology*? There are famous examples of launching great technologies before the market or the technology may have been ready: [Intel's web tablet in 2001](https://www.cnet.com/news/before-apples-ipad-there-was-the-intel-ipad-seriously/), early iterations of VR, or even Google glass. Some might argue that these projects were not great successes only because they were too early. Maybe the processing power was not enough, maybe the device was too bulky, or maybe the public was not ready for such a device. For us let's first see if we have the technology. We can determine if we have at least the bare minimum programming tools to create some *paint like* application called mini-paint--and in a sense, we have already achieved this from prior assignments!

Assume for task 0--that we in fact have the technology.

# Task 1 - Requirements analysis

The second part of the planning stage is to gather the project requirements. If you have made it through Task 0, you can report back to your client that the project is feasible. When we meet with the client however, we will want to very clearly communicate the deliverables that we would like to achieve. To do this, we perform a requirements analysis.

A [requirements analysis](https://en.wikipedia.org/wiki/Requirements_analysis) allows us to summarize amongst all the [stakeholders](https://www.projectmanager.com/blog/what-is-a-stakeholder) (i.e. people who are effected by the outcome of a project) what exactly is going into the project. This can take place in many forms, but the form we are going to do is to write different use cases.

## The Task

In the [UseCases](./UseCases) folder you are going to find 5 use cases. The [fifth use case](./UseCases/usecase5.md) is filled out for you as an example. 
Complete the following use cases (note that the fifth use case was already done for you as an example):

1. The window and drawable canvas should be 600x400 (600 pixels wide, 400 pixels high)
2. Pressing the number keys 1 through 8 allows you to draw in a different color.
	- 1 = Black
	- 2 = White
	- 3 = Red
	- 4 = Green
	- 5 = Blue
	- 6 = Yellow
	- 7 = Magenta
	- 8 = Cyan
3. Pressing the space key will clear the entire canvas. 
	- This means all pixels will be removed, and the entire canvas will be a solid color with the last color you have selected.
	- (In other words, this fills the entire canvas with the last selected color)
4. When the mouse is pressed and a user left-clicks (i.e. on the pressed event, not released) a pixel color will change wherever the mouse is located. This should allow me to drag and draw over the canvas like a pencil on a piece of paper.
5. Pressing the escape key should terminate the program.

### Summary of the pieces of a use case.

Below is a typical use case for a specific feature

* Use Case: *use-case-title*
* Primary Actor: *primary-actor*
* Goal in Context: *the aim of the primary-actor in a particular circumstance*
* Preconditions: *conditions that must be true before the scenario may play out*
* Trigger: *an action or actions that initiate the scenario*
* Scenario: *an enumerated list of steps describing the actions and interactions of the primary actor with the system*
* Exceptions: *errors or faults that may occur during the scenario. Should include remedy/corrective action taken by the primary actor*
* Priority: *relative importance of this use case compared to other use cases*
* When available: *the targeted release that covers this use case*
* Channel to actor: *the means through which the primary actor and the system communicate*
* Secondary Actor: *any other actors – people or systems – that may be involved in the scenario*
* Channels to Secondary Actors: *the means through which any secondary actors may interact with the system or other actors*
* Open Issues: *notes, concerns, or other materials*

## Testing

- Task 1
	- We will look over your user cases, make sure they are complete.
		- Some fields may not need to be filled in, use your best judgement and mark as N/A or justify why they are otherwise not needed.

# Submission/Deliverables

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary.

### Deliverables

- Task 0
	- No deliverable, just review your prior assignment to refresh yourself on what you did to implement mini-paint.
- Task 1
	- Fill in each of the [UseCases](./UseCases) in the repository

# Rubric

You (and any partner(s)) will receive the same grade from a scale of 0-2. Both partners should commit the same code.

- 0 for no work completed by the deadline
- 1 for some work completed, but something is not working properly
- 2 for a completed lab (with possible 'going further' options completed)

1. Feel free to play more with SFML! We will be working in this library more in the future!

# F.A.Q. (Instructor Anticipated Questions)

1. Q: I did not fill out one of the rows in the use cases section, is this okay?
	- A: Yes, some rows may not be relevant.
