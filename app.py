from flask import Flask, render_template, request, jsonify
import pyttsx3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_to_audio():
    text = request.form.get('text')
    selected_voice = request.form.get('voice')
    
    if not text.strip():
        return jsonify({'error': 'Please provide some text to convert!'})

    # Save the file in the static folder
    output_file = os.path.join('static', 'output.mp3')

    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if selected_voice == "Female":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        engine.save_to_file(text, output_file)
        engine.runAndWait()
        return jsonify({'success': True, 'file': '/' + output_file})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
