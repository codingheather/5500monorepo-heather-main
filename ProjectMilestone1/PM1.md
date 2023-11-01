# Project Milestone 1: Design

The design phase is a stage where software developers define the technical details of the product. 
These details can include wireframes or mockups of the frontend, an entity relationship diagram of the database, 
API design, sequence diagrams to illustrate the flow of your API's, and system interfaces. The design documents that are 
created during this phase can be classified into two categories:

* High-Level Design (HLD)
* Low-Level Design (LLD)

High-Level Design should address the following:
* Architecture of the application
    * Include details on how application is deployed to the Cloud
* Deployment Pipeline (Describes how changes to the codebase are tested and deployed to production)
* Wireframes/mockups of the frontend
* Description of each module in the backend (i.e. what the module does)

Low-Level Design should address the following:
* Entity Relationship Diagram (ERD) of all your proposed entities and relationships between entities of your database design
* ReST API design and specifications
  * Should cover what the input and output should be
  * Identify all potential error messages and corresponding HTML status codes
* Sequence diagram of each ReST API 
* Functional logic of each module in the backend (i.e. how the module does something)

You should create tasks that address these design concerns. Those tasks should be associated with an appropriate User Story. 
Remember that User Stories are living, breathing documents; they change as your team progress through the SDLC. In the design
phase of the SDLC, you should expect your tasks and User Stories to change as you create your design documents. 

# Resources

[Lucidchart - free for students](https://www.lucidchart.com/pages/usecase/education): This tool is good for creating architecture diagrams or UML diagrams.   

[Plantuml](https://plantuml.com/sequence-diagram): This tool is easy to use and recommended for creating sequence diagrams, ERD's, or UML diagrams. You can immediately create diagrams using [their online server](https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000). 

[Swagger article on API design](https://swagger.io/resources/articles/best-practices-in-api-design/?sbsearch=api%20design): Read this article on the nuts and bolts of good API design. And if you are advanced enough, you can use their [tool](https://app.swaggerhub.com/apis/HCASTILLOEXT/DataMaster/1.0.0#/) to create your API design. 

[HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) Useful for creating your API design

[HTTP Status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

# Deliverables

On your `opp-api` repo, create a `design-documents` folder at the root level. Put your design documents in that folder. You can include both text files and images in that folder. If you include text files, I highly encourage you to write in Markdown, a popular markup language used to write technical documentation. Knowing how to use Markdown is a practical skill that
every developer should know. Here's a [good guide](https://www.w3schools.io/file/markdown-introduction/) to get you started. 

Your team should create the following design documents:

* High Level Design
  * Diagram of your overall architecture; if you want, feel free to include any use of Cloud technologies
  * Wireframes of your UI
  * Description of each of your backend modules

* Low Level Design
  * Entity Relationship Diagram of your database
  * Sequence Diagram of each ReST API
    * Use [this tutorial to learn how to quickly create one](https://plantuml.com/sequence-diagram) 
  * ReST API design
    * You can use the Swagger Tool (hard)
    * Or you can do it the easy and old-fashioned way by simply writing it down on a text editor; below is an example template that you can use
  * Description of how each backend module performs its job
    * Submit a module or class diagram of its attributes and methods (look into [this tutorial](https://plantuml.com/class-diagram))

`<VERB> /<path>/<path to>/<api-route>`

`GET /api/<path_param>/?title=`

| Request Field | Field Type | Field Description |
|---------------|------------|-------------------|
| id | String | the item's id |
|some_data| int | really important data for a request |


| Response Field | Field Type | Field Description |
|----------------|---------|-------------------|
| access_token   | String  | the item's id |
| content-type   | MIME    |  |


Example request/response

`$ curl 'http://localhost:8000/read-all -i -H 'Accept: application/json`

Successful response
```
HTTP/1.1 200 OK
date: Thu, 26 Oct 2023 22:36:31 GMT
server: uvicorn
content-type: application/json

Response Body
[
  {
    "title": "learn fastapi",
    "owner_id": 1,
    "priority": 3,
    "complete": false,
    "id": 1,
    "description": "fdakfjlds jdlskfj"
  }
]
```

Other than Successful

```
HTTP/1.1 301 Moved Permanently
date: Thu, 26 Oct 2023 22:36:31 GMT
server: uvicorn
content-type: application/json

Response Body
[
  {
    "title": "learn fastapi",
    "owner_id": 1,
    "priority": 3,
    "complete": false,
    "id": 1,
    "description": "fdakfjlds jdlskfj"
  }
]
```






**On Canvas, submit the GitHub link to your project's opp-api repo. Only one team member should submit it on behalf of the team.**  
