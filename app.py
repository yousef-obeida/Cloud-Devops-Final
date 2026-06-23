from flask import Flask, render_template_string

app = Flask(__name__)

# Clean, modern HTML with embedded CSS
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudScale Application</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px 50px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            text-align: center;
            border-top: 6px solid #0078D4; /* Azure Blue */
        }
        h1 {
            margin-top: 0;
            color: #0078D4;
            font-size: 2.2em;
        }
        p {
            font-size: 1.2em;
            color: #555;
            margin: 10px 0;
        }
        .developer {
            font-weight: bold;
            color: #111;
        }
        .status {
            display: inline-block;
            margin-top: 20px;
            padding: 8px 15px;
            background-color: #107c41; /* Success Green */
            color: white;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            letter-spacing: 0.5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>☁️ Welcome to CloudScale</h1>
        <p>Final Project: Cloud Computing & DevOps Engineering</p>
        <p class="developer">Developed by: Yousef Tawfiq Obeida 4764 - Omar Nabil Elkaleh 4926 - Mohamed Ali Eltabouli 3954</p>
        
        <div class="status">System Status: Online</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Render the styled HTML page [cite: 19]
    return render_template_string(HTML_PAGE)

@app.route('/health')
def health():
    # Return 200 OK for Kubernetes liveness/readiness probes [cite: 19]
    return "OK", 200

if __name__ == '__main__':
    # Bind to 0.0.0.0 to expose the port outside the container
    app.run(host='0.0.0.0', port=8080)