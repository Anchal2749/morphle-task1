from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():

    name = "Anchal Maurya"  
    user = 'anchal' 

   
    ist = pytz.timezone('Asia/Kolkata')
    s_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    
    top_output = subprocess.getoutput('top -b -n 1')

   
    response = f"""
    Name: {name}<br>
    Username: {user}<br>
    Server Time: {s_time}<br>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)