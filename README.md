# Movie site
Movie Site is a user-friendly web application where users can explore a wide range of movies, read detailed information, and share their reviews. Each movie entry includes comprehensive details such as a description, release year,  genre and director. Users can contribute by leaving reviews and ratings, helping others discover great film.

## Installation

1. Clone the repository:
   `git clone https://github.com/matmaslanka/movies_site.git`
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
4.  Open a terminal and navigate to the project directory in bash: 
   `cd .\movie_site`
5. Add your own secret key to movie_site/settings.py on line 24.
   Example: "0ne2fxv8vpeisxbd1xtq2kx-vnlv_7bnf%8nwc+jj(bpoe3_@v"
   (Note: The secret key is hidden for security reasons.)
6. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`


## Running the project
1. Run the Django development server:
   `python manage.py runserver`
2. Access the project in your browser at: http://127.0.0.1:8000/.

## Usage
When the user runs the application, they will see the homepage. At the top of the page, there is a message displaying the user's login status (either logged in or logged out).

Below the title "Movie Reviewing Site," there are five tabs:

#### Home:
Redirects to the list of all movies. If no entries exist, the user will only see a sorting form. If entries are present, they will be listed. Users can edit their own entries if they are the author.
#### Add movie:
Allows logged-in users to create new movie entries. The user must fill out a form with the movie data, including title, release date, duration, rating, image, trailer URL, synopsis, genre, and director. It is important to add the genre and director first if they are not already on the list. Otherwise, the form data will be lost.
#### Login/Logout:
If the user is logged out, this tab displays "Login" and redirects to the login page. If the user is logged in, it shows "Logout" and allows the user to log out.
#### Register:
If the user does not have an account, they can register by clicking the "Register" button and filling in their information.

#### Adding reviews:
Logged-in users can add reviews by clicking on the movie they want to review. They can add their rating and review text.
Logged-out users can only see reviews, but they cannot add a review.

### Admin Access
(Optional) To access the Django admin interface, create a superuser account:
   `python manage.py createsuperuser`


