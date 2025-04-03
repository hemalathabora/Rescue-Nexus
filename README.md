 Rescue-Nexus

Rescue-Nexus is a disaster management platform aimed at improving response efficiency through AI-driven insights, crowdsourced data, and real-time updates. The platform provides interactive maps, weather predictions, and essential resources to assist disaster response teams and the public.

 🚀 Features

- Real-time Weather Forecasts: powered by ML & NASA data
- Interactive Map: showing disaster-prone areas & relief centers
- Crowdsourced Reporting: for live updates from affected regions
- AI-powered Resume Screener: (for emergency job matching & volunteer recruitment)
- E-Waste Connect: Crowdsourced Recycling Platform
- Django-based Backend: with REST API
- Deployed on Render

 📂 Project Structure
```
Rescue-Nexus/
│-- manage.py
│-- requirements.txt
│-- README.md
│-- .gitignore
│-- disaster_management/
│   │-- settings.py
│   │-- urls.py
│   │-- wsgi.py
│-- weather/
│   │-- models.py
│   │-- views.py
│   │-- serializers.py
│   │-- fetch_nasa_data.py
│   │-- predict_weather.py
│-- templates/
│   │-- index.html
│   │-- weather_results.html
```

 🛠 Setup & Installation

 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Rescue-Nexus.git
cd Rescue-Nexus
```

 2️⃣ Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
```

 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

 4️⃣ Run Migrations
```bash
python manage.py migrate
```

 5️⃣ Start the Development Server
```bash
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000/`

 🌍 Deployment on Render

1. Push your changes to GitHub:
```bash
git add .
git commit -m "Deploying to Render"
git push origin main
```
2. Connect GitHub to [Render](https://render.com/)
3. Deploy and set environment variables (e.g., `ALLOWED_HOSTS`, API keys)

 🛠 Environment Variables
Ensure these variables are set in `.env` or Render dashboard:
```env
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=rescue-nexus.onrender.com
DATABASE_URL=your_database_url
```

🤝 Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

📞 Contact

For queries, contact hemalathabora9@gmail.com or open an issue on GitHub.
