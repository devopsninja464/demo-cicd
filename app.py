from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = b"<h1>Broken Build</h1>"
<html>
<head>
  <meta charset="UTF-8">
  <title>AvantiIQ CI/CD</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #0D0F1A, #0D1A2E);
      font-family: system-ui, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #E8EDF5;
    }
    .card {
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(0,229,168,.25);
      border-radius: 20px;
      padding: 48px;
      max-width: 500px;
      width: 90%;
      text-align: center;
    }
    .logo {
      width: 60px; height: 60px;
      background: #00E5A8;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 900;
      color: #05080D;
      margin: 0 auto 24px;
    }
    h1 { font-size: 26px; font-weight: 800; margin-bottom: 8px; }
    .sub { color: rgba(232,237,245,.5); font-size: 14px; margin-bottom: 28px; }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0,229,168,.1);
      border: 1px solid rgba(0,229,168,.25);
      border-radius: 100px;
      padding: 5px 14px;
      font-size: 13px;
      font-weight: 600;
      color: #00E5A8;
      margin-bottom: 28px;
    }
    .dot {
      width: 8px; height: 8px;
      background: #00E5A8;
      border-radius: 50%;
      animation: pulse 2s ease-in-out infinite;
    }
    @keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:.4; } }
    .stats {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 24px;
    }
    .stat {
      background: rgba(255,255,255,.04);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 10px;
      padding: 14px 8px;
    }
    .val { font-size: 18px; font-weight: 800; color: #00E5A8; margin-bottom: 4px; }
    .lbl { font-size: 10px; color: rgba(232,237,245,.4); text-transform: uppercase; letter-spacing: 1px; }
    .footer { font-size: 12px; color: rgba(232,237,245,.25); }
    .footer span { color: rgba(0,229,168,.6); }
  </style>
</head>
<body>
  <div class="card">
    <div class="logo">Av</div>
    <h1>Deployed by Jenkins</h1>
    <p class="sub">Built, tested, and deployed automatically.<br>No manual steps.</p>
    <div class="badge"><div class="dot"></div>Pipeline: GREEN</div>
    <div class="stats">
      <div class="stat"><div class="val">v1.0</div><div class="lbl">Version</div></div>
      <div class="stat"><div class="val">AUTO</div><div class="lbl">Deployed by</div></div>
    </div>
    <div class="footer">Jenkins + Docker + AvantiIQ Labs<br><span>avantiiq.com</span></div>
  </div>
</body>
</html>'''


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML)

    def log_message(self, f, *a):
        pass


if __name__ == "__main__":
    print("AvantiIQ app starting on port 8000...")
    HTTPServer(("", 8000), Handler).serve_forever()
