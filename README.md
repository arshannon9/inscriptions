# INSCRIPTIONS OF LEPCIS MAGNA

## A Python-based web application, built using the Django framework, intended for use by scholars and enthusiasts to conduct research on the inscriptions of Lepcis Magna.

**Features:**

- The application can be used to:

  - Register individual users to track comments, collaborative contributions, and epigraphic dossiers
  - Store epigraphic data in SQL database for recall by users
  - Collect suggestions for edits and supplements from registered users
  - Search for inscriptions by location, content, and other identifying data
  - Collate epigraphic dossiers for use in research

**How to Run:**

1. **Installation:**

   - Python v.3.11.4 [Download Python](https://www.python.org/downloads/release/python-3114/) and Django v.4.2.7 [Download Django](https://www.djangoproject.com/download/) need to be installed.

2. **Set up a virtual environment:**

   - In the terminal, enter the command `python3 -m venv env`
   - If using Unix/macOS, enter `source env/bin/activate`
   - If using Windows, enter `.\env\Scripts\activate`

3. **Run the app:**
   - To start the Django server, enter `python3 manage.py runserver` in the terminal and click the link provided.

**Usage Guide:**

1. **Login/Register:**

   - The first page you encounter will be the Login page, which contains a login form and button labeled 'Login', as well as a 'Register here' link leading to the Register page. 'Login' and 'Register' links are also found on the right side of the navbar at the top of the page.
   - If visiting for the first time, click the 'Register here' link or the 'Register' link in the navbar, which will take you to the Register page. Fill out and submit the registration form, and if successful, you will be logged in automatically.
   - If already registered, fill out the login form and click the 'Login' button.
   - Registration is required to access the 'Create New Entry' and 'Epigraphic Dossier' functionalities.

2. **User Home:**

   - Upon login, you are directed to the User Home page.
   - In the navbar at the top of the User page, there are links to the 'Create New Entry' and 'Epigraphic Dossier' pages, as well as a 'Logout' link at the top right.
  
3. **Inscriptions:**

   - Both registered and non-registered users can access the 'Inscriptions' page, which displays basic information for every inscription in the database in a user-friendly card format.
   - Users can click the inscription card, which will take them to the 'Inscription Detail' page for that inscription, which includes the following data:
       - ID number
       - descriptive title
       - description of the physical inscription (size, material, etc.)
       - description of the text of the inscription (e.g., size and character of the inscription field)
       - description of the character and size of the letters
       - date
       - findspot (as specific as possible)
       - original location (if known)
       - last recorded location
       - interpretive transcription
       - diplomatic transcription
       - English translation (with plans for multi-lingual translations)
       - commentary
       - bibliography
       - images
    - If registered and logged in, user will be able to add the inscription to their personal epigraphhic dossier if not already part of it, and remove it if so. The user can access their dossier using the 'Epigraphic Dossier' link in the navbar.
  
4. **Categories:**

   - Both registered and non-registered users can access the 'Categories' page, which displays a list of categories (e.g., honorific, building, funerary, etc.).
   - Clicking on a category will bring you to a list of inscriptions belonging to that category.
  
5. **Bibliography:**

   - Both registered and non-registered users can access the 'Bibliography' page, which displays the bibliography of sources relevant to the inscriptions included in the database.
  
6. **Indices:**

   - Both registered and non-registered users can access the 'Indices', a series of pages that display indexed lists of epigraphic data relevant to particular inscriptions, including abbreviations, age at death, divine and sacred beings, emperors and imperial family, erasures, findspots, fragments, organizations, people, personal names, place names, symbols, words.
   - The choice of indexes is modeled after the [Inscriptions of Roman Tripolitania 2021 project] (https://irt2021.inslib.kcl.ac.uk/en/)

7. **Create New Entry:**

   - Registered users can access the 'Create New Entry' page, which displays a form for the creation and processing of new epigraphic entries, allowing for collaborative data input.
   - If an inscription is added via this form, and not via the Admin access to the database, the inscription will not be displayed until validated by an admin user.
  
8. **Epigraphic Dossier:**

   - Regsitered users can access a personal 'Epigraphic Dossier' page, which displays any inscription they have added to their own dossier (and have not removed).
   - This page functions similarly to the 'Inscriptions' page, but with content tailored to the specific user.


**Dependencies:**

- Django

**Database Schema:**

The models utilized by Django are found in 'lepcismagna/models.py'.

**Technologies Used:**

The application consists of:

- Frontend built using HTML, CSS, and JavaScript, with style enhancements using Bootstrap.
- Backend built using Python and Django, communicating with MySQL database using Django models.

**License:**

GPL-3.0

**Future Improvements:**

**Backend:**

- Data encryption
- Improved authentication and authorization systems
- Admin-only access protocols

**Frontend:**

- Implement search functionality for inscriptions using parameters based on the indices

**Credits:**

Thanks to:

- The IRT 2021 project for inspiring the creation of this project.
- David Malan, Brian Yu, and the Harvard cs50 crew for laying the knowledge foundations for this project.
