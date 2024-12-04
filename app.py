from flask import Flask, render_template, request

app = Flask(__name__)

# sample project data

projects = [
  {
    "title" : "python web scraper",
    "description": "scrapes data from website and stores in database",
    "technologies": ["Python", "BeautifulSoup4"],
    "github_link": "https.//github.com/odp31/web_scraper",
    "live_demo": None #optional link to live dmeo 
  },
  {
    "title": "machine learning model for image classification", 
    "description": "machine learning model",
    "technologies": ["Python", "TensorFlow", "Keras"],
    "github_link": "https://github.com/odp31/image_classifier",
    "live_demo": None
  },
]
# route for main portfolio page

@app.route('/')
def portfolio():
  return render_template('portfolio.html', projects=projects)

# route for specific project page
@app.route('/project/<python web scraper>')
def project_details(project_title):
  for project in projects:
    if project["title"] == project_title:
      return render_template('project_details.html', project=project)
  return "project not found", 404 # handle non existent project

if __name__ == '__main__':
  app.run(debug=True)
  
