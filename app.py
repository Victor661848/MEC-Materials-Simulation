<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MEC Molecular & Systems Lab | PhET-Style Interactive Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        darkBg: '#0b0f19',
                        panelBg: '#131c2e',
                        borderCol: '#1e293b',
                        neonCyan: '#00d4ff',
                        neonGreen: '#00ff9d',
                        neonRed: '#ff4b4b',
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #0b0f19; color: #f8fafc; }
st.markdown("""
    <style>
        canvas { display: block; width: 100%; height: 100%; border-radius: 0.75rem; background: #070a12; }
    </style>
""", unsafe_allow_html=True)    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Header -->
    <header class="border-b border-borderCol bg-panelBg/80 backdrop-blur sticky top-0 z-50 px-6 py-4 flex flex-wrap justify-between items-center shadow-lg">
        <div class="flex items-center space-x-3">
            <div class="bg-gradient-to-tr from-cyan-500 to-emerald-400 p-2.5 rounded-xl shadow-md shadow-cyan-500/20 text-darkBg font-black text-xl">
                st.markdown("⚡ Fast-charging anode enabled!")  # Correct: inside quotes
            </div>
            <div>
                <h1 class="text-xl font-bold tracking-tight bg-gradient-to-r from-cyan-400 to-emerald-400 bg-clip-text text-transparent">
                    BioElectrio NanoLab: Microbial Electrolysis Cell (MEC)
                </h1>
                <p class="text-xs text-slate-400">Interactive Molecular & Systems-Level Digital Twin Simulator</p>
            </div>
        </div>
        <div class="flex items-center space-x-3 mt-2 sm:mt-0">
            <span class="px-3 py-1 bg-cyan-950/80 border border-cyan-800/50 text-cyan-400 text-xs font-semibold rounded-full animate-pulse">
st.subheader("● Live Molecular Simulation Active")            </span>
        </div>
    </header>

    <!-- Main Layout -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left Column: Controls & Material Selector (5 cols) -->
        <section class="lg:col-span-5 flex flex-col space-y-6">
            
            <!-- Nanomaterial Selector Card -->
            <div class="bg-panelBg border border-borderCol rounded-2xl p-5 shadow-xl">
                <h2 class="text-sm font-semibold text-cyan-400 uppercase tracking-wider mb-3 flex items-center">
                    <span class="mr-2">🔬</span> Electrode Nanomaterial Architecture
                </h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3" id="material-buttons">
                    <button onclick="setMaterial('graphite')" data-mat="graphite" class="mat-btn text-left p-3 rounded-xl border border-borderCol bg-slate-800/50 hover:bg-slate-800 transition-all text-xs font-medium">
                        <div class="font-bold text-slate-300">Plain Graphite Felt</div>
                        <div class="text-[10px] text-slate-400 mt-1">1.0x Area | 40% Efficiency</div>
                    </button>
                    <button onclick="setMaterial('cnt')" data-mat="cnt" class="mat-btn text-left p-3 rounded-xl border border-cyan-500/50 bg-cyan-950/30 hover:bg-cyan-900/40 transition-all text-xs font-medium shadow-sm shadow-cyan-500/10">
                        <div class="font-bold text-cyan-300">Carbon Nanotubes (CNTs)</div>
                        <div class="text-[10px] text-cyan-400/80 mt-1">4.0x Area | 68% Efficiency</div>
                    </button>
                    <button onclick="setMaterial('nickel')" data-mat="nickel" class="mat-btn text-left p-3 rounded-xl border border-borderCol bg-slate-800/50 hover:bg-slate-800 transition-all text-xs font-medium">
                        <div class="font-bold text-slate-300">Nickel Catalyst</div>
                        <div class="text-[10px] text-slate-400 mt-1">2.5x Area | 75% Efficiency</div>
                    </button>
                    <button onclick="setMaterial('hybrid')" data-mat="hybrid" class="mat-btn text-left p-3 rounded-xl border border-emerald-500/50 bg-emerald-950/30 hover:bg-emerald-900/40 transition-all text-xs font-medium shadow-sm shadow-emerald-500/10">
                        <div class="font-bold text-emerald-300">Graphene + Ni Hybrid</div>
                        <div class="text-[10px] text-emerald-400/80 mt-1">9.0x Area | 92% Efficiency</div>
                    </button>
                </div>
            </div>

            <!-- Operating Parameters Sliders Card -->
            <div class="bg-panelBg border border-borderCol rounded-2xl p-5 shadow-xl flex-1 flex flex-col justify-between space-y-5">
                <div>
                    <h2 class="text-sm font-semibold text-emerald-400 uppercase tracking-wider mb-4 flex items-center">
                        <span class="mr-2">🎛️</span> Reactor Operational Levers
                    </h2>

                    <!-- Applied Voltage Slider -->
                    <div class="space-y-2 mb-4">
                        <div class="flex justify-between text-xs font-medium">
                            <span class="text-slate-300">Applied Voltage ($E_{app}$)</span>
                            <span id="val-voltage" class="text-cyan-400 font-bold">0.65 V</span>
                        </div>
                        <input type="range" id="slider-voltage" min="0.2" max="1.5" step="0.05" value="0.65" 
                            oninput="updateParams()" class="w-full accent-cyan-400 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        <p class="text-[10px] text-slate-400">Drives proton/electron transfer speed across the circuit.</p>
                    </div>

                    <!-- Initial COD Slider -->
                    <div class="space-y-2 mb-4">
                        <div class="flex justify-between text-xs font-medium">
                            <span class="text-slate-300">Wastewater Organic Load (COD)</span>
                            <span id="val-cod" class="text-emerald-400 font-bold">2000 mg/L</span>
                        </div>
                        <input type="range" id="slider-cod" min="500" max="5000" step="250" value="2000" 
                            oninput="updateParams()" class="w-full accent-emerald-400 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        <p class="text-[10px] text-slate-400">Concentration of organic food available for bacteria.</p>
                    </div>

                    <!-- Temperature Slider -->
                    <div class="space-y-2">
                        <div class="flex justify-between text-xs font-medium">
                            <span class="text-slate-300">Reactor Temperature</span>
                            <span id="val-temp" class="text-amber-400 font-bold">35 °C</span>
                        </div>
                        <input type="range" id="slider-temp" min="15" max="45" step="1" value="35" 
                            oninput="updateParams()" class="w-full accent-amber-400 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        <p class="text-[10px] text-slate-400">Influences microbial metabolic kinetics and reaction rate.</p>
                    </div>
                </div>

                <!-- Reset Button -->
                <button onclick="resetDefaults()" class="w-full py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-xl border border-borderCol transition-all shadow-sm">
                    Reset Default Parameters
                </button>
            </div>
        </section>

        <!-- Right Column: Canvas & Live Metrics (7 cols) -->
        <section class="lg:col-span-7 flex flex-col space-y-6">
            
            <!-- PhET-Style Interactive Canvas Container -->
            <div class="bg-panelBg border border-borderCol rounded-2xl p-4 shadow-xl flex flex-col relative">
                <div class="flex justify-between items-center mb-3 px-2">
                    <div class="flex items-center space-x-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
                        <h2 class="text-xs font-bold text-slate-200 uppercase tracking-wide">Live Molecular & Electrochemical Chamber View</h2>
                    </div>
                    <div class="text-[11px] text-slate-400 flex space-x-4">
                        <span>🟢 Bacteria</span>
                        <span>🟠 COD/Substrate</span>
                        <span>⚡ Electrons</span>
                        <span>🔵 $H_2$ Bubbles</span>
                    </div>
                </div>
                
                <!-- Canvas Element -->
                <div class="relative w-full aspect-[16/10] bg-[#070a12] rounded-xl overflow-hidden border border-borderCol">
                    <canvas id="simCanvas"></canvas>
                </div>
                
                <!-- Dynamic Legend / Status Notice -->
                <div class="mt-3 bg-slate-900/80 border border-borderCol rounded-xl p-3 text-xs text-slate-300 flex items-center justify-between">
                    <div id="canvas-status-text" class="font-medium text-cyan-300">
                        Status: Active biofilm colonizing nanotube anode. Hydrogen evolution reaction proceeding smoothly at cathode.
                    </div>
                    <div class="text-right text-[10px] text-slate-400 font-mono">
                        FPS: <span id="fps-counter" class="text-emerald-400">60</span>
                    </div>
                </div>
            </div>

            <!-- Real-Time Output Metrics Dashboard -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div class="bg-panelBg border border-borderCol rounded-2xl p-4 shadow-md flex flex-col justify-between">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase">H₂ Production Rate</span>
                    <div class="mt-2">
                        <span id="metric-h2" class="text-xl font-black text-emerald-400">14.2</span>
                        <span class="text-[10px] text-slate-400 ml-1">mmol/L·d</span>
                    </div>
                </div>
                <div class="bg-panelBg border border-borderCol rounded-2xl p-4 shadow-md flex flex-col justify-between">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase">Current Density</span>
                    <div class="mt-2">
                        <span id="metric-current" class="text-xl font-black text-cyan-400">4.8</span>
                        <span class="text-[10px] text-slate-400 ml-1">A/m²</span>
                    </div>
                </div>
                <div class="bg-panelBg border border-borderCol rounded-2xl p-4 shadow-md flex flex-col justify-between">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase">Est. Fuel Cost</span>
                    <div class="mt-2">
                        <span id="metric-cost" class="text-xl font-black text-amber-400">$2.15</span>
                        <span class="text-[10px] text-slate-400 ml-1">/kg $H_2$</span>
                    </div>
                </div>
                <div class="bg-panelBg border border-borderCol rounded-2xl p-4 shadow-md flex flex-col justify-between">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase">System Efficiency</span>
                    <div class="mt-2">
                        <span id="metric-eff" class="text-xl font-black text-indigo-400">68%</span>
                        <span class="text-[10px] text-slate-400 ml-1">CE</span>
                    </div>
                </div>
            </div>

        </section>
    </main>

    <!-- Footer -->
    <footer class="text-center py-4 text-xs text-slate-500 border-t border-borderCol bg-panelBg/40 mt-8">
        BioElectrio Systems Lab • Built for TKS Portfolio & Deep Tech Research Validation
    </footer>

    <!-- Simulation JavaScript Logic -->
    <script>
        // Simulation State
        const state = {
            material: 'cnt',
            voltage: 0.65,
            cod: 2000,
            temp: 35,
            // Material coefficients
            surfaceMultiplier: 4.0,
            efficiency: 0.68,
            baseRate: 1.5
        };

        // Material Presets
        const materialConfigs = {
            graphite: { surfaceMultiplier: 1.0, efficiency: 0.40, baseRate: 0.8 },
            cnt: { surfaceMultiplier: 4.0, efficiency: 0.68, baseRate: 1.8 },
            nickel: { surfaceMultiplier: 2.5, efficiency: 0.75, baseRate: 2.2 },
            hybrid: { surfaceMultiplier: 9.0, efficiency: 0.92, baseRate: 3.5 }
        };

        function setMaterial(matKey) {
            state.material = matKey;
            const config = materialConfigs[matKey];
            state.surfaceMultiplier = config.surfaceMultiplier;
            state.efficiency = config.efficiency;
            state.baseRate = config.baseRate;

            // Update UI Active Button Styles
            document.querySelectorAll('.mat-btn').forEach(btn => {
                btn.className = "mat-btn text-left p-3 rounded-xl border border-borderCol bg-slate-800/50 hover:bg-slate-800 transition-all text-xs font-medium";
            });
            const activeBtn = document.querySelector(`[data-mat="${matKey}"]`);
            if (activeBtn) {
                activeBtn.className = "mat-btn text-left p-3 rounded-xl border border-cyan-500/50 bg-cyan-950/30 hover:bg-cyan-900/40 transition-all text-xs font-medium shadow-sm shadow-cyan-500/10";
            }

            updateMetrics();
        }

        function updateParams() {
            state.voltage = parseFloat(document.getElementById('slider-voltage').value);
            state.cod = parseInt(document.getElementById('slider-cod').value);
            state.temp = parseInt(document.getElementById('slider-temp').value);

            document.getElementById('val-voltage').innerText = state.voltage.toFixed(2) + ' V';
            document.getElementById('val-cod').innerText = state.cod + ' mg/L';
            document.getElementById('val-temp').innerText = state.temp + ' °C';

            updateMetrics();
        }

        function resetDefaults() {
            document.getElementById('slider-voltage').value = 0.65;
            document.getElementById('slider-cod').value = 2000;
            document.getElementById('slider-temp').value = 35;
            setMaterial('cnt');
            updateParams();
        }

        function updateMetrics() {
            // Calculate dynamic outputs based on Monod kinetics & state parameters
            const tempFactor = 1.0 + (state.temp - 25) * 0.02;
            const codFactor = state.cod / 2000;
            const voltageFactor = Math.min(1.5, state.voltage / 0.6);

            const h2Rate = (state.baseRate * state.surfaceMultiplier * codFactor * tempFactor * voltageFactor).toFixed(1);
            const currentDensity = (h2Rate * 0.34 * state.efficiency).toFixed(1);
            const cost = Math.max(1.40, (4.50 / (state.surfaceMultiplier * state.efficiency * voltageFactor))).toFixed(2);
            const coulombicEff = Math.min(96, Math.round(state.efficiency * 100));

            document.getElementById('metric-h2').innerText = h2Rate;
            document.getElementById('metric-current').innerText = currentDensity;
            document.getElementById('metric-cost').innerText = '$' + cost;
            document.getElementById('metric-eff').innerText = coulombicEff + '%';
        }

        // --- CANVAS PhET ANIMATION ENGINE ---
        const canvas = document.getElementById('simCanvas');
        const ctx = canvas.getContext('2d');

        // Particle Arrays
        let bacteria = [];
        let codParticles = [];
        let electrons = [];
        let protons = [];
        let bubbles = [];

        function resizeCanvas() {
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width * window.devicePixelRatio;
            canvas.height = rect.height * window.devicePixelRatio;
            ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        }

        window.addEventListener('resize', resizeCanvas);

        function initParticles() {
            bacteria = [];
            codParticles = [];
            electrons = [];
            protons = [];
            bubbles = [];

            // Create anode bacteria nodes
            for (let i = 0; i < 35; i++) {
                bacteria.push({
                    x: 60 + Math.random() * 80,
                    y: 60 + Math.random() * 220,
                    radius: 6 + Math.random() * 4,
                    wiggleSpeed: 0.05 + Math.random() * 0.05,
                    angle: Math.random() * Math.PI * 2
                });
            }

            // Create COD particles in anode chamber
            for (let i = 0; i < 40; i++) {
                codParticles.push({
                    x: 40 + Math.random() * 180,
                    y: 40 + Math.random() * 240,
                    vx: (Math.random() - 0.5) * 0.8,
                    vy: (Math.random() - 0.5) * 0.8,
                    radius: 3
                });
            }
        }

        // Particle Spawners & Physics Loop
        function updateAndRender() {
            const width = canvas.clientWidth;
            const height = canvas.clientHeight;

            ctx.clearRect(0, 0, width, height);

            // 1. Draw Chamber Backgrounds (Split Reactor)
            const midX = width / 2;

            // Anode Chamber (Left)
            ctx.fillStyle = '#091220';
            ctx.fillRect(0, 0, midX - 15, height);
            ctx.strokeStyle = '#1e293b';
            ctx.lineWidth = 2;
            ctx.strokeRect(0, 0, midX - 15, height);

            // Cathode Chamber (Right)
            ctx.fillStyle = '#081a24';
            ctx.fillRect(midX + 15, 0, midX - 15, height);
            ctx.strokeRect(midX + 15, 0, midX - 15, height);

            // Proton Exchange Membrane (Center)
            ctx.fillStyle = '#1e293b';
            ctx.fillRect(midX - 15, 0, 30, height);
            ctx.fillStyle = '#38bdf8';
            ctx.font = '10px Inter';
            ctx.textAlign = 'center';
            ctx.save();
            ctx.translate(midX, height / 2);
            ctx.rotate(-Math.PI / 2);
            ctx.fillText('PROTON EXCHANGE MEMBRANE (PEM)', 0, 4);
            ctx.restore();

            // Labels
            ctx.fillStyle = '#00d4ff';
            ctx.font = 'bold 12px Inter';
            ctx.textAlign = 'left';
            ctx.fillText('ANODE CHAMBER (Wastewater COD)', 20, 25);

            ctx.fillStyle = '#00ff9d';
            ctx.fillText('CATHODE CHAMBER (Hydrogen Evolution)', midX + 35, 25);

            // 2. Draw Electrodes & Nanomaterial Texture
            // Anode Plate (Left wall of anode chamber or textured insert)
            ctx.fillStyle = state.material === 'cnt' || state.material === 'hybrid' ? '#0f766e' : '#334155';
            ctx.fillRect(30, 40, 15, height - 80);
            
            // Cathode Plate (Right wall of cathode chamber)
            ctx.fillStyle = state.material === 'nickel' || state.material === 'hybrid' ? '#047857' : '#475569';
            ctx.fillRect(width - 45, 40, 15, height - 80);

            // 3. Update & Render Bacteria
            bacteria.forEach(b => {
                b.angle += b.wiggleSpeed;
                const wx = b.x + Math.sin(b.angle) * 3;
                const wy = b.y + Math.cos(b.angle) * 3;

                ctx.fillStyle = state.material === 'hybrid' ? '#34d399' : '#10b981';
                ctx.beginPath();
                ctx.arc(wx, wy, b.radius, 0, Math.PI * 2);
                ctx.fill();

                // Draw pili / nanowire connection to anode
                ctx.strokeStyle = 'rgba(52, 211, 153, 0.3)';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(wx, wy);
                ctx.lineTo(45, wy);
                ctx.stroke();
            });

            // 4. Update & Render COD Substrate Particles
            ctx.fillStyle = '#fb923c';
            codParticles.forEach(p => {
                p.x += p.vx * (state.surfaceMultiplier * 0.3);
                p.y += p.vy;

                if (p.x < 40) p.x = midX - 30;
                if (p.x > midX - 30) p.x = 40;
                if (p.y < 40) p.y = height - 40;
                if (p.y > height - 40) p.y = 40;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fill();
            });

            // 5. External Circuit Wire & Electrons (Top Arch)
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(37, 40);
            ctx.lineTo(37, 15);
            ctx.lineTo(width - 37, 15);
            ctx.lineTo(width - 37, 40);
            ctx.stroke();

            // Voltmeter Box in Center of Circuit
            ctx.fillStyle = '#0f172a';
            ctx.fillRect(width / 2 - 35, 5, 70, 22);
            ctx.strokeStyle = '#00d4ff';
            ctx.strokeRect(width / 2 - 35, 5, 70, 22);
            ctx.fillStyle = '#00d4ff';
            ctx.font = 'bold 10px Inter';
            ctx.textAlign = 'center';
            ctx.fillText(`${state.voltage.toFixed(2)} V`, width / 2, 20);

            // Spawn & Render Electrons moving along the wire
            if (Math.random() < (0.2 * state.surfaceMultiplier)) {
                electrons.push({ progress: 0, speed: 0.02 * state.surfaceMultiplier });
            }

            ctx.fillStyle = '#00d4ff';
            electrons.forEach((e, index) => {
                e.progress += e.speed;
                if (e.progress > 1) {
                    electrons.splice(index, 1);
                    return;
                }
                // Map progress along wire path
                let ex, ey;
                const pathLen = (width - 74) + 50;
                const currentDist = e.progress * pathLen;
                if (currentDist < 25) {
                    ex = 37; ey = 40 - currentDist;
                } else if (currentDist < (width - 74 + 25)) {
                    ex = 37 + (currentDist - 25); ey = 15;
                } else {
                    ex = width - 37; ey = 15 + (currentDist - (width - 74 + 25));
                }

                ctx.beginPath();
                ctx.arc(ex, ey, 3, 0, Math.PI * 2);
                ctx.fill();
            });

            // 6. Spawn & Render Protons (H+) crossing PEM
            if (Math.random() < 0.3) {
                protons.push({
                    x: midX - 10,
                    y: 50 + Math.random() * (height - 100),
                    vx: (1.5 + state.voltage * 1.5),
                    vy: (Math.random() - 0.5) * 0.5
                });
            }

            ctx.fillStyle = '#facc15';
            protons.forEach((pr, index) => {
                pr.x += pr.vx;
                if (pr.x > midX + 20) {
                    protons.splice(index, 1);
                    return;
                }
                ctx.beginPath();
                ctx.arc(pr.x, pr.y, 2.5, 0, Math.PI * 2);
                ctx.fill();
            });

            // 7. Spawn & Render Hydrogen Bubbles on Cathode
            if (Math.random() < (0.15 * state.surfaceMultiplier * (state.efficiency))) {
                bubbles.push({
                    x: width - 50 + Math.random() * 10,
                    y: height - 60,
                    radius: 3 + Math.random() * 3,
                    vy: -(1.0 + Math.random() * 1.5)
                });
            }

            ctx.fillStyle = 'rgba(0, 255, 157, 0.7)';
            ctx.strokeStyle = '#00ff9d';
            bubbles.forEach((b, index) => {
                b.y += b.vy;
                if (b.y < 50) {
                    bubbles.splice(index, 1);
                    return;
                }
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.stroke();
            });

            requestAnimationFrame(updateAndRender);
        }

        // Initialize on load
        window.onload = function() {
            resizeCanvas();
            initParticles();
            updateParams();
            updateAndRender();
        };
    </script>
</body>
</html>
