# -*- coding: utf-8 -*-
# Torten-Duell
# IT('s) Possible
# 2026.11.20

EXT_ID = 'torten'
EXT_NAME = 'Torten-Duell'
EXT_DESCRIPTION = '🎂 Zwei Wichtel-Trupps werfen abwechselnd Torten aufeinander, mit Wind, Kratern im Gelände und Puddingsee. Wer satt ist, scheidet aus. Gegen den Computer oder zu zweit am Fernseher, Fernbedienung und Touch.'
EXT_LINKS = [('Torten-Duell', 'index')]
EXT_SETTINGS = []


def register(api):
    api.route('index', lambda req: PAGE)
    api.widget('Torten-Duell', lambda: {'text': 'Torten-Duell', 'sub': 'Abwechselnd werfen, 1–2 Spieler', 'icon': '🎂'}, ttl=3600, icon='🎂')


PAGE = r"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Torten-Duell</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}
html,body{height:100%;background:#120d1f;color:#f1eefc;font-family:system-ui,sans-serif;overflow:hidden}
#app{height:100dvh;display:flex;flex-direction:column}
#hud{flex:none;display:flex;gap:14px;align-items:center;justify-content:space-between;padding:6px 76px 6px 12px;background:#1c1431;border-bottom:1px solid #3a2c63;font-size:clamp(12px,2.3vmin,18px)}
#hud b{color:#ffd45a}
#stage{flex:1;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;background:#0b0816}
canvas{image-rendering:pixelated;image-rendering:crisp-edges;display:block;background:#0b0816;border-radius:6px;touch-action:none}
#hint{position:absolute;left:50%;top:8px;transform:translateX(-50%);max-width:92%;background:rgba(18,13,31,.88);border:1px solid #5a47a0;border-radius:10px;padding:7px 14px;font-size:clamp(12px,2.2vmin,18px);text-align:center;opacity:0;transition:opacity .25s;pointer-events:none}
#hint.on{opacity:1}
#bar{flex:none;display:flex;gap:6px;justify-content:center;flex-wrap:wrap;padding:6px 8px 8px;background:#1c1431;border-top:1px solid #3a2c63}
#bar button{min-width:58px;padding:4px 8px 3px;border-radius:12px;border:3px solid transparent;background:#2b2150;color:#fff;font-size:12px;display:flex;flex-direction:column;align-items:center;position:relative;cursor:pointer}
#bar button i{font-style:normal;font-size:clamp(20px,3.6vmin,32px);line-height:1.1}
#bar button b{font-weight:600;font-size:clamp(10px,1.7vmin,15px)}
#bar button u{text-decoration:none;position:absolute;right:3px;top:1px;font-weight:800;color:#ffd45a;font-size:clamp(11px,1.9vmin,16px)}
#bar button.sel{background:#4b3a96;border-color:#ffd45a}
#bar button.off{opacity:.35}
#bar button.go{background:#c0392b}
#bar button.f{outline:4px solid #5ec2ff;outline-offset:1px}
#bar .sep{width:10px}
#ov>:first-child{margin-top:auto}
#ov>:last-child{margin-bottom:auto}
#ov{position:absolute;inset:0;background:rgba(14,9,26,.82);display:none;flex-direction:column;align-items:center;justify-content:flex-start;gap:12px;padding:14px;text-align:center;overflow:auto}
#ov h1{font-size:clamp(24px,5vmin,44px);color:#ffd45a}
#ov p{max-width:660px;font-size:clamp(13px,2.4vmin,20px);color:#d8d2f2;line-height:1.35}
#ov .row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;max-width:720px}
.mb{background:#2f2560;color:#fff;border:3px solid transparent;border-radius:12px;padding:10px 16px;font-size:clamp(14px,2.6vmin,22px);font-weight:700;cursor:pointer}
.mb small{display:block;font-size:.7em;color:#ffd45a;font-weight:600}
.mb.f{border-color:#5ec2ff;background:#40318a}
</style></head><body>
<div id="app">
<div id="hud"><span id="ht"></span><span id="hs"></span></div>
<div id="stage"><canvas id="cv" width="640" height="320"></canvas><div id="hint"></div><div id="ov"></div></div>
<div id="bar"></div>
</div>
<script>
"use strict";
const $=s=>document.querySelector(s);
const el=(t,c)=>{const e=document.createElement(t);if(c)e.className=c;return e};
const W=320,H=160,PUD=H-5;
let seed=Date.now()%2147483647;
function rnd(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}
const cv=$('#cv'),ctx=cv.getContext('2d'),lcv=document.createElement('canvas');lcv.width=W;lcv.height=H;const lx=lcv.getContext('2d');
const tcv=document.createElement('canvas');tcv.width=W;tcv.height=H;const tctx=tcv.getContext('2d');const id=tctx.createImageData(W,H);
const TH=[
{a:'#0b1030',b:'#2b2f7a',g:'#7fe3ff',f:'#fff3b0',h:'#171b4d',s:'#ffe27a'},
{a:'#3a1450',b:'#e0603a',g:'#ffd45a',f:'#ffb347',h:'#2a0f3a',s:'#ffd0a0'},
{a:'#08201f',b:'#146a5e',g:'#6bffb8',f:'#b6ff7a',h:'#0a2b2a',s:'#8fffd0'},
{a:'#1b0a33',b:'#6a1b90',g:'#ff6bf0',f:'#dcdcff',h:'#2a0f4a',s:'#ff9bf6',d:1},
{a:'#0a1c33',b:'#2f78b0',g:'#b6f3ff',f:'#f0fcff',h:'#123a5e',s:'#ffffff'},
{a:'#14081f',b:'#7a1f3f',g:'#ff9a6b',f:'#ffdf6b',h:'#2a0a1a',s:'#ffcf6b'}];
const bgc=document.createElement('canvas');bgc.width=640;bgc.height=320;
const gt=document.createElement('canvas');gt.width=640;gt.height=90;
let th=TH[0],bits=[],cx=160,cy=60;
function setTheme(i){th=TH[i%TH.length];const c=bgc.getContext('2d'),g=c.createLinearGradient(0,0,0,320);g.addColorStop(0,th.a);g.addColorStop(1,th.b);c.fillStyle=g;c.fillRect(0,0,640,320);
 c.fillStyle=th.h;c.beginPath();c.moveTo(0,320);for(let x=0;x<=640;x+=16)c.lineTo(x,255+Math.sin(x/90+i)*22+Math.sin(x/37+i*2)*8);c.lineTo(640,320);c.closePath();c.fill();
 c.fillStyle=th.f;c.beginPath();c.arc(566,62,30,0,6.2832);c.fill();
 c.fillStyle='rgba(0,0,0,.09)';c.beginPath();c.arc(584,80,6,0,6.2832);c.fill();c.beginPath();c.arc(550,44,4,0,6.2832);c.fill();
 c.strokeStyle='#5a3b2a';c.lineWidth=3;c.beginPath();c.arc(566,68,12,.3,2.85);c.stroke();
 const g2=gt.getContext('2d');g2.clearRect(0,0,640,90);g2.font='bold 58px system-ui,sans-serif';g2.textAlign='center';g2.textBaseline='middle';
 g2.shadowColor=th.g;g2.shadowBlur=28;g2.fillStyle=th.g;g2.fillText("IT('s) Possible",320,46);g2.fillText("IT('s) Possible",320,46);
 g2.shadowBlur=10;g2.fillStyle='#fff';g2.fillText("IT('s) Possible",320,46);
 bits=[];for(let k=0;k<22;k++)bits.push({x:Math.random()*640,y:Math.random()*320,vx:(Math.random()-.5)*.3,vy:-.1-Math.random()*.3,p:Math.random()*6,r:2+(k%3)})}
function drawBg(t){ctx.drawImage(bgc,0,0);
 for(const b of bits){b.x+=b.vx;b.y+=b.vy;if(b.y<-4){b.y=324;b.x=Math.random()*640}if(b.x<-4)b.x=644;if(b.x>644)b.x=-4;
  ctx.globalAlpha=.3+.5*Math.sin(t/500+b.p);ctx.fillStyle=th.d?'hsl('+Math.floor((t/18+b.p*60)%360)+',90%,65%)':th.s;ctx.fillRect(b.x|0,b.y|0,b.r,b.r)}
 ctx.globalAlpha=.6+.35*Math.sin(t/650);ctx.drawImage(gt,0,Math.round(64+Math.sin(t/1100)*7));ctx.globalAlpha=1;
 const dx=Math.max(-2,Math.min(2,(cx*2-566)/90)),dy=Math.max(-2,Math.min(2,(cy*2-62)/70));ctx.fillStyle='#2b1d12';
 if(t%4300<150){ctx.fillRect(552,56,9,2);ctx.fillRect(572,56,9,2)}else{ctx.fillRect(554+dx,52+dy,5,8);ctx.fillRect(573+dx,52+dy,5,8);ctx.fillStyle='#fff';ctx.fillRect(555+dx,53+dy,1,2);ctx.fillRect(574+dx,53+dy,1,2)}}
let snd=true,AC=null,aid=true;
try{snd=localStorage.getItem('td_snd')!=='0';aid=localStorage.getItem('td_aid')!=='0'}catch(e){}
function save(){try{localStorage.setItem('td_snd',snd?'1':'0');localStorage.setItem('td_aid',aid?'1':'0')}catch(e){}}
function beep(f,d,t,v,when,f2){if(!snd)return;try{if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();if(AC.state==='suspended')AC.resume();const n=AC.currentTime+(when||0),o=AC.createOscillator(),g=AC.createGain();o.type=t||'square';o.frequency.setValueAtTime(f,n);if(f2)o.frequency.linearRampToValueAtTime(f2,n+d);g.gain.setValueAtTime(v||.04,n);g.gain.exponentialRampToValueAtTime(.0001,n+d);o.connect(g);g.connect(AC.destination);o.start(n);o.stop(n+d+.03)}catch(e){}}
const SFX={fire:()=>beep(300,.18,'triangle',.06,0,900),splat:()=>{beep(180,.25,'sawtooth',.07,0,60);beep(500,.1,'square',.03,.02,200)},mini:()=>beep(260,.1,'sawtooth',.04,0,90),plop:()=>beep(520,.2,'sine',.06,0,180),sel:()=>beep(700,.06,'square',.03),turn:()=>{beep(600,.08,'triangle',.05);beep(800,.1,'triangle',.05,.09)},win:()=>[523,659,784,1047].forEach((f,i)=>beep(f,.22,'triangle',.06,i*.14)),no:()=>beep(160,.14,'sawtooth',.03)};
const T=new Uint8Array(W*H);let dirty=false,dx0=0,dy0=0,dx1=-1,dy1=-1;
function sol(x,y){if(x<0||x>=W)return true;if(y<0||y>=H)return false;return T[y*W+x]!==0}
function solP(x,y){return x>=0&&x<W&&y>=0&&y<H&&T[y*W+x]!==0}
function colFree(c,fy){for(let k=0;k<8;k++)if(sol(c,fy-k))return false;return true}
function mark(x,y){if(!dirty){dx0=dx1=x;dy0=dy1=y;dirty=true}else{if(x<dx0)dx0=x;if(x>dx1)dx1=x;if(y<dy0)dy0=y;if(y>dy1)dy1=y}}
function px(x,y){const i=(y*W+x)*4,t=T[y*W+x],d=id.data;if(!t){d[i+3]=0;return}let r,g,b;
 if(t===3){const s=y%3===0;r=s?150:198;g=s?98:142;b=s?48:82}
 else{const top=y===0||T[(y-1)*W+x]===0;
  if(top){r=250;g=214;b=230}
  else if(y>1&&T[(y-2)*W+x]===0){r=236;g=170;b=200}
  else{const h=((x*31+y*17)^(x*7))&7;r=124+h*3;g=82+h*2;b=54+h}}
 d[i]=r;d[i+1]=g;d[i+2]=b;d[i+3]=255}
function paintAll(){for(let y=0;y<H;y++)for(let x=0;x<W;x++)px(x,y);tctx.putImageData(id,0,0);dirty=false}
function flush(){if(!dirty)return;const y0=Math.max(0,dy0-2),y1=Math.min(H-1,dy1+2),x0=Math.max(0,dx0),x1=Math.min(W-1,dx1);for(let y=y0;y<=y1;y++)for(let x=x0;x<=x1;x++)px(x,y);tctx.putImageData(id,0,0,x0,y0,x1-x0+1,y1-y0+1);dirty=false}
const PAL={S:'#f2c496',W:'#ffffff',T:'#f0b429',L:'#5b3a1e',E:'#222222',B:'#8a5a1a'};
const BASE=['....H...','...HHH..','..HHHHH.','..SSESS.','..WWWWW.','...WWW..','..TTTTT.','..TBBBT.','...T.T..'];
function mkRows(legs,mods){const r=BASE.concat([legs]).map(s=>s.split(''));(mods||[]).forEach(m=>{r[m[0]][m[1]]=m[2]});return r.map(x=>x.join(''))}
function mkS(rows,flip,hc){const c=document.createElement('canvas');c.width=8;c.height=rows.length;const x=c.getContext('2d');if(flip){x.translate(8,0);x.scale(-1,1)}rows.forEach((row,y)=>{for(let i=0;i<8;i++){const ch=row[i];if(ch!=='.'){x.fillStyle=ch==='H'?hc:PAL[ch];x.fillRect(i,y,1,1)}}});return c}
const HATC=['#e03a3a','#3a7ae0'];
const SPR=HATC.map(hc=>({stand:[mkS(mkRows('..LL.L..'),true,hc),mkS(mkRows('..LL.L..'),false,hc)],air:[mkS(mkRows('..L..L..',[[5,1,'S'],[5,7,'S']]),true,hc),mkS(mkRows('..L..L..',[[5,1,'S'],[5,7,'S']]),false,hc)]}));
const WEAP=[{k:'pie',n:'Torte',e:'🥧',r:9,d:38},{k:'big',n:'Riesentorte',e:'🎂',r:17,d:70},{k:'conf',n:'Streuer',e:'🎊',r:6,d:24}];
const TEAMN=['Rot','Blau'],TCOL=['#ff6b6b','#6bb0ff'];
const NAMES=[['Pip','Plum','Mimi','Fritz'],['Bob','Zotti','Knut','Lilo']];
const WI=['Huch!','Mampf!','Lecker!','Hui!','Uff!'],WF=['Platsch!','Pudding!'],WS=['Ich bin satt!','Pappsatt!'];
let bbs=[],bi=0,G=null,mode='main',zone='menu',paused=false,speed=1,sel=0,ptc=[],bub=[],sh=0,btns=[],mbs=[],mbi=0,hintT=0,tick=0,cfg={cpu:1,lvl:1,map:0},last=0,acc=0,held={},enterT=0,enterF=false,drag=null;
const ov=$('#ov'),bar=$('#bar');
function chat(w,arr,p){if(bub.length>=3||rnd()>p)return;const s=arr[(rnd()*arr.length)|0];ctx.font='bold 13px system-ui,sans-serif';bub.push({x:w.x,y:w.y-12,t:0,s,w:ctx.measureText(s).width})}
function say(t){const h=$('#hint');h.textContent=t;h.classList.add('on');hintT=Date.now()+5500}
const MAPN=['Zufall','Hügel','Tal','Berg','Inseln','Burgen'];
function genMap(kind){T.fill(0);const hh=new Array(W).fill(null);const p1=rnd()*6.28,p2=rnd()*6.28,a1=12+rnd()*10;
 for(let x=0;x<W;x++){let h;
  if(kind===1)h=100+Math.sin(x/38+p1)*a1+Math.sin(x/15+p2)*6;
  else if(kind===2)h=125-62*Math.pow((x-160)/160,2)+Math.sin(x/21+p1)*5;
  else if(kind===3)h=126-74*Math.exp(-Math.pow((x-160)/52,2))+Math.sin(x/17+p2)*4;
  else if(kind===4){const s=(x>=8&&x<=98)||(x>=124&&x<=196)||(x>=222&&x<=312);h=s?96+Math.sin(x/26+p1)*12:null}
  else{h=x<120||x>199?104:136;if(x>=148&&x<=171)h=84}
  hh[x]=h===null?null:Math.round(Math.max(40,Math.min(PUD-8,h)))}
 for(let x=0;x<W;x++){if(hh[x]===null)continue;for(let y=hh[x];y<PUD-1;y++)T[y*W+x]=1}
 if(kind===5){for(let y=84;y<136;y++)for(let x=148;x<=171;x++)T[y*W+x]=(y>=84)?3:T[y*W+x];
  for(let t=0;t<2;t++){const bx=t?262:46;for(let y=80;y<104;y++){for(let x=bx-4;x<=bx+4;x++)if(x<bx-1||x>bx+1||y<86)T[y*W+x]=3}}}
 paintAll()}
function surf(x){for(let y=0;y<PUD;y++)if(T[y*W+x])return y-1;return -1}
function newGame(){const kind=cfg.map===0?1+Math.floor(rnd()*5):cfg.map;genMap(kind);setTheme(Math.floor(rnd()*6));
 const ws=[[],[]],slots=[[22,56,90,70],[234,266,298,250]];
 for(let t=0;t<2;t++){let k=0;for(let i=0;i<3;i++){let x=slots[t][i]+Math.floor(rnd()*7-3);if(kind===5&&Math.abs(x-(t?262:46))<=6)x+=t?-12:12;let y=surf(x);for(let d=0;y<0&&d<40;d++){x+=t?-3:3;y=surf(x)}if(y<0)y=60;
  ws[t].push({t,n:NAMES[t][i],x,y,ap:100,st:'stand',dir:t?-1:1,vx:0,vy:0,fx:x,fy:y,fd:0,t0:0})}}
 G={ws,team:1,cur:0,next:[0,0],phase:'aim',st:0,wind:0,ammo:[[99,3,4],[99,3,4]],ang:[55,125],pow:[62,62],wp:[0,0],proj:[],over:null,turns:0,kind,cpuT:0,cpuPlan:null,winner:-1};
 ptc=[];bub=[];sh=0;tick=0;paused=false;speed=1;mode='play';zone='play';ov.style.display='none';pushTrap();mkBar();nextTurn(true)}
function alive(t){return G.ws[t].filter(w=>w.st!=='out')}
function cur(){return G.ws[G.team][G.cur]}
function isCpu(t){return cfg.cpu===2||(cfg.cpu===1&&t===1)}
function nextTurn(first){G.team=first?0:1-G.team;const L=G.ws[G.team];for(let k=0;k<L.length;k++){const i=(G.next[G.team]+k)%L.length;if(L[i].st!=='out'){G.cur=i;G.next[G.team]=i+1;break}}
 G.wind=Math.round(rnd()*10-5);G.phase='aim';G.st=0;G.cpuT=0;G.cpuPlan=null;G.turns++;SFX.turn();hud();
 const w=cur();say((isCpu(G.team)?'Computer ('+TEAMN[G.team]+')':'Team '+TEAMN[G.team])+': '+w.n+' ist dran'+(first?' · OK wirft, Zurück öffnet die untere Leiste (Torte wählen)':''));updBar()}
function hud(){if(!G)return;const w=cur();$('#ht').innerHTML='<span style="color:'+TCOL[G.team]+'">●</span> <b>'+w.n+'</b> · Team '+TEAMN[G.team];
 const wd=G.wind===0?'windstill':(G.wind<0?'◀ ':'')+'Wind '+Math.abs(G.wind)+(G.wind>0?' ▶':'');
 $('#hs').innerHTML='Rot '+alive(0).length+' : '+alive(1).length+' Blau · '+wd+' · Winkel <b>'+Math.round(G.ang[G.team])+'°</b> Kraft <b>'+Math.round(G.pow[G.team])+'</b>'}
function launch(){return{x:cur().x,y:cur().y-9}}
function vel(ang,pow){const a=ang*Math.PI/180;return{vx:Math.cos(a)*pow*.052,vy:-Math.sin(a)*pow*.052}}
function advance(p,list,shooter){p.age=(p.age||0)+1;p.vx+=G.wind*.003;p.vy+=.08;const sp=Math.max(Math.abs(p.vx),Math.abs(p.vy)),n=Math.max(1,Math.ceil(sp/.7));let lxp=p.x,lyp=p.y;
 for(let i=0;i<n;i++){p.x+=p.vx/n;p.y+=p.vy/n;if(p.x<-30||p.x>W+30||p.y>H+10)return{gone:1};const ix=Math.round(p.x),iy=Math.round(p.y);
  if(solP(ix,iy))return{x:lxp,y:lyp};
  for(const w of list){if(w.st==='out'||(w===shooter&&p.age<10))continue;if(Math.abs(ix-w.x)<=3&&iy>=w.y-9&&iy<=w.y)return{x:ix,y:iy,hit:w}}
  lxp=p.x;lyp=p.y}
 return null}
function fire(){if(!G||G.phase!=='aim')return false;const t=G.team,k=G.wp[t];if(!(G.ammo[t][k]>0)){SFX.no();say('Davon ist nichts mehr da.');return false}
 const v=vel(G.ang[t],G.pow[t]),o=launch();G.proj.push({x:o.x,y:o.y,vx:v.vx,vy:v.vy,k:WEAP[k].k,age:0,sp:0,sh:cur()});if(k>0)G.ammo[t][k]--;G.phase='shot';G.st=0;SFX.fire();updBar();return true}
function blast(bx,by,r,dmg){bx=Math.round(bx);by=Math.round(by);for(let y=Math.max(0,by-r);y<=Math.min(PUD-1,by+r);y++)for(let x=Math.max(0,bx-r);x<=Math.min(W-1,bx+r);x++){if((x-bx)*(x-bx)+(y-by)*(y-by)<=r*r&&T[y*W+x]){T[y*W+x]=0;mark(x,y)}}
 sh=Math.min(8,2+r/3);r>=9?SFX.splat():SFX.mini();const n=10+r*2;for(let i=0;i<n;i++){const a=rnd()*6.283,sp=.4+rnd()*(1+r/9);ptc.push({x:bx,y:by,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp-.5,l:18+(rnd()*14|0),c:['#ffffff','#fff1c8','#ffc6e0','#ffe27a'][i%4]})}
 for(const t of G.ws)for(const w of t){if(w.st==='out')continue;const dx=w.x-bx,dy=w.y-4-by,d=Math.sqrt(dx*dx+dy*dy);if(d<=r+7){const f=1-d/(r+7);const dm=Math.round(dmg*Math.max(.25,f));w.ap-=dm;chat(w,WI,.8);
   w.st='fly';w.fx=w.x;w.fy=w.y;w.vx=(Math.abs(dx)<1?(rnd()<.5?1:-1):dx/(d||1))*(.8+f*1.6);w.vy=-1.2-f*1.8;w.fd=0;
   if(w.ap<=0)goOut(w,true)}}}
function goOut(w,satt){w.ap=0;w.st='out';w.t0=0;chat(w,satt?WS:WF,1);for(let i=0;i<10;i++)ptc.push({x:w.x,y:w.y-5,vx:(rnd()-.5)*1.6,vy:-rnd()*1.6,l:24,c:satt?'#ffffff':'#ffd45a'})}
function actW(w){if(w.st==='out'){w.t0++;return}
 if(w.y>=PUD-1){goOut(w,false);SFX.plop();return}
 if(w.st==='stand'){if(!sol(w.x,w.y+1)){let f=false;for(let j=1;j<=3;j++)if(sol(w.x,w.y+1+j)){w.y+=j;f=true;break}if(!f){w.st='fall';w.fd=0}}return}
 if(w.st==='fall'){for(let i=0;i<2;i++){if(sol(w.x,w.y+1)){if(w.fd>44){const dm=Math.round((w.fd-44)*.7);w.ap-=dm;chat(w,['Plumps!','Aua?'],.9);if(w.ap<=0){goOut(w,false);return}}w.fd=0;w.st='stand';return}w.y++;w.fd++;if(w.y>=PUD-1){goOut(w,false);SFX.plop();return}}return}
 if(w.st==='fly'){w.vy=Math.min(5,w.vy+.13);let nx=w.fx+w.vx;if(!colFree(Math.round(nx),Math.round(w.fy))){w.vx=-w.vx*.5;nx=w.fx}w.fx=nx;const xi=Math.round(nx);let ny=w.fy+w.vy;
  if(w.vy<0){if(sol(xi,Math.round(ny)-8)){w.vy=0;ny=w.fy}}
  else{const y0=Math.round(w.fy),y1=Math.round(ny);for(let yy=y0+1;yy<=y1+1;yy++){if(sol(xi,yy)){w.fy=yy-1;w.x=xi;w.y=yy-1;w.st='stand';w.fd=0;return}}}
  w.fy=ny;w.x=xi;w.y=Math.round(ny);if(w.y>=PUD-1){goOut(w,false);SFX.plop()}}}
function settled(){for(const t of G.ws)for(const w of t)if(w.st==='fly'||w.st==='fall')return false;return true}
function step(){if(!G||G.over)return;tick++;
 for(const t of G.ws)for(const w of t)actW(w);
 const all=G.ws[0].concat(G.ws[1]);
 for(const p of G.proj.slice()){const r=advance(p,all,p.sh);
  if(r&&r.gone){G.proj.splice(G.proj.indexOf(p),1);continue}
  if(r){G.proj.splice(G.proj.indexOf(p),1);const k=p.k==='pie'?WEAP[0]:p.k==='big'?WEAP[1]:{r:6,d:24};blast(r.x,r.y,k.r,k.d);continue}
  if(p.k==='conf'&&!p.sp&&p.vy>0){p.sp=1;G.proj.splice(G.proj.indexOf(p),1);for(const o of[-1,0,1])G.proj.push({x:p.x,y:p.y,vx:p.vx+o*.9,vy:p.vy,k:'mini',age:20,sp:1,sh:p.sh});SFX.mini()}
  if(tick%2===0&&p.k!=='mini')ptc.push({x:p.x,y:p.y,vx:0,vy:0,l:7,c:p.k==='big'?'#ffd0e8':'#fff'})}
 fx();
 if(G.phase==='aim'){if(isCpu(G.team))cpuStep()}
 else if(G.phase==='shot'){G.st++;if(!G.proj.length){G.phase='settle';G.st=0}}
 else if(G.phase==='settle'){if(settled()){G.st++;if(G.st>26)endTurn()}else G.st=0}
 hud()}
function endTurn(){const a=alive(0).length,b=alive(1).length;
 if(!a||!b){G.over=1;G.winner=a?0:(b?1:-1);zone='menu';SFX.win();for(let i=0;i<80;i++)ptc.push({x:rnd()*W,y:-4-rnd()*30,vx:(rnd()-.5)*.8,vy:.3+rnd()*.9,l:120,c:['#ff5a5a','#ffd45a','#5ad2ff','#9be37a','#ff8ae6','#fff'][i%6]});
  const t=G.winner<0?'Unentschieden!':'Team '+TEAMN[G.winner]+' gewinnt!';showOv('🎂 '+t,G.winner<0?'Beide sind pappsatt.':(cfg.cpu?(G.winner===0?'Du hast den Computer satt gemacht.':'Der Computer war diesmal besser.'):'Glückwunsch! Der andere Wichtel-Trupp ist pappsatt.'),[['▶ Nochmal',newGame],['☰ Menü',mainMenu],['🚪 Beenden',quit]]);return}
 nextTurn(false)}
function fx(){for(const p of ptc){p.x+=p.vx;p.y+=p.vy;p.vy+=.07;p.l--}ptc=ptc.filter(p=>p.l>0);for(const b of bub)b.t++;bub=bub.filter(b=>b.t<46);sh*=.82}
function trace(o,ang,pow,list,shooter){const v=vel(ang,pow),p={x:o.x,y:o.y,vx:v.vx,vy:v.vy,age:0};for(let i=0;i<260;i++){const r=advance(p,list,shooter);if(r)return r.gone?{gone:1}:r}return{gone:1}}
function cpuStep(){const t=G.team,w=cur();
 if(!G.cpuPlan){G.cpuT++;if(G.cpuT<28)return;const foes=alive(1-t),mine=alive(t),o=launch(),all=G.ws[0].concat(G.ws[1]);let best=null;
  const target=foes[Math.floor(rnd()*foes.length)];const tc={x:target.x,y:target.y-4};
  for(let a=15;a<=165;a+=3)for(let pw=24;pw<=100;pw+=3){const r=trace(o,a,pw,all,w);if(r.gone)continue;let c=Math.hypot(r.x-tc.x,r.y-tc.y);
   for(const m of mine){const d=Math.hypot(r.x-m.x,r.y-(m.y-4));if(d<16)c+=(16-d)*6}
   if(!best||c<best.c)best={c,a,pw}}
  if(!best)best={a:G.ang[t],pw:G.pow[t],c:0};
  const e=[[9,14],[4,7],[1.2,2.5]][cfg.lvl];const ba=best.a+(rnd()*2-1)*e[0],bp=Math.max(15,Math.min(100,best.pw+(rnd()*2-1)*e[1]));
  let k=0;const ch=rnd();if(G.ammo[t][1]>0&&best.c<10&&ch<[.3,.5,.7][cfg.lvl])k=1;else if(G.ammo[t][2]>0&&ch>.85)k=2;
  G.wp[t]=k;G.cpuPlan={a:ba,p:bp,w:0};updBar();return}
 const pl=G.cpuPlan;let da=pl.a-G.ang[t],dp=pl.p-G.pow[t];const sa=2.4,sp=2.4;G.ang[t]+=Math.max(-sa,Math.min(sa,da));G.pow[t]+=Math.max(-sp,Math.min(sp,dp));
 if(Math.abs(da)<=sa&&Math.abs(dp)<=sp){pl.w++;if(pl.w>14)fire()}}
function mkBar(){bar.innerHTML='';btns=[];
 WEAP.forEach((w,i)=>{const b=el('button');b.innerHTML='<i>'+w.e+'</i><b>'+w.n+'</b><u></u>';b.onclick=()=>{ui();if(G&&G.phase==='aim'&&!isCpu(G.team)){G.wp[G.team]=i;updBar();SFX.sel();if(zone==='bar')leaveBar()}};bar.append(b);btns.push(b)});
 bar.append(el('span','sep'));
 const mk=(e,n,f,c)=>{const b=el('button',c);b.innerHTML='<i>'+e+'</i><b>'+n+'</b>';b.onclick=()=>{ui();f()};bar.append(b)};
 mk('💥','Feuer!',()=>{if(G&&!isCpu(G.team))fire()},'go');mk('⏸','Pause',pauseMenu);mk('☰','Menü',mainMenu);bbs=[...bar.querySelectorAll('button')];fit();updBar()}
function updBar(){if(!G)return;const t=G.team;btns.forEach((b,i)=>{b.classList.toggle('sel',G.wp[t]===i);const n=G.ammo[t][i];b.classList.toggle('off',!(n>0));b.querySelector('u').textContent=i===0?'∞':n})}
function barFocus(i){bi=Math.max(0,Math.min(bbs.length-1,i));bbs.forEach((b,k)=>b.classList.toggle('f',zone==='bar'&&k===bi))}
function enterBar(){if(!bbs.length||!G||G.over)return;zone='bar';held={};barFocus(G.phase==='aim'&&!isCpu(G.team)?G.wp[G.team]:3);say('Untere Leiste: Links/Rechts wählen, OK bestätigt, Zurück geht zurück zum Spiel')}
function leaveBar(){zone='play';barFocus(0);bbs.forEach(b=>b.classList.remove('f'))}
let trap=0,bk=0,quitting=0;
function quit(){quitting=1;if(trap)history.back();else closeGame()}
function pushTrap(){if(trap)return;try{history.pushState({td:1},'');trap=1}catch(e){}}
function closeGame(){try{if(window.parent!==window){window.parent.history.back();return}}catch(e){}if(history.length>1)history.back();else location.href='/ui/'}
function resume(){ov.style.display='none';zone='play';paused=false;leaveBar()}
addEventListener('popstate',()=>{if(!trap)return;trap=0;
 if(quitting){closeGame();return}
 if(mode==='play'&&G){pushTrap();if(Date.now()-bk<350)return;
  if(zone==='menu'){if(paused)resume();else if(G.over)mainMenu()}else if(zone==='bar')leaveBar();else enterBar()}
 else closeGame()});
function ui(){if(AC&&AC.state==='suspended')try{AC.resume()}catch(e){}}
function focusMb(i){mbs.forEach(x=>x.classList.remove('f'));mbi=Math.max(0,Math.min(mbs.length-1,i));if(mbs[mbi]){const b=mbs[mbi];b.classList.add('f');const r=b.getBoundingClientRect(),o=ov.getBoundingClientRect();if(r.top<o.top)ov.scrollTop-=o.top-r.top+8;else if(r.bottom>o.bottom)ov.scrollTop+=r.bottom-o.bottom+8}}
function showOv(title,msg,items,focusIdx){ov.innerHTML='';const h=el('h1');h.textContent=title;ov.append(h);
 if(msg){const p=el('p');p.textContent=msg;ov.append(p)}
 const row=el('div','row');for(const it of items){const b=el('button','mb');b.textContent=it[0];b.onclick=()=>{ui();it[1]()};row.append(b)}ov.append(row);
 ov.style.display='flex';zone='menu';mbs=[...ov.querySelectorAll('.mb')];focusMb(focusIdx||0)}
const LVN=['Leicht','Mittel','Schwer'];
function mainMenu(){mode='main';paused=false;if(G&&!G.over)G.over=1;G=null;bar.innerHTML='';btns=[];$('#ht').textContent='Torten-Duell';$('#hs').textContent='';
 showOv('🎂 Torten-Duell','Zwei Wichtel-Trupps werfen abwechselnd Torten. Wer getroffen wird, verliert Appetit. Ist der Appetit weg, ist der Wichtel satt. Sind alle satt, hat der Trupp verloren. Fernbedienung: Links/Rechts Winkel, Hoch/Runter Kraft, OK wirft. Die Zurück-Taste öffnet die untere Leiste (Torte wählen, Pause). Touch: vom Wichtel wegziehen und loslassen.',
  [['Gegen Computer: '+LVN[cfg.lvl],()=>{cfg.cpu=1;newGame()}],['Zu zweit (abwechselnd)',()=>{cfg.cpu=0;newGame()}],['Schwierigkeit: '+LVN[cfg.lvl],()=>{cfg.lvl=(cfg.lvl+1)%3;mainMenu()}],['Karte: '+MAPN[cfg.map],()=>{cfg.map=(cfg.map+1)%MAPN.length;mainMenu()}],['Zielhilfe: '+(aid?'an':'aus'),()=>{aid=!aid;save();mainMenu()}],['Ton: '+(snd?'an':'aus'),()=>{snd=!snd;save();mainMenu()}],['🚪 Beenden',quit]])}
function pauseMenu(){if(!G||G.over||zone==='menu')return;bbs.forEach(b=>b.classList.remove('f'));paused=true;showOv('Pause','',[['▶ Weiter',resume],['🔄 Neue Karte',newGame],['☰ Hauptmenü',mainMenu],['Zielhilfe: '+(aid?'an':'aus'),()=>{aid=!aid;save();pauseMenu()}],['🚪 Beenden',quit]])}
function navMenu(dir){if(!mbs.length)return;const cur_=mbs[mbi].getBoundingClientRect(),cxm=cur_.left+cur_.width/2,cym=cur_.top+cur_.height/2;let best=-1,bd=1e9;
 mbs.forEach((b,i)=>{if(i===mbi)return;const r=b.getBoundingClientRect(),x=r.left+r.width/2-cxm,y=r.top+r.height/2-cym;let pr,pe;
  if(dir==='ArrowRight'){pr=x;pe=Math.abs(y)}else if(dir==='ArrowLeft'){pr=-x;pe=Math.abs(y)}else if(dir==='ArrowDown'){pr=y;pe=Math.abs(x)}else{pr=-y;pe=Math.abs(x)}
  if(pr<=2)return;const d=pr+pe*2.2;if(d<bd){bd=d;best=i}});
 if(best>=0)focusMb(best)}
function myTurn(){return G&&!G.over&&G.phase==='aim'&&!isCpu(G.team)&&zone==='play'&&!paused}
function cycleW(d){if(!myTurn())return;const t=G.team;let k=G.wp[t];for(let i=0;i<3;i++){k=(k+d+3)%3;if(G.ammo[t][k]>0)break}G.wp[t]=k;updBar();SFX.sel();say(WEAP[k].n)}
addEventListener('keydown',e=>{if(e.ctrlKey||e.altKey||e.metaKey)return;const k=e.key;ui();let used=true;if(k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack')bk=Date.now();
 if(zone==='menu'){
  if(k.startsWith('Arrow'))navMenu(k);
  else if(k==='Enter'||k===' ')mbs[mbi]&&mbs[mbi].click();
  else if((k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack')&&paused){resume()}
  else used=false}
 else{
  const BACK=k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack';
  if(zone==='bar'){
   if(k==='ArrowLeft')barFocus(bi-1);else if(k==='ArrowRight')barFocus(bi+1);
   else if(k==='Enter'||k===' '){if(!e.repeat&&bbs[bi])bbs[bi].click()}
   else if(BACK||k==='ArrowUp'){leaveBar()}
   else if(k==='p'){pauseMenu()}
   else used=false}
  else if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','a','d','w','s'].includes(k)){held[k]=held[k]||Date.now()}
  else if(k==='Enter'||k===' '){if(!e.repeat&&myTurn())fire()}
  else if(BACK){enterBar()}
  else if(k==='p'){pauseMenu()}
  else if(/^[1-3]$/.test(k)){if(myTurn()&&G.ammo[G.team][+k-1]>0){G.wp[G.team]=+k-1;updBar();SFX.sel()}}
  else if(k==='PageDown'||k==='ChannelDown'||k==='MediaTrackNext'||k===']'){cycleW(1)}
  else if(k==='PageUp'||k==='ChannelUp'||k==='MediaTrackPrevious'||k==='['){cycleW(-1)}
  else if(k==='f'||k==='MediaFastForward'){speed=speed===1?2:speed===2?3:1;say('Tempo ×'+speed)}
  else used=false}
 if(used){e.preventDefault();e.stopPropagation()}},true);
addEventListener('keyup',e=>{delete held[e.key]},true);
function toLog(e){const r=cv.getBoundingClientRect();return[(e.clientX-r.left)/r.width*W,(e.clientY-r.top)/r.height*H]}
function aimTo(x,y){const w=cur(),o=launch(),dx=o.x-x,dy=o.y-y;let a=Math.atan2(-dy,dx)*180/Math.PI;a=Math.max(0,Math.min(180,a));G.ang[G.team]=a;G.pow[G.team]=Math.max(10,Math.min(100,Math.hypot(dx,dy)*1.25));hud()}
cv.addEventListener('pointerdown',e=>{ui();if(!myTurn())return;const[x,y]=toLog(e),w=cur();cx=x;cy=y;if(Math.hypot(x-w.x,y-(w.y-5))<=22){drag={};try{cv.setPointerCapture(e.pointerId)}catch(_){}}else{aimTo(2*w.x-x,2*w.y-y-10);drag=null}e.preventDefault()});
cv.addEventListener('pointermove',e=>{const[x,y]=toLog(e);cx=x;cy=y;if(drag&&myTurn()){const w=cur();aimTo(x,y)}});
cv.addEventListener('pointerup',e=>{if(drag){const w=cur(),[x,y]=toLog(e);drag=null;if(myTurn()&&Math.hypot(x-w.x,y-w.y)>12){aimTo(x,y);fire()}}});
function moveKeys(dt){if(!myTurn())return;const now=Date.now();const sp=(k,s)=>{const t=held[k];if(!t)return 0;return(now-t>450?s*3:s)};
 const t=G.team,da=sp('ArrowLeft',34)+sp('a',34)-sp('ArrowRight',34)-sp('d',34),dp=sp('ArrowUp',34)+sp('w',34)-sp('ArrowDown',34)-sp('s',34);
 if(da)G.ang[t]=Math.max(0,Math.min(180,G.ang[t]+da*dt/1000));if(dp)G.pow[t]=Math.max(10,Math.min(100,G.pow[t]+dp*dt/1000))}
function sprFor(w){const a=SPR[w.t][w.st==='stand'?'stand':'air'];return a[w.dir<0?0:1]}
function render(t){ctx.imageSmoothingEnabled=false;drawBg(t||0);if(!G)return;
 flush();lx.clearRect(0,0,W,H);lx.drawImage(tcv,0,0);
 lx.fillStyle='#ffd45a';for(let x=0;x<W;x++){const y=PUD+Math.round(Math.sin(x/9+t/260)*1.2);lx.fillRect(x,y,1,H-y)}lx.fillStyle='#fff3b0';for(let x=0;x<W;x+=7)lx.fillRect(x+((t/90)|0)%7,PUD+1,2,1);
 const act=G.over?null:cur();
 for(const tm of G.ws)for(const w of tm){if(w.st==='out'){if(w.t0<30&&w.y<PUD-2){lx.globalAlpha=1-w.t0/30;lx.drawImage(SPR[w.t].air[w.dir<0?0:1],w.x-4,w.y-9-w.t0*.3);lx.globalAlpha=1}continue}
  let hop=0;if(w===act&&G.phase==='aim')hop=Math.abs(Math.sin(t/160))*2;lx.drawImage(sprFor(w),w.x-4,Math.round(w.y-9-hop));
  const bw=12,bx=w.x-6,by=w.y-14;lx.fillStyle='rgba(0,0,0,.55)';lx.fillRect(bx-1,by-1,bw+2,4);lx.fillStyle=w.ap>50?'#7be07b':w.ap>25?'#ffd45a':'#ff6b6b';lx.fillRect(bx,by,Math.max(1,Math.round(bw*w.ap/100)),2);
  lx.fillStyle=TCOL[w.t];lx.fillRect(w.x-1,by-3,2,1)}
 for(const p of G.proj){lx.fillStyle=p.k==='big'?'#ff8ac4':p.k==='mini'?'#fff1c8':'#ffffff';const r=p.k==='big'?3:p.k==='mini'?1:2;lx.fillRect(Math.round(p.x)-r,Math.round(p.y)-r,r*2+1,r*2+1);lx.fillStyle='#ff5a8a';lx.fillRect(Math.round(p.x),Math.round(p.y)-r-1,1,1)}
 for(const p of ptc){lx.fillStyle=p.c;lx.fillRect(Math.round(p.x),Math.round(p.y),1,1)}
 if(sh>.6){ctx.save();ctx.translate((rnd()-.5)*sh,(rnd()-.5)*sh)}
 ctx.drawImage(lcv,0,0,640,320);if(sh>.6)ctx.restore();
 ctx.font='bold 13px system-ui,sans-serif';ctx.textAlign='center';
 for(const b of bub){const bw=b.w+12,X=Math.max(bw/2,Math.min(640-bw/2,b.x*2)),Y=Math.max(20,b.y*2-b.t*.5);ctx.fillStyle='rgba(255,255,255,.96)';ctx.fillRect(X-bw/2,Y-18,bw,18);ctx.fillRect(X-3,Y,6,4);ctx.fillStyle='#2a1c40';ctx.fillText(b.s,X,Y-5)}
 if(act&&G.phase==='aim'&&zone!=='menu'){const t0=G.team,o=launch(),a=G.ang[t0]*Math.PI/180,pw=G.pow[t0],L=(12+pw*.3)*2,X=o.x*2,Y=o.y*2;
  ctx.strokeStyle=TCOL[t0];ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(X+Math.cos(a)*14,Y-Math.sin(a)*14);ctx.lineTo(X+Math.cos(a)*L,Y-Math.sin(a)*L);ctx.stroke();
  ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(X+Math.cos(a)*L,Y-Math.sin(a)*L,4,0,6.2832);ctx.fill();cx=o.x+Math.cos(a)*40;cy=o.y-Math.sin(a)*40;
  if(aid&&!isCpu(t0)){const v=vel(G.ang[t0],pw),p={x:o.x,y:o.y,vx:v.vx,vy:v.vy,age:0};ctx.fillStyle='rgba(255,255,255,.7)';for(let i=0;i<44;i++){const r=advance(p,[],null);if(r)break;if(i%4===3)ctx.fillRect(Math.round(p.x*2)-1,Math.round(p.y*2)-1,3,3)}}
  ctx.fillStyle='#fff';ctx.font='bold 14px system-ui';ctx.fillText(Math.round(G.ang[t0])+'°  '+Math.round(pw)+'%',Math.max(50,Math.min(590,X)),Math.max(16,Y-60))}
 ctx.fillStyle='rgba(18,13,31,.6)';ctx.fillRect(4,4,120,20);ctx.fillStyle='#fff';ctx.font='bold 13px system-ui';ctx.textAlign='center';const wd=G.wind;ctx.fillText(wd===0?'Windstille':'Wind '+(wd<0?'◀'.repeat(-wd):'▶'.repeat(wd)),64,19);
 if(paused&&zone!=='menu'){ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(0,0,640,320)}}
function frame(t){const dt=Math.min(100,t-last);last=t;moveKeys(dt);
 if(G&&!paused&&zone!=='menu'||(G&&G.over)){acc+=dt*speed;while(acc>=33.3){acc-=33.3;if(G.over)fx();else step()}}else acc=0;
 if(hintT&&Date.now()>hintT){$('#hint').classList.remove('on');hintT=0}
 render(t);requestAnimationFrame(frame)}
function fit(){const st=$('#stage'),w=st.clientWidth,h=st.clientHeight;let cw=w,ch=w/2;if(ch>h){ch=h;cw=h*2}cv.style.width=Math.floor(cw)+'px';cv.style.height=Math.floor(ch)+'px'}
addEventListener('resize',fit);fit();try{new ResizeObserver(fit).observe($('#stage'))}catch(e){}
window.TG={seed:s=>{seed=s},cfg,start:(cpu,lvl,map)=>{cfg.cpu=cpu;cfg.lvl=lvl;cfg.map=map;newGame()},step:n=>{for(let i=0;i<(n||1);i++)step()},st:()=>G&&({phase:G.phase,team:G.team,cur:G.cur,over:G.over,winner:G.winner,wind:G.wind,ang:G.ang.slice(),pow:G.pow.slice(),ammo:G.ammo,proj:G.proj.length,turns:G.turns,alive:[alive(0).length,alive(1).length],zone,tick,kind:G.kind}),ws:()=>G.ws.map(t=>t.map(w=>({x:w.x,y:w.y,st:w.st,ap:w.ap}))),aim:(a,p,k)=>{G.ang[G.team]=a;G.pow[G.team]=p;if(k!==undefined)G.wp[G.team]=k},fire,cur:()=>({x:cur().x,y:cur().y}),terr:()=>T.reduce((s,v)=>s+(v?1:0),0)};
setTheme(0);mainMenu();requestAnimationFrame(frame);
</script></body></html>
"""
