from flask import Flask, jsonify
import control

app = Flask(__name__)

# Ruta raiz
@app.route('/')
def index():
    data = control.getData("https://apicomuna22.emcali.net.co/metrics/range_public?deviceId=0703060003")
    prompt = control.getPrompt(data)
    image_url = control.getImage(prompt)
    
    data_complete = {"url": image_url,
                     "prompt": prompt}
    
    return jsonify(data_complete)

if __name__ == '__main__':
    app.run(debug=True)
