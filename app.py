from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Charger les données des membres
with open('data/members.json', 'r', encoding='utf-8') as f:
    members = json.load(f)

@app.route('/')
def home():
    return render_template('members.html', members=members)

@app.route('/member/<int:member_id>')
def member_detail(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return "Member not found", 404
    return render_template('member_detail.html', member=member)

if __name__ == '__main__':
    app.run(debug=True)
