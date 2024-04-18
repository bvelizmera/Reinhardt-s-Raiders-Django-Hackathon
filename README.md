<h1>CAMPFIRE CAMPUS README.MD</h1>

<h2>Introduction</h2>

Campus Campfire is a site allowing college students to connect, create  events and leave their reviews on them. Students are also able to indicate that they will attend an event, and give it a star rating.

<img src='./ReadmeFiles/ReadmeImages/amiresponsive.png' alt='Responsiveness image of site, displayed on multiple devices.'>

The live site is deployed on Heroku [here](https://campus-campfire-d6ae0237c555.herokuapp.com/).

## Site Development
This site was developed using an Agile methodology, with a focus on getting a minimum viable product in place first before adding further features. User stories were sorted using MoSCoW prioritisation, and GitHub projects was used for the project board. An image of this at the end of the project can be seen below.

<img src='./ReadmeFiles/ReadmeImages/project_board.png' alt='Project board'>

User experience was considered throughout the development process in order to give a cohesive feel.

## Landing page for first time users

The landing page allows users to see a display with all upcoming events, including details such as how many students are attending. Users are unable to indicate that they will attend an event until they have registered as a student and logged in.

Users can see the site logo at the top of the page in bright blue with a navbar under it that contains the main sections of the site: Home, Register and Login. At the bottom of the page the user can find the footer with the names of the developers who worked together on this project. 

<strong>Landing page for first time users</strong>

<img src="./ReadmeFiles/ReadmeImages/landing_page.png" alt="home page landing page first time">

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

The Home page focuses mainly on the display of the events, as mentioned above. Each event is enclosed in a black square to differentiate it from the rest of events. The main features that can be highlighted are:

- The name of the event is as well a clickable button for the user. 

- Under the event name, the user can see the location, the date, and the creator of the event each one with a descriptive icon.  

- On the top right corner, the user can see the number of available spots and the number of participants attending with icon next to it. 

- Finally, on the bottom right corner there is a clickable button for those students who want to indicate that they will attend.
  - This button displays as "Register" for non-authenticated users, alongside a prompt explaining that they must register & create a student profile in order to attend. Clicking the button will direct them to the registration page.

- User experience in the events section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the name of the event and the button for registering.
 
  - The icons give important visual information about the event (location, date, author, number of participants) and help the user to navigate through the information provided.

  - The colour of the attending icon helps it stand out on the page.
  
  - The clickable button is easy  to identify, as it stands alone on the right corner, besides it gives straight and intuitive access to the new user who wants to register for an upcoming event. It also grows and changes the cursor when hovered over to add to this.

<strong>Home page Events section</strong>

<img src="./ReadmeFiles/ReadmeImages/homepage_event.png" alt="Home page Events section">


## Home page (Navbar and foooter) 

Apart from the events section the Home page also provides the user with a useful navbar and an informative footer. The navbar is divided into three main areas of interest: Home, Register and Login and the footer proportionate information of interest about the developers that collaborated on this project. Once the user is logged in the navbar links change to Home, My Events, Profile and Logout. The main features that can be highlighted are:

- The clickable sections in both, the navbar and the footer 

- The colour animation when the user hovers over the clickable parts.

- The change in the cursor icon when the user hovers over the clickable parts.

- User experience in the navbar and footer section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the different sections that can be found on the navbar.

  - The colour transition animation in the navbar and the footer, as well as the change in the cursor icon, both give clear indications about the clickable property of the elements in these sections. Besides, they produce an eye-catching effect on the user when these elements are hovered over, creating the need for clicking and a sense of mystery.

  - The Git hub cat icon in the footer,  gives important visual information about the names, as it makes explicit their contribution as developers in the project. 
  

<strong>Navbar: new user</strong>

<img src="./ReadmeFiles/ReadmeImages/navbar.png" alt="Home page Navbar section">

<strong>Navbar: logged in</strong>

<img src="./ReadmeFiles/ReadmeImages/navbar_loggedin.png" alt="Home page Navbar section">

<strong>Footer</strong>

<img src="./ReadmeFiles/ReadmeImages/footer.png" alt="Home page Footer section">




## Authentication

The allauth package was used to implement authentication for this site, and the templates adapted to fit the site theme. Users are able to sign up (register), log in and log out.

### Sign up
<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/registration.png">
</div>

### Log in

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/login.png">
</div>

### Log out

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/logout.png">
</div>

## Design Choices

### Fonts 

IntroRust was chosen as a more interesting font that would give character to the page. It was sourced from [here](https://www.fontspring.com/fonts/fontfabric/intro-rust-free?utm_source=fontsquirrel.com&utm_medium=download_link&utm_campaign=intro-rust#firstfreeproduct)

We selected the font style [Poppins](https://fonts.google.com/specimen/Poppins). It's a sans serif font, so very clear and easy to read. Its popularity on the web gives it instant recognition as well.

We selected more plain and simple design with professional colours but a big, vibrant pop of pink as an accent. We derived our colours from [coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/coolors.png">
</div>

### Wire Frames

The wireframes were constructed using Balsamiq in a group call to get feedback on all design choices. This was so front-end and back-end could be aligned even from the early stages to think of any pitfalls that could occur<br>

You can view the wireframes [here](./ReadmeFiles/Wireframes/CampusCampfire.pdf)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/wireframe.png">
</div>

### Database

We planned our models beforehand to avoid having to do migrations mid-project. We established the field types, one-to-many, PK or FK etc. 

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
    <td>None detected.</td>
    
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
    <td>As a reviewer, I want to be able to choose the star rating from a pre-populated list.</td>
    <td>Star ratings selectable from 1-5 stars.</td>
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
  
  <tr>
    <td>Bug: display of header and nav bar on mobile devices</td>
    <td>N/A</td>
    <td>These should collapse down on the smallest screen size</td>
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
  </table>


### Fixed Bugs
<table>
  <tr>
    <th>Bug</th>
    <th>Description</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>User upload of images</td>
  <td>Images uploaded through the site profile or event creation pages were not being added to cloudinary and so weren't being reflected in the database or created profile/event.</td>
  <td>This was an issue with the setup of the cloudinary upload field. A workaround was found employing the cloudinary upload widget to upload the image and then using JavaScript to populate the image URL for display in the created profile/event. This will be improved in the next sprint to bring the image upload into the form itself, since the solution to the bug has now been found.</td>
  </tr>
</table>

## Unfixed Bugs
<table>
  <tr>
    <th>Bug/Issue</th>
    <th>Description</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>"Attend" button for events does not change to reflect that a user is attending an event.</td>
  <td>The "Attend" button for each event on the home page should change to reflect that a signed-in user is attending.</td>
    
  <td>As with the image upload bug, the fix for this has been found on a subsequent project and will be implemented in the next sprint. It can be achieved using JavaScript.</td>
  </tr>
</table>


### Validator Testing 

For HTML validation https://validator.w3.org/

For CSS validation  https://jigsaw.w3.org/css-validator/

### Responsiveness

The site was tested for responsiveness across a range of screen sizes, and was found to adjust to the different screen sizes well. The below screenshot from [amiresponsive](https://ui.dev/amiresponsive) shows this.

A bug to be fixed in the next sprint is the display of the header and nav bar on mobile devices, both of which should adapt to fit the screen. The latter should collapse into a burger-style menu icon.

<img src="./ReadmeFiles/ReadmeImages/amiresponsive.png" alt="amiresponsive screenshot for site.">

#### Individual Pages
<strong> Home </strong>

![](./ReadmeFiles/responsiveGifs/home_responsive.gif)

## Deployment

Site successfully deployed on [heroku](https://campus-campfire-d6ae0237c555.herokuapp.com/)

## Technologies Used
This site involved the use of the following technologies & frameworks:
- HTML
- CSS
  - Bootstrap 5
- JavaScript
- Python
- Django 4
  - Package allauth for authorisation
  - Package crispy for form display
  - Package allauth for authorisation
  - Package summernote for admin page model display
  - Package whitenoise for handling static files
- Cloudinary for image storage
- ElephantSQL for database hosting
- Heroku for deployment
- GitHub for version control
- GitHub Projects for project management
- LucidChart to produce the database diagram
- Balsamiq for wireframing

### Other Credits 

Other useful tools were [Coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4) for colour palette selection and [fontawesome](https://fontawesome.com/) for icons.







### Content 

For validation in HTML https://validator.w3.org/

For validation in CSS https://jigsaw.w3.org/css-validator/

Wireframes produced using [Balsamiq](https://balsamiq.com/)

