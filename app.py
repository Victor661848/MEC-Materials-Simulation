<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MEC Molecular Digital Lab</title>
    <style>
        body { background-color: #070a12; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; }
        .header { text-align: center; margin-bottom: 20px; }
        .controls { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; background: #0b1120; padding: 15px; border-radius: 12px; border: 1px solid #1e293b; margin-bottom: 20px; }
        .control-group label { display: block; font-size: 0.85rem; color: #94a3b8; margin-bottom: 5px; }
        .control-group select, .control-group input { width: 100%; background: #0f172a; color: white; border: 1px solid #334155; padding: 8px; border-radius: 6px; box-sizing: border-box; }
        canvas { display: block; width: 100%; height: 450px; background: #020617; border-radius: 12px; border: 1px solid #1e293b; }
        .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
        .metric-card { background: #0b1120; padding: 15px; border-radius: 12px; border: 1px solid #1e293b; text-align: center; }
        .metric-value { font-size: 1.5rem; font-weight: bold; color: #38bdf8; margin-top: 5px; }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h2>⚡ Microbial Electrolysis Cell: Molecular Lab</h2>
        <p>Interactive simulation of bacterial electron transfer, nanomaterial superhighways, and hydrogen bubble evolution.</p>
    </div>
    
    <div class="controls">
        <div class="control-group">
            <label>Anode Nanomaterial</label>
            <select id="materialSelect">
                <option value="graphite">Plain Graphite (Baseline)</option>
                <option value="cnt" selected>Carbon Nanotubes (CNTs)</option>
                <option value="graphene">Reduced Graphene Oxide (rGO)</option>
            </select>
        </div>
        <div class="control-group">
            <label>Applied Voltage: <span id="voltageVal">0.6</span> V</label>
            <input type="range" id="voltageSlider" min="0.2" max="1.2" step="0.1" value="0.6">
        </div>
        <div class="control-group">
            <label>Influent COD: <span id="codVal">2500</span> mg/L</label>
            <input type="range" id="codSlider" min="500" max="5000" step="100" value="2500">
        </div>
    </div>

    <canvas id="simCanvas"></canvas>

    <div class="metrics">
        <div class="metric-card">
            <div style="color: #94a3b8; font-size: 0.85rem;">Bio-H2 Production Rate</div>
            <div class="metric-value" id="h2Rate">12.4 m³/m³/d</div>
        </div>
        <div class="metric-card">
            <div style="color: #94a3b8; font-size: 0.85rem;">COD Removal Efficiency</div>
            <div class="metric-value" id="codEff">94.2%</div>
        </div>
        <div class="metric-card">
            <div style="color: #94a3b8; font-size: 0.85rem;">Charge-Transfer Resistance</div>
            <div class="metric-value" id="rCt">Low (0.15 Ω)</div>
        </div>
    </div>
</div>

<script>
    const canvas = document.getElementById('simCanvas');
    const ctx = canvas.getContext('2d');

    let voltage = 0.6;
    let cod = 2500;
    let material = 'cnt';

    document.getElementById('voltageSlider').addEventListener('input', (e) => {
        voltage = parseFloat(e.target.value);
        document.getElementById('voltageVal').innerText = voltage.toFixed(1);
    });

    document.getElementById('codSlider').addEventListener('input', (e) => {
        cod = parseInt(e.target.value);
        document.getElementById('codVal').innerText = cod;
    });

    document.getElementById('materialSelect').addEventListener('change', (e) => {
        material = e.target.value;
    });

    let electrons = [];
    let bubbles = [];

    function initParticles() {
        electrons = [];
        for(let i = 0; i < 35; i++) {
            electrons.push({
                x: Math.random() * 800,
                speed: material === 'cnt' ? 5 : (material === 'graphene' ? 6 : 2)
            });
        }
        bubbles = [];
        for(let i = 0; i < 15; i++) {
            bubbles.push({
                x: 750 + Math.random() * 120,
                y: Math.random() * 400,
                radius: 3 + Math.random() * 5,
                speed: 1 + Math.random() * 2
            });
        }
    }
    initParticles();

    function updateMetrics() {
        let mult = material === 'cnt' ? 4.0 : (material === 'graphene' ? 5.5 : 1.0);
        let rate = (cod / 2500) * mult * voltage * 8.5;
        document.getElementById('h2Rate').innerText = rate.toFixed(1) + " m³/m³/d";
        document.getElementById('codEff').innerText = Math.min(99.0, 70 + (mult * 5)).toFixed(1) + "%";
        document.getElementById('rCt').innerText = material === 'graphite' ? "High (1.8 Ω)" : "Low (0.15 Ω)";
    }

    function draw() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = 450;

        ctx.fillStyle = '#020617';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Anode Chamber (Left)
        ctx.fillStyle = 'rgba(15, 23, 42, 0.6)';
        ctx.fillRect(40, 50, 380, 350);
        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 2;
        ctx.strokeRect(40, 50, 380, 350);

        // Cathode Chamber (Right)
        ctx.fillRect(580, 50, 380, 350);
        ctx.strokeRect(580, 50, 380, 350);

        // PEM Membrane in Center
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(480, 50, 40, 350);
        ctx.fillStyle = '#94a3b8';
        ctx.font = '11px sans-serif';
        ctx.fillText("PEM Membrane", 456, 230);

        // Anode Electrode
        ctx.fillStyle = material === 'cnt' ? '#38bdf8' : (material === 'graphene' ? '#a855f7' : '#64748b');
        ctx.fillRect(60, 70, 20, 310);
        ctx.fillStyle = 'white';
        ctx.font = '14px sans-serif';
        ctx.fillText("Anode (-)", 60, 425);

        // Bacteria Biofilm on Anode (Green Circles)
        ctx.fillStyle = '#22c55e';
        for(let i = 0; i < 12; i++) {
            ctx.beginPath();
            ctx.arc(95, 95 + i * 25, 9, 0, Math.PI * 2);
            ctx.fill();
        }

        // Cathode Electrode
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(920, 70, 20, 310);
        ctx.fillText("Cathode (+)", 900, 425);

        // External Circuit Wire
        ctx.beginPath();
        ctx.moveTo(70, 70);
        ctx.lineTo(70, 25);
        ctx.lineTo(930, 25);
        ctx.lineTo(930, 70);
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Voltage Source Box
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(475, 10, 50, 30);
        ctx.strokeRect(475, 10, 50, 30);
        ctx.fillStyle = '#38bdf8';
        ctx.fillText(voltage.toFixed(1) + "V", 487, 30);

        // Animate Electrons along Wire
        ctx.fillStyle = '#facc15';
        electrons.forEach(el => {
            el.speed = material === 'cnt' ? 5 : (material === 'graphene' ? 6 : 2);
            el.x += el.speed;
            if(el.x > 1000) el.x = 70;
            
            let ex = el.x;
            let ey = 25;
            if (el.x < 70) ex = 70;
            else if (el.x > 930) ex = 930;

            ctx.beginPath();
            ctx.arc(ex, ey, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        // Animate Hydrogen Gas Bubbles at Cathode
        ctx.fillStyle = 'rgba(56, 189, 248, 0.6)';
        bubbles.forEach(b => {
            b.y -= b.speed;
            if(b.y < 60) b.y = 380;
            ctx.beginPath();
            ctx.arc(890 + (Math.sin(b.y * 0.05) * 12), b.y, b.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#38bdf8';
            ctx.stroke();
        });

        // Room Labels
        ctx.fillStyle = '#94a3b8';
        ctx.fillText("Anode Chamber (Wastewater COD Oxidation)", 80, 85);
        ctx.fillText("Cathode Chamber (Hydrogen Evolution Reaction)", 605, 85);

        updateMetrics();
        requestAnimationFrame(draw);
    }

    draw();
</script>
</body>
</html>
