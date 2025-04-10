# 🌐 Digitální vizitka + Aplikace na počasí

Tento projekt kombinuje **profesionální portfolio** s webovou **aplikací na předpověď počasí**. Slouží jako ukázka mých dovedností v Pythonu, FastAPI, Djangu a moderním webovém vývoji.

---

## 🇬🇧 English version

### 🧩 What's included

#### ✅ Portfolio (Django)
- "About Me" section
- CV – view & download
- LeetCode solved tasks
- GitHub & LinkedIn links
- Projects overview

#### 🌦️ Weather App (FastAPI)
- Search weather by city
- Current weather overview with icons
- 5-day forecast with expandable cards
- Temperature & precipitation charts for today
- Background changes based on weather conditions

---

### ⚙️ Technologies Used

- **Backend:** Django, FastAPI
- **Frontend:** HTML, Tailwind CSS, Chart.js
- **Weather API:** OpenWeatherMap
- **Templating:** Jinja2

---

### 🚀 Local Setup

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Run the Django portfolio (terminal 1):

```bash
python manage.py runserver 8000
```

Available at: [http://localhost:8000](http://localhost:8000)

#### Run the FastAPI weather app (terminal 2):

```bash
uvicorn weather_app.main:app --reload --port 8001
```

Available at: [http://localhost:8001](http://localhost:8001)

---

## 📁 Project Structure

```
portfolio-weather/
│
├── weather_app/
│   ├── main.py
│   ├── templates/
│   └── static/
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✍️ Author

**Martin Jarábek**  
A teacher transitioning into programming  
🔗 [GitHub – Matty-Jaris](https://github.com/Matty-Jaris)  
📧 martin.jar91@seznam.cz

## 🇨🇿 Česká verze

### 🧩 Co projekt obsahuje

#### ✅ Portfolio (Django, statický web)
- Sekce *O mně*
- CV ke stažení i online náhled
- Výpis vyřešených úloh z LeetCode
- Odkazy na GitHub & LinkedIn
- Sekce s projekty

#### 🌦️ Aplikace na počasí (FastAPI)
- Vyhledávání počasí podle města
- Aktuální počasí s ikonami a přehledy
- 5denní předpověď s rozklikávacími kartami
- Grafy teploty a srážek pro aktuální den
- Styl pozadí dle aktuálního počasí

---

### ⚙️ Použité technologie

- **Backend:** Django, FastAPI
- **Frontend:** HTML, Tailwind CSS, Chart.js
- **API:** OpenWeatherMap
- **Templating:** Jinja2

---

### 🚀 Lokální spuštění

```bash
# Vytvoř a aktivuj virtuální prostředí
python -m venv venv
venv\Scripts\activate

# Instaluj závislosti
pip install -r requirements.txt
```

#### Spusť portfolio (Django):

```bash
python manage.py runserver 8000
```

Dostupné na: [http://localhost:8000](http://localhost:8000)

#### Spusť aplikaci na počasí (FastAPI – druhý terminál):

```bash
uvicorn weather_app.main:app --reload --port 8001
```

Dostupné na: [http://localhost:8001](http://localhost:8001)

---

## 📁 Struktura projektu

```
portfolio-weather/
│
├── weather_app/
│   ├── main.py
│   ├── templates/
│   └── static/
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✍️ Autor

**Mgr. Martin Jarábek**  
Učitel na cestě stát se programátorem  
🔗 [GitHub – Matty-Jaris](https://github.com/Matty-Jaris)  
📧 martin.jar91@seznam.cz

---

