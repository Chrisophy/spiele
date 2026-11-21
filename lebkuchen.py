# -*- coding: utf-8 -*-
# Lebkuchen-Alarm
# IT('s) Possible
# 2026.11.21

EXT_ID = 'lebkuchen'
EXT_NAME = 'Lebkuchen-Alarm'
EXT_DESCRIPTION = '🍪 Überlebens-Spiel: Eine lange Nacht, hungrige Lebkuchen-Monster. Du läufst, die Wichtel-Waffen feuern von allein. Sterne sammeln, Stufen aufsteigen, Verbesserungen wählen und durchhalten, bis die Sonne aufgeht. Mit Fernbedienung oder Touch, familienfreundlich.'
EXT_LINKS = [('Lebkuchen-Alarm', 'index')]
EXT_SETTINGS = []


def register(api):
    api.route('index', lambda req: PAGE)
    api.widget('Lebkuchen-Alarm', lambda: {'text': 'Lebkuchen-Alarm', 'sub': 'Überlebe die Nacht, 5–10 Minuten', 'icon': '🍪'}, ttl=3600, icon='🍪')


PAGE = r"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Lebkuchen-Alarm</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}
html,body{height:100%;background:#0b0f26;color:#f1eefc;font-family:system-ui,sans-serif;overflow:hidden}
#app{height:100dvh;display:flex;flex-direction:column}
#hud{flex:none;display:flex;gap:14px;align-items:center;justify-content:space-between;padding:6px 76px 6px 12px;background:#141a3d;border-bottom:1px solid #2f3a7a;font-size:clamp(12px,2.3vmin,18px)}
#hud b{color:#ffd45a}
#stage{flex:1;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;background:#070a1a}
canvas{image-rendering:pixelated;image-rendering:crisp-edges;display:block;background:#0b0f26;touch-action:none}
#hint{position:absolute;left:50%;top:13%;transform:translateX(-50%);max-width:92%;background:rgba(11,15,38,.88);border:1px solid #5a6ad0;border-radius:10px;padding:7px 14px;font-size:clamp(12px,2.4vmin,19px);text-align:center;display:none;pointer-events:none}
#ov>:first-child{margin-top:auto}
#ov>:last-child{margin-bottom:auto}
#ov{position:absolute;inset:0;background:rgba(9,12,30,.84);display:none;flex-direction:column;align-items:center;justify-content:flex-start;gap:12px;padding:14px;text-align:center;overflow:auto}
#ov h1{font-size:clamp(24px,5vmin,44px);color:#ffd45a}
#ov p{max-width:700px;font-size:clamp(13px,2.4vmin,20px);color:#d8dcf8;line-height:1.35}
#ov .row{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;max-width:900px}
#ov .col{display:flex;flex-direction:column;gap:9px;width:min(440px,92%)}
.mb{background:#27306a;color:#fff;border:3px solid transparent;border-radius:12px;padding:10px 16px;font-size:clamp(14px,2.6vmin,22px);font-weight:700;cursor:pointer}
.mb small{display:block;font-size:.72em;color:#ffd45a;font-weight:600}
.mb.f{border-color:#5ec2ff;background:#36429e}
.mb.card{width:min(230px,30%);min-width:150px;display:flex;flex-direction:column;align-items:center;gap:6px;padding:12px 10px}
.mb.card img{width:48px;height:48px;image-rendering:pixelated}
.mb.card span{font-weight:500;font-size:.72em;color:#d8dcf8;line-height:1.25}
</style></head><body>
<div id="app">
<div id="hud"><span id="ht">🍪 Lebkuchen-Alarm</span><span id="hs"></span></div>
<div id="stage"><canvas id="cv" width="480" height="270"></canvas><div id="hint"></div><div id="ov"></div></div>
</div>
<script>
"use strict";
const $=s=>document.querySelector(s);
const el=(t,c)=>{const e=document.createElement(t);if(c)e.className=c;return e};
const VW=480,VH=270;
let seed=(Date.now()%2147483647)|0;
function rnd(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}
const rr=(a,b)=>a+(b-a)*rnd();
function hh(a,b){let h=Math.imul(a,374761393)+Math.imul(b,668265263)|0;h=Math.imul(h^h>>>13,1274126177);return((h^h>>>16)>>>0)/4294967296}
const cv=$('#cv'),ctx=cv.getContext('2d');
const ov=$('#ov'),hint=$('#hint');
let snd=true,best={};
try{snd=localStorage.getItem('lb_snd')!=='0';best=JSON.parse(localStorage.getItem('lb_best')||'{}')||{}}catch(e){}
function save(){try{localStorage.setItem('lb_snd',snd?'1':'0');localStorage.setItem('lb_best',JSON.stringify(best))}catch(e){}}
const cfg={hero:0,dur:300,diff:1};

/* ---------- Sprites ---------- */
function mk(w,h,fn){const c=document.createElement('canvas');c.width=w;c.height=h;fn(c.getContext('2d'),w,h);return c}
function flash(s){const c=document.createElement('canvas');c.width=s.width;c.height=s.height;const g=c.getContext('2d');g.drawImage(s,0,0);g.globalCompositeOperation='source-atop';g.fillStyle='#fff';g.fillRect(0,0,c.width,c.height);return c}
function circ(g,x,y,r,c){g.fillStyle=c;g.beginPath();g.arc(x,y,r,0,7);g.fill()}
function rect(g,x,y,w,h,c){g.fillStyle=c;g.fillRect(x,y,w,h)}
function star(g,x,y,R,r,c,n,rot){n=n||5;rot=rot===undefined?-Math.PI/2:rot;g.fillStyle=c;g.beginPath();for(let i=0;i<n*2;i++){const a=rot+i*Math.PI/n,d=i%2?r:R;g.lineTo(x+Math.cos(a)*d,y+Math.sin(a)*d)}g.closePath();g.fill()}
function line(g,pts,c,w){g.strokeStyle=c;g.lineWidth=w||1;g.beginPath();pts.forEach((p,i)=>i?g.lineTo(p[0],p[1]):g.moveTo(p[0],p[1]));g.stroke()}
function heroSpr(hat,coat){return mk(16,22,g=>{
 rect(g,4,18,3,4,'#3a2a20');rect(g,9,18,3,4,'#3a2a20');
 rect(g,3,10,10,9,coat);rect(g,3,15,10,1.5,'#fff7e0');
 circ(g,8,9,4.5,'#ffd7b0');
 g.fillStyle='#fff';g.beginPath();g.moveTo(3.5,10);g.lineTo(12.5,10);g.lineTo(8,18);g.closePath();g.fill();
 rect(g,6,7,1.4,1.4,'#222');rect(g,9,7,1.4,1.4,'#222');
 g.fillStyle=hat;g.beginPath();g.moveTo(3,7);g.lineTo(13,7);g.lineTo(9,0.5);g.closePath();g.fill();
 circ(g,9.2,1.2,1.6,'#fff');rect(g,3,6.3,10,1.8,'#fff')})}
const SP={};
SP.keks=mk(14,16,g=>{const b='#b86b2b';circ(g,7,4.5,4.2,b);rect(g,3,8,8,5,b);rect(g,0,8,3,2,b);rect(g,11,8,3,2,b);rect(g,3,13,3,3,b);rect(g,8,13,3,3,b);
 line(g,[[3,9.5],[11,9.5]],'#fff',1);rect(g,5,3.5,1.3,1.6,'#fff');rect(g,8,3.5,1.3,1.6,'#fff');rect(g,5.4,4.2,.8,1,'#300');rect(g,8.4,4.2,.8,1,'#300');
 line(g,[[5,6.8],[6,6.2],[7,6.8],[8,6.2],[9,6.8]],'#fff',1);rect(g,6.4,10,1.2,1.2,'#e33');rect(g,6.4,12,1.2,1.2,'#3b3')});
SP.gummi=mk(12,12,g=>{circ(g,3,2.5,2,'#ff8c1a');circ(g,9,2.5,2,'#ff8c1a');circ(g,6,7,5,'#ff9f33');rect(g,3.6,5.5,1.4,1.6,'#fff');rect(g,7,5.5,1.4,1.6,'#fff');rect(g,4,6.2,.8,1,'#222');rect(g,7.4,6.2,.8,1,'#222');line(g,[[4,9.5],[6,8.6],[8,9.5]],'#7a3a00',.9)});
SP.wolke=mk(22,16,g=>{circ(g,6,9,5,'#8d93ad');circ(g,11,6,6,'#9aa0ba');circ(g,16,9,5,'#8d93ad');rect(g,5,9,12,5,'#8d93ad');
 line(g,[[6,6.5],[9.5,8]],'#223',1.2);line(g,[[16,6.5],[12.5,8]],'#223',1.2);rect(g,7.5,8.5,1.4,1.6,'#fff');rect(g,13,8.5,1.4,1.6,'#fff');line(g,[[8,12.5],[11,11.3],[14,12.5]],'#223',1)});
SP.stollen=mk(28,18,g=>{g.fillStyle='#d8a257';g.beginPath();g.ellipse(14,10,13,7.5,0,0,7);g.fill();g.fillStyle='#fff8e8';g.beginPath();g.ellipse(14,7,11,4.2,0,0,7);g.fill();
 rect(g,9,6,2,2.4,'#222');rect(g,17,6,2,2.4,'#222');line(g,[[8,4.8],[12,6]],'#222',1.2);line(g,[[20,4.8],[16,6]],'#222',1.2);line(g,[[10,11],[14,9.6],[18,11]],'#7a3a00',1.2);
 circ(g,5,11,1.4,'#c33');circ(g,23,11,1.4,'#3a3')});
SP.haus=mk(54,54,g=>{rect(g,6,22,42,28,'#a85f26');rect(g,6,44,42,6,'#8a4a1a');
 g.fillStyle='#f6f1ff';g.beginPath();g.moveTo(1,24);g.lineTo(27,3);g.lineTo(53,24);g.closePath();g.fill();
 for(let i=0;i<7;i++)circ(g,6+i*7,24.5,3,'#f6f1ff');
 [[14,15,'#ff5a7a'],[27,9,'#5ac8ff'],[40,15,'#ffd45a'],[22,19,'#7aff9a'],[33,19,'#ff9a3a']].forEach(a=>circ(g,a[0],a[1],1.8,a[2]));
 rect(g,21,34,12,16,'#4a2508');circ(g,30,43,1,'#ffd45a');
 rect(g,10,28,8,7,'#ffe27a');rect(g,36,28,8,7,'#ffe27a');
 line(g,[[10,27],[17,31]],'#a01010',1.6);line(g,[[44,27],[37,31]],'#a01010',1.6);rect(g,13,31,2,3,'#a01010');rect(g,39,31,2,3,'#a01010');
 line(g,[[19,40],[27,37.5],[35,40]],'#f6f1ff',1.4);rect(g,9,50,6,4,'#f6f1ff');rect(g,39,50,6,4,'#f6f1ff');
 for(let i=0;i<5;i++){rect(g,14+i*6,46,3,1.6,'#f6f1ff')}});
const FL={};for(const k of Object.keys(SP))FL[k]=flash(SP[k]);
const HEROES=[{n:'Rot',w:'str',hat:'#e23a3a',coat:'#b32b2b',t:'Zuckerstreusel'},{n:'Blau',w:'sch',hat:'#3a7be2',coat:'#2b57b3',t:'Schneebälle'},{n:'Grün',w:'zim',hat:'#2fb35a',coat:'#237f40',t:'Zimtstern'}];
HEROES.forEach(h=>{h.spr=heroSpr(h.hat,h.coat);h.fl=flash(h.spr)});
const STAR=[0,1,2].map(i=>mk(9,9,g=>{star(g,4.5,4.7,4.3,1.9,['#5ec2ff','#6bff9a','#ffd45a'][i],5);star(g,4.5,4.7,2.2,1,'#fff',5)}));
SP.herz=mk(11,10,g=>{g.fillStyle='#ff4a6a';g.beginPath();g.moveTo(5.5,9.5);g.bezierCurveTo(-3,4,2,-2,5.5,2.6);g.bezierCurveTo(9,-2,14,4,5.5,9.5);g.fill();rect(g,3,2.5,1.5,1.5,'#ffd0d8')});
SP.mag=mk(11,11,g=>{g.lineWidth=3;g.strokeStyle='#d33';g.beginPath();g.arc(5.5,5.5,3.4,Math.PI,0);g.stroke();rect(g,.8,5.5,3,4,'#d33');rect(g,7.2,5.5,3,4,'#d33');rect(g,.8,8,3,2,'#eee');rect(g,7.2,8,3,2,'#eee')});
const PJ={};
PJ.str=mk(7,7,g=>{circ(g,3.5,3.5,2.8,'#ff6bd0');rect(g,2.4,1.4,1.2,2.6,'#fff');rect(g,3.6,3,1.2,2.4,'#ffe27a')});
PJ.sch=mk(10,10,g=>{circ(g,5,5,4.5,'#d8f0ff');circ(g,4,4,3,'#fff');circ(g,6.5,6.5,1.6,'#a8d4f4')});
PJ.zim=mk(15,15,g=>{star(g,7.5,7.6,7,3,'#a0561f',5);star(g,7.5,7.6,4.3,1.8,'#d89050',5);rect(g,6.5,6.5,2,2,'#fff3d0')});
const FX=mk(13,13,g=>{star(g,6.5,6.5,6.4,1.6,'#fff7b0',4);star(g,6.5,6.5,3.4,1,'#fff',4)});
const ICON={};
ICON.str=mk(16,16,g=>{g.translate(8,8);g.rotate(.7);rect(g,-6,-2.5,12,5,'#ff6bd0');rect(g,-3,-2.5,2,5,'#fff');rect(g,1,-2.5,2,5,'#ffe27a')});
ICON.sch=mk(16,16,g=>{circ(g,8,8,6.5,'#d8f0ff');circ(g,6.5,6.5,4.5,'#fff');circ(g,10,10,2.4,'#a8d4f4')});
ICON.zim=mk(16,16,g=>{star(g,8,8.2,7.6,3.2,'#a0561f',5);star(g,8,8.2,4.6,2,'#d89050',5)});
ICON.pud=mk(16,16,g=>{g.fillStyle='#e8a53a';g.beginPath();g.moveTo(2,13);g.lineTo(14,13);g.lineTo(12.5,5);g.lineTo(3.5,5);g.closePath();g.fill();g.fillStyle='#5a2f10';g.beginPath();g.ellipse(8,5,5,2.6,0,0,7);g.fill();circ(g,8,2.6,1.7,'#e33')});
ICON.fun=mk(16,16,g=>{star(g,8,8,7.6,1.8,'#ffe27a',4);star(g,8,8,3.8,1,'#fff',4);circ(g,13,3,1.4,'#fff');circ(g,3,13,1.2,'#fff')});
ICON.sho=mk(16,16,g=>{rect(g,3,2,6,9,'#c46a2a');rect(g,3,9,11,5,'#c46a2a');rect(g,3,13,11,2,'#fff');rect(g,3,2,6,2,'#fff')});
ICON.her=SP.herz;
ICON.mag=SP.mag;
ICON.mue=mk(16,16,g=>{g.fillStyle='#e23a3a';g.beginPath();g.moveTo(2,12);g.lineTo(14,12);g.lineTo(9,1.5);g.closePath();g.fill();rect(g,2,11,12,3,'#fff');circ(g,9.5,2.2,2,'#fff')});
ICON.uhr=mk(16,16,g=>{circ(g,8,8.5,6.5,'#fff7e0');circ(g,8,8.5,5.2,'#fff');line(g,[[8,8.5],[8,4.5]],'#222',1.3);line(g,[[8,8.5],[11,10]],'#222',1.3);circ(g,3.5,3,2,'#e33');circ(g,12.5,3,2,'#e33')});
ICON.klee=mk(16,16,g=>{[[5,5],[11,5],[5,11],[11,11]].forEach(p=>circ(g,p[0],p[1],3.4,'#3fc96a'));rect(g,7.4,8,1.2,7,'#2a8a46')});
ICON.heal=mk(16,16,g=>{g.drawImage(SP.herz,2,3)});
const TILE=[0,1].map(v=>mk(64,64,g=>{let s=v*7919+13;const r=()=>{s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff};
 g.fillStyle='#1f2f66';g.fillRect(0,0,64,64);
 for(let i=0;i<14;i++){const x=r()*64,y=r()*64;g.fillStyle=i%3?'rgba(220,235,255,.5)':'rgba(120,160,255,.35)';g.fillRect(x|0,y|0,i%4?1:2,1)}
 if(v){for(let i=0;i<5;i++){const x=r()*60+2,y=r()*60+2;g.fillStyle='#2d4a8c';g.fillRect(x|0,y|0,1,3);g.fillRect((x+2)|0,(y+1)|0,1,2);g.fillRect((x-2)|0,(y+1)|0,1,2)}}}));
const DECO=[
 mk(22,32,g=>{rect(g,9,25,4,6,'#5a3a1a');g.fillStyle='#1f6b3a';[[16,1,11,10],[8,4,14,16],[3,9,18,24]].forEach(a=>{g.beginPath();g.moveTo(11,a[1]);g.lineTo(11+a[2]/2+1,a[3]);g.lineTo(11-a[2]/2-1,a[3]);g.closePath();g.fill()});
  g.fillStyle='#f4f8ff';g.beginPath();g.moveTo(11,1);g.lineTo(15,9);g.lineTo(7,9);g.fill();rect(g,6,15,3,2,'#f4f8ff');rect(g,13,19,3,2,'#f4f8ff');rect(g,8,23,4,2,'#f4f8ff');circ(g,9,12,1.2,'#ff5a7a');circ(g,14,17,1.2,'#ffd45a');circ(g,7,21,1.2,'#5ac8ff');star(g,11,1.5,2,.8,'#ffd45a',5)}),
 mk(12,11,g=>{rect(g,1,3,10,8,'#c0392b');rect(g,5,3,2,8,'#ffd45a');rect(g,1,6,10,2,'#ffd45a');circ(g,4,2,2,'#ffd45a');circ(g,8,2,2,'#ffd45a')}),
 mk(8,18,g=>{for(let i=0;i<9;i++)rect(g,2,i*2+1,4,2,i%2?'#fff':'#e23a3a');rect(g,4,0,4,2,'#e23a3a');rect(g,6,1,2,3,'#e23a3a')}),
 mk(10,12,g=>{g.fillStyle='#8fd8ff';g.beginPath();g.moveTo(5,0);g.lineTo(9,5);g.lineTo(5,11);g.lineTo(1,5);g.closePath();g.fill();g.fillStyle='#e6f8ff';g.beginPath();g.moveTo(5,0);g.lineTo(5,11);g.lineTo(1,5);g.closePath();g.fill()})];
const GLOW=mk(300,56,g=>{g.font='bold 30px system-ui,sans-serif';g.textAlign='center';g.textBaseline='middle';g.shadowColor='#7fe3ff';g.shadowBlur=14;g.fillStyle='#bff3ff';g.fillText("IT('s) Possible",150,28);g.shadowBlur=5;g.fillStyle='#fff';g.fillText("IT('s) Possible",150,28)});

/* ---------- Sound ---------- */
let AC=null;const lastS={};
function ac(){if(!AC)try{AC=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}return AC}
function tone(f,d,type,vol,slide,delay){if(!snd)return;const a=ac();if(!a)return;try{const t0=a.currentTime+(delay||0),o=a.createOscillator(),g=a.createGain();o.type=type||'square';o.frequency.setValueAtTime(f,t0);if(slide)o.frequency.exponentialRampToValueAtTime(Math.max(30,f*slide),t0+d);g.gain.setValueAtTime(vol||.04,t0);g.gain.exponentialRampToValueAtTime(.0001,t0+d);o.connect(g);g.connect(a.destination);o.start(t0);o.stop(t0+d+.03)}catch(e){}}
function sfx(n){const now=performance.now(),gap={pop:50,star:35,shot:110,hurt:200,boom:90,zap:120}[n]||0;if(gap&&lastS[n]&&now-lastS[n]<gap)return;lastS[n]=now;
 switch(n){case'pop':tone(320,.07,'square',.025,.5);break;case'star':tone(700+Math.min(500,(G?G.combo:0)*40),.06,'triangle',.03);break;case'shot':tone(520,.05,'square',.012,.6);break;
 case'hurt':tone(150,.2,'sawtooth',.06,.5);break;case'lvl':[523,659,784,1047].forEach((f,i)=>tone(f,.14,'triangle',.06,0,i*.09));break;
 case'win':[523,659,784,1047,1319].forEach((f,i)=>tone(f,.2,'triangle',.06,0,i*.12));break;case'lose':[392,330,262,196].forEach((f,i)=>tone(f,.25,'triangle',.06,0,i*.16));break;
 case'sel':tone(600,.05,'square',.03);break;case'ok':tone(800,.08,'square',.04);break;case'boom':tone(110,.25,'sawtooth',.06,.4);break;case'zap':tone(900,.1,'sawtooth',.03,.4);break;case'heal':tone(600,.15,'triangle',.05,1.6);break}}

/* ---------- Daten ---------- */
const WP=[
 {id:'str',n:'Zuckerstreusel',d:['Wirft Streusel auf den nächsten Gegner','Mehr Schaden','Ein Streusel mehr','Streusel durchbohren einen Gegner','Mehr Schaden, schneller','Noch ein Streusel']},
 {id:'sch',n:'Schneeball-Ring',d:['Zwei Schneebälle kreisen um dich','Mehr Schaden','Ein Schneeball mehr','Größerer Ring, mehr Schaden','Noch ein Schneeball','Noch ein Schneeball, schneller']},
 {id:'zim',n:'Zimtstern',d:['Fliegt in Laufrichtung durch alle Gegner','Mehr Schaden','Wirft schneller','Zwei Sterne','Mehr Schaden','Drei Sterne']},
 {id:'pud',n:'Pudding-Welle',d:['Schiebt Gegner weg und macht sie langsam','Größere Welle','Kommt öfter','Mehr Schaden','Größere Welle','Kommt viel öfter']},
 {id:'fun',n:'Funkenregen',d:['Funken treffen zufällige Gegner','Größerer Funke','Zwei Funken','Mehr Schaden','Drei Funken','Größerer Funke, öfter']}];
const PS=[
 {id:'sho',n:'Zuckerschuhe',d:'Du läufst 10% schneller'},
 {id:'her',n:'Lebkuchenherz',d:'Mehr Leben und langsame Heilung'},
 {id:'mag',n:'Sternen-Magnet',d:'Sterne kommen von weiter weg'},
 {id:'mue',n:'Zipfelmütze',d:'Alle Waffen machen 12% mehr Schaden'},
 {id:'uhr',n:'Sanduhr',d:'Waffen laden 8% schneller'},
 {id:'klee',n:'Glücksklee',d:'Mehr Sterne und öfter Herzen'}];
const ET={
 keks:{hp:10,sp:38,dmg:7,r:6,xp:1,kb:1},gummi:{hp:6,sp:54,dmg:5,r:5,xp:1,kb:1.2},wolke:{hp:24,sp:32,dmg:9,r:8,xp:3,kb:.8},
 stollen:{hp:85,sp:22,dmg:13,r:10,xp:10,kb:.35},haus:{hp:700,sp:20,dmg:18,r:20,xp:60,kb:.05,boss:1}};
const DF=[{n:'Leicht',hp:.8,dm:.7,sp:.8},{n:'Normal',hp:1,dm:1,sp:1},{n:'Knifflig',hp:1.25,dm:1.25,sp:1.25}];
const DURS=[300,600];
const WI=['str','sch','zim','pud','fun'];
const PSPEED=78,MAXEN=110,MAXST=150;
const mmss=t=>{t=Math.max(0,Math.ceil(t));return((t/60)|0)+':'+String(t%60).padStart(2,'0')};

/* ---------- Spielzustand ---------- */
let G=null,mode='main',joy=null,forced=null,keys={},acc=0,last=0,quitting=0,trap=0,bk=0,msgT=0;
const need=l=>Math.round((4+3*l+l*l*.25)*(G&&G.dur<400?.75:1));
function newGame(){const h=HEROES[cfg.hero];
 G={t:0,p:0,dur:cfg.dur,diff:cfg.diff,df:DF[cfg.diff],hero:cfg.hero,x:0,y:0,fx:1,fy:0,hp:100,mhp:100,inv:0,lvl:1,xp:0,nd:0,kills:0,combo:0,ph:'run',win:0,
  wp:{},ps:{},wt:{str:.3,zim:.5,pud:1,fun:.8},en:[],pr:[],st:[],pk:[],pt:[],pl:[],sp:[],sa:0,ev:[0,0,0],bs:[0,0],pid:0,cx:0,cy:0,dm:1,fr:0};
 G.wp[h.w]=1;G.nd=need(1);mode='play';ov.style.display='none';pushTrap();hudT();say('Lauf mit den Pfeiltasten. Deine Waffen feuern von allein. Zurück = Pause',4000);sfx('ok')}
const Wl=id=>G.wp[id]||0,Pl=id=>G.ps[id]||0;
function say(t,ms){hint.textContent=t;hint.style.display='block';msgT=performance.now()+(ms||2500)}
function hudT(){const hs=$('#hs');if(!G){hs.textContent=best.k?'':'';return}hs.innerHTML='⏱ <b>'+mmss(G.dur-G.t)+'</b> bis Sonnenaufgang · Stufe <b>'+G.lvl+'</b> · Vertrieben <b>'+G.kills+'</b>'}
function near(x,y,maxD,k,skip){const out=[];const m2=maxD*maxD;for(const e of G.en){if(e.dead)continue;const dx=e.x-x,dy=e.y-y,d=dx*dx+dy*dy;if(d>m2)continue;
  if(out.length<k){out.push([d,e]);out.sort((a,b)=>a[0]-b[0])}else if(d<out[k-1][0]){out[k-1]=[d,e];out.sort((a,b)=>a[0]-b[0])}}return out.map(a=>a[1])}
function hit(e,d,nx,ny,k){const S=G;e.hp-=d*S.dm;e.fl=.07;const T=ET[e.t];e.kx+=nx*k*T.kb;e.ky+=ny*k*T.kb;if(e.hp<=0)e.dead=1}
function spawn(type,ang,dist){const S=G;if(S.en.length>=MAXEN+10&&type!=='haus')return null;const T=ET[type],hs=(1+1.5*S.p)*S.df.hp*(type==='haus'?(1+S.bs[0]*.5):1);
 const e={t:type,x:S.x+Math.cos(ang)*dist,y:S.y+Math.sin(ang)*dist,hp:T.hp*hs,mhp:T.hp*hs,kx:0,ky:0,fl:0,sl:0,hc:[0,0,0,0,0],dead:0,pid:-1};S.en.push(e);return e}
function pickType(){const p=G.p,w=[['keks',10]];if(p>.06)w.push(['gummi',5]);if(p>.28)w.push(['wolke',2+4*p]);if(p>.5)w.push(['stollen',.6+2*(p-.5)]);
 let s=0;for(const a of w)s+=a[1];let r=rnd()*s;for(const a of w){r-=a[1];if(r<=0)return a[0]}return'keks'}
function dropStar(x,y,v){const S=G;if(S.st.length>=MAXST){S.xp+=v;return}S.st.push({x,y,v,t:S.t})}
function kill(e){const S=G,T=ET[e.t];S.kills++;S.combo=Math.min(12,S.combo+1);sfx('pop');
 for(let i=0;i<(T.boss?24:5);i++)if(S.pt.length<170)S.pt.push({x:e.x,y:e.y,vx:rr(-60,60),vy:rr(-80,10),l:rr(.3,.6),c:['#ff6bd0','#ffe27a','#7fe3ff','#fff','#6bff9a'][(rnd()*5)|0],s:rnd()<.3?2:1});
 const mul=1+.1*Pl('klee');dropStar(e.x,e.y,Math.round(T.xp*mul*(T.boss?1:1)));
 if(T.boss){for(let i=0;i<4;i++)dropStar(e.x+rr(-14,14),e.y+rr(-14,14),15);S.pk.push({k:'herz',x:e.x,y:e.y});S.pk.push({k:'mag',x:e.x+10,y:e.y+4});say('Das Lebkuchenhaus ist besiegt! 🎉',3000)}
 else{const r=rnd(),hc=.014+.006*Pl('klee');if(r<hc)S.pk.push({k:'herz',x:e.x,y:e.y});else if(r<hc+.006)S.pk.push({k:'mag',x:e.x,y:e.y})}}
function rollCards(){const S=G,pool=[];
 for(const w of WP){const l=Wl(w.id);if(l>=6)continue;if(!l&&Object.keys(S.wp).length>=4)continue;pool.push({k:'w',o:w,l})}
 const np=Object.keys(S.ps).length;for(const p of PS){const l=Pl(p.id);if(l>=5)continue;if(!l&&np>=4)continue;pool.push({k:'p',o:p,l})}
 for(let i=pool.length-1;i>0;i--){const j=(rnd()*(i+1))|0;[pool[i],pool[j]]=[pool[j],pool[i]]}
 const out=pool.slice(0,3);if(!out.length)out.push({k:'h',o:{id:'heal',n:'Leckerli',d:'Füllt dein Leben auf'},l:0});return out}
function applyCard(c){const S=G;if(c.k==='w')S.wp[c.o.id]=c.l+1;else if(c.k==='p'){S.ps[c.o.id]=c.l+1;if(c.o.id==='her'){S.mhp+=20;S.hp+=20}}else{S.hp=S.mhp}
 S.dm=1+.12*Pl('mue');sfx('ok')}
function levelUp(){const S=G;S.ph='lvl';S.xp-=S.nd;S.lvl++;S.nd=need(S.lvl);sfx('lvl');const ch=rollCards();held();
 showOv('⭐ Stufe '+S.lvl+'!','Wähle eine Verbesserung. Links/Rechts wählt, OK bestätigt.',ch.map(c=>({t:c.o.n,card:1,ic:ICON[c.o.id],sub:c.k==='h'?'Einmalig':c.l?'Stufe '+c.l+' → '+(c.l+1):'Neu!',d:c.k==='w'?c.o.d[c.l]:c.o.d,f:()=>{applyCard(c);ov.style.display='none';S.ph='run';if(S.xp>=S.nd)levelUp();else hudT()}})),0,'row')}
function held(){keys={};joy=null}

/* ---------- Simulation ---------- */
const GS=14,GN=56,gh=new Int32Array(GN*GN);
function step(){const S=G;if(!S||S.ph!=='run')return;const dt=1/60;S.t+=dt;S.p=Math.min(1,S.t/S.dur);S.fr++;
 if(S.inv>0)S.inv-=dt;
 let ix=0,iy=0;if(forced){ix=forced[0];iy=forced[1]}else if(joy){ix=joy.vx;iy=joy.vy}else{ix=(keys.ArrowRight||keys.d?1:0)-(keys.ArrowLeft||keys.a?1:0);iy=(keys.ArrowDown||keys.s?1:0)-(keys.ArrowUp||keys.w?1:0)}
 let m=Math.hypot(ix,iy);if(m>1){ix/=m;iy/=m;m=1}
 if(m>.05){S.fx=ix/m;S.fy=iy/m}
 const spd=PSPEED*(1+.1*Pl('sho'));S.x+=ix*spd*dt;S.y+=iy*spd*dt;
 if(Pl('her')&&S.hp<S.mhp)S.hp=Math.min(S.mhp,S.hp+.15*Pl('her')*dt);
 if(S.combo>0&&S.fr%90===0)S.combo--;
 const cdm=1-.08*Pl('uhr');
 /* Waffen */
 let l=Wl('str');if(l){S.wt.str-=dt;if(S.wt.str<=0){const n=1+((l-1)/2|0),ts=near(S.x,S.y,240,n);if(ts.length){S.wt.str=(l>=5?.7:.9)*cdm;ts.forEach(e=>{const dx=e.x-S.x,dy=e.y-S.y,d=Math.hypot(dx,dy)||1;S.pr.push({k:0,x:S.x,y:S.y-4,vx:dx/d*240,vy:dy/d*240,l:1.2,d:7+2*(l-1)+(l>=5?2:0),r:3.5,pc:l>=4?1:0})});sfx('shot')}else S.wt.str=.2}}
 l=Wl('zim');if(l){S.wt.zim-=dt;if(S.wt.zim<=0){S.wt.zim=(1.9-(l>=3?.35:0))*cdm;const n=l>=6?3:l>=4?2:1,a0=Math.atan2(S.fy,S.fx);for(let i=0;i<n;i++){const a=a0+(i-(n-1)/2)*.35;S.pr.push({k:2,x:S.x,y:S.y-4,vx:Math.cos(a)*150,vy:Math.sin(a)*150,l:1.3,d:12+3*l+(l>=5?3:0),r:7,pc:99,rot:0})}sfx('shot')}}
 l=Wl('pud');if(l){S.wt.pud-=dt;if(S.wt.pud<=0){S.wt.pud=(3.4-.25*l-(l>=3?.3:0))*cdm;S.pl.push({r:6,R:46+8*l+(l>=5?8:0),id:++S.pid,d:9+3*l+(l>=4?4:0)});sfx('boom')}}
 l=Wl('fun');if(l){S.wt.fun-=dt;if(S.wt.fun<=0){S.wt.fun=(1.7-.1*l)*cdm;const n=1+(l/2|0)+(l>=5?1:0),ts=near(S.x,S.y,230,12);for(let i=0;i<n&&ts.length;i++){const e=ts[(rnd()*ts.length)|0];S.sp.push({x:e.x,y:e.y,t:.3,r:16+2*l+(l>=6?4:0),d:14+4*l+(l>=4?4:0)})}}}
 l=Wl('sch');if(l){const n=[2,2,3,3,4,5][l-1],R=30+l*2+(l>=4?6:0),w=2.4+(l>=6?.8:0),dm=5+1.5*l+(l>=4?2:0);S.orb=[];
  for(let i=0;i<n;i++){const a=S.t*w+i*6.2832/n,bx=S.x+Math.cos(a)*R,by=S.y-4+Math.sin(a)*R;S.orb.push([bx,by]);
   for(const e of S.en){if(e.dead||e.hc[1]>S.t)continue;const dx=e.x-bx,dy=e.y-by,rr2=ET[e.t].r+5;if(dx*dx+dy*dy<rr2*rr2){e.hc[1]=S.t+.5;const d=Math.hypot(dx,dy)||1;hit(e,dm,dx/d,dy/d,90)}}}}
 else S.orb=null;
 /* Geschosse */
 for(const p of S.pr){p.x+=p.vx*dt;p.y+=p.vy*dt;p.l-=dt;if(p.k===2)p.rot+=dt*8;
  for(const e of S.en){if(e.dead)continue;const dx=e.x-p.x,dy=e.y-p.y,rr2=ET[e.t].r+p.r;if(dx*dx+dy*dy>rr2*rr2||e.hc[p.k]>S.t)continue;
   e.hc[p.k]=S.t+(p.k===2?.45:.3);const d=Math.hypot(p.vx,p.vy)||1;hit(e,p.d,p.vx/d,p.vy/d,p.k===2?110:70);if(p.k===2)continue;if(p.pc>0)p.pc--;else{p.l=0;break}}}
 S.pr=S.pr.filter(p=>p.l>0);
 for(const q of S.pl){q.r+=(q.R/.45)*dt;for(const e of S.en){if(e.dead||e.pid===q.id)continue;const dx=e.x-S.x,dy=e.y-S.y,d=Math.hypot(dx,dy),rr2=ET[e.t].r;if(d<q.r+rr2&&d>q.r-18-rr2){e.pid=q.id;e.sl=1.6;hit(e,q.d,dx/(d||1),dy/(d||1),170)}}}
 S.pl=S.pl.filter(q=>q.r<q.R);
 for(const f of S.sp){if(f.t>0){f.t-=dt;if(f.t<=0){f.fl=.15;sfx('zap');for(const e of S.en){if(e.dead)continue;const dx=e.x-f.x,dy=e.y-f.y,rr2=f.r+ET[e.t].r;if(dx*dx+dy*dy<rr2*rr2){const d=Math.hypot(dx,dy)||1;hit(e,f.d,dx/d,dy/d,60)}}}}else f.fl-=dt}
 S.sp=S.sp.filter(f=>f.t>0||f.fl>0);
 /* Spawns */
 const rate=(.9+5.2*Math.pow(S.p,1.1))*S.df.sp*(S.dur<400?1.25:1);S.sa=Math.min(3,S.sa+dt*rate);
 while(S.sa>=1&&S.en.length<MAXEN){const t=pickType();if(t==='gummi'){S.sa-=2;const a=rnd()*6.283;for(let i=0;i<3;i++)spawn('gummi',a+rr(-.2,.2),rr(290,320))}else{S.sa-=1;spawn(t,rnd()*6.283,rr(290,320))}}
 const EV=[[.18,'gummi',22,'Gummibär-Ring! Lauf durch eine Lücke!'],[.52,'keks',28,'Lebkuchen-Ring!'],[.76,'wolke',14,'Grummelwolken-Ring!']];
 EV.forEach((v,i)=>{if(!S.ev[i]&&S.p>=v[0]){S.ev[i]=1;for(let k=0;k<v[2];k++)spawn(v[1],k/v[2]*6.2832,235);say(v[3],3000)}});
 [[.42,0],[.8,1]].forEach(b=>{if(!S.bs[b[1]]&&S.p>=b[0]){S.bs[b[1]]=1;spawn('haus',rnd()*6.283,300);say('Das riesige Lebkuchenhaus kommt!',3500);sfx('boom')}});
 /* Gegner */
 const px=S.x,py=S.y; for(let i=0;i<S.en.length;i++){const e=S.en[i];if(e.dead)continue;const T=ET[e.t];let dx=px-e.x,dy=py-e.y,d=Math.hypot(dx,dy)||1;
  const v=T.sp*(e.sl>0?.55:1)*(1+.33*S.p)*(S.df.sp>1?1.08:1);if(e.sl>0)e.sl-=dt;
  e.x+=dx/d*v*dt+e.kx*dt;e.y+=dy/d*v*dt+e.ky*dt;e.kx*=.92;e.ky*=.92;if(e.fl>0)e.fl-=dt;
  if(d>340&&!T.boss){const a=rnd()*6.283;e.x=px+Math.cos(a)*300;e.y=py+Math.sin(a)*300;d=300}
  if(d<T.r+5&&S.inv<=0){S.hp-=T.dmg*S.df.dm;S.inv=.6;sfx('hurt');S.combo=0;if(S.hp<=0){S.hp=0;end(0)}}
  const gx_=((e.x-px)/GS+GN/2)|0,gy_=((e.y-py)/GS+GN/2)|0;e.gc=(gx_>=0&&gy_>=0&&gx_<GN&&gy_<GN)?gy_*GN+gx_:-1}
 /* Abstoßen (Gitter) */
 const L=S.en;const idx=[];for(const e of L)if(!e.dead&&e.gc>=0)idx.push(e);
 gh.fill(-1);const nx=new Int32Array(idx.length);for(let i=0;i<idx.length;i++){const e=idx[i];nx[i]=gh[e.gc];gh[e.gc]=i}
 for(let i=0;i<idx.length;i++){const e=idx[i],T=ET[e.t];if(T.boss)continue;const cx=e.gc%GN,cy=(e.gc/GN)|0;
  for(let oy=-1;oy<=1;oy++)for(let ox=-1;ox<=1;ox++){const X=cx+ox,Y=cy+oy;if(X<0||Y<0||X>=GN||Y>=GN)continue;for(let j=gh[Y*GN+X];j>=0;j=nx[j]){if(j===i)continue;const o=idx[j],dx=e.x-o.x,dy=e.y-o.y,md=(T.r+ET[o.t].r)*.8,d2=dx*dx+dy*dy;
    if(d2<md*md&&d2>.01){const d=Math.sqrt(d2),f=(md-d)*.5;e.x+=dx/d*f;e.y+=dy/d*f}}}}
 /* Tod */
 let w=0;for(let i=0;i<L.length;i++){const e=L[i];if(e.dead)kill(e);else L[w++]=e}L.length=w;
 /* Sterne & Pickups */
 const R=36*(1+.3*Pl('mag'));
 for(let i=S.st.length-1;i>=0;i--){const s=S.st[i];const dx=px-s.x,dy=py-s.y,d=Math.hypot(dx,dy);
  if(s.mg||d<R){s.mg=1;const v=220;s.x+=dx/(d||1)*v*dt;s.y+=dy/(d||1)*v*dt}
  if(d<8){S.xp+=s.v;S.st.splice(i,1);sfx('star')}}
 for(let i=S.pk.length-1;i>=0;i--){const k=S.pk[i];const d=Math.hypot(px-k.x,py-k.y);if(d<12){if(k.k==='herz'){S.hp=Math.min(S.mhp,S.hp+30);sfx('heal');say('Herz! +30 Leben',1500)}else{S.st.forEach(s=>s.mg=1);say('Sternen-Magnet!',1500);sfx('heal')}S.pk.splice(i,1)}}
 for(const p of S.pt){p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=160*dt;p.l-=dt}S.pt=S.pt.filter(p=>p.l>0);
 if(S.ph==='run'&&S.xp>=S.nd)levelUp();
 if(S.ph==='run'&&S.t>=S.dur)end(1)}
function end(win){const S=G;if(S.ph==='end')return;S.ph='end';S.win=win;
 if(win){for(const e of S.en){for(let i=0;i<3;i++)if(S.pt.length<170)S.pt.push({x:e.x,y:e.y,vx:rr(-40,40),vy:rr(-60,0),l:rr(.4,.9),c:'#ffe27a',s:2})}S.en=[];sfx('win')}else sfx('lose');
 const key=S.dur+'_'+S.diff,tm=win?S.dur:Math.floor(S.t);if(!best[key]||tm>best[key]){best[key]=tm;S.nb=1;save()}
 hudT();setTimeout(()=>{if(G===S&&S.ph==='end')endMenu()},win?900:1200)}
function endMenu(){const S=G;held();
 showOv(S.win?'🌅 Die Sonne geht auf!':'😴 Der Wichtel ist müde',(S.win?'Geschafft! Die Lebkuchen sind weg und es gibt Frühstück. ':'Die Lebkuchen waren zu viele. ')+'Zeit: '+mmss(S.t)+' von '+mmss(S.dur)+' · Stufe '+S.lvl+' · Vertrieben: '+S.kills+(S.nb?' · Neue Bestzeit!':''),
  [{t:'🔄 Nochmal',f:newGame},{t:'☰ Hauptmenü',f:mainMenu},{t:'🚪 Beenden',f:quit}],0,'col')}

/* ---------- Menüs ---------- */
let mbs=[],mbi=0;
function focusMb(i){mbs.forEach(x=>x.classList.remove('f'));mbi=Math.max(0,Math.min(mbs.length-1,i));if(mbs[mbi]){const b=mbs[mbi];b.classList.add('f');const r=b.getBoundingClientRect(),o=ov.getBoundingClientRect();if(r.top<o.top+8)ov.scrollTop-=o.top+8-r.top;else if(r.bottom>o.bottom-8)ov.scrollTop+=r.bottom-o.bottom+8}}
let curItems=[],curArgs=null;
function showOv(title,msg,items,focusIdx,layout){curItems=items;curArgs=[title,msg,items,layout];ov.innerHTML='';const h=el('h1');h.textContent=title;ov.append(h);
 if(msg){const p=el('p');p.textContent=msg;ov.append(p)}
 const box=el('div',layout||'col');items.forEach(it=>{const b=el('button','mb'+(it.card?' card':''));
  if(it.card){const im=new Image();im.src=it.ic.toDataURL();const a=el('b');a.textContent=it.t;const s=el('small');s.textContent=it.sub;const d=el('span');d.textContent=it.d;b.append(im,a,s,d)}else b.textContent=it.t;
  b.onclick=()=>{ui();it.f()};box.append(b)});ov.append(box);
 ov.style.display='flex';mbs=[...ov.querySelectorAll('.mb')];focusMb(focusIdx||0)}
function ui(){if(AC&&AC.state==='suspended')try{AC.resume()}catch(e){}}
function navMenu(dir){if(!mbs.length)return;const c=mbs[mbi].getBoundingClientRect(),cx=c.left+c.width/2,cy=c.top+c.height/2;let best_=-1,bd=1e9;
 mbs.forEach((b,i)=>{if(i===mbi)return;const r=b.getBoundingClientRect(),x=r.left+r.width/2-cx,y=r.top+r.height/2-cy;let pr,pe;
  if(dir==='ArrowRight'){pr=x;pe=Math.abs(y)}else if(dir==='ArrowLeft'){pr=-x;pe=Math.abs(y)}else if(dir==='ArrowDown'){pr=y;pe=Math.abs(x)}else{pr=-y;pe=Math.abs(x)}
  if(pr<=2)return;const d=pr+pe*2.2;if(d<bd){bd=d;best_=i}});if(best_>=0){focusMb(best_);sfx('sel')}}
function adj(d){const it=curItems[mbi];if(it&&it.adj){it.adj(d);sfx('sel');return true}return false}
function mainMenu(){mode='main';G=null;hudT();const h=HEROES[cfg.hero],key=cfg.dur+'_'+cfg.diff,b=best[key];
 showOv('🍪 Lebkuchen-Alarm','Die Nacht ist lang und die Lebkuchen sind hungrig! Lauf mit den Pfeiltasten, deine Waffen feuern von allein. Sammle Sterne, steige auf, wähle Verbesserungen und halte durch, bis die Sonne aufgeht. Zurück-Taste = Pause.'+(b?' Beste Zeit: '+mmss(b)+(b>=cfg.dur?' (geschafft!)':'')+'.':''),
 [{t:'▶ Spielen',f:newGame},
  {t:'Wichtel: '+h.n+' ('+h.t+')  ‹ ›',f:()=>{cfg.hero=(cfg.hero+1)%3;mainMenu();focusMb(1)},adj:d=>{cfg.hero=(cfg.hero+d+3)%3;mainMenu();focusMb(1)}},
  {t:'Nachtlänge: '+(cfg.dur/60)+' Minuten  ‹ ›',f:()=>{cfg.dur=cfg.dur===300?600:300;mainMenu();focusMb(2)},adj:()=>{cfg.dur=cfg.dur===300?600:300;mainMenu();focusMb(2)}},
  {t:'Schwierigkeit: '+DF[cfg.diff].n+'  ‹ ›',f:()=>{cfg.diff=(cfg.diff+1)%3;mainMenu();focusMb(3)},adj:d=>{cfg.diff=(cfg.diff+d+3)%3;mainMenu();focusMb(3)}},
  {t:'Ton: '+(snd?'an':'aus'),f:()=>{snd=!snd;save();mainMenu();focusMb(4)}},
  {t:'🚪 Beenden',f:quit}],0,'col')}
function pauseMenu(){if(!G||G.ph!=='run')return;G.ph='pause';held();
 showOv('Pause','Hoch/Runter wählt, OK bestätigt.',[{t:'▶ Weiter',f:resume},{t:'🔄 Neustart',f:newGame},{t:'☰ Hauptmenü',f:mainMenu},{t:'Ton: '+(snd?'an':'aus'),f:()=>{snd=!snd;save();pauseMenu_();focusMb(3)}},{t:'🚪 Beenden',f:quit}],0,'col')}
function pauseMenu_(){G.ph='run';pauseMenu()}
function resume(){if(!G||G.ph!=='pause')return;ov.style.display='none';G.ph='run';sfx('ok')}
function quit(){quitting=1;if(trap)history.back();else closeGame()}
function pushTrap(){if(trap)return;try{history.pushState({lb:1},'');trap=1}catch(e){}}
function closeGame(){try{if(window.parent!==window){window.parent.history.back();return}}catch(e){}if(history.length>1)history.back();else location.href='/ui/'}
addEventListener('popstate',()=>{if(!trap)return;trap=0;
 if(quitting){closeGame();return}
 if(mode==='play'&&G){pushTrap();if(Date.now()-bk<350)return;
  if(G.ph==='run')pauseMenu();else if(G.ph==='pause')resume();else if(G.ph==='end')mainMenu()}
 else closeGame()});
document.addEventListener('visibilitychange',()=>{if(document.hidden&&G&&G.ph==='run')pauseMenu()});
addEventListener('blur',()=>{keys={}});
addEventListener('keydown',e=>{if(e.ctrlKey||e.altKey||e.metaKey)return;const k=e.key;ui();let used=true;const BACK=k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack';if(BACK)bk=Date.now();
 const inMenu=ov.style.display==='flex';
 if(inMenu){
  if(k==='ArrowLeft'||k==='ArrowRight'){if(!adj(k==='ArrowRight'?1:-1))navMenu(k)}
  else if(k.startsWith('Arrow'))navMenu(k);
  else if(k==='Enter'||k===' '){if(!e.repeat&&mbs[mbi])mbs[mbi].click()}
  else if(BACK&&G&&G.ph==='pause')resume();
  else used=false}
 else if(G&&G.ph==='run'){
  if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','a','d','w','s'].includes(k))keys[k]=1;
  else if(BACK||k==='p'||k==='Enter'||k===' ')pauseMenu();
  else used=false}
 else used=false;
 if(used){e.preventDefault();e.stopPropagation()}},true);
addEventListener('keyup',e=>{delete keys[e.key]},true);
function toLog(e){const r=cv.getBoundingClientRect();return[(e.clientX-r.left)/r.width*VW,(e.clientY-r.top)/r.height*VH]}
cv.addEventListener('pointerdown',e=>{ui();if(!G||G.ph!=='run')return;const[x,y]=toLog(e);joy={id:e.pointerId,x0:x,y0:y,x,y,vx:0,vy:0};try{cv.setPointerCapture(e.pointerId)}catch(_){}e.preventDefault()});
cv.addEventListener('pointermove',e=>{if(!joy||joy.id!==e.pointerId)return;const[x,y]=toLog(e);joy.x=x;joy.y=y;let dx=x-joy.x0,dy=y-joy.y0;const d=Math.hypot(dx,dy);if(d>40){joy.x0=x-dx/d*40;joy.y0=y-dy/d*40;dx=x-joy.x0;dy=y-joy.y0}
 const m=Math.hypot(dx,dy);if(m<6){joy.vx=0;joy.vy=0}else{const s=Math.min(1,m/30);joy.vx=dx/m*s;joy.vy=dy/m*s}});
const jend=e=>{if(joy&&joy.id===e.pointerId)joy=null};cv.addEventListener('pointerup',jend);cv.addEventListener('pointercancel',jend);

/* ---------- Zeichnen ---------- */
let anim=0;
function draw(){const S=G,cx=S?S.x:0,cy=S?S.y:0,ox=Math.round(VW/2-cx),oy=Math.round(VH/2-cy);const g=ctx;
 const x0=Math.floor((cx-VW/2)/64),y0=Math.floor((cy-VH/2)/64);
 for(let ty=y0;ty<=y0+5;ty++)for(let tx=x0;tx<=x0+8;tx++)g.drawImage(TILE[hh(tx,ty)<.5?0:1],tx*64+ox,ty*64+oy);
 g.globalAlpha=.55+.25*Math.sin(anim*2);g.drawImage(GLOW,-150+ox,24+oy);g.globalAlpha=1;
 for(const s of(S?S.st:[])){const sx=s.x+ox,sy=s.y+oy;if(sx<-10||sx>VW+10||sy<-10||sy>VH+10)continue;g.drawImage(STAR[s.v>=15?2:s.v>=3?1:0],sx-4|0,sy-4+Math.round(Math.sin(anim*4+s.x)*1)|0)}
 for(const k of(S?S.pk:[])){const sp=SP[k.k];g.drawImage(sp,k.x+ox-sp.width/2|0,k.y+oy-sp.height/2+Math.round(Math.sin(anim*5)*1.5)|0)}
 const L=[];const dx0=Math.floor((cx-VW/2-30)/80),dy0=Math.floor((cy-VH/2-30)/80);
 for(let j=dy0;j<=dy0+4;j++)for(let i=dx0;i<=dx0+7;i++){const a=hh(i,j);if(a<.24){const t=hh(j,i)<.5?0:hh(i+5,j)<.5?1:hh(j+9,i)<.6?2:3;L.push({y:j*80+hh(i,j+3)*70,x:i*80+hh(i+3,j)*70,s:DECO[t],dc:1})}}
 if(S){for(const e of S.en)L.push({y:e.y+ET[e.t].r,e});L.push({y:S.y+8,pl:1})}else L.push({y:6,x:0,pl:1,idle:1});
 L.sort((a,b)=>a.y-b.y);
 for(const o of L){if(o.dc){g.drawImage(o.s,o.x+ox-o.s.width/2|0,o.y+oy-o.s.height|0)}
  else if(o.e){const e=o.e,sp=(e.fl>0?FL:SP)[e.t];g.drawImage(sp,e.x+ox-sp.width/2|0,e.y+oy-sp.height/2+Math.round(Math.sin(anim*8+e.x)*.8)|0)}
  else{const h=HEROES[S?S.hero:cfg.hero],blink=S&&S.inv>0&&((anim*20)|0)%2;if(!blink)g.drawImage(h.spr,(S?S.x:0)+ox-8|0,(S?S.y:0)+oy-20+(S&&(keys.ArrowLeft||keys.ArrowRight||keys.ArrowUp||keys.ArrowDown||joy)?Math.round(Math.sin(anim*16)*1):Math.round(Math.sin(anim*3)*.5))|0)}}
 if(S){
  for(const p of S.pr){if(p.k===2){g.save();g.translate(p.x+ox,p.y+oy);g.rotate(p.rot);g.drawImage(PJ.zim,-7.5,-7.5);g.restore()}else g.drawImage(PJ[p.k===0?'str':'sch'],p.x+ox-3.5|0,p.y+oy-3.5|0)}
  if(S.orb)for(const b of S.orb)g.drawImage(PJ.sch,b[0]+ox-5|0,b[1]+oy-5|0);
  for(const q of S.pl){g.strokeStyle='rgba(255,226,122,'+(.8*(1-q.r/q.R)+.15)+')';g.lineWidth=4;g.beginPath();g.arc(S.x+ox,S.y+oy-4,q.r,0,7);g.stroke()}
  for(const f of S.sp){if(f.t>0){g.strokeStyle='rgba(255,255,160,.8)';g.lineWidth=1;g.beginPath();g.arc(f.x+ox,f.y+oy,f.r*(1-f.t/.3*.4),0,7);g.stroke()}else{g.globalAlpha=Math.max(0,f.fl/.15);g.drawImage(FX,f.x+ox-f.r|0,f.y+oy-f.r|0,f.r*2,f.r*2);g.globalAlpha=1}}
  for(const p of S.pt){g.fillStyle=p.c;g.fillRect(p.x+ox|0,p.y+oy|0,p.s,p.s)}
  const na=.5*(1-S.p*S.p);if(na>.02){g.fillStyle='rgba(8,10,46,'+na+')';g.fillRect(0,0,VW,VH)}
  if(S.p>.88){g.fillStyle='rgba(255,170,70,'+(.16*(S.p-.88)/.12)+')';g.fillRect(0,0,VW,VH)}
  hudDraw(S)}
 else{g.fillStyle='rgba(8,10,46,.35)';g.fillRect(0,0,VW,VH)}}
function hudDraw(S){const g=ctx;g.fillStyle='rgba(0,0,0,.5)';g.fillRect(0,0,VW,7);g.fillStyle='#ffd45a';g.fillRect(0,0,Math.min(1,S.xp/S.nd)*VW,7);
 g.font='bold 9px system-ui,sans-serif';g.textBaseline='top';g.fillStyle='#fff';g.fillText('Stufe '+S.lvl,4,9);
 const t=S.p;g.fillStyle='rgba(0,0,0,.5)';g.fillRect(VW/2-60,9,120,5);g.fillStyle='#7fb8ff';g.fillRect(VW/2-60,9,120*t,5);g.fillStyle=t>.85?'#ffd45a':'#fff';g.beginPath();g.arc(VW/2-60+120*t,11.5,4,0,7);g.fill();
 const bw=90;g.drawImage(SP.herz,4,VH-16);g.fillStyle='rgba(0,0,0,.55)';g.fillRect(18,VH-14,bw+2,8);g.fillStyle=S.hp<S.mhp*.3?'#ff3a3a':'#ff6a8a';g.fillRect(19,VH-13,bw*S.hp/S.mhp,6);
 g.fillStyle='#fff';g.fillText(Math.ceil(S.hp)+'',bw+24,VH-15);
 let x=4;const row=(o,ic,l)=>{g.drawImage(ic,x,VH-36,16,16);g.fillStyle='#ffd45a';g.fillText(l,x+10,VH-28);x+=19};
 for(const id of WI)if(S.wp[id])row(id,ICON[id],S.wp[id]);x+=4;for(const p of PS)if(S.ps[p.id])row(p.id,ICON[p.id],S.ps[p.id]);
 const b=S.en.find(e=>ET[e.t].boss);if(b){g.fillStyle='rgba(0,0,0,.55)';g.fillRect(VW/2-70,18,140,7);g.fillStyle='#c0392b';g.fillRect(VW/2-69,19,138*Math.max(0,b.hp)/b.mhp,5);g.fillStyle='#fff';g.fillText('Lebkuchenhaus',VW/2-26,26)}
 if(joy){g.strokeStyle='rgba(255,255,255,.35)';g.lineWidth=2;g.beginPath();g.arc(joy.x0,joy.y0,22,0,7);g.stroke();g.fillStyle='rgba(255,255,255,.35)';g.beginPath();g.arc(joy.x,joy.y,9,0,7);g.fill()}}
function fit(){const st=$('#stage'),w=st.clientWidth,h=st.clientHeight,s=Math.min(w/VW,h/VH);cv.style.width=Math.floor(VW*s)+'px';cv.style.height=Math.floor(VH*s)+'px'}
addEventListener('resize',fit);
let hudAcc=0;
function frame(ts){requestAnimationFrame(frame);const dt=Math.min(.1,(ts-last)/1000||0);last=ts;anim+=dt;acc+=dt;let n=0;while(acc>=1/60&&n<4){acc-=1/60;step();n++}if(acc>1/60)acc=0;
 hudAcc+=dt;if(hudAcc>.25){hudAcc=0;hudT()}
 if(hint.style.display==='block'&&performance.now()>msgT)hint.style.display='none';
 draw()}

/* ---------- Test-Schnittstelle ---------- */
function botMove(){const S=G;let fx=0,fy=0;for(const e of S.en){const dx=S.x-e.x,dy=S.y-e.y,d2=dx*dx+dy*dy;if(d2<110*110){const d=Math.sqrt(d2)||1,w=(1-d/110)*(ET[e.t].boss?2.2:1);fx+=dx/d*w;fy+=dy/d*w}}
 let bs=null,bd=1e9;for(const s of S.st){const d=Math.hypot(s.x-S.x,s.y-S.y);if(d<bd){bd=d;bs=s}}
 if(bs&&bd<140&&Math.hypot(fx,fy)<.8){fx+=(bs.x-S.x)/bd*.6;fy+=(bs.y-S.y)/bd*.6}
 fx+=Math.cos(S.t*.35)*.22;fy+=Math.sin(S.t*.35)*.22;return[fx,fy]}
window.SV={
 seed:s=>{seed=s|0},
 start:(h,dur,diff)=>{cfg.hero=h;cfg.dur=dur;cfg.diff=diff;newGame()},
 st:()=>G&&{t:G.t,p:G.p,hp:G.hp,mhp:G.mhp,lvl:G.lvl,xp:G.xp,nd:G.nd,kills:G.kills,ph:G.ph,win:G.win,en:G.en.length,st:G.st.length,pr:G.pr.length,wp:G.wp,ps:G.ps,x:G.x,y:G.y,mode},
 step:n=>{for(let i=0;i<n;i++)step()},
 move:(x,y)=>{forced=x===null?null:[x,y]},
 pick:i=>{if(G&&G.ph==='lvl'&&mbs[i])mbs[i].click()},
 run:(n,bot)=>{for(let i=0;i<n;i++){if(!G||G.ph==='end')break;if(G.ph==='lvl'){mbs[0].click();continue}if(bot)forced=botMove();step()}forced=null;return G&&{t:G.t,hp:G.hp,lvl:G.lvl,ph:G.ph,win:G.win,kills:G.kills,en:G.en.length}},
 give:(k,v)=>{if(!G)return;if(k==='xp')G.xp+=v;else if(k==='hp')G.hp=v;else if(k==='t')G.t=v},
 spawn:(t,n)=>{for(let i=0;i<n;i++)spawn(t,rnd()*6.283,rr(60,200))},
 draw:()=>draw(),cards:()=>mbs.map(b=>b.innerText)};
fit();mainMenu();requestAnimationFrame(frame);
</script></body></html>
"""
