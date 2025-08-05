🚙 Crypto Price Checker - CI/CD Pipeline with Jenkins & Docker

🚀 Project Overview

Crypto Price Checker is a simple Flask-based web app that displays real-time cryptocurrency prices fetched from the CoinGecko API. The project is containerized using Docker and deployed to an AWS EC2 instance via a Jenkins CI/CD pipeline.

This project was built as part of a DevOps internship to demonstrate automation of software deployment using modern tools like GitHub, Docker, Jenkins, and AWS.

🎓 Internship Task #2

Objective: Automate the build and deployment of a Dockerized Flask app to AWS EC2 using Jenkins CI/CD.

 🧱 Tech Stack & Tools

* Frontend: HTML, CSS (in `templates/` and `static/`)
* Backend:Python (Flask)
* Deployment:

  * Docker (for containerization)
  * Jenkins (for CI/CD pipeline)
  * AWS EC2 (as deployment server)
  * GitHub (source code repository)

📝 Features

* ✨ Real-time cryptocurrency price fetching
* 📅 Triggered builds on every push to GitHub
* 🏢 Jenkins pipeline to build and deploy Docker container
* 🪧 Runs on a public-facing EC2 instance

 📊 Folder Structure

crypto-checker-pipeline/
├── static/                 # CSS/JS for frontend
├── templates/              # HTML templates
├── app.py                  # Flask app logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
├── .gitignore              # Git ignore file
├── README.md               # Project overview (you are here!)

🚛 How It Works
1. Code Push to GitHub 💾

You push changes to the GitHub repo:
`https://github.com/nithishmathematics/crypto-checker-pipeline`

 2. Jenkins Triggers CI/CD Pipeline 💪

Jenkins (hosted on EC2) fetches the code and runs these stages:

1. Clone Repo: Git pulls the latest code
2. Build Docker Image: Image is built from the Dockerfile
3. Stop Old Container: Any existing container is stopped/removed
4. Run New Container: Fresh app container is started and exposed on port 5000

3. Live App on EC2 🌐
You can now visit the app using your EC2 Public IP:
http://65.2.167.191:5000/
🤖 Setup Instructions (Local)

1. Clone the Repo
git clone https://github.com/nithishmathematics/crypto-checker-pipeline.git
cd crypto-checker-pipeline

2. Install Dependencies
pip install -r requirements.txt

3. Run the App
bash
python app.py
Visit: `http://localhost:5000`

🛠️ Run via Docker (Local)

1. Build Docker Image
docker build -t crypto-checker .

2. Run Docker Container
docker run -d -p 5000:5000 crypto-checker
Visit: \`[http://localhost](http://localhost):
