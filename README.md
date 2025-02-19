
# Django Prayer Times Application | Jadwal Sholat

This Django application provides a modern and efficient way to display prayer times for cities in Indonesia. It incorporates several enhancements for performance, user experience, and code structure.

## Features

- **Real-time Search with Debouncing:**  Instantly find cities as you type, with debouncing to minimize API calls and improve performance.
- **Caching:** API responses are cached to reduce load on the external prayer times service and speed up retrieval.
- **Database Storage:** City and prayer time data are stored in a database for efficient access and management.
- **Modern Responsive UI:**  A clean and modern user interface built with Tailwind CSS, ensuring a consistent experience across devices.
- **Real-time Clock Display:**  Displays the current time alongside the prayer times.
- **Improved Error Handling:**  Provides user-friendly error messages and feedback.

## Architecture

This application follows Django's Model-View-Template (MVT) architectural pattern, promoting a clean separation of concerns:

- **Models:** Define the data structure for cities and prayer times.
- **Views:** Handle user requests and interact with the models and services.
- **Templates:** Control the presentation of the data using HTML and templating.
- **Services:** (Optional but recommended)  A layer for handling business logic, such as fetching data from the external API or interacting with the database. This keeps views lean and organized.
- **URL Routing:**  Uses proper URL routing and namespacing for maintainability and scalability.

## Installation

1. **Create a new Django project and app:**

```bash
django-admin startproject prayer_project
cd prayer_project
python manage.py startapp prayer_times
```

2. **Install required packages:**

```bash
pip install django requests
```

3. **Project Setup:**

- Copy the code from the provided files (models.py, views.py, urls.py, templates/index.html, etc.) into the appropriate locations within your Django project structure.  Ensure the `prayer_times` app is correctly structured.
- Add `'prayer_times'` to the `INSTALLED_APPS` list in your `prayer_project/settings.py` file.

4. **Run migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server:**

```bash
python manage.py runserver
```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your browser to access the application.
2. Use the search bar to type the name of an Indonesian city.  Results will appear in real-time.
3. Select a city to view its prayer times by typing.

![jadwal-sholat](https://github.com/user-attachments/assets/dbb9b724-4306-480b-935f-8c2f8cf584ad)


## Technologies Used

- **Django:**  The Python web framework.
- **requests:** For making HTTP requests to the external prayer times API.
- **Tailwind CSS:** For styling the user interface.
- **API:** https://api.myquran.com/

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

Apache License
