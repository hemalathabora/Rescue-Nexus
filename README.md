
# Rescue Nexus

Overview
Rescue Nexus is a disaster management platform that aims to provide real-time information, coordination, and resources to individuals and emergency responders during a disaster. The platform uses advanced web technologies and data integration to display critical information, such as weather alerts, evacuation routes, and available resources, to enhance disaster response efforts.

# Features
- Real-Time Disaster Updates: Displays live data on disasters such as floods, earthquakes, and wildfires.
- Interactive Map: An interactive map with key disaster-related data points, including shelter locations and medical facilities.
- Weather Forecasting: Uses accurate weather prediction models to provide early warnings on weather-related disasters.
- Evacuation Routes: Provides updated evacuation routes and real-time traffic data for optimal evacuation.
- Resource Availability: Lists available resources such as food, water, medical aid, and more, during an ongoing disaster.
- Crowdsourced Information: Allows users to contribute live updates about the situation in their area.

# Technologies Used
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Django (Python)
- Database: PostgreSQL (or any other database of your choice)
- External APIs: Weather data API, Disaster management API (e.g., NASA, OpenWeatherMap)
- Version Control: Git & GitHub

# Installation

# Prerequisites
- Python 3.x
- Django
- PostgreSQL (or other database setup)
- Git

# Steps to Set Up Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rescue-nexus.git
   ```

2. Navigate to the project directory:
   ```bash
   cd rescue-nexus
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   - Create a PostgreSQL database and configure the `DATABASES` settings in `settings.py`.

6. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Visit `http://127.0.0.1:8000/` in your browser to see the project in action.

# Contributing

We welcome contributions to Rescue Nexus! If you want to improve the project, feel free to fork the repository, make your changes, and submit a pull request.

# Steps for Contribution
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Acknowledgements
- OpenWeatherMap: For providing weather data APIs.
- NASA Earth Science Division: For providing disaster-related data.
- Bootstrap: For responsive design elements.
- Django: For building the backend.
