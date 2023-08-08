# Milestone Project 2: Capitals Around the World

![Mockup on different screen sizes of home page](#)
Welcome to my third milestone project with the Code Institute. The purpose of this project it to build a full-stack site that allows your users to manage a common dataset about a particular domain. I have chosen to create a dictionary for motorcyling words and phrases. Users can sign up, add there own entries, edit and delete them. The definitions can then be displayed by all users.

<!-- **Please find my deployed site [here](https://mototorque-c015422a9ebb.herokuapp.com/).** -->

---

## Technologies used

- HTML5
- CSS3
- JavaScript
- Python3, using the following packages;
  - alembic==1.11.1
  - blinker==1.6.2
  - click==8.1.6
  - DateTime==5.2
  - Flask==2.3.2
  - Flask-Login==0.6.2
  - Flask-Migrate==4.0.4
  - Flask-SQLAlchemy==2.5.1
  - greenlet==2.0.2
  - itsdangerous==2.1.2
  - Mako==1.2.4
  - psycopg2==2.9.6
  - pytz==2023.3
  - SQLAlchemy==1.4.46
  - Werkzeug==2.3.6
  - zope.interface==6.0
- Balsamiq
- Font Awesome
- Google Fonts
- Materialize CSS
- GitHub
- codeanywhere
- Heroku
- ElephantSQL

---

## UX & UI

### Project Goals

The goal of the project is to collect enough definitions that they can eventually be published in book form.

### Customer Goals

Users can share their own words or phrases about motorcycling to the rest of the community, as well as having access to all data provided by other users.

### Features

- Users will have be able to sign up and login, allowing them to create and edit their own data entries.
- Users that are not logged in are able to browse the data entries added by other users but will not be able to add their own entries.
- The username of the data entry author will be cited on the definition, giving credit to the user.
- An administrator log on with be able to edit or delete all user's dictionary entries and delete users themselves.

### User Stories

As a user of the web application I should be able to find words or phrases and view their definitions.

As a user I should be cited for adding a word or phrase and definition.

As a user I should be able to edit or remove my contributons. No other user should be able to do this.

The webpage must be responsive so that it can be experienced on mobile, tablet and desktop.

### Wireframes

Before any code was written wireframes were created using [Balsamiq](https://balsamiq.com/) for each page on three different screen sizes; mobile, tablet and desktop.

[See all wireframes here](https://github.com/clawrence00/capitals_quiz/blob/main/documentation/images/#)

### Design Choices

For the majority of design choices inspiration was taken from motorcycle manufacturers such as Triumph, Harley Davidson, Yamaha & Kawasaki.

#### Font

Noto Sans from Google Fonts was chosen as the font with sans serif as back up. All of the motorcycle manufacturers mentioned above use sans serif fonts. Noto Sans is used on the Harley-Davidson website and therfore seemed like the obvious choice for this web application.

#### Colours

The colours have been kept simple. The navbar and footer are dark grey, using Materialize CSS' class blue-grey darken-3, and the font is white. The main part of the page is white and cards are used to display the information. These are also styled like the navbar and footer. Again, this reflects the styles found on the motorcycle manufacturer's websites.

The colours for the links have also be taken from Materialize CSS' colour palletes and have been applied via CSS targeting.

#### Styling

The styling has been created using Materialize CSS. Cards have been used throughout to display data and forms. Modals have been added to confirm actions for deletion or in the case of the browse link to minimize mulitple links appearing in the navbar. For mobile devices the navbar collapses and when teh menu icon is pressed a sidebar appears.

#### Images

No images have been used for this application. They would likely be distracting and not what you would typically find on an online dictionary web application unless they were user added images to reinforce definitions.

![Home page](documentation/images/#)

![Browse Modal](documentation/images/#)

![Browse all](documentation/images/#)

![Browse by letter](documentation/images/#)

---

## Credits

### Code

Where small pieces of code have been used these have been credited in comment strings near the code.

The following sources were used to establish the quiz functions and questions array:

- [caption](link)
- [Web Dev Simplified](https://www.youtube.com/watch?v=riDzcEQbX6k&ab_channel=WebDevSimplified)

This tutorial was used to create the function delay:

- [Prince Varshney - tutorialspoint](https://www.tutorialspoint.com/How-to-delay-a-JavaScript-function-call-using-JavaScript)

For incrementing the correct answer score I revisited this Code Institute lesson:

- [AJGreaves - CodeInstitute](https://github.com/Code-Institute-Solutions/love-maths-2.0-sourcecode/tree/master/03-displaying-the-question-and-answer/04-updating-the-scores)

 ---

## Testing

<!-- ### Principals of Testing

<!-- #### Automated Testing

- Known as Test Driven Development (TDD)
- Tests are written before any code therefore errors are picked up early in the development process.
- Testing is quick. Testing frameworks such as Jest are used to reliably run tests in parallel.
- Tests are specific to the code that is being tested
- Testing is only as good as the questions being asked. User experience is not tested.

#### Manual Testing

- Known as Behaviour Driven Development (BDD)
- Testing is performed from the perspective of the user, after code has been written.
- Testing can be time consuming and resource hungry depending on the size of the project.
- User experience is tested such as browser compatibility and user screen sizes (mobile or desktop).
- There can be a high error rate as a human is performing the testing and certain scenarios can be missed. --> -->

### Testing for this project

Manual testing was performed to check the functions of creating, reading, updating and deleting database records by authenticated users, non-authenticated users and the admin was working as intended. To record this testing a testscript was created to follow a sequence of steps with the expected output. The actual output was reported and screenshots were appended to provide evidence of this testing.

During the intial execution of the test script it was found that for step 30 the incorrect dicitonary record was deleted. This was due to the href attribute in the delete modal anchor tag not targeting the dicitonary record that had been selected for deletion. Steps 27 to 30 were repeated following the correction for this and all were found to pass.

### Bugs & Fixes

-

### Validation

The HTML for the welcome message and a question with answers was checked using the [W3C markup validation service](https://validator.w3.org/). There were some warnings relating to the browse table inside the browse modal. This starts with seven columns for teh letters, then 5 columns for the numbers. This was delibrately done to evenly spread the links out and does not affect the rendering of the table. Mulitple info messages were found where trailing back slashes are present in the code. These are present due to using the 'prettier-vscode' extension in the Codeanywhere IDE.

The CSS was checked using the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/). There were no issues to report.

Google Lighthouse was used on the mobile version of the home page. The initial findings for accessibility were not 100% due to an aria-label not being present on the mobile sidenav trigger button. This was added, along with a meta tag to described the web application for better search engine optimisation.

All evidence of the validation can be found in the [validation](#) folder.

---

## Future impelementations

In the intial wireframes there is a search bar present in the navbar. It was intended to add this element and the required functionality to get it to bring up a list of definitions based on a users search. Due to time constraints this was not possibly to apply to this version of the web application, however if I were to continue to build this further this is a feature that I would definately like to add as it would being more value to the end user.

A feedback system on the dictionary records would also be a great future feature where other users could like or dislike the records.

User profiles showing the users metrics for contributions, likes, dislikes and profile pictures.

---

## Deployment

The website was deployed using GitHub Pages. Here are the following steps required to **deploy the site**;

1. Select the repository.
2. In the repository navigation click 'Settings'.
3. In the list on the left, under 'Code and automation' select 'Pages'.
4. Under 'Build and deployment', 'Source' should be 'Deploy from branch'.
5. Under 'Build and deployment', 'Branch' select 'main'. The folder should be /(root). Click 'Save'.

Your site should now be live and hosted by GitHub Pages. It may take a minute or two for the site to become available.

To **clone this repository**;

1. On GitHub.com select the main page of the repository.
2. Click the green 'Code' button.
3. Select HTTPS. Click the clipboard icon to copy the repository URL.
4. Create a location on your machine where you want the repository to be cloned.
5. Using Git Bash change the working directory to the location where you want the repository to be cloned.
6. Type *git clone* and paste the URL of the repository, copied in step 3.
7. Press enter. A local clone has now been created on your machine.  
