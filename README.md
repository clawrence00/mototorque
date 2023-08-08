# Milestone Project 3: Moto Torque

![Mockup on different screen sizes of home page](https://github.com/clawrence00/mototorque/blob/main/docs/images/mockup.png)
Welcome to my third milestone project with the Code Institute. The purpose of this project it to build a full-stack site that allows your users to manage a common dataset about a particular domain. I have chosen to create a dictionary for motorcyling words and phrases. Users can sign up, add there own entries, edit and delete them. The definitions can then be displayed by all users.

**Please find my deployed site [here](https://mototorque-c015422a9ebb.herokuapp.com/).**

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

[See all wireframes here](https://github.com/clawrence00/mototorque/blob/main/docs/wireframes.pdf)

### Data Schema

The following data schema has been created to show the relationship between the data models and the entities within those models.

![Data schema](https://github.com/clawrence00/mototorque/blob/main/docs/images/data_schema.png)

The relationship is one to many. The user can have many records created in the dictionary. That dictionary record can only have one user. As the dictionary is user generated many users can create definitions for the same word or phrase, however, each of these words or phrases is a separate dictionary record. With this relationship it can be established which user created the dictionary record allowing this to be diplayed on the card and allowing only them (or the administrator) to edit or delete their own dictionary records.

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

![Home page](https://github.com/clawrence00/mototorque/blob/main/docs/images/home_page.png)

![Browse Modal](https://github.com/clawrence00/mototorque/blob/main/docs/images/browse_modal.png)

![Browse all](https://github.com/clawrence00/mototorque/blob/main/docs/images/browse_all.png)

![Browse by letter R](https://github.com/clawrence00/mototorque/blob/main/docs/images/browse_r.png)

---

## Credits

### Code

Where small pieces of code have been used these have been credited in comment strings near the code.

The walkthrough lesson from the code institute was used for the initial set up of the coding space, the required files and installing flask and psycopg2. It was also a greate base for creating the CRUD functionality that my project required.

- [Tim Nelson - Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+2022_Q3/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

This youtube playlist from John Elder at Codemy was really helpful, particularly for installing flask-migrate, flask-login and hashing passwords. Code snippets and naming conventions were taken from this project:

- [John Elder - Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz)

This youtube video from Corey Schafer was also used to establish flask-login fuctionality.

- [Corey Schafer](https://www.youtube.com/watch?v=CSHx6eCkmv0&ab_channel=CoreySchafer)

Several sources helped me build the code for the 'browse' route;

Rendering a page based on the link clicked

- [Answer from Ali Yılmaz](https://stackoverflow.com/questions/50426137/flask-get-clicked-link-info-and-display-on-rendered-page)
  
Filtering database values based on their first letter.

- [Answer from John Lehmann](https://stackoverflow.com/questions/20269260/how-do-i-do-a-starts-with-query-using-sql-alchemy)
  
This fixed an issue where only database entries with capital letters would be shown when browsing by a specific letter.

- [Answer from Haleemur Ali](https://stackoverflow.com/questions/30272217/use-variable-in-sqlalchemy-ilike-statement)

The solution for the failed test in the testing section below (deleting the incorrect record when using a modal) was quickly found after watching this video.

- [ParwizForogh](https://youtu.be/XTpLbBJTOM4?t=3911)

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

- I was struggling to migrate changes to my database. Installing flask-migrate really made this a simple and reliable process, where I could see which changes were made in the migrations folder.
- When creating the routes and html templates in Codeanywhere I was unable to use the words 'login' or 'logout' as this would cause an error when running the application. To get around this I used 'signin', 'enter_user' and 'signout' instead.
- I thought the browse function was not working correctly as I could not see any records when browsing by type for example the letter 'T'. When browsing by 'all' the records appeared. At the time the majority of the records created were called 'test'. As python is a strictly typed language when querying the database for words starting with 'T' none were found due to this. Once I realised this was the issue I was able to implement the use of 'ilike' to query the database for words starting with certain letters, irrelevent of whether they were capitalised or not.
- During testing, an error was found with the incorrect dictionary record being deleted. The delete modal was not target the selected dicitonary ID and therefore deleting the first record (by ID number) in the dictionary database.

### Validation

The HTML for the welcome message and a question with answers was checked using the [W3C markup validation service](https://validator.w3.org/). There were some warnings relating to the browse table inside the browse modal. This starts with seven columns for teh letters, then 5 columns for the numbers. This was delibrately done to evenly spread the links out and does not affect the rendering of the table. Mulitple info messages were found where trailing back slashes are present in the code. These are present due to using the 'prettier-vscode' extension in the Codeanywhere IDE.

The CSS was checked using the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/). There were no issues to report.

Google Lighthouse was used on the mobile version of the home page. The initial findings for accessibility were not 100% due to an aria-label not being present on the mobile sidenav trigger button. This was added, along with a meta tag to described the web application for better search engine optimisation.

All evidence of the validation can be found in the [validation](https://github.com/clawrence00/mototorque/tree/main/docs/validation) folder.

---

## Future impelementations

In the intial wireframes there is a search bar present in the navbar. It was intended to add this element and the required functionality to get it to bring up a list of definitions based on a users search. Due to time constraints this was not possible to apply to this version of the web application, however if I were to continue to build this further this is a feature that I would definately like to add as it would being more value to the end user.

A feedback system on the dictionary records would also be a great future feature where other users could like or dislike the records.

User profiles showing the user's metrics for contributions, likes, dislikes and profile pictures.

---

## Deployment

The website was deployed using Heroku. The PostgreSQL database was hosted by ElephantSQL. Here are the following steps required to **deploy the site**;

Set up ElephantSQL to host your database instance

1. Go to ElephantSQL.com and click "Get a managed database today"
2. Select "Try now for FREE" in the TINY TURTLE database plan
3. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
4. In the Create new team form:
 - Add a team name (your own name is fine)
 - Read and agree to the Terms of Service
 - Select Yes for GDPR
 - Provide your email address
 - Click “Create Team
5. Your account is successfully created! Click “Create New Instance”
6. Set up your plan
 - Give your plan a Name (this is commonly the name of the project)
 - Select the Tiny Turtle (Free) plan
 - You can leave the Tags field blank
7. Select “Select Region”
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Select a data center near you
9. Return to the ElephantSQL dashboard and click on the database instance name for this project. Leave this tab open.
   
In your IDE create files that Heroku will need
1. Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
  - pip freeze --local > requirements.txt
2. Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it.
3. Inside the file, add the following command
  - web: python app.py
4. Open your __init__.py file
5. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.
6. To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:
7. Save all your files and then add, commit and push your changes to GitHub

Conneting the database to Heroku

1. Log into Heroku.com and click “New” and then “Create a new app”
2. Choose a unique name for your app, select the region closest to you and click “Create app”
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var.

Deploy the site

1. Navigate to the “Deploy” tab of your app
2. In the Deployment method section, select “Connect to GitHub”
3. Search for your repo and click Connect
4. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository
5. Use the Manual deploy section and click Deploy Branch. This will start the build process.
6. The project is now in place and there is an empty database. The tables from the models.py file need to be added. Click the “More” button and select “Run console”.
7. Type python3 into the console and click Run
8. This opens the Python terminal. To create the tables use the following commands;
 - from mototorque import db
 - db.create_all()
9. Exit the Python terminal, by typing exit() and hitting enter, and close the console.
10. Click the “Open app” button to view the deployed site.

To **clone this repository**;

1. On GitHub.com select the main page of the repository.
2. Click the green 'Code' button.
3. Select HTTPS. Click the clipboard icon to copy the repository URL.
4. Create a location on your machine where you want the repository to be cloned.
5. Using Git Bash change the working directory to the location where you want the repository to be cloned.
6. Type *git clone* and paste the URL of the repository, copied in step 3.
7. Press enter. A local clone has now been created on your machine.  
