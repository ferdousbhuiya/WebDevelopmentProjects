from flask  import Flask

app = Flask(__name__)

def html_tag(tag):
    def decorator(function):
        def wrapped(*args, **kwargs):
            return f"<{tag}>{function(*args, **kwargs)}</{tag}>"
        return wrapped
    return decorator
@html_tag('b')
@app.route("/")
def home():
    return ("""
        <h1 style='text-align:center; color:red;'>I am Aqsa</h1>
        <img src='https://scontent-mia3-2.xx.fbcdn.net/v/t39.30808-6/409711479_6903716139682631_7759199876375289980_n.jpg?stp=cp6_dst-jpg&_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_ohc=8vBEw3fm7sIQ7kNvgH_1-1J&_nc_ht=scontent-mia3-2.xx&oh=00_AYCwXicze2l9jEGGREYlDL2S4rPlVunFFx7HkA2VPdfQrA&oe=66911336' width='500px' style='display: block; margin-left: auto; margin-right: auto;'>
    """)

if __name__ == "__main__":
    app.run(debug=True)