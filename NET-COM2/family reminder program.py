from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Store reminders in a dictionary
reminders = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    data = request.get_json()
    name = data.get('name')
    category = data.get('category')
    message = data.get('message')
    time = data.get('time')

    if name and category and message and time:
        if name not in reminders:
            reminders[name] = {
                'schedule': [],
                'medications': [],
                'todo': []
            }

        reminder = {
            'message': message,
            'time': time
        }

        # Add the reminder to the correct category
        if category == 'schedule':
            reminders[name]['schedule'].append(reminder)
        elif category == 'medications':
            reminders[name]['medications'].append(reminder)
        elif category == 'todo':
            reminders[name]['todo'].append(reminder)

        return jsonify({'message': 'Reminder added successfully!'})
    else:
        return jsonify({'message': 'Error: Missing data'})

@app.route('/reminders', methods=['GET'])
def get_reminders():
    return jsonify(reminders)

if __name__ == '__main__':
    app.run(debug=True)
