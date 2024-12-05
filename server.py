import logging
from flask import Flask, request

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    handlers=[logging.FileHandler("log.txt"), 
    logging.StreamHandler()], 
    level=logging.INFO
)
logging.getLogger("flask").setLevel(logging.ERROR)

app = Flask(__name__)
homes = "<h1 style='text-align: center'> HI COK IDUP NIH</h1>"

@app.route("/")
def homepages():
    return homes 
    
if __name__ == "__main__":
    app.run()
