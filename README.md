#  Weather App using Django  

A simple yet powerful **Weather Application** built with **Django** that fetches real-time weather data using the **OpenWeather API**.  
This project demonstrates API integration, Django fundamentals, and deployment on the cloud.  

---

##  Features  
-  Real-time weather data (temperature, description, and icons)  
-  Search weather by city name  
-  Responsive UI (HTML, CSS, Bootstrap)  
-  Stores recent city searches in database (SQLite)  
-  Deployed on Render (cloud hosting)  

---

## 🛠️ Tech Stack  
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **API:** [OpenWeather API](https://openweathermap.org/api)  
- **Deployment:** Render  

---

## Screenshot  

<img width="1919" height="839" alt="image" src="https://github.com/user-attachments/assets/09419b1a-070e-4c72-8d17-2dde800ab3da" />

<img width="1919" height="826" alt="Screenshot 2026-03-11 003849" src="https://github.com/user-attachments/assets/8d3f2ac0-66ee-47ce-b719-50c4c066dad9" />


---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/uzman2406/Weather_App_using_django.git
   cd Weather_App_using_django
2.Create virtual environment & activate
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3.Install dependencies
```
pip install -r requirements.txt
```

4.Add your OpenWeather API key

In your views.py (or .env file if configured), replace:
```
API_KEY = "your_api_key_here"

```
5.Run migrations
```
python manage.py migrate
```

6.Start development server
```
python manage.py runserver
```

7.Open in browser 
-->  http://127.0.0.1:8000
