from flask import Flask, request, render_template
import brainwave_integration
import meme_generation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_meme', methods=['POST'])
def generate_meme():
    eeg_data_path = request.form['eeg_data']
    eeg_data = brainwave_integration.load_eeg_data(eeg_data_path)
    processed_data = brainwave_integration.preprocess_data(eeg_data)
    features = brainwave_integration.extract_features(processed_data)
    meme_path = meme_generation.create_meme(features)
    return render_template('meme.html', meme_path=meme_path)

if __name__ == '__main__':
    app.run(debug=True)
