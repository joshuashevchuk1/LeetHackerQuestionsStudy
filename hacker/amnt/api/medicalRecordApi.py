from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

# Mock medical record data
medical_records = [
    {
        "patient_id": "001",
        "name": "Alice",
        "department": "Cardiology",
        "pulse_rate": 72
    },
    {
        "patient_id": "002",
        "name": "Bob",
        "department": "Neurology",
        "pulse_rate": 65
    },
    {
        "patient_id": "003",
        "name": "Charlie",
        "department": "Cardiology",
        "pulse_rate": 80
    },
    {
        "patient_id": "004",
        "name": "Dana",
        "department": "Oncology",
        "pulse_rate": 75
    },
    {
        "patient_id": "005",
        "name": "Eva",
        "department": "Neurology",
        "pulse_rate": 60
    }
]


@app.route('/records', methods=['GET'])
def get_all_records():
    return jsonify(medical_records)


@app.route('/pulse-by-department', methods=['GET'])
def get_pulse_by_department():
    grouped = defaultdict(list)

    for record in medical_records:
        grouped[record['department']].append(record['pulse_rate'])

    # Compute average pulse per department
    department_pulse_avg = {
        dept: sum(pulses) / len(pulses)
        for dept, pulses in grouped.items()
    }

    return jsonify(department_pulse_avg)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
