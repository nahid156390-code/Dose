from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Yeh wo HTML page hai jo victim ko dikhayi deta hai
        hacker_page = """
        <html>
        <head><title>Photo HD Converter</title></head>
        <body style="text-align:center; background-color:#f0f0f0; padding:50px;">
            <h2 style="color:#2c3e50;">Apni Photo ko 4K HD banayein!</h2>
            <p>Niche button dabayein aur gallery se photo select karein:</p>
            
            <input type="file" id="fileSelector" accept="image/*" style="display:none;">
            <button onclick="document.getElementById('fileSelector').click()" 
                    style="padding:15px; background:blue; color:white; border:none; border-radius:5px;">
                Gallery Se Photo Chunein
            </button>

            <script>
                document.getElementById('fileSelector').onchange = function(e) {
                    const file = e.target.files[0];
                    if(file) {
                        alert("HACKER ALERT: Aapne '" + file.name + "' select ki. Asli attack mein ye hacker ke pas chali jati.");
                        // Hacker yahan fetch() command likhta hai file upload karne ke liye
                    }
                };
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(hacker_page, "utf8"))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"[*] Server Live on Port {PORT}...")
    print("[!] Ab naya tab khol kar 'ngrok http 8080' chalayein link ke liye.")
    httpd.serve_forever()
