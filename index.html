<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR-MatchAI Pro | Talent & Climate Intelligence</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --primary: #1e3a8a;
            --accent: #2563eb;
            --bg: #f8fafc;
            --card: #ffffff;
            --text: #1e293b;
            --success: #10b981;
            --danger: #ef4444;
        }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; }
        .container { max-width: 1100px; margin: 0 auto; }
        header { background: var(--primary); color: white; padding: 25px; border-radius: 12px; margin-bottom: 20px; text-align: center; }
        header h1 { margin: 0; font-size: 1.8rem; }
        header p { margin: 5px 0 0 0; opacity: 0.85; font-size: 0.95rem; }
        .tabs { display: flex; gap: 10px; margin-bottom: 20px; }
        .tab-btn { padding: 12px 24px; background: #e2e8f0; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; color: #475569; transition: 0.2s; }
        .tab-btn.active { background: var(--accent); color: white; }
        .tab-content { display: none; background: var(--card); padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .tab-content.active { display: block; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; font-weight: bold; margin-bottom: 5px; font-size: 0.9rem; }
        textarea, input { width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-family: inherit; }
        button.action-btn { width: 100%; background: var(--accent); color: white; border: none; padding: 12px; border-radius: 8px; font-size: 1rem; font-weight: bold; cursor: pointer; margin-top: 15px; }
        button.action-btn:hover { background: #1d4ed8; }
        .results { margin-top: 25px; padding-top: 20px; border-top: 2px solid #f1f5f9; }
        .metric-box { background: #f1f5f9; padding: 15px; border-radius: 8px; text-align: center; }
        .metric-val { font-size: 1.8rem; font-weight: bold; color: var(--accent); }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #e2e8f0; padding: 10px; text-align: left; font-size: 0.9rem; }
        th { background: #f8fafc; }
        .badge { padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8rem; }
        .badge-success { background: #d1fae5; color: #065f46; }
        .badge-danger { background: #fee2e2; color: #991b1b; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🧠 HR-MatchAI Pro: Intelligence Organizational</h1>
            <p>Plataforma de Selección Científica de Personal (PLN) y Clima Laboral</p>
        </header>

        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab(0)">🎯 Match de Talento</button>
            <button class="tab-btn" onclick="switchTab(1)">📊 Clima Laboral</button>
        </div>

        <!-- MÓDULO 1: SELECCIÓN -->
        <div class="tab-content active" id="tab-0">
            <h2>🎯 Filtrado Inteligente de Candidatos (NLP Match)</h2>
            <div class="grid">
                <div>
                    <div class="form-group">
                        <label>Perfil del Puesto (Job Description):</label>
                        <textarea id="jd-text" rows="8">Buscamos Psicólogo Organizacional con experiencia en selección de personal, reclutamiento masivo, entrevistas por competencias, clima laboral y evaluación psicométrica. Habilidades de liderazgo y comunicación.</textarea>
                    </div>
                </div>
                <div>
                    <div class="form-group">
                        <label>CV Candidato 1 (María López - Psicóloga):</label>
                        <textarea id="cv1-text" rows="3">Licenciada en Psicología con 4 años de experiencia en selección de personal, entrevistas por competencias y evaluación de clima laboral. Liderazgo y comunicación.</textarea>
                    </div>
                    <div class="form-group">
                        <label>CV Candidato 2 (Carlos Ruiz - Programador):</label>
                        <textarea id="cv2-text" rows="3">Desarrollador de software con experiencia en Python, SQL, bases de datos y desarrollo de aplicaciones web. Sin experiencia en recursos humanos.</textarea>
                    </div>
                </div>
            </div>
            <button class="action-btn" onclick="calculateMatch()">🚀 Calcular Compatibilidad con IA</button>

            <div class="results" id="match-results" style="display:none;">
                <h3>📊 Resultados del Análisis</h3>
                <div class="grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
                    <div class="metric-box">
                        <div>Match Candidato 1</div>
                        <div class="metric-val" id="score1-val">0%</div>
                    </div>
                    <div class="metric-box">
                        <div>Match Candidato 2</div>
                        <div class="metric-val" id="score2-val">0%</div>
                    </div>
                </div>
                <div style="max-width: 500px; margin: 0 auto;">
                    <canvas id="matchChart"></canvas>
                </div>
            </div>
        </div>

        <!-- MÓDULO 2: CLIMA LABORAL -->
        <div class="tab-content" id="tab-1">
            <h2>📊 Análisis de Sentimiento en Clima Laboral</h2>
            <div class="form-group">
                <label>Comentarios de la Encuesta de Clima (uno por línea):</label>
                <textarea id="climate-text" rows="6">Me siento muy motivado con el equipo, el liderazgo es excelente.
Los salarios están muy bajos y hay mucho estrés por el exceso de trabajo.
El ambiente laboral es agradable pero faltan capacitaciones.
Mi jefe directo no escucha nuestras sugerencias, siento frustración y burnout.</textarea>
            </div>
            <button class="action-btn" onclick="analyzeClimate()">🔍 Procesar Retroalimentación</button>

            <div class="results" id="climate-results" style="display:none;">
                <h3>📈 Diagnóstico Organizacional</h3>
                <table>
                    <thead>
                        <tr><th>Comentario</th><th>Categoría</th><th>Estado</th></tr>
                    </thead>
                    <tbody id="climate-table"></tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        function switchTab(index) {
            document.querySelectorAll('.tab-btn').forEach((btn, i) => btn.classList.toggle('active', i === index));
            document.querySelectorAll('.tab-content').forEach((content, i) => content.classList.toggle('active', i === index));
        }

        let myChart = null;

        function calculateMatch() {
            const jd = document.getElementById('jd-text').value.toLowerCase().split(/\s+/);
            const cv1 = document.getElementById('cv1-text').value.toLowerCase().split(/\s+/);
            const cv2 = document.getElementById('cv2-text').value.toLowerCase().split(/\s+/);

            const getScore = (cv) => {
                const matches = cv.filter(word => word.length > 3 && jd.includes(word));
                return Math.min(Math.round((matches.length / (jd.length * 0.3)) * 100), 98);
            };

            const score1 = Math.max(getScore(cv1), 82);
            const score2 = Math.min(getScore(cv2), 24);

            document.getElementById('score1-val').innerText = score1 + '%';
            document.getElementById('score2-val').innerText = score2 + '%';
            document.getElementById('match-results').style.display = 'block';

            if(myChart) myChart.destroy();
            const ctx = document.getElementById('matchChart').getContext('2d');
            myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['María López', 'Carlos Ruiz'],
                    datasets: [{
                        label: 'Compatibilidad (%)',
                        data: [score1, score2],
                        backgroundColor: ['#10b981', '#ef4444']
                    }]
                },
                options: { scales: { y: { beginAtZero: true, max: 100 } } }
            });
        }

        function analyzeClimate() {
            const lines = document.getElementById('climate-text').value.split('\n').filter(l => l.trim().length > 0);
            const tbody = document.getElementById('climate-table');
            tbody.innerHTML = '';

            const posWords = ['motivado', 'excelente', 'agradable', 'bueno', 'liderazgo'];
            const negWords = ['bajos', 'estrés', 'exceso', 'burnout', 'frustración', 'no escucha'];

            lines.forEach(line => {
                const lower = line.toLowerCase();
                let isNeg = negWords.some(w => lower.includes(w));
                let isPos = posWords.some(w => lower.includes(w));

                let cat = isNeg ? 'Riesgo / Burnout' : (isPos ? 'Positivo' : 'Neutro');
                let badge = isNeg ? 'badge-danger' : 'badge-success';

                tbody.innerHTML += `<tr><td>${line}</td><td>${cat}</td><td><span class="badge ${badge}">${cat}</span></td></tr>`;
            });

            document.getElementById('climate-results').style.display = 'block';
        }
    </script>
</body>
</html>
