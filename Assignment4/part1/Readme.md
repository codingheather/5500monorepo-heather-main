# Writing Stories

There are many ways to elicit customer requirements during the [requirements analysis](https://en.wikipedia.org/wiki/Requirements_analysis) phase of the SDLC. 
[Use cases](https://en.wikipedia.org/wiki/Use_case) are a common tool in software engineering to identify requirements in a software system. For example, recall the user stories we had to
create for a making a Paint web application. 

But use cases are not the only tool for requirements analysis. Another popular tool from Agile development is [user stories](https://en.wikipedia.org/wiki/User_story). 
User stories follow a general template: 

* One-line description
* Acceptance Criteria

The one-line description follows this form:

`As a <role> I can <capability>, so that <receive benefit>`

Acceptance Criteria define the conditions that need to be met for a user story to be considered complete and accepted by the product owner or stakeholders. 
Acceptance criteria provide a detailed and testable description of what the user story should accomplish and serve as a way to ensure that the development team and stakeholders have a shared understanding of the story's requirements.

1. Specificity: Acceptance criteria should be specific and unambiguous, leaving no room for interpretation. They should be clear enough that both the development team and stakeholders understand what is expected.

2. Testability: Each acceptance criterion should be testable, meaning that it should be possible to verify whether the requirement has been met or not. Testing helps ensure that the user story has been implemented correctly.

3. Completeness: Acceptance criteria should cover all aspects of the user story's functionality. They should address different scenarios, edge cases, and any exceptional conditions that need to be considered.

4. Independence: Each acceptance criterion should be independent of the others. This means that meeting one criterion should not automatically fulfill the others. They should be standalone requirements.

5. Prioritization: Acceptance criteria can be prioritized, helping to define the most critical requirements and ensuring that the most important functionality is implemented first.

6. Measurability: Acceptance criteria often include specific metrics or values that can be used to measure whether the user story's goals have been achieved. This could be quantitative data or qualitative assessments.

7. Alignment with User Needs: Acceptance criteria should be directly tied to the needs and expectations of the end users. They should address what the user wants to achieve with the user story.

8. Acceptance by Stakeholders: Ultimately, the acceptance criteria are used by stakeholders (e.g., product owners or product managers) to determine if the user story is ready for acceptance and deployment.

For example, if you have a user story related to an e-commerce website, the acceptance criteria might include:

"When a user adds a product to the cart and proceeds to checkout, the system should correctly calculate the total order amount, including taxes and shipping fees."
"The user should receive an order confirmation email with the correct order details within 10 minutes of completing the purchase."
"If the user provides an invalid shipping address, they should see an error message indicating the issue, and the order should not be processed."

## Resources

https://www.easyagile.com/training/writing-good-user-stories.pdf

# Task 0

Go to www.paypal.com and explore the features and services of that platform. Choose one of their services such as Digital Wallet, Send Money, Sign Up, or Pay Bills and create a User Story based 
on that feature or service. Your user story should follow the template mentioned above.  

# Submission/Deliverables

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary.

### Deliverables

- Task 0
	- Write your user story in the file `user_story.md` in the folder [part1](./part1)
