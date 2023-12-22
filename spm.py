from flask import Flask

app = Flask(__name__)

running = True

@app.route('/stop-script', methods=['POST'])
def stop_script():
    global running
    running = False
    return 'Script stop request received.', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run Flask app on all available network interfaces on port 5000
