from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        form_dict = request.form.to_dict(flat=False)
        print(form_dict)
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)
