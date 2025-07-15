from flask import Flask, render_template

from flask_socketio import SocketIO, emit
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
@app.route('/')
def index():
return render_template('index.html')
@socketio.on('voice_command')
def handle_voice_command(data):
try:
text = data['audio']
response = handle_text(text)
emit('bot_response', {'response': response})
engine.say(response)
engine.runAndWait()
except Exception as e:
print("Error:", e)
emit('bot_response', {'response': "I,am here to clarify your doubts."})
def handle_text(text):
# Basic medical responses for 20 conditions
if "symptoms of flu" in text.lower():
return "Common symptoms of flu include fever, cough, sore throat, and body

26

aches."
elif "headache" in text.lower():
return "For a headache, you can rest in a quiet, dark room and take pain relief
medication if necessary."
elif "COVID-19" in text.lower():
return "Symptoms of COVID-19 include fever, cough, and difficulty breathing.
If you suspect you have COVID-19, please contact a healthcare provider."
elif "symptoms of cold" in text.lower():
return "Common cold symptoms include sneezing, runny nose, and a sore
throat."
elif "stomach ache" in text.lower():
return "For a stomach ache, avoid solid food for a while and try drinking clear
fluids."
elif "diabetes" in text.lower():
return "Symptoms of diabetes include increased thirst, frequent urination, and
unexplained weight loss."
elif "hypertension" in text.lower():
return "Hypertension often has no symptoms, but it can lead to serious health
issues if untreated."
elif "asthma" in text.lower():
return "Asthma symptoms include wheezing, shortness of breath, and chest
tightness."
elif "allergy" in text.lower():
return "Allergy symptoms include sneezing, itching, and a runny nose."
elif "symptoms of migraine" in text.lower():
return "Migraine symptoms include severe headache, nausea, and sensitivity to
light and sound."
elif "symptoms of depression" in text.lower():
return "Symptoms of depression include persistent sadness, loss of interest, and
fatigue."
elif "symptoms of anxiety" in text.lower():
return "Anxiety symptoms include excessive worry, restlessness, and muscle
tension."
elif "symptoms of food poisoning" in text.lower():
return "Symptoms of food poisoning include nausea, vomiting, and diarrhea."
elif "heart attack" in text.lower():
return "Symptoms of a heart attack include chest pain, shortness of breath, and
nausea. Seek emergency help immediately."
elif "stroke" in text.lower():
return "Symptoms of a stroke include sudden numbness, confusion, and
difficulty speaking. Seek emergency help immediately."
elif "symptoms of pneumonia" in text.lower():
return "Pneumonia symptoms include cough, fever, and difficulty breathing."

27
elif "kidney stones" in text.lower():
return "Symptoms of kidney stones include severe pain, nausea, and blood in
urine."
elif "UTI" in text.lower():
return "Symptoms of a urinary tract infection include a strong urge to urinate,
burning sensation during urination, and cloudy urine."
elif "symptoms of arthritis" in text.lower():
return "Arthritis symptoms include joint pain, stiffness, and swelling."
elif "anemia" in text.lower():
return "Symptoms of anemia include fatigue, weakness, and pale skin."

if __name__ == '__main__':
socketio.run(app)