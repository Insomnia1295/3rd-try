from flask import Flask, render_template
from flask.views import View

app=Flask(__name__)

class Homeview(View):
    def dispatch_request(self):
        return render_template("index.html")
    
app.add_url_rule("/",view_func=Homeview.as_view(name="index"))

if __name__ == "__main__":
    app.run(debug=True)
