# CS 5500 Project Overview

Your team is a startup of business development consultants, solutions architects, and software engineers who are building software solutions that allow consumers and businesses to process payments online instead of traditional point-of-sale (POS) systems. Your team has just received its Series-B funding and has been tasked to build an online-payment processing platform (OPP) that will compete against other platforms such as Paypal, Square, or Stripe. 

Your typical customer is two-fold: other software developers and small-to-medium sized business owners. For other software developers, they want ReST API's that they can easily consume to help them build payment applications on top of your OPP.    

For small-to-medium sized business owners, they want to replace their old point of sale system with a simple and easy-to-use web application. 

Thus, your goal is to build the backend that will support the ReST API's for the platform. In addition, you also need to build a simple frontend that will serve as the graphical user interface (GUI). 

Your software system needs to support the following:

* Process a customer’s credit card charges for a purchase
* Calculate the current total balance of fully processed funds
* Calculate the current total balance of fully processed funds for a certain time period 
* Get a list of all transactions that comprise the total balance
* Get a list of all accounts receivables (i.e pending purchaes) 
* Validate credit cards for any fraudulent credit card purchases and immediately reject any transaction using fraudulent payments
* Validate that debit cards have enough funds to cover the cost of a purchase
* Ability to create signup for an account with the platform
 

A few hard requirements:

* Upon validation, debit card purchases are instantly processed and do not have to wait for an arbitrary amount of time to clear the banking system
* However, credit card purchases have a minimum of two calendar days while in processing. Therefore, for at least the first two days of being processed, credit card purchases are considered to be "in-processing" and thus should not count towards a business owner's total balance of fully processed funds. Once two days have passed, that credit card purchase is considered "processed" and can be counted towards a business owner's total balance
* Credit card and debit cards must be validated before being processed; here is an [informative article](https://www.baeldung.com/java-validate-cc-number) on how credit cards are validated. Most companies use the [Lund Algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) to validate credit card numbers. Although the algorithm was patented, it is now part of the public domain.  
* Security is a must; the system must provide user authentication to prevent malicious users from accounts. The platform must ensure some sort of encryption or security when data is exchanged over the network 
