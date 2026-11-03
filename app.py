<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>BioElectrio NanoLab: Microbial Electrolysis Cell</title>
<meta name="color-scheme" content="dark">
<style>
:root{--bg:#060b16;--panel:#0c1424;--line:#1f2d45;--ink:#eaf0fa;--mute:#93a3bd;--accent:#38bdf8;--gold:#facc15;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:dark}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*,*::before,*::after{box-sizing:inherit}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:20px}
.wrap{max-width:1040px;margin:0 auto}
h1{font-size:1.45rem;margin:0 0 4px;font-weight:650;letter-spacing:-.01em}
.sub{color:var(--mute);margin:0 0 16px;max-width:70ch}
canvas{display:block;width:100%;aspect-ratio:1000/520;background:#030712;border:1px solid var(--line);border-radius:10px}
.legend{display:flex;flex-wrap:wrap;gap:6px 18px;margin:10px 2px 14px;color:var(--mute);font-size:.85rem}
.legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px}
.controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-bottom:14px}
.controls label,.lbl{display:block;color:var(--mute);font-size:.85rem;margin-bottom:6px}
.controls b{color:var(--ink);font-weight:600}
input[type=range]{width:100%;accent-color:var(--accent)}
.seg{display:flex;gap:6px;flex-wrap:wrap}
button{font:inherit;color:var(--ink);background:#101b30;border:1px solid #2a3b5a;border-radius:8px;padding:7px 11px;cursor:pointer}
button[aria-pressed=true]{background:#0e3a55;border-color:var(--accent)}
button:focus-visible,input:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:14px}
.m .k{color:var(--mute);font-size:.82rem}.m .v{font-size:1.45rem;font-weight:650;color:var(--accent);margin-top:2px}
.m .s{color:var(--mute);font-size:.78rem}
.cmp{display:grid;gap:8px}
.row{display:grid;grid-template-columns:150px 1fr 90px;gap:10px;align-items:center;font-size:.88rem}
.track{height:10px;background:#0a1220;border-radius:5px;overflow:hidden}
.fill{height:100%;border-radius:5px;transition:width .25s}
.row.on .nm{color:var(--ink);font-weight:600}.row .nm{color:var(--mute)}
.note{color:var(--mute);font-size:.8rem;margin-top:10px}
.eq{display:flex;flex-wrap:wrap;gap:10px;align-items:stretch}.eq .c{flex:1 1 190px}.op{align-self:center;font-size:1.5rem;color:var(--mute)}
.c{background:#0a1220;border:1px solid var(--line);border-radius:8px;padding:10px 12px}.total .v{color:var(--gold)}
.mrow{display:grid;grid-template-columns:140px 1fr 1fr 1fr;gap:12px;align-items:center;font-size:.85rem;margin-bottom:8px}
.mrow .nm{color:var(--mute)}.mrow.on .nm{color:var(--ink);font-weight:600}.mut{color:var(--mute);font-size:.78rem}
.chk{display:flex;align-items:center;gap:8px;color:var(--ink);font-size:.88rem;margin:0}
.hd{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:12px}.hd h1{color:#2dd4bf;margin:0 0 2px;font-size:1.3rem}
.logo{width:46px;height:46px;border-radius:12px;background:linear-gradient(135deg,#2dd4bf,#38bdf8);display:grid;place-items:center;font-size:1.4rem}
.pill{margin-left:auto;border:1px solid #1d5f6b;background:#0b2b36;color:#67e8f9;border-radius:999px;padding:6px 14px;font-size:.85rem}
.mats{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
.mc{text-align:left;padding:12px 14px;border-radius:10px;background:#0a1220;border:1px solid var(--line)}.mc b{display:block;font-size:.95rem;margin-bottom:2px}.mc span{color:var(--mute);font-size:.8rem}
.mc[aria-pressed=true]{border-color:var(--c);background:#0d2236}.mc[aria-pressed=true] b{color:var(--c)}
.ev{display:grid;grid-template-columns:minmax(150px,1fr) 2fr;gap:8px 18px;font-size:.86rem}.ev span:nth-child(odd){color:var(--ink);font-weight:600}.ev span:nth-child(even){color:var(--mute)}
@media(max-width:600px){.ev{grid-template-columns:1fr}.ev span:nth-child(even){margin-bottom:6px}}
@media(max-width:520px){.row{grid-template-columns:100px 1fr 70px}.mrow{grid-template-columns:80px 1fr 1fr 1fr;gap:8px}}
</style>
</head>
<body>
<div class="wrap">
<header class="hd"><div class="logo">⚡</div><div><h1>BioElectrio NanoLab: Microbial Electrolysis Cell (MEC)</h1><div class="mut">Interactive molecular and systems-level digital twin simulator</div></div><span class="pill" id="live">● Live molecular simulation active</span></header>
<p class="sub">Bacteria on the anode eat organic waste and release electrons. Switch the electrode material and watch how quickly those electrons reach the cathode and turn into hydrogen.</p>

<canvas id="sim" aria-label="Animated microbial electrolysis cell"></canvas>
<div class="legend">
<span><i style="background:#4ade80"></i>Bacteria</span>
<span><i style="background:#fde68a"></i>Organic waste (COD)</span>
<span><i style="background:#facc15"></i>Electron (e⁻)</span>
<span><i style="background:#fb7185"></i>Proton (H⁺)</span>
<span><i style="background:#38bdf8"></i>Hydrogen bubble (H₂)</span>
</div>

<div class="panel" style="margin-bottom:14px"><span class="lbl">Electrode nanomaterial architecture</span><div class="mats" id="mats"></div></div>
<div class="controls panel">
<div><label for="vs">Applied voltage: <b id="vv">0.8 V</b></label><input type="range" id="vs" min="0.2" max="1.2" step="0.1" value="0.8"><div class="mut">The paper lists 0.6–1.0 V as typical for MECs</div></div>
<div><label for="cs">Waste strength (COD): <b id="cv">2500 mg/L</b></label><input type="range" id="cs" min="500" max="5000" step="100" value="2500"></div>
<div><label for="ts">Sim speed: <b id="tv">1×</b></label><input type="range" id="ts" min="0.25" max="2" step="0.25" value="1"></div>
<div id="aubox" hidden><label for="aus">Gold catalyst boost: <b id="auv">20×</b></label><input type="range" id="aus" min="1" max="20" step="1" value="20"><div class="mut">The paper reports up to 20× over plain graphite</div></div>
<div style="display:flex;align-items:end"><button id="pp" aria-pressed="false">Pause</button></div>
</div>

<div class="metrics">
<div class="panel m"><div class="k">Hydrogen production (model)</div><div class="v" id="h2">–</div><div class="s">m³ H₂ per m³ reactor per day</div></div>
<div class="panel m"><div class="k">COD removal</div><div class="v" id="cod">–</div><div class="s">share of waste consumed</div></div>
<div class="panel m"><div class="k">Charge-transfer resistance</div><div class="v" id="rct">–</div><div class="s">lower means faster electron transfer</div></div>
<div class="panel m"><div class="k">Electrons reaching cathode</div><div class="v" id="ems">–</div><div class="s">per second, measured in the animation</div></div>
</div>

<div class="panel" style="margin-bottom:14px"><span class="lbl">What’s improving the rate?</span>
<p class="note" style="margin:0 0 12px">The electrode material changes up to three things. More surface area lets more bacteria attach (watch the biofilm grow). Better electron transfer lets each cell hand its electrons over faster (watch the electrons speed up). A gold catalyst, where used, speeds up the hydrogen-forming reaction itself (watch the electron flow surge). Compared with plain graphite:</p>
<div class="eq">
<div class="c m"><div class="k">More room for bacteria</div><div class="v" id="fa">–</div><div class="s" id="fas"></div></div>
<span class="op">×</span>
<div class="c m"><div class="k">Faster electron handoff</div><div class="v" id="ft">–</div><div class="s" id="fts"></div></div>
<span class="op">×</span>
<div class="c m"><div class="k">Catalyst on the surface</div><div class="v" id="fc">–</div><div class="s" id="fcs"></div></div>
<span class="op">=</span>
<div class="c m total"><div class="k">Hydrogen production</div><div class="v" id="fx">–</div><div class="s" id="fxs"></div></div>
</div>
<div id="mt" style="margin-top:16px"></div>
<span class="lbl" style="margin-top:12px">Experiment: change one property at a time</span>
<div class="seg">
<label class="chk"><input type="checkbox" id="hsa"> Give every material graphite’s surface area</label>
<label class="chk"><input type="checkbox" id="htr"> Give every material graphite’s electron transfer</label>
</div>
<p class="note">Surface area has diminishing returns because the biofilm fills up, so 4× the area gives well under 4× the bacteria loading. The paper describes surface area only in general terms, so those multiples are illustrative. The paper lists coulombic efficiencies of 54–90% for MECs, so the hybrid’s 92% is a best case.</p>
</div>

<div class="panel"><span class="lbl">Hydrogen rate at your current voltage and COD</span>
<div class="cmp" id="cmp"></div>
<p class="note">Efficiency and area follow the card values you supplied. They put graphene + nickel at about 4× plain graphite (roughly 3.3 m³/m³/day at 0.8 V), inside the 1.5–4.2 m³/m³/day the paper lists for typical cells and above the roughly 3× it reports for graphene alone. Gold at 20× is the paper’s upper bound and lands far above typical MEC rates, so read it as a ceiling, not a prediction. Real rates depend on reactor design, microbial community and cathode catalyst.</p></div>

<div class="panel" style="margin-top:14px"><span class="lbl">What the research reports</span>
<div class="ev">
<span>Graphite decorated with gold nanoparticles</span><span>Up to 20× more hydrogen than plain graphite (the gold option’s best-case setting)</span>
<span>Graphene-modified biocathode</span><span>2.49 m³ H₂/m³/day with 89% electron recovery, roughly 3× an unmodified electrode</span>
<span>Nickel cobaltite–graphene on nickel foam</span><span>3.2× the hydrogen of bare foam, with 58% COD removal</span>
<span>rGO–CeO₂ nanocomposite</span><span>98% hydrogen recovery at the cathode</span>
<span>Carbon nanotubes</span><span>Described as particularly effective anode materials; no rate given</span>
<span>Typical MEC operation</span><span>0.6–1.0 V; about 1.5–3.4 m³ H₂/m³/day for Shewanella and Geobacter</span>
<span>Open problems</span><span>Nanoparticle clumping, toxicity at high doses, long-term stability, cost</span>
</div>
<p class="note">Source: Maturi et al. (2026), Bioresources and Bioprocessing 13:17, doi:10.1186/s40643-025-01001-4 (CC BY 4.0), which summarises earlier studies. Several of its graphene figures are for the cathode rather than the anode.</p></div>
</div>

<script>
(function(){
const W=1000,H=520;
const MAT={
 graphite:{name:'Plain Graphite Felt',sa:1,tr:.4,rct:1.8,col:'#7c8798',reach:14},
 cnt:{name:'Carbon Nanotubes (CNTs)',sa:4,tr:.68,rct:.35,col:'#38bdf8',reach:50},
 ni:{name:'Nickel Catalyst',sa:2.5,tr:.75,rct:.4,col:'#fb923c',reach:34},
 hyb:{name:'Graphene + Ni Hybrid',sa:9,tr:.92,rct:.1,col:'#34d399',reach:58},
 au:{name:'Gold-decorated graphite',sa:1,tr:.4,rct:.6,col:'#e0a82e',body:'#7c8798',reach:14,cat:20}
};
const S={V:.8,cod:2500,mat:'cnt',paused:false,ts:1,holdSA:false,holdTR:false,au:20};
// sa = surface area vs graphite; tr = share of electrons each cell hands to the electrode
function pr(m){const g=MAT.graphite,x=MAT[m],sa=S.holdSA?g.sa:x.sa,tr=S.holdTR?g.tr:x.tr,load=sa/(sa+1);
 return{sa,tr,load,cat:m==='au'?S.au:1,eff:tr*load,rct:S.holdTR?g.rct:x.rct,n:Math.min(22,Math.round(6*Math.pow(sa,.75))),speed:400*Math.pow(tr,1.5)}}
const $=id=>document.getElementById(id);
const cv=$('sim'),ctx=cv.getContext('2d');
let sc=1;
function fit(){const r=cv.getBoundingClientRect(),d=window.devicePixelRatio||1;cv.width=Math.round(r.width*d);cv.height=Math.round(r.width*H/W*d);sc=cv.width/W}
window.addEventListener('resize',fit);fit();

function rng(s){return()=>(s=(s*16807)%2147483647)/2147483647}
const r1=rng(7),cntT=[],rgoS=[];
for(let i=0;i<44;i++)cntT.push({y:74+i*8.5,len:26+r1()*28,sw:r1()*6-3,ph:r1()*6});
for(let i=0;i<15;i++)rgoS.push({y:78+i*24,len:30+r1()*26,ph:r1()*6});

const ELEC={ax:60,aw:30,ytop:70,ybot:440,cx:910,cw:30,wy:28};
let film=[],free=[],sub=[],E=[],P=[],B=[],arrivals=[],simT=0,acc=0,pAcc=0;

function build(){
 const M=MAT[S.mat],n=pr(S.mat).n;film=[];
 for(let i=0;i<n;i++)film.push({x:90+M.reach+12+Math.random()*6,y:ELEC.ytop+22+(ELEC.ybot-ELEC.ytop-44)*(i+.5)/n,ph:Math.random()*6,fl:0});
 E=[];P=[];
}
function mkFree(){free=[];for(let i=0;i<5;i++)free.push({x:200+Math.random()*230,y:80+Math.random()*340,a:Math.random()*6.28,t:Math.random()*2})}
function syncSub(){const n=Math.round(S.cod/60);while(sub.length<n)sub.push({x:170+Math.random()*280,y:70+Math.random()*360});sub.length=n}
build();mkFree();syncSub();
$('mats').innerHTML=Object.keys(MAT).map(k=>{const x=MAT[k];return '<button class="mc" data-m="'+k+'" aria-pressed="'+(k===S.mat)+'" style="--c:'+x.col+'"><b>'+x.name+'</b><span>'+x.sa.toFixed(1)+'× area | '+Math.round(x.tr*100)+'% efficiency'+(x.cat>1?' | up to '+x.cat+'× catalyst':'')+'</span></button>'}).join('');

function calc(m){const mo=S.cod/(S.cod+1500),v=.1+.9*(S.V-.2);return{mo,v,t:pr(m).eff*pr(m).cat*mo*v}}
const rate=m=>10*calc(m).t;
function removal(m){const c=calc(m);return Math.min(98,100*(1-Math.exp(-4.2*pr(m).eff*(.4+c.v)*Math.pow(2500/S.cod,.35))))}

function spawn(){
 const M=MAT[S.mat],b=film[Math.floor(Math.random()*film.length)];if(!b)return;
 b.fl=.35;
 if(E.length<500)E.push({x:b.x,y:b.y,i:0,pts:[[75,b.y],[75,ELEC.wy],[925,ELEC.wy],[925,90+Math.random()*340]]});
 if(P.length<250)P.push({x:b.x+6,y:b.y+(Math.random()-.5)*10});
}
function step(dt){
 simT+=dt;const M=pr(S.mat),c=calc(S.mat);
 acc+=dt*40*c.t;while(acc>=1){acc--;spawn()}
 for(let i=E.length-1;i>=0;i--){
  const e=E[i],p=e.pts[e.i],dx=p[0]-e.x,dy=p[1]-e.y,d=Math.hypot(dx,dy);
  const sp=(e.i===0?M.speed*.6:M.speed)*(.5+c.v),mv=sp*dt;
  if(e.i===0){e.x+=(Math.random()-.5)*50*dt*(1-M.eff);e.y+=(Math.random()-.5)*50*dt*(1-M.eff)}
  if(mv>=d){e.x=p[0];e.y=p[1];e.i++;
   if(e.i>=e.pts.length){B.push({x:918,bx:918,y:e.y,r:2.5+Math.random()*3,vy:30+Math.random()*30,ph:Math.random()*6});arrivals.push(simT);E.splice(i,1)}
  }else{e.x+=dx/d*mv;e.y+=dy/d*mv}
 }
 for(let i=P.length-1;i>=0;i--){
  const q=P[i];q.x+=(90+220*c.v)*dt;q.y+=(Math.random()-.5)*90*dt;q.y=Math.max(70,Math.min(430,q.y));
  if(q.x>905)P.splice(i,1);
 }
 for(let i=B.length-1;i>=0;i--){const b=B[i];b.y-=b.vy*dt;b.x=b.bx+Math.sin(b.y*.06+b.ph)*5;b.r+=dt*.4;if(b.y<64)B.splice(i,1)}
 for(const f of free){f.t-=dt;if(f.t<=0){f.t=1+Math.random()*1.5;f.a=Math.random()*6.28}
  f.x+=Math.cos(f.a)*26*dt;f.y+=Math.sin(f.a)*26*dt;
  if(f.x<180||f.x>450){f.a=Math.PI-f.a;f.x=Math.max(180,Math.min(450,f.x))}
  if(f.y<70||f.y>430){f.a=-f.a;f.y=Math.max(70,Math.min(430,f.y))}}
 for(const s of sub){s.x+=(Math.random()-.5)*70*dt;s.y+=(Math.random()-.5)*70*dt;
  s.x=Math.max(150,Math.min(455,s.x));s.y=Math.max(62,Math.min(438,s.y))}
 for(const b of film)if(b.fl>0)b.fl-=dt;
 while(arrivals.length&&arrivals[0]<simT-5)arrivals.shift();
}

function rod(x,y,a,len,w,col,glow){
 ctx.save();ctx.translate(x,y);ctx.rotate(a);
 if(glow>0){ctx.fillStyle='rgba(250,204,21,'+(glow*1.6)+')';ctx.beginPath();ctx.ellipse(0,0,len+5,w+5,0,0,6.28);ctx.fill()}
 ctx.fillStyle=col;ctx.beginPath();ctx.ellipse(0,0,len,w,0,0,6.28);ctx.fill();
 ctx.fillStyle='rgba(255,255,255,.22)';ctx.beginPath();ctx.ellipse(-len*.2,-w*.35,len*.5,w*.3,0,0,6.28);ctx.fill();
 ctx.restore();
}
function dot(x,y,r,col){ctx.fillStyle=col;ctx.beginPath();ctx.arc(x,y,r,0,6.28);ctx.fill()}

function draw(){
 ctx.setTransform(sc,0,0,sc,0,0);
 ctx.fillStyle='#030712';ctx.fillRect(0,0,W,H);
 const M=MAT[S.mat];
 // chambers
 for(const x of[30,530]){
  ctx.fillStyle='rgba(18,32,58,.55)';ctx.fillRect(x,50,x===30?440:440,400);
  ctx.strokeStyle='#2c4064';ctx.lineWidth=2;ctx.strokeRect(x,50,440,400);
  ctx.strokeStyle='rgba(56,189,248,.25)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,62);ctx.lineTo(x+440,62);ctx.stroke();
 }
 // membrane
 ctx.fillStyle='#22314d';ctx.fillRect(470,50,60,400);
 ctx.fillStyle='#050b16';for(let y=62;y<445;y+=14){ctx.fillRect(494,y,12,5)}
 ctx.save();ctx.translate(488,250);ctx.rotate(-Math.PI/2);ctx.fillStyle='#93a3bd';ctx.font='12px system-ui';ctx.textAlign='center';ctx.fillText('Proton exchange membrane',0,0);ctx.restore();
 // anode electrode
 ctx.fillStyle=M.body||M.col;ctx.globalAlpha=(S.mat==='graphite'||S.mat==='au')?.9:.75;ctx.fillRect(ELEC.ax,ELEC.ytop,ELEC.aw,ELEC.ybot-ELEC.ytop);ctx.globalAlpha=1;
 ctx.lineCap='round';
 if(S.mat==='graphite'||S.mat==='au'){
  ctx.fillStyle='#7c8798';for(let y=ELEC.ytop;y<ELEC.ybot;y+=18){ctx.fillRect(90,y,6+((y*7)%6),10)}
  if(S.mat==='au'){ctx.fillStyle='#fcd34d';for(let i=0;i<80;i++){ctx.beginPath();ctx.arc(88+((i*37)%16),ELEC.ytop+4+(i*4.7)%360,2.4,0,6.28);ctx.fill()}}
 }else if(S.mat==='cnt'){
  ctx.strokeStyle='#7dd3fc';ctx.lineWidth=2.2;
  for(const t of cntT){ctx.beginPath();ctx.moveTo(90,t.y);const sw=Math.sin(simT*1.6+t.ph)*1.5+t.sw;ctx.quadraticCurveTo(90+t.len*.5,t.y+sw*2,90+t.len,t.y+sw*3);ctx.stroke()}
 }else{
  if(S.mat==='hyb'){ctx.strokeStyle='#6ee7b7';ctx.lineWidth=3;for(const s of rgoS){ctx.beginPath();for(let k=0;k<=s.len;k+=4){const yy=s.y+Math.sin(k*.35+s.ph+simT)*3.5;k?ctx.lineTo(90+k,yy):ctx.moveTo(90,yy)}ctx.stroke()}}
  ctx.fillStyle='#fb923c';const nn=S.mat==='ni'?90:60;for(let i=0;i<nn;i++){ctx.beginPath();ctx.arc(92+((i*53)%(S.mat==='ni'?34:46)),ELEC.ytop+4+(i*4.1)%360,S.mat==='ni'?3.2:2.4,0,6.28);ctx.fill()}
 }
 // cathode
 ctx.fillStyle='#f59e0b';ctx.fillRect(ELEC.cx,ELEC.ytop,ELEC.cw,ELEC.ybot-ELEC.ytop);
 // wire + source
 ctx.strokeStyle='#cbd5e1';ctx.lineWidth=3;ctx.lineCap='butt';ctx.beginPath();
 ctx.moveTo(75,ELEC.ytop);ctx.lineTo(75,ELEC.wy);ctx.lineTo(925,ELEC.wy);ctx.lineTo(925,ELEC.ytop);ctx.stroke();
 ctx.fillStyle='#0c1424';ctx.fillRect(470,10,60,36);ctx.strokeRect(470,10,60,36);
 ctx.fillStyle='#38bdf8';ctx.font='bold 15px system-ui';ctx.textAlign='center';ctx.fillText(S.V.toFixed(1)+' V',500,34);
 // labels
 ctx.fillStyle='#93a3bd';ctx.font='13px system-ui';ctx.textAlign='left';
 ctx.fillText('Anode (−): bacteria oxidize waste',40,478);
 ctx.textAlign='right';ctx.fillText('Cathode (+): protons + electrons make H₂',960,478);
 ctx.textAlign='left';ctx.fillStyle='#64748b';ctx.fillText(M.name,40,498);
 // substrate
 for(const s of sub)dot(s.x,s.y,2.2,'rgba(253,230,138,.8)');
 // bacteria
 for(const f of free)rod(f.x,f.y,f.a,9,4,'#22c55e',0);
 for(const b of film)rod(b.x,b.y,Math.PI/2+Math.sin(simT*2+b.ph)*.35,9,4.5,'#4ade80',Math.max(0,b.fl));
 // protons
 for(const q of P)dot(q.x,q.y,2.8,'#fb7185');
 // electrons
 for(const e of E){dot(e.x,e.y,4.5,'rgba(250,204,21,.25)');dot(e.x,e.y,2.8,'#facc15')}
 // bubbles
 for(const b of B){ctx.fillStyle='rgba(56,189,248,.22)';ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,6.28);ctx.fill();ctx.strokeStyle='#7dd3fc';ctx.lineWidth=1;ctx.stroke()}
}

function explain(){
 const m=S.mat,G=MAT.graphite,p=pr(m),fa=p.load/(G.sa/(G.sa+1)),ft=p.tr/G.tr,f1=x=>x.toFixed(1);
 $('fa').textContent=f1(fa)+'×';$('fas').textContent=f1(p.sa)+'× the area, but the biofilm saturates, so bacteria loading rises '+f1(fa)+'×';
 $('ft').textContent=f1(ft)+'×';$('fts').textContent=Math.round(p.tr*100)+'% of electrons handed over per cell vs '+Math.round(G.tr*100)+'% on graphite (resistance '+p.rct.toFixed(2)+' Ω)';
 $('fc').textContent=f1(p.cat)+'×';$('fcs').textContent=m==='au'?'Gold nanoparticles speed up hydrogen formation; the paper reports up to 20×':'No added catalyst on this anode';
 $('fx').textContent=f1(fa*ft*p.cat)+'×';$('fxs').textContent=f1(fa)+' × '+f1(ft)+' × '+f1(p.cat)+' as much hydrogen as graphite at this voltage and COD';
 $('mt').innerHTML='<div class="mrow"><span></span><span class="mut">Surface area (× graphite)</span><span class="mut">Electron transfer per cell</span><span class="mut">Catalyst boost</span></div>'+Object.keys(MAT).map(k=>{const x=MAT[k];return '<div class="mrow'+(k===m?' on':'')+'"><span class="nm">'+x.name+'</span><div><div class="track"><div class="fill" style="width:'+(x.sa/9*100)+'%;background:'+x.col+'"></div></div><span class="mut">'+f1(x.sa)+'× area</span></div><div><div class="track"><div class="fill" style="width:'+(x.tr*100)+'%;background:'+x.col+'"></div></div><span class="mut">'+Math.round(x.tr*100)+'% transfer</span></div><div><div class="track"><div class="fill" style="width:'+(pr(k).cat/20*100)+'%;background:'+x.col+'"></div></div><span class="mut">'+f1(pr(k).cat)+'× catalyst</span></div></div>'}).join('');
}
let lastM=0;
function metrics(){
 const m=S.mat;explain();
 $('h2').textContent=rate(m).toFixed(1);
 $('cod').textContent=removal(m).toFixed(0)+'%';
 $('rct').textContent=pr(m).rct.toFixed(2)+' Ω';
 $('ems').textContent=(arrivals.length/Math.min(5,Math.max(simT,1))).toFixed(1)+' /s';
 const rates=Object.keys(MAT).map(k=>rate(k)),mx=Math.max(...rates,1e-6);
 $('cmp').innerHTML=Object.keys(MAT).map((k,i)=>'<div class="row'+(k===m?' on':'')+'"><span class="nm">'+MAT[k].name+'</span><div class="track"><div class="fill" style="width:'+(rates[i]/mx*100).toFixed(0)+'%;background:'+MAT[k].col+'"></div></div><span>'+rates[i].toFixed(1)+'</span></div>').join('');
}

let last=performance.now();
function frame(now){
 const d=Math.min(.05,(now-last)/1000);last=now;
 if(!S.paused)step(d*S.ts);
 draw();
 if(now-lastM>250){lastM=now;metrics()}
 requestAnimationFrame(frame);
}

$('vs').addEventListener('input',e=>{S.V=parseFloat(e.target.value);$('vv').textContent=S.V.toFixed(1)+' V'});
$('cs').addEventListener('input',e=>{S.cod=parseInt(e.target.value);$('cv').textContent=S.cod+' mg/L';syncSub()});
$('ts').addEventListener('input',e=>{S.ts=parseFloat(e.target.value);$('tv').textContent=S.ts+'×'});
$('pp').addEventListener('click',e=>{S.paused=!S.paused;e.target.setAttribute('aria-pressed',S.paused);e.target.textContent=S.paused?'Resume':'Pause';$('live').textContent=S.paused?'● Simulation paused':'● Live molecular simulation active'});
document.querySelectorAll('#mats button').forEach(b=>b.addEventListener('click',()=>{
 S.mat=b.dataset.m;document.querySelectorAll('#mats button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 $('aubox').hidden=S.mat!=='au';build();arrivals=[];simT=Math.max(simT,0);metrics();
}));
$('aus').addEventListener('input',e=>{S.au=parseInt(e.target.value);$('auv').textContent=S.au+'×'});
$('hsa').addEventListener('change',e=>{S.holdSA=e.target.checked;build();arrivals=[];metrics()});
$('htr').addEventListener('change',e=>{S.holdTR=e.target.checked;build();arrivals=[];metrics()});
metrics();requestAnimationFrame(frame);
})();
</script>
</body>
</html>
