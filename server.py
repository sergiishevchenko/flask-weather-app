from flask import Flask, render_template

from python_org_news import get_python_news
from weather import weather_by_city

app = Flask(__name__)


@app.route("/")
def index():
    title = "Forecast"
    weather = weather_by_city("Lausanne, Switzerland")
    news = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news=news)


if __name__ == '__main__':
    app.run(debug=True)
