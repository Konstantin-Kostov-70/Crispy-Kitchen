## Crispy-Kitchen

### Overview
Crispy Kitchen is a dynamic website built using Django, designed for a restaurant business. The website serves as both a promotional platform and a content hub, featuring menus, special offers, blog posts about food, and customer interactions like reservations and comments. The project is structured into two main Django applications:

- **Crispy Kitchen (Main App)**: Handles menus, reservations, newsletter subscriptions, and customer messages.
- **Crispy Blog**: Manages blog posts related to food, where users can read and comment on news articles.

---

### Features

#### 1. Homepage
The homepage showcases a selection of **special menus** and **best offers**. It also includes recent **blog posts** from the `crispy_blog` app.

#### 2. Menus
- **Main Menu**: Lists all food items available at the restaurant, pulled from the `Menu` model.
- **Special Menu**: Highlights special offers with the ability to **like** food items. Each menu item can be viewed in detail, and users can express their preferences by liking the items.

#### 3. Blog Section
- Blog posts are managed under the `crispy_blog` app.
- Each post has its own **detail page** where users can read the post and leave comments.
- The blog uses the `Post` model to store entries, and users can comment using the `FoodComment` form.

#### 4. User Interaction
- **Food Likes**: Users can like or unlike food items in the menu.
- **Comments**: Users can comment on blog posts.
- **Reservation System**: A fully functional reservation form allows users to book a table. Upon submitting a reservation, a success message is displayed.
- **Newsletter Subscription**: Users can subscribe to a newsletter by filling out a form on the **About page**.

#### 5. Contact Page
- Users can leave messages for the restaurant using the **contact form**.

#### 6. Admin Section
- The site admin is accessible through a custom URL path (`/koss/`), with a honeypot feature protecting the default `/admin` route for enhanced security.

- To access the Django admin interface, navigate to the `/koss/` path on your local server, for example:

 - http://127.0.0.1:8000/koss/


## Security
The website implements several security features:

- **Django Honeypot**: Protects the default admin URL from potential attacks by redirecting `/admin/` to a honeypot.

---

### Setup Instructions

#### 1. System Requirements
- Python 3.x
- Django 4.x

# Install Python Dependencies

After cloning the repository, you will need to install the necessary Python dependencies. Follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/Konstantin-Kostov-70/Crispy-Kitchen.git
cd Crispy-Kitchen
```
### 2. Install Python dependencies:

Make sure you have **Python 3.x** installed on your system. Then, install the required dependencies by running:

```bash
pip install -r requirements.txt
```
### 3. Apply database migrations:

Run the following command to apply database migrations:

```bash
python manage.py migrate
```
### 4. Run the Django development server:

To start the server and view the website locally, use the following command:

```bash
python manage.py runserver
```

### 5. Make sure to create a superuser if you haven't already, by running:

```bash
python manage.py createsuperuser
```
## Application Structure

### `crispy_kitchen`

Handles the restaurant-related functionality, including menus, reservations, messages, and newsletter subscriptions.

- **Models:** `Menu`, `SpecialMenu`, `Reservation`, `Message`, `FoodLike`, `NewsLetter`.
- **Forms:** `ReservationForm`, `MessageForm`, `NewsLetterForm`.
- **Views:**
  - **IndexView:** Displays the homepage.
  - **MenuView:** Shows the main menu.
  - **ReservationView:** Handles reservations and displays a success message on submission.
  - **AboutView:** Manages the newsletter subscriptions.
  - **ContactView:** For users to leave messages.

---

### `crispy_blog`

Manages the blog posts about food.

- **Models:** `Post`, `FoodComment`.
- **Forms:** `FoodCommentForm`.
- **Views:**
  - **NewsDetailsView:** Shows blog post details and allows users to leave comments.
  - **MenuDetailView** and **SpecialMenuDetailView:** Display details about menu items and special offers.

## Usage

1. **Homepage**
   - Navigate to the homepage to view featured menu items and recent blog posts.

2. **Menus**
   - Check out the restaurant’s menu by visiting `/menu/` to view all available food items.
   - Explore the special offers by visiting `/special-menu/`.

3. **Blog**
   - Access the blog section by visiting `/blog/` to read articles about food.
   - Users can click on a blog post to read it in detail and leave comments.

4. **Reservations**
   - Users can make reservations through the Reservation Form. A success message will confirm when the reservation is submitted.

5. **Newsletter**
   - Users can subscribe to the newsletter by filling out the form on the About page.

## License
This project is licensed under the MIT License.

## Author
Crispy Kitchen was developed by **Konstantin Kostov** as part of a Django project for a restaurant.


