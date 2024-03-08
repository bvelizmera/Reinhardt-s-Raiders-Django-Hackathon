<h1>CAMPFIRE CAMPUS README.MD</h1>

<h2>Introduction</h2>

Campus Campfire is a site for college students who whan to connect, create events and leave their review on these events. As well students can select if they want to attend to an event and rate it onece it takes place.

## Landing page for first time users

The landing page allows users to see a display with all the upcommimg events ordered in chronologically way, being the closest one, the first appearing on the top of the page.

Besides, right at the top the users can see the logo of the page in bright blue with a navbar under it that contains the main sections of the site: Home, Register and Login. Alonside with the navbar, on the opposte side of the page the user can find the footer with the names of the developers who worked together on this project. 

<strong>Landing page for first time users</strong>

addd 

<img src="imge urls goes here" alt="home page landing page first time">

<strong>Home page across multiple devices</strong>


<img src="image url goes here" alt="Options page across different devices">

<br>

## Home page (Site Logo)

The first element that the user sees when visiting site, is the logo: Campfire Campus in big, bright blue font. 

- User experience in the Logo section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the name of the site.

  - The name of the site "Campfire Campus" indicates clearly that this is a website related with the academic world. In addition, the name indicates that it is a place for socialising and students are welcomed. 
  
  - Thanks to the Logo the user would feel comfortable and with a positive attitude even before checking the rest of the page. 

 <strong>Home page Logo section</strong>

<img src="./ReadmeFiles/ReadmeImages/logo.png" alt="Home page Logo section">  



## Home page (Events) 

The Home page focuses mainly on the display of the events, as we mentioned before the events appeared ordered in time. Each event is enclosed in a black square to differentiate it from the rest of events. The main features that can be highlighted are:

- The name of the event is as well a clickable button for the user. 

- Under the event name, the user can see the location, the date, and the creator of the event each one with a descriptive icon.  

- On the top right corner, the user can see the number of available spots and the number of participants attending with icon next to it. 

- Finally, on the bottom right corner there is a clickable button for those students who want to register.

- User experience in the events section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the name of the event and the button for registering.
 
  - The icons give important visual information about the event (location, date, author, number of participants) and help the user to navigate through the information provided.

  -The colour animation on the attending icon gives 
  
   - The clickable button is easy  to identify, as it stands alone on the right corner, besides it gives straight and intuitive access to the new user who wants to register for an upcoming event.

<strong>Home page Events section</strong>

<img src="imge urls goes here" alt="Home page Events section">


## Home page (Navbar and foooter) 

Apart from the events, section the Home page also provides the user with a useful navbar and a informative footer. The navbar is divided into three main areas of interest; Home, Register and Login and the footer proportionate information of interest about the developers that collaborated on this project. The main features that can be highlithed are:

- The clickable sections in both, the navbar and the footer 

- The colour animation when the user hovers over the clickable parts.

- The change in the cursor icon when the user hovers over the clickable parts.

- User experience in the navbar and footer section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the different sections that can be found on the navbar.

  - The colour transition animation in the navbar and the footer, as well as the change in the cursor icon, both give clear indications about the clickable property of the elements in these sections. Besides, they produce an eye-catching effect on the user when these elements are hoovered over, creating the need for clicking and a sense of mystery.

  - The Git hub cat icon in the footer,  gives important visual information about the names, as it makes explicit their contribution as developers in the project. 
  

<strong>Home page Events section</strong>

<img src="./ReadmeFiles/ReadmeImages/navbar.png" alt="Home page Navbar section">

<br>

<img src="./ReadmeFiles/ReadmeImages/footer.png" alt="Home page Footer section">




## Authentication

### Registration

We have a registration page built using the default django user registration form, we have a custom view to display messages back to the user to feedback when the form is incorrect but as the default view isn't very customizable it displays mid-form. A fully bespoke solution would be needed next project

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/registration.png">
</div>

### login

We have a simple frictionless login page so users can log in quickly, it will feedback to the user if there are errors. a future feature would be password recovery via email

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/login.png">
</div>

## Design Choices

### Fonts 

IntroRust was chosen as a more interesting font that would give character to the page. It was sourced from [here](https://www.fontspring.com/fonts/fontfabric/intro-rust-free?utm_source=fontsquirrel.com&utm_medium=download_link&utm_campaign=intro-rust#firstfreeproduct)

We selected the font style Poppins 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap'. It's is sans serif, so very clear and easy to read. it's popularity on the web gives it instant recognition as well'


We selected more plain and simple design with professional colours but a big, vibrant pop of pink as an accent. We derived our colours from [coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/coolors.png">
</div>

### Wire Frames

<strong>The wireframes were constructed using Balsamiq in a group call to get feedback on all design choices. This was so front-end and back-end could be aligned even from the early stages to think of any pitfalls that could occur<br></strong>

You can view the wireframes [here](./ReadmeFiles/Wireframes/CampusCampfire.pdf)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/wireframe.png">
</div>

### Database

We tried to plan out our models before had to avoid having to do migrations mid-project. we tried to work out the field types, one-to-many, PK or FK etc. 

Here is an image of our ERD:
<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/ERD.png">
</div>

## User Stories, features and bugs

<table>
  <tr>
    <th>User Story</th>
    <th>Features</th>
    <th>Bugs / Issues - tested across viewports of all devices using Google Dev Tools</th>
  </tr>
   <tr>
    <td>As a user I want to know the name of the website so that I can share it with people. </td>
    <td>Title of the app displayed on the header with an attractive font style.</td>
    <td>The title sometimes does not collapse properly.</td>
   
    
  </tr>
  <tr>
    <td>As a user I want to be able to create an account so I can have my own user profile.</td>
    <td>Create own account.<br>Log into profile.</td>
    <td>Error message displayed in the middle.</td>
  
  </tr>
   <tr>
    <td>As a student I can join events so that I can foster growth in my interests or studies</td>
    <td>Events page with all events displayed.<br>Organisers know who is attending.</td>
    <td>On event detail page attending button can't see student status.</td>
  <tr>
    <td>As a user I can update my profile so that other users can learn more about me and i see more related content</td>
    <td>Display name.<br>Display bio.</td>
    <td>Does not have a list of future events to be attended.<br>Because of the way that the user is prompted to create a student profile, the view function that is triggered will always take them on to the user events page rather than wherever they had come from. </td>
  </tr>
  <tr>
    <td>As a site owner I can collect feedback on events so that I can see which events are successful and popular and which arent.</td>
    <td>Rate events.<br>Comments system by attendees.</td>
    <td>None deteced.</td>
    
  </tr>
  <tr>
    <td>As a Organiser I can create events so that students can attend them.</td>
    <td>Specify date, time, location, course or interest, and max. participants.<br>List of students attending.<br>Add an event picture.</td>
    <td>List of students when event is expanded not.</td>
    
  </tr>
  <tr>
    <td>As a user, I want the site to be easily navigable.</td>
    <td>Different features of site are clearly identifiable</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a user, I want to be able to choose an answer from a pre-populated list.</td>
    <td>List of answers to be selected</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a user, I want to receive feedback on the answers.</td>
    <td>Clear signal of correct / incorrect answer</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a user, I want the site to be visually appealing.</td>
    <td> Select complementary colour scheme. <br>
    Different elements/features delineated.</td>
    <td>None detected</td>
    
  </tr>
  </table>

<br>


### User Stories and Features (to be implelemented next Sprint) 


  <table>
  <tr>
    <th>User Story</th>
    <th>Features</th>
    <th>Bugs / Issues</th>
  </tr>



  <tr>
    <td>As a student I want to able to search filter events so that I can attend events of my interest.</td>
    <td>Filter by category, words or interests.</td>
    <td>N/A</td>
  </tr>
  
  <tr>
    <td>As a Student I can get notified of upcoming events so that I am less likely to miss or forget the event.</td>
    <td>Get notifications from upcoming events.</td>
    <td>N/A</td>
  </tr>
  

  </table>

### Won't haves

  <table>
  <tr>
    <th>User Story</th>
    <th>Features</th>
    <th>Bugs / Issues</th>
  </tr>
  <tr>
    <td>As a user I want to be able to follow other students.</td>
    <td>Follow option.</td>
    <td>N/A</td>
  </tr>


## Fixed Bugs / Issues
<br>
<table>
  <tr>
    <th>Bug/Issue</th>
    <th>Image</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>"Select type" option overflows to below options box on smaller devices</td>
    <td><img src="assets/images/readMeImages/bugs/fixed/questionsoverflow.png" alt="Image showing box obscuring the logo on larger devices"></td>
    
  <td>We added media queries to ensure effective responsiveness</td>
  </tr>
  </table>

## Unfixed Bugs / Issues
<table>
  <tr>
    <th>Bug/Issue</th>
    <th>Image</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>On large devices the "Enter name" box obscures the brand logo and feels like a pop-up rather than an integrated element of the UX package</td>
    <td><img src="assets/images/readMeImages/amiresponsive/loginscreenpng.png" alt="Image showing box obscuring the logo on larger devices"></td>
    
  <td>Unfortunately we ran out of time to fix this. We would in future sprints change from an in-browser alert box to a html modal box, that would be styled and centred on the screen etc as part of a user management system.</td>
  </tr>
</table>


### Validator Testing 

For HTML validation https://validator.w3.org/

For CSS validation  https://jigsaw.w3.org/css-validator/

## Deployment

Site successfully deployed on [heroku](https://campus-campfire-d6ae0237c555.herokuapp.com/)

## Credits 

[Coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4) was used for colour pallette

[Bootstrap](https://getbootstrap.com/)

[fontawesome](https://fontawesome.com/)

### Content 

For validation in HTML https://validator.w3.org/

For validation in CSS https://jigsaw.w3.org/css-validator/

Wireframes produced using [Balsamiq](https://balsamiq.com/)

