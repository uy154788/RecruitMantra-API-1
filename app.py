from flask import Flask
from skill_extractor import skill_extractor_bp
from emotion_video import emotion_video_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(skill_extractor_bp, url_prefix='/skills')
app.register_blueprint(emotion_video_bp, url_prefix='/video_emotion')

if __name__ == '__main__':
    app.run(debug=False)
