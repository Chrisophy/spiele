# -*- coding: utf-8 -*-
# Entertain Master
# zusatzmetall
# 2026.11.23

EXT_ID = 'hanfeld'
EXT_NAME = 'Entertain Master'
EXT_DESCRIPTION = "📺 Entertain Master: Endloses Open-World-Spiel in Rheinhanfen. Ausgedachte Codes besorgen, Antennen und Kabel heimlich verlegen, Kunden mit allen Sendern versorgen, Filme scrapen und tauschen, Kino und Autokino kaufen, in Hollyhanf Videos drehen und am Ende den Fernsehturm übernehmen. Dazu Wohnung, Camping, Freibad, Rodelbahn und viel Quatsch. Fernbedienung und Touch. Alles nur Fiktion!"
EXT_LINKS = [('Entertain Master', 'index')]
EXT_SETTINGS = []


def register(api):
    api.route('index', lambda req: PAGE)
    api.widget('Entertain Master', lambda: {'text': 'Entertain Master', 'sub': 'Open-World in Rheinhanfen', 'icon': '📺'}, ttl=3600, icon='📺')


PAGE = r"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#000000">
<title>Entertain Master – Rheinhanfen</title>
<style>
:root{--bg:#0c100d;--p:#161c17;--p2:#1e2620;--ln:#2f3b31;--tx:#ece6d6;--mu:#9aa593;--am:#f2b441;--gr:#6bcf63;--rd:#e5604d;--bl:#6fb3e0}
*{box-sizing:border-box}
html,body{height:100%;margin:0;overflow:hidden;background:#000;color:var(--tx);font-family:"Trebuchet MS","Segoe UI",Roboto,Arial,sans-serif;-webkit-user-select:none;user-select:none}
#stage{position:fixed;left:0;top:0;width:100%;height:100%;background:#000;overflow:hidden}
#cv{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:100%;height:100%;background:#0c100d;image-rendering:pixelated}
#hud{position:absolute;left:1.4vw;right:calc(76px + 1vw);top:max(1.6vh,.5rem);display:flex;align-items:stretch;padding:.28rem .3rem;pointer-events:none;background:linear-gradient(180deg,rgba(20,27,22,.95),rgba(11,15,12,.92));border:1px solid #445246;border-radius:.85rem;box-shadow:0 .3rem 1rem rgba(0,0,0,.5)}
.chip{flex:1;padding:.05rem .6rem;min-width:0;border-left:1px solid rgba(255,255,255,.09);display:flex;flex-direction:column;justify-content:center}
.chip:first-child{border-left:none}
.chip small{display:block;font-size:.5rem;letter-spacing:.08em;color:var(--mu);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chip b{display:block;font-size:.84rem;line-height:1.3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chip .sub{display:block;font-size:.52rem;line-height:1.35;color:var(--mu);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chip.h{flex:1.25}.chip.t{flex:.7}
.chip.wb{flex:3.4;flex-direction:row;align-items:center;gap:.5rem}
.wm{flex:1;min-width:0}
.wm small{font-size:.48rem}
.wm .hb{height:.4rem;margin-top:.1rem}
.wm em{display:block;font-style:normal;font-size:.56rem;line-height:1.4;margin-top:.04rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.blink{animation:hbl 1s steps(2) infinite}@keyframes hbl{50%{opacity:.35}}
.am{color:var(--am)}.gr{color:var(--gr)}.rd{color:var(--rd)}.bl{color:var(--bl)}.mu{color:var(--mu)}
.hb{height:.55rem;background:#0b0f0c;border-radius:.4rem;margin-top:.25rem;overflow:hidden;border:1px solid var(--ln)}
.hb i{display:block;height:100%}
#trk{position:absolute;left:.5rem;bottom:.5rem;max-width:30%;pointer-events:none}
#trk div{background:rgba(12,16,13,.78);border:1px solid var(--ln);border-left:.3rem solid var(--am);border-radius:.4rem;padding:.2rem .5rem;margin-top:.25rem;font-size:.7rem;line-height:1.25}
#trk div.k{border-left-color:var(--rd)}#trk div.b{border-left-color:var(--bl)}
#prompt{position:absolute;left:50%;bottom:7%;transform:translateX(-50%);background:rgba(12,16,13,.85);border:2px solid var(--am);border-radius:.6rem;padding:.3rem .9rem;font-size:.95rem;display:none;white-space:nowrap}
#mm{position:absolute;right:.5rem;bottom:.5rem;width:13rem;height:8.2rem;transition:opacity .3s;border:2px solid var(--ln);border-radius:.4rem;background:#000;pointer-events:none}
#ov{position:absolute;left:0;top:0;right:0;bottom:0;background:rgba(0,0,0,.62);display:none}
#ov.c{background:rgba(0,0,0,.28)}
#ov.c #ovc{left:50%;right:auto;width:31rem;max-width:94%;transform:translateX(-50%);top:auto;bottom:4%;height:auto;max-height:92%}
#ov.c #hint{display:none}
.sitp .btn{margin:.22rem 0;padding:.42rem .9rem}
.sitp .hd{margin-bottom:.35rem}
#trk div.r{border-left-color:var(--gr)}
#ov.t{background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,.2) 40%,rgba(0,0,0,.65))}
#ovc{position:absolute;left:50%;width:69rem;max-width:94%;transform:translateX(-50%);top:6%;bottom:6%;overflow:hidden;background:rgba(14,19,15,.96);border:2px solid var(--ln);border-radius:.8rem;padding:.8rem}
#ov.t #ovc{background:none;border:none}
#hint{position:absolute;left:5%;right:5%;bottom:1.5%;font-size:.7rem;color:var(--mu);text-align:center;display:none}
.btn{display:block;padding:.55rem 1rem;margin:.3rem 0;background:var(--p2);border:1px solid var(--ln);border-radius:.55rem;font-size:1rem;cursor:pointer}
.btn small{display:block;font-size:.7rem;color:var(--mu);margin-top:.1rem}
.btn.off{opacity:.45}
.f{cursor:pointer}
.focus{outline:.2rem solid var(--am);outline-offset:.1rem;background:#2b3523!important;box-shadow:0 0 1.1rem rgba(242,180,65,.45);position:relative;z-index:3}
.title{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.title h1{font-family:Impact,"Arial Black",sans-serif;font-size:4rem;letter-spacing:.12em;margin:0;color:var(--am);text-shadow:0 .2rem 0 #6b4a0e,0 0 2rem rgba(242,180,65,.35)}
.title h1 span{color:var(--gr)}
.title p{margin:.2rem 0 1.2rem;color:#d8d2c0;letter-spacing:.3em;text-transform:uppercase;font-size:.85rem}
.title .menu{width:20rem}
.title .btn{text-align:center;font-size:1.15rem}
.panel{background:var(--p);border:1px solid var(--ln);border-radius:.7rem;padding:.6rem .8rem;min-height:0;overflow:auto}
.panel h3{margin:0;font-size:1.15rem;color:var(--am)}
.panel p{margin:.4rem 0;font-size:.85rem;line-height:1.35}
.tag{display:inline-block;padding:.1rem .5rem;border-radius:.4rem;border:1px solid var(--ln);font-size:.72rem;margin:.1rem .25rem .1rem 0}
.news{font-size:.78rem;margin:.2rem 0;color:#d8cfa8}
.place{max-width:34rem;margin:0 auto;height:100%;overflow:auto;padding:.3rem .5rem .3rem .3rem}
.place h2,.hd h2{margin:.1rem 0;color:var(--am);font-size:1.5rem}
.place .btn.m{border-left:.35rem solid var(--gr)}
.place .btn.d{border-left:.35rem solid var(--am)}
.mk{height:100%;display:flex;flex-direction:column}
.mkh{display:flex;justify-content:space-between;align-items:baseline}
.mkh h2{margin:0;color:var(--am);font-size:1.4rem}
.mrow{display:grid;grid-template-columns:7rem 5.2rem 5.6rem 6rem repeat(3,1fr) repeat(3,1fr);gap:.3rem;align-items:center;margin:.25rem 0}
.mrow.h .num{white-space:nowrap}.mrow .own{padding-right:1rem;font-size:1.2rem;font-weight:bold;color:var(--mu)}.mrow .own.has{color:var(--am)}
.leg{margin-top:.6rem;font-size:.72rem;line-height:1.5;color:var(--mu)}
.mrow.h{font-size:.64rem;color:var(--mu);letter-spacing:.08em}
.mrow .btn{margin:0;padding:.4rem .2rem;text-align:center;font-size:.85rem}
.mrow .btn.b{border-color:#46633f}.mrow .btn.s{border-color:#7a5a24}
.num{text-align:right;font-size:.95rem}
.two{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
.two .panel{display:flex;flex-direction:column}
.two .sc{flex:1;min-height:0;overflow:auto;padding:.3rem .35rem .3rem .3rem;margin:0 -.3rem}
.card{padding:.4rem .7rem;margin:0 0 .4rem;background:var(--p2);border:1px solid var(--ln);border-radius:.5rem;font-size:.82rem;line-height:1.3}
.card b{font-size:.92rem}
.card .rw{color:var(--gr);margin-top:.15rem;font-size:.78rem}
.tg{display:inline-block;font-size:.58rem;letter-spacing:.1em;padding:.05rem .4rem;border-radius:.3rem;margin-right:.4rem;color:#111;font-weight:bold}
.tg.l{background:var(--am)}.tg.b{background:var(--bl)}.tg.k{background:var(--rd)}
.hd{margin-bottom:.4rem}
.prodgrid{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
.prodgrid .btn{text-align:center}
#modal{position:absolute;left:0;top:0;right:0;bottom:0;background:rgba(0,0,0,.72);display:none;align-items:center;justify-content:center;z-index:20}
.mb{width:min(36rem,92%);max-height:90%;overflow:auto;background:#151b16;border:2px solid var(--am);border-radius:.8rem;padding:.9rem 1.1rem;box-shadow:0 0 3rem rgba(0,0,0,.8)}
.mb h2{margin:0 0 .4rem;color:var(--am);font-size:1.3rem}
.mt{font-size:.92rem;line-height:1.4;margin-bottom:.4rem}
.mb ul{margin:.3rem 0 .6rem;padding-left:1.1rem;font-size:.85rem;line-height:1.4}
.mc .btn small{display:inline;margin-left:.6rem}
#toast{position:absolute;left:50%;top:14%;transform:translateX(-50%);background:rgba(42,31,12,.95);border:1px solid var(--am);color:var(--tx);padding:.45rem 1rem;border-radius:.5rem;font-size:.9rem;display:none;z-index:30;max-width:80%;text-align:center}
.big{font-size:1rem;line-height:1.5}
.sum{width:100%}.sum td{padding:.2rem .6rem .2rem 0;font-size:1rem;text-align:left}.sum td+td{text-align:right;font-weight:bold}
.pmenu{max-width:24rem;margin:0 auto}
#tc{position:absolute;left:0;top:0;right:0;bottom:0;z-index:40;pointer-events:none;display:none;-webkit-touch-callout:none}
.touch #tc{display:block}
.touch #trk{bottom:11.8rem}
.tb{position:absolute;pointer-events:auto;touch-action:none;display:flex;align-items:center;justify-content:center;background:rgba(22,28,23,.55);border:2px solid rgba(242,180,65,.55);color:var(--tx);font-weight:bold;border-radius:.8rem;font-size:1.4rem;opacity:.7;-webkit-tap-highlight-color:transparent}
.tb.on{background:rgba(242,180,65,.6);opacity:1}
.tb.d{width:3.5rem;height:3.5rem}
#tUp{left:4.3rem;bottom:7.8rem}#tLf{left:.8rem;bottom:4.3rem}#tRt{left:7.8rem;bottom:4.3rem}#tDn{left:4.3rem;bottom:.8rem}
#tOk{right:.8rem;bottom:11.8rem;width:4.8rem;height:4.8rem;border-radius:50%;font-size:1.3rem}
#tBk{right:6.2rem;bottom:11.8rem;width:3.6rem;height:3.6rem;font-size:.9rem}
#trk{left:1.4vw;bottom:max(1.6vh,.5rem)}#mm{right:1.4vw;bottom:max(1.6vh,.5rem)}
#mm.fade{opacity:.15}
#mm.mmk{width:8.6rem;height:5.45rem}
#mm.mmoff{display:none}
</style>
</head>
<body>
<div id="stage">
<canvas id="cv" width="960" height="540"></canvas>
<div id="hud"></div>
<div id="trk"></div>
<div id="prompt"></div>
<canvas id="mm" width="304" height="192"></canvas>
<div id="ov"><div id="ovc"></div><div id="hint"></div></div>
<div id="tc"><div class="tb d" id="tUp">▲</div><div class="tb d" id="tLf">◀</div><div class="tb d" id="tRt">▶</div><div class="tb d" id="tDn">▼</div><div class="tb" id="tBk">MENÜ</div><div class="tb" id="tOk">OK</div></div>
<div id="modal"></div>
<div id="toast"></div>
</div>

<script>
(function(){
'use strict';
let ZONE=null;let VW=960,MW=118,MH=68;const TS=32,VH=540,DAY_S=3600,FOOT=104;
const VR=[6,24,42,60,74,92,112],HR=[0,14,30,46,62];
const GR=0,RD=1,SW=2,BL=3,WT=4,TR=5,FD=6,DK=7,FN=8,CR=9,BK=10,PG=11,SD=12,SA=13,SH=14,DP=15,LV=16,SN=17,RK=18,CF=19,AS=20,UM=21,LC=22,CY=23,MU=24,IC=25;
const SOL=new Uint8Array(32);[BL,WT,TR,FN,CR,BK,PG,DP,LV,RK,UM,LC,CY,MU].forEach(v=>{SOL[v]=1;});

const rnd=(a,b)=>a+Math.floor(Math.random()*(b-a+1));
const rf=(a,b)=>a+Math.random()*(b-a);
const pick=a=>a[Math.floor(Math.random()*a.length)];
const chance=p=>Math.random()<p;
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
const r5=v=>Math.round(v/5)*5;
const r10=v=>Math.round(v/10)*10;
const eur=n=>Math.round(n).toLocaleString('de-DE')+' €';
let seed=20261121;
function rng(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;}
const ri=(a,b)=>a+Math.floor(rng()*(b-a+1));

let T=new Uint8Array(MW*MH),BLD=[],MKS=[];const POCKETS=[],NOGO=[],SIGNS=[];
function tget(x,y){return(x<0||y<0||x>=MW||y>=MH)?WT:T[y*MW+x];}
function isSolid(x,y){const t=tget(x,y);return SOL[t]===1&&!(t===DP&&ZONE&&ZONE.swim);}
function fillR(x,y,w,h,v){for(let j=y;j<y+h;j++)for(let i=x;i<x+w;i++)if(i>=0&&j>=0&&i<MW&&j<MH)T[j*MW+i]=v;}
const PAL={wohn:['#b5654a','#a85a45','#c9886a','#8f6a5a','#b98f6f'],alt:['#c47f4a','#a35d3c','#d19a62','#8d5238','#bf7b58'],gew:['#7c8590','#6d7782','#8d9aa5','#59636d'],club:['#7a3fa8','#2f6fb5','#b53f8f','#3fb5a8'],villa:['#e2dccb','#d4ccb4','#c9bfa7']};
function addB(x,y,w,h,c,n,k,hh){fillR(x,y,w,h,BL);BLD.push({x:x,y:y,w:w,h:h,c:c,n:n||'',k:k||'house',hh:hh||6});}
function tree(x,y){if(tget(x,y)===GR||tget(x,y)===SW)T[y*MW+x]=TR;}
function lots(b,minW,maxW,minH,maxH){
 const out=[];let y=b.y0+1;
 while(y+minH-1<=b.y1-1){
  let h=ri(minH,maxH);if(y+h-1>b.y1-1)h=b.y1-y;
  let x=b.x0+1;
  while(x+minW-1<=b.x1-1){
   let w=ri(minW,maxW);if(x+w-1>b.x1-1)w=b.x1-x;
   out.push({x:x,y:y,w:w,h:h});x+=w+1;
  }
  y+=h+1;
 }
 return out;
}
function mkm(id,dist,kind,tx,ty,name,col){MKS.push({id:id,dist:dist,kind:kind,x:tx*TS+TS/2,y:ty*TS+TS/2,n:name,col:col});}
function generic(b,pal,minW,maxW,minH,maxH,specials,parkP){
 fillR(b.x0,b.y0,b.x1-b.x0+1,b.y1-b.y0+1,SW);
 const L=lots(b,minW,maxW,minH,maxH);
 const cx=(b.x0+b.x1)/2,cy=(b.y0+b.y1)/2;
 const sorted=L.slice().sort((p,q)=>Math.hypot(p.x+p.w/2-cx,p.y+p.h/2-cy)-Math.hypot(q.x+q.w/2-cx,q.y+q.h/2-cy));
 (specials||[]).forEach((s,i)=>{if(sorted[i]){sorted[i].sp=s;}});
 L.forEach(l=>{
  if(l.sp){
   addB(l.x,l.y,l.w,l.h,l.sp.col,l.sp.name,l.sp.kind||'house',8);
   mkm(l.sp.id,l.sp.dist,l.sp.mk,l.x+Math.floor(l.w/2),l.y+l.h,l.sp.label,l.sp.mc);
  }else if(rng()<(parkP===undefined?.14:parkP)){
   fillR(l.x,l.y,l.w,l.h,GR);POCKETS.push({x:l.x,y:l.y,w:l.w,h:l.h});
   const n=ri(1,2);for(let i=0;i<n;i++)tree(ri(l.x,l.x+l.w-1),ri(l.y,l.y+l.h-1));
  }else addB(l.x,l.y,l.w,l.h,pal[ri(0,pal.length-1)],'','house',ri(4,9));
 });
}
function blockOf(c,r){return{x0:VR[c]+2,x1:VR[c+1]-1,y0:HR[r]+2,y1:HR[r+1]-1};}
function genWorld(){
 T.fill(GR);
 fillR(0,0,5,MH,WT);fillR(5,0,1,MH,SW);
 VR.forEach(v=>fillR(v,0,2,MH,RD));
 HR.forEach(h=>fillR(6,h,MW-6,2,RD));
 for(let r=0;r<4;r++)for(let c=0;c<6;c++){const b=blockOf(c,r);fillR(b.x0,b.y0,b.x1-b.x0+1,b.y1-b.y0+1,SW);}
 let b=blockOf(0,0);
 fillR(10,4,12,8,SW);
 fillR(10,4,12,1,FN);fillR(10,11,12,1,FN);fillR(10,4,1,8,FN);fillR(21,4,1,8,FN);
 fillR(15,11,2,1,SW);
 addB(11,5,5,4,'#e8a63a','HANFBIER','house',8);
 addB(17,5,4,4,'#bfe6e0','HANF-LABOR','glass',6);
 fillR(11,10,2,1,CR);
 [[9,3],[22,3],[9,12],[22,12],[13,12],[18,12]].forEach(t=>tree(t[0],t[1]));
 mkm('hq','hq','hq',16,9,'Imbiss Hanfred Hanfbier','#6bcf63');
 b=blockOf(1,0);
 fillR(b.x0+1,b.y0+1,b.x1-b.x0-1,b.y1-b.y0-1,GR);
 [[28,4],[35,4],[28,9],[35,9]].forEach((v,i)=>addB(v[0],v[1],6,3,PAL.villa[i%3],i===1?'VILLA BLUMENTHAL':'','house',8));
 fillR(27,7,14,2,SW);fillR(27,3,14,1,SW);
 [[27,3],[41,3],[27,12],[41,12],[34,5],[34,10],[34,11]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 mkm('villen','villen','shop',37,7,'Villa Blumenthal','#f2b441');
 b=blockOf(2,0);
 fillR(b.x0+1,b.y0+1,b.x1-b.x0-1,b.y1-b.y0-1,GR);
 addB(46,3,12,3,'#9a6b5a','UNIVERSITÄT','house',8);
 addB(49,9,5,3,'#c9a46a','MENSA','house',6);
 fillR(45,6,14,3,SW);fillR(45,12,14,1,SW);
 [[45,3],[58,3],[45,10],[58,10],[47,10],[56,10],[47,12],[56,12],[46,7],[57,7]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 mkm('uni','uni','shop',51,12,'Mensa-Hinterhof','#f2b441');
 b=blockOf(3,0);
 addB(64,4,8,6,'#2f7a3a','STADION','stadium',10);
 addB(63,11,3,2,'#d08a3a','KIOSK','house',5);
 [[62,3],[73,3],[62,10],[73,10],[67,11],[69,11]].forEach(t=>tree(t[0],t[1]));
 mkm('stadion','stadion','shop',64,13,'Stadionkiosk','#f2b441');
 generic(blockOf(0,1),PAL.wohn,4,7,3,5,null,.16);
 generic(blockOf(1,1),PAL.alt,3,5,3,4,[{id:'altstadt',dist:'altstadt',mk:'shop',label:'Zum goldenen Fass',name:'ZUM GOLDENEN FASS',col:'#d9a23a',mc:'#f2b441'},{id:'willi',dist:'willi',mk:'willi',label:'Chefin Dr. Willi',name:'WILLIS KONTOR',col:'#7a2f2f',mc:'#e5604d'}],.1);
 b=blockOf(2,1);
 fillR(b.x0,b.y0,b.x1-b.x0+1,b.y1-b.y0+1,SW);
 addB(51,21,2,2,'#4da6d8','','fountain',3);
 [[47,18],[48,18],[55,18],[56,18],[47,27],[48,27],[55,27],[56,27]].forEach(t=>{T[t[1]*MW+t[0]]=CR;});
 for(let x=45;x<=58;x+=3){tree(x,17);tree(x,28);}
 for(let y=19;y<=26;y+=3){tree(45,y);tree(58,y);}
 generic(blockOf(3,1),PAL.club,3,5,3,4,[{id:'club',dist:'club',mk:'shop',label:'Club Neon',name:'CLUB NEON',kind:'neon',col:'#b53f8f',mc:'#f2b441'}],.1);
 b=blockOf(0,2);
 fillR(b.x0,b.y0,b.x1-b.x0+1,b.y1-b.y0+1,SW);
 fillR(1,35,5,1,DK);fillR(1,39,5,1,DK);fillR(1,43,5,1,DK);
 [[10,34,4],[15,34,3],[10,38,3],[14,38,4],[19,38,3],[10,42,4],[15,42,2]].forEach(g=>{for(let i=0;i<g[2];i++){T[g[1]*MW+g[0]+i]=CR;T[(g[1]+1)*MW+g[0]+i]=CR;}});
 addB(18,40,5,4,'#6d7782','GROSSHANDEL','house',8);
 mkm('hafen','hafen','shop',20,44,'Hafen-Großhandel','#f2b441');
 generic(blockOf(1,2),PAL.wohn,4,7,3,5,null,.16);
 generic(blockOf(2,2),PAL.gew,5,8,4,6,null,.1);
 b=blockOf(3,2);
 fillR(b.x0+1,b.y0+1,b.x1-b.x0-1,b.y1-b.y0-1,FD);
 addB(66,34,5,3,'#a3402f','LANDGUT','barn',7);
 addB(63,33,2,2,'#c9886a','','house',5);
 [[62,32],[73,32],[62,45],[73,45],[64,38],[70,38]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 mkm('land','land','shop',68,37,'Landgut Hopfenhof','#f2b441');
 genWorld2();
}
let FIRE=null,TRUCK=null,fireT=110,BOLT=null,FIRESM=[],BURNT=[],FWR=[],FWP=[],FWQ=[],FWS=null,HYD=[];
const SPF={
 fb:{x0:10*TS,y0:50*TS,x1:22*TS,y1:60*TS,gy0:53*TS,gy1:57*TS},
 bb:{x0:30*TS,y0:50*TS,x1:38*TS,y1:60*TS},
 bs:{x0:46*TS,y0:50*TS,x1:58*TS,y1:60*TS},
 rad:{x:67.5*TS,y:52.4*TS,R:3*TS}
};
const FPK={rad:{x:9*TS+16,y:6.6*TS,R:3.3*TS},karu:{x:12*TS+16,y:20*TS+16,R:2.4*TS,r:1.7*TS}};
const TEAMC=[['#e5504d','#2e86c1'],['#f1c40f','#27ae60'],['#8e44ad','#ff9a3c'],['#ecf0f1','#2c3e50'],['#16a085','#d35400']];
const BALC=['#ff4d7a','#5ff0ff','#ffd23f','#7bd86a','#b58cff','#ff9a3c'];
let SP=null,MG=null,cityWA=0,cityRid=[1,0,1,1,0,1,0,1],cityRT=12;
function fenceR(x0,y0,x1,y1,gaps){fillR(x0,y0,x1-x0+1,1,FN);fillR(x0,y1,x1-x0+1,1,FN);fillR(x0,y0,1,y1-y0+1,FN);fillR(x1,y0,1,y1-y0+1,FN);(gaps||[]).forEach(g=>{T[g[1]*MW+g[0]]=SW;});}
function genWorld2(){
 fenceR(9,49,22,60,[[15,49],[16,49],[15,60],[16,60]]);fillR(10,50,12,10,GR);
 [[8,48],[23,48],[8,61],[23,61]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 fenceR(29,49,38,60,[[33,49],[34,49]]);
 [27,40].forEach(x=>[52,55,58].forEach(y=>putBK(x,y,[SW])));
 [[26,48],[41,48],[26,61],[41,61]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 fenceR(45,49,58,60,[[47,60],[48,60]]);fillR(46,50,12,10,GR);
 [[44,48],[59,48],[44,61],[59,61]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 fillR(63,49,10,8,GR);
 addB(64,57,8,3,'#e85a9a','','parktor',6);
 [[63,49],[72,49],[63,52],[72,52],[63,55],[72,55]].forEach(t=>tree(t[0],t[1]));
 generic(blockOf(4,0),PAL.wohn,4,7,3,5,null,.16);
 let b=blockOf(4,1);
 fillR(b.x0+1,b.y0+1,b.x1-b.x0-1,b.y1-b.y0-1,GR);
 fillR(b.x0+1,25,b.x1-b.x0-1,1,SW);fillR(80,b.y0+1,1,b.y1-b.y0-1,SW);
 for(let y=b.y0+1;y<b.y1;y++)for(let x=b.x0+1;x<b.x1;x++){const dx=(x-86)/3.4,dy=(y-21)/2.3;if(dx*dx+dy*dy<=1)T[y*MW+x]=WT;}
 [[78,22],[83,27],[88,27],[90,17],[90,23],[82,17],[89,26],[78,28],[84,28]].forEach(t=>tree(t[0],t[1]));
 [[82,24],[88,24],[79,21],[84,18]].forEach(t=>putBK(t[0],t[1],[GR]));
 generic(blockOf(4,2),PAL.alt,3,5,3,4,null,.12);
 addB(78,50,6,4,'#3f8a4a','VEREINSHEIM','house',8);
 mkm('verein','verein','shop',80,54,'Vereinsheim SV Rheinhanfen','#f2b441');
 fillR(86,49,5,5,FD);fillR(86,55,5,5,FD);
 addB(89,49,2,2,'#c97b4a','','house',5);addB(86,58,2,2,'#7a9a5a','','house',5);
 [[77,57],[77,60],[83,59],[84,49],[90,60]].forEach(t=>tree(t[0],t[1]));
 [[80,57],[82,57]].forEach(t=>putBK(t[0],t[1],[SW]));
 genWorld3();
}
function genExtras2(){
 portal('p7',67,60,'parktor','Freizeitpark','Freizeitpark betreten','Du gehst durch das bunte Tor. Es riecht nach Zuckerwatte, Popcorn und Abenteuer!');MKS[MKS.length-1].to='fpark';
 [['spfb',15,48,'Fußballplatz','fb'],['spbb',33,48,'Basketballplatz','bb'],['spbs',47,61,'Baseballfeld','bs']].forEach(q=>{mkm(q[0],'','sk',q[1],q[2],q[3],'#ffb347');const m=MKS[MKS.length-1];m.sk=q[4];m.act=q[3]+': Mitspielen';});
 buedchen('bue3',77,17,'Büdchen am Stadtpark');
 genExtras3();
}

genWorld();
function putBK(x,y,ok){if(x>0&&y>0&&x<MW-1&&y<MH-1&&ok.indexOf(T[y*MW+x])>=0)T[y*MW+x]=BK;}
function clearBld(x0,y0,x1,y1){for(let i=BLD.length-1;i>=0;i--){const b=BLD[i];if(b.x<=x1&&b.x+b.w-1>=x0&&b.y<=y1&&b.y+b.h-1>=y0){fillR(b.x,b.y,b.w,b.h,SW);BLD.splice(i,1);}}}
function playground(x0,y0,x1,y1,gap,name){
 clearBld(x0-1,y0-1,x1+1,y1+1);
 fillR(x0-1,y0-1,x1-x0+3,y1-y0+3,SW);
 fillR(x0,y0,x1-x0+1,y1-y0+1,GR);
 fillR(x0,y0,x1-x0+1,1,FN);fillR(x0,y1,x1-x0+1,1,FN);fillR(x0,y0,1,y1-y0+1,FN);fillR(x1,y0,1,y1-y0+1,FN);
 fillR(gap,y1,2,1,SW);
 NOGO.push({x0:x0*TS,y0:y0*TS,x1:(x1+1)*TS,y1:(y1+1)*TS,n:name});
 SIGNS.push({x:gap*TS-6,y:(y1+1)*TS+16});
}
function buedchen(id,x,y,name){addB(x,y,2,2,'#3f9a78','BÜDCHEN','house',5);mkm(id,'','buedchen',x,y+2,name,'#46c2a0');MKS[MKS.length-1].act=name+' besuchen';}
function portal(id,tx,ty,obj,name,act,warp){mkm(id,'','portal',tx,ty,name,'#c06bff');const m=MKS[MKS.length-1];m.obj=obj;m.act=act;m.warp=warp;}
function genExtras(){
 playground(28,34,39,43,33,'Kita-Spielplatz');
 addB(30,35,5,3,'#e88fb0','KITA SONNENSCHEIN','house',6);
 fillR(36,36,3,2,SD);
 [[31,40],[34,40],[37,40]].forEach(t=>{T[t[1]*MW+t[0]]=PG;});
 putBK(32,39,[GR]);putBK(36,40,[GR]);tree(29,36);tree(38,41);tree(29,41);
 playground(10,18,15,23,12,'Spielplatz');
 [[11,20],[14,20]].forEach(t=>{T[t[1]*MW+t[0]]=PG;});
 fillR(12,21,2,1,SD);putBK(11,22,[GR]);
 [[19,10],[31,8],[37,8],[48,8],[52,7],[49,20],[49,24],[54,24],[54,19],[68,40]].forEach(b=>putBK(b[0],b[1],[SW,GR,FD]));
 POCKETS.forEach(pk=>{
  if(pk.w<3||pk.h<2||rng()>.85)return;
  const cx=pk.x+Math.floor(pk.w/2),cy=pk.y+Math.floor(pk.h/2);
  [[0,0],[1,0],[-1,0],[0,1],[0,-1]].some(o=>{if(T[(cy+o[1])*MW+cx+o[0]]===GR){T[(cy+o[1])*MW+cx+o[0]]=BK;return true;}return false;});
 });
 buedchen('bue1',56,21,'Büdchen am Brunnen');
 buedchen('bue2',54,6,'Uni-Büdchen');
 portal('p1',23,8,'gully','Gullydeckel','Gullydeckel öffnen','Du lüpfst den Gullydeckel und rutschst hinein. Wuuuusch!');
 portal('p2',27,8,'telefon','Telefonzelle','Telefonzelle betreten','Die Telefonzelle klingelt. Du gehst ran. Am anderen Ende rauscht es.');
 portal('p3',62,7,'dixi','Dixi-Klo','Dixi-Klo betreten','Du öffnest das Dixi. Innen ist es VIEL größer als außen.');
 portal('p4',70,42,'kuehl','Kühlschrank','Kühlschrank öffnen','Licht an. Dahinter: Neuland.');
 portal('p5',3,39,'schiff','Rhein-Schiff','Schiff nach Amsterdam nehmen','Du schnappst dir ein Boot am Anleger. Amsterdam ist von hier aus gar nicht so weit.');MKS[MKS.length-1].to='rhein';
 portal('p6',18,21,'buch','Märchenbuch','Märchenbuch aufschlagen','Du schlägst das Märchenbuch auf. Die Seiten blättern von selbst. Es war einmal ...');MKS[MKS.length-1].to='maerchen';
 addB(19,24,3,2,'#e8a63a','REISEBÜRO','house',6);
 mkm('reise','','sk',20,26,'Reisebüro','#ffb347');{const m=MKS[MKS.length-1];m.sk='reise';m.act='Reisebüro: Europa-Karte öffnen';}
 genExtras2();
}
genExtras();
const MKQ={};MKS.forEach(m=>{MKQ[m.id]=m;});
function mdist(a,b){const p=MKQ[a],q=MKQ[b];return Math.hypot(p.x-q.x,p.y-q.y)/TS;}
const ZONES=[{x:73.5*TS,y:12.5*TS},{x:73.5*TS,y:28.5*TS},{x:23.5*TS,y:38.5*TS},{x:91.5*TS,y:28.5*TS}];
const YARD={x0:11*TS,y0:5*TS,x1:21*TS,y1:11*TS};
const GATE={x:16*TS+16,y:10*TS+16},VAN0={x:13*TS+16,y:10*TS+16};

const GOODS={
 m_curry:{n:'Currywurst-Menü',u:'Menü',base:8},
 m_pizza:{n:'Pizza-Menü',u:'Menü',base:10},
 m_doener:{n:'Döner-Menü',u:'Menü',base:8},
 m_gyros:{n:'Gyros-Teller',u:'Teller',base:11},
 m_asia:{n:'Asia-Box',u:'Box',base:9},
 m_kuchen:{n:'Kaffee & Kuchen',u:'Gedeck',base:6},
 b_alt:{n:'Alt',u:'Sixpack',base:8},
 b_pils:{n:'Pils',u:'Sixpack',base:7},
 b_koelsch:{n:'Kölsch',u:'Sixpack',base:7},
 b_frei:{n:'Alkoholfrei',u:'Sixpack',base:6},
 c_apo:{n:'Rezept-Päckchen',u:'Päckchen',base:0},
 c_holl:{n:'Coffeeshop-Gras',u:'Tütchen',base:10},
 c_str:{n:'Straßen-Gras',u:'Tütchen',base:6},
 koffer:{n:'Geheimrezept',base:0}
};
const MENUS=['m_curry','m_pizza','m_doener','m_gyros','m_asia','m_kuchen'];
const BEERS=['b_alt','b_pils','b_koelsch','b_frei'];
const WEED=['c_holl','c_str'];
const TRADE=MENUS.concat(BEERS,WEED,['c_apo']);
const ALC={b_alt:1,b_pils:1,b_koelsch:1};
const ILL={c_holl:1,c_str:1};
const SELL=MENUS.concat(BEERS,WEED);
const SHOP={hq:['m_curry'],pizza:['m_pizza'],doener:['m_doener'],grieche:['m_gyros'],asia:['m_asia'],cafe:['m_kuchen'],mega:['b_alt','b_pils','b_koelsch','b_frei'],land:['b_alt','b_frei'],hafen:['b_pils','b_koelsch']};
const DIST={
 hq:{n:'Imbiss Hanfred Hanfbier',sub:'Deine Zentrale',d:'Hier startet jede Tour. Die Küche brutzelt Currywurst-Menüs, du lieferst aus. Abends ist hier alles sicher, und Chefin Willi hat immer einen Spruch parat.'},
 apo:{n:'Rhein-Apotheke',sub:'Dein Hauptjob',d:'Apothekerin Dr. Kräutlein packt Rezepte für ihre Patienten: Medizinal-Cannabis in Apotheken-Qualität, verplombt und legal. Du bringst die Päckchen zu den Patienten. Ehrliche Arbeit, fester Lohn, gutes Trinkgeld.'},
 villen:{n:'Villa Blumenthal',sub:'Villenviertel',c:1,d:'Wohlhabende Kundschaft bestellt gern und gibt gutes Trinkgeld.'},
 uni:{n:'Mensa-Hinterhof',sub:'Uni-Viertel',c:1,d:'Chronisch pleite, chronisch hungrig. Bier nur an Volljährige mit Ausweis.'},
 altstadt:{n:'Zum goldenen Fass',sub:'Altstadt',c:1,d:'Die längste Theke der Stadt. Wenn das Fass leer ist, bestellen die Wirte Nachschub bei dir.'},
 land:{n:'Landgut Hopfenhof',sub:'Landgut',c:1,pf:.9,d:'Die Hofbrauerei braut Alt und Alkoholfreies. Der Bauer winkt freundlich und verkauft ab Hof.'},
 club:{n:'Club Neon',sub:'Clubmeile',c:1,d:'Bass, Nebel und volle Taschen. Die Türsteher kontrollieren Ausweise: Alkohol erst ab 18!'},
 hafen:{n:'Hafen-Großhandel',sub:'Hafen',c:1,pf:.9,d:'Pils und Kölsch palettenweise und günstig. Und hinten im Hof steht Kalle, der leise „Psst“ macht.'},
 stadion:{n:'Stadionkiosk',sub:'Stadion',c:1,d:'90 Minuten Hunger und Durst. An Spieltagen wird pausenlos bestellt.'},
 verein:{n:'Vereinsheim SV Rheinhanfen',sub:'Sportpark',c:1,d:'Nach dem Training haben alle Hunger. Hier wird nur Alkoholfreies bestellt, die Jugend ist ja dabei.'},
 pizza:{n:'Pizzeria Bella Rheinhanfen',sub:'Grachtenviertel',food:'pizza',d:'Steinofen, Basilikum und ein Chef, der bei jeder Bestellung singt. Hier gibt es das Pizza-Menü.'},
 doener:{n:'Döner-Palast',sub:'Grachtenviertel',food:'doener',d:'Der Spieß dreht sich seit Jahren ohne Pause. Mit allem und scharf: das Döner-Menü.'},
 grieche:{n:'Taverna Olympia',sub:'Grachtenviertel',food:'grieche',d:'Blau-weiße Tischdecken, der Gyros-Teller dampft, und der Ouzo kommt aufs Haus. Opa!'},
 asia:{n:'Asia Wok Glück',sub:'Grachtenviertel',food:'asia',d:'Der Wok zischt, die Asia-Boxen stapeln sich, und in jede gehört ein Glückskeks.'},
 cafe:{n:'Cafeteria Kanalblick',sub:'Grachtenviertel',food:'cafe',d:'Kaffee und Kuchen zum Mitnehmen, dazu ein Fensterplatz mit Blick auf die Boote.'},
 mega:{n:'MEGAMARKT',sub:'Riesen-Supermarkt',food:'mega',pf:.85,d:'So groß, dass es zwischen den Regalen Straßenschilder gibt. Alt, Pils, Kölsch und Alkoholfrei, alles günstig.'}
};
const CUST=Object.keys(DIST).filter(k=>DIST[k].c);
const MARKETS=CUST;
const BRAU_CAP=[3,5,8,12],HAUS_CAP=[2,4,6,9];
const UPS={
 trunk:{n:'Lieferrucksack',cost:[300,800,1600],eff:l=>'Du trägst '+(20+10*l)+' Sachen'},
 thermo:{n:'Thermobox',cost:[400,1000,2000],eff:l=>'Menüs bleiben heiß: +'+(l*10)+' % Liefergeld'},
 tuning:{n:'Getunter Van',cost:[700,1600],eff:l=>'Van fährt '+(l*25)+' km/h-Punkte schneller'},
 leib:{n:'Maskottchen-Team',cost:[500,1200,2500],eff:l=>'Miesepeter-Streiche werden zu '+(l*20)+'% früh vereitelt'},
 anwalt:{n:'Anwalt',cost:[800,1800],eff:l=>l===1?'Festnahme kostet weniger, Fahndung sinkt schneller':'Noch geringere Strafen'}
};
const NAMES={
 lieferung:['Wirt Harald','Schützenverein','Kleingärtner-Club','Hochzeitsgesellschaft','Fußball-Fanclub','Chor Frohsinn','Kegelclub Alle Neune','WG Chaos','Spieleabend bei Familie Kaya','Büro-Feierabend'],
 rezept:['Opa Heinz (Rücken)','Frau Becker (Migräne)','Herr Novak (Schlafprobleme)','Tante Gerda (Rheuma)','Herr Özdemir (Knie)','Frau Lindner (Appetit)','Herr Petersen (Schmerzen)','Frau Albers (Nerven)'],
 beschaffung:['Bauer Alois'],
 kurier:['Oma Käthe (Familienrezept)','Seniorenheim Abendsonne','Opa Willis Küche','Frau Müller (Rezept)']
};
const EVT=[
 {t:'Stadtfest in der Altstadt: Alle wollen Alt und Currywurst-Menüs.',m:[['b_alt','altstadt',1.5],['m_curry','altstadt',1.4]]},
 {t:'Heimspiel im Stadion: Die Fans bestellen Pils und Currywurst.',m:[['b_pils','stadion',1.6],['m_curry','stadion',1.5]]},
 {t:'Semesterstart: Die Uni bestellt Döner und Asia-Boxen.',m:[['m_doener','uni',1.5],['m_asia','uni',1.4]]},
 {t:'Hitzewelle: Alkoholfreies ist überall gefragt.',m:[['b_frei','*',1.5]]},
 {t:'Regentag: Keiner will raus, der Lieferdienst boomt.',m:[['m_*','*',1.3]]},
 {t:'Grippewelle: In der Rhein-Apotheke stapeln sich die Rezepte.',m:[['rezept','*',1.4]]},
 {t:'Großkontrolle der Polizei: Straßenhandel ist heute besonders riskant.',m:[['street','*',1.8]]},
 {t:'Gartenparty im Villenviertel: Gyros und Kölsch für alle.',m:[['m_gyros','villen',1.5],['b_koelsch','villen',1.4]]},
 {t:'Pokalspiel im Sportpark: Das Vereinsheim will Pizza und Alkoholfreies.',m:[['m_pizza','verein',1.6],['b_frei','verein',1.5]]},
 {t:'Kaffeeklatsch auf dem Landgut: Kaffee und Kuchen für den ganzen Hof.',m:[['m_kuchen','land',1.6]]},
 {t:'Clubnacht im Neon: Kölsch und Asia-Boxen gehen weg wie nichts.',m:[['b_koelsch','club',1.5],['m_asia','club',1.4]]}
];

let G=null;
let notify=function(){};
function cap(){return 20+10*(G.up.trunk||0);}
function startsN(){try{return +localStorage.getItem('hh_starts')||0;}catch(e){return 0;}}
function bumpStarts(){try{localStorage.setItem('hh_starts',String(startsN()+1));}catch(e){}}
function champOk(){return true;}
function champHint(){return '';}
function mkInv(){const o={koffer:0};TRADE.forEach(g=>{o[g]=0;});return o;}
function mkMkt(){const o={};TRADE.forEach(g=>{o[g]=1;});return o;}
function gq(g,q){const G0=GOODS[g]||{n:g};return q+'× '+G0.n+(G0.u==='Sixpack'||G0.u==='Tütchen'?' ('+G0.u+')':'');}
function used(){return TRADE.reduce((s,g)=>s+(G.inv[g]||0),0)+(G.inv.koffer||0);}
function heat(v){G.heat=clamp(G.heat+v,0,100);}
function evMult(g,d){let m=1;G.events.forEach(e=>{(e.m||[]).forEach(x=>{const a=x[0];const hit=a===g||a==='*'||(a.length>1&&a.slice(-1)==='*'&&g.indexOf(a.slice(0,-1))===0);if(hit&&(x[1]===d||x[1]==='*'))m*=x[2];});});return m;}
function price(g,d){const D=DIST[d];return Math.max(1,Math.round(GOODS[g].base*((D&&D.pf)||1)*(G.mkt[g]||1)));}
function pedPrice(g){const m=G.mkt[g]||1;if(g==='c_holl')return Math.round(28*m);if(g==='c_str')return Math.round(18*m);if(g==='c_plant')return Math.round(40*m);return Math.max(2,Math.round(GOODS[g].base*1.8*m));}
function sellP(g,d){return pedPrice(g);}
function rollMarket(){
 TRADE.forEach(g=>{const v=G.mkt[g]||1;G.mkt[g]=clamp(v*(1+(Math.random()-.5)*.14)+(1-v)*.3,.88,1.15);});
 G.noise={};G.imp={};
}
function pk(m){return m.t==='kurier'||m.t==='rezept';}
function srcTxt(g){return Object.keys(SHOP).filter(k=>SHOP[k].indexOf(g)>=0).map(k=>DIST[k].n).join(', ');}
function nearSrc(g,to,x,y){
 let b=null,bd=1e9;
 Object.keys(SHOP).forEach(k=>{if(SHOP[k].indexOf(g)<0||!MKQ[k])return;const d=x!==undefined?Math.hypot(MKQ[k].x-x,MKQ[k].y-y):(MKQ[to]?mdist(k,to):0);if(d<bd){bd=d;b=k;}});
 return b||to;
}
function mTgt(m){if(pk(m))return m.got?m.to:m.from;if((G.inv[m.item]||0)<m.q)return nearSrc(m.item,m.to,P.x,P.y);return m.to;}
function mkOffer(ft){
 const ban=G.apoBan&&G.day<G.apoBan;
 const w=[['rezept',ban?0:5*evMult('rezept','*')],['lieferung',4.5],['kurier',1]];
 const tot=w.reduce((s,x)=>s+x[1],0);
 let r=Math.random()*tot,t='lieferung';
 for(let i=0;i<w.length;i++){if(r<w[i][1]){t=w[i][0];break;}r-=w[i][1];}
 if(ft&&!(ft==='rezept'&&ban))t=ft;
 const sc=1+G.resp*.03;
 const o={id:G.nid++,t:t,got:false,cl:rnd(0,99),dl:G.day+rnd(2,4)};
 if(t==='rezept'){
  o.from='apo';o.to=pick(CUST);
  o.rw=r5((rnd(45,75)+mdist('apo',o.to)*1.2+G.resp*3)*evMult('rezept','*'));
  o.dl=G.day+rnd(1,3);
 }else if(t==='lieferung'){
  let it=null,to=null;
  const ev=[];G.events.forEach(e=>(e.m||[]).forEach(x=>{if(GOODS[x[0]]&&TRADE.indexOf(x[0])>=0)ev.push(x);}));
  if(ev.length&&chance(.45)){const x=pick(ev);it=x[0];if(x[1]!=='*'&&DIST[x[1]])to=x[1];}
  if(!it)it=chance(.6)?pick(MENUS):pick(BEERS);
  if(!to){const pool=CUST.filter(k=>(SHOP[k]||[]).indexOf(it)<0&&!(ALC[it]&&k==='verein'));to=pick(pool);}
  if(ALC[it]&&to==='verein')it='b_frei';
  o.item=it;o.to=to;
  o.q=Math.max(1,Math.round(rnd(2,5)*sc));
  const src=nearSrc(it,to);
  o.rw=r5((o.q*GOODS[it].base*1.5+25+mdist(src,to)*1.4)*(1+.1*(G.up.thermo||0))*(G.masc&&G.masc[src]?1.15:1)*evMult(it,to));
 }else{
  o.from=pick(Object.keys(DIST));
  do{o.to=pick(Object.keys(DIST));}while(o.to===o.from);
  o.rw=r10(rnd(250,450)+mdist(o.from,o.to)*6+G.resp*15);
  o.dl=G.day+rnd(2,4);
 }
 {const k0=(t==='lieferung'&&o.item&&GOODS[o.item])?o.q*GOODS[o.item].base:0;o.rw=r5(k0+(o.rw-k0)*.5);}
 return o;
}
function offerTarget(){return Math.min(7,4+Math.floor(G.resp/6));}
function fillOffers(){while(G.offers.length<offerTarget())G.offers.push(mkOffer());}
function mTitle(o){const L=NAMES[o.t]||NAMES.lieferung;return L[o.cl%L.length];}
function mLine(o){
 if(o.t==='kurier')return 'Geheimrezept abholen: '+DIST[o.from].n+'. Übergabe: '+DIST[o.to].n+'.';
 if(o.t==='rezept')return 'Rezept-Päckchen abholen: Rhein-Apotheke. Zum Patienten: '+DIST[o.to].n+'.';
 return 'Bestellung: '+gq(o.item,o.q)+' nach '+DIST[o.to].n+'. Gibt es bei: '+srcTxt(o.item)+'.';
}
function canPickup(m){return pk(m)&&!m.got&&G.loc===m.from;}
function canDeliver(m){if(G.loc!==m.to)return false;if(pk(m))return m.got;return (G.inv[m.item]||0)>=m.q;}
function whyNot(m){
 if(m.t==='rezept')return m.got?'':'Hol das Päckchen erst in der Rhein-Apotheke ab.';
 if(m.t==='kurier')return m.got?'':'Du hast das Paket noch nicht abgeholt.';
 return 'Dir fehlen noch '+Math.max(0,m.q-(G.inv[m.item]||0))+'. '+GOODS[m.item].n+' gibt es bei: '+srcTxt(m.item)+'.';
}
function accept(id){
 if(G.active.length>=4)return{ok:false,msg:'Du kannst nur 4 Aufträge gleichzeitig führen.'};
 const i=G.offers.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:'Angebot nicht mehr da.'};
 const o=G.offers.splice(i,1)[0];G.active.push(o);
 return{ok:true,msg:'Auftrag angenommen: '+mTitle(o)+'.'+(o.t==='rezept'?' Ab in die Rhein-Apotheke.':o.t==='lieferung'?' Einkaufen bei: '+srcTxt(o.item)+'.':'')};
}
function failM(m){if(m.t==='kurier'&&m.got)G.inv.koffer=Math.max(0,G.inv.koffer-1);if(m.t==='rezept'&&m.got)G.inv.c_apo=Math.max(0,(G.inv.c_apo||0)-1);}
function abandon(id){
 const i=G.active.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:'Auftrag nicht gefunden.'};
 const m=G.active.splice(i,1)[0];failM(m);G.resp=Math.max(0,G.resp-1);
 return{ok:true,msg:'Auftrag abgebrochen (-1 Respekt).'};
}
function pickup(id){
 const m=G.active.find(o=>o.id===id);if(!m||!canPickup(m))return{ok:false,msg:'Hier gibt es nichts abzuholen.'};
 if(used()>=cap())return{ok:false,msg:'Du kannst nichts mehr tragen.'};
 m.got=true;
 if(m.t==='rezept'){G.inv.c_apo=(G.inv.c_apo||0)+1;return{ok:true,msg:'Dr. Kräutlein reicht dir das verplombte Päckchen für '+mTitle(m)+': "Nur für den Patienten. Und schön vorsichtig fahren!"'};}
 G.inv.koffer++;heat(6);
 return{ok:true,msg:'Du übernimmst das Geheimrezept. Streng geheim, aber lecker.'};
}
function deliver(id){
 const m=G.active.find(o=>o.id===id);if(!m||!canDeliver(m))return{ok:false,msg:m?whyNot(m):'Auftrag nicht gefunden.'};
 if(m.t==='kurier')G.inv.koffer--;else if(m.t==='rezept')G.inv.c_apo--;else G.inv[m.item]-=m.q;
 G.active.splice(G.active.indexOf(m),1);
 G.cash+=m.rw;G.stats.earned+=m.rw;G.stats.done++;popAdd(1);xpAdd(m.t==='rezept'?12:10);if(m.t==='rezept')G.stats.apo=(G.stats.apo||0)+1;
 const rp=m.t==='kurier'?2:1;G.resp+=rp;
 if(m.t==='rezept')return{ok:true,msg:mTitle(m)+' bedankt sich herzlich. Lohn und Trinkgeld: +'+eur(m.rw)+', +1 Respekt.'};
 return{ok:true,msg:'Auftrag erledigt: +'+eur(m.rw)+' und +'+rp+' Respekt.'};
}
function buyAt(g,q,d){
 const ok=(SHOP[d]||[]).indexOf(g)>=0||(d==='coffeeshop'&&g==='c_holl')||(d==='kalle'&&g==='c_str');
 if(!ok||!GOODS[g])return{ok:false,msg:'Das gibt es hier nicht.'};
 const p=price(g,d),room=cap()-used(),aff=Math.floor(G.cash/p);
 const n=q==='max'?Math.min(room,aff):Math.min(+q,room,aff);
 if(n<=0)return{ok:false,n:0,msg:aff<1?'Nicht genug Geld.':'Du kannst nicht mehr tragen.'};
 G.cash-=n*p;G.inv[g]=(G.inv[g]||0)+n;if(ILL[g])heat(g==='c_str'?4:1);
 return{ok:true,n:n,msg:gq(g,n)+' gekauft für '+eur(n*p)+'.'};
}
function buy(g,q){return buyAt(g,q,G.loc);}
function sell(g,q){return{ok:false,msg:'Verkauft wird an deine Kundschaft und an Leute auf der Straße: ansprechen und etwas anbieten.'};}
function needAt(d){
 const L=SHOP[d]||[],o={};
 G.active.forEach(m=>{if(m.t==='lieferung'&&L.indexOf(m.item)>=0)o[m.item]=(o[m.item]||0)+m.q;});
 const r=[];Object.keys(o).forEach(g=>{const n=o[g]-(G.inv[g]||0);if(n>0)r.push([g,n]);});
 return r;
}
function buyNeeded(d){
 const L=needAt(d);if(!L.length)return{ok:false,msg:'Für deine Aufträge brauchst du hier nichts.'};
 const got=[];
 for(const x of L){const r=buyAt(x[0],x[1],d);if(!r.ok||r.n<x[1]){if(r.ok)got.push(gq(x[0],r.n));return{ok:got.length>0,msg:(got.length?'Eingekauft: '+got.join(', ')+'. ':'')+(r.ok?'Mehr ging nicht: Geld oder Platz reicht nicht.':r.msg)};}got.push(gq(x[0],x[1]));}
 return{ok:true,msg:'Eingekauft: '+got.join(', ')+'. Ab zur Kundschaft!'};
}
function startBrew(q){return{ok:false,msg:'Die Küche kocht jetzt selbst. Du lieferst nur noch aus.'};}
function startGrow(q){return startBrew(q);}
function collect(){return startBrew();}
function buyUp(k){
 const u=UPS[k],l=G.up[k]||0;
 if(l>=u.cost.length)return{ok:false,msg:'Schon auf Höchststufe.'};
 if(G.cash<u.cost[l])return{ok:false,msg:'Dafür fehlt dir das Geld.'};
 G.cash-=u.cost[l];G.up[k]=l+1;
 return{ok:true,msg:u.n+' ausgebaut auf Stufe '+G.up[k]+'.'};
}
function payDebt(q){
 const n=q==='all'?Math.min(G.cash,G.debt):Math.min(+q,G.cash,G.debt);
 if(n<=0)return{ok:false,msg:G.debt<=0?'Du hast keinen Vorschuss offen.':'Du hast kein Geld dabei.'};
 G.cash-=n;G.debt-=n;
 return{ok:true,msg:eur(n)+' zurückgezahlt.'};
}
function loan(n){
 if(G.debt+n>8000)return{ok:false,msg:'Chefin Willi gibt keinen Vorschuss mehr. Limit: 8.000 €.'};
 G.cash+=n;G.debt+=n;
 return{ok:true,msg:eur(n)+' Vorschuss ausgezahlt. Chefin Willi lächelt.'};
}
function cargoVal(){return TRADE.reduce((s,g)=>s+(G.inv[g]||0)*GOODS[g].base,0)+(G.inv.c_apo||0)*40+(G.inv.koffer||0)*300;}
function illegal(){return G.heat>=30?(G.inv.c_holl||0)+(G.inv.c_str||0)+(G.inv.c_plant||0):0;}
function loseGoods(frac){let n=0;SELL.forEach(g=>{const l=Math.ceil((G.inv[g]||0)*frac);G.inv[g]-=l;n+=l;});return n;}
function migrateEco(){
 const OLD={zutat:12,wasser:6,cola:10,limo:10,kaffee:12,eis:14,pommes:18,curry:26,haehnchen:34,schnitzel:42,bier:30,wein:60,champ:180};
 let ref=0;
 Object.keys(OLD).forEach(k=>{if(typeof G.inv[k]==='number'&&G.inv[k]>0)ref+=G.inv[k]*OLD[k];delete G.inv[k];delete G.mkt[k];});
 const p=G.prod;
 if(p&&p.out){ref+=(p.out.curry||0)*26+(p.out.eis||0)*14;p.out={curry:0,eis:0};}
 if(p&&p.brau&&p.brau.n>0){ref+=p.brau.n*24;p.brau={n:0,left:0};}
 if(p&&p.haus&&p.haus.n>0){ref+=p.haus.n*24;p.haus={n:0,left:0};}
 if(ref>0){const v=Math.round(ref*.8);G.cash+=v;G.migr=v;}
}
function newDay(slept){
 const L=[];
 G.day++;G.frust=100;G.calm=0;try{if(WORLDS.sender)WORLDS.sender.splats=[];}catch(e){}
 if(G.debt>0){const a=Math.round(G.debt*.02);G.debt+=a;L.push('Chefin Willi rechnet '+eur(a)+' Zinsen auf den Vorschuss.');}
 dayHook(L);homeDay(L);medDay(L);
 heat(slept?-12:-5);
 if(G.apoBan&&G.day>=G.apoBan){G.apoBan=0;L.push('Dr. Kräutlein ruft an: "Na gut, du bekommst noch eine Chance. Ab heute wieder Rezept-Touren!"');}
 rollMarket();
 G.events=G.events.filter(e=>{e.left--;return e.left>0;});
 if(G.events.length<2&&chance(.45)){
  const t=pick(EVT);
  if(!G.events.some(e=>e.t===t.t)){G.events.push({t:t.t,left:rnd(1,2),m:t.m});L.push('Neuigkeit: '+t.t);}
 }
 G.active=G.active.filter(m=>{
  if(m.dl<G.day){failM(m);G.resp=Math.max(0,G.resp-1);L.push('Auftrag verpasst: '+mTitle(m)+' (-1 Respekt).');return false;}
  return true;
 });
 G.offers=G.offers.filter(o=>o.dl>=G.day&&!(o.t==='rezept'&&G.apoBan&&G.day<G.apoBan));
 fillOffers();
 try{gangHeist(L);}catch(e){}
 return L;
}
function worth(){
 let w=G.cash-G.debt;
 SELL.forEach(g=>{w+=(G.inv[g]||0)*GOODS[g].base*.8;});
 w+=ownWorth();
 return Math.round(w);
}
function rank(w){
 if(w<-3000)return'Schuldenkönig';
 if(w<0)return'Pleitegeier';
 if(w<1500)return'Aushilfsbote';
 if(w<4000)return'Fahrradkurier';
 if(w<8000)return'Lieferprofi';
 if(w<15000)return'Chef-Kurier';
 if(w<30000)return'Lieferlegende';
 if(w<60000)return'Stadtbaron';
 if(w<120000)return'Landschaftskönig';
 if(w<250000)return'Europa-Mogul';
 return'Legende von Rheinhanfen';
}
function clock(){const h=G.t/DAY_S*24,hh=Math.floor(h),mm=Math.floor((h-hh)*60);return(hh<10?'0':'')+hh+':'+(mm<10?'0':'')+mm;}
function hour(){return G.t/DAY_S*24;}
function newGame(){
 bumpStarts();
 G={day:1,t:8/24*DAY_S,cash:900,debt:2500,heat:5,resp:0,loc:'',
  inv:mkInv(),
  up:{brau:0,haus:0,trunk:0,tuning:0,leib:0,anwalt:0,thermo:0},apoBan:0,
  prod:{brau:{n:0,left:0},haus:{n:0,left:0},out:{curry:0,eis:0}},
  mkt:mkMkt(),noise:{},imp:{},events:[],offers:[],active:[],nid:1,won:false,mood:62,drunk:0,high:0,stock:{bier:3,joint:2,gluehwein:0},ammo:{dose:0,stein:0,schnee:0,ei:0},sel:'',ret:null,pistol:false,tank:0,wet:0,hero:0,heroE:0,fang:0,zahn:0,teaT:0,
  stats:{done:0,earned:0,arrests:0,fights:0,apo:0,street:0}};
 rollMarket();G.offers.push(mkOffer('rezept'));G.offers.push(mkOffer('lieferung'));fillOffers();
 resetEntities();
 gangHeist([],true);
}

const SK='hh_welt_save_v1';
function saveAll(){try{localStorage.setItem(SK,JSON.stringify({G:G,P:{x:(ZONE&&G.ret?G.ret:P).x,y:(ZONE&&G.ret?G.ret:P).y},V:{x:V.x,y:V.y,a:V.a}}));}catch(e){}}
function hasSave(){try{return !!localStorage.getItem(SK);}catch(e){return false;}}
function fixG(){
 if(!G.inv)G.inv={};if(!G.mkt)G.mkt={};if(!G.prod)G.prod={brau:{n:0,left:0},haus:{n:0,left:0}};
 migrateEco();
 if(!G.up)G.up={};['trunk','tuning','leib','anwalt','thermo'].forEach(k=>{if(typeof G.up[k]!=='number')G.up[k]=0;});
 if(!G.stats)G.stats={done:0,earned:0,arrests:0,fights:0};if(G.stats.apo===undefined)G.stats.apo=0;if(G.stats.street===undefined)G.stats.street=0;
 if(G.apoBan===undefined)G.apoBan=0;
 TRADE.forEach(g=>{if(typeof G.inv[g]!=='number')G.inv[g]=0;if(typeof G.mkt[g]!=='number')G.mkt[g]=1;});
 if(typeof G.inv.koffer!=='number')G.inv.koffer=0;
 if(!G.prod.out||typeof G.prod.out.curry!=='number')G.prod.out={curry:0,eis:0};
 G.noise={};G.imp={};
 G.offers=(G.offers||[]).filter(o=>o.t==='kurier'||o.t==='rezept'||(o.t==='lieferung'&&TRADE.indexOf(o.item)>=0&&DIST[o.to]));
 G.active=(G.active||[]).filter(o=>o.t==='kurier'||o.t==='rezept'||(o.t==='lieferung'&&TRADE.indexOf(o.item)>=0&&DIST[o.to]));
 if(G.champSeen===undefined)G.champSeen=false;
 if(G.mood===undefined)G.mood=62;
 if(G.drunk===undefined)G.drunk=0;
 if(G.hero===undefined)G.hero=0;
 if(G.heroE===undefined)G.heroE=0;
 if(G.fang===undefined)G.fang=0;
 if(G.zahn===undefined)G.zahn=0;
 G.teaT=0;
 if(G.high===undefined)G.high=0;
 if(!G.stock)G.stock={bier:3,joint:2};
 if(!G.ammo)G.ammo={dose:0,stein:0,schnee:0,ei:0};
 if(G.ammo.ei===undefined)G.ammo.ei=0;
 if(G.sel===undefined)G.sel='';
 if(G.stock.gluehwein===undefined)G.stock.gluehwein=0;
 if(G.pistol===undefined)G.pistol=false;
 if(G.tank===undefined)G.tank=0;
 G.wet=0;
 G.ret=null;
}
function loadAll(){
 try{
  const s=JSON.parse(localStorage.getItem(SK));if(!s||!s.G)return false;
  G=s.G;G.loc='';fixG();bumpStarts();toCity();resetEntities();
  P.x=s.P.x;P.y=s.P.y;V.x=s.V.x;V.y=s.V.y;V.a=s.V.a;if(!(V.x>TS&&V.y>TS&&V.x<MW*TS-TS&&V.y<MH*TS-TS)||hit(V.x,V.y,12)){V.x=VAN0.x;V.y=VAN0.y;V.a=0;V.sp=0;}
  return true;
 }catch(e){return false;}
}

const keys={up:0,down:0,left:0,right:0};
const P={x:GATE.x,y:GATE.y,vx:0,vy:0,a:0,inCar:false,stun:0,walk:0};
const V={x:VAN0.x,y:VAN0.y,a:0,sp:0};
const cam={x:0,y:0};
let traffic=[],peds=[],cops=[],thugs=[],chasers=[],kids=[],PICKS=[],FX=[],PR=[],RACE=null,CITYENT=null,fade=null,shake=0,pickT=5,eruptT=12,fdt=.016,flash=0,tipShown=false;const WORLDS={};
let wanted=0,escapeT=0,bustT=0,flowT=0,saveT=0,msgCb=function(){},busted=function(){};
const FLOW=new Int16Array(MW*MH);
const NX=VR.map(v=>(v+1)*TS),NY=HR.map(h=>(h+1)*TS);

function hit(x,y,r){
 const x0=Math.floor((x-r)/TS),x1=Math.floor((x+r)/TS),y0=Math.floor((y-r)/TS),y1=Math.floor((y+r)/TS);
 for(let j=y0;j<=y1;j++)for(let i=x0;i<=x1;i++)if(isSolid(i,j))return true;
 return false;
}
function moveE(e,dx,dy,r){
 e.hx=false;e.hy=false;
 let nx=e.x+dx;if(hit(nx,e.y,r)){nx=e.x;e.hx=true;}e.x=nx;
 let ny=e.y+dy;if(hit(e.x,ny,r)){ny=e.y;e.hy=true;}e.y=ny;
 e.x=clamp(e.x,TS,MW*TS-TS);e.y=clamp(e.y,TS,MH*TS-TS);
}
function walkable(x,y){return !isSolid(Math.floor(x/TS),Math.floor(y/TS));}
function randTile(types,minD,maxD,fx,fy){
 for(let k=0;k<400;k++){
  const x=rnd(1,MW-2),y=rnd(1,MH-2),t=T[y*MW+x];
  if(types.indexOf(t)<0)continue;
  const px=x*TS+16,py=y*TS+16;
  if(fx!==undefined){const d=Math.hypot(px-fx,py-fy);if(d<minD||d>maxD)continue;}
  return{x:px,y:py};
 }
 return{x:GATE.x,y:GATE.y};
}
function setNext(c){
 const o=[];
 [[1,0],[-1,0],[0,1],[0,-1]].forEach(d=>{
  const ni=c.ni+d[0],nj=c.nj+d[1];
  if(ni>=0&&ni<VR.length&&nj>=0&&nj<HR.length&&!(ni===c.i&&nj===c.j))o.push([ni,nj]);
 });
 const p=pick(o);c.i=c.ni;c.j=c.nj;c.ni=p[0];c.nj=p[1];
 c.dx=Math.sign(c.ni-c.i);c.dy=Math.sign(c.nj-c.j);
 c.len=Math.hypot(NX[c.ni]-NX[c.i],NY[c.nj]-NY[c.j]);c.s=0;
 c.tox=-c.dy*16;c.toy=c.dx*16;
}
function mkCar(cop){
 const i=rnd(0,VR.length-1),j=rnd(0,HR.length-1);
 let ni=i,nj=j;if(chance(.5)){ni=i+(i<VR.length-1&&chance(.6)?1:-1);}else{nj=j+(j<HR.length-1&&chance(.6)?1:-1);}
 ni=clamp(ni,0,VR.length-1);nj=clamp(nj,0,HR.length-1);if(ni===i&&nj===j){ni=i===0?1:i-1;}
 const c={i:i,j:j,ni:ni,nj:nj,s:rf(0,200),dx:0,dy:0,len:1,ox:0,oy:0,tox:0,toy:0,sp:0,x:0,y:0,a:0,cop:cop,col:cop?'#f4f4f4':pick(['#c0392b','#2e86c1','#27ae60','#f1c40f','#8e44ad','#7f8c8d','#d35400','#ecf0f1']),blocked:0,free:0};
 c.dx=Math.sign(c.ni-c.i);c.dy=Math.sign(c.nj-c.j);
 c.len=Math.hypot(NX[c.ni]-NX[c.i],NY[c.nj]-NY[c.j]);c.s=Math.min(c.s,c.len-10);
 c.tox=-c.dy*16;c.toy=c.dx*16;c.ox=c.tox;c.oy=c.toy;
 c.x=NX[c.i]+c.dx*c.s+c.ox;c.y=NY[c.j]+c.dy*c.s+c.oy;c.a=Math.atan2(c.dy,c.dx);
 return c;
}
function resetEntities(){
 traffic=[];for(let i=0;i<19;i++)traffic.push(mkCar(false));for(let i=0;i<2;i++)traffic.push(mkCar(true));
 peds=[];for(let i=0;i<40;i++){const p=randTile([SW,GR],0,0);peds.push(mkPed(p.x,p.y));}
 addTeens();
 cops=[];for(let i=0;i<6;i++){const p=randTile([SW],0,0);cops.push({x:p.x,y:p.y,a:rf(0,6.28),t:rf(.5,3),sp:30,alert:0,hx:false,hy:false,hx0:p.x,hy0:p.y});}
 thugs=[];ZONES.forEach(z=>{for(let i=0;i<2;i++)thugs.push({x:z.x+rf(-20,20),y:z.y+rf(-20,20),a:rf(0,6.28),t:rf(.5,2),hx0:z.x,hy0:z.y,st:'idle',cool:0,ko:0,hp:2,stun:0,hx:false,hy:false});});
 chasers=[];wanted=0;escapeT=0;bustT=0;
 kids=[];NOGO.forEach(n=>{const c=n.n==='Kita-Spielplatz'?5:3;for(let i=0;i<c;i++){let x=n.x0+60,y=n.y0+60;for(let k=0;k<30;k++){x=rf(n.x0+30,n.x1-30);y=rf(n.y0+30,n.y1-30);if(!hit(x,y,6))break;}kids.push({x:x,y:y,a:rf(0,6.28),t:rf(.5,2),col:pick(['#ff6b9d','#ffd23f','#4dd0e1','#9ccc65','#ff8a65']),walk:0,z:n});}});
 PICKS=[];for(let i=0;i<42;i++)spawnPick(true);FX=[];PR=[];RACE=null;P.sit=null;P.dance=0;P.ride=null;P.build=null;P.coast=null;MG=null;campEnd(true);fireReset();POLO=null;CAS=[];mkCityRides();spInit();
 P.x=GATE.x;P.y=GATE.y;P.vx=0;P.vy=0;P.inCar=false;P.ride=null;P.build=null;P.coast=null;MG=null;campEnd(true);fireReset();POLO=null;P.stun=0;
 V.x=VAN0.x;V.y=VAN0.y;V.a=0;V.sp=0;
}

function computeFlow(){
 FLOW.fill(-1);
 const q=new Int32Array(MW*MH);let h=0,t=0;
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 const s=clamp(Math.floor(py/TS),0,MH-1)*MW+clamp(Math.floor(px/TS),0,MW-1);
 FLOW[s]=0;q[t++]=s;
 while(h<t){
  const c=q[h++],cx=c%MW,cy=(c-cx)/MW,d=FLOW[c]+1;
  if(cx>0&&FLOW[c-1]<0&&!isSolid(cx-1,cy)){FLOW[c-1]=d;q[t++]=c-1;}
  if(cx<MW-1&&FLOW[c+1]<0&&!isSolid(cx+1,cy)){FLOW[c+1]=d;q[t++]=c+1;}
  if(cy>0&&FLOW[c-MW]<0&&!isSolid(cx,cy-1)){FLOW[c-MW]=d;q[t++]=c-MW;}
  if(cy<MH-1&&FLOW[c+MW]<0&&!isSolid(cx,cy+1)){FLOW[c+MW]=d;q[t++]=c+MW;}
 }
}
function chaseStep(u,sp,dt,r){
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 let tx=px,ty=py;
 const d=Math.hypot(px-u.x,py-u.y);
 const cx=clamp(Math.floor(u.x/TS),0,MW-1),cy=clamp(Math.floor(u.y/TS),0,MH-1),cur=FLOW[cy*MW+cx];
 if(d>TS*1.6&&cur>0){
  let best=cur,bx=-1,by=-1;
  [[1,0],[-1,0],[0,1],[0,-1]].forEach(o=>{
   const nx=cx+o[0],ny=cy+o[1];if(nx<0||ny<0||nx>=MW||ny>=MH)return;
   const f=FLOW[ny*MW+nx];if(f>=0&&f<best){best=f;bx=nx;by=ny;}
  });
  if(bx>=0){tx=bx*TS+16;ty=by*TS+16;}
 }
 const dx=tx-u.x,dy=ty-u.y,l=Math.hypot(dx,dy)||1;
 u.a=Math.atan2(dy,dx);
 moveE(u,dx/l*sp*dt,dy/l*sp*dt,r);
}

function startWanted(why){
 if(wanted>0)return;
 wanted=1+(G.heat>=40?1:0)+(G.heat>=75?1:0);escapeT=0;bustT=0;
 heat(5);
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 chasers=[];
 for(let i=0;i<wanted+1;i++){const p=randTile([RD,SW],520,760,px,py);chasers.push({x:p.x,y:p.y,a:0,kind:'officer',hx:false,hy:false});}
 for(let i=0;i<wanted-1;i++){const p=randTile([RD],520,800,px,py);chasers.push({x:p.x,y:p.y,a:0,kind:'car',hx:false,hy:false});}
 msgCb(why||'Fahndung! Die Polizei ist hinter dir her. Hau ab!');
 computeFlow();
}
function endWanted(msg){
 wanted=0;chasers=[];escapeT=0;bustT=0;heat(-10);
 if(msg)msgCb(msg);
}
function arrest(){
 G.stats.arrests++;P.hide=null;popAdd(-8);
 const lost=0;
 const frac=G.up.anwalt>0?(G.up.anwalt>1?.15:.22):.35,loss=Math.round(G.cash*frac);
 G.cash-=loss;
 for(let i=G.active.length-1;i>=0;i--){const m=G.active[i];if(m.t==='kurier'&&m.got){G.active.splice(i,1);G.resp=Math.max(0,G.resp-1);}}
 G.inv.koffer=0;const ARX=streetBust();G.heat=Math.min(G.heat,35);
 wanted=0;chasers=[];escapeT=0;bustT=0;
 P.x=GATE.x;P.y=GATE.y;P.vx=0;P.vy=0;P.inCar=false;P.ride=null;P.build=null;P.coast=null;MG=null;campEnd(true);fireReset();POLO=null;V.x=VAN0.x;V.y=VAN0.y;V.a=0;V.sp=0;
 const L=sleepTo(6,false);
 busted([(ARX?'Strafe wegen Straßenhandel: ':'Verwarnung wegen Falschparkens: ')+eur(loss)+'.','Du verbringst die Nacht zur Beruhigung auf der Wache.'].concat(ARX?[ARX]:[],L));
}
function sleepTo(h,slept){
 const L=[];
 if(hour()>=h){const l=newDay(slept);l.forEach(x=>L.push(x));}
 G.t=h/24*DAY_S;
 return L;
}
function sleepHome(){
 const L=sleepTo(6,true);
 saveAll();
 return L;
}
function mugging(u){
 u.st='cool';u.cool=25;u.stun=1.2;
 const t=pick(['Der Miesepeter will dir die Ware klauen, rutscht aber auf einer Bananenschale aus und landet in der Pfütze. Du verlierst nichts!','Der Miesepeter greift nach deiner Tasche, bekommt aber nur ein Konfetti-Bömbchen ab. Du verlierst nichts!','Der Miesepeter schleicht sich an, stolpert über seine eigenen Schnürsenkel und fällt in einen Heuballen. Du verlierst nichts!']);
 addFx(u.x,u.y-18,pick(['Oups!','Schlitter!','Plumps!']),'#ffd23f',1.2);
 msgCb(chance(G.up.leib*.2)?'Das Maskottchen-Team vereitelt den Streich der Miesepeter schon vorher. Du verlierst nichts!':t);
}
function pushOut(e,r){
 traffic.forEach(c=>{
  const dx=e.x-c.x,dy=e.y-c.y,d=Math.hypot(dx,dy),m=r+12;
  if(d<m&&d>0){const nx=e.x+dx/d*(m-d),ny=e.y+dy/d*(m-d);if(!hit(nx,ny,r)){e.x=nx;e.y=ny;}else if(!hit(nx,e.y,r))e.x=nx;else if(!hit(e.x,ny,r))e.y=ny;}
 });
}
function drive(dt,ax,ay){
 const maxS=250+25*G.up.tuning;
 if(ay<0)V.sp=Math.min(maxS,V.sp+280*dt);
 else if(ay>0){if(V.sp>10)V.sp=Math.max(0,V.sp-560*dt);else V.sp=Math.max(-110,V.sp-220*dt);}
 else V.sp-=Math.sign(V.sp)*Math.min(Math.abs(V.sp),150*dt);
 const steer=ax*2.5*clamp(Math.abs(V.sp)/90,0,1)*(V.sp<0?-1:1);
 V.a+=steer*dt;
 moveE(V,Math.cos(V.a)*V.sp*dt,Math.sin(V.a)*V.sp*dt,12);
 if(V.hx||V.hy)V.sp*=-.25;
 traffic.forEach(c=>{
  const dx=V.x-c.x,dy=V.y-c.y,d=Math.hypot(dx,dy);
  if(d<26&&d>0){V.x+=dx/d*(26-d);V.y+=dy/d*(26-d);V.sp*=.7;c.blocked=Math.max(c.blocked,0.5);}
 });
}
function inYard(x,y){return x>YARD.x0&&x<YARD.x1&&y>YARD.y0&&y<YARD.y1;}

function trafficUpdate(dt){
 traffic.forEach(c=>{
  let sp=c.cop?105:rf(0,0)+95+((c.i+c.j)%3)*12;
  let blockedNow=false;
  const ents=[{x:P.inCar?V.x:P.x,y:P.inCar?V.y:P.y}];
  traffic.forEach(o=>{if(o!==c)ents.push(o);});
  for(let k=0;k<ents.length&&!blockedNow;k++){
   const e=ents[k],vx=e.x-c.x,vy=e.y-c.y,fwd=vx*c.dx+vy*c.dy,lat=Math.abs(vx*-c.dy+vy*c.dx);
   if(fwd>0&&fwd<52&&lat<20)blockedNow=true;
  }
  if(c.free>0){c.free-=dt;blockedNow=false;}
  if(blockedNow){c.blocked+=dt;if(c.blocked>3){c.free=1.5;c.blocked=0;}sp=0;}else c.blocked=Math.max(0,c.blocked-dt);
  c.sp+=(sp-c.sp)*Math.min(1,dt*4);
  c.s+=c.sp*dt;
  if(c.s>=c.len)setNext(c);
  c.ox+=(c.tox-c.ox)*Math.min(1,dt*4);c.oy+=(c.toy-c.oy)*Math.min(1,dt*4);
  c.x=NX[c.i]+c.dx*c.s+c.ox;c.y=NY[c.j]+c.dy*c.s+c.oy;
  const ta=Math.atan2(c.dy,c.dx);let da=ta-c.a;while(da>Math.PI)da-=6.283;while(da<-Math.PI)da+=6.283;c.a+=da*Math.min(1,dt*6);
 });
}
function wander(u,dt,sp,onlyWalk){
 u.t-=dt;
 const bad=v=>v===RD||(v===DK&&!onlyWalk),ct=T[clamp(Math.floor(u.y/TS),0,MH-1)*MW+clamp(Math.floor(u.x/TS),0,MW-1)];
 if(bad(ct)){
  if(!(u.esc>0)){u.esc=1.2;const cx=Math.floor(u.x/TS),cy=Math.floor(u.y/TS);let best=null,bk=9;[[1,0],[-1,0],[0,1],[0,-1]].forEach(d=>{for(let k=1;k<=4&&k<bk;k++){if(isSolid(cx+d[0]*k,cy+d[1]*k))break;if(!bad(tget(cx+d[0]*k,cy+d[1]*k))){bk=k;best=d;break;}}});if(best)u.a=Math.atan2(best[1],best[0])+rf(-.25,.25);}
  u.esc-=dt;
  const ex=u.x+Math.cos(u.a)*sp*dt,ey=u.y+Math.sin(u.a)*sp*dt;
  if(isSolid(Math.floor(ex/TS),Math.floor(ey/TS))){u.esc=0;return;}
  u.x=ex;u.y=ey;u.walk=(u.walk||0)+sp*dt*.15;return;
 }
 u.esc=0;
 const nx=u.x+Math.cos(u.a)*sp*dt,ny=u.y+Math.sin(u.a)*sp*dt;
 const tt=T[clamp(Math.floor(ny/TS),0,MH-1)*MW+clamp(Math.floor(nx/TS),0,MW-1)];
 if(u.t<=0||isSolid(Math.floor(nx/TS),Math.floor(ny/TS))||tt===RD||tt===DK&&!onlyWalk){u.a=rf(0,6.283);u.t=rf(.8,3);return;}
 u.x=nx;u.y=ny;u.walk=(u.walk||0)+sp*dt*.15;
 if(u.hx0!==undefined&&Math.hypot(u.x-u.hx0,u.y-u.hy0)>200){u.a=Math.atan2(u.hy0-u.y,u.hx0-u.x);u.t=1;}
}
function pedsUpdate(dt){
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 peds.forEach(p=>{
  if(p.snow){if(p.wob>0)p.wob-=dt;if(p.melt!==undefined)p.melt-=dt;return;}
  if(p.st==='lie')return;
  if(campPed(p,dt)||poloPed(p,dt)||pedExt(p,dt))return;
  if(p.st!=='walk'){
   p.stT-=dt;
   if(p.st==='race'){raceStep(p,dt);return;}
   if(p.st==='dazed'){p.a+=dt*6;if(p.stT<=0){p.st='angry';p.stT=2.5;addFx(p.x,p.y-14,'#!?*','#e5604d',1.2);}}
   else if(p.st==='angry'){
    const a=Math.atan2(p.y-py,p.x-px);p.a=a;
    const nx=p.x+Math.cos(a)*78*dt,ny=p.y+Math.sin(a)*78*dt;
    if(!isSolid(Math.floor(nx/TS),Math.floor(ny/TS))){p.x=nx;p.y=ny;p.walk+=dt*8;}
    if(p.stT<=0)p.st='walk';
   }
   else if(p.stT<=0)p.st='walk';
   return;
  }
  const d=Math.hypot(p.x-px,p.y-py);
  if(P.inCar&&d<70){p.a=Math.atan2(p.y-py,p.x-px);const nx=p.x+Math.cos(p.a)*100*dt,ny=p.y+Math.sin(p.a)*100*dt;if(!isSolid(Math.floor(nx/TS),Math.floor(ny/TS))){p.x=nx;p.y=ny;}}
  else wander(p,dt,p.sp,false);
 });
}
function copsUpdate(dt){
 const ill=illegal()>0&&wanted===0&&!P.hide;
 const sneak=P.inCar&&Math.abs(V.sp)>150?.6:1;
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 const watch=(c,r)=>{
  const d=Math.hypot(c.x-px,c.y-py);
  if(ill&&d<(r+G.heat*1.2)*sneak){c.alert=(c.alert||0)+dt;if(c.alert>1){c.alert=0;startWanted();}}
  else c.alert=Math.max(0,(c.alert||0)-dt);
 };
 cops.forEach(c=>{wander(c,dt,c.sp,false);watch(c,130);});
 traffic.forEach(c=>{if(c.cop)watch(c,150);});
}
function chasersUpdate(dt){
 if(wanted<=0)return;
 if(P.hide){hideChase(dt);return;}
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 let minD=1e9,touch=false;
 chasers.forEach(u=>{
  const car=u.kind==='car';
  chaseStep(u,car?205+wanted*10:92,dt,car?12:7);
  const d=Math.hypot(u.x-px,u.y-py);minD=Math.min(minD,d);
  if(d<(car?24:19)&&(car||!P.inCar||Math.abs(V.sp)<120))touch=true;
 });
 if(touch){bustT+=dt;if(bustT>.7){arrest();return;}}else bustT=Math.max(0,bustT-dt);
 if(inYard(px,py)){escapeT+=dt*3;}
 else if(minD>420)escapeT+=dt;else escapeT=Math.max(0,escapeT-dt*2);
 if(escapeT>7){endWanted('Du hast die Polizei abgeschüttelt.');}
}
function thugsUpdate(dt){
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y;
 const val=cargoVal();
 thugs.forEach(u=>{
  u.stun=Math.max(0,u.stun-dt);
  if(u.ko>0){u.ko-=dt;if(u.ko<=0){u.st='idle';u.hp=2;u.x=u.hx0;u.y=u.hy0;}return;}
  const d=Math.hypot(u.x-px,u.y-py);
  if(u.loot){lootStep(u,dt,d,px,py);return;}
  if(u.st==='cool'){u.cool-=dt;if(u.cool<=0)u.st='idle';else if(Math.hypot(u.x-u.hx0,u.y-u.hy0)>30){const a=Math.atan2(u.hy0-u.y,u.hx0-u.x);moveE(u,Math.cos(a)*80*dt,Math.sin(a)*80*dt,8);u.a=a;}return;}
  if(u.st==='idle'){
   wander(u,dt,34,false);
   if(d<170&&(val>=150||G.cash>600)&&wanted===0&&!inYard(px,py)){u.st='chase';u.chaseT=0;if(Math.hypot(P.x-u.x,P.y-u.y)<200&&!P.inCar)msgCb('Die Miesepeter haben dich entdeckt!');}
  }else if(u.st==='chase'){
   u.chaseT+=dt;
   if(u.stun<=0){
    if(u.chaseT>14||d>420){u.st='cool';u.cool=6;}
    else chaseStep(u,88,dt,8);
   }
   if(d<17&&u.stun<=0)mugging(u);
  }
 });
}
const PN=['Heinz','Gisela','Kevin','Mehmet','Luise','Dieter','Yasemin','Tobi','Birgit','Ali','Sabine','Jürgen','Chantal','Uwe','Fatma','Lars','Hannelore','Ömer'];
const PJ=['Büdchen-Stammgast','Hobby-Philosoph','Taubenflüsterer','Gartenzwerg-Sammler','Profi-Spaziergänger','Wolkenzähler','Kartoffelschäler im Ruhestand','Zeitreisender (sagt er)','Straßenmusiker ohne Instrument','Pfandflaschen-Experte','Freizeit-Detektiv','Sockenvertreter','Bio-Brotbäcker','Hundeflüsterer ohne Hund'];
const PCOL=['#c0392b','#2980b9','#27ae60','#f39c12','#8e44ad','#16a085','#d35400','#bdc3c7'];
function mkPed(x,y){return{x:x,y:y,a:rf(0,6.28),t:rf(.5,3),col:pick(PCOL),sp:rf(25,45),walk:0,hx:false,hy:false,like:chance(popLike()),st:'walk',stT:0,nm:pick(PN),jb:pick(PJ)};}
const AMN={dose:'Dose',stein:'Stein',schnee:'Schneeball',ei:'Ei',wasser:'Wasserpistole'};
const HITL={dose:['DONG!','Meine Dose!','Das war Pfand!'],stein:['AUA!','Mein Zeh!','Ein Stein!'],schnee:['PFFF!','Kalt!','Schneeballschlacht!'],ei:['Platsch!','Platsch!','Platsch!']};
const BEERL=['Ahh, schön kühl.','Prost, Pflanze!','Das schmeckt nach Sommer.','Ein Schluck für die Tauben.','Hopfen, du Gute.','Klingt nach Feierabend.'];
const SMOKEL=['Puh ... alles ein bisschen weicher.','Die Welt hat plötzlich eine bessere Auflösung.','Deine Hände sind faszinierend.','Der Rauch macht Schleifen. Hübsch.'];
const THOUGHTS=['Was, wenn Enten eigentlich kleine Boote sind?','Pixel sind auch nur Quadrate mit Träumen.','Die Bank flüstert: Sitz.','Warum heißt Kölsch eigentlich Kölsch?','Dein Schatten hat eine Gehaltserhöhung verdient.','Wolken sind Gedanken vom Himmel.','Eine Taube nickt dir respektvoll zu.','Alles ist ein bisschen weicher.','Sind Bäume eigentlich Fans von Erde?'];
const HIL=['Doppel-High-Five! Ihr zwei versteht euch.','Er strahlt und klatscht gleich nochmal.','Klatsch! Das war ein Profi-High-Five.'];
const HIN=['Ein höfliches High Five. Immerhin.','Klatsch! Kurz, trocken, ehrlich.','Ein zaghaftes Abklatschen. Man kennt sich noch nicht.'];
const WXMSG={rain:'Es fängt an zu regnen. Die Laune sinkt, der Schirm fehlt.',snow:'Wintereinbruch! Mitten in der Stadt. Schneebälle gefällig?',heat:'Hitzewelle! Ein kühles Bier wäre jetzt perfekt.',sun:'Die Sonne kommt raus. Die Welt wird freundlicher.'};
const WXC={type:'sun',t:75};
const WP=[];for(let i=0;i<150;i++)WP.push({x:Math.random(),y:Math.random(),s:.6+Math.random()*.8});
let thT=8,splashT=0,noGoIn=null,eruptT2=0;
function wxType(){return ZONE?ZONE.wx:WXC.type;}
function wxLabel(){if(ZONE)return ZONE.title.toUpperCase();const w=WXC.type;return w==='rain'?'REGEN':w==='snow'?'SCHNEE':w==='heat'?'HITZE':'';}
function wxUpdate(dt){
 if(ZONE)return;
 WXC.t-=dt;
 if(WXC.t<=0){
  const r=Math.random();let n=r<.4?'sun':r<.65?'rain':r<.82?'snow':'heat';
  if(n===WXC.type)n='sun';
  WXC.type=n;WXC.t=rf(45,95);
  msgCb(WXMSG[n]);
 }
 if(WXC.type==='rain'&&flash<=0&&chance(dt*.03)){flash=.7;sfx('thunder');boltStrike();addFx(P.x+rf(-100,100),P.y-30,'BUMM!','#fff3a0',1.2);}
 if(flash>0)flash=Math.max(0,flash-dt*2);
}
function inNoGo(x,y){if(ZONE){const q=ZONE.nogo;return q&&x>q.x0&&x<q.x1&&y>q.y0&&y<q.y1?q:null;}for(let i=0;i<NOGO.length;i++){const n=NOGO[i];if(x>n.x0&&x<n.x1&&y>n.y0&&y<n.y1)return n;}return null;}
function addFx(x,y,txt,col,life,vy){FX.push({x:x,y:y,vx:rf(-8,8),vy:vy===undefined?-26:vy,t:0,life:life||1.3,txt:txt,col:col||'#fff'});}
function smokeFx(x,y){FX.push({x:x+rf(-3,3),y:y,vx:rf(-6,6),vy:-18,t:0,life:rf(1.2,2),sm:1,r:rf(3,6)});}
function mood(v,why){G.mood=clamp(G.mood+v,0,100);if(why)addFx(P.x,P.y-18,why,v>=0?'#6bcf63':'#e5604d');}
function moodWord(){const m=G.mood;return m>=85?'Euphorisch':m>=65?'Gut drauf':m>=45?'Okay':m>=25?'Mies drauf':'Auf 180';}
function fxUpdate(dt){
 for(let i=FX.length-1;i>=0;i--){const f=FX[i];f.t+=dt;f.x+=f.vx*dt;f.y+=f.vy*dt;if(f.g)f.vy+=f.g*dt;if(f.t>=f.life)FX.splice(i,1);}
 if(FX.length>170)FX.splice(0,FX.length-170);
}
function moodTick(dt){
 const w=wxType();
 let d=(55-G.mood)*.01;
 if(w==='rain')d-=.25;else if(w==='heat')d-=.12;else if(w==='sun'&&G.mood<70)d+=.05;
 if(ZONE)d+=ZONE.moodGain;
 if(P.sit&&!inNoGo(P.x,P.y))d+=.5;
 if(G.high>0){G.high-=dt;d+=.1;thT-=dt;if(thT<=0){thT=rf(10,16);toast(pick(THOUGHTS));}if(P.sit&&chance(dt*2))smokeFx(P.x,P.y-6);}
 G.drunk=Math.max(0,G.drunk-dt/45);
 G.mood=clamp(G.mood+d*dt,0,100);
 if(P.dance>0)P.dance-=dt;
 const ng=inNoGo(P.x,P.y);
 if(ng&&!noGoIn){toast(ng.n.charAt(0).toUpperCase()+ng.n.slice(1)+': Kein Alkohol, kein Rauch, keine Prügelei. Hier spielen Kinder!');}
 noGoIn=ng;
}
function kidsUpdate(dt){
 kids.forEach(k=>{
  k.t-=dt;
  const nx=k.x+Math.cos(k.a)*28*dt,ny=k.y+Math.sin(k.a)*28*dt,r=k.z;
  if(k.t<=0||nx<r.x0+12||nx>r.x1-12||ny<r.y0+12||ny>r.y1-12||isSolid(Math.floor(nx/TS),Math.floor(ny/TS))){k.a=rf(0,6.283);k.t=rf(.6,2);return;}
  k.x=nx;k.y=ny;k.walk+=dt*5;
 });
}
function bfsField(sx,sy,F){
 F.fill(-1);
 const q=new Int32Array(MW*MH);let h=0,t=0;
 const s=clamp(sy,0,MH-1)*MW+clamp(sx,0,MW-1);
 F[s]=0;q[t++]=s;
 while(h<t){
  const c=q[h++],cx=c%MW,cy=(c-cx)/MW,d=F[c]+1;
  if(cx>0&&F[c-1]<0&&!isSolid(cx-1,cy)){F[c-1]=d;q[t++]=c-1;}
  if(cx<MW-1&&F[c+1]<0&&!isSolid(cx+1,cy)){F[c+1]=d;q[t++]=c+1;}
  if(cy>0&&F[c-MW]<0&&!isSolid(cx,cy-1)){F[c-MW]=d;q[t++]=c-MW;}
  if(cy<MH-1&&F[c+MW]<0&&!isSolid(cx,cy+1)){F[c+MW]=d;q[t++]=c+MW;}
 }
}
function raceStep(p,dt){
 if(!RACE||RACE.p!==p){p.st='walk';return;}
 const F=RACE.field,cx=clamp(Math.floor(p.x/TS),0,MW-1),cy=clamp(Math.floor(p.y/TS),0,MH-1),cur=F[cy*MW+cx];
 let tx=RACE.gx,ty=RACE.gy;
 if(cur>0){
  let best=cur,bx=-1,by=-1;
  [[1,0],[-1,0],[0,1],[0,-1]].forEach(o=>{const nx=cx+o[0],ny=cy+o[1];if(nx<0||ny<0||nx>=MW||ny>=MH)return;const f=F[ny*MW+nx];if(f>=0&&f<best){best=f;bx=nx;by=ny;}});
  if(bx>=0){tx=bx*TS+16;ty=by*TS+16;}
 }
 const dx=tx-p.x,dy=ty-p.y,l=Math.hypot(dx,dy)||1;
 p.a=Math.atan2(dy,dx);
 moveE(p,dx/l*RACE.sp*dt,dy/l*RACE.sp*dt,7);
 p.walk+=RACE.sp*dt*.15;
}
function startRace(p){
 if(RACE)return{ok:false,msg:'Du rennst schon.'};
 if(wanted>0)return{ok:false,msg:'Mit der Polizei im Nacken? Lieber nicht.'};
 bfsField(Math.floor(P.x/TS),Math.floor(P.y/TS),FLOW);
 const cand=[];
 for(let j=1;j<MH-1;j++)for(let i=1;i<MW-1;i++){
  const d=FLOW[j*MW+i],t=T[j*MW+i];
  if(d>=14&&d<=24&&t!==RD&&t!==DP&&t!==SH&&t!==DK&&!inNoGo(i*TS+16,j*TS+16))cand.push([i,j]);
 }
 if(!cand.length)return{ok:false,msg:'Hier ist kein Platz für ein Rennen.'};
 const g=pick(cand);
 RACE={p:p,gx:g[0]*TS+16,gy:g[1]*TS+16,t:0,max:36,sp:rf(90,102),field:new Int16Array(FLOW.length)};
 bfsField(g[0],g[1],RACE.field);
 p.st='race';p.stT=999;
 return{ok:true,msg:'Wettrennen gegen '+p.nm+'! Wer zuerst am Ring ist, gewinnt.'};
}
function endRace(msg,dm,col){
 if(RACE){RACE.p.st='wait';RACE.p.stT=2;}
 RACE=null;
 mood(dm,dm>0?'+'+dm:'');
 toast(msg);
}
function raceUpdate(dt){
 if(!RACE)return;
 RACE.t+=dt;
 const px=P.inCar?V.x:P.x,py=P.inCar?V.y:P.y,p=RACE.p;
 if(Math.hypot(px-RACE.gx,py-RACE.gy)<30){G.resp++;endRace('GEWONNEN! '+p.nm+' japst noch. +1 Respekt.',12);}
 else if(Math.hypot(p.x-RACE.gx,p.y-RACE.gy)<30)endRace(p.nm+' war schneller. Ein fairer Verlust, ein knallroter Kopf.',3);
 else if(RACE.t>RACE.max)endRace('Das Rennen ist unentschieden verlaufen. Beide sind irgendwo falsch abgebogen.',4);
 else if(wanted>0)endRace('Rennen abgebrochen. Die Polizei hat andere Pläne.',0);
}
function curAmmo(){const o=['schnee','stein','dose','ei'];if(G.sel==='wasser'&&G.pistol)return 'wasser';if(G.sel&&G.sel!=='wasser'&&G.ammo[G.sel]>0)return G.sel;for(let i=0;i<4;i++)if(G.ammo[o[i]]>0)return o[i];return G.pistol?'wasser':'';}
function copNear(x,y,r){
 if(ZONE)return false;
 return cops.some(c=>Math.hypot(c.x-x,c.y-y)<r)||traffic.some(c=>c.cop&&Math.hypot(c.x-x,c.y-y)<r);
}
function throwIt(){
 const t=curAmmo();if(!t)return false;
 if(t==='wasser')return shootWater();
 if(inNoGo(P.x,P.y)){toast(ZONE&&ZONE.name==='fpark'?'Im Freizeitpark wird nichts geworfen, höchstens beim Dosenwerfen!':'Auf dem Spielplatz wird nichts geworfen!');return true;}
 if(t==='ei'&&!(ZONE&&ZONE.name==='sender')){toast('Eier sind nur für die Senderkulissen gedacht.');return true;}
 let a=P.a;
 if(ZONE&&ZONE.name==='sender'){const st=senderTarget();if(st)a=Math.atan2(st.ty-P.y,st.tx-P.x);else toast('Geh näher an eine Kulisse heran.');}
 else{const best=aimBest(240,false);if(best)a=Math.atan2(best.y-P.y,best.x-P.x);}
 G.ammo[t]--;P.a=a;
 PR.push({x:P.x,y:P.y,vx:Math.cos(a)*340,vy:Math.sin(a)*340,t:0,type:t});
 sfx('throw');
 return true;
}
function dropAmmo(b){
 if(b.type==='ei'){addFx(b.x,b.y,'Platsch!','#ffe08a',.8);return;}
 if(b.type==='schnee'){addFx(b.x,b.y,'Pfff!','#e6f3ff',.8);return;}
 PICKS.push({x:b.x,y:b.y,t:b.type});
}
function hitPed(p,b){
 if(p.snow){p.wob=.7;addFx(p.x,p.y-26,b.type==='schnee'?'Brrr!':'Klonk!','#cfe9ff');mood(3,'+Spaß');sfx('crunch');p.hp=(p.hp||0)+1;if(p.hp>=3)toppleSnow(p,false);return;}
 p.st='dazed';p.stT=2;addFx(p.x,p.y-16,pick(HITL[b.type]),'#ffd23f');sfx('hit');
 for(let i=0;i<3;i++)FX.push({x:p.x,y:p.y-8,vx:rf(-30,30),vy:rf(-40,-10),t:0,life:.9,txt:'★',col:'#ffd23f'});
 if(RACE&&RACE.p===p)RACE=null;
 if(p.like){p.st='laugh';p.stT=2;addFx(p.x,p.y-28,'Haha, gut!','#6bcf63');mood(5,'+5');}
 else if(G.mood<50)mood(7,'Das tat gut');
 else mood(2);
}
function hitCop(c){
 addFx(c.x,c.y-16,'Ey!','#ffd23f');heat(10);if(c.alert!==undefined)c.alert=1.1;
 if(wanted===0&&!ZONE&&chance(.55))startWanted('Du hast einen Polizisten getroffen! Lauf!');
}
function projUpdate(dt){
 for(let i=PR.length-1;i>=0;i--){
  const b=PR[i];if(b.type==='wasser'){if(waterProj(b,dt))PR.splice(i,1);continue;}b.t+=dt;
  const nx=b.x+b.vx*dt,ny=b.y+b.vy*dt,tx=Math.floor(nx/TS),ty=Math.floor(ny/TS);
  let done=false;
  const tt=tget(tx,ty);
  if(tt===LV){addFx(nx,ny,'Zisch!','#ff8040',.9);done=true;}
  else if(tt===DP||tt===SH){addFx(nx,ny,'Platsch!','#9fd8ff',.9);done=true;}
  else if(isSolid(tx,ty)){if(!(ZONE&&ZONE.name==='sender'&&senderHit(b,nx,ny,tx,ty)))dropAmmo(b);done=true;}
  else if(b.type!=='ei'){
   for(let k=0;k<peds.length&&!done;k++){const p=peds[k];if(Math.hypot(p.x-nx,p.y-ny)<(p.snow?13:11)){hitPed(p,b);dropAmmo(b);done=true;}}
   for(let k=0;k<cops.length&&!done;k++){const c=cops[k];if(Math.hypot(c.x-nx,c.y-ny)<11){hitCop(c);dropAmmo(b);done=true;}}
   for(let k=0;k<traffic.length&&!done;k++){const c=traffic[k];if(Math.hypot(c.x-nx,c.y-ny)<17){addFx(c.x,c.y-14,'HUPP!','#ffd23f',1);if(c.cop)hitCop(c);dropAmmo(b);done=true;}}
   for(let k=0;k<thugs.length&&!done;k++){const u=thugs[k];if(u.ko<=0&&Math.hypot(u.x-nx,u.y-ny)<12){u.stun=1;addFx(u.x,u.y-16,'Hä?!','#ff8a65');dropAmmo(b);done=true;}}
  }
  if(!done&&b.t>.85){dropAmmo(b);done=true;}
  if(done)PR.splice(i,1);else{b.x=nx;b.y=ny;}
 }
}
function spawnPick(init){
 const ty=pick(ZONE?ZONE.pickTypes:['dose','dose','stein']);
 let p=null;
 if(ZONE){
  for(let k=0;k<60;k++){
   const x=rnd(2,MW-3),y=rnd(2,MH-3);
   if(ZONE.walk.indexOf(T[y*MW+x])>=0){const px=x*TS+16,py=y*TS+16;if(init||Math.hypot(px-P.x,py-P.y)>260){p={x:px,y:py};break;}}
  }
  if(!p)return;
 }else{
  p=ty==='stein'?randTile([GR],init?0:260,init?0:2000,init?undefined:P.x,init?undefined:P.y):randTile([SW,GR],init?0:260,init?0:2000,init?undefined:P.x,init?undefined:P.y);
  if(p.x===GATE.x&&p.y===GATE.y)return;
  if(inNoGo(p.x,p.y))return;
 }
 PICKS.push({x:p.x+rf(-9,9),y:p.y+rf(-9,9),t:ty});
}
function picksUpdate(dt){
 if(!P.inCar&&!P.sit){
  for(let i=PICKS.length-1;i>=0;i--){
   const k=PICKS[i];
   if(Math.hypot(k.x-P.x,k.y-P.y)<15&&G.ammo[k.t]<(k.t==='dose'?40:9)){
    G.ammo[k.t]++;PICKS.splice(i,1);addFx(P.x,P.y-16,'+'+AMN[k.t],'#cfe9ff');
    if(!tipShown){tipShown=true;toast('Aufgehoben! OK wirft es auf Passanten. Im Rucksack wählst du, was.');}
   }
  }
 }
 pickT-=dt;
 if(pickT<=0){pickT=9;if(PICKS.length<(ZONE?ZONE.pickCap:litterCap()))spawnPick(false);}
 const snowy=wxType()==='snow'||(ZONE&&ZONE.name==='berge');
 G.snowT=(G.snowT||0)+dt;
 if(snowy){if(G.snowT>1.2){G.snowT=0;if(G.ammo.schnee<6)G.ammo.schnee++;}}
 else if(G.snowT>8){G.snowT=0;if(G.ammo.schnee>0){G.ammo.schnee--;if(G.ammo.schnee===0)toast('Deine Schneebälle sind geschmolzen.');}}
}
function nearPed(){
 if(P.inCar||P.sit||P.ride||P.build)return null;
 let b=null,bd=36;
 peds.forEach(p=>{if(p.snow||(p.st!=='walk'&&p.st!=='lie'))return;const d=Math.hypot(p.x-P.x,p.y-P.y);if(d<bd){bd=d;b=p;}});
 return b;
}
function nearSeat(){
 if(P.inCar||P.sit||P.ride||P.build)return null;
 const tx=Math.floor(P.x/TS),ty=Math.floor(P.y/TS);let b=null,bd=46;
 for(let j=ty-2;j<=ty+2;j++)for(let i=tx-2;i<=tx+2;i++){
  const t=tget(i,j);if(t!==BK&&t!==LC)continue;
  const x=i*TS+16,y=j*TS+16,d=Math.hypot(x-P.x,y-P.y);
  if(d<bd){bd=d;b={tx:i,ty:j,x:x,y:y,t:t};}
 }
 return b;
}
function freeSpot(x,y){
 if(!hit(x,y,7))return{x:x,y:y};
 for(let r=16;r<=140;r+=12)for(let k=0;k<12;k++){const a=k/12*6.283,nx=x+Math.cos(a)*r,ny=y+Math.sin(a)*r;if(!hit(nx,ny,7))return{x:nx,y:ny};}
 return{x:x,y:y};
}
function sitDown(s){
 P.sit=s;P.x=s.x;P.y=s.y;P.vx=P.vy=0;P.a=Math.PI/2;
 keys.left=keys.right=keys.up=keys.down=0;
 sfx('sit');show('sit');
}
function standUp(){
 if(!P.sit)return;
 const s=P.sit;P.sit=null;
 const q=freeSpot(s.x,s.y+30);
 P.x=q.x;P.y=q.y;P.vx=P.vy=0;
}
function noUse(){const n=inNoGo(P.x,P.y);if(n)return 'Hier ist '+n.n+': Kein Alkohol, kein Rauch!';if(minorNear(P.x,P.y,120))return 'Jugendschutz: Nicht vor Kindern und Jugendlichen!';return '';}
function doDrink(){
 const w=noUse();if(w){toast(w);return false;}
 if(G.stock.bier<1){toast('Kein Bier mehr. Das Büdchen hat Nachschub.');return false;}
 G.stock.bier--;G.drunk+=1;sfx('glug');needAdd(0,20);
 mood(6+(wxType()==='heat'?3:0),'Prost!');
 toast(pick(BEERL));
 if(G.drunk>=6)blackout();
 return true;
}
function doSmoke(){
 const w=noUse();if(w){toast(w);return false;}
 if(G.stock.joint<1){toast('Kein Joint mehr. Das Büdchen hat Nachschub.');return false;}
 G.stock.joint--;G.high=Math.min(150,G.high+50);mood(8,'Puh ...');sfx('puff');
 for(let i=0;i<7;i++)smokeFx(P.x,P.y-8);
 if(!inYard(P.x,P.y)&&copNear(P.x,P.y,170)&&chance(.6)){
  const f=Math.min(G.cash,30);G.cash-=f;mood(-5);
  toast('Ordnungsamt: '+eur(f)+' Verwarngeld fürs Kiffen in der Öffentlichkeit. Ein Blick, eine Rechnung.');
  return true;
 }
 toast(pick(SMOKEL));
 if(G.teaT>0)mood(6,'Tee & Joint!');
 if(!(ZONE&&ZONE.name==='wal')&&chance(.22))tripWarp('Du schließt kurz die Augen ... und machst sie woanders wieder auf.');
 return true;
}
function startFade(txt,cb){sfx('warp');fade={t:0,dur:2.2,txt:txt,cb:cb,done:false};keys.left=keys.right=keys.up=keys.down=0;}
function pickZone(not){
 const m=G.mood,w={strand:m>=65?6:1.2,vulkan:m<=35?6:1,berge:2.2,hoehle:2.2,amsterdam:1.6,maerchen:1.8,schlaraff:1.2,bayern:1.4,portugal:1.4,wuppertal:1.4,oesterreich:1.4,koeln:1.4,feldweg:1.6,sender:1.4,helden:1.4,amt:1.4,fpark:1.6,malle:1.6};
 if(not)delete w[not];
 let s=0;for(const k in w)s+=w[k];
 let r=Math.random()*s;
 for(const k in w){r-=w[k];if(r<=0)return k;}
 return 'strand';
}
function tripWarp(txt){
 if(P.sit)standUp();
 if(P.ride)leaveRide(true);
 closeAll();
 const to=ZONE&&chance(.4)?null:pickZone(ZONE?ZONE.name:null);
 if(!ZONE)G.ret={x:P.x,y:P.y};
 startFade(txt,()=>{if(to)enterZone(to);else leaveZone(false);});
}
function blackout(){
 G.drunk=3;
 tripWarp('Dir wird kurz schwarz vor Augen ... Prost, Mahlzeit. Du wachst irgendwo anders auf, mit Sonnenbrille und ohne Erinnerung.');
}
function usePortal(mk){
 if(P.inCar){toast('Steig erst aus dem Van aus.');return;}
 if(P.ride){toast('Steig erst ab.');return;}
 if(fade)return;
 if(mk.home&&ZONE&&['bayern','portugal','wuppertal','oesterreich','koeln','gallien','camping','holly'].indexOf(ZONE.name)>=0){UI.euroFrom='';show('euro');return;}
 if(mk.home){startFade(mk.warp,()=>leaveZone(false));return;}
 if(mk.to){if(!ZONE)G.ret={x:mk.x,y:mk.y};startFade(mk.warp,()=>enterZone(mk.to));return;}
 const dest=pickZone(ZONE?ZONE.name:null);
 if(!ZONE)G.ret={x:mk.x,y:mk.y+32};
 let why='';
 if(dest==='strand'&&G.mood>=65)why=' Deine gute Laune zieht dich an den Strand!';
 else if(dest==='vulkan'&&G.mood<=35)why=' Mit dieser Laune geht es zum Vulkan. Dampf ablassen!';
 startFade(mk.warp+why,()=>enterZone(dest));
}
function useWorld(w){T=w.T;MW=w.MW;MH=w.MH;WC=w.WC;MM=w.MM;BLD=w.BLD;MKS=w.MKS;}
function enterZone(name){
 if(G&&G.ammo&&name!=='sender'){G.ammo.ei=0;if(G.sel==='ei')G.sel='';}
 let z=WORLDS[name];
 if(!z){z=genZone(name);renderZone(z);WORLDS[name]=z;}
 if(!ZONE)CITYENT={traffic:traffic,peds:peds,cops:cops,thugs:thugs,chasers:chasers,kids:kids,picks:PICKS,rides:RIDES};
 if(RACE){RACE.p.st='walk';RACE=null;}
 ZONE=z;useWorld(z);skEnter(z);
 traffic=[];cops=[];thugs=[];chasers=[];kids=[];peds=zonePeds(z);PICKS=[];RIDES=z.rides;CAS=[];P.ride=null;P.build=null;P.coast=null;MG=null;campEnd(true);fireReset();POLO=null;P.fish=null;P.fight=null;G.wet=0;
 for(let i=0;i<10;i++)spawnPick(true);
 PR=[];FX=[];wanted=0;escapeT=0;bustT=0;
 P.x=z.spawn.x;P.y=z.spawn.y;P.vx=P.vy=0;P.inCar=false;P.sit=null;
 if(z.spawnRide){const R=z.rides[0];R.x=z.spawn.x;R.y=z.spawn.y;R.a=0;R.sp=0;P.ride=R;}
 sfx('arrive');
 cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
 UI.hudS=null;UI.trkS=null;
 renderMini();
 toast(z.title+': '+z.hint);
}
function leaveZone(silent){
 if(!ZONE)return;
 if(G&&G.ammo){G.ammo.ei=0;if(G.sel==='ei')G.sel='';}
 if(RACE){RACE.p.st='walk';RACE=null;}
 ZONE=null;useWorld(CITY);
 traffic=CITYENT.traffic;peds=CITYENT.peds;cops=CITYENT.cops;thugs=CITYENT.thugs;chasers=CITYENT.chasers;kids=CITYENT.kids;PICKS=CITYENT.picks;RIDES=CITYENT.rides;CAS=[];P.ride=null;P.build=null;P.coast=null;MG=null;campEnd(true);fireReset();POLO=null;
 PR=[];FX=[];wanted=0;chasers=[];escapeT=0;bustT=0;
 const r=G.ret||{x:GATE.x,y:GATE.y},q=freeSpot(r.x,r.y);
 P.x=q.x;P.y=q.y;P.vx=P.vy=0;P.inCar=false;P.sit=null;
 cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
 UI.hudS=null;UI.trkS=null;
 renderMini();
 if(!(V.x>TS&&V.y>TS&&V.x<MW*TS-TS&&V.y<MH*TS-TS)||hit(V.x,V.y,12)){V.x=VAN0.x;V.y=VAN0.y;V.a=0;V.sp=0;}
 if(!silent)toast('Zurück in Rheinhanfen. Alles beim Alten, nur du bist besser drauf.');
}
function toCity(){if(ZONE)leaveZone(true);}
function zonePeds(z){
 const out=[];
 const rt=types=>{for(let k=0;k<200;k++){const x=rnd(2,ZW-3),y=rnd(2,ZH-3);if(types.indexOf(z.T[y*ZW+x])>=0)return{x:x*TS+16,y:y*TS+16};}return null;};
 const add=(n,types,fn)=>{for(let i=0;i<n;i++){const p=rt(types);if(!p)continue;const q=mkPed(p.x,p.y);if(fn)fn(q);out.push(q);}};
 if(z.name==='strand'){add(4,[SA,SH],q=>{q.gun=chance(.55);q.gc=pick(GUNC);});strandKids(z,out);add(5,[SA],q=>{q.st='lie';q.stT=1e9;q.tw=pick(['#e5604d','#2e86c1','#f1c40f','#27ae60','#8e44ad']);});}
 else if(z.name==='vulkan'){add(4,[AS]);}
 else if(z.name==='berge'){add(4,[SN,IC]);[[14,12],[28,11],[40,16]].forEach(s=>{const q=mkPed(s[0]*TS+16,s[1]*TS+16);q.snow=true;q.hp=0;out.push(q);});}
 else if(z.name==='hoehle')add(3,[CF]);else if(z.name==='wal'){let ji=0;add(3,[CF],q=>{if(ji++===0){q.nm='Jonas';q.jb='Wohnt hier. Seit Kurzem. Oder seit der Bibel.';}});}else if(z.name==='maerchen')add(3,[GR,SW]);else if(z.name==='schlaraff')add(4,[GR]);else if(z.name==='bayern')add(7,[GR]);else if(z.name==='portugal')add(8,[SW,SA]);else if(z.name==='wuppertal')add(8,[SW]);else if(z.name==='oesterreich')add(6,[GR]);else if(z.name==='koeln')add(10,[SW]);else if(z.name==='feldweg')add(4,[GR,SA]);else if(z.name==='sender')add(4,[SW]);else if(z.name==='helden')add(3,[SW]);else if(z.name==='amt')add(4,[SW]);else if(z.name==='rhein')add(5,[GR]);else if(z.name==='amsterdam')add(10,[SW],q=>{if(chance(.5))q.col='#ff7a1a';});else if(z.name==='fpark'){add(8,[SW],q=>{if(chance(.35))q.bal=pick(BALC);});add(7,[SW],q=>{q.kid=true;q.nm=pick(['Lena','Ben','Mia','Emil','Finn','Lotta','Ole','Paul']);q.jb=pick(['Achterbahn-Fan','Zuckerwatte-Expertin','Karussell-Kapitän','Autoscooter-Profi','Riesenrad-Winkerin']);q.like=chance(.5);q.sp=rf(35,55);if(chance(.6))q.bal=pick(BALC);});}else if(z.name==='malle')mallePeds(z,add);else if(z.name==='zoo')add(8,[SW]);else if(z.name==='freibad')add(6,[GR]);else if(z.name==='camping')add(7,[GR,SW]);else if(z.name==='gallien')add(2,[SW]);
 return out;
}
function zoneUpdate(dt){
 if(!ZONE)return;
 if(ZONE.name==='vulkan'){
  eruptT-=dt;
  if(eruptT<=0){
   eruptT=rf(18,30);shake=1;sfx('rumble');toast('RUMMS! Der Vulkan hustet.');
   for(let i=0;i<9;i++)FX.push({x:P.x+rf(-240,240),y:P.y+rf(-120,140),vx:rf(-20,20),vy:rf(-130,-70),g:280,t:0,life:1.3,dot:'#ff7a1a',r:rf(3,6)});
  }
 }
 if(ZONE.name==='hoehle'&&chance(dt*.35)){const l=chance(.5);FX.push({x:P.x+(l?-360:360),y:P.y+rf(-110,110),vx:(l?1:-1)*rf(90,140),vy:rf(-15,15),t:0,life:5,bat:1});}
}
function doScream(mk){
 if(mk.cd>0){toast('Der Stein ist noch heiser. Gleich nochmal.');return;}
 mk.cd=18;shake=1.2;sfx('scream');
 addFx(P.x,P.y-24,'AAAAAAAH!!!','#ff6a4a',2,-20);
 for(let i=0;i<10;i++)FX.push({x:P.x+rf(-80,80),y:P.y+rf(-50,50),vx:rf(-40,40),vy:rf(-140,-60),g:260,t:0,life:1.2,dot:'#ff7a1a',r:rf(3,5)});
 if(G.mood<50){G.mood=Math.min(100,G.mood+28);toast('Das hat gut getan! Die Wut ist weg.');}
 else{mood(6);toast('Du brüllst den Berg an. Der Berg brüllt zurück.');}
}
function doDisco(mk){
 if(mk.cd>0){toast('Die Discokugel braucht eine Verschnaufpause.');return;}
 mk.cd=14;P.dance=6;mood(10,'+10 ♪');sfx('disco');
 for(let i=0;i<8;i++)addFx(P.x+rf(-30,30),P.y+rf(-30,10),pick(['♪','♫','★']),pick(['#ff5fd0','#5ff0ff','#ffd23f']),1.6,-30);
 toast('Du tanzt, als würde niemand zusehen. Die Fledermäuse sehen aber zu.');
}
let flowAge=9;
function update(dt){
 if(!G)return;
 flowAge+=dt;fdt=dt;
 G.t+=dt;
 if(G.t>=DAY_S){G.t-=DAY_S;const L=newDay(false);msgCb('Tag '+G.day+' beginnt. '+(L[0]||''));saveAll();checkWin();}
 if(P.sit&&(wanted>0||P.stun>0)){standUp();closeAll();}
 const sitting=!!P.hide||!!P.sit||!!P.build||!!P.fish||!!P.fight||!!P.coast||!!MG;
 const ax=sitting?0:(keys.right?1:0)-(keys.left?1:0),ay=sitting?0:(keys.down?1:0)-(keys.up?1:0);
 P.stun=Math.max(0,P.stun-dt);
 if(P.ride){rideDrive(dt,ax,ay);}
 else if(P.inCar){if(ZONE){P.inCar=false;V.sp=0;}else{drive(dt,ax,ay);P.x=V.x;P.y=V.y;}}
 else if(!sitting){
  const load=used()/cap();
  const wet=tget(Math.floor(P.x/TS),Math.floor(P.y/TS))===SH;
  const sp=FOOT*(1-.35*load)*(P.stun>0?.3:1)*(wet?.6:1)*(isDeep(P.x,P.y)?.55:1)*(G.high>0?.88:1)*(P.heroT>0?1.3:1)*(P.fast>0?1.7:1)*((G.hun===0||G.dur===0)?.85:1);
  let tx=ax,ty=ay;const l=Math.hypot(tx,ty);
  if(l>0){
   tx=tx/l*sp;ty=ty/l*sp;P.a=Math.atan2(ty,tx);
   if(G.drunk>=2){const k=(G.drunk-1)*13;tx+=Math.sin(timeNow*2.3)*k;ty+=Math.cos(timeNow*1.9)*k;}
  }
  P.vx+=(tx-P.vx)*Math.min(1,dt*14);P.vy+=(ty-P.vy)*Math.min(1,dt*14);
  moveE(P,P.vx*dt,P.vy*dt,7);pushOut(P,7);unstuckTick();
  P.walk+=Math.hypot(P.vx,P.vy)*dt*.12;
  if(wet&&l>0){splashT-=dt;if(splashT<=0){splashT=.25;addFx(P.x,P.y+4,'~','#9fd8ff',.6,-8);}}
 }
 if((wanted>0||thugs.some(u=>u.st==='chase'))&&flowAge>.3){computeFlow();flowAge=0;}
 trafficUpdate(dt);pedsUpdate(dt);copsUpdate(dt);chasersUpdate(dt);thugsUpdate(dt);
 kidsUpdate(dt);projUpdate(dt);picksUpdate(dt);raceUpdate(dt);moodTick(dt);wxUpdate(dt);fxUpdate(dt);zoneUpdate(dt);extUpdate(dt);
 MKS.forEach(m=>{if(m.cd>0)m.cd-=dt;});
 saveT+=dt;if(saveT>45&&wanted===0){saveT=0;saveAll();}
 const RR=P.ride;const tx=P.x+(P.inCar?Math.cos(V.a)*V.sp*.3:RR?Math.cos(RR.a)*RR.sp*.28:0)+(P.sit&&P.sit.t==='decke'&&UI.screen==='sit'?(P.x+300-VW/2<=MW*TS-VW?300:-330):0)-VW/2,ty=P.y+(P.inCar?Math.sin(V.a)*V.sp*.3:RR?Math.sin(RR.a)*RR.sp*.28:0)-VH/2;
 cam.x+=(tx-cam.x)*Math.min(1,dt*6);cam.y+=(ty-cam.y)*Math.min(1,dt*6);
 cam.x=camX(cam.x);cam.y=camY(cam.y);
}
function checkWin(){if(!G)return;const M=[15000,30000,60000,120000,250000,500000,1000000],i=G.mile||0;if(i<M.length&&worth()>=M[i]){G.mile=i+1;G.won=true;msgCb('__win:'+M[i]);}}
function nearMarker(){
 let b=null,bd=38;
 MKS.forEach(m=>{const d=Math.hypot(m.x-P.x,m.y-P.y);if(d<bd){bd=d;b=m;}});
 return b;
}
function nearVan(){return !ZONE&&!P.inCar&&Math.hypot(V.x-P.x,V.y-P.y)<56;}
function enterVan(){P.inCar=true;P.vx=P.vy=0;}
function exitVan(){
 const a=V.a+Math.PI/2;
 for(const s of[1,-1]){
  const x=V.x+Math.cos(a)*s*26,y=V.y+Math.sin(a)*s*26;
  if(!hit(x,y,7)){P.x=x;P.y=y;P.inCar=false;V.sp=0;return true;}
 }
 const x=V.x-Math.cos(V.a)*30,y=V.y-Math.sin(V.a)*30;
 if(!hit(x,y,7)){P.x=x;P.y=y;P.inCar=false;V.sp=0;return true;}
 return false;
}
function callVan(){
 if(ZONE)return{ok:false,msg:'Hier fährt kein Taxi. Wirklich nicht.'};
 if(P.inCar)return{ok:false,msg:'Du sitzt schon im Van.'};
 if(G.cash<25)return{ok:false,msg:'Der Fahrer will 25 € Trinkgeld.'};
 let best=null,bd=1e9;
 for(let j=0;j<MH;j++)for(let i=0;i<MW;i++){
  if(T[j*MW+i]!==RD)continue;
  const x=i*TS+16,y=j*TS+16,d=Math.hypot(x-P.x,y-P.y);
  if(d>60&&d<bd){bd=d;best=[x,y];}
 }
 if(!best)return{ok:false,msg:'Kein Platz für den Van gefunden.'};
 G.cash-=25;V.x=best[0];V.y=best[1];V.sp=0;V.a=0;
 return{ok:true,msg:'Der Van wartet an der nächsten Straße (-25 €).'};
}

function bcol(c,a){
 const n=parseInt(c.slice(1),16);let r=(n>>16)+a,g=((n>>8)&255)+a,b=(n&255)+a;
 r=clamp(r,0,255);g=clamp(g,0,255);b=clamp(b,0,255);
 return'rgb('+r+','+g+','+b+')';
}
let WC=document.createElement('canvas');WC.width=MW*TS;WC.height=MH*TS;
let MM=document.createElement('canvas');MM.width=304;MM.height=192;
const CITY={T:T,MW:MW,MH:MH,WC:WC,MM:MM,BLD:BLD,MKS:MKS};
function hash(x,y){return((x*73856093)^(y*19349663))>>>0;}
function renderWorld(){
 const c=WC.getContext('2d');
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  const t=T[y*MW+x],px=x*TS,py=y*TS,h=hash(x,y)&7;
  if(t===GR||t===TR||t===FN||t===PG||(t===BK&&!(tget(x-1,y)===SW||tget(x+1,y)===SW||tget(x,y-1)===SW||tget(x,y+1)===SW))){c.fillStyle=h<3?'#3f6b3a':h<6?'#437040':'#3a6336';c.fillRect(px,py,TS,TS);}
  else if(t===SD){c.fillStyle=h<4?'#e3cf8d':'#dbc47f';c.fillRect(px,py,TS,TS);}
  else if(t===RD){c.fillStyle='#3a3d42';c.fillRect(px,py,TS,TS);}
  else if(t===SW||t===BL||t===CR||t===BK){c.fillStyle=h<4?'#9d9d96':'#94948d';c.fillRect(px,py,TS,TS);c.strokeStyle='rgba(0,0,0,.08)';c.strokeRect(px+.5,py+.5,TS-1,TS-1);}
  else if(t===WT){c.fillStyle='#255d86';c.fillRect(px,py,TS,TS);if(h<3){c.fillStyle='rgba(255,255,255,.13)';c.fillRect(px+4+h*3,py+8+h*2,12,2);}}
  else if(t===FD){c.fillStyle='#7a9a3a';c.fillRect(px,py,TS,TS);c.fillStyle='#5f8530';for(let k=0;k<4;k++)c.fillRect(px,py+k*8+2,TS,3);}
  else if(t===DK){c.fillStyle='#8a6a44';c.fillRect(px,py,TS,TS);c.strokeStyle='#5f4529';for(let k=1;k<4;k++){c.beginPath();c.moveTo(px,py+k*8);c.lineTo(px+TS,py+k*8);c.stroke();}}
 }
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  if(T[y*MW+x]!==SW)continue;
  const px=x*TS,py=y*TS;c.fillStyle='rgba(255,255,255,.16)';
  if(tget(x,y-1)===RD)c.fillRect(px,py,TS,2);
  if(tget(x,y+1)===RD)c.fillRect(px,py+TS-2,TS,2);
  if(tget(x-1,y)===RD)c.fillRect(px,py,2,TS);
  if(tget(x+1,y)===RD)c.fillRect(px+TS-2,py,2,TS);
 }
 c.fillStyle='#d6cd8a';
 VR.forEach(v=>{const cx=(v+1)*TS-1;for(let y=0;y<MH*TS;y+=28){const ty=Math.floor(y/TS);if(HR.some(h=>ty===h||ty===h+1))continue;c.fillRect(cx,y+4,2,14);}});
 HR.forEach(h=>{const cy=(h+1)*TS-1;for(let x=6*TS;x<MW*TS;x+=28){const tx=Math.floor(x/TS);if(VR.some(v=>tx===v||tx===v+1))continue;c.fillRect(x+4,cy,14,2);}});
 c.fillStyle='rgba(255,255,255,.55)';
 VR.forEach(v=>HR.forEach(h=>{
  for(let k=0;k<4;k++){c.fillRect(v*TS+k*16+2,h*TS-10,10,8);c.fillRect(v*TS+k*16+2,(h+2)*TS+2,10,8);c.fillRect(v*TS-10,h*TS+k*16+2,8,10);c.fillRect((v+2)*TS+2,h*TS+k*16+2,8,10);}
 }));
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  const t=T[y*MW+x],px=x*TS,py=y*TS;
  if(t===CR){
   const cols=['#c0392b','#2e86c1','#27ae60','#d4a017','#7f8c8d'];
   c.fillStyle='rgba(0,0,0,.25)';c.fillRect(px+4,py+4,TS-2,TS-2);
   c.fillStyle=cols[hash(x,y)%5];c.fillRect(px+1,py+1,TS-3,TS-3);
   c.strokeStyle='rgba(0,0,0,.35)';c.strokeRect(px+1.5,py+1.5,TS-4,TS-4);
   for(let k=1;k<4;k++){c.beginPath();c.moveTo(px+k*8,py+2);c.lineTo(px+k*8,py+TS-3);c.stroke();}
  }else if(t===BK){drawBench(c,px,py);
  }else if(t===PG){drawPlay(c,px,py,hash(x,y)%3);
  }else if(t===FN){
   const l=tget(x-1,y)===FN,r=tget(x+1,y)===FN,u=tget(x,y-1)===FN,d=tget(x,y+1)===FN;
   c.fillStyle='#8c7b62';
   if(l||r)c.fillRect(px,py+TS/2-2,TS,4);
   if(u||d)c.fillRect(px+TS/2-2,py,4,TS);
   c.fillStyle='#5f5240';c.fillRect(px+TS/2-3,py+TS/2-3,6,6);
  }
 }
 drawSportsStatic(c);
 BLD.forEach(b=>drawBuilding(c,b));
 SIGNS.forEach(sg=>drawSign(c,sg));
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  if(T[y*MW+x]!==TR)continue;
  const px=x*TS+16,py=y*TS+16;
  c.fillStyle='rgba(0,0,0,.28)';c.beginPath();c.arc(px+4,py+5,14,0,6.283);c.fill();
  c.fillStyle='#2b5a2b';c.beginPath();c.arc(px,py,14,0,6.283);c.fill();
  c.fillStyle='#3d7a37';c.beginPath();c.arc(px-2,py-2,10,0,6.283);c.fill();
  c.fillStyle='#57a04b';c.beginPath();c.arc(px-4,py-4,5,0,6.283);c.fill();
 }
 const mc=MM.getContext('2d'),S=2.5;
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  const t=T[y*MW+x];
  mc.fillStyle=t===RD?'#555a62':t===BL?'#8a6a5a':t===WT?'#255d86':t===TR?'#2b5a2b':t===GR?'#3f6b3a':t===FD?'#7a9a3a':t===DK?'#8a6a44':t===CR?'#7f6f4f':t===BK?'#7a5a3a':t===PG?'#c06a3a':t===SD?'#d9c27a':'#9d9d96';
  mc.fillRect(x*S,y*S,S,S);
 }
 spMini(mc,S);
}
function drawBuilding(c,b){
 const x=b.x*TS,y=b.y*TS,w=b.w*TS,h=b.h*TS,hh=b.hh;
 c.fillStyle='rgba(0,0,0,.3)';c.fillRect(x+hh,y+hh,w,h);
 c.fillStyle=bcol(b.c,-55);c.fillRect(x,y,w,h);
 if(b.k==='stadium'){
  c.fillStyle='#9aa0a8';c.fillRect(x,y,w,h-3);
  c.fillStyle='#6f757d';c.beginPath();c.ellipse(x+w/2,y+(h-3)/2,w/2-3,(h-3)/2-3,0,0,6.283);c.fill();
  c.fillStyle='#2f8a3a';c.beginPath();c.ellipse(x+w/2,y+(h-3)/2,w/2-18,(h-3)/2-16,0,0,6.283);c.fill();
  c.strokeStyle='rgba(255,255,255,.7)';c.lineWidth=2;c.strokeRect(x+w/2-34,y+(h-3)/2-26,68,52);c.beginPath();c.moveTo(x+w/2,y+(h-3)/2-26);c.lineTo(x+w/2,y+(h-3)/2+26);c.stroke();c.lineWidth=1;
 }else if(b.k==='fountain'){
  c.fillStyle='#b8b8b0';c.fillRect(x,y,w,h-2);
  c.fillStyle=b.c;c.beginPath();c.arc(x+w/2,y+h/2,w/2-5,0,6.283);c.fill();
  c.fillStyle='#bfe9ff';c.beginPath();c.arc(x+w/2,y+h/2,8,0,6.283);c.fill();
 }else{
  c.fillStyle=b.c;c.fillRect(x+1,y+1,w-2,h-hh-1);
  c.strokeStyle='rgba(0,0,0,.35)';c.strokeRect(x+1.5,y+1.5,w-3,h-hh-2);
  if(b.k==='amt'){
   const hh2=h-hh;
   c.fillStyle='#cfc7b0';c.fillRect(x+1,y+1,w-2,hh2-1);
   c.strokeStyle='rgba(0,0,0,.12)';for(let i=12;i<w-6;i+=16){c.beginPath();c.moveTo(x+i,y+2);c.lineTo(x+i,y+hh2-1);c.stroke();}
   c.fillStyle='#8a8f98';c.fillRect(x+6,y+4,w-12,8);
   c.fillStyle='#5a5448';c.fillRect(x+w/2-18,y+hh2-22,36,20);c.fillStyle='#e8e0c8';c.fillRect(x+w/2-15,y+hh2-19,14,16);c.fillRect(x+w/2+1,y+hh2-19,14,16);
  }else if(b.k==='ente'){
   const hh2=h-hh,ex=x+w/2,ey=y+hh2/2;
   c.fillStyle='#8fd0f0';c.fillRect(x+1,y+1,w-2,hh2-1);
   c.strokeStyle='rgba(255,255,255,.6)';c.lineWidth=2;c.beginPath();c.ellipse(ex,ey+8,w*.4,hh2*.3,0,0,6.283);c.stroke();c.lineWidth=1;
   c.fillStyle='#ffd92a';c.beginPath();c.ellipse(ex-4,ey+2,w*.28,hh2*.3,0,0,6.283);c.fill();
   c.fillStyle='#f2b81a';c.beginPath();c.ellipse(ex-12,ey+6,w*.14,hh2*.14,-.4,0,6.283);c.fill();
   c.fillStyle='#ffd92a';c.beginPath();c.arc(ex+w*.2,ey-hh2*.1,hh2*.17,0,6.283);c.fill();
   c.fillStyle='#ff8a1a';c.beginPath();c.ellipse(ex+w*.2+hh2*.2,ey-hh2*.08,hh2*.1,hh2*.06,0,0,6.283);c.fill();
   c.fillStyle='#222';c.beginPath();c.arc(ex+w*.2+2,ey-hh2*.2,2.2,0,6.283);c.fill();
  }else if(b.k==='sender'){
   const hh2=h-hh,sx=x+10,sy=y+10,sw=w-20,sh=hh2-34;
   c.fillStyle='#3a4150';c.fillRect(x+1,y+1,w-2,hh2-1);
   c.fillStyle='#0b0e14';c.fillRect(sx-4,sy-4,sw+8,sh+8);
   const cl=['#e8e8e8','#e8d84a','#4ad8e8','#4ae85a','#e84ae0','#e8584a','#4a5ae8'],bw=sw/7;
   c.globalAlpha=.55;for(let i=0;i<7;i++){c.fillStyle=cl[i];c.fillRect(sx+i*bw,sy,bw,sh);}c.globalAlpha=1;
   c.fillStyle='rgba(255,255,255,.12)';c.fillRect(sx,sy,sw,sh*.35);
   c.strokeStyle='#cfd3da';c.lineWidth=3;c.beginPath();c.moveTo(x+w-18,y+hh2-4);c.lineTo(x+w-18,y+hh2-22);c.stroke();c.beginPath();c.arc(x+w-18,y+hh2-24,6,Math.PI,0);c.stroke();c.lineWidth=1;
   c.fillStyle='#8a6a3a';c.fillRect(x+6,y+hh2-16,w-12,12);
   c.fillStyle='#d8b878';for(let i=0;i<w-20;i+=14)c.fillRect(x+10+i,y+hh2-14,7,8);
   c.font='bold 34px Arial';c.textAlign='center';c.textBaseline='middle';c.lineWidth=5;c.strokeStyle='rgba(0,0,0,.75)';c.strokeText(b.sn,sx+sw/2,sy+sh/2);c.fillStyle='#fff';c.fillText(b.sn,sx+sw/2,sy+sh/2);c.lineWidth=1;
   c.font='bold 8px Arial';c.fillStyle='#3a2a10';c.fillText('PAPPKULISSE',x+w/2,y+hh2-10);
  }else if(b.k==='glass'){
   c.strokeStyle='rgba(60,110,110,.7)';for(let i=1;i<b.w*2;i++){c.beginPath();c.moveTo(x+i*16,y+2);c.lineTo(x+i*16,y+h-hh-1);c.stroke();}
   c.fillStyle='rgba(255,255,255,.25)';c.fillRect(x+6,y+6,w-12,10);
  }else if(b.k==='barn'){
   c.strokeStyle='#f1e6d0';c.lineWidth=3;c.beginPath();c.moveTo(x+6,y+6);c.lineTo(x+w-6,y+h-hh-6);c.moveTo(x+w-6,y+6);c.lineTo(x+6,y+h-hh-6);c.stroke();c.lineWidth=1;
   }else if(b.k==='pudding'){
   const hh2=h-hh;
   c.fillStyle='#f1c96a';c.beginPath();c.ellipse(x+w/2,y+hh2/2,w/2-4,hh2/2-3,0,0,6.283);c.fill();
   c.fillStyle='#7a3f14';c.beginPath();c.moveTo(x+8,y+hh2*.45);for(let i=0;i<=w-16;i+=16)c.quadraticCurveTo(x+8+i+8,y+hh2*.45+10+((i>>4)%3)*10,x+8+i+16,y+hh2*.45);c.lineTo(x+w-8,y+10);c.lineTo(x+8,y+10);c.closePath();c.fill();
   c.fillStyle='rgba(255,255,255,.35)';c.fillRect(x+24,y+14,36,5);
   c.fillStyle='#d8352f';c.beginPath();c.arc(x+w/2,y+14,11,0,6.283);c.fill();c.fillStyle='rgba(255,255,255,.6)';c.fillRect(x+w/2-5,y+8,4,4);c.strokeStyle='#3a6a2a';c.lineWidth=2;c.beginPath();c.moveTo(x+w/2,y+4);c.lineTo(x+w/2+6,y-3);c.stroke();c.lineWidth=1;
  }else if(b.k==='dom'){
   const hh2=h-hh;
   c.fillStyle='#6f7178';c.fillRect(x+w*.3,y+hh2*.35,w*.4,hh2*.65);
   [x+w*.1,x+w*.72].forEach(q=>{c.fillStyle='#5d5f66';c.fillRect(q,y+hh2*.25,w*.18,hh2*.75);c.fillStyle='#43454c';c.beginPath();c.moveTo(q-3,y+hh2*.25);c.lineTo(q+w*.09,y-30);c.lineTo(q+w*.18+3,y+hh2*.25);c.closePath();c.fill();c.fillStyle='#2d2f35';c.fillRect(q+w*.09-3,y+hh2*.4,6,16);c.fillRect(q+w*.09-3,y+hh2*.62,6,16);});
   c.fillStyle='#2d2f35';c.beginPath();c.arc(x+w/2,y+hh2-30,12,Math.PI,0);c.fill();c.fillRect(x+w/2-12,y+hh2-30,24,30);
  }else if(b.k==='ball'){
   const hh2=h-hh;
   c.fillStyle='#c9a24a';for(let i=10;i<w-10;i+=24)c.fillRect(x+i,y+8,6,hh2-12);
   c.fillStyle='#9fd8ef';for(let i=22;i<w-22;i+=24){c.beginPath();c.arc(x+i,y+hh2*.5,8,Math.PI,0);c.fill();c.fillRect(x+i-8,y+hh2*.5,16,18);}
   c.fillStyle='#8a2f3a';c.fillRect(x,y,w,6);
  }else if(b.k==='schiefer'){
   const hh2=h-hh;
   c.fillStyle='#2f343b';for(let i=0;i<w-4;i+=8)for(let j=0;j<hh2-4;j+=6)if(((i>>3)+((j/6)|0))%2===0)c.fillRect(x+2+i,y+2+j,8,6);
   [x+10,x+w-26].forEach(q=>{c.fillStyle='#f4f6f8';c.fillRect(q,y+hh2*.45,16,18);c.fillStyle='#6fa06a';c.fillRect(q-5,y+hh2*.45,5,18);c.fillRect(q+16,y+hh2*.45,5,18);c.fillStyle='#9fd8ef';c.fillRect(q+2,y+hh2*.45+2,5,14);c.fillRect(q+9,y+hh2*.45+2,5,14);});
   c.fillStyle='#6a6e76';c.fillRect(x,y,w,5);
  }else if(b.k==='brau'){
   const hh2=h-hh;
   c.fillStyle='#8a3a28';for(let i=0;i<w-4;i+=16)for(let j=0;j<hh2-4;j+=8)c.fillRect(x+2+i+(((j>>3)&1)?8:0),y+2+j,14,6);
   [x+22,x+w-22].forEach(q=>{c.fillStyle='#b8651f';c.beginPath();c.arc(q,y+hh2-26,18,0,6.283);c.fill();c.fillStyle='#e0903a';c.beginPath();c.arc(q-5,y+hh2-31,8,0,6.283);c.fill();c.fillStyle='#8a4a14';c.fillRect(q-3,y+hh2-52,6,10);});
   c.fillStyle='#5a3416';c.fillRect(x+w/2-12,y+hh2-30,24,30);
  }else if(b.k==='azul'){
   const hh2=h-hh;
   for(let i=0;i<w-4;i+=8)for(let j=0;j<hh2-4;j+=8){c.fillStyle=((i+j)>>3)%2?'#f5f8ff':'#2f62b8';c.fillRect(x+2+i,y+2+j,8,8);}
   c.fillStyle='#e5604d';c.fillRect(x,y,w,5);c.fillStyle='#7a4a24';c.fillRect(x+w/2-6,y+hh2-22,12,20);
  }else if(b.k==='burg'){
   const hh2=h-hh;
   c.fillStyle='#f3efe4';c.fillRect(x+w*.18,y+hh2*.38,w*.64,hh2*.62);
   [[x+4,hh2*.3],[x+w-30,hh2*.3],[x+w/2-13,hh2*.05]].forEach(q=>{
    c.fillStyle='#e8e1cf';c.fillRect(q[0],y+q[1],26,hh2-q[1]);
    c.fillStyle='#2f6fc4';c.beginPath();c.moveTo(q[0]-3,y+q[1]);c.lineTo(q[0]+13,y+q[1]-24);c.lineTo(q[0]+29,y+q[1]);c.closePath();c.fill();
    c.fillStyle='#3a4a6a';c.fillRect(q[0]+11,y+q[1]+8,4,9);c.fillRect(q[0]+11,y+q[1]+26,4,9);
   });
   c.fillStyle='#5a3416';c.fillRect(x+w/2-9,y+hh2-24,18,24);c.beginPath();c.arc(x+w/2,y+hh2-24,9,Math.PI,0);c.fill();
  }else if(b.k==='ginger'){
    const hh2=h-hh;
    c.fillStyle='#8a4f24';for(let i=0;i<w-4;i+=16)for(let j=0;j<hh2-4;j+=16)if(((i+j)>>4)%2===0)c.fillRect(x+2+i,y+2+j,16,16);
    c.strokeStyle='#fff7e6';c.lineWidth=4;c.beginPath();c.moveTo(x+3,y+7);for(let i=0;i<w-6;i+=12)c.quadraticCurveTo(x+3+i+6,y+19,x+3+i+12,y+7);c.stroke();
    c.lineWidth=3;c.strokeRect(x+4,y+4,w-8,hh2-8);
    c.fillStyle='#5a3416';c.fillRect(x+w/2-14,y+hh2-38,28,34);c.strokeStyle='#fff7e6';c.lineWidth=3;c.beginPath();c.arc(x+w/2,y+hh2-38,14,Math.PI,0);c.stroke();c.strokeRect(x+w/2-14,y+hh2-38,28,34);
    c.fillStyle='#e5504d';c.beginPath();c.arc(x+w/2+8,y+hh2-20,2.6,0,6.283);c.fill();
    [[x+26,y+36,'#ffb3d1'],[x+w-52,y+36,'#bfe6ff']].forEach(q=>{c.fillStyle=q[2];c.fillRect(q[0],q[1],26,26);c.strokeStyle='#fff7e6';c.lineWidth=3;c.strokeRect(q[0],q[1],26,26);c.beginPath();c.moveTo(q[0]+13,q[1]);c.lineTo(q[0]+13,q[1]+26);c.moveTo(q[0],q[1]+13);c.lineTo(q[0]+26,q[1]+13);c.stroke();});
    c.lineWidth=1;
    for(let k=0;k<2;k++){const cxx=x+(k?w-10:10);for(let i=0;i<8;i++){c.fillStyle=i%2?'#fff':'#e5504d';c.fillRect(cxx-3,y+hh2-6-i*6,6,6);}}
  }else if(b.k==='parktor'){
   const hh2=h-hh;
   c.fillStyle='#ffd23f';c.fillRect(x+1,y+hh2-30,w-2,28);
   for(let i=0;i<w;i+=20){c.fillStyle='#e5504d';c.beginPath();c.moveTo(x+i,y+hh2-30);c.lineTo(Math.min(x+w,x+i+20),y+hh2-30);c.lineTo(Math.min(x+w,x+i+10),y+hh2-18);c.closePath();c.fill();}
   c.fillStyle='#3a1f4a';c.beginPath();c.moveTo(x+w/2-30,y+hh2);c.lineTo(x+w/2-30,y+hh2-22);c.arc(x+w/2,y+hh2-22,30,Math.PI,0);c.lineTo(x+w/2+30,y+hh2);c.closePath();c.fill();
   c.fillStyle='rgba(255,210,63,.35)';for(let i=0;i<5;i++){c.beginPath();c.arc(x+w/2-20+i*10,y+hh2-38+Math.abs(i-2)*4,2,0,6.283);c.fill();}
   [x+4,x+w-40].forEach(tx=>{c.fillStyle='#2e86c1';c.fillRect(tx,y-8,36,hh2+8);c.fillStyle='#5fb0f0';c.fillRect(tx,y-8,36,6);c.fillStyle='#ffd23f';c.fillRect(tx+12,y+14,12,16);
    c.fillStyle='#e5504d';c.beginPath();c.moveTo(tx-4,y-8);c.lineTo(tx+40,y-8);c.lineTo(tx+18,y-40);c.closePath();c.fill();
    c.strokeStyle='#5a3416';c.lineWidth=2;c.beginPath();c.moveTo(tx+18,y-40);c.lineTo(tx+18,y-54);c.stroke();c.lineWidth=1;
    c.fillStyle='#ffd23f';c.beginPath();c.moveTo(tx+18,y-54);c.lineTo(tx+32,y-50);c.lineTo(tx+18,y-46);c.closePath();c.fill();});
   c.font='bold 15px Arial';c.textAlign='center';c.textBaseline='middle';c.lineWidth=4;c.strokeStyle='rgba(60,20,60,.85)';c.strokeText('FREIZEITPARK',x+w/2,y+20);c.fillStyle='#fff';c.fillText('FREIZEITPARK',x+w/2,y+20);c.lineWidth=1;c.textAlign='start';c.textBaseline='alphabetic';
  }else if(b.k==='bude'){
   const hh2=h-hh,aw=Math.round(hh2*.42);
   for(let i=0;i*12<w-2;i++){c.fillStyle=i%2?'#fff':b.c;c.fillRect(x+1+i*12,y+1,Math.min(12,w-2-i*12),aw);}
   c.fillStyle='rgba(0,0,0,.2)';c.fillRect(x+1,y+1+aw,w-2,3);
   c.fillStyle='#f4e8c8';c.fillRect(x+6,y+aw+6,w-12,hh2-aw-14);
   c.fillStyle='#8a5a2a';c.fillRect(x+3,y+hh2-8,w-6,6);
  }else if(b.k==='feuerwache'){
   const hh2=h-hh,gw=(w-24)/3;
   c.fillStyle='#e8e8e8';c.fillRect(x+1,y+1,w-2,7);
   for(let i=0;i<3;i++){const gx=x+8+i*(gw+4);c.fillStyle='#7a1d1d';c.fillRect(gx,y+hh2-30,gw,28);c.strokeStyle='rgba(255,255,255,.3)';for(let k=1;k<5;k++){c.beginPath();c.moveTo(gx,y+hh2-30+k*5.6);c.lineTo(gx+gw,y+hh2-30+k*5.6);c.stroke();}}
   c.fillStyle='#2f7fd8';c.beginPath();c.arc(x+w-16,y+16,6,0,6.283);c.fill();c.fillStyle='#fff';c.font='bold 11px Arial';c.textAlign='center';c.textBaseline='middle';c.fillText('112',x+18,y+16);c.textAlign='start';c.textBaseline='alphabetic';
  }else if(b.k==='kh'){
   const hh2=h-hh;
   c.fillStyle='#cfd8de';c.fillRect(x+1,y+1,w-2,6);
   c.fillStyle='#e5504d';c.fillRect(x+30,y+hh2/2-16,12,32);c.fillRect(x+20,y+hh2/2-6,32,12);
   c.strokeStyle='#f1c40f';c.lineWidth=3;c.beginPath();c.arc(x+w-40,y+hh2/2,24,0,6.283);c.stroke();c.lineWidth=1;
   c.fillStyle='#f1c40f';c.font='bold 22px Arial';c.textAlign='center';c.textBaseline='middle';c.fillText('H',x+w-40,y+hh2/2+1);c.textAlign='start';c.textBaseline='alphabetic';
  }else if(b.k==='neon'){
   c.strokeStyle='#ff5fd0';c.lineWidth=3;c.strokeRect(x+4,y+4,w-8,h-hh-8);c.strokeStyle='#5ff0ff';c.strokeRect(x+9,y+9,w-18,h-hh-18);c.lineWidth=1;
  }else{
   c.strokeStyle='rgba(255,255,255,.16)';c.beginPath();c.moveTo(x+w/2,y+2);c.lineTo(x+w/2,y+h-hh-2);c.stroke();
   if(b.w>=4){c.fillStyle='rgba(0,0,0,.28)';c.fillRect(x+8,y+8,10,8);}
   if(b.h>=4){c.fillStyle='rgba(255,255,255,.2)';c.fillRect(x+w-20,y+h-hh-18,12,10);}
  }
 }
 if(b.n){
  let fs=13;c.font='bold '+fs+'px Arial';
  while(c.measureText(b.n).width>w-8&&fs>7){fs--;c.font='bold '+fs+'px Arial';}
  c.textAlign='center';c.textBaseline='middle';c.lineWidth=3;c.strokeStyle='rgba(0,0,0,.65)';
  c.strokeText(b.n,x+w/2,y+(h-hh)/2);c.fillStyle='#fff';c.fillText(b.n,x+w/2,y+(h-hh)/2);c.lineWidth=1;
 }
}

function drawBench(c,px,py){
 c.fillStyle='rgba(0,0,0,.25)';c.fillRect(px+4,py+13,26,12);
 c.fillStyle='#6b4a2b';c.fillRect(px+3,py+11,26,4);c.fillRect(px+3,py+16,26,4);c.fillRect(px+3,py+21,26,3);
 c.fillStyle='#8a6339';c.fillRect(px+3,py+11,26,2);c.fillRect(px+3,py+16,26,2);c.fillRect(px+3,py+21,26,1.5);
 c.fillStyle='#3a3a3a';c.fillRect(px+5,py+10,3,15);c.fillRect(px+24,py+10,3,15);
}
function drawPlay(c,px,py,v){
 c.fillStyle='rgba(0,0,0,.25)';c.fillRect(px+5,py+8,24,22);
 if(v===0){
  c.fillStyle='#e0452f';c.fillRect(px+3,py+3,11,11);c.fillStyle='#ffd23f';c.fillRect(px+11,py+6,13,23);
  c.fillStyle='rgba(255,255,255,.4)';c.fillRect(px+14,py+8,2,19);
 }else if(v===1){
  c.fillStyle='#5a4a3a';c.fillRect(px+3,py+4,26,3);c.fillRect(px+3,py+4,3,24);c.fillRect(px+26,py+4,3,24);
  c.strokeStyle='#999';c.beginPath();c.moveTo(px+10,py+7);c.lineTo(px+10,py+20);c.moveTo(px+22,py+7);c.lineTo(px+22,py+20);c.stroke();
  c.fillStyle='#3d7de0';c.fillRect(px+7,py+20,7,3);c.fillRect(px+19,py+20,7,3);
 }else{
  c.fillStyle='#777';c.beginPath();c.moveTo(px+16,py+10);c.lineTo(px+10,py+24);c.lineTo(px+22,py+24);c.closePath();c.fill();
  c.fillStyle='#2e9d4f';c.fillRect(px+2,py+10,28,5);c.fillStyle='#e0452f';c.fillRect(px+2,py+8,5,9);c.fillRect(px+25,py+8,5,9);
 }
}
function drawSign(c,s){
 const x=s.x,y=s.y;
 c.fillStyle='rgba(0,0,0,.25)';c.fillRect(x-12,y-24,26,26);
 c.fillStyle='#555';c.fillRect(x-1,y-4,3,20);
 c.fillStyle='#fafafa';c.fillRect(x-13,y-26,26,22);
 c.strokeStyle='#c0392b';c.lineWidth=2;c.strokeRect(x-12,y-25,24,20);
 c.fillStyle='#b8862b';c.fillRect(x-7,y-21,4,10);c.fillRect(x-6,y-23,2,3);
 c.fillStyle='#222';c.fillRect(x+1,y-14,8,2.5);c.fillStyle='#ff7a1a';c.fillRect(x+9,y-14,2,2.5);
 c.beginPath();c.arc(x,y-15,9,0,6.283);c.stroke();c.beginPath();c.moveTo(x-7,y-8);c.lineTo(x+7,y-22);c.stroke();c.lineWidth=1;
}
function zrng(s0){let s=s0|0;return function(){s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
const ZW=48,ZH=30;
const ZINFO={
 holly:{title:'Hollyhanf',hint:'Studios, Walk of Fame und Palmen. Hier drehst du Videos, kaufst Lizenzen und feierst Premieren.',wx:'sun',gain:.7,base:SW,walk:[SW,GR],picks:['dose'],cap:5},
 freibad:{title:'Freibad',hint:'Drei Wasserrutschen, ein Sprungturm mit Rentner-Jury und Pommes rot-weiß. Nicht rennen!',wx:'sun',gain:.6,base:GR,walk:[GR,SW],picks:['dose'],cap:4,swim:true},
 gamsbahn:{title:'Gamsblitz-Bahn',hint:'Die große Rodelbahn: sechs lange Geraden, fünf Haarnadelkurven und zwei Sprunghügel. Die Gondel bringt dich immer wieder hoch.',wx:'snow',gain:.5,base:SN,walk:[SN],picks:['stein'],cap:4},
 camping:{title:'Camping Tulpenwiese',hint:'Holland! Käse-Wohnwagen, Wurfzelte, eine Windmühle und Dauercamper Herbert mit seinen Gartenzwergen.',wx:'sun',gain:.6,base:GR,walk:[GR,SW],picks:['dose','stein'],cap:6,swim:true},
 strand:{title:'Strand',hint:'Sonne, Sand und Sorglosigkeit. Sandburgen, Wasserpistolen, Boote!',swim:true,wx:'sun',gain:.4,base:SA,walk:[SA],picks:['stein','dose','stein'],cap:12},
 vulkan:{title:'Vulkan',hint:'Heiß, laut und herrlich ungemütlich. Hier darfst du schreien.',wx:'ash',gain:0,base:AS,walk:[AS],picks:['stein','stein','stein'],cap:18},
 berge:{title:'Alpen',hint:'Schnee bis zum Horizont. Rodelbahn Gamsblitz mit Schlepplift, Glühwein, Schneemänner!',wx:'snow',gain:.3,base:SN,walk:[SN],picks:['stein','dose'],cap:8},
 hoehle:{title:'Höhle',hint:'Dunkel, feucht und leuchtende Pilze. Irgendwo tropft es.',swim:true,wx:'none',gain:.15,base:CF,walk:[CF],picks:['stein','dose'],cap:10},
 rhein:{title:'Rhein',hint:'Volle Fahrt! Immer flussabwärts, bis Amsterdam. Hoch fährt, Links und Rechts lenkt.',wx:'sun',gain:.35,base:GR,walk:[GR],picks:['stein','dose'],cap:8,swim:true},
 amsterdam:{title:'Amsterdam',hint:'Grachten, Fahrräder, Tulpen. Willkommen in Holland!',wx:'sun',gain:.3,base:SW,walk:[SW],picks:['stein','dose'],cap:10,swim:true},
 wal:{title:'Wal-Bauch',hint:'Warm, wabbelig und überraschend gemütlich. Sofa, Tee, Joint ...',wx:'none',gain:.6,base:CF,walk:[CF],picks:['dose'],cap:3,swim:true},
 maerchen:{title:'Märchenwald',hint:'Lebkuchenhaus, Frau Holle, sieben Zwerge ... Hier ist alles ein bisschen verzaubert.',wx:'none',gain:.5,base:GR,walk:[GR],picks:['dose','stein'],cap:6},
 schlaraff:{title:'Schlaraffenland',hint:'Pudding-Berge, ein Milchsee und Brathähnchen im Anflug. Mund auf!',wx:'none',gain:.6,base:GR,walk:[GR],picks:['dose'],cap:3},
 bayern:{title:'Bayern',hint:'Berge, Biergarten, Blasmusik und ein Schloss wie aus dem Bilderbuch. Servus!',swim:true,wx:'sun',gain:.5,base:GR,walk:[GR],picks:['stein','dose'],cap:8},
 portugal:{title:'Portugal',hint:'Gelbe Tram, Fado und Sardinen. Das Meer rauscht. Olá!',swim:true,wx:'sun',gain:.5,base:SW,walk:[SW,SA],picks:['stein','dose'],cap:8},
 wuppertal:{title:'Wuppertal',hint:'Die Schwebebahn schwebt, die Wupper plätschert und im Brauhaus zischt das Bier. Glück auf!',swim:true,wx:'none',gain:.5,base:SW,walk:[SW],picks:['stein','dose'],cap:8},
 oesterreich:{title:'Österreich',hint:'Skipiste mit Sessellift, Kaffeehaus, Walzer und Kühe mit Glocken. Servus und herzlich willkommen!',swim:true,wx:'sun',gain:.5,base:GR,walk:[GR],picks:['stein','dose'],cap:8},
 koeln:{title:'Köln',hint:'Dom, Kölsch und ein Köbes, der immer recht hat. Alaaf!',swim:true,wx:'sun',gain:.5,base:SW,walk:[SW],picks:['stein','dose'],cap:8},
 feldweg:{title:'Feldweg',hint:'Hopfenranken, Hanfreihen und Bienen. Atme durch, hier duftet es nach Sommer.',wx:'sun',gain:.6,base:GR,walk:[GR,SA],picks:['dose','stein'],cap:6},
 sender:{title:'Senderviertel',hint:'Vier Pappkulissen, eine Wurfbude und viel Luft für Frust. Wirf Dosen und Eier, danach atmest du durch.',wx:'none',gain:.5,base:SW,walk:[SW],picks:['dose'],cap:4},
 helden:{title:'Heldenplatz',hint:'Fünf Superhelden mit ganz eigenem Look und Quatsch im Kopf. Sprich sie an und bestehe die Heldenprüfung.',wx:'sun',gain:.5,base:SW,walk:[SW],picks:['dose','stein'],cap:6},
 amt:{title:'Amt für Alles',hint:'Wartenummern, Stempel und ein Zwerg, der nie zuständig ist. Hier ist alles ein bisschen Formular.',wx:'none',gain:.4,base:SW,walk:[SW],picks:['dose'],cap:4},
 fpark:{title:'Freizeitpark',hint:'Achterbahn, Riesenrad, Karussell, Autoscooter und Zuckerwatte. Alle Fahrten sind im Eintritt drin!',wx:'sun',gain:.6,base:SW,walk:[SW,GR],picks:['dose'],cap:3},
 malle:{title:'Ballermann',hint:'Mallorca! Strand, Schlagerbühne, Sangria-Bar und Polonaise. Sonnenhut nicht vergessen!',swim:true,wx:'sun',gain:.7,base:SW,walk:[SW,SA],picks:['dose'],cap:4},
 zoo:{title:'Tierpark',hint:'Zebras, Giraffen, Lamas, Kängurus, Pinguine und Flamingos. Jedes Tier, das du zurückbringst, wohnt jetzt hier.',wx:'sun',gain:.6,base:SW,walk:[SW,GR,SA],picks:['dose'],cap:3},
 gallien:{title:'Gallierdorf',hint:'Rundhütten, eine Druidin mit Zauberkessel und nebenan ein Römerlager, das im Kreis marschiert.',wx:'sun',gain:.5,base:GR,walk:[GR,SA,SW],picks:['stein','dose'],cap:6},
 plantage:{title:'Fernsehturm',hint:'Hightech-Fernsehturm der GlotzKonzern AG mit Lager für Receiver, Antennen, Kabel und Fernseher. Zaun, Kameras, Wachleute. Beim Pförtner gibt es Schichten als Techniker.',wx:'sun',gain:.3,base:GR,walk:[GR,SW,SA],picks:['dose'],cap:4}
};
const ZPO={
 holly:{home:['bahn','Flughafen-Shuttle','Zum Flughafen-Shuttle','Der Shuttle hupt. Die Anzeige kennt alle Ziele.'],wild:['parktor','Kulissentür','Durch die Kulissentür','Hinter der Kulisse ist ... eine andere Kulisse. Und dann ganz woanders.']},
 freibad:{home:['parktor','Drehkreuz','Durchs Drehkreuz nach Hause','Du gehst durchs Drehkreuz. Die nassen Haare trocknen auf dem Heimweg.'],wild:['gully','Abfluss-Gitter','Durch den Abfluss rutschen','Gurgel, gurgel … Du rutschst durch den Abfluss und landest ganz woanders.']},
 gamsbahn:{home:['schlitten','Wanderweg in die Alpen','Zurück in die Alpen','Du stapfst den Wanderweg hinunter in die Alpen.','berge'],wild:['huette','Hütten-Tür','Hütten-Tür öffnen','Die Tür knarzt. Dahinter ist es ganz woanders.']},
 camping:{home:['bahn','Bushaltestelle','Zur Bushaltestelle gehen','Der Bus hupt zweimal. Die Anzeige kennt alle Ziele.'],wild:['tulpe','Riesen-Tulpe','In die Riesen-Tulpe klettern','Du kletterst in die Riesen-Tulpe. Sie klappt zu, schaukelt, und du purzelst ganz woanders raus.']},
 strand:{home:['strandkorb','Strandkorb','Strandkorb zuklappen','Du kuschelst dich in den Strandkorb und klappst ihn zu. Wenn du ihn öffnest: zu Hause.'],wild:['surfbrett','Surfbrett','Aufs Surfbrett steigen','Eine Riesenwelle! Du surfst direkt aus dem Bild.']},
 vulkan:{home:['notausgang','Notausgang','Notausgang nehmen','Du nimmst den grünen Notausgang. Er riecht nach Pizza.'],wild:['lavalampe','Lava-Lampe','In die Lava-Lampe springen','Du hüpfst in die Lava-Lampe. Glibber, glibber, plopp!']},
 berge:{home:['huette','Hütten-Tür','Hütten-Tür öffnen','Die Tür knarzt. Dahinter ist es überraschend städtisch.'],wild:['schlitten','Rodelschlitten','Losrodeln','Du rodelst los. Und rodelst. Und rodelst. Und rodelst ...']},
 hoehle:{home:['leiter','Leiter nach oben','Leiter hochklettern','Du kletterst Sprosse für Sprosse zurück in die Stadt.'],wild:['tropf','Tropfsteinloch','Ins Loch kriechen','Du zwängst dich durchs Loch. Schmatz!']},
 rhein:{home:['anleger','Anleger Düsseldorf','Zurück nach Düsseldorf','Du legst am Düsseldorfer Rheinufer an. Alles noch da.'],wild:['anleger','Anleger Amsterdam','Weiterfahren nach Amsterdam','Immer der Strömung nach. Moment, das sind schon Grachten!','amsterdam']},
 amsterdam:{home:['anleger','Boot nach Düsseldorf','Boot zurück nehmen','Du tuckerst den Rhein hinauf. Düsseldorf, hier bin ich wieder.'],wild:['tulpe','Riesen-Tulpe','In die Tulpe klettern','Du kletterst in die Riesen-Tulpe. Es riecht nach Frühling, dann nach Neuland.']},
 wal:{home:['blasloch','Blasloch','Durchs Blasloch hinaus','Der Wal niest kräftig. Du fliegst in hohem Bogen hinaus ins Meer!','strand'],wild:['tee','Leuchtender Tee','Den Leuchttee probieren','Ein seltsam leuchtender Tee. Du trinkst, und die Welt dreht sich weiter.']},
 maerchen:{home:['buch','Märchenbuch','Märchenbuch zuklappen','Ende gut, alles gut. Du klappst das Märchenbuch zu, und Rheinhanfen ist wieder da.'],wild:['brunnen','Brunnen','In den Brunnen springen','Du springst in den Brunnen. Plumps! Du fällst und fällst, und unten ist es überraschend hell.']},
 schlaraff:{home:['loeffel','Riesenlöffel','Löffel zurück nehmen','Du setzt dich auf den Riesenlöffel und rutschst zurück in den Märchenwald.','maerchen'],wild:['kuchen','Zuckerkuchen','In den Kuchen beißen','Du beißt in den Kuchen. Die Füllung trägt dich fort.']},
 bayern:{home:['bahn','Bahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Auf der Anzeigetafel steht: Alle Ziele.'],wild:['kuckuck','Kuckucksuhr','Die Kuckucksuhr aufziehen','Der Kuckuck ruft dreizehn Mal. Dann wird alles anders.']},
 portugal:{home:['flug','Flughafen','Zum Flughafen gehen','Du gehst zum Flughafen. Die Möwen wünschen gute Reise.'],wild:['galo','Hahn von Barcelos','Den bunten Hahn streicheln','Der bunte Hahn kräht aus voller Brust. Das Kikeriki trägt dich fort.']},
 wuppertal:{home:['bahn','Hauptbahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Die Schwebebahn winkt von oben.'],wild:['waffel','Riesenwaffel','In die Waffel beißen','Du beißt in eine Bergische Waffel. Heiße Kirschen spritzen, und die Welt dreht sich weiter.']},
 oesterreich:{home:['bahn','Bahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Die Anzeigetafel kennt alle Ziele.'],wild:['strudel','Riesen-Strudel','In den Strudel kriechen','Du kriechst in den Apfelstrudel. Es wird warm, süß und ein bisschen puderzuckrig.']},
 koeln:{home:['bahn','Hauptbahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Die Gleise zeigen in alle Richtungen.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 feldweg:{home:['tor','Gartentor','Durchs Gartentor gehen','Du gehst durchs Gartentor zurück in die Stadt. Es quietscht freundlich.'],wild:['heu','Heuballen','In den Heuballen springen','Du springst in den Heuballen. Er duftet nach Sommer und schluckt dich.']},
 sender:{home:['tor','Studiotor','Durchs Studiotor gehen','Du gehst durchs Studiotor zurück in die Stadt. Der Wachmann winkt.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 helden:{home:['tor','Stadttor','Durchs Stadttor gehen','Du gehst durchs Stadttor zurück in die Stadt. Eine Taube salutiert.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 amt:{home:['tor','Amtstür','Durch die Amtstür gehen','Du gehst durch die Amtstür zurück in die Stadt. Sie ist die einzige Tür, die zuständig war.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 fpark:{home:['parktor','Parkausgang','Zum Ausgang gehen','Du gehst durch das bunte Tor zurück in die Stadt. In der Tasche: Popcornkrümel und gute Laune.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 malle:{home:['flug','Rückflug','Zum Rückflug','Ab in den Ferienflieger! Zwei Stunden später landest du mit Sonnenbrand und Ohrwurm in Rheinhanfen.'],wild:['surfbrett','Surfbrett','Aufs Surfbrett steigen','Eine Riesenwelle! Du surfst direkt aus dem Bild.']},
 zoo:{home:['parktor','Tierpark-Ausgang','Zum Ausgang gehen','Du winkst den Flamingos zum Abschied und gehst zurück nach Rheinhanfen.'],wild:['konfetti','Konfetti-Kanone','Die Konfetti-Kanone zünden','Peng! Konfetti überall, und du wirbelst mit davon.']},
 gallien:{home:['bahn','Kutschenhalt','Zur Kutsche gehen','Die Kutsche wartet schon.'],wild:['brunnen','Dorfbrunnen','In den Dorfbrunnen springen','Platsch! Du fällst und fällst ... und landest ganz woanders.']},
 plantage:{home:['tor','Feldweg zum Landgut','Zurück zum Landgut','Du gehst den Feldweg zurück zum Landgut Hopfenhof.'],wild:['heu','Heuballen','In den Heuballen springen','Du springst in den Heuballen. Er duftet nach Sommer und schluckt dich ganz.']}
};
const ZWILD={strand:[42,23],vulkan:[43,25],berge:[42,8],hoehle:[39,21],rhein:[44,rheinY(44)+7],amsterdam:[43,16],wal:[40,15],maerchen:[38,23],schlaraff:[40,22],bayern:[44,22],portugal:[44,22],wuppertal:[44,25],oesterreich:[44,17],koeln:[44,20],feldweg:[44,22],sender:[44,24],helden:[44,24],amt:[44,24],fpark:[44,24],malle:[44,24],zoo:[44,14],gallien:[28,1],plantage:[46,14],freibad:[45,27],camping:[45,5],gamsbahn:[45,28],holly:[45,27]};
const ZHOME={rhein:[3,rheinY(3)+7],amsterdam:[6,26],wal:[8,15],maerchen:[6,24],schlaraff:[6,24],bayern:[6,25],portugal:[12,24],wuppertal:[6,26],oesterreich:[6,26],koeln:[6,22],feldweg:[4,22],sender:[5,24],helden:[5,24],amt:[5,24],fpark:[5,24],malle:[5,24],zoo:[3,14],gallien:[6,27],plantage:[3,15],freibad:[2,16],camping:[2,10],gamsbahn:[9,28],holly:[2,19]};
function genZone(name){
 const I=ZINFO[name];
 const z={name:name,title:I.title,hint:I.hint,wx:I.wx,moodGain:I.gain,base:I.base,walk:I.walk,pickTypes:I.picks,pickCap:I.cap,dark:name==='hoehle',T:new Uint8Array(ZW*ZH),MW:ZW,MH:ZH,BLD:[],MKS:[],glows:[],WC:document.createElement('canvas'),MM:document.createElement('canvas'),spawn:null,swim:!!I.swim,rides:[],nogo:null,spawnRide:false};
 z.WC.width=ZW*TS;z.WC.height=ZH*TS;z.MM.width=304;z.MM.height=192;
 const r=zrng(name.charCodeAt(0)*7919+name.length*104729);
 const R=(a,b)=>a+Math.floor(r()*(b-a+1));
 const Tz=z.T;
 const zs=(x,y,v)=>{if(x>=0&&y>=0&&x<ZW&&y<ZH)Tz[y*ZW+x]=v;};
 const zg=(x,y)=>(x<0||y<0||x>=ZW||y>=ZH)?RK:Tz[y*ZW+x];
 const zf=(x,y,w,h,v)=>{for(let j=y;j<y+h;j++)for(let i=x;i<x+w;i++)zs(i,j,v);};
 const zc=(cx,cy,rx,ry,v,only)=>{for(let j=Math.floor(cy-ry)-1;j<=cy+ry+1;j++)for(let i=Math.floor(cx-rx)-1;i<=cx+rx+1;i++){const dx=(i-cx)/rx,dy=(j-cy)/ry;if(dx*dx+dy*dy<=1&&(!only||only.indexOf(zg(i,j))>=0))zs(i,j,v);}};
 const mk=(id,kind,tx,ty,n,act,obj,warp)=>{const m={id:id,dist:'',kind:kind,x:tx*TS+16,y:ty*TS+16,n:n,act:act,obj:obj,warp:warp,col:kind==='portal'?'#c06bff':kind==='buedchen'?'#46c2a0':kind==='scream'?'#ff5030':'#ff5fd0'};z.MKS.push(m);return m;};
 const clr=(tx,ty,rd,v)=>{for(let j=ty-rd;j<=ty+rd;j++)for(let i=tx-rd;i<=tx+rd;i++)zs(i,j,v);};
 const base=I.base;
 if(name==='strand'){
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){const sh=9+Math.round(Math.sin(x*.45)*1.4+Math.sin(x*.17)*1.2);zs(x,y,y<sh-2?DP:y<sh?SH:SA);}
  for(let i=0;i<18;i++){const x=R(2,ZW-3),y=R(13,ZH-3);if(zg(x,y)===SA)zs(x,y,TR);}
  for(let i=0;i<8;i++){const x=R(3,ZW-5),y=R(11,ZH-4);if(zg(x,y)===SA&&zg(x+1,y)===SA){zs(x,y,UM);zs(x+1,y,LC);}}
  for(let x=17;x<=25;x++)zs(x,19,FN);
  clr(38,16,2,SA);zf(36,13,5,3,BL);z.BLD.push({x:36,y:13,w:5,h:3,c:'#e0a040',n:'STRANDBAR',k:'house',hh:6});
  mk('bar','buedchen',38,16,'Strandbar','Strandbar besuchen');
  z.sharks=[];for(let i=0;i<3;i++)z.sharks.push({x:(8+i*15+R(0,4))*TS+16,y:R(1,3)*TS+16,a:r()*6.283,cool:0,flee:0,wag:0,shk:0});
  z.whale={x:12*TS,y:2.4*TS,a:0,sp:22,open:0,spout:3,seen:false};
  z.nogo={x0:4*TS,y0:13*TS,x1:30*TS,y1:18*TS,n:'Kinderstrand'};
  {const shf=x=>9+Math.round(Math.sin(x*.45)*1.4+Math.sin(x*.17)*1.2);[[14,1],[30,3]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,(shf(q[0])-q[1])*TS+16,0)));}
 }else if(name==='vulkan'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=AS;
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if(x<2||y<2||x>=ZW-2||y>=ZH-2||((x<3||y<3||x>=ZW-3||y>=ZH-3)&&r()<.5))zs(x,y,RK);}
  zc(24,9,6.5,5.5,RK);zc(24,9,2.6,2.2,LV);
  [[10,12,3.2,2.2],[37,19,4,2.6],[14,21,2.4,1.8],[40,9,2.4,2.2],[31,5,2,1.6]].forEach(q=>zc(q[0],q[1],q[2],q[3],LV,[AS]));
  clr(24,17,1,AS);
  mk('scream','scream',24,17,'Wut-Stein','Wut herausschreien');
 }else if(name==='berge'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SN;
  for(let x=0;x<ZW;x++){const h=3+Math.round(Math.sin(x*.5)*1.2+Math.sin(x*.19)*1.5);for(let y=0;y<h;y++)zs(x,y,RK);}
  zc(34,22,6.5,3.2,IC);
  for(let i=0;i<46;i++){const x=R(1,ZW-2),y=R(7,ZH-2);if(zg(x,y)===SN)zs(x,y,TR);}
  clr(21,19,2,SN);zf(19,16,5,3,BL);z.BLD.push({x:19,y:16,w:5,h:3,c:'#8a5a35',n:'SKIHÜTTE',k:'house',hh:6});
  mk('hutbar','buedchen',21,19,'Glühwein-Hütte','Glühwein-Hütte besuchen');
  [[10,8],[27,9],[44,10],[6,7]].forEach(q=>{let x=q[0],y=q[1];for(let k=0;k<14&&zg(x,y)!==SN;k++)y++;z.rides.push(mkRide('sled',x*TS+16,y*TS+16,1.57));});
  [[14,12],[28,11],[40,16]].forEach(q=>clr(q[0],q[1],1,SN));
  zf(2,13,15,8,SN);zf(3,14,6,3,BL);z.BLD.push({x:3,y:14,w:6,h:3,c:'#b0402f',n:'WEIHNACHTSWERKSTATT',k:'house',hh:6});
  {const m=mk('werk','sk',5,17,'Weihnachtswerkstatt','Weihnachtswerkstatt besuchen');m.sk='werk';m.col='#ffb347';}
  kBerge(z,{zs:zs,zg:zg,mk:mk});
 }else if(name==='hoehle'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=RK;
  const ch=[[6,25,4],[15,21,3.6],[22,13,5],[11,9,3.6],[33,8,4.6],[39,21,4.6],[27,25,3.6],[43,14,3]];
  ch.forEach(c=>zc(c[0],c[1],c[2],c[2]*.85,CF));
  const tun=(a,b)=>{let x=ch[a][0],y=ch[a][1];const tx=ch[b][0],ty=ch[b][1];while(x!==tx){x+=Math.sign(tx-x);zf(x,y-1,1,3,CF);}while(y!==ty){y+=Math.sign(ty-y);zf(x-1,y,3,1,CF);}};
  [[0,1],[1,2],[2,3],[2,4],[4,7],[7,5],[5,6],[6,1]].forEach(t=>tun(t[0],t[1]));
  zc(33,8,3.4,2.8,SH,[CF]);zc(33,8,2.2,1.8,DP);
  for(let i=0;i<60;i++){
   const x=R(2,ZW-3),y=R(2,ZH-3);
   if(zg(x,y)!==CF)continue;
   if(zg(x-1,y)!==RK&&zg(x+1,y)!==RK&&zg(x,y-1)!==RK&&zg(x,y+1)!==RK)continue;
   zs(x,y,i%2?CY:MU);
  }
  clr(22,13,1,CF);clr(36,10,1,CF);
  mk('disco','disco',22,13,'Höhlen-Disco','Tanzen');
  mk('hbar','buedchen',36,10,'Höhlen-Bar','Höhlen-Bar besuchen');
 }else if(name==='rhein'){
  const cy=rheinY;
  for(let i=0;i<ZW*ZH;i++)Tz[i]=GR;
  for(let x=0;x<ZW;x++){const c=cy(x);for(let y=c-4;y<=c+4;y++)zs(x,y,(y===c-4||y===c+4)?SH:DP);}
  [[12,-2],[19,2],[24,-2],[30,2],[36,-1]].forEach(q=>{const y=cy(q[0])+q[1];zc(q[0],y,1.2,1.05,GR,[DP,SH]);if(q[1]<0)zs(q[0],y,TR);});
  for(let i=0;i<46;i++){const x=R(1,ZW-2),y=R(1,ZH-2);if(zg(x,y)===GR&&Math.abs(y-cy(x))>5)zs(x,y,TR);}
  const lm=(x,top,w,h,col,n)=>{const y=top?Math.max(1,cy(x)-6-h):cy(x)+6;zf(x,y,w,h,BL);z.BLD.push({x:x,y:y,w:w,h:h,c:col,n:n,k:'house',hh:8});};
  lm(5,true,3,3,'#9aa4b0','RHEINTURM');lm(15,true,4,3,'#7d8590','KÖLNER DOM');lm(26,false,4,3,'#6d6a64','LORELEY');lm(34,true,4,3,'#b0805a','ZOLL NL');lm(38,false,3,3,'#c9a24a','MÜHLE');
  z.rides.push(mkRide('boat',3*TS+16,cy(3)*TS+16,0));z.spawnRide=true;
 }else if(name==='amsterdam'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  zf(0,8,ZW,3,DP);zf(0,19,ZW,3,DP);zf(22,11,3,8,DP);
  zf(11,8,2,3,DK);zf(36,19,2,3,DK);zf(22,14,3,2,DK);
  const hc=['#8b3a2f','#c97b4a','#3a5a7a','#b8a45a','#6a4a7a','#4a7a5a'];
  const hs=(x,y,w,h,i)=>{zf(x,y,w,h,BL);z.BLD.push({x:x,y:y,w:w,h:h,c:hc[i%6],n:'',k:'house',hh:6});};
  let ci=0;
  for(let x=2;x<ZW-3;x+=3){if(x>=10&&x<=13)continue;const h=r()<.5?3:4;hs(x,7-h,2,h,ci++);}
  for(let x=3;x<=19;x+=3)hs(x,12,2,3,ci++);
  for(let x=36;x<=43;x+=3)hs(x,12,2,3,ci++);
  for(let x=11;x<=35;x+=3){if(x>=26&&x<=35)continue;hs(x,22+1,2,2,ci++);}
  zf(29,12,3,2,BL);z.BLD.push({x:29,y:12,w:3,h:2,c:'#2f7a4a',n:'COFFEESHOP',k:'house',hh:6});
  zf(39,23,3,3,BL);z.BLD.push({x:39,y:23,w:3,h:3,c:'#c9a24a',n:'MÜHLE',k:'house',hh:8});
  zf(26,25,9,4,FD);
  clr(30,14,1,SW);
  mk('cafe','buedchen',30,14,'Coffeeshop Zum frohen Hanf','Coffeeshop besuchen');
  for(let i=0;i<26;i++){const x=R(1,ZW-2),y=R(12,ZH-2);if(zg(x,y)===SW&&zg(x,y-1)===SW&&zg(x,y+1)===SW)zs(x,y,TR);}
  [[30,9],[16,20],[42,9]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
  [[13,17],[19,17],[36,16],[8,16]].forEach(q=>z.rides.push(mkRide('bike',q[0]*TS+16,q[1]*TS+16,r()*6.283)));

 }else if(name==='wal'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=RK;
  zc(24,15,21,12,CF);zc(9,14,7,9,CF);zc(39,14,7,9,CF);
  [12,18,30,36].forEach(x=>{zf(x,7,1,2,RK);zf(x,22,1,2,RK);});
  zc(31,19,4,3,SH,[CF]);zc(31,19,2.6,1.8,DP);
  [[20,12],[21,12],[27,12],[28,12],[22,18],[23,18]].forEach(q=>zs(q[0],q[1],LC));
  for(let i=0;i<60;i++){
   const x=R(2,ZW-3),y=R(2,ZH-3);
   if(zg(x,y)!==CF)continue;
   if(zg(x-1,y)!==RK&&zg(x+1,y)!==RK&&zg(x,y-1)!==RK&&zg(x,y+1)!==RK)continue;
   zs(x,y,MU);
  }
  clr(24,15,1,CF);
  mk('tee','buedchen',24,15,'Tee-Ecke im Wal','Tee-Ecke besuchen');
 }else if(name==='maerchen'){
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){const e=x<2||y<2||x>ZW-3||y>ZH-3;if(e&&r()<.8)zs(x,y,TR);else if(r()<.05)zs(x,y,TR);}
  for(let i=0;i<16;i++){const x=R(3,ZW-4),y=R(3,ZH-4);if(zg(x,y)===GR)zs(x,y,MU);}
  for(let k=0;k<10;k++){const a=k/10*6.283;const x=Math.round(24+Math.cos(a)*3.4),y=Math.round(19+Math.sin(a)*2.5);zs(x,y,MU);}
  [[12,16,4,3],[22,6,5,2],[14,10,3,3],[40,6,4,3],[26,27,6,1]].forEach(q=>zf(q[0],q[1],q[2],q[3],FD));
  zc(19,19,3.5,2.2,SH);
  zf(8,8,1,17,SW);zf(8,14,37,1,SW);zf(30,10,1,5,SW);zf(8,24,31,1,SW);zf(38,18,1,7,SW);
  zf(6,5,5,3,BL);z.BLD.push({x:6,y:5,w:5,h:3,c:'#7d9cc4',n:'FRAU HOLLE',k:'house',hh:6});
  zf(7,8,3,2,GR);zf(8,8,1,2,SW);
  {const m=mk('holle','sk',8,8,'Frau Holles Haus','Frau Holle besuchen');m.sk='holle';m.col='#ffb347';}
  zf(28,6,6,4,BL);z.BLD.push({x:28,y:6,w:6,h:4,c:'#a8642e',n:'LEBKUCHENHAUS',k:'ginger',hh:6});
  zf(28,10,5,2,GR);zf(30,10,1,2,SW);zf(32,10,3,2,GR);
  {const m=mk('haus','sk',30,10,'Lebkuchenhaus','Lebkuchenhaus und liebe Hexe');m.sk='haus';m.col='#ffb347';}
  zf(11,25,25,3,GR);
  {const m=mk('hase','sk',12,26,'Hase und Igel','Wettlauf Hase und Igel');m.sk='hase';m.col='#ffb347';}
  zf(42,21,3,3,GR);
  {const m=mk('schl','portal',43,22,'Schlaraffenland','Ins Schlaraffenland gehen','kuchen','Du isst dich durch einen Berg aus Griesbrei. Dahinter: Schlaraffenland!');m.to='schlaraff';}
  zf(17,9,5,4,GR);
  {const m=mk('tisch','sk',19,12,'Tischlein deck dich','Tischlein deck dich ausprobieren');m.sk='tisch';m.col='#ffb347';}
  zf(38,15,4,3,BL);z.BLD.push({x:38,y:15,w:4,h:3,c:'#8a6a9a',n:'ZWERGENSTUBE',k:'house',hh:6});
  zf(39,18,1,1,GR);
  mk('zstube','buedchen',39,18,'Zwergenstube','Zwergenstube besuchen');
 }else if(name==='schlaraff'){
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){const e=x<2||y<2||x>ZW-3||y>ZH-3;if(e&&r()<.75)zs(x,y,TR);else if(r()<.04)zs(x,y,TR);}
  zc(32,19,6.5,4,SH);
  zf(9,4,9,7,GR);zf(10,5,8,5,BL);z.BLD.push({x:10,y:5,w:8,h:5,c:'#e8b64a',n:'PUDDINGBERG',k:'pudding',hh:6});
  {const m=mk('pudding','sk',14,10,'Puddingberg','Puddingberg besuchen');m.sk='pudding';m.col='#ffb347';}
 }else if(name==='bayern'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=GR;
  for(let x=0;x<ZW;x++){const h=4+Math.round(Math.sin(x*.45)*1.3+Math.sin(x*.17)*1.6);for(let y=0;y<h;y++)zs(x,y,RK);}
  zc(35,22,7,4.4,SH);zc(35,22,4.8,2.8,DP);
  for(let i=0;i<44;i++){const x=R(1,ZW-2),y=R(8,ZH-2);if(zg(x,y)===GR&&!(x>=14&&x<=31&&y>=10&&y<=21)&&!(x>=33&&x<=44&&y>=7&&y<=13))zs(x,y,TR);}
  clr(20,15,1,GR);zf(18,12,6,3,BL);z.BLD.push({x:18,y:12,w:6,h:3,c:'#b5651d',n:'BIERGARTEN',k:'house',hh:6});
  mk('biergarten','buedchen',20,15,'Biergarten','Biergarten besuchen');
  clr(39,11,1,GR);zf(37,7,6,4,BL);z.BLD.push({x:37,y:7,w:6,h:4,c:'#e9e2d2',n:'',k:'burg',hh:6});
  {const m=mk('burg','sk',39,11,'Märchenschloss','Märchenschloss besuchen');m.sk='burg';m.col='#ffb347';}
  [[32,22],[38,22]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
 }else if(name==='portugal'){
  const sh=y=>4+Math.round(Math.sin(y*.5)*1.2);
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){const sv=sh(y);zs(x,y,x<sv-1?DP:x<sv?SH:x<sv+3?SA:SW);}
  for(let y=0;y<ZH;y++)for(let x=9;x<ZW;x++){if((x>ZW-3||y<2||y>ZH-3)&&r()<.7)zs(x,y,TR);}
  for(let i=0;i<14;i++){const x=R(9,ZW-2),y=R(2,ZH-2);if(zg(x,y)===SW&&(y<7||y>22))zs(x,y,TR);}
  const hc=['#e8c14a','#d86a4a','#4a8ec9','#e9e4d8','#6aaa7a','#c97fb0'];let hi=0;
  for(let x=10;x<=42;x+=4){zf(x,8,3,3,BL);z.BLD.push({x:x,y:8,w:3,h:3,c:hc[hi%6],n:'',k:hi%3===1?'azul':'house',hh:6});hi++;}
  clr(27,21,1,SW);clr(23,23,1,SW);
  for(let x=10;x<=42;x+=4){if(x===26)continue;zf(x,18,3,3,BL);z.BLD.push({x:x,y:18,w:3,h:3,c:hc[hi%6],n:'',k:hi%3===0?'azul':'house',hh:6});hi++;}
  zf(26,18,4,3,BL);z.BLD.push({x:26,y:18,w:4,h:3,c:'#c9a24a',n:'TASCA',k:'house',hh:6});
  mk('tasca','buedchen',27,21,'Tasca','Tasca besuchen');
  [[1,6],[1,19]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
 }else if(name==='wuppertal'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  for(let x=0;x<ZW;x++){const c=wcy(x);zs(x,c-1,SH);zs(x,c,DP);zs(x,c+1,SH);}
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.75)zs(x,y,TR);}
  for(let i=0;i<14;i++){const x=R(2,ZW-3),y=R(18,ZH-3);if(zg(x,y)===SW)zs(x,y,TR);}
  zf(14,wcy(14)-1,1,3,DK);zf(34,wcy(34)-1,1,3,DK);
  [7,25,41].forEach(x=>z.rides.push(mkRide('boat',x*TS+16,(wcy(x)-1)*TS+18,0)));
  const sc=['#3a4048','#444b54','#394450','#4a4640'];let hi=0;
  for(let x=3;x<=43;x+=4){zf(x,4,3,3,BL);z.BLD.push({x:x,y:4,w:3,h:3,c:sc[hi%4],n:'',k:'schiefer',hh:6});hi++;}
  for(let x=11;x<=35;x+=4){zf(x,20,3,3,BL);z.BLD.push({x:x,y:20,w:3,h:3,c:sc[hi%4],n:'',k:'schiefer',hh:6});hi++;}
  zf(16,8,7,4,BL);z.BLD.push({x:16,y:8,w:7,h:4,c:'#a8432f',n:'BRAUHAUS',k:'brau',hh:6});
  mk('brauhaus','buedchen',21,12,'Brauhaus','Brauhaus besuchen');
  {const m=mk('braum','sk',17,12,'Braumeister','Braumeister besuchen');m.sk='braum';m.col='#ffb347';}
 }else if(name==='oesterreich'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=GR;
  for(let x=0;x<ZW;x++){const h=5+Math.round(Math.sin(x*.4)*1.5+Math.sin(x*.15)*1.8);for(let y=0;y<h;y++)zs(x,y,RK);}
  zc(38,24,5.5,3.2,SH);zc(38,24,3.6,2,DP);
  for(let i=0;i<40;i++){const x=R(1,ZW-2),y=R(9,ZH-2);if(zg(x,y)===GR&&!(x>=16&&x<=30&&y>=10&&y<=21)&&!(x>=34&&x<=44&&y>=8&&y<=14))zs(x,y,TR);}
  clr(22,15,1,GR);zf(20,12,6,3,BL);z.BLD.push({x:20,y:12,w:6,h:3,c:'#8a5a3a',n:'KAFFEEHAUS',k:'house',hh:6});
  mk('kaffee','buedchen',22,15,'Kaffeehaus','Kaffeehaus besuchen');
  clr(39,13,1,GR);zf(36,9,7,4,BL);z.BLD.push({x:36,y:9,w:7,h:4,c:'#e8d8a8',n:'BALLSAAL',k:'ball',hh:6});
  {const m=mk('walzer','sk',39,13,'Ballsaal','Ballsaal besuchen');m.sk='walzer';m.col='#ffb347';}
  [[37,24],[40,24]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
  kOesi(z,{zs:zs,zg:zg,mk:mk});
 }else if(name==='koeln'){
  const kc=x=>26+Math.round(Math.sin(x*.25));
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  for(let x=0;x<ZW;x++){const c=kc(x);zs(x,c-1,SH);zs(x,c,DP);zs(x,c+1,DP);for(let y=c+2;y<ZH;y++)zs(x,y,SH);}
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2)&&r()<.75)zs(x,y,TR);}
  zf(20,3,8,6,BL);z.BLD.push({x:20,y:3,w:8,h:6,c:'#7d7f86',n:'KÖLNER DOM',k:'dom',hh:6});
  const hc=['#e8c14a','#d86a4a','#4a8ec9','#6aaa7a','#c97fb0','#e9e4d8'];let hi=0;
  [3,7,11,26,30,34,38,42].forEach(x=>{zf(x,11,3,3,BL);z.BLD.push({x:x,y:11,w:3,h:3,c:hc[hi%6],n:'',k:'house',hh:6});hi++;});
  [3,7,11,31,35,39].forEach(x=>{zf(x,3,3,3,BL);z.BLD.push({x:x,y:3,w:3,h:3,c:hc[hi%6],n:'',k:'house',hh:6});hi++;});
  zf(16,11,7,3,BL);z.BLD.push({x:16,y:11,w:7,h:3,c:'#b5503a',n:'KÖLSCH-HAUS',k:'house',hh:6});
  mk('koelsch','buedchen',19,14,'Kölsch-Haus','Kölsch-Haus besuchen');
  [[10,0],[30,0]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,kc(q[0])*TS+16,0)));
 }else if(name==='feldweg'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=GR;
  zf(0,15,ZW,2,SA);zf(4,17,2,6,SA);zf(23,17,2,5,SA);
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.8)zs(x,y,TR);}
  for(let i=0;i<10;i++){const x=R(2,ZW-3),y=R(24,ZH-3);if(zg(x,y)===GR)zs(x,y,TR);}
  zf(9,19,5,3,BL);z.BLD.push({x:9,y:19,w:5,h:3,c:'#b8864a',n:'GARTENHAUS',k:'house',hh:6});
  zf(27,19,6,3,BL);z.BLD.push({x:27,y:19,w:6,h:3,c:'#8a5a3a',n:'HOFLADEN',k:'house',hh:6});
  mk('hofladen','buedchen',29,22,'Hofladen','Hofladen besuchen');
  zs(16,18,LC);zs(17,18,LC);zs(36,18,LC);zs(37,18,LC);
  clr(24,14,0,GR);
  {const m=mk('tafel','sk',24,14,'Info-Tafel','Info-Tafel lesen');m.sk='tafel';m.col='#ffb347';}
  medFeld(z,{zs:zs,zg:zg,mk:mk});
 }else if(name==='sender'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.75)zs(x,y,TR);}
  [['RTL',2,'#8a8f9a'],['PRO7',13,'#7f8fa0'],['ARD',24,'#8f98a3'],['ZDF',35,'#9a998f']].forEach(q=>{zf(q[1],3,9,6,BL);z.BLD.push({x:q[1],y:3,w:9,h:6,c:q[2],n:'',sn:q[0],k:'sender',hh:8});});
  clr(24,17,1,SW);
  zf(23,16,3,1,BL);z.BLD.push({x:23,y:16,w:3,h:1,c:'#b5651d',n:'WURFBUDE',k:'house',hh:6});
  {const m=mk('wurf','sk',24,17,'Wurfbude','Wurfbude besuchen');m.sk='wurf';m.col='#ffb347';}
 }else if(name==='helden'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.8)zs(x,y,TR);}
  zf(22,8,4,3,BL);z.BLD.push({x:22,y:8,w:4,h:3,c:'#f2d03a',n:'GROSSE GUMMIENTE',k:'ente',hh:6});
  clr(24,14,1,SW);
  {const m=mk('prue','sk',24,14,'Heldenprüfung','Heldenprüfung ablegen');m.sk='prue';m.col='#ffb347';}
 }else if(name==='amt'){
  for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
  for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.8)zs(x,y,TR);}
  zf(14,3,20,6,BL);z.BLD.push({x:14,y:3,w:20,h:6,c:'#cfc7b0',n:'AMT FÜR ALLES',k:'amt',hh:8});
  clr(24,12,1,SW);clr(32,12,1,SW);
  zf(23,11,2,1,BL);z.BLD.push({x:23,y:11,w:2,h:1,c:'#c0392b',n:'NUMMER',k:'house',hh:6});
  zf(31,11,3,1,BL);z.BLD.push({x:31,y:11,w:3,h:1,c:'#8a5a3a',n:'STEMPEL',k:'house',hh:6});
  {const m=mk('nummer','sk',24,12,'Wartenummern-Automat','Wartenummer ziehen');m.sk='nummer';m.col='#ffb347';}
  {const m=mk('stempel','sk',32,12,'Stempeltisch','Stempeltisch benutzen');m.sk='stempel';m.col='#ffb347';}
 }else if(name==='fpark'){
  genFpark(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='malle'){
  genMalle(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='gallien'){
  genGallien(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='zoo'){
  genZoo(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='plantage'){
  genPlantage(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='freibad'){
  genFreibad(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='camping'){
  genCamping(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='gamsbahn'){
  genGamsbahn(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }else if(name==='holly'){
  genHolly(z,{zs:zs,zg:zg,zf:zf,mk:mk,R:R,r:r});
 }
 const po=ZPO[name],HP=ZHOME[name]||[6,25],hx=HP[0],hy=HP[1],wx=ZWILD[name][0],wy=ZWILD[name][1];
 clr(hx,hy,2,base);clr(wx,wy,1,base);
 const hm=mk('home','portal',hx,hy,po.home[1],po.home[2],po.home[0],po.home[3]);hm.home=true;if(po.home[4]){hm.home=false;hm.to=po.home[4];}
 const wm=mk('wild','portal',wx,wy,po.wild[1],po.wild[2],po.wild[0],po.wild[3]);if(po.wild[4])wm.to=po.wild[4];
 z.spawn=z.spawnRide?{x:z.rides[0].x,y:z.rides[0].y}:{x:(hx+2)*TS+16,y:hy*TS+16};
 const q=new Int32Array(ZW*ZH).fill(-1);let h=0,t=0;
 const s0=Math.floor(z.spawn.y/TS)*ZW+Math.floor(z.spawn.x/TS);q[t++]=s0;const seen=new Uint8Array(ZW*ZH);seen[s0]=1;
 while(h<t){const c=q[h++],cx=c%ZW,cy=(c-cx)/ZW;[[1,0],[-1,0],[0,1],[0,-1]].forEach(o=>{const nx=cx+o[0],ny=cy+o[1];if(nx<0||ny<0||nx>=ZW||ny>=ZH)return;const k=ny*ZW+nx;if(seen[k]||(SOL[Tz[k]]===1&&!(I.swim&&Tz[k]===DP)))return;seen[k]=1;q[t++]=k;});}
 const ok=z.MKS.every(m=>seen[Math.floor(m.y/TS)*ZW+Math.floor(m.x/TS)]);
 if(!ok){for(let i=0;i<ZW*ZH;i++){const v=Tz[i];if(v===TR||v===UM||v===LC||v===CY||v===MU)Tz[i]=base;}}
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){const v=Tz[y*ZW+x];if(v===MU)z.glows.push({x:x*TS+16,y:y*TS+16,c:'#7dffb0'});else if(v===CY)z.glows.push({x:x*TS+16,y:y*TS+16,c:'#a58bff'});}
 return z;
}
function zoneTile(c,t,px,py,h,nm,x,y,g){
 if(t===SA){c.fillStyle=h<3?'#e8d49c':h<6?'#e2cd92':'#dcc688';c.fillRect(px,py,TS,TS);if(h===1){c.fillStyle='rgba(120,90,40,.25)';c.fillRect(px+8,py+10,3,2);}}
 else if(t===SH||t===DP){
  const deep=t===DP;c.fillStyle=deep?'#2c80b4':'#5ec0d6';if(nm==='hoehle')c.fillStyle=deep?'#173653':'#25506f';if(nm==='wal')c.fillStyle=deep?'#2a8fa8':'#6cc6c6';if(nm==='schlaraff')c.fillStyle='#f3efe6';c.fillRect(px,py,TS,TS);
  if(h<3){c.fillStyle='rgba(255,255,255,.18)';c.fillRect(px+4+h*3,py+8+h*3,12,2);}
  if(!deep&&nm==='strand'&&g(x,y+1)===SA){c.fillStyle='rgba(255,255,255,.7)';c.fillRect(px,py+TS-4,TS,3);}
 }

 else if(t===GR&&(nm==='maerchen'||nm==='schlaraff'||nm==='bayern'||nm==='oesterreich'||nm==='feldweg'||nm==='fpark'||nm==='camping')){c.fillStyle=h<3?'#7cbf5c':h<6?'#74b755':'#82c563';c.fillRect(px,py,TS,TS);if(h===1){c.fillStyle='#fff';c.fillRect(px+7,py+9,3,3);c.fillStyle='#f4d03f';c.fillRect(px+8,py+10,1,1);}else if(h===3){c.fillStyle='#ff7fb0';c.fillRect(px+19,py+17,3,3);c.fillStyle='#fff3a0';c.fillRect(px+20,py+18,1,1);}else if(h===5){c.fillStyle='#b58cff';c.fillRect(px+12,py+22,3,3);}else if(h===2){c.fillStyle='rgba(255,255,255,.25)';c.fillRect(px+6,py+14,8,2);}}
 else if(t===GR){c.fillStyle=h<3?'#6fae56':h<6?'#68a64f':'#74b45c';c.fillRect(px,py,TS,TS);if(h===2){c.fillStyle='rgba(255,255,255,.35)';c.fillRect(px+8,py+10,2,2);c.fillStyle='#f4d03f';c.fillRect(px+20,py+18,2,2);}}
 else if(t===SW&&nm==='malle'){c.fillStyle=((x+y)&1)?'#e8c9a0':'#e0bd90';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(170,110,60,.2)';c.fillRect(px,py,TS,1);c.fillRect(px,py,1,TS);}
 else if(t===SW&&nm==='fpark'){c.fillStyle=((x+y)&1)?'#eadcbc':'#e3d2ae';c.fillRect(px,py,TS,TS);if(h===1||h===5){c.fillStyle=['#ff4d7a','#5ff0ff','#ffd23f','#7bd86a'][(x*7+y*3)&3];c.fillRect(px+8+h*2,py+10,3,3);}}
 else if(t===RD&&nm==='fpark'){c.fillStyle=h<4?'#2b2e3c':'#282b38';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(95,240,255,.1)';c.fillRect(px,py,TS,1);c.fillRect(px,py,1,TS);}
 else if(t===SW&&nm==='freibad'){c.fillStyle=((x+y)&1)?'#eaf2f6':'#dfeaf0';c.fillRect(px,py,TS,TS);c.strokeStyle='rgba(110,150,175,.28)';c.strokeRect(px+.5,py+.5,TS-1,TS-1);}
 else if(t===SW&&nm==='portugal'){c.fillStyle=((x+y)&1)?'#ede7d9':'#e4dccb';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(60,60,75,.3)';for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(((a+b+x+y)&1)===0)c.fillRect(px+2+a*8,py+2+b*8,4,4);}
 else if(t===SW){c.fillStyle=h<4?'#b9a58f':'#b09b84';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(90,60,40,.28)';c.fillRect(px,py+15,TS,1);c.fillRect(px+((y&1)?8:20),py,1,15);c.fillRect(px+((y&1)?20:8),py+16,1,16);}
 else if(t===DK){c.fillStyle='#a67c3a';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(60,35,10,.4)';for(let k=0;k<4;k++)c.fillRect(px,py+k*8+7,TS,1);}
 else if(t===FD){c.fillStyle='#4f8a3a';c.fillRect(px,py,TS,TS);const tc=['#e5504d','#f4d03f','#e87fb5','#ff9a3c'][((x>>1)+y)&3];for(let a=0;a<4;a++)for(let b=0;b<3;b++){c.fillStyle=tc;c.fillRect(px+3+a*7,py+4+b*10,4,5);c.fillStyle='#2f6a2a';c.fillRect(px+4+a*7,py+9+b*10,2,3);}}
 else if(t===AS){c.fillStyle=h<3?'#3a3231':h<6?'#332c2b':'#3f3736';c.fillRect(px,py,TS,TS);if(h===0){c.fillStyle='#7a2a10';c.fillRect(px+6,py+14,14,2);c.fillRect(px+16,py+16,2,8);}}
 else if(t===LV){c.fillStyle='#e8501a';c.fillRect(px,py,TS,TS);c.fillStyle=h<3?'#ffb13a':'#ff7a1a';c.fillRect(px+4+h*2,py+6+h,10,6);c.fillStyle='#9a2a0a';c.fillRect(px+18,py+18,8,5);}
 else if(t===SN){c.fillStyle=h<3?'#eef3f8':h<6?'#e4ecf4':'#f5f8fb';c.fillRect(px,py,TS,TS);if(h===2){c.fillStyle='rgba(120,150,190,.25)';c.fillRect(px+6,py+20,14,3);}}
 else if(t===IC){c.fillStyle='#b9dcf0';c.fillRect(px,py,TS,TS);c.fillStyle='rgba(255,255,255,.6)';c.fillRect(px+4+h*2,py+10,12,2);c.fillRect(px+14,py+20,8,1);}
 else if(t===CF&&nm==='wal'){c.fillStyle=h<3?'#d98aa0':h<6?'#d27f97':'#de93a8';c.fillRect(px,py,TS,TS);if(h===2){c.fillStyle='rgba(255,255,255,.14)';c.fillRect(px+6,py+8,14,5);}if(h===5){c.fillStyle='rgba(120,30,60,.16)';c.fillRect(px+14,py+18,10,4);}}
 else if(t===CF){c.fillStyle=h<3?'#352f40':h<6?'#2f2a3a':'#3b3547';c.fillRect(px,py,TS,TS);if(h===4){c.fillStyle='rgba(255,255,255,.05)';c.fillRect(px+8,py+8,6,4);}}
 else if(t===RK){
  const col=nm==='vulkan'?['#241d1c','#4a3a38']:(nm==='berge'||nm==='gamsbahn')?['#7d8590','#a9b2bd']:(nm==='bayern'||nm==='oesterreich')?['#8b8478','#b5ad9c']:nm==='wal'?['#7a2a45','#a8456a']:['#14111b','#2e2840'];
  c.fillStyle=col[0];c.fillRect(px,py,TS,TS);
  if(g(x,y+1)!==RK){c.fillStyle=col[1];c.fillRect(px,py+TS-8,TS,8);}
  if(h<2){c.fillStyle='rgba(255,255,255,.07)';c.fillRect(px+6+h*6,py+6,10,8);}
  if((nm==='berge'||nm==='bayern'||nm==='oesterreich'||nm==='gamsbahn')&&g(x,y-1)!==RK){c.fillStyle='#f4f8fb';c.fillRect(px,py,TS,8);}
 }
 else{c.fillStyle='#ff00ff';c.fillRect(px,py,TS,TS);}
}
function renderZone(z){
 const c=z.WC.getContext('2d'),Tz=z.T,nm=z.name;
 const g=(x,y)=>(x<0||y<0||x>=ZW||y>=ZH)?RK:Tz[y*ZW+x];
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){
  let t=Tz[y*ZW+x];
  if(t===TR||t===UM||t===LC||t===FN||t===BL||t===CY||t===MU)t=z.base;
  zoneTile(c,t,x*TS,y*TS,hash(x,y)&7,nm,x,y,g);
 }
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){
  const t=Tz[y*ZW+x],px=x*TS+16,py=y*TS+16;
  if(t===TR){
   c.fillStyle='rgba(0,0,0,.25)';c.beginPath();c.ellipse(px+4,py+10,12,6,0,0,6.283);c.fill();
   if(nm==='strand'||nm==='portugal'||nm==='malle'||nm==='holly'){
    c.strokeStyle='#7a5a32';c.lineWidth=4;c.beginPath();c.moveTo(px,py+8);c.lineTo(px+2,py-2);c.stroke();
    c.strokeStyle='#2f9a3f';c.lineWidth=3;
    for(let k=0;k<6;k++){const a=k/6*6.283;c.beginPath();c.moveTo(px+2,py-2);c.lineTo(px+2+Math.cos(a)*14,py-2+Math.sin(a)*10);c.stroke();}
    c.fillStyle='#6b4a1f';c.beginPath();c.arc(px+1,py-1,2.5,0,6.283);c.fill();c.lineWidth=1;
   }else if(nm==='maerchen'||nm==='schlaraff'){
    const hv=hash(x,y)%4,cc=(nm==='schlaraff'?[['#ff9ec7','#ffc2dc'],['#9ed8ff','#c4e8ff'],['#ffe08a','#fff0b8'],['#b9f0c0','#d8f8dc']]:[['#2f7a3f','#3f9a4f'],['#357f5a','#46a374'],['#4f8a2f','#6aae3f'],['#a8527a','#d4709f']])[hv];
    c.fillStyle='#5a3d22';c.fillRect(px-3,py+1,6,11);c.fillStyle='#2b1a0e';c.beginPath();c.ellipse(px,py+7,1.8,2.6,0,0,6.283);c.fill();
    c.fillStyle=cc[0];c.beginPath();c.arc(px,py-5,14,0,6.283);c.fill();c.fillStyle=cc[1];c.beginPath();c.arc(px-4,py-9,8,0,6.283);c.fill();c.beginPath();c.arc(px+6,py-4,6,0,6.283);c.fill();
    c.fillStyle='rgba(255,255,255,.45)';c.fillRect(px-6,py-10,2,2);c.fillRect(px+4,py-8,2,2);
   }else if(nm==='rhein'||nm==='amsterdam'||nm==='bayern'||nm==='wuppertal'||nm==='oesterreich'||nm==='koeln'||nm==='feldweg'||nm==='sender'||nm==='helden'||nm==='amt'||nm==='fpark'||nm==='zoo'||nm==='gallien'||nm==='plantage'||nm==='camping'||nm==='freibad'){
    c.fillStyle='rgba(0,0,0,.25)';c.beginPath();c.ellipse(px+4,py+10,12,6,0,0,6.283);c.fill();
    c.fillStyle='#5a3d22';c.fillRect(px-2,py+2,4,10);c.fillStyle='#2f7a3f';c.beginPath();c.arc(px,py-4,12,0,6.283);c.fill();c.fillStyle='#3f9a4f';c.beginPath();c.arc(px-3,py-7,7,0,6.283);c.fill();
   }else{
    c.fillStyle='#5a3d22';c.fillRect(px-2,py+4,4,8);
    c.fillStyle='#1f5a3a';c.beginPath();c.moveTo(px,py-16);c.lineTo(px+13,py+4);c.lineTo(px-13,py+4);c.closePath();c.fill();
    c.fillStyle='#2b7a4b';c.beginPath();c.moveTo(px,py-10);c.lineTo(px+10,py+2);c.lineTo(px-10,py+2);c.closePath();c.fill();
    c.fillStyle='#f4f8fb';c.beginPath();c.moveTo(px,py-16);c.lineTo(px+6,py-6);c.lineTo(px-6,py-6);c.closePath();c.fill();
   }
  }else if(t===UM){
   const cols=['#e5604d','#2e86c1','#f1c40f','#27ae60'];
   c.fillStyle='rgba(0,0,0,.2)';c.beginPath();c.ellipse(px+4,py+8,14,8,0,0,6.283);c.fill();
   c.fillStyle=cols[hash(x,y)%4];c.beginPath();c.arc(px,py,13,0,6.283);c.fill();
   c.fillStyle='#fff';for(let k=0;k<4;k++){c.beginPath();c.moveTo(px,py);c.arc(px,py,13,k*1.571,k*1.571+.5);c.closePath();c.fill();}
   c.fillStyle='#5a4a3a';c.beginPath();c.arc(px,py,2,0,6.283);c.fill();
  }else if(t===LC&&nm==='wal'){
   c.fillStyle='#4a2a6a';c.fillRect(px-14,py-10,28,20);c.fillStyle='#8a5fb3';c.fillRect(px-12,py-8,24,11);c.fillStyle='#ffd23f';c.fillRect(px-4,py+3,8,4);
  }else if(t===LC){
   c.fillStyle='#fff';c.fillRect(px-13,py-9,26,18);c.fillStyle=['#e5604d','#2e86c1','#f1c40f'][hash(x,y)%3];c.fillRect(px-13,py-9,26,6);c.fillRect(px-13,py+3,26,6);c.strokeStyle='rgba(0,0,0,.3)';c.strokeRect(px-12.5,py-8.5,25,17);
  }else if(t===FN&&nm==='plantage'){fencePlant(c,px,py,g,x,y);
  }else if(t===FN&&(nm==='zoo'||nm==='gallien')){fenceZG(c,nm,px,py,g,x,y);
  }else if(t===FN&&nm==='fpark'){
   const l=g(x-1,y)===FN,rr=g(x+1,y)===FN,u=g(x,y-1)===FN,d=g(x,y+1)===FN;
   c.fillStyle='rgba(0,0,0,.25)';if(l||rr)c.fillRect(px-16,py+1,32,6);if(u||d)c.fillRect(px-1,py-16,6,32);
   c.fillStyle='#ffd23f';if(l||rr)c.fillRect(px-16,py-3,32,5);if(u||d)c.fillRect(px-3,py-16,5,32);
   c.fillStyle='#e5504d';c.beginPath();c.arc(px,py,5,0,6.283);c.fill();c.fillStyle='#fff';c.beginPath();c.arc(px-1,py-1,1.6,0,6.283);c.fill();
  }else if(t===FN&&nm==='strand'){
   const l=g(x-1,y)===FN,rr=g(x+1,y)===FN;
   c.strokeStyle='rgba(255,255,255,.85)';c.lineWidth=1;
   c.fillStyle='rgba(255,255,255,.35)';c.fillRect(px-16,py-8,32,10);
   for(let k=0;k<5;k++){c.beginPath();c.moveTo(px-16+k*8,py-8);c.lineTo(px-16+k*8,py+2);c.stroke();}
   if(!l){c.fillStyle='#5a4a3a';c.fillRect(px-16,py-14,3,26);}
   if(!rr){c.fillStyle='#5a4a3a';c.fillRect(px+13,py-14,3,26);}
  }else if(t===CY){
   c.fillStyle='rgba(165,139,255,.35)';c.beginPath();c.arc(px,py,14,0,6.283);c.fill();
   c.fillStyle='#a58bff';c.beginPath();c.moveTo(px-3,py+9);c.lineTo(px-8,py-2);c.lineTo(px-3,py-12);c.lineTo(px+2,py-2);c.lineTo(px+2,py+9);c.closePath();c.fill();
   c.fillStyle='#5ff0ff';c.beginPath();c.moveTo(px+2,py+9);c.lineTo(px+3,py-6);c.lineTo(px+9,py+2);c.lineTo(px+9,py+9);c.closePath();c.fill();
   c.fillStyle='rgba(255,255,255,.7)';c.fillRect(px-4,py-8,2,6);
  }else if(t===MU&&nm==='maerchen'){
   c.fillStyle='rgba(0,0,0,.2)';c.beginPath();c.ellipse(px+3,py+10,11,5,0,0,6.283);c.fill();
   c.fillStyle='#f4ead0';c.fillRect(px-3,py,6,10);
   c.fillStyle='#d8352f';c.beginPath();c.ellipse(px,py+1,12,9,0,Math.PI,0);c.fill();c.fillRect(px-12,py,24,2);
   c.fillStyle='#fff';c.beginPath();c.arc(px-5,py-4,2.2,0,6.283);c.arc(px+3,py-6,2.6,0,6.283);c.arc(px+7,py-1,1.8,0,6.283);c.fill();
  }else if(t===MU&&nm==='wal'){
   c.fillStyle='rgba(255,200,240,.35)';c.beginPath();c.arc(px,py,12,0,6.283);c.fill();c.fillStyle='#ffd6f2';c.beginPath();c.arc(px,py,5,0,6.283);c.fill();c.fillStyle='#fff';c.fillRect(px-1,py-2,2,2);
  }else if(t===MU){
   c.fillStyle='rgba(125,255,176,.3)';c.beginPath();c.arc(px,py,13,0,6.283);c.fill();
   c.fillStyle='#d8e8d0';c.fillRect(px-2,py,4,9);
   c.fillStyle='#3fe08f';c.beginPath();c.ellipse(px,py,10,7,0,Math.PI,0);c.fill();c.fillRect(px-10,py,20,2);
   c.fillStyle='#d9ffe8';c.fillRect(px-4,py-4,3,2);c.fillRect(px+3,py-3,2,2);
  }
 }
 if(nm==='fpark')fparkStatic(c);
 z.BLD.forEach(b=>drawBuilding(c,b));
 if(nm==='zoo'||nm==='gallien')zgStatic(c,z);
 if(nm==='plantage')plantStatic(c,z);
 kStatic(c,z);medStatic(c,z);
 const mc=z.MM.getContext('2d'),S=6;
 mc.clearRect(0,0,304,192);
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){
  const t=Tz[y*ZW+x];
  mc.fillStyle=t===RD?'#2b2e3c':t===GR?'#6fae56':t===SW?'#b9a58f':t===DK?'#a67c3a':t===FD?'#e0508a':t===SA?'#e2cd92':t===SH?'#5ec0d6':t===DP?'#2c80b4':t===AS?'#3a3231':t===LV?'#e8501a':t===SN?'#eef3f8':t===IC?'#b9dcf0':t===CF?'#352f40':t===RK?(nm==='berge'?'#7d8590':(nm==='bayern'||nm==='oesterreich')?'#8b8478':nm==='vulkan'?'#241d1c':'#14111b'):t===TR?'#2f7a3f':t===BL?'#8a6a5a':t===MU?'#3fe08f':t===CY?'#a58bff':'#c8b48a';
  if(nm==='hoehle'&&(t===SH||t===DP))mc.fillStyle='#25506f';
  if(nm==='wal'&&t===CF)mc.fillStyle='#d98aa0';
  if(nm==='wal'&&t===RK)mc.fillStyle='#7a2a45';
  if(nm==='wal'&&t===LC)mc.fillStyle='#8a5fb3';
  if((nm==='maerchen'||nm==='schlaraff')&&t===GR)mc.fillStyle='#7cbf5c';
  if(nm==='schlaraff'&&t===SH)mc.fillStyle='#f3efe6';
  if(nm==='plantage'&&t===FD)mc.fillStyle='#3f8a3a';
  mc.fillRect(x*S,y*S,S,S);
 }
}
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');
const mm=document.getElementById('mm'),mctx=mm.getContext('2d');
let timeNow=0;
function circle(x,y,r){ctx.beginPath();ctx.arc(x,y,r,0,6.283);ctx.fill();}
function drawCar(x,y,a,col,kind,t){
 ctx.save();ctx.translate(x,y);ctx.rotate(a);
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(-16,-8,36,20);
 ctx.fillStyle=col;ctx.fillRect(-18,-10,36,20);
 if(kind==='van'){ctx.fillStyle='#e9e3d0';ctx.fillRect(-18,-10,24,20);ctx.fillStyle='#d4a017';ctx.fillRect(-14,-3,14,6);}
 else{ctx.fillStyle=bcol(col.length===7?col:'#888888',-35);ctx.fillRect(-8,-8,16,16);}
 if(kind==='cop'||kind==='chase'){ctx.fillStyle='#1b3a8a';ctx.fillRect(-8,-10,12,20);ctx.fillStyle='#f4f4f4';ctx.fillRect(-18,-10,10,20);ctx.fillRect(8,-10,10,20);
  const on=Math.floor(t*6)%2===0&&kind==='chase';ctx.fillStyle=on?'#ff3030':'#3070ff';ctx.fillRect(-2,-8,5,7);ctx.fillStyle=on?'#3070ff':'#ff3030';ctx.fillRect(-2,1,5,7);}
 ctx.fillStyle='#1c2a3a';ctx.fillRect(8,-8,6,16);
 ctx.fillStyle='#ffe9a0';ctx.fillRect(16,-9,3,5);ctx.fillRect(16,4,3,5);
 ctx.fillStyle='#a02020';ctx.fillRect(-19,-9,2,4);ctx.fillRect(-19,5,2,4);
 ctx.restore();
}
function drawPerson(x,y,a,col,kind,walk,sc){
 ctx.save();ctx.translate(x,y);if(sc)ctx.scale(sc,sc);
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(2,3,8,6,0,0,6.283);ctx.fill();
 ctx.rotate(a);
 if(kind==='me')drawCape();
 const sw=Math.sin(walk||0)*3;
 ctx.fillStyle=col;ctx.beginPath();ctx.ellipse(0,0,4.5,7.5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e8c39e';circle(sw,-7,2.2);circle(-sw,7,2.2);
 ctx.fillStyle=kind==='cop'?'#14233f':kind==='thug'?'#222':'#4a3a2a';circle(0,0,4.2);
 if(kind==='cop'){ctx.fillStyle='#2a4a8a';circle(0,0,3.2);ctx.fillStyle='#fff';ctx.fillRect(-.5,-1,3,2);}
 ctx.restore();
}
function drawLie(x,y,col){
 ctx.fillStyle='rgba(0,0,0,.2)';ctx.fillRect(x-13,y-6,28,17);
 ctx.fillStyle=col;ctx.fillRect(x-14,y-8,28,16);
 ctx.fillStyle='rgba(255,255,255,.8)';ctx.fillRect(x-14,y-2,28,3);
 ctx.fillStyle='#e8c39e';circle(x-8,y,3.6);ctx.fillRect(x-4,y-3,16,6);
 ctx.fillStyle='#222';ctx.fillRect(x-10,y-2,4,2);
}
function drawSnowman(p){
 const w=p.wob>0?Math.sin(timeNow*30)*2*p.wob:0;
 ctx.fillStyle='rgba(0,0,0,.2)';ctx.beginPath();ctx.ellipse(p.x+3,p.y+9,11,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#fff';circle(p.x,p.y+3,9);circle(p.x,p.y-5,7);
 ctx.fillStyle='#e6edf4';circle(p.x+2,p.y+5,5);
 ctx.fillStyle='#fff';circle(p.x+w,p.y-13,5.5);
 ctx.fillStyle='#222';circle(p.x+w-2,p.y-14,1);circle(p.x+w+2,p.y-14,1);circle(p.x,p.y-4,1);circle(p.x,p.y+1,1);
 ctx.fillStyle='#ff7a1a';ctx.beginPath();ctx.moveTo(p.x+w,p.y-12);ctx.lineTo(p.x+w+8,p.y-11);ctx.lineTo(p.x+w,p.y-10);ctx.fill();
 ctx.fillStyle='#222';ctx.fillRect(p.x+w-5,p.y-20,10,3);ctx.fillRect(p.x+w-3,p.y-25,6,6);
}
function drawSitter(x,y){
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x+2,y+6,9,6,0,0,6.283);ctx.fill();
 ctx.fillStyle='#d4a017';ctx.beginPath();ctx.ellipse(x,y+1,7.5,5.5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#4a3a2a';circle(x,y,4.2);
 ctx.fillStyle='#e8c39e';circle(x-7,y+4,2.2);circle(x+7,y+4,2.2);
 ctx.fillStyle='#caa24a';ctx.fillRect(x+6,y+1,3,7);
}
function drawPick(k){
 if(k.t==='dose'){ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(k.x-2,k.y-3,7,10);ctx.fillStyle='#c9ced6';ctx.fillRect(k.x-3,k.y-5,6,10);ctx.fillStyle='#e5604d';ctx.fillRect(k.x-3,k.y-1,6,3);ctx.fillStyle='rgba(255,255,255,.8)';ctx.fillRect(k.x-2,k.y-5,1.5,10);}
 else{ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(k.x+1,k.y+2,6,4,0,0,6.283);ctx.fill();ctx.fillStyle='#8d8d92';ctx.beginPath();ctx.ellipse(k.x,k.y,5.5,4,0,0,6.283);ctx.fill();ctx.fillStyle='rgba(255,255,255,.35)';ctx.fillRect(k.x-3,k.y-2,3,1.5);}
}
function drawPortalObj(m,t){
 const x=m.x,y=m.y,pl=Math.sin(t*3);
 ctx.fillStyle='rgba(192,107,255,'+(.16+.1*pl)+')';circle(x,y,28+pl*3);
 const o=m.obj;
 ctx.fillStyle='rgba(0,0,0,.3)';
 if(o==='gully'){ctx.fillStyle='#262626';circle(x,y,14);ctx.fillStyle='#4a4a4a';circle(x,y,12);ctx.strokeStyle='#2b2b2b';for(let k=-8;k<=8;k+=4){ctx.beginPath();ctx.moveTo(x-10,y+k);ctx.lineTo(x+10,y+k);ctx.stroke();}ctx.fillStyle='rgba(120,255,140,'+(.35+.25*pl)+')';circle(x,y,6);}
 else if(o==='telefon'){ctx.fillRect(x-9,y-8,22,22);ctx.fillStyle='#f2c61c';ctx.fillRect(x-11,y-12,22,24);ctx.fillStyle='#7ec8e8';ctx.fillRect(x-8,y-9,16,11);ctx.fillStyle='#222';ctx.fillRect(x-4,y+4,8,5);ctx.fillStyle='#d4a017';ctx.fillRect(x-11,y-12,22,2);}
 else if(o==='dixi'){ctx.fillRect(x-8,y-8,20,22);ctx.fillStyle='#2e86c1';ctx.fillRect(x-10,y-13,20,26);ctx.fillStyle='#fff';ctx.fillRect(x-10,y-13,20,4);ctx.fillStyle='#1b5a85';ctx.fillRect(x-6,y-6,12,16);ctx.fillStyle='#ffd23f';ctx.fillRect(x+2,y+1,2,2);}
 else if(o==='kuehl'){ctx.fillRect(x-8,y-9,20,24);ctx.fillStyle='#f2f4f7';ctx.fillRect(x-10,y-14,20,28);ctx.strokeStyle='#9aa3ad';ctx.strokeRect(x-9.5,y-13.5,19,27);ctx.beginPath();ctx.moveTo(x-10,y-2);ctx.lineTo(x+10,y-2);ctx.stroke();ctx.fillStyle='#9aa3ad';ctx.fillRect(x+6,y-10,2,6);ctx.fillRect(x+6,y+2,2,8);ctx.fillStyle='rgba(255,240,150,'+(.4+.3*pl)+')';ctx.fillRect(x-8,y-12,14,3);}
 else if(o==='strandkorb'){ctx.fillStyle='#e0b66a';ctx.beginPath();ctx.ellipse(x,y+2,14,12,0,0,6.283);ctx.fill();ctx.fillStyle='#fff';ctx.beginPath();ctx.ellipse(x,y-4,12,9,0,Math.PI,0);ctx.fill();ctx.fillStyle='#e5604d';for(let k=-10;k<=6;k+=8)ctx.fillRect(x+k,y-12,5,9);ctx.fillStyle='#a67c2e';ctx.fillRect(x-12,y+3,24,2);}
 else if(o==='surfbrett'){ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.ellipse(x,y,8,15,0,0,6.283);ctx.fill();ctx.fillStyle='#e5604d';ctx.fillRect(x-1.5,y-13,3,26);ctx.fillStyle='#2e86c1';ctx.fillRect(x-7,y-4,14,3);}
 else if(o==='notausgang'){ctx.fillRect(x-10,y-10,24,22);ctx.fillStyle='#1c8a45';ctx.fillRect(x-12,y-14,24,26);ctx.fillStyle='#fff';ctx.fillRect(x-8,y-10,16,10);ctx.fillStyle='#1c8a45';ctx.fillRect(x-1,y-9,3,8);ctx.fillRect(x-5,y-7,5,2);ctx.fillStyle='#fff';ctx.fillRect(x-6,y+3,12,3);}
 else if(o==='lavalampe'){ctx.fillStyle='#444';ctx.fillRect(x-8,y+8,16,6);ctx.fillStyle='#d6401a';ctx.beginPath();ctx.moveTo(x-5,y+8);ctx.lineTo(x-8,y-6);ctx.quadraticCurveTo(x,y-18,x+8,y-6);ctx.lineTo(x+5,y+8);ctx.closePath();ctx.fill();ctx.fillStyle='#ffd23f';circle(x-1,y+1+pl*2,3.5);circle(x+2,y-6-pl*2,2.5);ctx.fillStyle='#444';ctx.fillRect(x-4,y-17,8,3);}
 else if(o==='huette'){ctx.fillRect(x-10,y-8,24,22);ctx.fillStyle='#7a4a24';ctx.fillRect(x-12,y-14,24,28);ctx.fillStyle='#5a3416';ctx.beginPath();ctx.arc(x,y+2,8,Math.PI,0);ctx.fillRect(x-8,y+2,16,10);ctx.fill();ctx.fillStyle='#ffd23f';circle(x+4,y+6,1.5);ctx.fillStyle='#f4f8fb';ctx.fillRect(x-12,y-14,24,4);}
 else if(o==='schlitten'){ctx.fillRect(x-9,y-8,22,18);ctx.fillStyle='#b5651d';ctx.fillRect(x-10,y-10,20,14);ctx.fillStyle='#e5604d';ctx.fillRect(x-8,y-8,16,4);ctx.strokeStyle='#777';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x-12,y+7);ctx.lineTo(x+12,y+7);ctx.moveTo(x-12,y+7);ctx.quadraticCurveTo(x-16,y+4,x-13,y+1);ctx.stroke();ctx.lineWidth=1;}
 else if(o==='anleger'||o==='schiff'){ctx.fillStyle='#8a6a3a';ctx.fillRect(x-13,y-6,26,14);ctx.fillStyle='#a67c3a';ctx.fillRect(x-13,y-6,26,3);ctx.fillRect(x-13,y,26,3);ctx.fillStyle='#e8e2d0';ctx.beginPath();ctx.moveTo(x-9,y-6);ctx.lineTo(x+9,y-6);ctx.lineTo(x+13,y-14);ctx.lineTo(x-13,y-14);ctx.closePath();ctx.fill();ctx.fillStyle='#2e86c1';ctx.fillRect(x-11,y-13,22,3);ctx.fillStyle='#e5604d';ctx.fillRect(x-2,y-22,4,8);}
 else if(o==='tulpe'){ctx.fillStyle='#2f9a3f';ctx.fillRect(x-1.5,y,3,14);ctx.beginPath();ctx.ellipse(x-6,y+8,6,2.5,-.6,0,6.283);ctx.fill();ctx.fillStyle='#e5504d';ctx.beginPath();ctx.moveTo(x-9,y-4);ctx.quadraticCurveTo(x-10,y+6,x,y+8);ctx.quadraticCurveTo(x+10,y+6,x+9,y-4);ctx.lineTo(x+4,y-1);ctx.lineTo(x,y-9);ctx.lineTo(x-4,y-1);ctx.closePath();ctx.fill();ctx.fillStyle='#ff9a3c';ctx.fillRect(x-2,y-3,4,8);}
  else if(o==='kuchen'){ctx.fillRect(x-12,y-6,26,20);ctx.fillStyle='#e8b64a';ctx.fillRect(x-13,y-2,26,14);ctx.fillStyle='#fff7e6';ctx.fillRect(x-13,y-8,26,7);ctx.fillStyle='#e5504d';circle(x,y-11,3.4);ctx.fillStyle='#7a3f14';ctx.fillRect(x-13,y+8,26,4);}
  else if(o==='loeffel'){ctx.strokeStyle='#9aa0a8';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x-12,y+12);ctx.lineTo(x+4,y-6);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#b8bec6';ctx.beginPath();ctx.ellipse(x+8,y-10,9,7,.7,0,6.283);ctx.fill();ctx.fillStyle='#f1c96a';ctx.beginPath();ctx.ellipse(x+8,y-10,6.5,4.6,.7,0,6.283);ctx.fill();}
  else if(o==='buch'){ctx.fillRect(x-12,y-9,26,22);ctx.fillStyle='#7a3b2a';ctx.fillRect(x-13,y-11,26,22);ctx.fillStyle='#f4ead0';ctx.fillRect(x-11,y-9,10,18);ctx.fillRect(x+1,y-9,10,18);ctx.fillStyle='#c9b98d';for(let k=0;k<4;k++){ctx.fillRect(x-9,y-6+k*4,6,1);ctx.fillRect(x+3,y-6+k*4,6,1);}ctx.fillStyle='#ffd23f';circle(x,y-14-Math.abs(Math.sin(t*3))*3,2.2);}
 else if(o==='tor'){ctx.fillRect(x-12,y-8,26,22);ctx.fillStyle='#8a5a2a';ctx.fillRect(x-12,y-12,4,24);ctx.fillRect(x+8,y-12,4,24);ctx.fillStyle='#b8864a';ctx.fillRect(x-8,y-8,16,3);ctx.fillRect(x-8,y,16,3);ctx.fillRect(x-8,y+8,16,3);ctx.fillStyle='#e8d8a8';ctx.fillRect(x-1,y-8,2,19);}
 else if(o==='heu'){ctx.beginPath();ctx.ellipse(x+2,y+4,15,12,0,0,6.283);ctx.fill();ctx.fillStyle='#d8b45a';circle(x,y,14);ctx.strokeStyle='#a8842e';ctx.lineWidth=1.5;for(let r2=4;r2<=12;r2+=4){ctx.beginPath();ctx.arc(x,y,r2,0,6.283);ctx.stroke();}ctx.lineWidth=1;}
 else if(o==='strudel'){ctx.fillRect(x-14,y-8,28,20);ctx.fillStyle='#d8a050';ctx.beginPath();ctx.ellipse(x,y,15,9,-.2,0,6.283);ctx.fill();ctx.fillStyle='#e8c070';ctx.beginPath();ctx.ellipse(x-1,y-2,12,5,-.2,0,6.283);ctx.fill();ctx.fillStyle='#fff';for(let k=-10;k<=10;k+=5)circle(x+k,y-3+((k/5)%2)*2,1.4);ctx.fillStyle='#8a3a28';circle(x+13,y,2);}
 else if(o==='konfetti'){ctx.fillRect(x-8,y-6,20,20);ctx.fillStyle='#e5504d';ctx.beginPath();ctx.moveTo(x-9,y+12);ctx.lineTo(x+3,y-8);ctx.lineTo(x+9,y+2);ctx.closePath();ctx.fill();ctx.fillStyle='#ffd23f';ctx.fillRect(x-4,y+2,8,2);['#5ff0ff','#ff5fd0','#6bcf63','#ffd23f'].forEach((c0,i)=>{ctx.fillStyle=c0;ctx.fillRect(x+4+i*3,y-14-(i%2)*5,3,3);});}
 else if(o==='waffel'){ctx.fillRect(x-12,y-10,26,24);ctx.fillStyle='#d8a050';ctx.fillRect(x-13,y-12,26,24);ctx.strokeStyle='#a8742e';for(let k=-8;k<=8;k+=8){ctx.beginPath();ctx.moveTo(x+k,y-12);ctx.lineTo(x+k,y+12);ctx.moveTo(x-13,y+k);ctx.lineTo(x+13,y+k);ctx.stroke();}ctx.fillStyle='#b01f2a';circle(x-4,y-3,3);circle(x+5,y+4,3);ctx.fillStyle='#fff';ctx.fillRect(x-1,y-12,5,3);}
 else if(o==='bahn'){ctx.fillRect(x-12,y-6,26,20);ctx.fillStyle='#2c3e50';ctx.fillRect(x-13,y-12,26,22);ctx.fillStyle='#f1c40f';ctx.fillRect(x-11,y-10,22,7);ctx.fillStyle='#ecf0f1';ctx.fillRect(x-9,y,18,4);ctx.fillStyle='#e5504d';ctx.fillRect(x-11,y+5,22,3);ctx.fillStyle='#888';circle(x-7,y+10,2.4);circle(x+7,y+10,2.4);ctx.fillStyle='#ffe08a';circle(x,y-6.5,1.6);}
 else if(o==='flug'){ctx.fillStyle='#f4f6f8';ctx.beginPath();ctx.ellipse(x,y,14,4.6,0,0,6.283);ctx.fill();ctx.beginPath();ctx.moveTo(x-2,y);ctx.lineTo(x-8,y-14);ctx.lineTo(x-3,y-14);ctx.lineTo(x+5,y);ctx.lineTo(x-3,y+14);ctx.lineTo(x-8,y+14);ctx.closePath();ctx.fill();ctx.fillStyle='#d8352f';ctx.beginPath();ctx.moveTo(x-12,y);ctx.lineTo(x-16,y-7);ctx.lineTo(x-12,y-7);ctx.closePath();ctx.fill();ctx.fillStyle='#2e86c1';circle(x+9,y-1,1.4);}
 else if(o==='kuckuck'){ctx.fillRect(x-10,y-6,24,22);ctx.fillStyle='#7a4a24';ctx.fillRect(x-11,y-8,22,22);ctx.fillStyle='#5a3416';ctx.beginPath();ctx.moveTo(x-13,y-8);ctx.lineTo(x,y-20);ctx.lineTo(x+13,y-8);ctx.closePath();ctx.fill();ctx.fillStyle='#f4ead0';circle(x,y+2,6.4);ctx.strokeStyle='#333';ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(x,y+2);ctx.lineTo(x,y-2);ctx.moveTo(x,y+2);ctx.lineTo(x+3,y+3);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#ffd23f';ctx.fillRect(x-1,y+9,2,5);circle(x,y+16,2.4);}
 else if(o==='galo'){ctx.fillStyle='#d8352f';ctx.beginPath();ctx.ellipse(x,y+2,9,11,0,0,6.283);ctx.fill();ctx.fillStyle='#2f62b8';circle(x,y-9,5.4);ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.moveTo(x+4,y-9);ctx.lineTo(x+11,y-7);ctx.lineTo(x+4,y-6);ctx.fill();ctx.fillStyle='#d8352f';ctx.fillRect(x-2,y-17,4,4);ctx.fillStyle='#fff';circle(x-1,y-10,1.2);ctx.fillStyle='#2e9d4f';ctx.fillRect(x-6,y+2,12,3);ctx.fillStyle='#ffd23f';ctx.fillRect(x-6,y+6,12,2);ctx.fillRect(x-4,y+12,2,4);ctx.fillRect(x+2,y+12,2,4);}
 else if(o==='brunnen'){ctx.beginPath();ctx.ellipse(x+2,y+4,15,12,0,0,6.283);ctx.fill();ctx.fillStyle='#9aa0a8';circle(x,y,14);ctx.fillStyle='#7d838c';circle(x,y,11);ctx.fillStyle='#2c80b4';circle(x,y,8.5);ctx.fillStyle='rgba(255,255,255,.4)';ctx.fillRect(x-5,y-3,6,2);ctx.strokeStyle='#5a3a1f';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x-12,y-14);ctx.lineTo(x-12,y+2);ctx.moveTo(x+12,y-14);ctx.lineTo(x+12,y+2);ctx.moveTo(x-13,y-14);ctx.lineTo(x+13,y-14);ctx.stroke();ctx.lineWidth=1;}
 else if(o==='parktor'){ctx.fillRect(x-10,y-6,24,16);ctx.fillStyle='#ffd23f';ctx.fillRect(x-13,y-9,26,16);ctx.fillStyle='#e5504d';ctx.fillRect(x-13,y-9,26,4);ctx.fillStyle='#3a1f4a';ctx.font='bold 8px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('TICKET',x,y+1);ctx.textAlign='start';ctx.textBaseline='alphabetic';}
 else if(o==='leiter'){ctx.fillStyle='#000';ctx.beginPath();ctx.ellipse(x,y,13,10,0,0,6.283);ctx.fill();ctx.strokeStyle='#a67c2e';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x-5,y-9);ctx.lineTo(x-5,y+9);ctx.moveTo(x+5,y-9);ctx.lineTo(x+5,y+9);for(let k=-6;k<=6;k+=4){ctx.moveTo(x-5,y+k);ctx.lineTo(x+5,y+k);}ctx.stroke();ctx.lineWidth=1;}
 else{ctx.fillStyle='#000';ctx.beginPath();ctx.ellipse(x,y,12,9,0,0,6.283);ctx.fill();ctx.fillStyle='#6a5f78';ctx.beginPath();for(let k=-8;k<=8;k+=8){ctx.moveTo(x+k-3,y-9);ctx.lineTo(x+k,y-2);ctx.lineTo(x+k+3,y-9);}ctx.fill();ctx.fillStyle='rgba(120,190,255,.7)';circle(x+3,y+3,1.5);}
}
function drawMarker(m,hl){
 const pulse=1+Math.sin(timeNow*4)*.12,k=m.dist;
 if(m.kind==='portal'){drawPortalObj(m,timeNow);return;}
 if(m.kind==='disco'){
  ctx.fillStyle='rgba(255,95,208,'+(.18+.1*Math.sin(timeNow*5))+')';circle(m.x,m.y,30);
  ctx.fillStyle='#cfd6e0';circle(m.x,m.y,11);
  for(let i=0;i<8;i++){ctx.fillStyle=['#ff5fd0','#5ff0ff','#ffd23f','#fff'][i%4];const a=i/8*6.283+timeNow*2;ctx.fillRect(m.x+Math.cos(a)*7-2,m.y+Math.sin(a)*7-2,4,4);}
  return;
 }
 if(hl&&(hl.has(k+'|d')||hl.has(k+'|p'))){ctx.strokeStyle=hl.has(k+'|p')?'#6bcf63':'#f2b441';ctx.lineWidth=4;ctx.beginPath();ctx.arc(m.x,m.y,24*pulse,0,6.283);ctx.stroke();ctx.lineWidth=1;}
 ctx.fillStyle='rgba(0,0,0,.35)';circle(m.x,m.y+2,17);
 ctx.fillStyle=m.col;circle(m.x,m.y,15);
 ctx.fillStyle='#111';ctx.font='bold 15px Arial';ctx.textAlign='center';ctx.textBaseline='middle';
 ctx.fillText(m.id==='apo'?'+':m.kind==='hq'?'H':m.kind==='willi'?'W':m.kind==='buedchen'?'B':m.kind==='scream'?'!':m.kind==='sk'?'★':'€',m.x,m.y+1);
}
function drawPed(p){
 if(p.snow){drawSnowman(p);return;}
 if(p.st==='lie'){drawLie(p.x,p.y,p.tw||'#e5604d');return;}
 let y=p.y,a=p.a;
 if(p.st==='dance'){y+=Math.sin(timeNow*14)*2;a=timeNow*5;}
 else if((p.st==='party'&&p.pd&&p.arr)||p.st==='polo'){y+=Math.sin(timeNow*9+p.x)*2;a=p.a+Math.sin(timeNow*4+p.y)*.7;}
 else if(p.st==='dazed')a=timeNow*9;
 if(isDeep(p.x,p.y))drawSwim(p.x,y,a,p.col,p.walk);else drawPerson(p.x,y,a,p.col,'ped',p.walk,p.kid?.72:p.teen?.88:p.oma?.96:undefined);
 if(p.oma){ctx.fillStyle='#e2e2ea';circle(p.x,y-1,3.3);ctx.fillStyle='#b5503d';ctx.fillRect(p.x+Math.cos(a+1.57)*8-2,y+Math.sin(a+1.57)*8-2,5,4);}
 if(p.gun){ctx.save();ctx.translate(p.x,y);ctx.rotate(a);ctx.fillStyle=p.gc||'#3fd0ff';ctx.fillRect(5,-2,9,4);ctx.fillStyle='#222';ctx.fillRect(12,-1,3,2);ctx.restore();}
 if(p.bal)drawBal(p.x,y,p.bal);
 ctx.textAlign='center';ctx.textBaseline='middle';
 if(p.teen&&Math.hypot(p.x-P.x,p.y-P.y)<150){ctx.fillStyle='#9ccc65';ctx.font='bold 9px Arial';ctx.fillText('U18',p.x,p.y-22);}
 if(p.like&&p.st!=='dazed'){ctx.fillStyle='#ff4d7a';ctx.font='bold 13px Arial';ctx.fillText('♥',p.x,p.y-13+Math.sin(timeNow*3+p.x)*1.5);}
 if(p.st==='race'){ctx.fillStyle='#ffd23f';ctx.font='bold 14px Arial';ctx.fillText('»',p.x,p.y-13);}
}
function drawWeather(w){
 const t=timeNow;
 if(w==='rain'){
  ctx.strokeStyle='rgba(180,205,255,.55)';ctx.lineWidth=1.2;ctx.beginPath();
  WP.forEach(p=>{const x=((p.x*VW+t*110*p.s)%VW+VW)%VW,y=((p.y*VH+t*560*p.s)%VH+VH)%VH;ctx.moveTo(x,y);ctx.lineTo(x-4,y+11);});
  ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='rgba(30,45,80,.16)';ctx.fillRect(0,0,VW,VH);
 }else if(w==='snow'){
  ctx.fillStyle='rgba(255,255,255,.92)';
  WP.forEach(p=>{const x=(((p.x*VW+Math.sin(t*p.s+p.y*9)*14+t*14*p.s)%VW)+VW)%VW,y=((p.y*VH+t*55*p.s)%VH+VH)%VH;ctx.fillRect(x,y,2.2*p.s,2.2*p.s);});
  if(!ZONE){ctx.fillStyle='rgba(235,245,255,.2)';ctx.fillRect(0,0,VW,VH);}
 }else if(w==='ash'){
  WP.forEach((p,i)=>{if(i%2)return;const x=(((p.x*VW+Math.sin(t*p.s+p.y*7)*18)%VW)+VW)%VW,y=((p.y*VH-t*38*p.s)%VH+VH)%VH;ctx.fillStyle=i%4?'rgba(255,140,50,.85)':'rgba(120,110,110,.7)';ctx.fillRect(x,y,2*p.s,2*p.s);});
  ctx.fillStyle='rgba(120,30,0,'+(.08+.03*Math.sin(t*2))+')';ctx.fillRect(0,0,VW,VH);
 }else if(w==='heat'){
  ctx.fillStyle='rgba(255,170,60,'+(.09+.03*Math.sin(t*2))+')';ctx.fillRect(0,0,VW,VH);
 }else if(w==='sun'&&ZONE){
  ctx.fillStyle='rgba(255,230,160,.06)';ctx.fillRect(0,0,VW,VH);
 }
}
const DKC=document.createElement('canvas');DKC.width=960;DKC.height=540;
function caveDark(cx,cy){
 if(DKC.width!==VW){DKC.width=VW;DKC.height=VH;}
 const d=DKC.getContext('2d');
 d.globalCompositeOperation='source-over';d.clearRect(0,0,VW,VH);d.fillStyle='rgba(3,4,12,.93)';d.fillRect(0,0,VW,VH);
 d.globalCompositeOperation='destination-out';
 const lamp=(x,y,r,a)=>{const g=d.createRadialGradient(x,y,2,x,y,r);g.addColorStop(0,'rgba(0,0,0,'+a+')');g.addColorStop(1,'rgba(0,0,0,0)');d.fillStyle=g;d.fillRect(x-r,y-r,r*2,r*2);};
 lamp(P.x-cx,P.y-cy,175,1);
 MKS.forEach(m=>{if(m.x>cx-120&&m.x<cx+VW+120&&m.y>cy-120&&m.y<cy+VH+120)lamp(m.x-cx,m.y-cy,95,.85);});
 ZONE.glows.forEach(g=>{if(g.x>cx-60&&g.x<cx+VW+60&&g.y>cy-60&&g.y<cy+VH+60)lamp(g.x-cx,g.y-cy,44,.7);});
 ctx.drawImage(DKC,0,0);
 ctx.globalCompositeOperation='lighter';
 ZONE.glows.forEach(g=>{if(g.x>cx-60&&g.x<cx+VW+60&&g.y>cy-60&&g.y<cy+VH+60){const gr=ctx.createRadialGradient(g.x-cx,g.y-cy,1,g.x-cx,g.y-cy,28);gr.addColorStop(0,g.c+'99');gr.addColorStop(1,g.c+'00');ctx.fillStyle=gr;ctx.fillRect(g.x-cx-28,g.y-cy-28,56,56);}});
 ctx.globalCompositeOperation='source-over';
}
function render(){
 timeNow=performance.now()/1000;
 if(shake>0)shake=Math.max(0,shake-fdt*1.2);
 const hi=G&&G.high>0?Math.min(1,G.high/10):0;
 const ox=Math.round(Math.sin(timeNow*1.9)*5*hi+(shake?rf(-1,1)*shake*7:0)),oy=Math.round(Math.cos(timeNow*1.5)*4*hi+(shake?rf(-1,1)*shake*7:0));
 const cx=camX(Math.round(cam.x)+ox),cy=camY(Math.round(cam.y)+oy);
 ctx.imageSmoothingEnabled=false;
 drawWC(cx,cy);mmFade(cx,cy);
 ctx.save();ctx.translate(-cx,-cy);
 const inView=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 const hl=new Set();
 if(G&&!ZONE){
  G.active.forEach(m=>{
   if(pk(m)&&!m.got)hl.add(m.from+'|p');
   else if(pk(m)||canHave(m))hl.add(m.to+'|d');
   else{hl.add(m.to+'|w');hl.add(nearSrc(m.item,m.to,P.x,P.y)+'|p');}
  });
 }
 MKS.forEach(m=>{if(inView(m.x,m.y,60))drawMarker(m,hl);});
 PICKS.forEach(k=>{if(inView(k.x,k.y,10))drawPick(k);});
 drawSeaLife(cx,cy);
 CAS.forEach(c=>{if(inView(c.x,c.y,40))drawCastle(c);});
 RIDES.forEach(R=>{if(inView(R.x,R.y,40))drawRide(R);});
 bridgeOver();
 drawCamp(cx,cy);
 kids.forEach(k=>{if(inView(k.x,k.y,20))drawPerson(k.x,k.y,k.a,k.col,'ped',k.walk,.7);});
 peds.forEach(p=>{if(inView(p.x,p.y,24)){drawPed(p);pActDraw(p);}});
 drawSketch(cx,cy);
 cops.forEach(p=>{if(inView(p.x,p.y,20))drawPerson(p.x,p.y,p.a,'#2a4a8a','cop',p.walk);});
 thugs.forEach(u=>{if(inView(u.x,u.y,20)){if(u.ko>0){ctx.fillStyle='#7a1f1f';ctx.fillRect(u.x-8,u.y-4,16,8);ctx.fillStyle='#e8c39e';circle(u.x+9,u.y,3);}else{drawPerson(u.x,u.y,u.a,'#8a1f2a','thug',u.walk);if(u.loot)drawSack(u);}}});
 chasers.forEach(u=>{if(!inView(u.x,u.y,40))return;if(u.kind==='car')drawCar(u.x,u.y,u.a,'#f4f4f4','chase',timeNow);else drawPerson(u.x,u.y,u.a,'#2a4a8a','cop',timeNow*8);});
 traffic.forEach(c=>{if(inView(c.x,c.y,40)){drawCar(c.x,c.y,c.a,c.col,c.cop?'cop':'civ',timeNow);if(c.spuer)medVanDraw(c);}});
 if(!ZONE)drawCar(V.x,V.y,V.a,'#e9e3d0','van',timeNow);
 if(!P.inCar&&!P.ride&&!P.hide&&G){
  if(P.sit)drawSitter(P.x,P.y);
  else if(isDeep(P.x,P.y))drawSwim(P.x,P.y,P.a,'#d4a017',P.walk);
  else{const dn=P.dance>0;drawPerson(P.x,P.y+(dn?Math.sin(timeNow*14)*2:0),dn?timeNow*5:P.a,'#d4a017','me',P.walk,P.tiny>0?.6:P.big>0?1.6:undefined);}
 }
 drawFishing();
 if(G&&G.ballon&&!P.inCar&&!P.ride)drawBal(P.x,P.y,G.ballon);
 if(G&&P.build){const k=P.build.t/P.build.dur;ctx.strokeStyle='#ffd23f';ctx.lineWidth=3;ctx.beginPath();ctx.arc(P.x,P.y,16,-1.57,-1.57+6.283*k);ctx.stroke();ctx.lineWidth=1;}
 if(G&&G.wet>0&&!P.inCar){ctx.fillStyle='rgba(140,200,255,.85)';for(let i=0;i<4;i++){const q=timeNow*3+i*1.6;circle(P.x+Math.cos(q)*9,P.y+((timeNow*40+i*9)%16)-6,1.4);}}
 PR.forEach(b=>{
  const z=Math.sin(Math.PI*Math.min(1,b.t/.85))*12;
  ctx.fillStyle='rgba(0,0,0,.3)';circle(b.x,b.y+2,3);
  if(b.type==='dose'){ctx.fillStyle='#c9ced6';ctx.fillRect(b.x-2,b.y-z-4,5,8);}
  else if(b.type==='stein'){ctx.fillStyle='#8d8d92';circle(b.x,b.y-z,4);}
  else if(b.type==='ei'){ctx.fillStyle='#fff7e0';ctx.beginPath();ctx.ellipse(b.x,b.y-z,3.2,4.2,.5,0,6.283);ctx.fill();ctx.strokeStyle='#d8c898';ctx.stroke();}
  else if(b.type==='wasser'){ctx.fillStyle='rgba(120,200,255,.9)';circle(b.x,b.y-2,2.6);ctx.fillStyle='rgba(255,255,255,.75)';circle(b.x-b.vx*.012,b.y-2-b.vy*.012,1.7);}
  else{ctx.fillStyle='#fff';circle(b.x,b.y-z,4);ctx.strokeStyle='#cfe3f5';ctx.stroke();}
 });
 FX.forEach(f=>{
  if(!inView(f.x,f.y,30))return;
  const k=f.t/f.life,a=Math.max(0,1-k*k);
  if(f.sm){ctx.fillStyle='rgba(225,225,225,'+(.4*a)+')';circle(f.x,f.y,f.r+k*5);}
  else if(f.dot){ctx.fillStyle=f.dot;circle(f.x,f.y,f.r);}
  else if(f.bat){ctx.fillStyle='#0b0a10';const fl=Math.sin(timeNow*24)*4;ctx.beginPath();ctx.moveTo(f.x-9,f.y-fl);ctx.lineTo(f.x,f.y+2);ctx.lineTo(f.x+9,f.y-fl);ctx.lineTo(f.x,f.y-2);ctx.closePath();ctx.fill();ctx.fillStyle='#ff5050';circle(f.x-1.5,f.y-1,.8);circle(f.x+1.5,f.y-1,.8);}
  else{ctx.globalAlpha=a;ctx.fillStyle=f.col;ctx.font='bold 13px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.65)';ctx.strokeText(f.txt,f.x,f.y);ctx.fillText(f.txt,f.x,f.y);ctx.globalAlpha=1;ctx.lineWidth=1;}
 });
 if(G){
  const gx=P.x,gy=P.y;let tgt=null,td=1e9;
  if(!ZONE)G.active.forEach(m=>{
   const k=mTgt(m);
   const mk=MKQ[k];if(!mk)return;const d=Math.hypot(mk.x-gx,mk.y-gy);if(d<td){td=d;tgt=mk;}
  });
  if(tgt&&td>70){
   const a=Math.atan2(tgt.y-gy,tgt.x-gx);
   ctx.save();ctx.translate(gx+Math.cos(a)*48,gy+Math.sin(a)*48);ctx.rotate(a);
   ctx.fillStyle='#f2b441';ctx.strokeStyle='#000';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(10,0);ctx.lineTo(-6,-8);ctx.lineTo(-3,0);ctx.lineTo(-6,8);ctx.closePath();ctx.fill();ctx.stroke();ctx.restore();
  }
  if(RACE){
   const pl=1+Math.sin(timeNow*6)*.15;
   ctx.strokeStyle='#6bcf63';ctx.lineWidth=5;ctx.beginPath();ctx.arc(RACE.gx,RACE.gy,22*pl,0,6.283);ctx.stroke();ctx.lineWidth=1;
   ctx.fillStyle='#6bcf63';ctx.font='bold 14px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('ZIEL',RACE.gx,RACE.gy);
   const d=Math.hypot(RACE.gx-gx,RACE.gy-gy);
   if(d>70){
    const a=Math.atan2(RACE.gy-gy,RACE.gx-gx);
    ctx.save();ctx.translate(gx+Math.cos(a)*48,gy+Math.sin(a)*48);ctx.rotate(a);
    ctx.fillStyle='#6bcf63';ctx.strokeStyle='#000';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(10,0);ctx.lineTo(-6,-8);ctx.lineTo(-3,0);ctx.lineTo(-6,8);ctx.closePath();ctx.fill();ctx.stroke();ctx.restore();
   }
  }
  thugs.forEach(u=>{if(u.st==='chase'&&u.ko<=0&&inView(u.x,u.y,20)){ctx.fillStyle='#ff4040';ctx.font='bold 16px Arial';ctx.textAlign='center';ctx.fillText('!',u.x,u.y-14);}});
  cops.forEach(c=>{if(c.alert>0&&inView(c.x,c.y,20)){ctx.fillStyle='#ffd23f';ctx.font='bold 18px Arial';ctx.textAlign='center';ctx.fillText('!',c.x,c.y-14);}});
 }
 ctx.restore();
 if(G){
  const wx=wxType();
  if(!ZONE){
   const h=hour();let dark=0;
   if(h>=20)dark=Math.min(1,(h-20)/2);else if(h<5)dark=1;else if(h<7)dark=1-(h-5)/2;
   if(dark>0){ctx.fillStyle='rgba(6,10,40,'+(dark*.5)+')';ctx.fillRect(0,0,VW,VH);
    MKS.forEach(m=>{if(!inView(m.x,m.y,80))return;const g=ctx.createRadialGradient(m.x-cx,m.y-cy,2,m.x-cx,m.y-cy,60);g.addColorStop(0,'rgba(255,220,140,'+(dark*.5)+')');g.addColorStop(1,'rgba(255,220,140,0)');ctx.fillStyle=g;ctx.fillRect(m.x-cx-60,m.y-cy-60,120,120);});
   }
  }
  if(ZONE&&ZONE.dark)caveDark(cx,cy);
  campGlow(cx,cy);fireGlow(cx,cy);fwDraw(cx,cy);
  drawWeather(wx);
  if(flash>0){ctx.fillStyle='rgba(255,255,255,'+flash*.6+')';ctx.fillRect(0,0,VW,VH);}
  if(hi>0){ctx.fillStyle='hsla('+Math.floor((timeNow*45)%360)+',85%,55%,'+(.12*hi)+')';ctx.fillRect(0,0,VW,VH);}
  if(G.drunk>=3){ctx.fillStyle='rgba(255,200,120,'+Math.min(.14,(G.drunk-2)*.04)+')';ctx.fillRect(0,0,VW,VH);}
 }
 if(MG&&G&&!ZONE)drawMG();
 if(fade){
  const k=fade.t/fade.dur,a=Math.min(1,Math.sin(Math.PI*k)*1.8);
  ctx.fillStyle='rgba(0,0,0,'+a+')';ctx.fillRect(0,0,VW,VH);
  if(a>.55){
   ctx.fillStyle='rgba(255,255,255,'+Math.min(1,(a-.55)*3)+')';ctx.font='bold 22px Trebuchet MS,Arial';ctx.textAlign='center';ctx.textBaseline='middle';
   const words=fade.txt.split(' ');let line='',y=VH/2-18,lines=[];
   words.forEach(w=>{const t=line?line+' '+w:w;if(ctx.measureText(t).width>VW*.7&&line){lines.push(line);line=w;}else line=t;});
   lines.push(line);
   lines.forEach((l,i)=>ctx.fillText(l,VW/2,VH/2-(lines.length-1)*14+i*28));
  }
 }
}
function canHave(m){return G.inv[m.item]>=m.q;}
function mS(){return ZONE?6:2.5;}
function renderMini(){
 mctx.clearRect(0,0,mm.width,mm.height);
 miniDraw(mctx,false);
}

const SND={c:null,m:null,on:true,last:{},mt:0,mn:0};
try{SND.on=localStorage.getItem('hh_snd')!=='0';}catch(e){}
function sndWake(){
 try{
  if(!SND.c){const A=window.AudioContext||window.webkitAudioContext;if(!A)return;SND.c=new A();SND.m=SND.c.createGain();SND.m.gain.value=.6;SND.m.connect(SND.c.destination);}
  if(SND.c.state==='suspended')SND.c.resume();
 }catch(e){}
}
function tn(f,d,ty,v,sl,dl){
 if(!SND.on||!SND.c||SND.c.state!=='running')return;
 try{
  const c=SND.c,t0=c.currentTime+(dl||0),o=c.createOscillator(),g=c.createGain();
  o.type=ty||'square';o.frequency.setValueAtTime(f,t0);
  if(sl)o.frequency.exponentialRampToValueAtTime(Math.max(20,sl),t0+d);
  g.gain.setValueAtTime(0.0001,t0);g.gain.linearRampToValueAtTime(v||.12,t0+.012);g.gain.exponentialRampToValueAtTime(.0008,t0+d);
  o.connect(g);g.connect(SND.m);o.start(t0);o.stop(t0+d+.06);
 }catch(e){}
}
function nz(d,v,f,ty,dl,f2){
 if(!SND.on||!SND.c||SND.c.state!=='running')return;
 try{
  const c=SND.c,t0=c.currentTime+(dl||0),n=Math.max(8,Math.floor(c.sampleRate*d)),b=c.createBuffer(1,n,c.sampleRate),a=b.getChannelData(0);
  for(let i=0;i<n;i++)a[i]=(Math.random()*2-1)*(1-i/n);
  const s=c.createBufferSource();s.buffer=b;
  const fl=c.createBiquadFilter();fl.type=ty||'bandpass';fl.frequency.setValueAtTime(f||1500,t0);
  if(f2)fl.frequency.exponentialRampToValueAtTime(f2,t0+d);
  const g=c.createGain();g.gain.value=v||.2;
  s.connect(fl);fl.connect(g);g.connect(SND.m);s.start(t0);
 }catch(e){}
}
const SFX={
 tick(){tn(900,.04,'square',.04);},
 ok(){tn(660,.07,'square',.07);tn(990,.09,'square',.07,0,.06);},
 back(){tn(520,.07,'square',.06,330);},
 coin(){tn(988,.07,'square',.08);tn(1319,.16,'square',.08,0,.07);},
 throw(){nz(.16,.22,900,'bandpass',0,2600);},
 squirt(){nz(.14,.16,3200,'highpass');tn(1500,.08,'sine',.03,2400);},
 splash(){nz(.32,.26,1200,'lowpass',0,300);tn(300,.12,'sine',.05,120);},
 hit(){tn(220,.1,'square',.12,90);nz(.07,.18,700,'bandpass');},
 bonk(){tn(150,.16,'triangle',.2,60);nz(.08,.14,400,'lowpass');},
 glug(){for(let i=0;i<4;i++)tn(260+i*40,.07,'sine',.1,150,i*.09);},
 puff(){nz(.5,.12,900,'lowpass',0,200);tn(180,.4,'sine',.03,120);},
 sit(){tn(200,.09,'triangle',.14,140);},
 warp(){tn(180,1.1,'sawtooth',.06,1400);tn(1400,1.0,'sine',.05,200,.15);nz(1.1,.1,400,'bandpass',0,3000);},
 arrive(){tn(520,.12,'square',.07);tn(660,.12,'square',.07,0,.1);tn(880,.22,'square',.07,0,.2);},
 clap(){nz(.05,.35,2200,'bandpass');nz(.05,.3,2000,'bandpass',.1);},
 aww(){tn(520,.35,'sine',.1,780);tn(660,.4,'sine',.08,990,.14);},
 pfft(){nz(.3,.22,600,'bandpass',0,200);},
 scream(){tn(500,1.2,'sawtooth',.1,1100);tn(400,1.2,'square',.05,900);nz(1.1,.12,1800,'bandpass');},
 rumble(){nz(1.4,.35,160,'lowpass');tn(55,1.2,'sine',.2,35);},
 thunder(){nz(1.6,.4,220,'lowpass',.1);tn(70,1.3,'sine',.15,30,.1);},
 disco(){for(let i=0;i<4;i++){tn(330,.08,'square',.07,0,i*.12);tn(660,.08,'square',.05,0,i*.12+.06);}},
 pat(){nz(.07,.3,500,'lowpass');nz(.07,.3,450,'lowpass',.14);nz(.07,.3,400,'lowpass',.28);},
 crumble(){nz(.5,.3,600,'lowpass',0,150);},
 crunch(){nz(.22,.3,1800,'bandpass',0,400);},
 ride(){tn(300,.12,'square',.07,600);tn(450,.14,'square',.07,900,.1);},
 oma(){tn(700,.5,'sawtooth',.1,350);tn(740,.5,'square',.05,380,.04);},
 honk(){tn(330,.22,'square',.12);tn(262,.3,'square',.12,0,.12);},
 wave(){nz(.35,.07,700,'lowpass',0,250);},
 swish(){nz(.25,.1,2200,'highpass');},
 roll(){nz(.18,.05,500,'bandpass');},
 bite(){tn(880,.08,'square',.09);tn(1100,.1,'square',.09,0,.08);},
 catch(){tn(523,.1,'square',.08);tn(784,.1,'square',.08,0,.09);tn(1047,.2,'square',.08,0,.18);},
 whale(){tn(110,1.6,'sine',.18,70);tn(165,1.4,'sine',.08,95,.2);},
 power(){tn(300,.5,'sawtooth',.07,1200);tn(600,.5,'square',.05,1800,.1);},
 win(){[523,659,784,1047].forEach((f,i)=>tn(f,.2,'square',.09,0,i*.13));},
 magic(){[880,1175,1568,1976].forEach((f,i)=>tn(f,.2,'sine',.07,0,i*.08));},
 musik(){[392,494,587,494,659,587].forEach((f,i)=>tn(f,.14,'square',.07,0,i*.12));},
 ding(){tn(1568,.1,'sine',.09);tn(1568,.1,'sine',.09,0,.16);},
 muh(){tn(150,.5,'sawtooth',.1,100);tn(200,.3,'sawtooth',.05,140,.1);},
 hoho(){tn(120,.16,'sawtooth',.1,90);tn(120,.16,'sawtooth',.1,90,.2);tn(100,.26,'sawtooth',.1,70,.4);}
};
function sfx(n){
 if(!SND.on||!SND.c)return;
 const now=performance.now();
 if(SND.last[n]&&now-SND.last[n]<70)return;
 SND.last[n]=now;
 try{if(SFX[n])SFX[n]();}catch(e){}
}
function toggleSnd(){
 SND.on=!SND.on;
 try{localStorage.setItem('hh_snd',SND.on?'1':'0');}catch(e){}
 if(SND.on){sndWake();setTimeout(()=>sfx('ok'),60);}
}

const RP={
 sled:{mx:330,ac:120,br:150,dr:28,tn:2.3,r:9,g:80},
 chair:{mx:215,ac:340,br:540,dr:170,tn:3.6,r:8,g:0},
 boat:{mx:300,ac:210,br:240,dr:60,tn:2.1,r:11,g:0},
 bike:{mx:250,ac:260,br:420,dr:110,tn:3,r:8,g:0},
 scoot:{mx:170,ac:300,br:420,dr:140,tn:3.4,r:11,g:0}
};
const RN={sled:'Rodelschlitten',chair:'Rollstuhl',boat:'Boot',bike:'Fahrrad',scoot:'Autoscooter'};
const RMSG={
 sled:['Rodeln! Der Hang gehört dir. Hoch beschleunigt, Links und Rechts lenkt.','Schlitten frei! Je steiler, desto lustiger.'],
 chair:['Der Rollstuhl hat Rückenwind. Und ein erstaunlich gutes Fahrwerk.','Vorsicht, Kurven! Der Rollstuhl hat ordentlich Dampf.'],
 boat:['Leinen los! Hoch fährt, Links und Rechts lenkt.','Ahoi! Das Boot schaukelt, die Laune auch.'],
 bike:['Aufs Rad! Klingeling.','Fahrrad geschnappt. Holland-Gefühl inklusive.'],
 scoot:['Autoscooter! Hoch gibt Gas, Links und Rechts lenkt. Rempeln ausdrücklich erlaubt.','Funken sprühen von der Decke. Ab geht die wilde Fahrt!']
};
let RIDES=[],CAS=[];
function mkRide(k,x,y,a){return{k:k,x:x,y:y,a:a||0,sp:0,snd:0,hx:false,hy:false,oma:null,stolen:false};}
function isWaterT(t){return t===SH||t===DP;}
function isDeep(x,y){return !!(ZONE&&ZONE.swim&&tget(Math.floor(x/TS),Math.floor(y/TS))===DP);}
function rideBlocked(R,x,y){
 const r=RP[R.k].r;
 if(R.k==='boat'){
  const x0=Math.floor((x-r)/TS),x1=Math.floor((x+r)/TS),y0=Math.floor((y-r)/TS),y1=Math.floor((y+r)/TS);
  return !boatFree(x,y);
 }
 if(R.k==='scoot'){
  const x0=Math.floor((x-r)/TS),x1=Math.floor((x+r)/TS),y0=Math.floor((y-r)/TS),y1=Math.floor((y+r)/TS);
  for(let j=y0;j<=y1;j++)for(let i=x0;i<=x1;i++)if(tget(i,j)!==RD)return true;
  return false;
 }
 return hit(x,y,r)||rideWet(R,x,y);
}
function rideMove(R,dx,dy){
 if(R.k==='boat'){boatMove(R,dx,dy);return;}
 R.hx=false;R.hy=false;
 let nx=R.x+dx;if(rideBlocked(R,nx,R.y)){nx=R.x;R.hx=true;}R.x=nx;
 let ny=R.y+dy;if(rideBlocked(R,R.x,ny)){ny=R.y;R.hy=true;}R.y=ny;
 R.x=clamp(R.x,TS,MW*TS-TS);R.y=clamp(R.y,TS,MH*TS-TS);
}
function rideDrive(dt,ax,ay){
 const R=P.ride,p=RP[R.k];
 let mx=p.mx,dr=p.dr;
 const t=tget(Math.floor(R.x/TS),Math.floor(R.y/TS));
 if(R.k==='sled'||R.k==='ski'){if(t===IC){mx*=1.35;dr*=.3;}else if(t!==SN){mx*=.5;dr*=4;}}
 if(R.k==='boat'&&ZONE&&ZONE.name==='rhein')mx=390;
 if(ay<0)R.sp=Math.min(mx,R.sp+p.ac*dt);
 else if(ay>0){if(R.sp>10)R.sp=Math.max(0,R.sp-p.br*dt);else R.sp=Math.max(-70,R.sp-p.ac*.5*dt);}
 else R.sp-=Math.sign(R.sp)*Math.min(Math.abs(R.sp),dr*dt);
 if(p.g)R.sp+=Math.sin(R.a)*p.g*dt;
 R.sp=clamp(R.sp,-80,mx*1.15);
 const steer=ax*p.tn*clamp(Math.abs(R.sp)/80,R.k==='boat'?.7:.25,1)*(R.sp<0?-1:1)*(R.k==='ski'?-1:1);
 R.a+=steer*dt;if(R.k==='ski')R.a=clamp(R.a,.3,Math.PI-.3);
 let dx=Math.cos(R.a)*R.sp*dt,dy=Math.sin(R.a)*R.sp*dt;
 rideMove(R,dx,dy);
 if(R.k==='boat'&&ZONE&&ZONE.name==='rhein'){const hx=R.hx,hy=R.hy;rideMove(R,26*dt,0);R.hx=hx;R.hy=hy;}
 if(R.hx||R.hy){
  if(Math.abs(R.sp)>120){
   addFx(R.x,R.y-16,pick(['Bonk!','Rums!','Hoppla!']),'#ffd23f');sfx('bonk');shake=.35;
   if(R.k==='sled'||R.k==='bike'||R.k==='chair'||R.k==='scoot')mood(1);
  }
  if(R.k==='boat')R.sp*=(R.hx&&R.hy)?-.2:Math.max(0,1-dt*1.8);else R.sp*=-.3;
 }
 P.x=R.x;P.y=R.y;
 R.snd-=dt;
 if(R.snd<=0&&Math.abs(R.sp)>90){R.snd=R.k==='boat'?.5:.38;sfx(R.k==='boat'?'wave':R.k==='sled'?'swish':'roll');}
 if(Math.abs(R.sp)>70&&chance(dt*18)){
  const bx=R.x-Math.cos(R.a)*14+rf(-4,4),by=R.y-Math.sin(R.a)*14+rf(-4,4);
  if(R.k==='boat')FX.push({x:bx,y:by,vx:rf(-6,6),vy:rf(-6,6),t:0,life:.6,dot:'rgba(255,255,255,.75)',r:rf(2,4)});
  else if(R.k==='sled'&&(t===SN||t===IC))FX.push({x:bx,y:by,vx:rf(-12,12),vy:rf(-14,-2),t:0,life:.5,dot:'#fff',r:rf(1.5,3)});
 }
 if(Math.abs(R.sp)>110&&!(R.k==='boat'&&t===DK)){
  peds.forEach(q=>{
   if(Math.hypot(q.x-R.x,q.y-R.y)>17)return;
   if(q.snow){toppleSnow(q,true);return;}
   if(q.st!=='walk')return;
   q.st='dazed';q.stT=1.6;addFx(q.x,q.y-16,pick(['Huch!','Hoppla!','Na hör mal!']),'#ffd23f');sfx('hit');mood(3,'+3');
  });
 }
}
function nearRide(){
 if(P.ride||P.inCar||P.sit||P.build)return null;
 let b=null,bd=34;
 RIDES.forEach(R=>{if(R.rc)return;const d=Math.hypot(R.x-P.x,R.y-P.y);if(d<bd){bd=d;b=R;}});
 return b;
}
function takeRide(R){
 if(R.oma&&!R.stolen)stealChair(R);
 if(XRD[R.k]&&!R.stolen)xrSteal(R);
 P.ride=R;R.sp=0;P.vx=P.vy=0;P.x=R.x;P.y=R.y;
 keys.left=keys.right=keys.up=keys.down=0;
 sfx('ride');
 if(!R.oma||R.stolen)toast(pick(RMSG[R.k]));
}
function leaveRide(force){
 const R=P.ride;if(!R)return false;
 if(!force&&Math.abs(R.sp)>110){toast('Erst langsamer werden, dann absteigen.');return false;}
 let best=null;
 for(const r of[26,34,44]){
  for(let k=0;k<12;k++){
   const a=k/12*6.283+R.a+1.57,x=R.x+Math.cos(a)*r,y=R.y+Math.sin(a)*r;
   if(hit(x,y,7))continue;
   const w=isWaterT(tget(Math.floor(x/TS),Math.floor(y/TS)));
   if(!best||(best.w&&!w)){best={x:x,y:y,w:w};}
   if(!w)break;
  }
  if(best&&!best.w)break;
 }
 if(!best){if(!force)toast('Hier ist kein Platz zum Absteigen.');return false;}
 P.ride=null;P.x=best.x;P.y=best.y;P.vx=P.vy=0;R.sp=0;
 if(best.w){addFx(P.x,P.y-10,'Platsch!','#9fd8ff');sfx('splash');}
 return true;
}
const OMAN=['Oma Erna','Oma Gertrud','Oma Hilde','Oma Frieda'];
function stealChair(R){
 const o=R.oma;R.stolen=true;R.oma=null;
 o.st='chase';o.stT=1e9;o.chair=R;o.gone=0;o.swat=0;o.x=R.x;o.y=R.y;
 peds.push(o);
 heat(4);mood(10,'Frechheit siegt');sfx('oma');
 addFx(o.x,o.y-28,'MEIN ROLLSTUHL!','#ff8a65',2.2);
 toast(pick([o.nm+' springt auf: "Mein Rollstuhl! Ich fahr den nur aus Bequemlichkeit!" Sie sprintet erstaunlich gut.','Plötzlich ist '+o.nm+' topfit und schimpft hinterher. Niemand kommt zu Schaden, nur der Stolz.','"Junger Mann!" ruft '+o.nm+' und schwingt die Handtasche. Fahr los!']));
}
function omaStep(p,dt){
 const R=p.chair;
 const riding=P.ride===R;
 p.gone+=riding?dt:0;
 let tx,ty,sp=88;
 if(riding){tx=P.x;ty=P.y;}else{tx=R.x;ty=R.y;sp=96;}
 const d=Math.hypot(tx-p.x,ty-p.y);
 p.a=Math.atan2(ty-p.y,tx-p.x);
 if(d>16){moveE(p,Math.cos(p.a)*sp*dt,Math.sin(p.a)*sp*dt,7);p.walk+=dt*10;}
 if(!riding&&!P.ride){
  if(Math.hypot(R.x-p.x,R.y-p.y)<22){
   R.oma=p;R.stolen=false;R.x=R.x;p.st='walk';p.chair=null;
   const i=peds.indexOf(p);if(i>=0)peds.splice(i,1);
   addFx(R.x,R.y-24,'Danke, junger Mann!','#6bcf63',2);mood(2);sfx('aww');
   toast(p.nm+' hat ihren Rollstuhl zurück und nimmt Platz. "Und jetzt schäm dich!" Sie lächelt dabei.');
   return;
  }
  const dp=Math.hypot(P.x-p.x,P.y-p.y);
  p.swat-=dt;
  if(dp<20&&p.swat<=0){
   p.swat=3;P.stun=.7;addFx(P.x,P.y-18,'Pflopp!','#ffd23f');sfx('pfft');mood(2);
   toast('Pflopp! Die Handtasche ist erstaunlich weich. Nur der Stolz tut kurz weh.');
  }
 }
 if(p.gone>50&&riding){
  p.st='walk';p.chair=null;p.oma=false;p.stT=0;
  addFx(p.x,p.y-26,'Dann behalt ihn halt!','#6bcf63',2.4);mood(6,'+6');sfx('aww');
  toast(p.nm+' gibt auf: "Behalt ihn halt, ich geh eh lieber zu Fuß!" Der Rollstuhl gehört jetzt dir.');
 }
}
function pedExt(p,dt){
 if(p.oma&&p.st==='chase'){omaStep(p,dt);return true;}
 if(p.flee>0){
  p.flee-=dt;
  const a=Math.atan2(p.y-P.y,p.x-P.x);p.a=a;
  moveE(p,Math.cos(a)*90*dt,Math.sin(a)*90*dt,7);p.walk+=dt*10;
  if(p.flee<=0)p.st='walk';
  return true;
 }
 if(p.gun&&p.st==='walk'&&ZONE&&ZONE.name==='strand'&&!P.sit){
  const d=Math.hypot(p.x-P.x,p.y-P.y);
  const home=p.kid&&p.hx0!==undefined?Math.hypot(p.x-p.hx0,p.y-p.hy0):0;
  if(d<280&&home<330){
   p.a=Math.atan2(P.y-p.y,P.x-p.x);
   if(d>120){moveE(p,Math.cos(p.a)*54*dt,Math.sin(p.a)*54*dt,7);p.walk+=dt*8;}
   p.fireT=(p.fireT===undefined?rf(.6,1.6):p.fireT)-dt;
   if(p.fireT<=0&&d<230){
    p.fireT=rf(1.2,2.4);
    const a=p.a+rf(-.12,.12);
    PR.push({x:p.x,y:p.y,vx:Math.cos(a)*300,vy:Math.sin(a)*300,t:0,type:'wasser',from:'ped',life:.65});
    sfx('squirt');
   }
   return true;
  }
 }
 return false;
}
function shootWater(){
 if(G.tank<1){toast('Der Tank ist leer. Ab ins Wasser zum Auffüllen!');return true;}
 const best=aimBest(240,true);
 let a=P.a;
 if(best)a=Math.atan2(best.y-P.y,best.x-P.x);
 G.tank--;P.a=a;
 PR.push({x:P.x+Math.cos(a)*8,y:P.y+Math.sin(a)*8,vx:Math.cos(a)*430,vy:Math.sin(a)*430,t:0,type:'wasser',life:.5});
 sfx('squirt');
 return true;
}
function hitWater(p){
 if(p.snow){p.wob=.5;return;}
 sfx('splash');
 addFx(p.x,p.y-16,pick(['Kreisch!','Nass!','Kalt!','Hihi!']),'#9fd8ff');
 for(let i=0;i<4;i++)FX.push({x:p.x,y:p.y-6,vx:rf(-30,30),vy:rf(-40,-10),g:120,t:0,life:.6,dot:'#9fd8ff',r:rf(1.5,3)});
 if(p.kid||p.gun||p.like){p.flee=rf(1.6,2.6);p.st='walk';mood(3,'+3');}
 else{p.st='angry';p.stT=1.6;mood(1);}
 if(p.kid&&chance(.5))p.gun=true;
}
function aimBest(rng,allowKid){
 let best=null,bd=rng||240;
 const t=curAmmo();
 peds.concat(cops).forEach(u=>{
  if(u.st==='lie'||u.chair)return;
  if((u.kid||u.teen)&&t!=='wasser'&&!allowKid)return;
  const d=Math.hypot(u.x-P.x,u.y-P.y);if(d>bd||d<10)return;
  let da=Math.atan2(u.y-P.y,u.x-P.x)-P.a;while(da>Math.PI)da-=6.283;while(da<-Math.PI)da+=6.283;
  if(Math.abs(da)<.75){bd=d;best=u;}
 });
 return best;
}
function nearSnowman(){
 if(P.ride||P.inCar||P.sit)return null;
 let b=null,bd=34;
 peds.forEach(p=>{if(!p.snow)return;const d=Math.hypot(p.x-P.x,p.y-P.y);if(d<bd){bd=d;b=p;}});
 return b;
}
function toppleSnow(p,soft){
 const i=peds.indexOf(p);if(i>=0)peds.splice(i,1);
 for(let k=0;k<8;k++)FX.push({x:p.x+rf(-6,6),y:p.y+rf(-14,4),vx:rf(-40,40),vy:rf(-60,-10),g:200,t:0,life:.8,dot:'#fff',r:rf(2,4)});
 addFx(p.x,p.y-20,pick(['Plumps!','Pfff!','Schneemann kaputt!']),'#cfe9ff');sfx('crunch');
 if(!soft){G.ammo.schnee=Math.min(9,G.ammo.schnee+2);mood(G.mood<45?9:5,'+Spaß');toast('Der Schneemann ist hin. Dafür hast du Schneebälle für die nächste Schlacht.');}
}
function kickSnowman(p){
 P.a=Math.atan2(p.y-P.y,p.x-P.x);
 toppleSnow(p,false);
}
function nearCastle(){
 if(P.ride||P.inCar||P.sit)return null;
 let b=null,bd=34;
 CAS.forEach(c=>{const d=Math.hypot(c.x-P.x,c.y-P.y);if(d<bd){bd=d;b=c;}});
 return b;
}
function kickCastle(c){
 const i=CAS.indexOf(c);if(i>=0)CAS.splice(i,1);
 P.a=Math.atan2(c.y-P.y,c.x-P.x);
 for(let k=0;k<12;k++)FX.push({x:c.x+rf(-8,8),y:c.y+rf(-10,4),vx:rf(-60,60),vy:rf(-80,-20),g:240,t:0,life:.9,dot:'#e2c27a',r:rf(2,4)});
 addFx(c.x,c.y-22,pick(['BUMM!','Zack!','Sandsturm!','Weg damit!']),'#ffd23f');sfx('crumble');
 mood(G.mood<45?10:5,'+Spaß');
 toast(pick(['Die Sandburg ist Geschichte. Es fühlt sich überraschend gut an.','Zack, plattgetreten. Der Sand fliegt bis in die Schuhe.','Wutsand! Ein gewaltiger Tritt, ein sehr kleiner Schaden.']));
}
function ctxBuild(){
 if(P.ride||P.sit||P.inCar||P.build||inNoGo(P.x,P.y))return '';
 const t=tget(Math.floor(P.x/TS),Math.floor(P.y/TS));
 if(ZONE&&ZONE.name==='strand'&&t===SA&&CAS.length<14&&!CAS.some(c=>Math.hypot(c.x-P.x,c.y-P.y)<36))return 'castle';
 const snowy=(ZONE&&ZONE.name==='berge'&&t===SN)||(!ZONE&&wxType()==='snow'&&(t===GR||t===SW||t===SD||t===FD));
 if(snowy&&G.ammo.schnee>=3&&!peds.some(p=>p.snow&&Math.hypot(p.x-P.x,p.y-P.y)<42))return 'snow';
 return '';
}
function startBuild(k){
 P.build={k:k,t:0,dur:k==='castle'?1.4:1.7,fx:0};
 P.vx=P.vy=0;keys.left=keys.right=keys.up=keys.down=0;
 toast(k==='castle'?'Du schaufelst Sand zusammen ...':'Du rollst drei Schneebälle zusammen ...');
}
function buildUpdate(dt){
 const b=P.build;if(!b)return;
 b.t+=dt;b.fx-=dt;
 if(b.fx<=0){
  b.fx=.18;sfx(b.k==='castle'?'roll':'roll');
  FX.push({x:P.x+rf(-12,12),y:P.y+rf(-6,8),vx:rf(-20,20),vy:rf(-40,-10),g:160,t:0,life:.5,dot:b.k==='castle'?'#e2c27a':'#fff',r:rf(1.5,3)});
 }
 if(b.t<b.dur)return;
 P.build=null;
 if(b.k==='knab'||b.k==='kiss'||b.k==='pack'){skBuildDone(b);return;}
 if(b.k==='dig'){digDone();return;}
 const x=P.x+Math.cos(P.a)*22,y=P.y+Math.sin(P.a)*22,q=hit(x,y,8)?{x:P.x,y:P.y}:{x:x,y:y};
 if(b.k==='castle'){
  CAS.push({x:q.x,y:q.y,c:pick(['#e5604d','#2e86c1','#f1c40f','#8e44ad'])});
  mood(7,'+7 Sandburg');sfx('pat');
  toast(pick(['Fertig: Eine Sandburg mit Burggraben und Fahne. Sehr stabil, wirklich.','Dein Meisterwerk steht. Die Möwen sind beeindruckt.','Sandburg gebaut. Jetzt könntest du sie auch wieder kaputt treten ...']));
 }else{
  G.ammo.schnee-=3;
  const sm=mkPed(q.x,q.y);sm.snow=true;sm.hp=0;sm.built=true;sm.wob=0;if(!ZONE)sm.melt=50;
  peds.push(sm);
  mood(9,'+9 Schneemann');sfx('pat');
  toast(pick(['Ein Schneemann entsteht! Mit Karotte und allem.','Schneemann fertig. Er sieht dich vorwurfsvoll an, weil er keine Ohren hat.','Der Schneemann wäre stolz auf dich.']));
 }
}
function extUpdate(dt){
 if(!G)return;
 if(G.wet>0)G.wet-=dt;
 const t=tget(Math.floor(P.x/TS),Math.floor(P.y/TS));
 const inW=!P.ride&&!P.inCar&&(t===SH||isDeep(P.x,P.y));
 if(inW&&!P.wasW){addFx(P.x,P.y-8,'Platsch!','#9fd8ff');sfx('splash');}
 P.wasW=inW;
 if(inW){G.wet=Math.max(G.wet||0,3);if(G.pistol&&G.tank<30)G.tank=Math.min(30,G.tank+dt*14);if(isDeep(P.x,P.y)&&chance(dt*3))mood(.8);}
 else if(P.ride&&P.ride.k==='boat'&&G.pistol&&G.tank<30)G.tank=Math.min(30,G.tank+dt*8);
 buildUpdate(dt);
 for(let i=peds.length-1;i>=0;i--){const p=peds[i];if(p.snow&&p.melt!==undefined&&p.melt<=0){peds.splice(i,1);addFx(p.x,p.y-12,'Plopp ...','#cfe9ff');}}
 if(ZONE&&ZONE.name==='strand'){
  ZONE.kt=(ZONE.kt===undefined?18:ZONE.kt)-dt;
  if(ZONE.kt<=0){
   ZONE.kt=rf(22,34);
   const ks=peds.filter(p=>p.kid&&p.st==='walk'&&tget(Math.floor(p.x/TS),Math.floor(p.y/TS))===SA);
   if(ks.length&&CAS.length<9){const k=pick(ks);CAS.push({x:k.x+rf(-14,14),y:k.y+rf(-8,14),c:pick(['#e5604d','#2e86c1','#f1c40f','#8e44ad'])});addFx(k.x,k.y-18,'Fertig!','#ffd23f');}
  }
 }
 if(ZONE&&ZONE.name==='rhein'&&P.ride&&P.ride.k==='boat'&&P.ride.x>(MW-3)*TS&&!fade){
  P.ride.sp=0;
  startFade('Ein Schild am Ufer: "Welkom in Nederland!" Du fährst direkt in die Amsterdamer Grachten. Das ging fix.',()=>enterZone('amsterdam'));
 }
 ext6Update(dt);ext7Update(dt);ext8Update(dt);ext9Update(dt);ext10Update(dt);ext11Update(dt);ext12Update(dt);ext14Update(dt);ext16Update(dt);ext17Update(dt);ext18Update(dt);ext19Update(dt);campUpdate(dt);fireUpdate(dt);fwUpdate(dt);fairyUpdate(dt);malleUpdate(dt);aniUpdate(dt);galUpdate(dt);plantUpdate(dt);needTick(dt);bepUpdate(dt);qUpdate(dt);mowTick();kUpdate(dt);medTick(dt);
}
function drawCastle(c){
 ctx.fillStyle='rgba(0,0,0,.2)';ctx.beginPath();ctx.ellipse(c.x+3,c.y+7,17,7,0,0,6.283);ctx.fill();
 ctx.fillStyle='#d4b46a';ctx.beginPath();ctx.ellipse(c.x,c.y+3,16,8,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e2c27a';ctx.fillRect(c.x-12,c.y-4,24,8);
 [-11,-2,7].forEach((o,i)=>{const h=i===1?16:11;ctx.fillStyle='#e8cd86';ctx.fillRect(c.x+o,c.y-h,6,h+2);ctx.fillStyle='#d4b46a';ctx.fillRect(c.x+o,c.y-h,2,2);ctx.fillRect(c.x+o+4,c.y-h,2,2);});
 ctx.strokeStyle='#6a4a2a';ctx.lineWidth=1.5;ctx.beginPath();ctx.moveTo(c.x+1,c.y-16);ctx.lineTo(c.x+1,c.y-26);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle=c.c;ctx.beginPath();ctx.moveTo(c.x+1,c.y-26);ctx.lineTo(c.x+9,c.y-23);ctx.lineTo(c.x+1,c.y-20);ctx.fill();
 ctx.fillStyle='#8a6a3a';ctx.fillRect(c.x-2,c.y-1,4,5);
}
function drawSwim(x,y,a,col,walk){
 ctx.save();ctx.translate(x,y);
 ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=1.5;
 const r=Math.sin(timeNow*3+x)*1.5;
 ctx.beginPath();ctx.ellipse(0,3,11+r,6+r*.5,0,0,6.283);ctx.stroke();
 ctx.beginPath();ctx.ellipse(0,3,16-r,9-r*.5,0,0,6.283);ctx.stroke();ctx.lineWidth=1;
 ctx.rotate(a);
 const sw=Math.sin((walk||0)*1.6+timeNow*5)*4;
 ctx.fillStyle='#e8c39e';circle(-2,-7+sw,2.2);circle(-2,7-sw,2.2);
 ctx.fillStyle=col;ctx.beginPath();ctx.ellipse(0,0,3.6,6.2,0,0,6.283);ctx.fill();
 ctx.fillStyle='#4a3a2a';circle(1,0,3.6);
 ctx.restore();
}
function drawRide(R){
 const me=P.ride===R;
 ctx.save();ctx.translate(R.x,R.y);
 ctx.fillStyle='rgba(0,0,0,.26)';ctx.beginPath();ctx.ellipse(2,5,14,8,0,0,6.283);ctx.fill();
 ctx.rotate(R.a);
 if(R.k==='sled'){
  ctx.fillStyle='#777';ctx.fillRect(-15,-9,30,2.5);ctx.fillRect(-15,6.5,30,2.5);ctx.beginPath();ctx.arc(15,-8,2,0,6.283);ctx.arc(15,8,2,0,6.283);ctx.fill();
  ctx.fillStyle='#b5651d';ctx.fillRect(-12,-7,24,14);ctx.fillStyle='#e5604d';ctx.fillRect(-12,-7,24,3);ctx.fillStyle='rgba(0,0,0,.18)';ctx.fillRect(-12,3,24,4);
 }else if(R.k==='chair'){
  ctx.fillStyle='#222';ctx.fillRect(-7,-12,11,3);ctx.fillRect(-7,9,11,3);
  ctx.fillStyle='#8a929c';ctx.fillRect(-7,-9,2,18);
  ctx.fillStyle='#4a5a8a';ctx.fillRect(-6,-7,12,14);ctx.fillStyle='#3a4872';ctx.fillRect(-8,-7,3,14);
  ctx.fillStyle='#8a929c';ctx.fillRect(7,-4,5,8);ctx.fillStyle='#222';circle(10,-6,1.5);circle(10,6,1.5);
 }else if(R.k==='boat'){
  ctx.fillStyle='#caa46a';ctx.beginPath();ctx.moveTo(20,0);ctx.quadraticCurveTo(10,-12,-15,-10);ctx.lineTo(-15,10);ctx.quadraticCurveTo(10,12,20,0);ctx.fill();
  ctx.fillStyle='#a8722f';ctx.beginPath();ctx.moveTo(15,0);ctx.quadraticCurveTo(8,-8,-12,-7);ctx.lineTo(-12,7);ctx.quadraticCurveTo(8,8,15,0);ctx.fill();
  ctx.fillStyle='#e5604d';ctx.fillRect(-15,-3,6,6);
  ctx.strokeStyle='rgba(255,255,255,.7)';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(20,0);ctx.quadraticCurveTo(10,-12,-15,-10);ctx.moveTo(20,0);ctx.quadraticCurveTo(10,12,-15,10);ctx.stroke();ctx.lineWidth=1;
 }else if(R.k==='scoot'){
  ctx.fillStyle='#1a1a1a';ctx.beginPath();ctx.ellipse(0,0,15.5,12.5,0,0,6.283);ctx.fill();
  ctx.fillStyle=R.col||'#e5504d';ctx.beginPath();ctx.ellipse(0,0,13,10,0,0,6.283);ctx.fill();
  ctx.fillStyle='rgba(255,255,255,.35)';ctx.beginPath();ctx.ellipse(6,-3,5,3,0,0,6.283);ctx.fill();
  ctx.fillStyle='#2a2a2a';ctx.fillRect(-10,-6,9,12);ctx.fillStyle='#ffd23f';ctx.fillRect(9,-5,3,3);ctx.fillRect(9,2,3,3);
 }else if(R.k==='ski'){skiDraw(R);
 }else if(XRD[R.k]){xrDraw(R);
 }else{
  ctx.strokeStyle='#222';ctx.lineWidth=2.2;ctx.beginPath();ctx.arc(-9,0,5.5,0,6.283);ctx.stroke();ctx.beginPath();ctx.arc(9,0,5.5,0,6.283);ctx.stroke();
  ctx.strokeStyle='#e5604d';ctx.lineWidth=2.4;ctx.beginPath();ctx.moveTo(-9,0);ctx.lineTo(0,0);ctx.lineTo(9,0);ctx.moveTo(9,0);ctx.lineTo(8,-1);ctx.stroke();
  ctx.strokeStyle='#222';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(8,-6);ctx.lineTo(8,6);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#222';ctx.fillRect(-3,-2,5,4);
 }
 ctx.restore();
 if(me){drawPerson(R.x,R.y,R.a,'#d4a017','me',0,.92);}
 else if(R.rc)drawPerson(R.x,R.y,R.a,R.rc,'ped',0,.8);
 if(R.k==='scoot'){const bx=R.x-Math.cos(R.a)*10,by=R.y-Math.sin(R.a)*10;ctx.strokeStyle='#9aa0a8';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(bx,by);ctx.lineTo(bx,by-30);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle=Math.sin(timeNow*20+R.x)>.3?'#5ff0ff':'#fff';circle(bx,by-31,2.2);}
 if(R.oma){
  drawPerson(R.x-Math.cos(R.a)*1,R.y-Math.sin(R.a)*1,R.a,'#9a7bbf','ped',0,.95);
  ctx.fillStyle='#e2e2ea';circle(R.x,R.y,3.5);ctx.fillStyle='#cfcfd8';circle(R.x-Math.cos(R.a)*2,R.y-Math.sin(R.a)*2,2.4);
  ctx.fillStyle='#b5503d';ctx.fillRect(R.x+Math.cos(R.a+1.57)*8-2,R.y+Math.sin(R.a+1.57)*8-2,5,4);
 }
}
function doGluehwein(){
 const w=noUse();if(w){toast(w);return false;}
 if(G.stock.gluehwein<1){toast('Kein Glühwein mehr. Die Hütten-Bar hat Nachschub.');return false;}
 G.stock.gluehwein--;G.drunk+=.7;needAdd(0,15);
 const cold=wxType()==='snow'||(ZONE&&ZONE.name==='berge');
 mood(7+(cold?6:0),'Mmh, warm!');sfx('glug');
 for(let i=0;i<5;i++)smokeFx(P.x,P.y-8);
 toast(pick(cold?['Dampfender Glühwein im Schnee. Es gibt kaum etwas Schöneres.','Die Hände werden warm, die Nase auch. Die Laune sowieso.','Zimt, Nelken, Orange. Der Winter kann kommen.']:['Glühwein ohne Schnee? Mutig. Aber es schmeckt trotzdem.','Warm von innen. Passt zu jedem Wetter, behauptet der Stand.']));
 if(G.drunk>=6)blackout();
 return true;
}
const GUNC=['#ff5fd0','#3fd0ff','#ffd23f','#7cff5f','#ff8a3c'];
function strandKids(z,out){
 const n=z.nogo;if(!n)return;
 const nm=['Lena','Ben','Mia','Emil','Finn','Lotta','Ole'];
 for(let i=0;i<6;i++){
  let x=(n.x0+n.x1)/2,y=(n.y0+n.y1)/2;
  for(let k=0;k<60;k++){
   const cx=rf(n.x0+40,n.x1-40),cy=rf(n.y0+30,n.y1-30);
   if(z.T[Math.floor(cy/TS)*ZW+Math.floor(cx/TS)]===SA){x=cx;y=cy;break;}
  }
  const q=mkPed(x,y);q.kid=true;q.gun=true;q.gc=pick(GUNC);q.hx0=(n.x0+n.x1)/2;q.hy0=(n.y0+n.y1)/2;
  q.nm=pick(nm);q.jb=pick(['Sandburg-Architekt','Wasserpistolen-Profi','Eis-Experte','Muschelsammlerin']);q.like=chance(.5);q.sp=rf(35,55);
  out.push(q);
 }
}
function waterProj(b,dt){
 b.t+=dt;
 const nx=b.x+b.vx*dt,ny=b.y+b.vy*dt,tx=Math.floor(nx/TS),ty=Math.floor(ny/TS);
 if(b.t>(b.life||.5))return true;
 if(isSolid(tx,ty)){
  for(let i=0;i<3;i++)FX.push({x:nx,y:ny,vx:rf(-25,25),vy:rf(-30,-5),g:120,t:0,life:.4,dot:'#9fd8ff',r:rf(1.2,2.4)});
  return true;
 }
 if(b.from==='ped'){
  if(!P.sit&&Math.hypot(P.x-nx,P.y-ny)<12){
   if(G.wet<3.5)addFx(P.x,P.y-18,pick(['Nass!','Platsch!','Kalt!','Hihi!']),'#9fd8ff');
   G.wet=5;mood(1,0);sfx('splash');
   for(let i=0;i<4;i++)FX.push({x:P.x,y:P.y-6,vx:rf(-30,30),vy:rf(-40,-10),g:120,t:0,life:.6,dot:'#9fd8ff',r:rf(1.5,3)});
   return true;
  }
 }else{
  for(let k=0;k<peds.length;k++){
   const p=peds[k];
   if(p.chair)continue;
   if(Math.hypot(p.x-nx,p.y-ny)<(p.snow?13:12)){hitWater(p);return true;}
  }
 }
 b.x=nx;b.y=ny;return false;
}
function mkCityRides(){
 RIDES=[];
 for(let i=0;i<2;i++){
  let p=null;
  for(let k=0;k<40;k++){const q=randTile([SW],0,0);if(!inNoGo(q.x,q.y)&&!hit(q.x,q.y,10)){p=q;break;}}
  if(!p)continue;
  const R=mkRide('chair',p.x,p.y,rf(0,6.283));
  const o=mkPed(p.x,p.y);o.oma=true;o.nm=OMAN[i%OMAN.length];o.jb='Rollstuhl-Profi';o.col='#9a7bbf';o.like=true;
  R.oma=o;RIDES.push(R);
 }
 for(let i=0;i<3;i++){
  const p=randTile([SW],0,0);
  if(inNoGo(p.x,p.y)||hit(p.x,p.y,10))continue;
  RIDES.push(mkRide('bike',p.x,p.y,rf(0,6.283)));
 }
 xRides();
 cityBoats();
}
function rheinY(x){return Math.round(15+Math.sin(x*.21)*3+Math.sin(x*.07+1)*2);}


const TEENJ=['16 Jahre alt, schwört aber, er sei 18','Schülersprecher mit Skateboard','Hausaufgaben-Flüchtling','Hat noch ein Pausenbrot dabei','Sammelt Sticker und Meinungen'];
const TEENN=['Lukas','Mia','Emre','Lena','Jonas','Sophie'];
function heroRank(){const h=Math.floor(G.hero||0);return h<3?'Neuling mit Cape':h<8?'Nachbarschaftsheld':h<16?'Park-Retter':h<30?'Imbiss-Held':'Superheld';}
function addHeroE(n){G.heroE=Math.min(100,(G.heroE||0)+n);}
function minorNear(x,y,r){
 if(!ZONE)for(let i=0;i<SKC.length;i++){const d=SKC[i];if(d.minor&&Math.hypot(d.x-x,d.y-y)<r)return true;}
 for(let i=0;i<kids.length;i++){if(Math.hypot(kids[i].x-x,kids[i].y-y)<r)return true;}
 for(let i=0;i<peds.length;i++){const p=peds[i];if((p.kid||p.teen)&&Math.hypot(p.x-x,p.y-y)<r)return true;}
 if(!ZONE&&SP){const L=['fb','bb','bs'];for(let k=0;k<3;k++){const f=SP[L[k]];if(f.jung&&f.pl.some(q=>Math.hypot(q.x-x,q.y-y)<r))return true;}}
 return false;
}
function addTeens(){
 for(let i=0;i<6;i++){
  const g=ZONES[i%ZONES.length];let x=g.x+rf(-70,70),y=g.y+rf(-70,70);
  const bad=(x,y)=>hit(x,y,7)||tget(Math.floor(x/TS),Math.floor(y/TS))===RD;
  for(let k=0;k<40&&bad(x,y);k++){x=g.x+rf(-90,90);y=g.y+rf(-90,90);}
  if(bad(x,y))continue;
  const q=mkPed(x,y);q.teen=true;q.nm=TEENN[i%TEENN.length];q.jb=pick(TEENJ);q.like=chance(.4);peds.push(q);
 }
}
function gangTH(){return ZONE&&CITYENT?CITYENT.thugs:thugs;}
function gangHeist(L,force){
 const TH=gangTH();
 TH.forEach(u=>{if(u.loot){u.loot.d++;if(u.loot.d>=2){if(u.loot.own)G.inv[u.loot.g]=(G.inv[u.loot.g]||0)+u.loot.q;L.push('Den Miesepetern wird von '+gq(u.loot.g,u.loot.q)+' ganz schlecht. Sie bringen alles zurück und entschuldigen sich.');u.loot=null;}}});
 if(!force&&!chance(.75))return;
 const c=TH.filter(u=>!u.loot&&u.ko<=0);if(!c.length)return;
 const u=pick(c);
 let g=pick(MENUS),own=false,q=rnd(3,6);
 u.loot={g:g,q:q,own:own,d:0};u.deal=0;u.dealCool=0;
 const txt='Die Miesepeter haben '+gq(g,q)+(own?' aus dem Imbiss-Lager':' von einer Lieferung')+' stibitzt und verstecken sich damit im Park. Schnapp sie dir, du gewinnst sowieso!';
 L.push(txt);
 setTimeout(()=>{try{msgCb(txt);}catch(e){}},force?400:3500);
}
function heroWin(u){
 let m='Der Miesepeter rutscht auf einer Bananenschale aus und sieht Sternchen.';
 G.hero=(G.hero||0)+.5;popAdd(2);xpAdd(6);
 if(u.loot){
  const l=u.loot,r=l.q*20+(l.own?0:60);
  G.cash+=r;G.stats.earned+=r;if(l.own)G.inv[l.g]=(G.inv[l.g]||0)+l.q;
  G.hero+=1+l.q/6;addHeroE(35);
  m='Beute zurück! '+gq(l.g,l.q)+(l.own?' liegen wieder im Imbiss-Lager.':' gehen zurück an die Kundschaft.')+' Belohnung '+eur(r)+'.';
  u.loot=null;sfx('win');
 }
 if(u.deal>0){G.hero+=1;G.cash+=50;m+=' Jugendschutz-Bonus: +50 €.';u.deal=0;u.dealT=null;u.dealCool=30;}
 else if(!/Belohnung/.test(m)){const c=rnd(15,40);G.cash+=c;m+=' Fundprämie '+eur(c)+'.';}
 P.heroT=10;
 msgCb(m);
}
function nearThug(){return !P.inCar&&thugs.some(u=>u.ko<=0&&(u.st==='chase'||u.loot)&&Math.hypot(u.x-P.x,u.y-P.y)<(G.heroE>=100?95:40));}
function punch(){
 const sup=G.heroE>=100,R=sup?100:40;
 let best=null,bd=R;
 thugs.forEach(u=>{if(u.ko>0)return;const d=Math.hypot(u.x-P.x,u.y-P.y);if(d<bd){bd=d;best=u;}});
 if(!best)return false;
 if(sup){
  G.heroE=0;shake=.9;sfx('scream');sfx('power');
  addFx(P.x,P.y-24,'SUPER-KONFETTI!','#ffd23f',1.6);
  for(let i=0;i<14;i++)FX.push({x:P.x,y:P.y,vx:Math.cos(i/14*6.283)*150,vy:Math.sin(i/14*6.283)*150,g:0,t:0,life:.6,dot:'#ffd23f',r:3});
  thugs.forEach(u=>{if(u.ko>0)return;if(Math.hypot(u.x-P.x,u.y-P.y)<100){u.hp=0;u.ko=25;u.st='cool';G.stats.fights++;heroWin(u);}});
  return true;
 }
 best.hp--;best.stun=.5;G.stats.fights++;sfx('hit');
 const a=Math.atan2(best.y-P.y,best.x-P.x);moveE(best,Math.cos(a)*22,Math.sin(a)*22,8);P.a=a;
 addFx(best.x,best.y-16,pick(['PFFT!','SPLASH!','KONFETTI!']),'#ffd23f',.8);
 if(best.hp<=0){best.ko=25;best.st='cool';heroWin(best);}
 return true;
}
function dealCheck(u,dt){
 u.dealCool=(u.dealCool||0)-dt;
 if(u.deal>0){
  u.deal+=dt;
  if(u.deal>10){
   u.deal=0;u.dealCool=30;const t=u.dealT;u.dealT=null;
   if(t){addFx(t.x,t.y-18,'Nee, ich bin erst 16!','#9ccc65',1.8);}
   msgCb('Der Jugendliche ist abgehauen. Verkauft wurde nichts, aber die Miesepeter geben nicht auf.');
  }
  return;
 }
 if(u.dealCool>0)return;
 const t=peds.find(p=>p.teen&&Math.hypot(p.x-u.x,p.y-u.y)<70);
 if(t){u.deal=.01;u.dealT=t;addFx(t.x,t.y-22,'!','#ff4040',2);addFx(u.x,u.y-22,'Psst ...','#ff8a65',2);msgCb('Ein Miesepeter bedrängt einen Jugendlichen im Park! Hilf ihm, Superheld!');}
}
function lootStep(u,dt,d,px,py){
 u.stun=Math.max(0,u.stun-dt);
 u.tauntT=(u.tauntT||0)-dt;
 if(u.st==='chase')u.st='idle';
 if(d<150&&u.stun<=0){
  const a=Math.atan2(u.y-py,u.x-px);moveE(u,Math.cos(a)*74*dt,Math.sin(a)*74*dt,8);u.a=a;u.walk=(u.walk||0)+dt*9;
  if(u.tauntT<=0){u.tauntT=4;addFx(u.x,u.y-20,pick(['Meins!','Fang mich!','Ohne Rezept!','Haha!']),'#ff8a65');}
 }else{
  if(Math.hypot(u.x-u.hx0,u.y-u.hy0)>150){const a=Math.atan2(u.hy0-u.y,u.hx0-u.x);moveE(u,Math.cos(a)*45*dt,Math.sin(a)*45*dt,8);u.a=a;u.walk=(u.walk||0)+dt*5;}
  else wander(u,dt,26,false);
 }
 dealCheck(u,dt);
}
function drawSack(u){
 ctx.strokeStyle='rgba(255,60,80,'+(.55+.25*Math.sin(timeNow*6))+')';ctx.lineWidth=2;ctx.beginPath();ctx.arc(u.x,u.y,19+Math.sin(timeNow*5)*2,0,6.283);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#8a6a3a';circle(u.x-7,u.y-3,5);
 ctx.fillStyle='#ffd23f';ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('$',u.x-7,u.y-3);
}
function drawCape(){
 const fl=Math.sin(timeNow*10)*2*Math.min(1,Math.hypot(P.vx,P.vy)/50)+(P.heroT>0?3:0);
 ctx.fillStyle='#d62828';ctx.beginPath();ctx.moveTo(0,-6);ctx.lineTo(0,6);ctx.lineTo(-11-fl,10);ctx.lineTo(-14-fl,0);ctx.lineTo(-11-fl,-10);ctx.closePath();ctx.fill();
 ctx.fillStyle='#ffd23f';ctx.fillRect(-9-fl*.6,-2,4,4);
}

const FISHT=[
 {n:'eine Sardine',m:4,w:30},{n:'einen Karpfen',m:6,w:26},{n:'einen Hecht',m:8,w:14},
 {n:'einen Goldfisch',m:10,w:8,t:'Ein Goldfisch! Er flüstert einen Wunsch. Du hörst nicht hin.'},
 {n:'einen alten Stiefel',m:3,w:10,nf:1,t:'Ein Stiefel! Immerhin wasserdicht.'},
 {n:'eine Flaschenpost',m:6,w:6,nf:1,c:20,t:'Flaschenpost! Darin: 20 € und ein Heiratsantrag an Unbekannt.'},
 {n:'eine Schatzkiste',m:12,w:3,nf:1,c:80,t:'Eine Schatzkiste! Drin: 80 € und ein Piratenhut.'}
];
function waterAhead(){
 if(!ZONE||!ZONE.swim||P.inCar||P.ride||P.sit||P.build||P.fish||P.fight||fade)return null;
 if(isDeep(P.x,P.y))return null;
 for(let d=18;d<=114;d+=16){const x=P.x+Math.cos(P.a)*d,y=P.y+Math.sin(P.a)*d;if(tget(Math.floor(x/TS),Math.floor(y/TS))===DP)return{x:x,y:y};}
 return null;
}
function startFish(){
 const w=waterAhead();if(!w)return;
 P.fish={x:w.x,y:w.y,t:0,w:rf(2.2,5),st:'wait'};P.vx=P.vy=0;sfx('swish');
 toast('Angel ausgeworfen. Warte, bis es zuckt, dann OK!');
}
function fishUpdate(dt){
 const f=P.fish;if(!f)return;
 if(keys.left||keys.right||keys.up||keys.down){P.fish=null;toast('Leine eingeholt.');return;}
 f.t+=dt;
 if(f.st==='wait'){if(f.t>=f.w){f.st='bite';f.t=0;sfx('bite');addFx(f.x,f.y-18,'!','#ff4040',1.2);}}
 else if(f.t>1.3){P.fish=null;addFx(f.x,f.y-14,'Entwischt!','#fff');toast('Zu langsam. Der Fisch ist weg.');}
}
function fishPull(){
 const f=P.fish;if(!f)return;
 if(f.st==='wait'){P.fish=null;toast('Zu früh! Die Fische lachen dich aus.');return;}
 P.fish=null;
 let s=0;FISHT.forEach(x=>{s+=x.w;});let r=Math.random()*s,c=FISHT[0];
 for(let i=0;i<FISHT.length;i++){r-=FISHT[i].w;if(r<=0){c=FISHT[i];break;}}
 const sk=ZONE&&ZONE.sharks&&ZONE.sharks.some(q=>Math.hypot(q.x-f.x,q.y-f.y)<200);
 if(sk&&chance(.35)){sfx('splash');mood(2,'+2');addFx(f.x,f.y-14,'SCHNAPP!','#ffffff');toast('Ein Hai klaut dir den Fang. Frechheit! Aber er hat sich bedankt.');return;}
 sfx('catch');mood(c.m,'+'+c.m);
 if(c.c){G.cash+=c.c;G.stats.earned+=c.c;}
 if(!c.nf){G.fang=(G.fang||0)+1;}
 addFx(f.x,f.y-16,'Fang!','#ffd23f',1.2);
 toast(c.t||('Du hast '+c.n+' gefangen! Sie wird im Strandgrill verewigt.'));
 if(!c.nf&&G.fang===10){G.cash+=100;toast('Zehn Fische! Du bist jetzt der Angelkönig von Rheinhanfen: +100 €.');}
}
function drawFishing(){
 const f=P.fish;if(!f)return;
 const bob=f.st==='bite'?Math.sin(timeNow*35)*2.5:Math.sin(timeNow*3)*1;
 ctx.strokeStyle='rgba(255,255,255,.8)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(P.x+Math.cos(P.a)*6,P.y+Math.sin(P.a)*6-4);ctx.quadraticCurveTo((P.x+f.x)/2,Math.min(P.y,f.y)-18,f.x,f.y+bob);ctx.stroke();
 ctx.strokeStyle='rgba(255,255,255,.5)';ctx.beginPath();ctx.ellipse(f.x,f.y+bob+2,8+Math.sin(timeNow*4)*2,4,0,0,6.283);ctx.stroke();
 ctx.fillStyle='#fff';circle(f.x,f.y+bob,3.5);ctx.fillStyle='#e5303a';ctx.beginPath();ctx.arc(f.x,f.y+bob,3.5,Math.PI,0);ctx.fill();
 if(f.st==='bite'){ctx.fillStyle='#ff4040';ctx.font='bold 22px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('!',f.x,f.y-18);}
}

function angTurn(a,b,k){let d=b-a;while(d>Math.PI)d-=6.283;while(d<-Math.PI)d+=6.283;return a+d*Math.min(1,k);}
function deepAt(x,y){return !!(ZONE&&ZONE.swim&&tget(Math.floor(x/TS),Math.floor(y/TS))===DP);}
function sharksUpdate(dt){
 const Z=ZONE;if(!Z||!Z.sharks)return;
 const inW=isDeep(P.x,P.y);
 Z.sharks.forEach(s=>{
  s.cool=Math.max(0,s.cool-dt);s.wag=(s.wag||0)+dt*6;if(s.shk>0)s.shk-=dt;
  if(P.fight&&P.fight.s===s)return;
  const d=Math.hypot(P.x-s.x,P.y-s.y);
  let sp=36;
  if(s.flee>0){s.flee-=dt;s.a=angTurn(s.a,Math.atan2(s.y-P.y,s.x-P.x),dt*3);sp=110;}
  else if(inW&&d<240){s.a=angTurn(s.a,Math.atan2(P.y-s.y,P.x-s.x),dt*2.2);sp=d<100?68:90;}
  else if(chance(dt*.5))s.a+=rf(-.9,.9);
  const nx=s.x+Math.cos(s.a)*sp*dt,ny=s.y+Math.sin(s.a)*sp*dt;
  if(deepAt(nx,ny)&&deepAt(nx+Math.cos(s.a)*22,ny+Math.sin(s.a)*22)){s.x=nx;s.y=ny;}else{s.a+=2+rf(-.4,.4);}
  if(s.flee<=0&&s.cool<=0&&inW&&!P.fight&&d<26){
   s.cool=3;shake=.3;sfx('bonk');addFx(P.x,P.y-16,pick(['Rempler!','Flosse!','Hui!']),'#ffffff');
   const a=Math.atan2(P.y-s.y,P.x-s.x);
   if(P.ride){P.ride.sp*=.3;moveE(P.ride,Math.cos(a)*18,Math.sin(a)*18,11);P.x=P.ride.x;P.y=P.ride.y;}
   else moveE(P,Math.cos(a)*30,Math.sin(a)*30,7);
  }
 });
}
function nearShark(){
 if(!ZONE||!ZONE.sharks||P.inCar||P.ride||P.fight||fade||!isDeep(P.x,P.y))return null;
 let b=null,bd=46;
 ZONE.sharks.forEach(s=>{if(s.flee>0)return;const d=Math.hypot(s.x-P.x,s.y-P.y);if(d<bd){bd=d;b=s;}});
 return b;
}
function startFight(s){
 P.fight={s:s,t:0,hits:0,need:6,max:7};P.vx=P.vy=0;s.cool=99;
 sfx('bonk');addFx(s.x,s.y-18,'GRRR!','#ffffff');
 toast('Hai-Ringkampf! Drück OK, so schnell du kannst!');
}
function sharkPress(){
 const f=P.fight;if(!f)return;
 f.hits++;f.s.shk=.25;sfx('hit');
 addFx(f.s.x+rf(-12,12),f.s.y-12,pick(['PFFT!','SPLASH!','PLUMPS!','KONFETTI!']),'#ffd23f',.8);
 for(let i=0;i<4;i++)FX.push({x:f.s.x,y:f.s.y,vx:rf(-60,60),vy:rf(-80,-20),g:200,t:0,life:.7,dot:'#cfeaff',r:2.5});
 if(f.hits>=f.need){
  const s=f.s;P.fight=null;s.flee=7;s.cool=6;G.zahn=(G.zahn||0)+1;G.hero=(G.hero||0)+.5;addHeroE(25);
  mood(14,'Hai besiegt!');sfx('win');
  addFx(s.x,s.y-20,'Ich geb auf!','#ffffff',1.8);
  toast('Der Hai gibt auf, schwimmt beleidigt davon und lässt einen Zahn zurück. Haizähne: '+G.zahn+'.');
 }
}
function fightUpdate(dt){
 const f=P.fight;if(!f)return;
 f.t+=dt;
 if(f.t>=f.max){
  const s=f.s;P.fight=null;s.cool=4;
  const a=Math.atan2(P.y-s.y,P.x-s.x);moveE(P,Math.cos(a)*40,Math.sin(a)*40,7);
  toast('Der Hai schüttelt dich ab und tut so, als wäre nichts gewesen.');
 }
}
function drawShark(s){
 ctx.save();ctx.translate(s.x,s.y);ctx.rotate(s.a);
 const w=Math.sin(s.wag||0)*4+(s.shk>0?Math.sin(timeNow*40)*3:0);
 ctx.strokeStyle='rgba(255,255,255,.35)';ctx.lineWidth=1.5;ctx.beginPath();ctx.ellipse(-8,0,26,10,0,0,6.283);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='rgba(0,40,70,.25)';ctx.beginPath();ctx.ellipse(2,5,23,8,0,0,6.283);ctx.fill();
 ctx.fillStyle='#7d8a96';ctx.beginPath();ctx.moveTo(26,0);ctx.quadraticCurveTo(10,-9,-12,-5);ctx.lineTo(-26,w-9);ctx.lineTo(-21,w);ctx.lineTo(-26,w+9);ctx.lineTo(-12,5);ctx.quadraticCurveTo(10,9,26,0);ctx.fill();
 ctx.fillStyle='#69757f';ctx.beginPath();ctx.moveTo(7,-6);ctx.lineTo(-1,-17);ctx.lineTo(-4,-5);ctx.fill();ctx.beginPath();ctx.moveTo(7,6);ctx.lineTo(-1,17);ctx.lineTo(-4,5);ctx.fill();
 ctx.fillStyle='#4f5b66';ctx.beginPath();ctx.moveTo(4,0);ctx.lineTo(-9,-3);ctx.lineTo(-9,3);ctx.fill();
 if(s.flee>0){ctx.fillStyle='#111';ctx.fillRect(15,-5,5,4);ctx.fillRect(15,1,5,4);}
 else{ctx.fillStyle='#111';ctx.fillRect(16,-4,2,2);ctx.fillRect(16,2,2,2);ctx.fillStyle='#fff';ctx.fillRect(22,-1,2,2);}
 ctx.restore();
}
function whaleUpdate(dt){
 const W=ZONE&&ZONE.whale;if(!W)return;
 W.x+=Math.cos(W.a)*W.sp*dt;
 if(W.x>43*TS)W.a=Math.PI;else if(W.x<6*TS)W.a=0;
 if(W.open>0&&!fade)W.open=Math.max(0,W.open-dt*.8);
 W.spout-=dt;
 if(W.spout<=0){
  W.spout=rf(4,7);
  const dir=Math.cos(W.a)>=0?1:-1;
  for(let i=0;i<9;i++)FX.push({x:W.x+dir*22,y:W.y-4,vx:rf(-18,18),vy:rf(-120,-70),g:200,t:0,life:1,dot:'#d8f0ff',r:rf(2,3.5)});
 }
 if(!W.seen&&Math.hypot(P.x-W.x,P.y-W.y)<300){W.seen=true;toast('Da! Ein Wal! Schwimm oder fahr ran und sag Hallo.');}
}
function nearWhale(){
 const W=ZONE&&ZONE.whale;if(!W||P.inCar||fade||P.fight||!isDeep(P.x,P.y))return null;
 return Math.hypot(P.x-W.x,P.y-W.y)<100?W:null;
}
function swallow(){
 const W=ZONE.whale;W.open=1;
 if(P.ride){P.ride.sp=0;P.ride=null;}
 sfx('whale');
 startFade('Der Wal sagt Hallo, öffnet sein riesiges Maul ... SCHLUCK! Es wird warm, wabbelig und seltsam gemütlich.',()=>{enterZone('wal');});
}
function drawWhale(W){
 ctx.save();ctx.translate(W.x,W.y);ctx.scale(Math.cos(W.a)>=0?1:-1,1);
 const tw=Math.sin(timeNow*1.6)*8;
 ctx.strokeStyle='rgba(255,255,255,.4)';ctx.lineWidth=2;ctx.beginPath();ctx.ellipse(-4,2,92,32,0,0,6.283);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='rgba(0,40,70,.25)';ctx.beginPath();ctx.ellipse(4,10,82,26,0,0,6.283);ctx.fill();
 ctx.fillStyle='#46708f';
 ctx.beginPath();ctx.ellipse(0,0,78,26,0,0,6.283);ctx.fill();
 ctx.beginPath();ctx.moveTo(-60,-13);ctx.lineTo(-92,tw-5);ctx.lineTo(-92,tw+5);ctx.lineTo(-60,13);ctx.closePath();ctx.fill();
 ctx.beginPath();ctx.ellipse(-98,tw-14,10,24,.5,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(-98,tw+14,10,24,-.5,0,6.283);ctx.fill();
 ctx.fillStyle='#5b87a8';ctx.beginPath();ctx.ellipse(8,-3,60,13,0,0,6.283);ctx.fill();
 ctx.fillStyle='#46708f';ctx.beginPath();ctx.ellipse(24,22,14,6,.5,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(24,-22,14,6,-.5,0,6.283);ctx.fill();
 ctx.fillStyle='#e8f3fa';ctx.fillRect(20,-1,4,2);ctx.fillRect(34,-1,4,2);
 ctx.fillStyle='#fff';circle(52,-15,4.5);circle(52,15,4.5);ctx.fillStyle='#111';circle(53,-15,2.2);circle(53,15,2.2);
 if(W.open>0){ctx.fillStyle='#7a1f3a';ctx.beginPath();ctx.ellipse(74,0,16*W.open+2,22*W.open+2,0,0,6.283);ctx.fill();ctx.fillStyle='#e07a98';ctx.beginPath();ctx.ellipse(70,0,9*W.open,12*W.open,0,0,6.283);ctx.fill();}
 else{ctx.strokeStyle='#2c4a63';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(78,-6);ctx.quadraticCurveTo(66,0,78,6);ctx.stroke();ctx.lineWidth=1;}
 ctx.restore();
}
function drawSeaLife(cx,cy){
 if(!ZONE)return;
 const inView=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 if(ZONE.whale&&inView(ZONE.whale.x,ZONE.whale.y,130))drawWhale(ZONE.whale);
 if(ZONE.sharks)ZONE.sharks.forEach(s=>{if(inView(s.x,s.y,40))drawShark(s);});
}
function teaBonus(){
 G.teaT=40;needAdd(0,30);
 mood(7+(G.high>0?5:0),G.high>0?'Tee & Joint!':'Ahh, Tee!');sfx('glug');
 toast(pick(['Kamillentee aus der Walwärme. Schmeckt nach Meer und Geborgenheit.','Du pustest in die Tasse. Der Wal brummt zufrieden vor sich hin.','Ein Schluck Tee, ein Zug Joint. Der Wal summt dazu.']));
}
function ext6Update(dt){
 if(!G)return;
 if(fade){P.fish=null;P.fight=null;}
 if(P.heroT>0)P.heroT-=dt;
 if(G.teaT>0)G.teaT-=dt;
 if(G.heroE===undefined)G.heroE=0;
 if(G.heroE<100){G.heroE=Math.min(100,G.heroE+dt*1.8);if(G.heroE>=100){toast('Heldenkraft aufgeladen! Der nächste Treffer ist ein SUPER-KONFETTI.');sfx('power');}}
 fishUpdate(dt);sharksUpdate(dt);fightUpdate(dt);whaleUpdate(dt);
}
window.HHX={zone:function(){return ZONE;},skl:skl,skEvent:skEvent,skOpen:skOpen,skAct:skAct,nearSk:nearSk,skClear:function(){SKC.length=0;},gangHeist:gangHeist,heroWin:heroWin,punch:punch,startFish:startFish,fishPull:fishPull,waterAhead:waterAhead,nearShark:nearShark,startFight:startFight,sharkPress:sharkPress,nearWhale:nearWhale,swallow:swallow,minorNear:minorNear,addTeens:addTeens,heroRank:heroRank,lootStep:lootStep,dealCheck:dealCheck,teaBonus:teaBonus,gangTH:gangTH};

let SKC=[],SKT=40,SKL='';
const ZWN=[['Gluckser','#e5604d','#3d6fb5'],['Wuschel','#f1c40f','#8a4a2a'],['Knorzel','#2e86c1','#b5651d'],['Zipfel','#8e44ad','#4a7a3a'],['Mampfi','#e67e22','#5a5a8a'],['Brösel','#16a085','#a03a3a'],['Tüddel','#d35bb5','#3a6a8a']];
const ZWB=['#f4f4f4','#e6d9b8','#c9c9c9','#f0e0c8','#d8d8e0','#e9dfcf','#fafafa'];
const ZWL=['Wir haben keine Zeit. Wir marschieren.','Hast du Pilze gesehen? Nur so.','Wir sind sieben. Das ist Absicht.','Mein Bart ist länger als dein Feierabend.','Wohin? Immer der Nase nach. Das ist der Plan.','Wir suchen die Mitte vom Nirgendwo.','Ich trage die Laterne. Die anderen tragen Meinungen.','Nicht stehen bleiben! Wer stehen bleibt, muss Mützen zählen.'];
const WUNSCH=['Ein Schlitten, der von allein den Berg hochfährt.','Mehr Wochenende pro Woche.','Eine Taube, die Hallo sagt.','Schnee, aber nur zum Spielen.','Ein Bett, das nie klingelt.'];
const KNABL=['Mmh! Ein Gumdrop-Fenster. Fruchtig und leicht klebrig.','Du knabberst an der Dachkante. Zimt, Honig, Glück.','Krack! Ein Stück Zuckerguss. Das Haus wächst bestimmt nach.','Lebkuchen von der Wand. Wer hat das erfunden? Ein Genie.'];
function skl(){return(ZONE?ZONE.ska:SKC)||[];}
function skOk(x,y){
 if(hit(x,y,6))return false;
 const t=tget(Math.floor(x/TS),Math.floor(y/TS));
 if(t===RD)return false;
 if(!ZONE&&t===DK)return false;
 if(t===SH||t===DP)return false;
 return true;
}
function mkZwerge(x,y){
 const g=[];
 for(let i=0;i<7;i++){const q=ZWN[i];g.push({k:'zw',i:i,nm:q[0],hc:q[1],jc:q[2],bc:ZWB[i],x:x-i*16,y:y,a:0,walk:rf(0,6),hop:0,cd:0,dn:0,steer:rf(1,3),lead:i===0});}
 g.forEach(d=>{const f=freeSpot(d.x,d.y);d.x=f.x;d.y=f.y;});
 return g;
}
function mkMusik(x,y){const f=freeSpot(x,y);return{k:'mu',x:f.x,y:f.y,a:rf(0,6.28),walk:0,cd:0,dn:0,play:0,steer:rf(1,3),life:90,lead:true};}
function steerStep(d,dt,sp){
 d.steer-=dt;
 if(d.steer<=0){d.a+=rf(-.8,.8);d.steer=rf(3,6);}
 const nx=d.x+Math.cos(d.a)*sp*dt,ny=d.y+Math.sin(d.a)*sp*dt;
 if(skOk(nx,ny)){d.x=nx;d.y=ny;d.walk+=dt*8;}
 else{d.a+=(chance(.5)?1:-1)*rf(1.2,2.2);d.steer=rf(1,3);}
}
function zwStep(g,dt){
 for(let i=0;i<g.length;i++){
  const d=g[i];
  if(d.dn>0){d.dn-=dt;d.walk+=dt*10;continue;}
  if(i===0){steerStep(d,dt,44);continue;}
  const p=g[i-1],dx=p.x-d.x,dy=p.y-d.y,L=Math.hypot(dx,dy);
  if(L>240){const f=freeSpot(p.x,p.y);d.x=f.x;d.y=f.y;continue;}
  if(L>17){
   d.a=Math.atan2(dy,dx);
   const s=Math.min(47*dt,L-17),sx=Math.cos(d.a)*s,sy=Math.sin(d.a)*s;
   if(skOk(d.x+sx,d.y+sy)){d.x+=sx;d.y+=sy;d.walk+=dt*8;}
   else if(skOk(d.x+sx,d.y)){d.x+=sx;d.walk+=dt*8;}
   else if(skOk(d.x,d.y+sy)){d.y+=sy;d.walk+=dt*8;}
  }
 }
}
function skSpawn(){
 for(let k=0;k<70;k++){
  const a=rf(0,6.283),d=rf(260,430),x=P.x+Math.cos(a)*d,y=P.y+Math.sin(a)*d;
  const tx=Math.floor(x/TS),ty=Math.floor(y/TS);
  if(tx<3||ty<3||tx>MW-4||ty>MH-4)continue;
  const t=tget(tx,ty);
  if(t!==SW&&t!==GR)continue;
  if(!skOk(x,y))continue;
  return{x:x,y:y,a:Math.atan2(P.y-y,P.x-x)+rf(-.5,.5)};
 }
 return null;
}
function skEvent(){
 const k=pick(['zwerge','musik','holle','schnee','alice','merlin','herk','pirat','kitz'].filter(q=>q!==SKL));
 if(k==='holle'){
  if(WXC.type==='snow')return;
  SKL=k;WXC.type='snow';WXC.t=rf(40,60);
  toast('Irgendwo schüttelt Frau Holle ihre Kissen aus. In Rheinhanfen schneit es Federn!');
  mood(3,'+3 Schnee');sfx('magic');
  for(let i=0;i<10;i++)addFx(P.x+rf(-120,120),P.y+rf(-90,-20),'*','#ffffff',2.2,rf(12,30));
  return;
 }
 const sp=skSpawn();if(!sp)return;
 SKL=k;
 if(fairyEvent(k,sp)){sfx('arrive');return;}
 if(k==='zwerge'){
  const g=mkZwerge(sp.x,sp.y);g.forEach(d=>{d.a=sp.a;d.ev=1;});g[0].life=85;
  SKC.push.apply(SKC,g);
  toast('Sieben Zwerge marschieren durchs Bild. Niemand fragt, wohin.');
 }else{
  const m=mkMusik(sp.x,sp.y);m.a=sp.a;m.ev=1;SKC.push(m);
  toast('Die Stadtmusikanten sind in der Stadt: Esel, Hund, Katze und Hahn als Turm aus Talent.');
 }
 sfx('arrive');
}
function skEnter(z){
 if(z.skInit)return;
 z.skInit=true;
 if(z.name==='maerchen'){
  z.ska=mkZwerge(36*TS+16,21*TS+16);
  fairyMaerchen(z);qMaerchen(z);
  z.ska.push({k:'hexe',x:33.6*TS,y:10.9*TS,a:0,cd:0});
  z.ska.push({k:'holle',x:10.4*TS,y:8.9*TS,a:0,cd:0,fe:0});
  const mu=mkMusik(21*TS,12*TS);mu.life=1e9;z.ska.push(mu);
  z.ska.push({k:'hase',x:13*TS+16,y:26*TS+12,st:'idle',dir:1,round:0,t:0,walk:0,bet:null,cd:0});
  z.ska.push({k:'ig',e:0,x:13*TS+16,y:26*TS+30,show:0});z.ska.push({k:'ig',e:1,x:33*TS+16,y:26*TS+30,show:0});
  {const f1=freeSpot(16*TS,15*TS),f2=freeSpot(13*TS,18*TS);z.ska.push({k:'kap',x:f1.x,y:f1.y,a:0,walk:0,steer:2,cd:0,pause:0});z.ska.push({k:'wolf',x:f2.x,y:f2.y,a:0,walk:0,steer:2,cd:0,st:'lurk',t:rf(14,22),zz:0,hop:0});}
  const cx0=28*TS,cy0=6*TS,cc=['#e5504d','#2e86c1','#f1c40f','#27ae60','#d35bb5','#ff9a3c'];
  z.candy=[[22,20],[62,14],[100,24],[140,14],[170,22],[30,56],[80,46],[118,52],[160,60],[98,86]].map((s,i)=>({x:cx0+s[0],y:cy0+s[1],c:cc[i%6],on:true,t:0}));
  z.wx0='none';z.hcd=0;z.tcd=0;
 }else if(z.name==='schlaraff'){
  z.ska=[[16,14],[28,10],[30,24],[22,20]].map((q,i)=>({k:'huhn',x:q[0]*TS,y:q[1]*TS,a:i*1.6,steer:rf(1,3),walk:i,cd:0}));
 }else if(z.name==='bayern'){
  z.ska=[];
  [[8,12],[11,15],[14,19],[10,22]].forEach(q=>z.ska.push(mkKuh(q[0]*TS,q[1]*TS)));
  const bl=mkMusik(22*TS,19*TS);bl.v='blas';bl.life=1e9;z.ska.push(bl);
 }else if(z.name==='oesterreich'){
  z.ska=[[24,21],[28,23],[22,25]].map(q=>{const c=mkKuh(q[0]*TS,q[1]*TS);c.hx=25*TS;c.hy=23*TS;return c;});
  z.ska.push({k:'jodl',x:15.5*TS,y:8.6*TS,a:0,cd:0});kSkaOesi(z);
 }else if(z.name==='gallien'){
  galSka(z);
 }else if(z.name==='zoo'){
  zooSka(z);
 }else if(z.name==='plantage'){
  plantageSka(z);
 }else if(z.name==='freibad'||z.name==='camping'){
  kSka(z);
 }else if(z.name==='holly'){
  medSka(z);
 }else if(z.name==='amt'){
  z.ska=[[18,18,'beamt'],[30,19,'forma'],[22,22,'ordn'],[36,17,'zgn']].map(q=>({k:q[2],x:q[0]*TS,y:q[1]*TS,hx:q[0]*TS,hy:q[1]*TS,a:rf(0,6.28),walk:0,steer:2,cd:rf(1,5)}));
  z.ska.push(xnNew('roem',20.5,15.8,{a:-Math.PI/2}),xnNew('rom',22.4,15.8,{a:-Math.PI/2}));
 }else if(z.name==='helden'){
  z.ska=[[12,12],[36,12],[14,21],[34,21],[24,19]].map((q,i)=>({k:'hero',hv:i,x:q[0]*TS,y:q[1]*TS,hx:q[0]*TS,hy:q[1]*TS,a:rf(0,6.28),walk:0,steer:2,cd:rf(1,5)}));
 }else if(z.name==='sender'){
  z.ska=[[20,14,'mod'],[31,15,'prak'],[11,17,'gurke'],[37,18,'rep']].map(q=>({k:q[2],x:q[0]*TS,y:q[1]*TS,hx:q[0]*TS,hy:q[1]*TS,a:rf(0,6.28),walk:0,steer:2,cd:rf(1,5)}));
 }else if(z.name==='feldweg'){
  z.ska=[{k:'bauer',x:24*TS,y:17*TS+16,a:0,walk:0,steer:2,cd:0}];
  [[10,10,'#ffd23f'],[34,9,'#ff9a3c'],[24,12,'#5ff0ff'],[40,11,'#ff5fd0']].forEach(q=>z.ska.push({k:'falter',x:q[0]*TS,y:q[1]*TS,hx:q[0]*TS,hy:q[1]*TS,a:rf(0,6.28),steer:1,walk:rf(0,6),col:q[2]}));
 }else if(z.name==='koeln'){
  z.ska=[{k:'koebes',x:19*TS,y:16*TS,a:0,walk:0,steer:2,cd:0}];
  const jk=mkMusik(30*TS,17*TS);jk.v='jeck';jk.life=1e9;z.ska.push(jk);
 }else if(z.name==='wuppertal'){
  z.ska=[{k:'schweb',x:5*TS,y:wcy(5)*TS+16,dir:1,st:'go',t:0,cd:0,walk:0}];
 }else if(z.name==='portugal'){
  z.ska=[{k:'tram',x:10*TS,y:14*TS+26,dir:1,st:'go',t:0,cd:0,walk:0},{k:'fado',x:23*TS,y:23*TS,a:0,cd:0,walk:0}];
 }else if(z.name==='fpark'){
  z.ska=[{k:'flocke',x:24*TS+16,y:27*TS,hx:24*TS+16,hy:27*TS,a:0,walk:0,steer:2,cd2:0,tk:2}];
 }else if(z.name==='berge'){
  z.ska=[];
  z.ska.push({k:'wm',x:9.5*TS,y:17.6*TS,a:0,cd:0,ho:6});
  let gx=18,gy=0;while(gy<ZH&&z.T[gy*ZW+gx]===RK)gy++;
  z.ska.push({k:'gr',x:gx*TS+16,y:gy*TS+8,hx:gx*TS+16,hy:gy*TS+8,st:'hide',t:0,cd:0,gf:0,a:0});
  z.pcd=0;z.packs=0;qBerge(z);kSkaBerge(z);
 }
}
function nearSk(){
 if(P.inCar||P.sit||P.ride||P.build||P.fish||P.fight)return null;
 let b=null,bd=99;
 skl().forEach(d=>{
  if(d.k==='ig'||d.k==='falter')return;
  const r=d.k==='gr'?46:d.k==='mu'?40:(d.k==='tram'||d.k==='schweb')?72:34,dd=Math.hypot(d.x-P.x,d.y-P.y)-(r-34);
  if(dd<34&&dd<bd){bd=dd;b=d;}
 });
 return b;
}
function skPrompt(d){
 if(d.k==='flocke')return 'OK: Flocke abklatschen';
 if(FAIRY[d.k])return 'OK: '+FAIRY[d.k].p;
 if(d.k==='zw')return 'OK: '+d.nm+' zuwinken';
 if(d.k==='hexe')return 'OK: Zur lieben Hexe';
 if(d.k==='holle')return 'OK: Frau Holle helfen';
 if(d.k==='wm')return 'OK: Weihnachtsmann ansprechen';
 if(d.k==='gr')return 'OK: Berg-Griesgram ansprechen';
 if(d.k==='kap')return 'OK: Rotkäppchen ansprechen';
 if(d.k==='hase')return 'OK: Hasen ansprechen';
 if(d.k==='huhn')return 'OK: Brathähnchen schnappen';
 if(d.k==='kuh')return 'OK: Kuh streicheln';
 if(d.k==='fado')return 'OK: Dem Fado lauschen';
 if(d.k==='tram')return 'OK: Straßenbahn nehmen';
 if(d.k==='schweb')return 'OK: Schwebebahn nehmen';
 if(d.k==='tuffi')return 'OK: Tuffi zuwinken';
 if(d.k==='koebes')return 'OK: Köbes ansprechen';
 if(d.k==='bauer')return 'OK: Bauer Hannes ansprechen';
 if(d.k==='mod')return 'OK: Moderator ansprechen';
 if(d.k==='prak')return 'OK: Praktikant ansprechen';
 if(d.k==='gurke')return 'OK: Werbe-Gurke ansprechen';
 if(d.k==='rep')return 'OK: Reporter ansprechen';
 if(d.k==='hero')return 'OK: '+HER[d.hv].n+' ansprechen';
 if(YK[d.k])return ykPrompt(d);
 if(QSK[d.k])return qPrompt(d);
 if(PSK[d.k])return plantPrompt(d);
 if(XNPC[d.k])return xnPrompt(d);
 if(AMD[d.k])return 'OK: '+AMD[d.k].n+' ansprechen';
 if(d.k==='jodl')return 'OK: Dem Jodler zuhören';
 if(d.k==='mu'&&d.v==='jeck')return 'OK: Mitschunkeln';
 if(d.k==='mu'&&d.v==='blas')return 'OK: Zugabe von der Blaskapelle';
 if(d.k==='wolf')return d.st==='sleep'?'OK: Schlafenden Wolf ansehen':'OK: Wolf ansprechen';
 return 'OK: Zugabe fordern';
}
function startSk(k,dur,msg){
 P.build={k:k,t:0,dur:dur,fx:0};
 P.vx=P.vy=0;keys.left=keys.right=keys.up=keys.down=0;
 toast(msg);
}
function mdl(title,text,ch){showModal({title:title,text:text,choices:ch.map(c=>({label:c[0],a:'skA',p:c[1],off:!!c[2]})).concat([{label:'Tschüss',a:'mclose'}])});}
function skMarker(mk){
 const k=mk.sk||mk.id;
 if(k==='haus')hexeMenu();
 else if(k==='holle')holleMenu();
 else if(k==='werk')werkMenu();
 else if(k==='tisch')tischMenu();
 else if(k==='hase')hasenMenu();
 else if(k==='pudding')puddingMenu();
 else if(k==='burg')burgMenu();
 else if(k==='braum')braumeisterMenu();
 else if(k==='walzer')walzerMenu();
 else if(k==='tafel')natureMenu();
 else if(k==='wurf')wurfMenu();
 else if(k==='prue')pruMenu();
 else if(k==='nummer')nummerMenu();
 else if(k==='stempel')stempelMenu();
 else if(k==='reise'){UI.euroFrom='';show('euro');}
 else if(k==='fb'||k==='bb'||k==='bs')sportMenu(k);
 else if(k==='bahn'||k==='rad'||k==='karu')fpMenu(k);
 else if(k==='dosen')dosMenu();
 else if(k==='fw')fwMenu();
 else if(k==='kh')khMenu();
 else if(KSKM[k])KSKM[k](mk);
 else if(k==='zoo')zooMenu();
 else if(k==='kessel')druidMenu();
 else if(k==='pfoertner')pfoertnerMenu();
 else if(k==='ausgang')ausgangMenu();
 else if(ESK[k])eMenu(k);
}
function skOpen(d){
 if(d.k==='flocke'){flockeHi(d);return;}
 if(FAIRY[d.k]){fairyOpen(d);return;}
 if(d.k==='zw'){
  if(d.cd>0){toast(d.nm+' ist im Marschmodus und kann gerade nicht.');return;}
  d.cd=7;d.hop=.8;mood(3,'+3');sfx('clap');
  addFx(d.x,d.y-20,'Klatsch!','#ffd23f');
  toast(d.nm+': "'+pick(ZWL)+'"');
 }else if(d.k==='hexe')hexeMenu();
 else if(d.k==='holle')holleMenu();
 else if(d.k==='wm')werkMenu();
 else if(d.k==='gr')griesMenu(d);
 else if(d.k==='kap')kapMenu();
 else if(d.k==='wolf')wolfMenu();
 else if(d.k==='hase')hasenMenu();
 else if(d.k==='huhn')huhnFang(d);
 else if(d.k==='kuh')kuhStreichel(d);
 else if(d.k==='fado')fadoHoeren(d);
 else if(d.k==='tram')tramFahrt(d);
 else if(d.k==='schweb')schwebFahrt(d);
 else if(d.k==='tuffi')tuffiRuessel(d);
 else if(d.k==='koebes')koebesAnsprechen(d);
 else if(d.k==='bauer')bauerMenu();
 else if(d.k==='mod')modMenu();
 else if(d.k==='prak')prakMenu();
 else if(d.k==='gurke')gurkeMenu();
 else if(d.k==='rep')repMenu();
 else if(d.k==='hero')heroMenu(d.hv);
 else if(YK[d.k])ykOpen(d);
 else if(QSK[d.k])qOpen(d);
 else if(PSK[d.k])plantOpen(d);
 else if(XNPC[d.k])xnOpen(d);
 else if(AMD[d.k])amtMenu(d.k);
 else if(d.k==='jodl')jodlerMenu();
 else if(d.k==='mu'){
  if((d.v==='blas'||d.v==='jeck')&&!d.skip){schunkelMenu(d);return;}
  d.skip=false;
  if(d.cd>0){toast(d.v==='blas'?'Die Blaskapelle holt kurz Luft. Tuba braucht viel davon.':d.v==='jeck'?'Die Jecken holen kurz Luft. Alaaf ist anstrengend.':'Die Stadtmusikanten holen kurz Luft.');return;}
  d.cd=12;d.play=5;mood(6,'+6 Zugabe');sfx('musik');
  (d.v==='blas'?['Oans!','Zwoa!','Drei!','Humtata!']:d.v==='jeck'?['Alaaf!','Kamelle!','Strüßje!','Tätää!']:['I-A!','Wuff!','Miau!','Kikeriki!']).forEach((s,i)=>addFx(d.x+(i-1.5)*10,d.y-36-i*3,s,'#ffe08a',1.8));
  peds.forEach(p=>{if(!p.snow&&p.st==='walk'&&Math.hypot(p.x-d.x,p.y-d.y)<220){p.st='dance';p.stT=6;}});
  skl().forEach(q=>{if(q.k==='zw')q.dn=5;});
  toast(d.v==='blas'?'Die Blaskapelle spielt einen zünftigen Marsch. Alle in Hörweite schunkeln mit.':d.v==='jeck'?'Die Jecken ziehen vorbei, werfen Kamelle und Konfetti, und alle schunkeln untergehakt mit. Alaaf!':'Die Stadtmusikanten spielen auf. Alle in Hörweite tanzen mit.');
 }
}
function hexeMenu(){
 const z=ZONE,off=!z||z.tcd>0;
 mdl('Lebkuchenhaus','Die liebe Hexe winkt aus dem Fenster: "Na, mein Schatz? Du siehst hungrig aus. Knabber ruhig am Haus, es wächst von allein nach."',[
  ['Am Haus knabbern','knab'],['Lebkuchen einpacken ('+(G.lk||0)+' / 5)','lk'],['Kräutertee mit der Hexe','tee',off],['Einen Zauber wünschen','zau']]);
}
function holleMenu(){
 mdl('Frau Holle','"Ach, gut dass du da bist! Die Betten müssen geschüttelt werden, damit es auf der Welt schneit. Und das Brot im Ofen ruft schon wieder."',[
  ['Kissen mitschütteln','kiss',!!(ZONE&&ZONE.hcd>0)],['Brot aus dem Ofen holen','brot']]);
}
function werkMenu(){
 const g=skl().find(d=>d.k==='gr');
 mdl('Weihnachtswerkstatt','Der Weihnachtsmann: "Ho ho ho! Jedes Jahr dasselbe Chaos. Und jede Nacht stehen fertige Pakete da, die ich nie gepackt habe. Ich vermute einen Helfer im Berg."'+(g&&g.st==='help'?' Der Griesgram packt in der Ecke. Er schaut weg.':''),[
  ['Geschenke einpacken helfen','pack',!!(ZONE&&ZONE.pcd>0)],['Wunschzettel abgeben','wish']]);
}
function griesMenu(g){
 if(g.st==='help'||g.st==='go'){toast(pick(['Der Griesgram murmelt: "Schleife schief. Alles Mist."','Er schaut kurz hoch, brummt, packt weiter. Ein Mundwinkel zuckt.']));return;}
 if(g.st==='hide')g.st='peek';g.t=3;
 const n=G.lk||0;
 const txt=g.gf<1?'Aus der Felsspalte starren dich zwei gelbe Augen an. "Hmpf. Geh weg. Ich mag keine Leute. Und keinen Trubel."':g.gf<3?'Der Griesgram knurrt: "Lebkuchen? Für mich? ... Na gut. Aber das heißt nichts."':'Er scharrt verlegen mit dem Fuß: "Ich glaube, ich könnte dem Dicken im roten Mantel mal helfen. Nur dieses eine Mal."';
 showModal({title:'Berg-Griesgram',text:txt,choices:[{label:'Lebkuchen anbieten ('+n+')',a:'skA',p:'gift',off:n<1},{label:'Freundlich winken',a:'skA',p:'wave'},{label:'Weitergehen',a:'mclose'}]});
}
function skAct(p){
 const z=ZONE;
 if(p==='zau'){
  showModal({title:'Zauberwunsch',text:'Die Hexe zwinkert: "Aber nur harmlose Zauber, mein Schatz. Ich habe da Regeln."',choices:[{label:'Seifenblasen-Zauber',a:'skA',p:'z1'},{label:'Tanz-Zauber',a:'skA',p:'z2'},{label:'Glitzerregen',a:'skA',p:'z3'},{label:'Doch nicht',a:'mclose'}]});
  return;
 }
 closeModal();
 if(skAct2(p)||skAct3(p)||skAct4(p)||skAct5(p)||skAct6(p)||skAct7(p)||skAct8(p)||skAct9(p)||skAct10(p)||skAct11(p)||skAct12(p)||skAct13(p)||skAct14(p)||skAct15(p)||skAct16(p)||skAct17(p)||skAct18(p)||skAct21(p)||skAct20(p)||skAct19(p))return;
 if(p==='knab'){
  const c=z&&z.candy?z.candy.filter(q=>q.on):[];
  if(!c.length){toast('Das Haus ist kahl gefuttert. Die Hexe schnippt, und alles ist wieder da.');if(z&&z.candy)z.candy.forEach(q=>{q.on=true;});mood(5,'+5');sfx('magic');return;}
  startSk('knab',1.3,'Du lehnst dich ans Lebkuchenhaus und beißt hinein ...');
 }else if(p==='lk'){
  if((G.lk||0)>=5){toast('Deine Taschen sind schon voller Lebkuchen.');return;}
  G.lk=(G.lk||0)+1;mood(1);sfx('coin');toast('Lebkuchen eingesteckt ('+G.lk+' / 5). Für später. Oder für einen Griesgram.');
 }else if(p==='tee'){
  if(z.tcd>0)return;z.tcd=25;
  mood(6,'+6 Kräutertee');sfx('glug');
  toast(pick(['Kräutertee aus der Hexenküche. Schmeckt nach Wiese, Honig und Geborgenheit.','Ihr sitzt am Kessel und plaudert. Die Hexe kennt erstaunlich gute Witze.']));
 }else if(p==='z1'){
  const h=skl().find(d=>d.k==='hexe')||P;
  for(let i=0;i<14;i++)FX.push({x:P.x+rf(-40,40),y:P.y+rf(-6,16),vx:rf(-14,14),vy:rf(-34,-12),g:-4,t:0,life:rf(2,3.4),dot:'rgba(170,225,255,.8)',r:rf(3,6)});
  mood(5,'+5 Seifenblasen');sfx('magic');toast('Seifenblasen überall! Eine schwebt dir direkt auf die Nase.');
 }else if(p==='z2'){
  peds.forEach(q=>{if(!q.snow&&q.st==='walk'&&Math.hypot(q.x-P.x,q.y-P.y)<260){q.st='dance';q.stT=7;}});
  skl().forEach(q=>{if(q.k==='zw')q.dn=7;});
  P.dance=Math.max(P.dance||0,6);
  mood(6,'+6 Tanzzauber');sfx('disco');toast('Alle Füße zucken. Der Tanz-Zauber erwischt jeden, auch dich!');
 }else if(p==='z3'){
  for(let i=0;i<24;i++)FX.push({x:P.x+rf(-60,60),y:P.y-rf(40,90),vx:rf(-8,8),vy:rf(30,70),g:20,t:0,life:rf(1.2,2),dot:pick(['#ffd23f','#ffe9a0','#fff','#ffb3f0']),r:rf(1.5,3)});
  mood(5,'+5 Glitzer');sfx('magic');toast('Glitzerregen! Alles funkelt, sogar deine Schuhe.');
 }else if(p==='kiss'){
  if(z.hcd>0)return;
  startSk('kiss',2.6,'Du packst ein Kissen und schüttelst es kräftig ...');
 }else if(p==='brot'){
  mood(4,'+4 Brot');sfx('crunch');toast('Das Brot ruft: "Zieh mich raus!" Du ziehst. Es ist warm und riecht nach Zuhause.');
 }else if(p==='pack'){
  if(z.pcd>0)return;
  startSk('pack',3.2,'Du faltest Papier, klebst Schleifen und stapelst Pakete ...');
 }else if(p==='wish'){
  mood(4,'+4 Wunschzettel');sfx('ok');toast('Dein Wunsch: "'+pick(WUNSCH)+'" Der Weihnachtsmann notiert es mit Kringel.');
 }else if(p==='wave'){
  const g=skl().find(d=>d.k==='gr');
  mood(2,'+2');sfx('clap');
  toast(g&&g.gf>0?'Er hebt zwei Finger. Ein Fortschritt!':pick(['Er brummt. Aber sein Mundwinkel zuckt einen Millimeter.','"Hmpf." Das war fast ein Hallo.']));
 }else if(p==='gift'){
  const g=skl().find(d=>d.k==='gr');if(!g||(G.lk||0)<1)return;
  G.lk--;g.gf++;sfx('coin');g.st='peek';g.t=3;
  if(g.gf>=3){
   const wm=skl().find(d=>d.k==='wm');
   g.st='go';g.tx=wm.x+30;g.ty=wm.y+10;
   toast('Der Griesgram verschlingt den dritten Lebkuchen und seufzt. Dann stapft er los, zur Werkstatt. "Ich mach das nur, weil ich muss."');
   mood(12,'+12 Griesgram taut auf');sfx('hoho');
  }else toast(g.gf===1?'Er schnüffelt am Lebkuchen. Er beißt ab. Er guckt, als hätte er nichts getan.':'Der zweite Lebkuchen verschwindet schneller. Er blinzelt verlegen.');
 }
}
function skBuildDone(b){
 const z=ZONE;
 if(b.k==='knab'){
  const c=z&&z.candy?z.candy.filter(q=>q.on):[];
  if(c.length){const q=pick(c);q.on=false;q.t=0;for(let i=0;i<8;i++)FX.push({x:q.x,y:q.y,vx:rf(-30,30),vy:rf(-40,-10),g:160,t:0,life:.6,dot:'#d9a35a',r:rf(1.5,2.6)});}
  mood(4,'+4 Knabbern');sfx('crunch');toast(pick(KNABL));
 }else if(b.k==='kiss'){
  z.hcd=20;z.wx='snow';z.wxT=32;
  const h=skl().find(d=>d.k==='holle');
  for(let i=0;i<30;i++)FX.push({x:P.x+rf(-70,70),y:P.y-rf(10,90),vx:rf(-15,15),vy:rf(20,60),g:10,t:0,life:rf(1.4,2.4),dot:i%3?'#fff':'#ffd23f',r:rf(1.6,3)});
  G.cash+=25;sfx('coin');mood(8,'+8 Goldregen');
  toast('Federn wirbeln, und dann: Goldregen! +25 €. Frau Holle strahlt. Auf der Welt schneit es jetzt.');
 }else if(b.k==='pack'){
  z.pcd=12;z.packs++;
  mood(8,'+8 Geschenke');sfx('pat');
  const g=skl().find(d=>d.k==='gr');
  if(z.packs%3===0){G.cash+=20;sfx('coin');toast('Der Weihnachtsmann steckt dir 20 € Taschengeld zu. Hinter dir raschelt es im Berg: Ein graues Mützchen verschwindet hinter einem Felsen.');}
  else toast(g&&g.st==='help'?'Der Griesgram packt mit. "Schleife schief", murmelt er, und bindet sie neu.':pick(['Ein Paket fertig. Der Weihnachtsmann nickt anerkennend.','Du faltest Papier wie ein Profi. Die Schleife sitzt sogar gerade.']));
 }
}
function skRewardHelp(g){
 G.cash+=50;sfx('coin');
 toast('Der Weihnachtsmann strahlt: "Endlich Verstärkung!" Er schiebt dir 50 € für die Vermittlung zu.');
}
function ext7Update(dt){
 if(!G)return;
 const z=ZONE;
 if(z){
  if(z.hcd>0)z.hcd-=dt;if(z.tcd>0)z.tcd-=dt;if(z.pcd>0)z.pcd-=dt;
  if(z.wxT>0){z.wxT-=dt;if(z.wxT<=0)z.wx=z.wx0||'none';}
  if(z.candy)z.candy.forEach(c=>{if(!c.on){c.t+=dt;if(c.t>28)c.on=true;}});
 }else{
  SKT-=dt;
  if(SKT<=0){SKT=rf(80,150);if(!SKC.length&&wanted===0&&!P.inCar){if(!(chance(.35)&&qEvent()))skEvent();}}
 }
 const L=skl();
 const zw=L.filter(d=>d.k==='zw');
 if(zw.length)zwStep(zw,dt);
 L.forEach(d=>{
  if(d.cd>0)d.cd-=dt;
  if(d.hop>0)d.hop-=dt;
  if(d.k==='mu'){
   if(d.play>0){d.play-=dt;d.walk+=dt*10;if(chance(dt*3))addFx(d.x+rf(-10,10),d.y-40,pick(['♪','♫']),'#ffe08a',1.4);}
   else steerStep(d,dt,30);
  }else if(d.k==='holle'){
   d.fe-=dt;
   if(d.fe<=0){d.fe=.35;if(Math.hypot(d.x-P.x,d.y-P.y)<420)FX.push({x:d.x+14,y:d.y-18,vx:rf(-14,14),vy:rf(8,26),g:2,t:0,life:rf(2,3.4),dot:'#fff',r:rf(1.4,2.4)});}
  }else if(d.k==='wm'){
   d.ho-=dt;
   if(d.ho<=0){d.ho=rf(8,14);if(Math.hypot(d.x-P.x,d.y-P.y)<260){addFx(d.x,d.y-44,'Ho ho ho!','#ffd23f',1.5);sfx('hoho');}}
  }else if(d.k==='gr'){
   const dd=Math.hypot(d.hx-P.x,d.hy-P.y);
   if(d.st==='hide'){if(dd<150&&d.cd<=0){d.st='peek';d.t=3;}}
   else if(d.st==='peek'){d.t-=dt;if(d.gf<1&&dd<54){d.st='duck';d.t=3;addFx(d.x,d.y-24,'Hmpf!','#cfd6e0',1.2);}else if(d.t<=0||dd>230){d.st='hide';d.cd=5;}}
   else if(d.st==='duck'){d.t-=dt;if(d.t<=0){d.st='hide';d.cd=4;}}
   else if(d.st==='go'){
    const dx=d.tx-d.x,dy=d.ty-d.y,L2=Math.hypot(dx,dy);d.a=Math.atan2(dy,dx);
    if(L2>3){d.x+=dx/L2*58*dt;d.y+=dy/L2*58*dt;d.walk+=dt*8;}
    else{d.st='help';d.a=0;if(!z.helped){z.helped=true;skRewardHelp(d);}}
   }
  }
 });
 if(!z&&SKC.length){
  const ld=SKC.find(d=>d.lead);
  if(ld){
   if(ld.life!==undefined){ld.life-=dt;}
   if(ld.life<=0&&(Math.hypot(ld.x-P.x,ld.y-P.y)>380||ld.life<-25))SKC.length=0;
  }else SKC.length=0;
 }
}
function drawCandy(c){
 ctx.fillStyle='rgba(0,0,0,.25)';circle(c.x+1,c.y+2,4.6);
 ctx.fillStyle=c.c;circle(c.x,c.y,4.4);
 ctx.fillStyle='rgba(255,255,255,.65)';circle(c.x-1.4,c.y-1.5,1.4);
}
function drawZwerg(d){
 const hp=d.hop>0?Math.abs(Math.sin(d.hop*10))*7:0,dn=d.dn>0;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+4,7,5,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(d.x,d.y-hp);ctx.rotate(dn?timeNow*6+d.i:d.a);
 const sw=Math.sin(d.walk)*2.6;
 ctx.fillStyle=d.jc;ctx.beginPath();ctx.ellipse(0,0,4.8,6.4,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e8c39e';circle(sw,-6.5,2);circle(-sw,6.5,2);
 ctx.fillStyle=d.bc;ctx.beginPath();ctx.ellipse(3.2,0,3.6,4.2,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e8c39e';circle(1,0,2.6);
 ctx.fillStyle=d.hc;circle(-1.2,0,4);
 ctx.beginPath();ctx.moveTo(-3,-3);ctx.lineTo(-3,3);ctx.lineTo(-12,sw*.6);ctx.closePath();ctx.fill();
 ctx.fillStyle='#fff';circle(-12,sw*.6,1.4);
 ctx.restore();
 if(Math.hypot(d.x-P.x,d.y-P.y)<110){ctx.fillStyle='#fff';ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(d.nm,d.x,d.y-18-hp);}
}
function drawHexe(d){
 const t=timeNow,x=d.x,y=d.y,kx=x+30,ky=y+6;
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x+2,y+3,11,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e8501a';
 for(let k=0;k<3;k++){ctx.beginPath();ctx.moveTo(kx-8+k*8,ky+12);ctx.lineTo(kx-5+k*8,ky+3-Math.sin(t*9+k)*2.5);ctx.lineTo(kx-2+k*8,ky+12);ctx.fill();}
 ctx.fillStyle='#2a2a2e';circle(kx,ky,10);ctx.fillStyle='#4fd18a';circle(kx,ky,7.5);
 ctx.fillStyle='#b9ffd8';for(let k=0;k<3;k++)circle(kx-4+k*4,ky-1+Math.sin(t*5+k*2)*2,1.5);
 ctx.fillStyle='rgba(255,255,255,.3)';circle(kx+Math.sin(t*2)*3,ky-13-((t*14)%10),3);
 ctx.fillStyle='#7a4ab3';ctx.beginPath();ctx.moveTo(x-10,y);ctx.lineTo(x+10,y);ctx.lineTo(x+5,y-15);ctx.lineTo(x-5,y-15);ctx.closePath();ctx.fill();
 ctx.fillStyle='#f4ead0';ctx.fillRect(x-4,y-13,8,12);
 ctx.strokeStyle='#5a3a2a';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x+5,y-11);ctx.lineTo(kx-3,ky-4+Math.sin(t*4)*2);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#e8c39e';circle(x,y-19,5);
 ctx.fillStyle='#d9d9e6';circle(x-4,y-17,2.4);circle(x+4,y-17,2.4);
 ctx.fillStyle='#e58aa8';circle(x-3,y-18,1.2);circle(x+3,y-18,1.2);
 ctx.fillStyle='#222';ctx.fillRect(x-2.6,y-21,1.4,1.6);ctx.fillRect(x+1.4,y-21,1.4,1.6);
 ctx.strokeStyle='#a03a3a';ctx.beginPath();ctx.arc(x,y-18.4,2,.2,2.9);ctx.stroke();
 ctx.fillStyle='#3a2060';ctx.beginPath();ctx.ellipse(x,y-24,9,2.6,0,0,6.283);ctx.fill();
 ctx.beginPath();ctx.moveTo(x-6,y-24);ctx.lineTo(x+6,y-24);ctx.lineTo(x+1,y-40);ctx.lineTo(x+4,y-42);ctx.lineTo(x-1,y-41);ctx.closePath();ctx.fill();
 ctx.fillStyle='#ffd23f';ctx.fillRect(x-5.4,y-27,10.8,2.4);
 ctx.fillStyle='#ff4d7a';ctx.font='bold 11px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('♥',x+10,y-36+Math.sin(t*3)*1.5);
}
function drawHolle(d){
 const t=timeNow,x=d.x,y=d.y;
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x+2,y+3,11,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#8fb5e0';ctx.beginPath();ctx.moveTo(x-10,y);ctx.lineTo(x+10,y);ctx.lineTo(x+5,y-15);ctx.lineTo(x-5,y-15);ctx.closePath();ctx.fill();
 ctx.fillStyle='#fff';ctx.fillRect(x-4,y-12,8,11);
 ctx.fillStyle='#e8c39e';circle(x,y-19,5);
 ctx.fillStyle='#f2f2f2';ctx.beginPath();ctx.arc(x,y-21,5.6,Math.PI,0);ctx.fill();circle(x,y-27,3.4);
 ctx.fillStyle='#222';ctx.fillRect(x-2.6,y-20,1.4,1.6);ctx.fillRect(x+1.4,y-20,1.4,1.6);
 ctx.strokeStyle='#a03a3a';ctx.beginPath();ctx.arc(x,y-17.6,2,.2,2.9);ctx.stroke();
 ctx.save();ctx.translate(x+13,y-14);ctx.rotate(Math.sin(t*7)*.5);
 ctx.fillStyle='#fff';ctx.fillRect(-9,-6,18,12);ctx.strokeStyle='#c9d4e4';ctx.strokeRect(-8.5,-5.5,17,11);ctx.fillStyle='#dfe8f4';ctx.fillRect(-5,-1,10,2);
 ctx.restore();
 ctx.strokeStyle='#8fb5e0';ctx.lineWidth=2.4;ctx.beginPath();ctx.moveTo(x+4,y-11);ctx.lineTo(x+11,y-14);ctx.stroke();ctx.lineWidth=1;
}
function drawWm(d){
 const x=d.x,y=d.y;
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x+2,y+3,12,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#8a5a34';circle(x+18,y-4,8);ctx.fillStyle='#6f4524';ctx.fillRect(x+15,y-14,6,3);
 ctx.fillStyle='#222';ctx.fillRect(x-7,y-3,6,4);ctx.fillRect(x+1,y-3,6,4);
 ctx.fillStyle='#c9302c';ctx.beginPath();ctx.moveTo(x-11,y-2);ctx.lineTo(x+11,y-2);ctx.lineTo(x+6,y-20);ctx.lineTo(x-6,y-20);ctx.closePath();ctx.fill();
 ctx.fillStyle='#f4f4f4';ctx.fillRect(x-11,y-4,22,3);ctx.fillRect(x-2,y-20,4,18);
 ctx.fillStyle='#222';ctx.fillRect(x-6,y-11,12,3);ctx.fillStyle='#ffd23f';ctx.fillRect(x-2,y-11.5,4,4);
 ctx.fillStyle='#e8c39e';circle(x,y-25,5);
 ctx.fillStyle='#f4f4f4';ctx.beginPath();ctx.arc(x,y-23,6.4,0,Math.PI);ctx.fill();circle(x-2,y-24,3);circle(x+2,y-24,3);
 ctx.fillStyle='#222';ctx.fillRect(x-2.6,y-27,1.4,1.6);ctx.fillRect(x+1.4,y-27,1.4,1.6);
 ctx.fillStyle='#e58a8a';circle(x,y-26,1.2);
 ctx.fillStyle='#c9302c';ctx.beginPath();ctx.moveTo(x-6,y-28);ctx.lineTo(x+6,y-28);ctx.lineTo(x+3,y-39);ctx.closePath();ctx.fill();
 ctx.fillStyle='#f4f4f4';ctx.fillRect(x-6.5,y-29,13,3);circle(x+3,y-39,2.6);
}
function drawGries(d){
 const x=d.hx,y=d.hy,t=timeNow;
 if(d.st==='help'||d.st==='go'){
  ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+3,9,4,0,0,6.283);ctx.fill();
  ctx.fillStyle='#6e7b8f';circle(d.x,d.y-6,8);
  ctx.fillStyle='#7a3b6b';ctx.fillRect(d.x-8,d.y-2,16,4);
  ctx.fillStyle='#6e7b8f';ctx.beginPath();ctx.moveTo(d.x-6,d.y-12);ctx.lineTo(d.x-3,d.y-17);ctx.lineTo(d.x,d.y-12);ctx.lineTo(d.x+3,d.y-17);ctx.lineTo(d.x+6,d.y-12);ctx.fill();
  ctx.fillStyle='#ffd23f';circle(d.x-3,d.y-7,1.8);circle(d.x+3,d.y-7,1.8);
  ctx.fillStyle='#222';ctx.fillRect(d.x-4.6,d.y-9.4,3.6,1.2);ctx.fillRect(d.x+1,d.y-9.4,3.6,1.2);
  ctx.fillStyle='#b27a6a';circle(d.x,d.y-4,2.6);
  ctx.fillStyle='rgba(255,120,140,.7)';circle(d.x-5.5,d.y-4,1.6);circle(d.x+5.5,d.y-4,1.6);
  if(d.st==='help'){ctx.fillStyle='#2e86c1';ctx.fillRect(d.x+8,d.y-1,9,8);ctx.fillStyle='#ffd23f';ctx.fillRect(d.x+11.5,d.y-1,2,8);}
  return;
 }
 ctx.fillStyle='rgba(8,8,16,.92)';ctx.beginPath();ctx.ellipse(x,y+2,15,12,0,Math.PI,0);ctx.lineTo(x+15,y+12);ctx.lineTo(x-15,y+12);ctx.closePath();ctx.fill();
 if(d.st==='hide'||d.st==='duck'){
  ctx.fillStyle='#ffd23f';circle(x-5,y+2,1.8);circle(x+5,y+2,1.8);
  ctx.fillStyle='#222';ctx.fillRect(x-7,y-.6,5,1.4);ctx.fillRect(x+2,y-.6,5,1.4);
  return;
 }
 const b=Math.sin(t*3)*1;
 ctx.fillStyle='#6e7b8f';circle(x,y+3+b,9);
 ctx.beginPath();ctx.moveTo(x-7,y-3+b);ctx.lineTo(x-4,y-9+b);ctx.lineTo(x-1,y-3+b);ctx.lineTo(x+2,y-9+b);ctx.lineTo(x+5,y-3+b);ctx.fill();
 ctx.fillStyle='#7a3b6b';ctx.fillRect(x-9,y+9+b,18,4);
 ctx.fillStyle='#ffd23f';circle(x-3.5,y+2+b,2);circle(x+3.5,y+2+b,2);
 ctx.fillStyle='#222';ctx.fillRect(x-6,y-1.4+b,4.4,1.4);ctx.fillRect(x+1.6,y-1.4+b,4.4,1.4);circle(x-3,y+2+b,.8);circle(x+3,y+2+b,.8);
 ctx.fillStyle='#b27a6a';circle(x,y+5+b,3);
 ctx.strokeStyle='#222';ctx.beginPath();ctx.arc(x,y+11+b,3,3.5,5.9);ctx.stroke();
 ctx.fillStyle='#8a929c';ctx.fillRect(x-12,y+10,5,3);ctx.fillRect(x+7,y+10,5,3);
}
function drawMusik(d){
 const t=timeNow,x=d.x,y=d.y,b=Math.sin(d.walk*.6)*1.2,pl=d.play>0?Math.sin(t*14)*2:0;
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x+2,y+4,14,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#8f949c';ctx.beginPath();ctx.ellipse(x,y-4+b,13,8,0,0,6.283);ctx.fill();
 ctx.fillRect(x-9,y+2+b,3,5);ctx.fillRect(x+6,y+2+b,3,5);
 ctx.beginPath();ctx.ellipse(x+11,y-8+b,5,4,0,0,6.283);ctx.fill();
 ctx.fillStyle='#8f949c';ctx.fillRect(x+9,y-18+b,2.4,8);ctx.fillRect(x+13,y-18+b,2.4,8);
 ctx.fillStyle='#caccd2';ctx.beginPath();ctx.ellipse(x+13,y-6+b,2.6,2,0,0,6.283);ctx.fill();
 ctx.fillStyle='#8a5a34';ctx.beginPath();ctx.ellipse(x,y-15+b+pl*.3,9,5.6,0,0,6.283);ctx.fill();
 circle(x+8,y-18+b,4);ctx.fillStyle='#5a3a1f';ctx.fillRect(x+9,y-23+b,3,5);
 ctx.fillStyle='#ff9a3c';ctx.beginPath();ctx.ellipse(x,y-23+b+pl*.5,7,4.6,0,0,6.283);ctx.fill();
 circle(x+5,y-26+b,3.6);ctx.beginPath();ctx.moveTo(x+3,y-28+b);ctx.lineTo(x+4,y-32+b);ctx.lineTo(x+6,y-28+b);ctx.fill();ctx.beginPath();ctx.moveTo(x+6,y-28+b);ctx.lineTo(x+8,y-32+b);ctx.lineTo(x+8,y-27+b);ctx.fill();
 ctx.fillStyle='#e5504d';ctx.beginPath();ctx.ellipse(x-1,y-30+b+pl,5.4,4.2,0,0,6.283);ctx.fill();
 ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.moveTo(x+3,y-31+b+pl);ctx.lineTo(x+7,y-30+b+pl);ctx.lineTo(x+3,y-29+b+pl);ctx.fill();
 ctx.fillStyle='#e5504d';circle(x-1,y-35+b+pl,2);circle(x+1,y-35.6+b+pl,1.8);circle(x-3,y-34.6+b+pl,1.6);
}
function drawSleigh(x,y){
 ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(x+4,y+14,44,9,0,0,6.283);ctx.fill();
 ctx.strokeStyle='#9aa0a8';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x-30,y+11);ctx.lineTo(x+28,y+11);ctx.quadraticCurveTo(x+38,y+11,x+35,y+2);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#b0302a';ctx.beginPath();ctx.moveTo(x-30,y-6);ctx.lineTo(x+26,y-6);ctx.quadraticCurveTo(x+35,y-4,x+30,y+9);ctx.lineTo(x-26,y+9);ctx.closePath();ctx.fill();
 ctx.fillStyle='#ffd23f';ctx.fillRect(x-28,y-6,54,3);
 [[-24,-17,12,11,'#2e86c1'],[-9,-22,15,16,'#27ae60'],[8,-16,12,10,'#f1c40f'],[-18,-27,10,10,'#d35bb5'],[14,-24,9,8,'#ff9a3c']].forEach(q=>{ctx.fillStyle=q[4];ctx.fillRect(x+q[0],y+q[1],q[2],q[3]);ctx.fillStyle='rgba(255,255,255,.85)';ctx.fillRect(x+q[0]+q[2]/2-1,y+q[1],2,q[3]);ctx.fillRect(x+q[0],y+q[1]+q[3]/2-1,q[2],2);});
 const rb=Math.sin(timeNow*2)*1;
 [60,92].forEach(o=>{
  ctx.strokeStyle='#5a3a1f';ctx.beginPath();ctx.moveTo(x+30,y);ctx.lineTo(x+o,y-2);ctx.stroke();
  ctx.fillStyle='#8a5a34';ctx.beginPath();ctx.ellipse(x+o+10,y-3+rb,13,6,0,0,6.283);ctx.fill();
  ctx.fillRect(x+o+1,y+2,3,8);ctx.fillRect(x+o+16,y+2,3,8);
  circle(x+o+24,y-7+rb,5);
  ctx.strokeStyle='#5a3a1f';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(x+o+23,y-11+rb);ctx.lineTo(x+o+21,y-19+rb);ctx.moveTo(x+o+23,y-15+rb);ctx.lineTo(x+o+27,y-18+rb);ctx.moveTo(x+o+26,y-11+rb);ctx.lineTo(x+o+28,y-19+rb);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#222';circle(x+o+26,y-8+rb,1);
 });
}
function drawSketch(cx,cy){
 if(!ZONE)medDraw(cx,cy);
 const iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 if(ZONE){
  if(ZONE.candy)ZONE.candy.forEach(c=>{if(c.on&&iv(c.x,c.y,10))drawCandy(c);});
  if(ZONE.name==='maerchen'&&iv(19*TS,11*TS,60))drawTisch();
  if(ZONE.name==='maerchen'&&iv(23*TS,26*TS,520))drawAcker();
  if(ZONE.name==='berge'&&iv(12.5*TS,18*TS,120))drawSleigh(12.5*TS,18.3*TS);
  if(ZONE.name==='bayern')drawBayernDeko(cx,cy);
  if(ZONE.name==='portugal')drawRails(cx,cy);
  if(ZONE.name==='wuppertal')drawGirder(cx,cy);
  if(ZONE.name==='sender'){drawSender(cx,cy);drawSender2(cx,cy);}
  if(ZONE.name==='amt')drawAmt(cx,cy);
  if(ZONE.name==='fpark')drawFpark(cx,cy);
  if(ZONE.name==='maerchen')drawMaerchen2(cx,cy);
  if(ZONE.name==='gallien'||ZONE.name==='zoo')drawZG(cx,cy);
  kDraw(cx,cy);medZDraw(cx,cy);
 }else{drawCityExtra(cx,cy);drawFireWorld(cx,cy);}
 hideDraw(cx,cy);drawAnimals(cx,cy);immoDraw(cx,cy);bepDraw(cx,cy);
 skl().forEach(d=>{
  if(!iv(d.x,d.y,60))return;
  if(d.k==='flocke')drawFlocke(d);
  else if(FAIRY[d.k])drawFairy(d);
  else if(d.k==='zw')drawZwerg(d);
  else if(d.k==='hexe')drawHexe(d);
  else if(d.k==='holle')drawHolle(d);
  else if(d.k==='wm')drawWm(d);
  else if(d.k==='gr')drawGries(d);
  else if(d.k==='mu'){if(d.v==='blas')drawBlas(d);else if(d.v==='jeck')drawJeck(d);else drawMusik(d);}
  else if(d.k==='kap')drawKap(d);
  else if(d.k==='wolf')drawWolf(d);
  else if(d.k==='hase')drawHase(d);
  else if(d.k==='ig')drawIgel(d);
  else if(d.k==='huhn')drawHuhn(d);
  else if(d.k==='kuh')drawKuh(d);
  else if(d.k==='tram')drawTram(d);
  else if(d.k==='schweb')drawSchweb(d);
  else if(d.k==='tuffi')drawTuffi(d);
  else if(d.k==='koebes')drawKoebes(d);
  else if(d.k==='jodl')drawJodler(d);
  else if(d.k==='bauer')drawBauer(d);
  else if(d.k==='mod')drawMod(d);
  else if(d.k==='prak')drawPrak(d);
  else if(d.k==='gurke')drawGurke(d);
  else if(d.k==='rep')drawRep(d);
  else if(d.k==='hero')drawHero(d);
  else if(d.k==='beamt')drawBeamt(d);
  else if(d.k==='forma')drawForma(d);
  else if(d.k==='ordn')drawOrdn(d);
  else if(XNPC[d.k])xnDraw(d);
  else if(PSK[d.k])plantDraw(d);
  else if(QSK[d.k])qDraw(d);
  else if(YK[d.k])ykDraw(d);
  else if(d.k==='zgn')drawGnom(d);
  else if(d.k==='falter')drawFalter(d);
  else if(d.k==='fado')drawFado(d);
 });
}

const GESCHENKE=['Ein Gutschein für einen Mittagsschlaf. Einlösbar jederzeit.','Ein Paar Socken mit eingebautem Rückenwind.','Eine Tafel Schokolade, die nie ganz alle wird.','Ein Buch, das sich selbst vorliest.','Ein Regenschirm, der nur über dir regnet, wenn du es willst.','Ein Kuschelkissen mit Gute-Laune-Garantie.','Ein Kuchenstück, noch warm. Obwohl es im Karton war.','Ein Jahresabo für Sonnenuntergänge.'];
function tischMenu(){
 const z=ZONE,f=z&&z.feast>0;
 mdl('Tischlein deck dich','Ein schlichter Holztisch mitten im Wald. Auf einem Schildchen steht: "Sag es einfach laut."',[
  ['Tischlein, deck dich!','tdeck',f],['Geschenke auspacken ('+(z&&z.gifts>0?z.gifts:0)+')','tgift',!(f&&z.gifts>0)]]);
}
function kapMenu(){
 mdl('Rotkäppchen','"Ich bringe der Großmutter Kuchen. Aber da hinten im Gebüsch sitzt ein Wolf, der immer so unschuldig pfeift."',[
  ['Kuchen probieren','kuchen'],['Wolf im Auge behalten','warn']]);
}
function wolfMenu(){
 const w=skl().find(d=>d.k==='wolf');
 if(w&&w.zz>0){toast('Der Wolf schläft tief. Zzz ... Kuchen ... zzz ...');return;}
 const n=G.lk||0;
 showModal({title:'Der Wolf',text:'Der Wolf pfeift unschuldig und guckt in den Himmel. "Ich? Ich wollte doch nur ein Stück Kuchen. Hab seit Tagen nichts gehabt. Außer Kuchen."',choices:[{label:'Lebkuchen anbieten ('+n+')',a:'skA',p:'wlk',off:n<1},{label:'Hinterm Ohr kraulen',a:'skA',p:'wkr'},{label:'Weitergehen',a:'mclose'}]});
}
function skAct2(p){
 const z=ZONE;
 if(p==='tdeck'){
  if(z.feast>0)return true;
  z.feast=30;z.gifts=3;
  sfx('magic');mood(8,'+8 Festmahl');
  skl().forEach(q=>{if(q.k==='zw')q.dn=6;});
  const w=skl().find(d=>d.k==='wolf');if(w){w.zz=Math.max(w.zz||0,20);w.st='sleep';}
  toast('"Tischlein, deck dich!" Und wirklich: Kuchen, Brot, Saft und drei Geschenke. Sogar der Wolf kommt friedlich satt ins Nickerchen.');
  return true;
 }
 if(p==='tgift'){
  if(!(z.feast>0&&z.gifts>0))return true;
  z.gifts--;sfx('coin');mood(6,'+6 Geschenk');
  if(chance(.5)){G.cash+=10;}
  toast('Du packst aus: '+pick(GESCHENKE));
  return true;
 }
 if(p==='kuchen'){mood(4,'+4 Kuchen');sfx('crunch');toast('Rotkäppchens Kuchen: Mürbeteig, Kirschen, Liebe. Du bekommst ein halbes Stück und ein Lächeln.');return true;}
 if(p==='warn'){
  const w=skl().find(d=>d.k==='wolf');if(w&&w.st==='sneak'){w.st='lurk';w.t=18;}
  mood(2,'+2');sfx('clap');toast('Du schaust dem Gebüsch streng in die Augen. Es raschelt verlegen.');return true;
 }
 if(p==='wlk'){
  const w=skl().find(d=>d.k==='wolf'),k=skl().find(d=>d.k==='kap');
  if(!w||(G.lk||0)<1)return true;
  G.lk--;w.zz=45;w.st='sleep';G.cash+=15;
  mood(9,'+9 Wolf besänftigt');sfx('coin');
  toast('Der Wolf verschlingt den Lebkuchen, seufzt und rollt sich zusammen. Rotkäppchen steckt dir 15 € Finderlohn zu. Zzz ...');
  return true;
 }
 if(p==='wkr'){
  const w=skl().find(d=>d.k==='wolf');if(w)w.hop=.9;
  mood(4,'+4 Wolf kraulen');sfx('aww');toast(pick(['Der Wolf wedelt wie ein großer Hund. Er würde das niemals zugeben.','Sein Hinterbein zuckt. Das ist wohl die Lieblingsstelle.']));
  return true;
 }
 return false;
}
function leash(d,hx,hy,r){
 if(Math.hypot(d.x-hx,d.y-hy)>r){d.a=Math.atan2(hy-d.y,hx-d.x);d.steer=2;}
}
function ext8Update(dt){
 if(!G||!ZONE||ZONE.name!=='maerchen')return;
 const z=ZONE,L=skl();
 if(z.feast>0){
  z.feast-=dt;
  if(z.feast<=0)z.gifts=0;
  if(chance(dt*7))FX.push({x:19*TS+16+rf(-22,22),y:11*TS+rf(-6,14),vx:rf(-8,8),vy:rf(-30,-10),g:0,t:0,life:1.2,dot:pick(['#ffd23f','#fff','#ffb3f0']),r:rf(1.4,2.6)});
 }
 const k=L.find(d=>d.k==='kap'),w=L.find(d=>d.k==='wolf');
 if(k){
  if(k.pause>0)k.pause-=dt;
  else{leash(k,16*TS,15*TS,260);steerStep(k,dt,24);}
 }
 if(w&&k){
  if(w.zz>0){w.zz-=dt;w.st='sleep';if(chance(dt*.8))addFx(w.x+6,w.y-16,'Z','#cfd6e0',1.6);if(w.zz<=0){w.st='lurk';w.t=rf(16,28);addFx(w.x,w.y-20,'Gähn ... Kuchen?','#cfd6e0',1.6);}return;}
  const dk=Math.hypot(k.x-w.x,k.y-w.y);
  if(w.st==='lurk'){
   leash(w,14*TS,18*TS,300);steerStep(w,dt,22);
   w.t-=dt;if(w.t<=0)w.st='sneak';
  }else if(w.st==='sneak'){
   const dp=Math.hypot(P.x-w.x,P.y-w.y);
   if(dp<46){w.st='lurk';w.t=rf(14,22);addFx(w.x,w.y-20,'Ich tu nix!','#ffe08a',1.4);return;}
   w.a=Math.atan2(k.y-w.y,k.x-w.x);
   if(dk>18){const nx=w.x+Math.cos(w.a)*40*dt,ny=w.y+Math.sin(w.a)*40*dt;if(skOk(nx,ny)){w.x=nx;w.y=ny;w.walk+=dt*8;}else if(skOk(nx,w.y))w.x=nx;else if(skOk(w.x,ny))w.y=ny;}
   else{
    w.st='run';w.t=5;k.pause=2.5;sfx('pfft');
    addFx(w.x,w.y-22,'Nasch!','#ffd23f',1.3);addFx(k.x,k.y-30,'Hey, mein Kuchen!','#ff9a9a',1.8);
    if(Math.hypot(P.x-k.x,P.y-k.y)<420)toast('Der Wolf klaut Rotkäppchen ein Stück Kuchen und flitzt davon. Niemand wird gefressen, nur genascht.');
   }
  }else if(w.st==='run'){
   w.t-=dt;w.a=Math.atan2(w.y-k.y,w.x-k.x);
   const nx=w.x+Math.cos(w.a)*70*dt,ny=w.y+Math.sin(w.a)*70*dt;
   if(skOk(nx,ny)){w.x=nx;w.y=ny;w.walk+=dt*12;}else w.a+=1.5;
   if(w.t<=0){w.st='lurk';w.t=rf(18,30);}
  }
 }
}
function drawKap(d){
 const x=d.x,y=d.y;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+2,y+3,9,4,0,0,6.283);ctx.fill();
 ctx.fillStyle='#d8352f';ctx.beginPath();ctx.moveTo(x-9,y);ctx.lineTo(x+9,y);ctx.lineTo(x+5,y-14);ctx.lineTo(x-5,y-14);ctx.closePath();ctx.fill();
 ctx.fillStyle='#f4ead0';ctx.fillRect(x-3,y-13,6,5);
 ctx.fillStyle='#e8c39e';circle(x,y-18,4.6);
 ctx.fillStyle='#d8352f';ctx.beginPath();ctx.arc(x,y-19,6,Math.PI,0);ctx.fill();ctx.fillRect(x-6,y-19,12,3);
 ctx.fillStyle='#222';ctx.fillRect(x-2.4,y-18,1.4,1.6);ctx.fillRect(x+1,y-18,1.4,1.6);
 ctx.strokeStyle='#a03a3a';ctx.beginPath();ctx.arc(x,y-16,1.8,.2,2.9);ctx.stroke();
 ctx.fillStyle='#9a6a3a';ctx.fillRect(x+7,y-8,10,8);ctx.fillStyle='#fff';ctx.fillRect(x+8,y-10,8,3);ctx.fillStyle='#e5504d';ctx.fillRect(x+9,y-10,2,3);ctx.fillRect(x+13,y-10,2,3);
 ctx.strokeStyle='#7a5a2a';ctx.beginPath();ctx.arc(x+12,y-8,5,Math.PI,0);ctx.stroke();
}
function drawWolf(w){
 const t=timeNow,x=w.x,y=w.y,sl=w.st==='sleep',hp=w.hop>0?Math.abs(Math.sin(w.hop*10))*5:0;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+2,y+4,13,5,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y-hp);
 const fl=Math.cos(w.a)<0?-1:1;ctx.scale(fl,1);
 const lg=sl?0:Math.sin(w.walk)*2.4;
 ctx.fillStyle='#6a6c73';ctx.fillRect(-9,sl?0:-1,3,sl?3:7+lg);ctx.fillRect(5,sl?0:-1,3,sl?3:7-lg);
 ctx.strokeStyle='#7d7f86';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(-12,-5);ctx.quadraticCurveTo(-20,sl?-2:-12+Math.sin(t*6)*3,-18,sl?4:-16);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#7d7f86';ctx.beginPath();ctx.ellipse(0,-5,13,sl?6:7.4,0,0,6.283);ctx.fill();
 ctx.fillStyle='#c9ccd2';ctx.beginPath();ctx.ellipse(-1,-2,8,3.2,0,0,6.283);ctx.fill();
 const hx=sl?10:12,hy=sl?-2:-11;
 ctx.fillStyle='#7d7f86';circle(hx,hy,6);
 ctx.beginPath();ctx.moveTo(hx-5,hy-3);ctx.lineTo(hx-3,hy-11);ctx.lineTo(hx,hy-4);ctx.fill();ctx.beginPath();ctx.moveTo(hx+1,hy-4);ctx.lineTo(hx+4,hy-11);ctx.lineTo(hx+6,hy-3);ctx.fill();
 ctx.fillStyle='#c9ccd2';ctx.beginPath();ctx.ellipse(hx+6,hy+2,5,3.2,0,0,6.283);ctx.fill();
 ctx.fillStyle='#222';circle(hx+10,hy+1,1.4);
 if(sl){ctx.strokeStyle='#222';ctx.beginPath();ctx.moveTo(hx+1,hy-1);ctx.lineTo(hx+4,hy-1);ctx.stroke();}
 else{ctx.fillStyle='#ffd23f';circle(hx+2,hy-2,1.6);ctx.fillStyle='#222';circle(hx+3,hy-2,.8);}
 ctx.restore();
}
function drawTisch(){
 const z=ZONE,x=19*TS+16,y=11*TS+20,f=z.feast>0;
 ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(x+3,y+14,32,8,0,0,6.283);ctx.fill();
 ctx.fillStyle='#6f4524';ctx.fillRect(x-24,y,5,14);ctx.fillRect(x+19,y,5,14);
 ctx.fillStyle=f?'#fff':'#8a5a34';ctx.fillRect(x-28,y-8,56,12);
 if(f){ctx.fillStyle='#e5504d';for(let i=0;i<7;i++)ctx.fillRect(x-28+i*8,y-8,4,12);ctx.fillStyle='rgba(255,255,255,.85)';for(let i=0;i<7;i++)ctx.fillRect(x-24+i*8,y-8,4,12);}
 else{ctx.fillStyle='#a8723f';ctx.fillRect(x-28,y-8,56,3);}
 if(f){
  ctx.fillStyle='#d9a35a';ctx.beginPath();ctx.ellipse(x-18,y-12,8,5,0,0,6.283);ctx.fill();ctx.fillStyle='#b07a3a';ctx.fillRect(x-24,y-14,3,2);
  ctx.fillStyle='#f4ead0';ctx.fillRect(x-8,y-17,13,9);ctx.fillStyle='#e5504d';ctx.fillRect(x-8,y-17,13,3);ctx.fillStyle='#ffd23f';ctx.fillRect(x-2,y-22,2,5);
  ctx.fillStyle='#ff9a3c';ctx.beginPath();ctx.moveTo(x+10,y-8);ctx.lineTo(x+8,y-20);ctx.lineTo(x+18,y-20);ctx.lineTo(x+16,y-8);ctx.fill();
  if(z.gifts>0)[[x+22,'#2e86c1'],[x+24,'#27ae60'],[x+20,'#d35bb5']].slice(0,z.gifts).forEach((q,i)=>{ctx.fillStyle=q[1];ctx.fillRect(q[0]-5,y-18-i*9,12,9);ctx.fillStyle='rgba(255,255,255,.85)';ctx.fillRect(q[0]+0,y-18-i*9,2,9);ctx.fillRect(q[0]-5,y-14-i*9,12,2);});
 }
}

function hasenMenu(){
 const h=skl().find(d=>d.k==='hase');
 if(!h)return;
 if(h.st!=='idle'){toast(h.st==='tired'?'Der Hase hechelt: "Noch eine Runde ... morgen. Vielleicht."':'Das Rennen läuft! Nicht blinzeln.');return;}
 mdl('Hase und Igel','Der Hase lacht: "Ich bin der Schnellste im ganzen Wald! Wer wettet gegen mich?" Der Igel zuckt nur kurz mit den Stacheln.',[['Einfach zuschauen','hr0'],['Auf den Hasen wetten (2 €)','hrh',G.cash<2],['Auf den Igel wetten (2 €)','hri',G.cash<2]]);
}
function puddingMenu(){
 mdl('Puddingberg','Ein Berg aus Vanillepudding, dick mit Karamell überzogen, oben thront eine Kirsche. Er wackelt leise vor sich hin.',[['Löffeln, bis es nicht mehr geht','pl'],['Auf dem Pudding hüpfen','ph'],['Schokosoße drübergießen','ps']]);
}
function huhnFang(d){
 if(d.cd>0){toast('Das Hähnchen ist gerade außer Reichweite.');return;}
 d.cd=8;
 if(chance(.55)){mood(6,'+6 Hähnchen');sfx('crunch');toast(pick(['Knusprig, saftig, mitten im Flug gefangen. Du bedankst dich beim Hähnchen. Es winkt mit dem Flügel.','Ein Hähnchen fliegt dir direkt in die Hände. So macht Abendessen Spaß.']));}
 else{addFx(d.x,d.y-30,'Flatter!','#ffe08a',1.2);d.a+=3.14;d.steer=2;toast('Entwischt! Das Hähnchen flattert lachend davon.');}
}
function hasenStart(bet){
 const h=skl().find(d=>d.k==='hase');if(!h||h.st!=='idle')return;
 if(bet){G.cash-=2;sfx('coin');}
 h.bet=bet;h.st='run';h.dir=1;h.round=0;h.x=13*TS+16;
 toast(bet==='hase'?'Du wettest auf den Hasen. Mutig.':bet==='igel'?'Du wettest auf den Igel. Klug.':'Auf die Plätze, fertig, los!');
 sfx('arrive');
}
function skAct3(p){
 if(p==='hr0'){hasenStart(null);return true;}
 if(p==='hrh'){hasenStart('hase');return true;}
 if(p==='hri'){hasenStart('igel');return true;}
 if(p==='pl'){mood(4,'+4 Pudding');sfx('glug');toast(pick(['Löffel für Löffel. Der Berg schrumpft nicht, er lächelt nur.','Vanille, Karamell, Kirschensaft: Du bist im Himmel mit Löffel.']));return true;}
 if(p==='ph'){mood(6,'+6 Hüpfen');sfx('bonk');shake=.3;addFx(P.x,P.y-20,'Wackel!','#ffd23f',1.2);toast('Boing! Der Pudding federt dich zurück in die Luft. Du landest wackelnd, aber glücklich.');return true;}
 if(p==='ps'){mood(3,'+3 Schoko');sfx('pat');toast('Schokosoße läuft den Berg hinab. Der Berg freut sich sichtlich.');return true;}
 return false;
}
function ext9Update(dt){
 if(!G||!ZONE)return;
 const z=ZONE,L=skl();
 if(z.name==='maerchen'){
  const h=L.find(d=>d.k==='hase');
  if(!h)return;
  const x0=13*TS+16,x1=33*TS+16,i1=L.find(d=>d.k==='ig'&&d.e===0),i2=L.find(d=>d.k==='ig'&&d.e===1);
  [i1,i2].forEach(i=>{if(i&&i.show>0)i.show-=dt;});
  if(h.st==='run'){
   h.x+=h.dir*175*dt;h.walk+=dt*16;
   if((h.dir>0&&h.x>=x1-26)||(h.dir<0&&h.x<=x0+26)){
    h.st='pop';h.t=1.7;h.round++;
    const ig=h.dir>0?i2:i1;ig.show=1.7;
    addFx(ig.x,ig.y-34,'Ich bin schon da!','#ffe08a',1.7);sfx('honk');
   }
  }else if(h.st==='pop'){
   h.t-=dt;
   if(h.t<=0){
    if(h.round>=3){
     h.st='tired';h.t=16;i1.show=16;i2.show=16;
     addFx(h.x,h.y-26,'Hechel ...','#cfd6e0',2);sfx('aww');mood(8,'+8 Wettlauf');
     if(h.bet==='igel'){G.cash+=5;sfx('coin');toast('Der Igel gewinnt, wie immer. Deine Wette zahlt 5 €. Er und seine Frau klatschen sich ab.');}
     else if(h.bet==='hase')toast('Der Hase verliert, wie immer. Deine 2 € sind weg, dafür war es herrlich. Er liegt japsend im Acker.');
     else toast('Der Igel und seine Frau klatschen sich ab. Der Hase liegt japsend im Acker. Müde, aber unversehrt.');
     h.bet=null;
    }else{h.dir=-h.dir;h.st='run';}
   }
  }else if(h.st==='tired'){
   h.t-=dt;if(chance(dt*.8))addFx(h.x,h.y-22,'*hechel*','#cfd6e0',1.4);
   if(h.t<=0){h.st='idle';h.x=x0;h.dir=1;h.round=0;}
  }
 }else if(z.name==='schlaraff'){
  L.forEach(d=>{
   if(d.k!=='huhn')return;
   if(d.cd>0)d.cd-=dt;
   d.steer-=dt;if(d.steer<=0){d.a+=rf(-1,1);d.steer=rf(1.5,3.5);}
   if(Math.hypot(d.x-24*TS,d.y-15*TS)>520){d.a=Math.atan2(15*TS-d.y,24*TS-d.x);d.steer=2;}
   d.x=clamp(d.x+Math.cos(d.a)*42*dt,3*TS,(ZW-3)*TS);d.y=clamp(d.y+Math.sin(d.a)*42*dt,3*TS,(ZH-3)*TS);d.walk+=dt*12;
  });
 }
}
function drawAcker(){
 const x=11*TS,y=25*TS,w=24*TS,h=3*TS;
 ctx.fillStyle='#8b6b47';ctx.fillRect(x,y,w,h);
 ctx.strokeStyle='#6d5236';ctx.lineWidth=2;
 for(let i=0;i<12;i++){ctx.beginPath();ctx.moveTo(x,y+4+i*8);ctx.lineTo(x+w,y+4+i*8);ctx.stroke();}
 ctx.lineWidth=1;
 ctx.fillStyle='#6fae56';for(let i=0;i<9;i++){circle(x+30+i*70,y+h-8,5);}
 ctx.fillStyle='#fff';ctx.fillRect(x+4,y-6,3,h+6);ctx.fillRect(x+w-7,y-6,3,h+6);
 ctx.fillStyle='#e5504d';ctx.fillRect(x+4,y-6,10,5);ctx.fillRect(x+w-7,y-6,10,5);
}
function drawHase(h){
 const x=h.x,y=h.y,sl=h.st==='tired',run=h.st==='run',hp=run?Math.abs(Math.sin(h.walk))*5:0,f=h.dir||1;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+2,y+3,13,4,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y-hp);ctx.scale(f,1);
 ctx.fillStyle='#a58f78';
 if(sl){ctx.beginPath();ctx.ellipse(0,-5,12,5.4,0,0,6.283);ctx.fill();circle(11,-6,5);ctx.beginPath();ctx.ellipse(8,-10,2.4,7,-1.2,0,6.283);ctx.fill();ctx.fillStyle='#ff7f9a';ctx.beginPath();ctx.ellipse(15,-4,2,3.6,0,0,6.283);ctx.fill();}
 else{
  ctx.beginPath();ctx.ellipse(-1,-8,10,6.4,0,0,6.283);ctx.fill();
  const lg=run?Math.sin(h.walk*1.2)*4:0;
  ctx.fillRect(-9+lg,-3,7,3);ctx.fillRect(4-lg,-3,5,3);
  circle(9,-13,5);
  ctx.beginPath();ctx.ellipse(6,-23,2.4,8,-.3,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(10,-23,2.4,8,.2,0,6.283);ctx.fill();
  ctx.fillStyle='#f6c7d0';ctx.beginPath();ctx.ellipse(6,-23,1,5,-.3,0,6.283);ctx.fill();
 }
 ctx.fillStyle='#fff';circle(-11,sl?-6:-9,3);
 ctx.fillStyle='#222';circle(sl?13:12,sl?-7:-14,1.1);
 ctx.restore();
}
function drawIgel(i){
 if(i.show<=0)return;
 const rise=Math.min(1,(i.show>1e3?1:Math.min(1.7-Math.max(0,1.7-i.show),i.show))*6);
 const x=i.x,y=i.y;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+2,y+2,10,4,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y-10*Math.min(1,rise));
 ctx.fillStyle='#6a4a2a';
 for(let k=0;k<11;k++){const a=Math.PI+k/10*Math.PI;ctx.beginPath();ctx.moveTo(Math.cos(a)*7,Math.sin(a)*7);ctx.lineTo(Math.cos(a)*13,Math.sin(a)*13);ctx.lineTo(Math.cos(a+.25)*7,Math.sin(a+.25)*7);ctx.fill();}
 ctx.fillStyle='#8a6a42';ctx.beginPath();ctx.ellipse(0,0,10,8,0,Math.PI,0);ctx.fill();
 ctx.fillStyle='#e8c39e';ctx.beginPath();ctx.ellipse(0,1,8,6,0,0,Math.PI);ctx.fill();ctx.fillRect(-8,-1,16,2);
 ctx.fillStyle='#222';circle(-3,0,1.1);circle(3,0,1.1);circle(0,2.6,1.3);
 ctx.strokeStyle='#222';ctx.beginPath();ctx.arc(0,3.6,2,.3,2.8);ctx.stroke();
 ctx.restore();
}
function drawHuhn(d){
 const t=timeNow,x=d.x,y=d.y,b=Math.sin(t*3+d.x*.01)*3,fl=Math.cos(d.a)<0?-1:1,w=Math.sin(d.walk)*6;
 ctx.fillStyle='rgba(0,0,0,.22)';ctx.beginPath();ctx.ellipse(x+3,y+6,9,3.4,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y-18+b);ctx.scale(fl,1);
 ctx.fillStyle='#e0a050';ctx.beginPath();ctx.moveTo(-2,-2);ctx.lineTo(-10,-10-w);ctx.lineTo(4,-3);ctx.fill();ctx.beginPath();ctx.moveTo(-2,2);ctx.lineTo(-10,10+w);ctx.lineTo(4,3);ctx.fill();
 ctx.fillStyle='#c9772f';ctx.beginPath();ctx.ellipse(0,0,10,6.6,0,0,6.283);ctx.fill();
 ctx.fillStyle='#e29a4a';ctx.beginPath();ctx.ellipse(-1,-2,6,2.6,0,0,6.283);ctx.fill();
 ctx.fillStyle='#c9772f';circle(10,-3,4.2);ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.moveTo(13,-4);ctx.lineTo(18,-2.6);ctx.lineTo(13,-1.6);ctx.fill();
 ctx.fillStyle='#222';circle(10,-4.4,1);
 ctx.fillStyle='#e5504d';ctx.fillRect(8,-8,4,2.4);
 ctx.fillStyle='#8a5a34';ctx.fillRect(-4,5.4,2.6,5);ctx.fillRect(2,5.4,2.6,5);
 ctx.restore();
}

const EURO={
 city:{n:'Rheinhanfen',x:58,y:34,warp:'Du reist zurück nach Rheinhanfen. Alles beim Alten, nur du bist besser drauf.'},
 amsterdam:{n:'Amsterdam',x:54,y:12,warp:'Du steigst in den Zug nach Westen. Grachten, Fahrräder, Tulpen: Willkommen in Amsterdam!'},
 wuppertal:{n:'Wuppertal',x:78,y:20,warp:'Der Zug rattert ins Bergische Land. Es geht bergauf, bergab und manchmal sogar in der Luft: Wuppertal!'},
 bayern:{n:'Bayern',x:88,y:39,warp:'Der Zug rollt nach Süden. Die Berge werden höher, die Hosen kürzer. Servus, Bayern!'},
 portugal:{n:'Portugal',x:13,y:68,warp:'Dein Flugzeug landet in Lissabon. Es riecht nach Meer, Zimt und Pastel de Nata. Olá, Portugal!'},
 amt:{n:'Amt für Alles',x:30,y:40,warp:'Du ziehst eine Nummer und fährst ab. Vor dir liegt das Amt für Alles: Hier ist jede Tür die falsche, und das mit Absicht.'},
 helden:{n:'Heldenplatz',x:44,y:50,warp:'Du landest auf dem Heldenplatz. Hier tragen alle Umhänge, Bademäntel und sehr große Pantoffeln.'},
 sender:{n:'Senderviertel',x:78,y:56,warp:'Du fährst ins Senderviertel. Hier stehen vier riesige Pappkulissen und eine Wurfbude. Zeit, Dampf abzulassen!'},
 feldweg:{n:'Feldweg',x:45,y:22,warp:'Du läufst aus der Stadt hinaus, durch den Garten, auf den Feldweg. Es duftet nach Hopfen, Heu und Sommer.'},
 koeln:{n:'Köln',x:66,y:45,warp:'Der Zug rollt den Rhein entlang. Draußen: Dom, Brücken und überall jemand, der Alaaf ruft. Willkommen in Köln!'},
 oesterreich:{n:'Österreich',x:108,y:51,warp:'Der Zug fährt über die Grenze. Du merkst es nicht, es gibt hier keine. Plötzlich Berge, Kaffeehäuser und Walzermusik: Österreich!'},
 fpark:{n:'Freizeitpark',x:112,y:27,warp:'Der Bus hält direkt vor dem bunten Tor. Es duftet nach Zuckerwatte, die Achterbahn rattert schon: Willkommen im Freizeitpark!'},
 malle:{n:'Mallorca (Ballermann)',x:47,y:66,warp:'Der Ferienflieger landet in Palma. Sonne, Strand, Schlager: Willkommen am Ballermann!'},
 holly:{n:'Hollyhanf (USA)',x:14,y:29,warp:'Zwölf Stunden Flug, zwei Filme, ein Hotdog. Willkommen in Hollyhanf!'},
 camping:{n:'Camping (NL)',x:20,y:14,warp:'Der Bus rollt nach Holland, vorbei an Windmühlen und Kühen. Endstation: Camping Tulpenwiese. Hoi!'},
 gallien:{n:'Gallierdorf',x:22,y:52,warp:'Die Kutsche rumpelt über eine alte Römerstraße. Rundhütten, Rauch aus dem Kessel und nebenan ein Römerlager: Willkommen im Gallierdorf!'}
};
const eup=(p,f)=>'<polygon points="'+p+'" fill="'+f+'" stroke="#2d4a2a" stroke-width=".5" stroke-linejoin="round"/>';
const eut=(x,y,s)=>'<text x="'+x+'" y="'+y+'" font-size="3" fill="rgba(255,255,255,.55)" text-anchor="middle" font-family="Arial">'+s+'</text>';
const EUSVG='<svg viewBox="0 0 160 100" style="position:absolute;left:0;top:0;width:100%;height:100%"><rect width="160" height="100" fill="#1d4a6b"/>'+
 '<path d="M0 20Q10 17 20 20T40 20T60 20M100 80Q110 77 120 80T140 80T160 80M0 92Q10 89 20 92T40 92" stroke="rgba(255,255,255,.12)" stroke-width=".6" fill="none"/>'+
 eup('28,6 36,4 40,12 36,22 28,24 24,16','#6f9a55')+
 eup('6,52 22,48 36,52 40,62 34,74 24,86 12,88 6,80 4,66','#a6b85e')+
 eup('4,56 12,54 16,62 15,78 10,84 5,76 3,64','#e0c85e')+
 eup('22,48 28,34 44,28 56,32 66,38 64,52 54,64 40,62 36,52','#7aa65a')+
 eup('48,8 60,6 64,12 62,24 52,28 46,20','#e09a4a')+
 eup('52,28 62,24 64,12 74,10 84,14 90,24 94,34 90,44 80,50 66,48 60,40 56,34','#8cba66')+
 eup('76,36 94,34 100,44 90,50 78,46','#cfd98a')+
 eup('90,46 100,42 120,44 128,50 114,54 98,54','#c98a6a')+
 eup('80,54 96,56 100,70 110,84 102,90 94,80 88,66 80,60','#9aa85a')+
 eut(40,44,'FRANKREICH')+eut(78,22,'DEUTSCHLAND')+eut(24,70,'SPANIEN')+eut(92,70,'ITALIEN')+eut(32,15,'UK')+
 '</svg>';
function mkKuh(x,y){const f=freeSpot(x,y);return{k:'kuh',x:f.x,y:f.y,a:rf(0,6.28),walk:0,steer:rf(1,3),cd:0,mu:0,pause:0};}
function kuhStreichel(d){
 if(d.cd>0){toast('Die Kuh kaut gerade. Wiederkäuen ist harte Arbeit.');return;}
 d.cd=9;d.mu=1.4;mood(3,'+3 Muh');sfx('muh');
 addFx(d.x,d.y-34,'Muuuh!','#ffffff',1.6);
 toast(pick(['Die Kuh schaut dich tief an. Du hast das Gefühl, sie versteht dich besser als manche Menschen.','Muh. Das heißt in Kuh: Schön, dass du da bist. Oder: Mehr Gras bitte.','Du streichelst die Kuh. Ihre Glocke bimmelt zufrieden. Das ist Wellness.']));
}
function fadoHoeren(d){
 if(d.cd>0){toast('Die Fado-Sängerin macht eine Pause und seufzt wunderschön.');return;}
 d.cd=16;mood(5,'+5 Saudade');sfx('musik');
 ['♪','♫','♪'].forEach((s,i)=>addFx(d.x+(i-1)*12,d.y-40-i*4,s,'#ffe08a',2));
 peds.forEach(p=>{if(!p.snow&&p.st==='walk'&&Math.hypot(p.x-d.x,p.y-d.y)<200){p.st='dance';p.stT=5;}});
 toast(pick(['Fado: ein Lied über das süße Heimweh nach etwas, das man nie hatte. Du bekommst eine Gänsehaut. Eine schöne.','Die Sängerin singt von Meer, Sehnsucht und Sardinen. Alle schwanken im Takt mit.','Saudade nennt man das: wehmütig, warm und irgendwie tröstlich. Du bist sehr zufrieden mit der Welt.']));
}
function tramFahrt(d){
 if(fade)return;
 if(d.cd>0){toast('Die Bahn macht gerade Pause. Ding-Ding kommt gleich.');return;}
 const x0=10*TS,x1=44*TS,to=P.x<(x0+x1)/2?x1:x0;
 d.cd=10;sfx('ding');
 startFade('Ding-Ding! Die gelbe Straßenbahn ruckelt über die Hügel, bimmelt um jede Ecke und setzt dich am anderen Ende ab.',()=>{
  P.x=to+(to===x1?-48:48);P.y=16*TS+16;P.vx=P.vy=0;
  d.x=to;d.st='wait';d.t=3;d.dir=to===x1?-1:1;
  mood(3,'+3 Tram');cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
 });
}
function burgMenu(){
 mdl('Märchenschloss','Der Schlossherr winkt vom Balkon: "Willkommen! Das Schloss ist ein bisschen zu groß, ein bisschen zu weiß und ein bisschen zu schön für jeden vernünftigen Zweck. Genau deshalb steht es hier."',[['Zum Balkon hochwinken','bw'],['Schlossführung mitmachen','bf',!!(ZONE&&ZONE.bcd>0)]]);
}
const BFL=['Hier der Saal der tausend Kerzen. Neunhundertneunundneunzig davon sind aus Versehen Zimmerpflanzen.','Und hier die Schatzkammer. Sie enthält den größten Schatz des Landes: eine funktionierende Heizung.','Links sehen Sie die Wendeltreppe. Sie ist so lang, dass man oben schon wieder müde unten ankommt.','Dieser Raum ist dem Schlossgespenst vorbehalten. Es kommt nur dienstags und ist sehr höflich.'];
function skAct4(p){
 if(p==='bw'){mood(4,'+4 Winken');sfx('clap');addFx(P.x,P.y-24,'Servus!','#ffd23f',1.5);toast('Der Schlossherr winkt mit dem Taschentuch zurück. Dann wirft er dir eine Kusshand zu. Dann ein Brezn. Das war nett.');return true;}
 if(p==='bf'){if(ZONE)ZONE.bcd=25;mood(6,'+6 Führung');sfx('magic');toast(pick(BFL));return true;}
 return false;
}
function drawKuh(d){
 const t=timeNow,x=d.x,y=d.y,fl=Math.cos(d.a)<0?-1:1,w=Math.sin(d.walk)*2,b=d.mu>0?Math.sin(t*12)*1.2:0;
 ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(x+2,y+4,17,5,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y+b);ctx.scale(fl,1);
 ctx.fillStyle='#e9e5dc';ctx.fillRect(-10,-8,3,9+w*.4);ctx.fillRect(-3,-8,3,9-w*.4);ctx.fillRect(4,-8,3,9+w*.4);ctx.fillRect(10,-8,3,9-w*.4);
 ctx.fillStyle='#f6f3ec';ctx.beginPath();ctx.ellipse(0,-15,15,8.6,0,0,6.283);ctx.fill();
 ctx.fillStyle='#33302c';ctx.beginPath();ctx.ellipse(-5,-17,5,3.6,.3,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(6,-12,4,3,0,0,6.283);ctx.fill();
 ctx.fillStyle='#f3b6b6';ctx.beginPath();ctx.ellipse(-4,-7,3.6,2.4,0,0,6.283);ctx.fill();
 ctx.strokeStyle='#d8d2c4';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(-15,-17);ctx.lineTo(-19,-9+w*.4);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#f6f3ec';ctx.beginPath();ctx.ellipse(16,-17,6.4,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#f3b6b6';ctx.beginPath();ctx.ellipse(20.5,-15.5,3.4,2.8,0,0,6.283);ctx.fill();
 ctx.fillStyle='#33302c';ctx.beginPath();ctx.ellipse(13,-22,2.6,1.6,-.5,0,6.283);ctx.fill();circle(15.4,-19,1);
 ctx.strokeStyle='#e8d9a0';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(15,-22);ctx.lineTo(14,-27);ctx.moveTo(18,-22);ctx.lineTo(19,-27);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#ffd23f';circle(11,-9,2.4);
 ctx.restore();
}
function drawBlas(d){
 const t=timeNow,pl=d.play>0;
 [[-16,'#2f6a3a'],[0,'#c0392b'],[16,'#2e6fb5']].forEach((q,i)=>{
  const bx=d.x+q[0],by=d.y+(pl?Math.sin(t*10+i)*1.6:0);
  drawPerson(bx,by,d.a+i*.3,q[1],'ped',d.walk+i);
  ctx.fillStyle='#d8a62b';ctx.beginPath();ctx.arc(bx+Math.cos(d.a+i*.3)*7,by+Math.sin(d.a+i*.3)*7-4,i===1?5.6:4,0,6.283);ctx.fill();
  ctx.fillStyle='#8a6a1b';ctx.beginPath();ctx.arc(bx+Math.cos(d.a+i*.3)*7,by+Math.sin(d.a+i*.3)*7-4,i===1?2.6:1.8,0,6.283);ctx.fill();
  ctx.fillStyle='#2f6a3a';ctx.fillRect(bx-4,by-14,8,3);ctx.fillStyle='#e5504d';ctx.fillRect(bx+2,by-18,2,5);
 });
}
function drawTram(d){
 const x=d.x,y=d.y,f=d.dir||1,mv=d.st==='go'?Math.sin(timeNow*20)*.8:0;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.fillRect(x-48,y,98,6);
 ctx.save();ctx.translate(x,y+mv);ctx.scale(f,1);
 ctx.strokeStyle='#555';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(-14,-30);ctx.lineTo(-6,-40);ctx.lineTo(8,-40);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#e0ae10';ctx.fillRect(-48,-30,96,28);
 ctx.fillStyle='#f4c81d';ctx.fillRect(-47,-29,94,12);
 ctx.fillStyle='#fff';ctx.fillRect(-48,-19,96,3);
 ctx.fillStyle='#9fd8ef';for(let i=0;i<6;i++)ctx.fillRect(-42+i*15,-27,10,9);
 ctx.fillStyle='#6a4a1a';ctx.fillRect(34,-27,10,22);ctx.fillStyle='#9fd8ef';ctx.fillRect(35,-26,8,10);
 ctx.fillStyle='#3a3a3a';circle(-34,-2,5);circle(-10,-2,5);circle(14,-2,5);circle(36,-2,5);
 ctx.fillStyle='#fff7c0';circle(47,-10,2.4);
 ctx.restore();
}
function drawFado(d){
 const x=d.x,y=d.y;
 drawPerson(x,y,1.57,'#26262e','ped',0);
 ctx.fillStyle='#26262e';ctx.beginPath();ctx.ellipse(x,y+2,9,6,0,0,6.283);ctx.fill();
 ctx.fillStyle='#c9a24a';ctx.beginPath();ctx.ellipse(x+8,y+4,5.4,7,.5,0,6.283);ctx.fill();
 ctx.strokeStyle='#6a4a1a';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x+10,y);ctx.lineTo(x+16,y-9);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#3a2a12';circle(x+8,y+4,1.6);
 ctx.fillStyle='#e5504d';ctx.fillRect(x-3,y-3,6,2);
}
function drawBayernDeko(cx,cy){
 [[17,18],[22,18],[27,18]].forEach(q=>{
  const x=q[0]*TS,y=q[1]*TS;
  if(x<cx-80||x>cx+VW+80||y<cy-80||y>cy+VH+80)return;
  drawBench(ctx,x-4,y-12);
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(x-1,y+5,38,12);
  ctx.fillStyle='#8a6339';ctx.fillRect(x-3,y,40,14);
  for(let i=0;i<9;i++)for(let j=0;j<3;j++){ctx.fillStyle=(i+j)%2?'#fff':'#4a86d8';ctx.fillRect(x-1+i*4,y+1+j*4,4,4);}
  ctx.fillStyle='#e8b64a';ctx.fillRect(x+6,y+2,5,7);ctx.fillRect(x+20,y+3,5,7);
  ctx.fillStyle='#fff';ctx.fillRect(x+6,y+2,5,2);ctx.fillRect(x+20,y+3,5,2);
  drawBench(ctx,x-4,y+8);
 });
}
function drawRails(cx,cy){
 const y=14*TS+26;
 if(y<cy-20||y>cy+VH+20)return;
 const xa=Math.max(9*TS,cx-40),xb=Math.min(45*TS,cx+VW+40);
 ctx.fillStyle='#6a5a48';for(let x=Math.floor(xa/12)*12;x<xb;x+=12)ctx.fillRect(x,y-3,4,12);
 ctx.fillStyle='#9a9fa8';ctx.fillRect(xa,y-1,xb-xa,2);ctx.fillRect(xa,y+5,xb-xa,2);
}
function ext10Update(dt){
 if(!G||!ZONE)return;
 const z=ZONE,L=skl();
 if(z.bcd>0)z.bcd-=dt;
 if(z.name==='bayern'||z.name==='oesterreich'){
  L.forEach(d=>{
   if(d.k==='kuh'){
    if(d.mu>0)d.mu-=dt;
    if(d.pause>0){d.pause-=dt;return;}
    d.steer-=dt;if(d.steer<=0){d.a+=rf(-1.2,1.2);d.steer=rf(2,5);if(chance(.4))d.pause=rf(2,5);}
    leash(d,d.hx||9*TS,d.hy||17*TS,300);
    const nx=d.x+Math.cos(d.a)*14*dt,ny=d.y+Math.sin(d.a)*14*dt;
    if(skOk(nx,ny)){d.x=nx;d.y=ny;d.walk+=dt*6;}else{d.a+=rf(1.5,3);d.steer=1;}
   }else if(d.k==='mu'&&d.v==='blas'&&!(d.play>0))leash(d,22*TS,18*TS,260);
  });
 }else if(z.name==='portugal'){
  L.forEach(d=>{
   if(d.k==='tram'){
    const x0=10*TS,x1=44*TS;
    if(d.st==='wait'){d.t-=dt;if(d.t<=0)d.st='go';}
    else{
     d.x+=d.dir*64*dt;
     if(d.x>=x1){d.x=x1;d.dir=-1;d.st='wait';d.t=4;sfx('ding');}
     else if(d.x<=x0){d.x=x0;d.dir=1;d.st='wait';d.t=4;sfx('ding');}
    }
   }else if(d.k==='fado'){
    if(chance(dt*.25)&&Math.hypot(d.x-P.x,d.y-P.y)<300)addFx(d.x,d.y-36,pick(['♪','♫']),'#ffe08a',1.8);
   }
  });
 }
}

const wcy=x=>15+Math.round(Math.sin(x*.3)*1.2);
function schwebFahrt(d){
 if(fade)return;
 if(d.cd>0){toast('Die Schwebebahn ist gerade unterwegs. Sie kommt gleich wieder, sie schwebt ja nur.');return;}
 const x0=5*TS,x1=43*TS,to=P.x<(x0+x1)/2?x1:x0,tx=Math.floor(to/TS);
 d.cd=10;sfx('ding');
 startFade('Die Schwebebahn quietscht los und schwebt hoch über der Wupper. Unten glitzert der Fluss, oben hängt der Himmel. Bergisch schön!',()=>{
  P.x=to+(to===x1?-40:40);P.y=(wcy(tx)-2)*TS+16;P.vx=P.vy=0;
  d.x=to;d.st='wait';d.t=3;d.dir=to===x1?-1:1;
  mood(4,'+4 Schwebebahn');cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
  if(chance(.4)&&ZONE&&!ZONE.ska.some(q=>q.k==='tuffi'))tuffiSpringt();
 });
}
function tuffiSpringt(){
 const z=ZONE;if(!z)return;
 const x=clamp(P.x+rf(-120,120),4*TS,43*TS);
 z.ska.push({k:'tuffi',x:x,y:wcy(Math.floor(x/TS))*TS+16,dir:chance(.5)?1:-1,life:28,walk:0,cd:0});
 sfx('glug');mood(8,'+8 Tuffi');
 for(let i=0;i<8;i++)addFx(x+rf(-24,24),wcy(Math.floor(x/TS))*TS-6,pick(['~','°','*']),'#bfe9ff',1.6,rf(-30,-10));
 addFx(x,wcy(Math.floor(x/TS))*TS-30,'PLATSCH!','#ffffff',1.8);
 toast('Wie 1950: Zirkuselefant Tuffi hüpft aus der Schwebebahn in die Wupper! Ihr geht es prima. Sie planscht und winkt mit dem Rüssel.');
}
function tuffiRuessel(d){
 if(d.cd>0){toast('Tuffi holt gerade Wasser im Rüssel. Gleich gibt es eine Dusche.');return;}
 d.cd=7;mood(5,'+5 Rüssel-Dusche');sfx('glug');
 for(let i=0;i<6;i++)addFx(d.x+rf(-18,18),d.y-30-i*4,'°','#bfe9ff',1.4,rf(-40,-10));
 toast(pick(['Tuffi duscht dich mit einem Rüsselstrahl. Du bist nass und strahlend glücklich.','Der Elefant trötet fröhlich. In Wuppertal ist das ein ganz normaler Dienstag.']));
}
function braumeisterMenu(){
 const z=ZONE;
 mdl('Braumeister','Der Braumeister wischt die Hände an der Schürze ab: "Willkommen im Brauhaus! Bei uns braut sich das Bier fast von selbst. Ich passe nur auf, dass es dabei nicht singt."',[['Im Kupferkessel rühren','bmr'],['Fass anstechen (Fest!)','bmf',!!(z&&z.fcd>0)]]);
}
function skAct5(p){
 if(p==='bmr'){mood(4,'+4 Rühren');sfx('glug');addFx(P.x,P.y-24,'Blubb!','#ffd23f',1.4);toast(pick(['Du rührst im Kupferkessel. Es riecht nach warmem Brot und ein bisschen nach Urlaub.','Rühr, rühr, rühr. Der Sud blubbert zufrieden. Der Braumeister nickt anerkennend.']));return true;}
 if(p==='bmf'){
  const z=ZONE;if(z)z.fcd=40;
  sfx('musik');mood(7,'+7 Fassanstich');
  ['Glück auf!','Prost!','Hurra!'].forEach((s,i)=>addFx(P.x+(i-1)*22,P.y-32-i*4,s,'#ffe08a',1.8));
  peds.forEach(q=>{if(!q.snow&&q.st==='walk'&&Math.hypot(q.x-P.x,q.y-P.y)<240){q.st='dance';q.stT=6;}});
  toast('Der Braumeister schlägt den Zapfhahn ein. Alle jubeln, tanzen und stoßen mit Kirschsaft, Wasser und gutem Gewissen an. Es spritzt nur Schaum.');
  return true;
 }
 return false;
}
function drawGirder(cx,cy){
 const xa=Math.max(5,Math.floor(cx/TS)-1),xb=Math.min(43,Math.ceil((cx+VW)/TS)+1);
 if(xb<xa)return;
 ctx.strokeStyle='#8a929c';
 for(let x=xa;x<=xb;x++){
  const y=wcy(x)*TS+16-34,y2=wcy(x+1)*TS+16-34,px=x*TS+16,px2=(x+1)*TS+16;
  ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(px,y);ctx.lineTo(px2,y2);ctx.stroke();
  ctx.beginPath();ctx.moveTo(px,y+7);ctx.lineTo(px2,y2+7);ctx.stroke();
  ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(px,y);ctx.lineTo(px+16,y2+7);ctx.lineTo(px2,y2);ctx.stroke();
  if(x%6===0){
   const yb=wcy(x)*TS+16;
   ctx.lineWidth=4;ctx.strokeStyle='#6f7882';
   ctx.beginPath();ctx.moveTo(px-1,y+7);ctx.lineTo(px-14,yb+30);ctx.moveTo(px+1,y+7);ctx.lineTo(px+14,yb+30);ctx.stroke();
   ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(px-8,yb);ctx.lineTo(px+8,yb);ctx.stroke();
   ctx.strokeStyle='#8a929c';
  }
 }
 ctx.lineWidth=1;
}
function drawSchweb(d){
 const x=d.x,y=wcy(Math.floor(d.x/TS))*TS+16,f=d.dir||1,mv=d.st==='go'?Math.sin(timeNow*9)*.8:0;
 ctx.save();ctx.translate(x,y+mv);ctx.scale(f,1);
 ctx.fillStyle='rgba(0,0,0,.18)';ctx.fillRect(-46,14,92,6);
 ctx.fillStyle='#555e68';ctx.fillRect(-30,-30,5,8);ctx.fillRect(25,-30,5,8);
 ctx.fillStyle='#2f6fc4';ctx.beginPath();ctx.moveTo(-48,-6);ctx.lineTo(-48,-20);ctx.quadraticCurveTo(-46,-24,-40,-24);ctx.lineTo(40,-24);ctx.quadraticCurveTo(50,-24,50,-14);ctx.lineTo(50,-6);ctx.closePath();ctx.fill();
 ctx.fillStyle='#f4f6f8';ctx.fillRect(-48,-15,98,5);
 ctx.fillStyle='#9fd8ef';for(let i=0;i<6;i++)ctx.fillRect(-42+i*14,-22,10,7);
 ctx.fillRect(42,-22,6,8);
 ctx.fillStyle='#fff7c0';circle(49,-12,2.2);
 ctx.fillStyle='#3a4048';ctx.fillRect(-46,-6,94,3);
 ctx.restore();
}
function drawTuffi(d){
 const t=timeNow,x=d.x,y=d.y,f=d.dir||1,b=Math.sin(t*3)*1.5;
 ctx.fillStyle='rgba(255,255,255,.35)';ctx.beginPath();ctx.ellipse(x,y+6,24,6,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y+b);ctx.scale(f,1);
 ctx.fillStyle='#a9aeb8';ctx.beginPath();ctx.ellipse(0,-6,17,9,0,0,6.283);ctx.fill();
 circle(15,-12,8);
 ctx.fillStyle='#8f95a0';ctx.beginPath();ctx.ellipse(11,-10,7,9,.2,0,6.283);ctx.fill();
 ctx.strokeStyle='#a9aeb8';ctx.lineWidth=5;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(21,-10);ctx.quadraticCurveTo(28,-8,27,-20+Math.sin(t*5)*3);ctx.stroke();ctx.lineWidth=1;ctx.lineCap='butt';
 ctx.fillStyle='#222';circle(18,-14,1.2);
 ctx.fillStyle='rgba(120,190,255,.6)';ctx.fillRect(-18,-1,36,4);
 ctx.restore();
}
function ext11Update(dt){
 if(!G||!ZONE||ZONE.name!=='wuppertal')return;
 const z=ZONE,L=skl();
 if(z.fcd>0)z.fcd-=dt;
 for(let i=L.length-1;i>=0;i--){
  const d=L[i];
  if(d.k==='schweb'){
   const x0=5*TS,x1=43*TS;
   if(d.st==='wait'){d.t-=dt;if(d.t<=0)d.st='go';}
   else{
    d.x+=d.dir*58*dt;
    if(d.x>=x1){d.x=x1;d.dir=-1;d.st='wait';d.t=5;sfx('ding');}
    else if(d.x<=x0){d.x=x0;d.dir=1;d.st='wait';d.t=5;sfx('ding');}
   }
   d.y=wcy(Math.floor(d.x/TS))*TS+16;
  }else if(d.k==='tuffi'){
   d.life-=dt;d.walk+=dt;
   d.x+=d.dir*20*dt;if(d.x>43*TS)d.dir=-1;if(d.x<5*TS)d.dir=1;
   d.y=wcy(Math.floor(d.x/TS))*TS+16;
   if(chance(dt*.7))addFx(d.x+rf(-10,10),d.y-24,pick(['Törööö!','°','Plansch!']),'#cfe9ff',1.4);
   if(d.life<=0)L.splice(i,1);
  }
 }
}

const KBL=['Köbes: "Nä, Alt? Dat jibt et hier nich. Hier trinkt man Kölsch, Jung!"','Köbes: "Wat willste? Setz dich hin und jenieß, bevor ich et mir anders überlege."','Köbes: "Kölsch hammer. Alles andere is Gemüse."','Köbes: "Mir is egal, wer du bist. Du kriss trotzdem keen Alt."'];
function koebesAnsprechen(d){
 if(d.cd>0){toast('Der Köbes hat zu tun. Er ignoriert dich mit voller Hingabe.');return;}
 d.cd=18;mood(5,'+5 Köbes');sfx('honk');
 addFx(d.x,d.y-34,'Nä!','#ffe08a',1.4);
 const kid=minorNear(P.x,P.y,90);
 if(kid)toast(pick(KBL)+' Er stellt dir stattdessen einen Apfelsaft hin.');
 else if(chance(.5)&&G.stock.bier<40){G.stock.bier++;toast(pick(KBL)+' Er knallt dir ungefragt ein Kölsch hin. Wer zuerst winkt, hat verloren.');}
 else toast(pick(KBL));
}
function jodlerHoeren(d){
 if(d.cd>0){toast('Der Jodler holt tief Luft. Die Berge warten geduldig.');return;}
 d.cd=14;mood(6,'+6 Jodeln');sfx('musik');
 ['Holla-di-ri-ö!','ö ö ö','ö ...'].forEach((s,i)=>addFx(d.x+14+i*34,d.y-40-i*8,s,'#ffe08a',2.2));
 peds.forEach(p=>{if(!p.snow&&p.st==='walk'&&Math.hypot(p.x-d.x,p.y-d.y)<240){p.st='dance';p.stT=5;}});
 toast(pick(['Der Jodler jodelt, das Echo jodelt zurück, und dann jodelt die Kuh im Hintergrund auch noch mit. Mehrstimmig!','Du jodelst mit. Es klingt furchtbar, aber die Berge klatschen trotzdem.']));
}
function walzerMenu(){
 mdl('Ballsaal','Ein Saal voller Kronleuchter. Ein Herr im Frack verbeugt sich: "Darf ich bitten? Eins, zwei, drei, eins, zwei, drei."',[['Walzer tanzen','wz'],['Walzer-Gymnastik mitmachen','mm:walzer:0'],['Kronleuchter bewundern','wk']]);
}
function skAct6(p){
 if(p==='wz'){
  closeAll();sfx('disco');P.dance=5;mood(8,'+8 Walzer');
  for(let i=0;i<6;i++)addFx(P.x+rf(-30,30),P.y+rf(-26,8),pick(['♪','♫']),pick(['#ffd23f','#ffffff','#ffb3f0']),1.8,-30);
  peds.forEach(q=>{if(!q.snow&&q.st==='walk'&&Math.hypot(q.x-P.x,q.y-P.y)<220){q.st='dance';q.stT=5;}});
  toast('Eins, zwei, drei! Du walzerst durch den Saal, und der Kronleuchter dreht sich vor Neid.');
  return true;
 }
 if(p==='wk'){mood(3,'+3 Glanz');sfx('magic');toast(pick(['Der Kronleuchter hat dreitausend Kristalle. Zweitausendneunhundert davon sind Eiswürfel. Ganz sicher.','Du schaust hoch. Der Kronleuchter funkelt zurück.']));return true;}
 return false;
}
function drawJodler(d){
 const x=d.x,y=d.y;
 drawPerson(x,y,0,'#2f6a3a','ped',0);
 ctx.fillStyle='#e5504d';ctx.fillRect(x-3,y-14,6,3);ctx.fillStyle='#2f6a3a';ctx.fillRect(x-5,y-12,10,2);
 ctx.strokeStyle='#8a5a2a';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x+4,y-2);ctx.lineTo(x+40,y-16);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#6a3e1a';ctx.beginPath();ctx.arc(x+41,y-17,5,0,6.283);ctx.fill();
}
function drawKoebes(d){
 const x=d.x,y=d.y,a=d.a;
 drawPerson(x,y,a,'#2a4f9a','ped',d.walk);
 ctx.fillStyle='#d8d8de';ctx.beginPath();ctx.ellipse(x+Math.cos(a)*8,y+Math.sin(a)*8-6,8,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#f1c96a';for(let i=-1;i<=1;i++)ctx.fillRect(x+Math.cos(a)*8+i*4-1.5,y+Math.sin(a)*8-13,3,7);
 ctx.fillStyle='#fff';for(let i=-1;i<=1;i++)ctx.fillRect(x+Math.cos(a)*8+i*4-1.5,y+Math.sin(a)*8-13,3,2);
}
function drawJeck(d){
 const t=timeNow,pl=d.play>0;
 [[-16,'#e5504d','#ffd23f'],[0,'#7a3fc4','#5ff0ff'],[16,'#27ae60','#ff5fd0']].forEach((q,i)=>{
  const bx=d.x+q[0],by=d.y+(pl?Math.sin(t*10+i)*1.8:0);
  drawPerson(bx,by,d.a+i*.3,q[1],'ped',d.walk+i);
  ctx.fillStyle=q[2];ctx.beginPath();ctx.moveTo(bx-5,by-12);ctx.lineTo(bx,by-26);ctx.lineTo(bx+5,by-12);ctx.closePath();ctx.fill();
  ctx.fillStyle='#fff';circle(bx,by-26,1.8);
 });
 if(pl&&chance(.4))FX.push({x:d.x+rf(-30,30),y:d.y-30,vx:rf(-20,20),vy:rf(-10,20),g:20,t:0,life:1.4,dot:pick(['#ff5fd0','#ffd23f','#5ff0ff','#6bcf63']),r:2});
}
function ext12Update(dt){
 if(!G||!ZONE)return;
 const z=ZONE,L=skl();
 if(z.name==='koeln'){
  L.forEach(d=>{
   if(d.k==='koebes'){leash(d,19*TS,16*TS,230);steerStep(d,dt,26);}
   else if(d.k==='mu'&&d.v==='jeck'&&!(d.play>0))leash(d,30*TS,17*TS,240);
  });
 }
}

const MMS={
 walzer:{t:'Walzer-Gymnastik',s:['Eins, zwei, drei: Verlagere dein Gewicht im Walzertakt von einem Fuß auf den anderen. Acht Mal.','Halte die Arme, als hättest du einen Tanzpartner, und kreise sie langsam. Acht Mal.','Dreh dich einmal langsam um dich selbst, erst rechts herum, dann links herum.']},
 jodeln:{t:'Jodel-Training',s:['Atme tief in den Bauch ein und lang und ruhig wieder aus. Drei Mal.','Heb die Arme wie ein Alphorn nach vorn und strecke dich lang. Zwei Mal.','Ruf laut oder leise: Holla-di-ri-ö! Mit Echo, wenn du magst.']},
 schunkeln:{t:'Schunkel-Runde',s:['Wiege dich links und rechts, mit Nachbarn untergehakt oder ganz allein. Sechzehn Mal.','Marschiere auf der Stelle. Zwanzig Schritte, Knie schön hoch.','Hände hoch, klatschen und laut Alaaf oder Servus rufen!']},
 ernte:{t:'Ernte-Gymnastik',s:['Bücke dich und richte dich wieder auf, wie beim Pflücken. Zehn Mal, ganz gemütlich.','Strecke dich nach oben zu den Hopfenranken. Fünf Mal.','Trag einen unsichtbaren Korb ein paar Schritte und schüttel danach die Arme locker aus.']},
 amt:{t:'Warte-Gymnastik',s:['Setz dich aufrecht hin und kreise die Schultern langsam: acht Mal nach vorn, acht Mal zurück.','Strecke die Beine aus, wippe mit den Füßen und dehne den Nacken, einmal zur rechten und einmal zur linken Schulter.','Steh auf, strecke dich zur Decke und lass die Arme ganz langsam locker fallen. Zwei Mal, mit einem Seufzer.']},
 held:{t:'Heldenpose',s:['Stell dich breitbeinig hin, die Hände in die Hüften, die Brust raus. Fünf Atemzüge lang.','Strecke einen Arm schräg nach oben, als würdest du losfliegen, und halte die Pose zehn Sekunden. Dann wechsle den Arm.','Wirf dir einen imaginären Umhang über, drehe dich einmal um dich selbst und lächle stolz.']},
 atem:{t:'Durchatmen',s:['Atme langsam durch die Nase ein und zähle dabei bis vier.','Halte kurz inne, zähle bis zwei und lass die Schultern sinken.','Atme langsam durch den Mund aus und zähle bis sechs. Wiederhole das zwei Mal.']}
};
function mmStart(k,i){
 const m=MMS[k];if(!m)return;
 if(i>=m.s.length){mmDone();return;}
 showModal({title:m.t+' ('+(i+1)+'/'+m.s.length+')',text:(i===0?'Freiwillig und nur so viel, wie dir gut tut. Du kannst jederzeit aufhören. ':'')+m.s[i],choices:[{label:'Geschafft!',a:'skA',p:'mm:'+k+':'+(i+1)},{label:'Aufhören',a:'mclose'}]});
}
function mmDone(){
 closeAll();G.mm=(G.mm||0)+1;
 mood(10,'+10 Mitgemacht');sfx('magic');
 ['Super!','Bravo!','Geschafft!'].forEach((s,i)=>addFx(P.x+(i-1)*26,P.y-30-i*5,s,'#ffd23f',2));
 peds.forEach(q=>{if(!q.snow&&q.st==='walk'&&Math.hypot(q.x-P.x,q.y-P.y)<220){q.st='dance';q.stT=5;}});
 toast(pick(['Das hast du toll gemacht! Alle in der Nähe klatschen und machen gleich mit.','Bewegung, Spaß und gute Laune: ein Dreiklang, der immer funktioniert.','Geschafft! Du fühlst dich leichter, und die Leute ringsum sind beeindruckt.'])+(G.mm===10?' Zehn Mal mitgemacht: Du bist jetzt Mitmach-Meister!':''));
}
function jodlerMenu(){
 mdl('Jodler','Der Jodler stützt das Alphorn ab: "Jodeln ist wie Singen, nur mit mehr Berg. Machst du mit?"',[['Zuhören','jh'],['Jodel-Training mitmachen','mm:jodeln:0']]);
}
function schunkelMenu(d){
 mdl(d.v==='jeck'?'Die Jecken':'Die Blaskapelle',d.v==='jeck'?'Die Jecken haken sich unter: "Komm, schunkel mit! Hier ist keiner allein."':'Die Kapelle spielt den nächsten Marsch an: "Komm, schunkel mit! Wir haben noch Platz."',[['Zugabe fordern','mzug'],['Schunkel-Runde mitmachen','mm:schunkeln:0']]);
}
function skAct7(p){
 if(p.indexOf('mm:')===0){const a=p.split(':');mmStart(a[1],+a[2]);return true;}
 if(p==='jh'){const d=skl().find(q=>q.k==='jodl');if(d)jodlerHoeren(d);return true;}
 if(p==='mzug'){const d=skl().find(q=>q.k==='mu'&&(q.v==='blas'||q.v==='jeck'));if(d){closeAll();d.skip=true;skOpen(d);}return true;}
 return false;
}

const NATUR={
 pilze:['Pilze: Vorsicht beim Sammeln','Wildpilze sind schwer zu bestimmen. Verwechslungen können schwere Vergiftungen auslösen, manche Giftpilze sind lebensgefährlich und zeigen Beschwerden erst nach Stunden, wenn der Schaden schon da ist. Kochen, Braten oder Trocknen macht Giftpilze nicht ungefährlich. Wer nicht sicher ist, lässt sie stehen. Bei Beschwerden nach einer Pilzmahlzeit: sofort Notruf 112 oder den Giftnotruf deiner Region anrufen.'],
 psilo:['Berauschende Pilze: nur Nachteile','Sie sind in Deutschland verboten. Besitz, Anbau und Handel sind strafbar. Mögliche Nachteile: Angst und Panik, Verwirrung, Verfolgungsgedanken, Unfälle durch Fehleinschätzung und das Auslösen oder Verschlimmern psychischer Erkrankungen. Die Wirkung ist unberechenbar und lässt sich nicht steuern. Im Spiel kommen sie nicht vor und werden nicht empfohlen.'],
 hanf:['Hanf und Cannabis: Nachteile','Cannabis ist nur für Erwachsene und unter strengen gesetzlichen Regeln erlaubt, für unter 18 Jahre verboten. Mögliche Nachteile: Konzentration, Gedächtnis und Reaktion lassen nach, am Steuer ist es gefährlich, Abhängigkeit ist möglich, Rauchen reizt die Atemwege, bei Jugendlichen kann es die Gehirnentwicklung stören, und es kann Angst und Psychosen begünstigen. Wechselwirkungen mit Medikamenten sind möglich.'],
 hopfen:['Hopfen und Alkohol: Nachteile','Alkohol ist ein Zellgift. Er macht abhängig, belastet Leber und Herz, stört den Schlaf, erhöht das Unfall- und Streitrisiko und ist für unter 18, Schwangere und Autofahrer tabu. Hopfen selbst kann Allergien auslösen und ist für Hunde giftig. Hunde dürfen weder Hopfen noch Treber fressen.'],
 allg:['Natur ist nicht automatisch harmlos','Pflanzen und Pilze können Allergien, Vergiftungen und Wechselwirkungen mit Medikamenten auslösen. Hinter "ist doch natürlich" steckt kein Sicherheitsversprechen. Bei Beschwerden: Arztpraxis oder Notruf 112. Dieses Spiel macht keine Gesundheitsversprechen und empfiehlt keine Substanzen.']
};
function natureMenu(){
 mdl('Info-Tafel: Natur und Vorsicht','Hier steht, was die Natur auch kann, nämlich Probleme machen. Nur Nachteile und Risiken, keine Empfehlungen.',[['Pilze','nt:pilze'],['Berauschende Pilze','nt:psilo'],['Hanf','nt:hanf'],['Hopfen und Alkohol','nt:hopfen'],['Allgemein','nt:allg']]);
}
function bauerMenu(){
 mdl('Bauer Hannes','Der Bauer schiebt den Strohhut zurück: "Schön, dass du da bist! Hopfen klettert, Hanf wächst gerade nach oben, und die Bienen arbeiten für alle."',[['Plaudern','bpl'],['Bienen beobachten','bbi'],['Bei der Ernte mitmachen','mm:ernte:0']]);
}
function skAct8(p){
 if(p.indexOf('nt:')===0){const n=NATUR[p.slice(3)];if(n)showModal({title:n[0],text:n[1],choices:[{label:'Zurück zur Tafel',a:'skA',p:'ntm'},{label:'Fertig',a:'mclose'}]});return true;}
 if(p==='ntm'){natureMenu();return true;}
 if(p==='bpl'){mood(3,'+3 Plausch');sfx('pat');toast(pick(['Hannes: "Hopfen klettert im Sommer bis zu sieben Meter hoch. Immer im Uhrzeigersinn, ganz ohne Navi."','Hannes: "Industriehanf liefert Fasern für Seile, Stoffe und Dämmstoffe. Ein echtes Multitalent, und wächst wie Unkraut."','Hannes: "Der Duft kommt von den Blättern. Wer genau schnuppert, riecht Sommer."']));return true;}
 if(p==='bbi'){mood(3,'+3 Summ');sfx('pat');for(let i=0;i<4;i++)addFx(P.x+rf(-30,30),P.y-rf(10,40),'Summ','#ffe08a',1.6,rf(-20,-5));toast('Die Bienen fliegen von Blüte zu Blüte. Sie nehmen keine Notiz von dir, und das ist das größte Kompliment.');return true;}
 return false;
}
function drawFelder(cx,cy){
 const x0=3*TS,x1=20*TS,y0=4*TS,y1=13*TS+20;
 if(cy<y1+40&&cy+VH>y0-40){
  if(cx<x1+40&&cx+VW>x0-40){
   for(let x=x0+12;x<x1;x+=40){
    if(x<cx-30||x>cx+VW+30)continue;
    ctx.fillStyle='rgba(0,0,0,.18)';ctx.fillRect(x+3,y0+8,3,y1-y0);
    ctx.strokeStyle='#6a4a2a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x,y0);ctx.lineTo(x,y1);ctx.stroke();
    ctx.strokeStyle='#3f9a3f';ctx.lineWidth=5;ctx.beginPath();
    for(let y=y0;y<y1;y+=4){const o=Math.sin(y*.09+x)*6;if(y===y0)ctx.moveTo(x+o,y);else ctx.lineTo(x+o,y);}
    ctx.stroke();ctx.lineWidth=1;
    for(let y=y0+16;y<y1-6;y+=26){const o=Math.sin(y*.09+x)*6,sd=((y/26)|0)%2?1:-1;ctx.fillStyle='#a8d86a';ctx.beginPath();ctx.ellipse(x+o+sd*8,y+4,3.4,5.6,0,0,6.283);ctx.fill();ctx.fillStyle='#2f8a3a';ctx.beginPath();ctx.ellipse(x+o-sd*7,y-4,6,3.4,sd*.5,0,6.283);ctx.fill();}
   }
  }
 }
 const h0=28*TS,h1=45*TS;
 if(cy<y1+40&&cy+VH>y0-40&&cx<h1+40&&cx+VW>h0-40){
  for(let x=h0+14;x<h1;x+=36)for(let y=y0+22;y<y1;y+=40){
   if(x<cx-30||x>cx+VW+30||y<cy-40||y>cy+VH+40)continue;
   ctx.fillStyle='rgba(0,0,0,.15)';ctx.beginPath();ctx.ellipse(x+3,y+4,10,4,0,0,6.283);ctx.fill();
   ctx.strokeStyle='#3a8a3a';ctx.lineWidth=4;ctx.lineCap='round';ctx.beginPath();
   for(let k=-2;k<=2;k++){ctx.moveTo(x,y);ctx.lineTo(x+k*8,y-20+Math.abs(k)*5);}
   ctx.stroke();
   ctx.strokeStyle='#5cb85c';ctx.lineWidth=1.5;ctx.beginPath();
   for(let k=-2;k<=2;k++){ctx.moveTo(x,y);ctx.lineTo(x+k*8,y-20+Math.abs(k)*5);}
   ctx.stroke();ctx.lineCap='butt';ctx.lineWidth=1;
  }
 }
}
function drawBauer(d){
 const x=d.x,y=d.y;
 drawPerson(x,y,d.a,'#3a6aa8','ped',d.walk);
 ctx.fillStyle='#e8c96a';circle(x,y-1,9.5);ctx.fillStyle='#c9a24a';circle(x,y-1,4.2);
}
function drawFalter(d){
 const t=timeNow,fl=Math.abs(Math.sin(t*14+d.walk))*5+1;
 ctx.fillStyle=d.col;ctx.beginPath();ctx.ellipse(d.x-fl*.5,d.y-18,fl,3.6,.5,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(d.x+fl*.5,d.y-18,fl,3.6,-.5,0,6.283);ctx.fill();
 ctx.fillStyle='#333';ctx.fillRect(d.x-.6,d.y-21,1.2,6);
}
function ext14Update(dt){
 if(!G||!ZONE||ZONE.name!=='feldweg')return;
 const L=skl();
 L.forEach(d=>{
  if(d.k==='bauer'){leash(d,24*TS,17*TS,200);steerStep(d,dt,20);}
  else if(d.k==='falter'){
   d.walk+=dt;d.steer-=dt;if(d.steer<=0){d.a+=rf(-1.6,1.6);d.steer=rf(.6,1.6);}
   leash(d,d.hx,d.hy,280);
   d.x=clamp(d.x+Math.cos(d.a)*38*dt,3*TS,(ZW-3)*TS);d.y=clamp(d.y+Math.sin(d.a)*38*dt,3*TS,(ZH-3)*TS);
  }
 });
 if(chance(dt*6)){
  const x=P.x+rf(-320,320),y=P.y+rf(-200,200);
  const inH=x>3*TS&&x<20*TS&&y>4*TS&&y<14*TS,inN=x>28*TS&&x<45*TS&&y>4*TS&&y<14*TS;
  if(inH||inN)FX.push({x:x,y:y,vx:rf(-8,8),vy:rf(-14,-4),g:0,t:0,life:rf(2,3.5),dot:inH?pick(['#c8f08a','#a8d86a','#fff3a0']):pick(['#7acb6a','#d8f0a0','#fff3a0']),r:rf(1.2,2.2)});
 }
 if(chance(dt*.08)&&Math.hypot(24*TS-P.x,9*TS-P.y)<500)addFx(P.x+rf(-80,80),P.y-30,'Summ','#ffe08a',1.4,rf(-20,-5));
}

function frustV(){return G.frust===undefined?100:G.frust;}
function wurfMenu(){
 mdl('Wurfbude','Gratis für alle, die Dampf ablassen wollen. Die vier Sender-Gebäude sind Pappkulissen, es steht niemand dahinter. Dosen und Eier fliegen hier nur auf Kulissen, nie auf Menschen. Frust-Barometer: '+Math.round(frustV())+' %.',[['Dosen holen (bis 9)','wd'],['Eier holen (bis 9)','we'],['Was nervt mich eigentlich?','wnerv'],['Durchatmen (mitmachen)','mm:atem:0']]);
}
const WNERV=[
 ['Zu viel Werbung','Werbung nervt viele. Nutze die Pause für ein Glas Wasser, streck dich kurz oder mach das Fenster auf. Aufnahmen und Mediatheken lassen sich oft vorspulen. Und die Fernbedienung hat auch einen Ausschalter.'],
 ['Das Programm ist mir zu doof','Umschalten ist auch eine Meinung. Wer es genauer sagen will, schreibt dem Sender sachlich eine Nachricht an den Zuschauerservice. Das ist sinnvoller als jedes Ei.'],
 ['Die Nachrichten machen mir Stress','Nachrichten zu festen Zeiten reichen oft aus, einmal am Tag ist völlig in Ordnung. Danach Fernseher aus und kurz an die frische Luft. Wenn dich Sorgen länger belasten, hilft ein Gespräch mit jemandem, dem du vertraust.'],
 ['Alles zusammen','Dann mach eine Pause: Fernseher aus, zehn Minuten spazieren, Wasser trinken, jemanden anrufen. Wenn der Frust oft sehr groß ist, sprich mit einer Vertrauensperson oder mit deiner Ärztin oder deinem Arzt. Du musst das nicht allein tragen.']
];
function skAct9(p){
 if(p==='wd'){G.ammo.dose=9;if(!G.sel||G.sel==='ei')G.sel='dose';sfx('pick');toast('Dosen aufgefüllt: 9. Zum Werfen OK drücken, gezielt wird automatisch auf die Kulissen.');return true;}
 if(p==='we'){G.ammo.ei=9;G.sel='ei';sfx('pick');toast('Eier aufgefüllt: 9. Geh nah an die Kulissen und drück OK.');return true;}
 if(p==='wnerv'){mdl('Was nervt mich eigentlich?','Such dir eins aus, dann gibt es einen Tipp.',WNERV.map((q,i)=>[q[0],'wn:'+i]));return true;}
 if(p.indexOf('wn:')===0){const q=WNERV[+p.slice(3)];if(q)showModal({title:q[0],text:q[1],choices:[{label:'Noch ein Thema',a:'skA',p:'wnerv'},{label:'Fertig',a:'mclose'}]});return true;}
 return false;
}
function senderTarget(){
 const L=ZONE.BLD.filter(q=>q.k==='sender');let best=null,bd=1e9;
 L.forEach(q=>{const cx=(q.x+q.w/2)*TS,by=(q.y+q.h)*TS;if(P.y<by)return;const d=Math.abs(cx-P.x)+Math.abs(by-P.y)*.3;if(d<bd){bd=d;best={tx:clamp(P.x,q.x*TS+20,(q.x+q.w)*TS-20),ty:by-12};}});
 return best;
}
function calmDown(){
 G.calm=1;mood(15,'+Ruhe');sfx('win');
 showModal({title:'Besser?',text:'Der Frust ist raus, das Barometer steht auf null. Atme einmal tief durch. Im echten Leben bleiben Eier im Kühlschrank: Sie treffen Menschen und Häuser wirklich und machen nur Dreck und Ärger. Hier durfte die Pappe es abbekommen, und jetzt kannst du in Ruhe überlegen, was dich wirklich beschäftigt.',choices:[{label:'Durchatmen (mitmachen)',a:'skA',p:'mm:atem:0'},{label:'Was nervt mich eigentlich?',a:'skA',p:'wnerv'},{label:'Fertig',a:'mclose'}]});
}
function senderHit(b,nx,ny,tx,ty){
 const bl=ZONE.BLD.find(q=>q.k==='sender'&&tx>=q.x&&tx<q.x+q.w&&ty>=q.y&&ty<q.y+q.h);if(!bl)return false;
 const egg=b.type==='ei',bot=(bl.y+bl.h)*TS,roofB=bot-bl.hh-6;
 const sx=clamp(nx,bl.x*TS+14,(bl.x+bl.w)*TS-14),sy=clamp(ny-8,bl.y*TS+16,roofB);
 ZONE.splats=ZONE.splats||[];
 ZONE.splats.push({x:sx,y:sy,k:egg?'e':'d',r:rf(9,14),a:rf(0,6.28)});
 if(ZONE.splats.length>140)ZONE.splats.shift();
 addFx(sx,sy-14,egg?pick(['PLATSCH!','SPLAT!','KLECKS!']):pick(['KLONG!','DING!','BONG!']),egg?'#ffe08a':'#cfd6e0',1);
 if(chance(.55))addFx(sx,sy-30,pick(STN[bl.sn].h),'#9fd8ff',1.5);
 quoteAdd(1);lachband(sx,sy);
 for(let i=0;i<5;i++)FX.push({x:sx,y:sy,vx:rf(-50,50),vy:rf(-60,10),g:160,t:0,life:.7,dot:egg?'#ffe08a':'#cfd6e0',r:2.4});
 sfx(egg?'crunch':'bonk');
 if(!egg)PICKS.push({x:sx,y:bot+14,t:'dose'});
 const f0=frustV(),f1=Math.max(0,f0-(egg?5:3));G.frust=f1;
 [75,50,25].forEach(m=>{if(f0>m&&f1<=m)toast('Frust-Barometer: '+m+' %. Es wird leichter.');});
 if(f1<=0&&!G.calm)setTimeout(()=>{try{calmDown();}catch(e){}},500);
 return true;
}
function drawSender(cx,cy){
 const z=ZONE;if(!z)return;
 (z.splats||[]).forEach(s=>{
  if(s.x<cx-30||s.x>cx+VW+30||s.y<cy-30||s.y>cy+VH+30)return;
  if(s.k==='e'){
   ctx.fillStyle='rgba(255,252,235,.92)';ctx.beginPath();ctx.ellipse(s.x,s.y,s.r,s.r*.78,s.a,0,6.283);ctx.fill();
   ctx.beginPath();ctx.ellipse(s.x+s.r*.7,s.y+s.r*.25,s.r*.38,s.r*.3,s.a,0,6.283);ctx.fill();
   ctx.fillStyle='#ffc41f';ctx.beginPath();ctx.arc(s.x,s.y,s.r*.34,0,6.283);ctx.fill();
  }else{
   ctx.fillStyle='rgba(50,55,65,.6)';ctx.beginPath();ctx.arc(s.x,s.y,5,0,6.283);ctx.fill();
   ctx.strokeStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.arc(s.x,s.y,7.5,0,6.283);ctx.stroke();
  }
 });
 const gx=27*TS+8,gy=15*TS+4,f=frustV()/100;
 if(gx>cx-40&&gx<cx+VW+40&&gy>cy-80&&gy<cy+VH+60){
  ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(gx-6,gy-26,24,66);
  ctx.fillStyle='#f4f6f8';ctx.fillRect(gx-9,gy-30,24,68);
  ctx.fillStyle='#2b2f38';ctx.fillRect(gx-5,gy-5,16,38);
  ctx.fillStyle='hsl('+Math.round(120*(1-f))+',70%,50%)';ctx.fillRect(gx-5,gy+33-38*f,16,38*f);
  ctx.fillStyle='#2b2f38';ctx.font='bold 7px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('FRUST',gx+3,gy-24);ctx.fillText(Math.round(f*100)+'%',gx+3,gy-14);ctx.textAlign='start';ctx.textBaseline='alphabetic';
 }
}

const STN={
 RTL:{t:['Dschungelcamp für Zimmerpflanzen','Die Bachelorette wählt zwischen drei Toastern','Gerichtsshow: Der Fall der verschwundenen Socke','Mein Gartenzwerg, mein Hof, mein Sieg','Verkehrs-Alarm: Eine Ente hat Vorfahrt'],k:['EILMELDUNG: Wolke gesichtet, mehr nach der Werbung','Kuh übernimmt Vorstand, Gerücht bestätigt','Gleich: Cliffhanger, aber erst nach 12 Minuten Werbung'],h:['Wir bitten um Verständnis!','Und jetzt die Werbung!','Das Drama geht weiter!']},
 PRO7:{t:['Die Rosenschlacht der Gartenzwerge, 47. Wiederholung','Topmodel für Kartoffeln','Raumschiff Wäscheständer','Zwei Typen und ein Toaster','Superheld Opa, Folge 912'],k:['Nach der Werbung geht es weiter. Nach der nächsten auch.','Wiederholung der Wiederholung der Wiederholung','Heute neu: Gestern'],h:['Bild verrutscht!','Gleich geht es weiter!','Nach der Werbung!']},
 ARD:{t:['Nachrichten um Acht-ish: Heute mit Wolke','Krimi am Sonntag: Wer hat den Kuchen angeschnitten?','Wetter vor dem Wetter','Sport: Synchron-Pusten, Finale','Brisant-ish: Die Katze und ihr Anwalt'],k:['Wetter: Es regnet Pudding, vereinzelt Pfannkuchen','Zuschauer um drei Uhr nachts: 1 (Hund)','Breaking: Fernbedienung gefunden'],h:['Kein Empfang!','Rauschen ...','Bitte warten ...']},
 ZDF:{t:['Der Landarzt der Zimmerpflanzen','Kochen mit Opa, aber ohne Rezept','Volksmusik-Gala: Alle jodeln gleichzeitig','Fernsehgarten der tausend Gartenzwerge','Quiz: Wer wird Hausmeister?'],k:['Zuschauer-Anruf: Es klingelt, niemand hebt ab','Heute im Programm: das Programm','Die Mediathek ist gerade im Urlaub'],h:['Testbild übt!','Moment, das Bild tanzt!','Sendepause, aber lustig!']}
};
const SGN=[[6,13,['WERBEPAUSE','Bitte 12 Min. warten']],[40,13,['MODERATOREN','nicht füttern']],[14,21,['KLATSCH-ZONE','Applaus ist Pflicht']],[34,21,['WIEDERHOLUNG','Wie gestern. Und vorgestern.']],[22,25,['HIER KÖNNTE','Ihre Werbung stehen']]];
function quoteV(){return G.quote|0;}
function quoteAdd(n){
 const a=quoteV(),b=a+n;G.quote=b;
 const T={5:'Eilmeldung: Die Quote steigt! Alle Sender wollen jetzt Eier-Shows.',15:'Sondersendung: "Ei trifft Kulisse". Wir schalten live zur Kulisse. Die Kulisse sagt nichts.',30:'Die Kulisse bekommt eine eigene Show: "Pappe sucht den Superstar".',50:'Fernsehpreis für das beste Ei! Du nimmst ihn bescheiden entgegen, mit Konfetti.'};
 Object.keys(T).forEach(m=>{if(a<+m&&b>=+m){toast(T[m]);sfx('clap');if(+m===50){mood(10,'+Preis');for(let i=0;i<30;i++)FX.push({x:P.x,y:P.y,vx:rf(-110,110),vy:rf(-140,-30),g:150,t:0,life:1.4,dot:pick(['#ffd23f','#ff5fd0','#5ff0ff','#7bd86a']),r:2.6});}}});
}
function lachband(x,y){if(chance(.3)){addFx(x,y-44,pick(['HAHAHA (vom Band)','Applaus vom Band','Buh! (vom Band)','Oooh! (vom Band)']),'#e8e8ff',1.6);sfx('clap');}}
function modMenu(){mdl('Moderator Mike Mikrofon','"Willkommen, willkommen, WILLKOMMEN! Sie sind live auf Sendung, und niemand sieht zu. Was möchten Sie der Nation sagen?"',[['Ich will nur Eier werfen','mq:0'],['Ich hätte gern eine Werbepause','mq:1'],['Ich bin die Nation','mq:2'],['Bei mir ist der Ton aus','mq:3']]);}
const MQ=[
 '"Ein mutiger Beitrag! Dafür gibt es Applaus vom Band." Von irgendwoher kommt ein Lacher. Das Band hat längst Feierabend.',
 '"Genau jetzt?!" Mike zögert, dann wird er mitten im Satz zum Teleshop-Verkäufer: "Dieses Mikrofon, nur heute, GRATIS!" Er hält es dir hin und nimmt es wieder weg.',
 '"Was für ein Zufall, wir suchen gerade eine Nation!" Er überreicht dir eine Urkunde, die er sofort wieder zurückfordert. Sie ist die einzige.',
 '"Wir hören Sie ganz wunderbar!" Er winkt in eine Kamera, die nur aus Pappe besteht. Die Pappe winkt nicht zurück, aber sie hat Haltung.'
];
function prakMenu(){mdl('Praktikant Paul','"Klappe, die vierhundertste! Ich bin Praktikant seit elf Jahren. Es ist nur vorübergehend, sagt man mir."',[['Frag nach dem Gehalt','pk:0'],['Biete ihm Eier an','pk:1'],['Ruf: Klappe!','pk:2']]);}
const PK=[
 'Gehalt? Er bekommt eine Brezel pro Monat und sehr viel Erfahrung. Er strahlt: "Die Brezel ist Bio!"',
 'Er lehnt ab: "Eier sind Chefsache, ich darf nur Kaffee tragen." Dann trägt er zwölf Kaffee, null Eier und sehr viel Verantwortung davon.',
 'KLAPPE! Alle erstarren. Zwei Sekunden lang ist es still. Dann niest ein Hund. Der Praktikant notiert: "Beste Szene der Woche."'
];
function gurkeMenu(){mdl('Werbe-Gurke Gerd','"Brauchen Sie das? NEIN! Aber SIE bekommen es TROTZDEM! Und zwar fast gratis, Sie zahlen nur Versand: 0 €!"',[['Den Ei-Fänger bestellen','gt:0'],['Den Dosen-Öffner für Dosen ohne Deckel','gt:1'],['Die Fernbedienung für die Fernbedienung','gt:2']]);}
const GT=[
 'Bestellt! Der Ei-Fänger kommt am Montag. Welcher Montag, wird nicht verraten. Gerd fügt hinzu: "Wenn Sie jetzt anrufen, bekommen Sie zwei zum Preis von zwei!"',
 'Bestellt! Der Dosen-Öffner öffnet Dosen ohne Deckel. Gerd: "Er funktioniert garantiert, es gibt nichts zu öffnen." Du bekommst nichts und bist trotzdem begeistert.',
 'Bestellt! Die zweite Fernbedienung bedient die erste Fernbedienung. Ab sofort musst du nur noch eine Fernbedienung finden. Gerd: "Das ist der Fortschritt!"'
];
function repMenu(){mdl('Reporter Rainer Rauschen','"Straßenumfrage! Eine einzige Frage, und die Nation sieht gespannt zu, also drei Leute. Was ist schlimmer?"',[['Werbung im Film','rp:0'],['Film in der Werbung','rp:1'],['Beides, aber mit Eiern','rp:2']]);}
const RPL=[
 '"Zwei Drittel der Befragten sind derselbe Mann in verschiedenen Mänteln." Rainer nickt ernst und schreibt "Mehrheit" auf seinen Block.',
 '"Spannend! Ein Drittel sagt Film, ein Drittel sagt Werbung, ein Drittel sagt: Hä?" Das ist laut Rainer repräsentativ.',
 '"Ein Ergebnis für die Geschichtsbücher!" Er will die Antwort live senden, aber das Mikrofon ist ein Plüschball. Er sendet trotzdem.'
];
function skAct10(p){
 const T=[['mq:',MQ,modMenu,'Noch eine Frage'],['pk:',PK,prakMenu,'Noch ein Satz'],['gt:',GT,gurkeMenu,'Noch ein Angebot'],['rp:',RPL,repMenu,'Noch eine Umfrage']];
 for(let i=0;i<T.length;i++){const q=T[i];if(p.indexOf(q[0])===0){const t=q[1][+p.slice(q[0].length)];if(t){mood(4,'+Lacher');quoteAdd(2);sfx('clap');showModal({title:'Satire pur',text:t,choices:[{label:q[3],a:'skA',p:'sq:'+i},{label:'Fertig',a:'mclose'}]});}return true;}}
 if(p.indexOf('sq:')===0){[modMenu,prakMenu,gurkeMenu,repMenu][+p.slice(3)]();return true;}
 return false;
}
function drawMod(d){drawPerson(d.x,d.y,d.a,'#d8b030','ped',d.walk);ctx.fillStyle='#ffe9a8';ctx.beginPath();ctx.ellipse(d.x+Math.cos(d.a+.4)*3,d.y+Math.sin(d.a+.4)*3-1,6,4.5,d.a,0,6.283);ctx.fill();ctx.strokeStyle='#222';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(d.x+Math.cos(d.a)*6,d.y+Math.sin(d.a)*6);ctx.lineTo(d.x+Math.cos(d.a)*17,d.y+Math.sin(d.a)*17);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#e8e8e8';circle(d.x+Math.cos(d.a)*19,d.y+Math.sin(d.a)*19,4.6);}
function drawPrak(d){drawPerson(d.x,d.y,d.a,'#5a9ad8','ped',d.walk);const bx=d.x+Math.cos(d.a)*10,by=d.y+Math.sin(d.a)*10;ctx.fillStyle='#161616';ctx.fillRect(bx-6,by-4,12,8);ctx.fillStyle='#f4f4f4';for(let i=0;i<3;i++)ctx.fillRect(bx-5+i*4,by-4,2,3);}
function drawGurke(d){ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+4,8,13,d.a+1.57,0,6.283);ctx.fill();ctx.fillStyle='#4fa83c';ctx.beginPath();ctx.ellipse(d.x,d.y,8,13,d.a+1.57,0,6.283);ctx.fill();ctx.fillStyle='#3a8a2c';for(let i=-2;i<=2;i++)circle(d.x+Math.cos(d.a)*i*4+Math.cos(d.a+1.57)*3,d.y+Math.sin(d.a)*i*4+Math.sin(d.a+1.57)*3,1.4);ctx.fillStyle='#111';ctx.fillRect(d.x+Math.cos(d.a)*9-5,d.y+Math.sin(d.a)*9-2,10,4);ctx.fillStyle='#ffd23f';circle(d.x+Math.cos(d.a+1.57)*9,d.y+Math.sin(d.a+1.57)*9,2.4);circle(d.x-Math.cos(d.a+1.57)*9,d.y-Math.sin(d.a+1.57)*9,2.4);}
function drawRep(d){drawPerson(d.x,d.y,d.a,'#e8584a','ped',d.walk);ctx.strokeStyle='#222';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(d.x+Math.cos(d.a)*6,d.y+Math.sin(d.a)*6);ctx.lineTo(d.x+Math.cos(d.a)*15,d.y+Math.sin(d.a)*15);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#3a3a3a';circle(d.x+Math.cos(d.a)*18,d.y+Math.sin(d.a)*18,5.2);ctx.fillStyle='#555';circle(d.x+Math.cos(d.a)*18-1,d.y+Math.sin(d.a)*18-1,2.4);}
function ext16Update(dt){
 if(!G||!ZONE||ZONE.name!=='sender')return;
 skl().forEach(d=>{
  const dp=Math.hypot(P.x-d.x,P.y-d.y);
  if(d.k==='mod'){leash(d,d.hx,d.hy,170);steerStep(d,dt,16);}
  else if(d.k==='prak'){leash(d,d.hx,d.hy,230);steerStep(d,dt,52);if(chance(dt*.04)){addFx(d.x,d.y-18,'Plumps!','#ffd23f',1);d.a+=3;}}
  else if(d.k==='gurke'){leash(d,d.hx,d.hy,150);steerStep(d,dt,14);}
  else if(d.k==='rep'){
   if(dp>46&&dp<260){d.a=Math.atan2(P.y-d.y,P.x-d.x);const nx=d.x+Math.cos(d.a)*34*dt,ny=d.y+Math.sin(d.a)*34*dt;if(skOk(nx,ny)){d.x=nx;d.y=ny;d.walk+=dt*8;}}
   else{leash(d,d.hx,d.hy,200);steerStep(d,dt,16);}
  }else return;
  d.cd=(d.cd||0)-dt;
  if(d.cd<=0&&dp<320){d.cd=rf(6,12);const L={mod:['Und weiter geht\'s!','Bleiben Sie dran!','Applaus, bitte!','Gleich nach der Werbung!'],prak:['Klappe!','Ich bin nur kurz hier!','Wo ist der Kaffee?!'],gurke:['Nur heute: 0 €!','Jetzt anrufen!','Gurke, Gurke, Gurke!'],rep:['Eine Frage!','Kurz in die Kamera!','Wie fühlen Sie sich?']}[d.k];addFx(d.x,d.y-26,pick(L),'#fff2b0',1.8);}
 });
}
function drawSender2(cx,cy){
 const z=ZONE;if(!z)return;
 z.BLD.forEach(b=>{
  if(b.k!=='sender')return;
  const x=b.x*TS,y=b.y*TS,w=b.w*TS,h=b.h*TS;
  if(x>cx+VW||x+w<cx||y>cy+VH||y+h<cy)return;
  const S=STN[b.sn],hh2=h-b.hh,sx=x+10,sy=y+10,sw=w-20,sh=hh2-34;
  ctx.save();ctx.beginPath();ctx.rect(sx,sy,sw,sh);ctx.clip();
  ctx.fillStyle='rgba(0,0,0,.65)';ctx.fillRect(sx,sy,sw,16);ctx.fillRect(sx,sy+sh-16,sw,16);
  ctx.font='bold 10px Arial';ctx.textBaseline='middle';ctx.textAlign='left';
  ctx.fillStyle='#ffd23f';ctx.fillText('JETZT: '+S.t[Math.floor(timeNow/4+b.x)%S.t.length],sx+5,sy+8);
  if(!b.tx)b.tx=S.k.join('   +++   ')+'   +++   ';
  if(!b.tw){ctx.font='bold 9px Arial';b.tw=ctx.measureText(b.tx).width;}
  ctx.font='bold 9px Arial';ctx.fillStyle='#fff';
  const off=(timeNow*38+b.x*20)%(b.tw);
  ctx.fillText(b.tx,sx-off,sy+sh-8);ctx.fillText(b.tx,sx-off+b.tw,sy+sh-8);
  ctx.restore();
 });
 SGN.forEach(q=>{
  const x=q[0]*TS,y=q[1]*TS;if(x<cx-90||x>cx+VW+90||y<cy-50||y>cy+VH+50)return;
  ctx.fillStyle='rgba(0,0,0,.28)';ctx.fillRect(x-42,y-18,92,42);
  ctx.fillStyle='#7a5a3a';ctx.fillRect(x-2,y+14,5,14);
  ctx.fillStyle='#f4efe0';ctx.fillRect(x-46,y-22,92,40);ctx.strokeStyle='#2b2f38';ctx.lineWidth=2;ctx.strokeRect(x-46,y-22,92,40);ctx.lineWidth=1;
  ctx.fillStyle='#b8302f';ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(q[2][0],x,y-10);
  ctx.fillStyle='#2b2f38';ctx.font='bold 7px Arial';ctx.fillText(q[2][1],x,y+4);
 });
 const gx=27*TS+8+34,gy=15*TS+4;
 if(gx>cx-60&&gx<cx+VW+60&&gy>cy-80&&gy<cy+VH+60){
  ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(gx-3,gy-26,66,50);
  ctx.fillStyle='#f4f6f8';ctx.fillRect(gx-6,gy-30,66,52);
  ctx.fillStyle='#2b2f38';ctx.font='bold 7px Arial';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText('ZUSCHAUER',gx+27,gy-23);ctx.font='bold 13px Arial';ctx.fillStyle='#b8302f';ctx.fillText(String(1+quoteV()*7),gx+27,gy-9);ctx.font='bold 7px Arial';ctx.fillStyle='#2b2f38';ctx.fillText('(davon 1 Hund)',gx+27,gy+6);ctx.fillText('Quote steigt!',gx+27,gy+15);
 }
 ctx.textAlign='start';ctx.textBaseline='alphabetic';
}

const HER=[
 {n:'Toast-Titan',s:['Ich bin goldbraun!','Butter, bei Fuß!','Nicht verbrannt, nur dramatisch!'],t:'"Ich bin knusprig, ich bin golden, und ich bin NICHT verbrannt! Meine Superkraft: Ich springe genau im richtigen Moment aus dem Toaster."',q:['Wer ist dein Erzfeind?','Zeig mir deine Superkraft','Kannst du fliegen?'],a:[
  'Der Montag! Er kommt jede Woche wieder, obwohl ihn keiner eingeladen hat. Toast-Titan hat ihn schon dreimal besiegt. Der Montag kommt trotzdem.',
  'Er springt hoch, dreht sich in der Luft und landet butterseitig nach oben. Das ist laut Toast-Titan die schwerste Pose der Welt. Er klatscht sich selbst Applaus.',
  '"Kann ich nicht, aber ich kann sehr hoch hüpfen und dann sehr dramatisch fallen. Das nennt man Heldentum."']},
 {n:'Doktor Dauerwelle',s:['Fön an!','Meine Locken streiten wieder!','Zeit steht still, Frisur nicht!'],t:'"Ich halte die Zeit an, solange der Fön läuft! Leider nur 40 Sekunden, dann muss ich Locken nachlegen."',q:['Wer ist dein Erzfeind?','Zeig mir deine Superkraft','Was ist mit deinen Locken?'],a:[
  'Die Luftfeuchtigkeit! Sie lauert in jeder Wolke und wartet, bis die Frisur sitzt. Deshalb trägt der Doktor immer einen Regenschirm. Zwei.',
  'Er schaltet den Fön ein, und die Welt wird still. Nur seine Frisur wackelt noch. Nach 40 Sekunden fällt der Strom aus, und alle tun so, als wäre nichts gewesen.',
  'Jede Locke ist ein Superheld. Er hat etwa 4.000, und sie streiten sich ständig, wer vorne stehen darf.']},
 {n:'Frau Wäscheleine',s:['Alles aufhängen!','Wo ist die zweite Socke?','Leine frei!'],t:'"Ich hänge alles auf, was nicht bei drei auf den Bäumen ist!" Sie zieht eine Leine hinter sich her, an der drei Socken flattern, die nie ein Paar werden.',q:['Wer ist dein Erzfeind?','Zeig mir deine Superkraft','Wie heißen die Socken?'],a:[
  'Der Wäscheberg! Er wächst nachts, wenn niemand hinsieht. Sie hat ihn schon dreimal sortiert, er kam trotzdem wieder. Er hat inzwischen einen Namen und eine Meinung.',
  'Sie wirft die Leine aus, fängt jede Socke und hängt alles ordentlich nebeneinander auf. Am Ende gibt es zwei Paare und eine übrig gebliebene Socke, "den Einzelgänger".',
  'Eins, Zwei und Der Rest. Eins und Zwei verstehen sich gut. Der Rest sucht seit Jahren seinen Partner. Es gibt Hoffnung.']},
 {n:'Rasenmäher-Rächer',s:['Zu lang!','Brrrrrr!','Alles wird kürzer!'],t:'"Ich mähe alles, was zu lang ist: Gras, Wartezeiten, Reden von Moderatoren!" Er schiebt einen Rasenmäher, der brummt wie eine große, zufriedene Hummel.',q:['Wer ist dein Erzfeind?','Zeig mir deine Superkraft','Was ist mit Wartezeiten?'],a:[
  'Der Löwenzahn. Er lacht jedes Mal und wächst nach. Der Rächer sagt: "Eines Tages mähe ich ihm das Grinsen weg." Dann pustet er ihm lieber eine Pusteblume vor.',
  'Er mäht eine perfekte Spirale ins Gras. Alle Zuschauer sagen "Aaah". Es ist die einzige Superkraft mit Genehmigung vom Ordnungsamt.',
  'Er hat die Wartezeit auf dem Amt auf nur zwei Stunden gemäht. Das hat sich herumgesprochen. Seitdem bekommt er Blumen.']},
 {n:'Hausschuh-Held',s:['Schlurf, schlurf!','Pantoffel-Warp!','Kaffee? Später!'],t:'"Ich trage einen Bademantel und eine Maske aus einem riesigen Pantoffel. Niemand erkennt mich, nicht mal ich selbst." Er schlurft gemütlich über den Platz.',q:['Wer ist dein Erzfeind?','Zeig mir deine Superkraft','Was ist mit deiner Maske?'],a:[
  'Der Kalte Fußboden! Er schleicht sich nachts an und pikst in die Zehen. Der Held bekämpft ihn mit Wollsocken. Der Boden lacht, aber nur ein bisschen.',
  'Er schlurft so schnell, dass er fast nicht von der Stelle kommt. Das nennt er "Pantoffel-Warp". Die Gegner sind verwirrt, die Kuh auch.',
  'Der Pantoffel hat links ein Loch, durch das er die Welt anschaut. Er sagt, es sei das beste Visier der Welt: kaum Durchzug, dafür Aussicht.']}
];
function heroMenu(v){
 const h=HER[v];
 G.hm=G.hm||{};if(!G.hm[v]){G.hm[v]=1;G.hero=(G.hero||0)+.5;toast('Heldentreffen '+Object.keys(G.hm).length+' von 5: '+h.n+'.');}
 mdl(h.n,h.t,h.q.map((q,i)=>[q,'hm:'+v+':'+i]));
}
function pruMenu(){
 const n=Object.keys(G.hm||{}).length;
 mdl('Heldenprüfung','"Willkommen zur Heldenprüfung! Bestehen kann jeder, Durchfallen kann keiner. Es gibt nur Heldenpunkte und Applaus. Niemand kämpft, niemand wird verletzt." Heldentreffen: '+n+' von 5.',[['Heldenpose üben (mitmachen)','mm:held:0'],['Unser Motto lesen','pm'],['Heldenschein abholen','hsch']]);
}
function skAct11(p){
 if(p.indexOf('hm:')===0){const a=p.split(':'),h=HER[+a[1]];if(h){mood(4,'+Lacher');sfx('clap');showModal({title:h.n,text:h.a[+a[2]],choices:[{label:'Noch eine Frage',a:'skA',p:'hn:'+a[1]},{label:'Fertig',a:'mclose'}]});}return true;}
 if(p.indexOf('hn:')===0){heroMenu(+p.slice(3));return true;}
 if(p==='pm'){showModal({title:'Unser Motto',text:'Held ist, wer freundlich bleibt, wenn der Toast verbrennt. Held ist, wer die Eier im Kühlschrank lässt. Held ist, wer den Wäscheberg sortiert. Und Held ist, wer Pause macht, wenn es zu viel wird.',choices:[{label:'Zurück',a:'skA',p:'pz'},{label:'Fertig',a:'mclose'}]});return true;}
 if(p==='pz'){pruMenu();return true;}
 if(p==='hsch'){
  const n=Object.keys(G.hm||{}).length;
  if(G.schein){toast('Du hast deinen Heldenschein schon. Er ist laminiert und riecht nach Toast.');return true;}
  if(n<5){toast('Dir fehlen noch '+(5-n)+' Heldentreffen für den Heldenschein.');return true;}
  G.schein=1;G.hero=(G.hero||0)+2;mood(12,'+Heldenschein');sfx('win');
  for(let i=0;i<30;i++)FX.push({x:P.x,y:P.y,vx:rf(-110,110),vy:rf(-140,-30),g:150,t:0,life:1.4,dot:pick(['#ffd23f','#ff5fd0','#5ff0ff','#7bd86a']),r:2.6});
  showModal({title:'Heldenschein!',text:'Du hast alle fünf Helden getroffen und bekommst den offiziellen Heldenschein, laminiert, mit Foto von dir als Toast. Du darfst ab sofort überall dramatisch fallen.',choices:[{label:'Danke!',a:'mclose'}]});
  return true;
 }
 return false;
}
function drawHero(d){
 const x=d.x,y=d.y,v=d.hv,t=timeNow;
 ctx.save();ctx.translate(x,y);ctx.rotate(d.a);
 if(v===0){ctx.fillStyle='#f2d36a';ctx.beginPath();ctx.moveTo(-8,4);ctx.lineTo(-22,11);ctx.lineTo(-22,-11);ctx.lineTo(-8,-4);ctx.closePath();ctx.fill();}
 if(v===2){ctx.strokeStyle='#cfd6e0';ctx.lineWidth=1.5;ctx.beginPath();ctx.moveTo(-6,0);for(let i=1;i<=6;i++)ctx.lineTo(-6-i*6,Math.sin(t*5+i)*3);ctx.stroke();ctx.lineWidth=1;['#e8584a','#4a9ae8','#f2d36a'].forEach((c,i)=>{ctx.fillStyle=c;ctx.fillRect(-14-i*9,Math.sin(t*5+i*2)*3+1,4,6);});}
 ctx.restore();
 drawPerson(x,y,d.a,['#c98a3a','#f4f6f8','#2fa8a0','#4fa83c','#e8d04a'][v],'ped',d.walk);
 ctx.save();ctx.translate(x,y);ctx.rotate(d.a);
 if(v===0){ctx.fillStyle='#e8b45a';ctx.fillRect(-8,-8,16,16);ctx.strokeStyle='#9a5f1c';ctx.lineWidth=2;ctx.strokeRect(-8,-8,16,16);ctx.lineWidth=1;ctx.fillStyle='#fff2a8';ctx.fillRect(-3,-3,7,5);}
 else if(v===1){ctx.fillStyle='#ff8fc8';circle(1,0,9);ctx.strokeStyle='#d8508f';ctx.lineWidth=1.5;ctx.beginPath();for(let a=0;a<12;a+=.4)ctx.lineTo(1+Math.cos(a)*a*.7,Math.sin(a)*a*.7);ctx.stroke();ctx.lineWidth=1;}
 else if(v===3){ctx.fillStyle='#3a6a2c';ctx.fillRect(9,-6,12,12);ctx.fillStyle='#bfc6d0';circle(15,0,4.5);ctx.strokeStyle='#555';ctx.beginPath();ctx.moveTo(15-4,0);ctx.lineTo(15+4,0);ctx.moveTo(15,-4);ctx.lineTo(15,4);ctx.stroke();}
 else if(v===4){ctx.fillStyle='#f6e27a';ctx.beginPath();ctx.ellipse(-2,0,10,8,0,0,6.283);ctx.fill();ctx.fillStyle='#9a6a3a';ctx.beginPath();ctx.ellipse(4,0,8,6,0,0,6.283);ctx.fill();ctx.fillStyle='#222';circle(6,-1,1.6);ctx.fillStyle='#ff8fc8';ctx.beginPath();ctx.ellipse(2,-9,4,2.2,0,0,6.283);ctx.ellipse(2,9,4,2.2,0,0,6.283);ctx.fill();}
 ctx.restore();
}
function ext17Update(dt){
 if(!G||!ZONE||ZONE.name!=='helden')return;
 skl().forEach(d=>{
  if(d.k!=='hero')return;
  const dp=Math.hypot(P.x-d.x,P.y-d.y),v=d.hv;
  leash(d,d.hx,d.hy,v===2?240:170);steerStep(d,dt,[22,14,30,26,12][v]);
  if(v===3&&chance(dt*6))FX.push({x:d.x+Math.cos(d.a)*15,y:d.y+Math.sin(d.a)*15,vx:rf(-30,30),vy:rf(-40,-10),g:90,t:0,life:.6,dot:pick(['#4fa83c','#7bd86a']),r:1.8});
  d.cd=(d.cd||0)-dt;
  if(d.cd<=0&&dp<320){d.cd=rf(7,12);addFx(d.x,d.y-26,pick(HER[v].s),'#fff2b0',1.8);}
 });
}

const AMB=['Nr. 3 bitte zu Schalter 12','Nr. 3 bitte zu Schalter 12 (nochmal)','Nr. 4 ist noch nicht dran, auch nicht bald','Schalter 7 ist gerade im Urlaub','Mittagspause: 8:00 bis 8:05 Uhr','Bitte Ihre Nummer bereithalten (haben Sie eine?)','Heute neu: Warten mit Aussicht','Schalter -1 ist jetzt geöffnet','Nr. 0 wird gesucht, bitte melden'];
const AMS=[[8,14,['BITTE WARTEN','Sie machen das toll']],[40,14,['AUSKUNFT','Nicht hier. Nebenan.']],[8,22,['PAUSE','8:00 bis 8:05 Uhr']],[40,22,['FORMULAR 38b','hier NICHT erhältlich']],[24,25,['RECHTS WARTEN','LINKS AUCH']]];
function stampAdd(txt){
 G.stamps=(G.stamps|0)+1;
 ZONE.stamps=ZONE.stamps||[];ZONE.stamps.push({x:P.x+rf(-22,22),y:P.y+rf(14,30),t:txt,a:rf(-.5,.5)});
 if(ZONE.stamps.length>40)ZONE.stamps.shift();
 sfx('bonk');addFx(P.x,P.y-18,'KLONK!','#ffd23f',1);
 const T={10:'Du bist jetzt Stempelmeister. Das ist ein echter Titel, er steht auf einem Zettel.',25:'Beförderung zum stellvertretenden Vizeleiter des Referats für Referate! Gehalt: eine zweite Brezel.'};
 if(T[G.stamps]){toast(T[G.stamps]);sfx('clap');mood(8,'+Beförderung');for(let i=0;i<24;i++)FX.push({x:P.x,y:P.y,vx:rf(-110,110),vy:rf(-140,-30),g:150,t:0,life:1.4,dot:pick(['#ffd23f','#ff5fd0','#5ff0ff','#7bd86a']),r:2.6});}
}
function nummerMenu(){
 mdl('Wartenummern-Automat','Ein Automat mit einem einzigen Knopf. Auf dem Display steht: "Aktuell aufgerufen: Nr. 3. Ihre Wartezeit: ungefähr ja."',[['Nummer ziehen','nr'],['Aufruf abwarten','nw'],['Warte-Gymnastik (mitmachen)','mm:amt:0']]);
}
function stempelMenu(){
 mdl('Stempeltisch','Ein Tisch voller Stempel und ein Kissen in Amtsfarbe. Ein Zettel: "Gestempelt ist halb genehmigt." Gestempelt: '+(G.stamps|0)+'.',[['GENEHMIGT','sg:0'],['ABGELEHNT (aber freundlich)','sg:1'],['VORLÄUFIG ENDGÜLTIG','sg:2'],['ZUR SICHERHEIT NOCHMAL','sg:3']]);
}
const SG=[
 ['GENEHMIGT','GENEHMIGT! Was genau, weiß niemand. Aber es ist genehmigt, und das fühlt sich gut an.'],
 ['ABGELEHNT','ABGELEHNT, aber freundlich. Dazu gibt es eine Brezel und den Satz: "Das haben Sie ganz toll beantragt."'],
 ['VORLÄUFIG ENDGÜLTIG','VORLÄUFIG ENDGÜLTIG: der höchste Rang im Amt. Es gilt für immer, aber nur bis Dienstag.'],
 ['NOCHMAL','ZUR SICHERHEIT NOCHMAL gestempelt. Das Papier ist jetzt so schwer, dass es amtlich als Möbelstück gilt.']
];
const BE={
 t:'"Zuständig bin ich nicht, aber ich stempel schon mal." Er stempelt dabei ununterbrochen, auch die Luft.',n:'Herr Stempel',
 q:['Ich möchte etwas beantragen','Wo ist die Toilette?','Ich habe Zeit'],
 a:['"Dafür brauchen Sie Formular 38b. Dafür brauchen Sie Formular 38a. Dafür brauchen Sie ein Passbild von Ihrem Passbild." Er nickt zufrieden.','"Zuständig ist Referat 7, Zimmer 7. Zimmer 7 ist das Referat. Das Referat ist in Zimmer 7. Viel Erfolg." Er stempelt dir vorsorglich die Stirn. Mit Wasser.','"Dann sind Sie hier genau richtig, hier hat man Zeit seit 1974." Er holt einen Stuhl und stellt ihn so hin, dass du ihn nicht erreichst.']};
const FO={
 t:'"Ich habe für jeden Anlass ein Formular! Auch für Anlässe ohne Anlass." Sie trägt einen Stapel, der höher ist als sie, und niemand weiß, wie sie dabei sehen kann.',n:'Frau Formular',
 q:['Antrag auf Antrag','Formular für Spaß','Formular für Formulare'],
 a:['Sie reicht dir den "Antrag auf Antrag". Er hat einen Absatz: "Hiermit beantrage ich, dass ich beantragen darf." Du unterschreibst. Sie lächelt und beantragt sofort den nächsten.','Das Formular für Spaß ist leer, weil Spaß sich nicht beantragen lässt. Sie bittet trotzdem um Durchschriften in dreifacher Ausfertigung. Alle drei sind leer, und alle drei sind glücklich.','Das Formular für Formulare wird auf einem Formular ausgefüllt. Sie nennt das "Rekursion" und bekommt feuchte Augen vor Stolz.']};
const OR={
 t:'Ein riesiger Aktenordner auf zwei Beinen. Auf dem Rücken steht in Handschrift: "BITTE NICHT ÖFFNEN (ich bin voll)".',n:'Ordnerich',
 q:['Was ist in dir drin?','Wie fühlst du dich?','Willst du abgeheftet werden?'],
 a:['"Zwölf Anträge, ein Sandwich vom letzten Jahr und ein Hauch von Hoffnung." Er hustet, und ein Locher fällt heraus. Beide tun so, als wäre nichts gewesen.','"Gelocht. Immer ein bisschen gelocht." Er schaut traurig an sich herab und rückt die Metallringe zurecht.','"Ich möchte nur nicht unter Sonstiges." Er zittert. Unter Sonstiges ist der schlimmste Ort der Welt. Dort liegen die verlorenen Socken des Amtes.']};
const ZG={
 t:'Ein Gartenzwerg mit einem Schild: "NICHT ZUSTÄNDIG". Er zeigt mit dem ganzen Arm in eine Richtung, die sich ständig ändert.',n:'Zuständigkeits-Zwerg',
 q:['Wer ist denn zuständig?','Wo ist die Auskunft?','Kannst du helfen?'],
 a:['"Der Zwerg links von mir." Du schaust nach links. Da steht niemand. Er nickt weise, als wäre das die Antwort.','"Nebenan." Du gehst nebenan. Nebenan sagt: "Nebenan." Die Auskunft ist ein Kreis, und der Zwerg ist sein Mittelpunkt.','"Nein, aber ich zeige dir gern genau, wo man nicht helfen kann." Er zeigt es dir sehr genau. Es ist beeindruckend.']};
const AMD={beamt:BE,forma:FO,ordn:OR,zgn:ZG};
function amtMenu(k){const d=AMD[k];mdl(d.n,d.t,d.q.map((q,i)=>[q,'ax:'+k+':'+i]));}
function skAct12(p){
 if(p==='nr'){
  if(G.tk){toast('Du hast schon die Nummer '+G.tk+'. Mehr Nummern machen es nicht schneller, aber lustiger.');return true;}
  G.tk=1000+Math.floor(Math.random()*9000);sfx('ding');
  showModal({title:'Nummer gezogen',text:'Deine Nummer: '+G.tk+'. Aktuell aufgerufen wird die Nr. 3. Das Display wünscht dir "viel Spaß beim Warten".',choices:[{label:'Zurück zum Automaten',a:'skA',p:'nm'},{label:'Fertig',a:'mclose'}]});
  return true;
 }
 if(p==='nm'){nummerMenu();return true;}
 if(p==='nw'){
  if(!G.tk){toast('Ohne Nummer wartet man nicht, man steht nur herum. Zieh erst eine Nummer.');return true;}
  const n=G.tk;G.tk=0;G.waited=(G.waited|0)+1;mood(8,'+Aufgerufen');sfx('win');
  showModal({title:'Ding-Dong!',text:'Nummer '+n+' bitte zu Schalter 0! Du gehst zu Schalter 0. Schalter 0 gibt es nicht, aber ein Schild verkündet: "Gut gewartet! Sie bekommen Applaus." Alle Anwesenden applaudieren. Gewartet: '+G.waited+' Mal.',choices:[{label:'Verbeugen',a:'mclose'}]});
  return true;
 }
 if(p.indexOf('sg:')===0){
  const q=SG[+p.slice(3)];if(q){stampAdd(q[0]);showModal({title:'Gestempelt!',text:q[1],choices:[{label:'Noch ein Stempel',a:'skA',p:'sm'},{label:'Fertig',a:'mclose'}]});}
  return true;
 }
 if(p==='sm'){stempelMenu();return true;}
 if(p.indexOf('ax:')===0){
  const a=p.split(':'),d=AMD[a[1]];
  if(d){mood(4,'+Lacher');sfx('clap');showModal({title:d.n,text:d.a[+a[2]],choices:[{label:'Noch eine Frage',a:'skA',p:'ay:'+a[1]},{label:'Fertig',a:'mclose'}]});}
  return true;
 }
 if(p.indexOf('ay:')===0){amtMenu(p.slice(3));return true;}
 return false;
}
function drawBeamt(d){drawPerson(d.x,d.y,d.a,'#7a8494','ped',d.walk);const k=Math.abs(Math.sin(timeNow*6))*3;ctx.fillStyle='#8a5a3a';ctx.fillRect(d.x+Math.cos(d.a)*9-5,d.y+Math.sin(d.a)*9-5-k,10,10);ctx.fillStyle='#c0392b';ctx.fillRect(d.x+Math.cos(d.a)*9-4,d.y+Math.sin(d.a)*9-4-k,8,8);}
function drawForma(d){drawPerson(d.x,d.y,d.a,'#b08ad8','ped',d.walk);const w=Math.sin(timeNow*3+d.x)*2;for(let i=0;i<6;i++){ctx.fillStyle=i%2?'#f4f4f4':'#e8e0c8';ctx.fillRect(d.x+Math.cos(d.a)*10-7+w,d.y+Math.sin(d.a)*10-7-i*2.2,14,10);}ctx.strokeStyle='#d8c040';ctx.strokeRect(d.x+Math.cos(d.a)*10-7+w,d.y+Math.sin(d.a)*10-7-12,14,10);}
function drawOrdn(d){const s=Math.sin(timeNow*8+d.x)*1.2;ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(d.x-9,d.y-4,20,26);ctx.fillStyle='#2f4f9a';ctx.fillRect(d.x-10,d.y-14,20,26);ctx.fillStyle='#f4f4f4';ctx.fillRect(d.x-6,d.y-9,12,10);ctx.fillStyle='#bfc6d0';ctx.fillRect(d.x-1,d.y-14,2,5);ctx.fillRect(d.x-1,d.y+9,2,3);ctx.fillStyle='#111';ctx.fillRect(d.x-6,d.y+12+s,5,4);ctx.fillRect(d.x+2,d.y+12-s,5,4);ctx.fillStyle='#fff';ctx.fillRect(d.x-4,d.y-6,3,3);ctx.fillRect(d.x+1,d.y-6,3,3);}
function drawGnom(d){drawPerson(d.x,d.y,d.a,'#6a8a4a','ped',d.walk);ctx.fillStyle='#d8352f';ctx.beginPath();ctx.moveTo(d.x-6,d.y);ctx.lineTo(d.x,d.y-15);ctx.lineTo(d.x+6,d.y);ctx.closePath();ctx.fill();ctx.fillStyle='#f4f4f4';ctx.fillRect(d.x+Math.cos(d.a)*10-8,d.y+Math.sin(d.a)*10-5,16,10);ctx.fillStyle='#b8302f';ctx.fillRect(d.x+Math.cos(d.a)*10-6,d.y+Math.sin(d.a)*10-1,12,2);}
function ext18Update(dt){
 if(!G||!ZONE||ZONE.name!=='amt')return;
 const sp={beamt:12,forma:18,ordn:16,zgn:24},LN={beamt:['Gestempelt!','Moment, ich stempel das kurz.','Zuständig? Nein, aber trotzdem.'],forma:['Formulare, Formulare!','Haben Sie das ausgefüllt?','In dreifacher Ausfertigung!'],ordn:['Ich bin voll!','Bitte nicht lochen!','Klack, klack!'],zgn:['Nicht zuständig!','Dahinten!','Nebenan!']};
 skl().forEach(d=>{
  if(!sp[d.k])return;
  const dp=Math.hypot(P.x-d.x,P.y-d.y);
  leash(d,d.hx,d.hy,d.k==='zgn'?230:160);steerStep(d,dt,sp[d.k]);
  if(d.k==='forma'&&chance(dt*1.2))FX.push({x:d.x+rf(-8,8),y:d.y-12,vx:rf(-20,20),vy:rf(-30,-10),g:60,t:0,life:1,dot:'#f4f4f4',r:2});
  d.cd=(d.cd||0)-dt;
  if(d.cd<=0&&dp<320){d.cd=rf(6,11);addFx(d.x,d.y-26,pick(LN[d.k]),'#fff2b0',1.8);}
 });
}
function drawAmt(cx,cy){
 const z=ZONE;if(!z)return;
 (z.stamps||[]).forEach(s=>{
  if(s.x<cx-60||s.x>cx+VW+60||s.y<cy-30||s.y>cy+VH+30)return;
  ctx.save();ctx.translate(s.x,s.y);ctx.rotate(s.a);ctx.font='bold 8px Arial';const sw=ctx.measureText(s.t).width/2+6;ctx.strokeStyle='rgba(200,40,40,.8)';ctx.lineWidth=2;ctx.strokeRect(-sw,-8,sw*2,16);ctx.fillStyle='rgba(200,40,40,.85)';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(s.t,0,0);ctx.restore();
 });
 z.BLD.forEach(b=>{
  if(b.k!=='amt')return;
  const bx=(b.x+b.w/2)*TS,by=b.y*TS+(b.h*TS-b.hh)-38;
  if(bx<cx-180||bx>cx+VW+180||by<cy-40||by>cy+VH+40)return;
  ctx.fillStyle='#10131a';ctx.fillRect(bx-150,by,300,24);ctx.strokeStyle='#8a8f98';ctx.strokeRect(bx-150,by,300,24);
  const i=Math.floor(timeNow/3.2)%(AMB.length+1);
  const tx=i===AMB.length?(G.tk?'Ihre Nr. '+G.tk+': ca. in 4 Wochen':'Ziehen Sie eine Nummer. Oder nicht.'):AMB[i];
  ctx.font='bold 10px Arial';ctx.fillStyle='#ffb347';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(tx,bx,by+12);
 });
 for(let i=0;i<7;i++){
  const x=(17+i*2)*TS,y=15*TS;
  if(x<cx-30||x>cx+VW+30||y<cy-30||y>cy+VH+30)continue;
  ctx.fillStyle='#c9ced6';ctx.beginPath();ctx.arc(x,y,3,0,6.283);ctx.fill();
  if(i<6){ctx.strokeStyle='#c0392b';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x,y);ctx.quadraticCurveTo(x+TS,y+7,x+2*TS,y);ctx.stroke();ctx.lineWidth=1;}
 }
 AMS.forEach(q=>{
  const x=q[0]*TS,y=q[1]*TS;if(x<cx-90||x>cx+VW+90||y<cy-50||y>cy+VH+50)return;
  ctx.fillStyle='rgba(0,0,0,.28)';ctx.fillRect(x-42,y-18,92,42);
  ctx.fillStyle='#7a5a3a';ctx.fillRect(x-2,y+14,5,14);
  ctx.fillStyle='#f4efe0';ctx.fillRect(x-46,y-22,92,40);ctx.strokeStyle='#2b2f38';ctx.lineWidth=2;ctx.strokeRect(x-46,y-22,92,40);ctx.lineWidth=1;
  ctx.fillStyle='#b8302f';ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(q[2][0],x,y-10);
  ctx.fillStyle='#2b2f38';ctx.font='bold 7px Arial';ctx.fillText(q[2][1],x,y+4);
 });
 ctx.textAlign='start';ctx.textBaseline='alphabetic';
}

function circ2(c,x,y,r){c.beginPath();c.arc(x,y,r,0,6.283);c.fill();}
function bsPts(){const F=SPF.bs,H={x:(F.x0+F.x1)/2,y:F.y1-48},d=84;return{H:H,B1:{x:H.x+d,y:H.y-d},B2:{x:H.x,y:H.y-2*d},B3:{x:H.x-d,y:H.y-d},M:{x:H.x,y:H.y-d+8}};}
function spCenter(k){const F=SPF[k];return{x:(F.x0+F.x1)/2,y:(F.y0+F.y1)/2};}
function spNight(){if(!G)return false;const h=hour();return h>=21||h<7;}
function spPl(t,role,x,y,f){return{t:t,role:role,x:x,y:y,hx:x,hy:y,a:t?Math.PI:0,walk:rf(0,6),cd:rf(0,1),sp:rf(70,92),col:role==='gk'?(t?'#2fbf4f':'#f4d03f'):f.cols[t],i:0};}
function spInit(){
 SP={fb:{pl:[],ball:{x:0,y:0,vx:0,vy:0,z:0},sc:[0,0],cel:0,reset:0,roll:0,occ:0,jung:false,cols:TEAMC[0]},
  bb:{pl:[],ball:{x:0,y:0,z:0},sc:[0,0],roll:0,occ:0,jung:false,cols:TEAMC[1],st:'play',hold:null,shot:null,tm:0,atk:0},
  bs:{pl:[],ball:{x:0,y:0,z:0},runs:0,roll:0,occ:0,jung:false,cols:TEAMC[2],st:'wind',tm:0}};
 ['fb','bb','bs'].forEach(k=>spRoll(k));
}
function fbBallReset(){const f=SP.fb,c=spCenter('fb');f.ball.x=c.x;f.ball.y=c.y;f.ball.vx=0;f.ball.vy=0;f.ball.z=0;}
function spRoll(k){
 const f=SP[k],F=SPF[k];
 f.occ=chance(spNight()?.2:.72)?1:0;f.jung=chance(.35);f.cols=pick(TEAMC);f.pl=[];f.roll=rf(90,170);
 if(k==='fb'){
  f.sc=[0,0];f.cel=0;f.reset=0;fbBallReset();
  if(f.occ){const n=rnd(3,5),FM={3:[[.3,.3],[.3,.7],[.6,.5]],4:[[.25,.3],[.25,.7],[.55,.35],[.55,.65]],5:[[.22,.25],[.22,.75],[.45,.5],[.65,.3],[.65,.7]]}[n];
   for(let t=0;t<2;t++){f.pl.push(spPl(t,'gk',t?F.x1-14:F.x0+14,(F.y0+F.y1)/2,f));FM.forEach(q=>{const x=t?F.x1-q[0]*(F.x1-F.x0):F.x0+q[0]*(F.x1-F.x0),y=F.y0+q[1]*(F.y1-F.y0);f.pl.push(spPl(t,'f',x,y,f));});}}
 }else if(k==='bb'){
  f.sc=[0,0];f.st='play';f.shot=null;f.hold=null;f.tm=0;
  const c=spCenter('bb');f.ball.x=c.x;f.ball.y=c.y;f.ball.z=0;
  if(f.occ){const n=rnd(1,3);for(let t=0;t<2;t++)for(let i=0;i<n;i++){const p=spPl(t,'f',rf(F.x0+30,F.x1-30),rf(F.y0+70,F.y1-70),f);p.i=i;f.pl.push(p);}f.hold=pick(f.pl);f.atk=f.hold.t;}
 }else{
  f.runs=0;f.st='wind';f.tm=rf(1,2);f.fly=null;f.run=null;const B=bsPts();f.ball.x=B.M.x;f.ball.y=B.M.y;f.ball.z=0;
  if(f.occ){
   [['pit',B.M.x,B.M.y],['cat',B.H.x,B.H.y+18],['b1',B.B1.x+10,B.B1.y-8],['ss',B.H.x-48,B.H.y-128],['b2',B.H.x+48,B.H.y-128],['lf',B.H.x-120,F.y0+34],['cf',B.H.x,F.y0+24],['rf',B.H.x+120,F.y0+34]].forEach(q=>f.pl.push(spPl(0,q[0],q[1],q[2],f)));
   f.pl.push(spPl(1,'bat',B.H.x-16,B.H.y+2,f));
  }
 }
 f.pl.forEach(p=>{p.jung=f.jung;if(k!=='fb')p.col=f.cols[p.t];});
}
function spTick(dt){
 if(ZONE||!SP)return;
 cityWA+=dt*.28;cityRT-=dt;if(cityRT<=0){cityRT=rf(10,20);const k=rnd(0,7);cityRid[k]=cityRid[k]?0:1;}
 ['fb','bb','bs'].forEach(k=>{
  const f=SP[k],c=spCenter(k),d=Math.hypot(P.x-c.x,P.y-c.y);
  f.roll-=dt;if(f.roll<=0){if(d>760&&!(MG&&MG.f===k))spRoll(k);else f.roll=15;}
  if(MG&&MG.f===k)return;
  if(d>1400)return;
  if(k==='fb')fbTick(f,dt);else if(k==='bb')bbTick(f,dt);else bsTick(f,dt);
 });
}
function fbTick(f,dt){
 const F=SPF.fb,b=f.ball,mx=(F.x0+F.x1)/2,my=(F.y0+F.y1)/2;
 if(f.cel>0)f.cel-=dt;
 if(f.reset>0){f.reset-=dt;if(f.reset<=0)fbBallReset();}
 else{
  b.x+=b.vx*dt;b.y+=b.vy*dt;const k=Math.exp(-1.05*dt);b.vx*=k;b.vy*=k;b.rot=(b.rot||0)+Math.hypot(b.vx,b.vy)*dt*.08;
  if(b.y>F.gy0&&b.y<F.gy1&&(b.x<F.x0+3||b.x>F.x1-3))fbGoal(b.x<mx?1:0);
  else{
   if(b.x<F.x0+5){b.x=F.x0+5;b.vx=Math.abs(b.vx)*.55;}if(b.x>F.x1-5){b.x=F.x1-5;b.vx=-Math.abs(b.vx)*.55;}
   if(b.y<F.y0+5){b.y=F.y0+5;b.vy=Math.abs(b.vy)*.55;}if(b.y>F.y1-5){b.y=F.y1-5;b.vy=-Math.abs(b.vy)*.55;}
  }
 }
 if(G&&!P.inCar&&!P.ride&&!P.sit&&!P.coast&&!MG&&f.reset<=0){
  f.pcd=(f.pcd||0)-dt;const d=Math.hypot(P.x-b.x,P.y-b.y),s=Math.hypot(P.vx,P.vy);
  if(d<14&&s>25&&f.pcd<=0){const a=Math.atan2(P.vy,P.vx)+rf(-.1,.1),v=s*2.4+70;b.vx=Math.cos(a)*v;b.vy=Math.sin(a)*v;b.last='P';f.pcd=.35;sfx('roll');}
 }
 if(!f.occ)return;
 const nr=[null,null],nd=[1e9,1e9];
 f.pl.forEach(p=>{if(p.role==='gk')return;const d=Math.hypot(p.x-b.x,p.y-b.y);if(d<nd[p.t]){nd[p.t]=d;nr[p.t]=p;}});
 f.pl.forEach(p=>{
  p.cd-=dt;
  if(f.cel>0){p.walk+=dt*12;return;}
  let tx,ty,sp;
  if(p.role==='gk'){tx=p.t?F.x1-14:F.x0+14;ty=clamp(b.y,F.gy0+8,F.gy1-8);sp=62;}
  else if(p===nr[p.t]&&f.reset<=0){tx=b.x+(p.t?8:-8);ty=b.y;sp=p.sp;}
  else{tx=clamp(p.hx+(b.x-mx)*.45,F.x0+20,F.x1-20);ty=clamp(p.hy+(b.y-my)*.3,F.y0+16,F.y1-16);sp=p.sp*.6;}
  const dx=tx-p.x,dy=ty-p.y,d=Math.hypot(dx,dy);
  if(d>2){const s=Math.min(d,sp*dt);p.x+=dx/d*s;p.y+=dy/d*s;p.a=Math.atan2(dy,dx);p.walk+=s*.16;}
  else p.a=Math.atan2(b.y-p.y,b.x-p.x);
  if(f.reset<=0&&p.cd<=0&&Math.hypot(p.x-b.x,p.y-b.y)<12){
   p.cd=.55;let a,v;
   const mates=f.pl.filter(q=>q.t===p.t&&q!==p&&q.role!=='gk');
   const gx=p.t?F.x0:F.x1,gd=Math.hypot(gx-b.x,my-b.y);
   if(p.role==='gk'){a=Math.atan2(my+rf(-80,80)-b.y,(p.t?F.x0:F.x1)-b.x);v=rf(230,300);}
   else if(gd<170){a=Math.atan2(my+rf(-56,56)-b.y,gx-b.x)+rf(-.15,.15);v=rf(230,320);}
   else if(mates.length&&chance(.25)){const m=pick(mates);a=Math.atan2(m.y-b.y,m.x-b.x);v=rf(150,200);}
   else{a=Math.atan2(my+rf(-40,40)-b.y,gx-b.x)+rf(-.5,.5);v=rf(85,125);}
   b.vx=Math.cos(a)*v;b.vy=Math.sin(a)*v;b.last=p.t;
  }
 });
}
function fbGoal(t){
 const f=SP.fb,b=f.ball,near=Math.hypot(P.x-b.x,P.y-b.y)<700;
 b.vx=0;b.vy=0;f.reset=1.6;
 if(b.last==='P'&&G){
  G.tore=(G.tore||0)+1;mood(6,'TOR!');addFx(b.x,b.y-24,'TOOOR!','#ffd23f',2);sfx('win');
  if(G.tore===10)toast('Zehn Tore im Sportpark! Du bist jetzt Ehrenmitglied im SV Rheinhanfen.');
  else if(f.occ)toast(pick(['Tor! Beide Teams jubeln. Wem es zählt, ist allen egal.','Tooor! Der Torwart schaut ungläubig ins Netz.','Ein Kunstschuss! Sogar die Tauben am Zaun klatschen.']));
  return;
 }
 if(f.occ){f.sc[t]++;f.cel=1.4;if(near&&G){addFx(b.x,b.y-24,'TOOOR!','#ffd23f',1.8);sfx('clap');}}
}
function bbSpot(t){const F=SPF.bb,hx=(F.x0+F.x1)/2,H=t?F.y1-22:F.y0+22,a=rf(.3,2.84),r=rf(55,120);return{x:clamp(hx+Math.cos(a)*r,F.x0+14,F.x1-14),y:H+(t?-1:1)*Math.abs(Math.sin(a))*r};}
function bbTick(f,dt){
 if(!f.occ)return;
 const F=SPF.bb,hx=(F.x0+F.x1)/2,HY=[F.y0+22,F.y1-22],b=f.ball;
 f.tm+=dt;
 const atk=f.hold?f.hold.t:f.atk;
 f.pl.forEach(p=>{
  p.cd-=dt;let tx=p.x,ty=p.y,sp=p.sp*.75;
  if(f.st==='reb'&&f.reb){tx=f.reb.x;ty=f.reb.y;sp=p.sp;}
  else if(p===f.hold){if(!p.spot)p.spot=bbSpot(p.t);tx=p.spot.x;ty=p.spot.y;sp=p.sp*.6;}
  else if(p.t===atk){if(!p.spot||p.cd<=0){p.cd=rf(1.4,3);p.spot=bbSpot(p.t);}tx=p.spot.x;ty=p.spot.y;}
  else{const m=f.pl.find(q=>q.t===atk&&q.i===p.i)||f.hold;if(m){tx=m.x+(hx-m.x)*.3;ty=m.y+(HY[atk]-m.y)*.3;}sp=p.sp*.85;}
  const dx=tx-p.x,dy=ty-p.y,d=Math.hypot(dx,dy);
  if(d>2){const s=Math.min(d,sp*dt);p.x+=dx/d*s;p.y+=dy/d*s;p.a=Math.atan2(dy,dx);p.walk+=s*.16;}
 });
 if(f.st==='play'&&f.hold){
  const h=f.hold;b.x=h.x+Math.cos(h.a)*7;b.y=h.y+Math.sin(h.a)*7;b.z=Math.abs(Math.sin(f.tm*9))*7;
  if(f.tm>2.2&&((h.spot&&Math.hypot(h.x-h.spot.x,h.y-h.spot.y)<8)||f.tm>4.5)){
   f.st='shot';f.atk=h.t;f.shot={sx:b.x,sy:b.y,tx:hx,ty:HY[h.t],t:0,make:chance(.5),by:h};f.hold=null;f.tm=0;h.spot=null;
  }
 }else if(f.st==='shot'){
  const s=f.shot;s.t+=dt;const k=Math.min(1,s.t/.85);
  b.x=s.sx+(s.tx-s.sx)*k;b.y=s.sy+(s.ty-s.sy)*k;b.z=Math.sin(Math.PI*k)*46+k*10;
  if(k>=1){
   const near=G&&Math.hypot(P.x-b.x,P.y-b.y)<600;
   if(s.make){f.sc[s.by.t]+=2;if(near){addFx(s.tx,s.ty-26,pick(['Korb!','Swish!','Zwei Punkte!']),'#ffd23f',1.4);sfx('clap');}
    const o=f.pl.filter(q=>q.t!==s.by.t);f.hold=o.length?pick(o):s.by;f.hold.spot=null;f.atk=f.hold.t;f.st='play';f.tm=0;}
   else{if(near)addFx(s.tx,s.ty-26,pick(['Ring!','Daneben!','Klonk!']),'#cfd6e0',1.2);
    f.st='reb';f.reb={x:clamp(s.tx+rf(-60,60),F.x0+16,F.x1-16),y:s.ty+(s.by.t?-1:1)*rf(30,80)};f.rt=0;f.rsx=b.x;f.rsy=b.y;}
  }
 }else if(f.st==='reb'){
  f.rt+=dt;const k=Math.min(1,f.rt/.5);b.x=f.rsx+(f.reb.x-f.rsx)*k;b.y=f.rsy+(f.reb.y-f.rsy)*k;b.z=Math.sin(Math.PI*k)*16;
  if(k>=1){let best=null,bd=1e9;f.pl.forEach(p=>{const d=Math.hypot(p.x-b.x,p.y-b.y);if(d<bd){bd=d;best=p;}});if(best&&(bd<14||f.rt>2.5)){f.hold=best;best.spot=null;f.atk=best.t;f.st='play';f.tm=0;}}
 }
}
function bsTick(f,dt){
 if(!f.occ)return;
 const F=SPF.bs,B=bsPts(),b=f.ball;
 f.tm-=dt;
 const pit=f.pl.find(p=>p.role==='pit'),bat=f.pl.find(p=>p.role==='bat');
 if(!pit||!bat)return;
 const near=G&&Math.hypot(P.x-B.H.x,P.y-B.H.y)<650;
 f.pl.forEach(p=>{
  let tx=p.hx,ty=p.hy,sp=p.sp*.8;
  if(f.fly&&p===f.fly.ch){tx=f.fly.tx;ty=f.fly.ty;sp=p.sp*1.1;}
  if(p===bat&&f.run){tx=f.run.pts[f.run.i].x;ty=f.run.pts[f.run.i].y;sp=115;}
  const dx=tx-p.x,dy=ty-p.y,d=Math.hypot(dx,dy);
  if(d>2){const s=Math.min(d,sp*dt);p.x+=dx/d*s;p.y+=dy/d*s;p.a=Math.atan2(dy,dx);p.walk+=s*.16;}
  else{if(p!==bat)p.a=Math.atan2(b.y-p.y,b.x-p.x);else p.a=-Math.PI/2;if(p===bat&&f.run){f.run.i++;if(f.run.i>=f.run.pts.length)f.run=null;}}
 });
 if(f.st==='wind'){b.x=pit.x;b.y=pit.y-4;b.z=8;if(f.tm<=0){f.st='pitch';f.tm=.55;}}
 else if(f.st==='pitch'){
  const k=1-Math.max(0,f.tm)/.55;b.x=pit.x+(B.H.x-pit.x)*k;b.y=pit.y+(B.H.y-pit.y)*k;b.z=8;
  if(f.tm<=0){
   const r=Math.random();
   if(r<.45||f.run){f.st='back';f.tm=.6;if(near)addFx(B.H.x,B.H.y-26,pick(['Strike!','Ball!','Strike zwei!','Vorbeigeschwungen!']),'#ffffff',1.1);}
   else if(r<.8){
    const T={x:rf(F.x0+30,F.x1-30),y:rf(F.y0+18,B.B2.y-10)};f.fly={sx:B.H.x,sy:B.H.y,tx:T.x,ty:T.y,t:0,dur:1.1,h:60};
    let ch=null,cd=1e9;f.pl.forEach(p=>{if(['lf','cf','rf','ss','b2'].indexOf(p.role)<0)return;const d=Math.hypot(p.x-T.x,p.y-T.y);if(d<cd){cd=d;ch=p;}});f.fly.ch=ch;
    f.st='hitf';f.run={pts:[B.B1,{x:bat.hx,y:bat.hy}],i:0};if(near){addFx(B.H.x,B.H.y-28,'Klack!','#ffd23f',1);sfx('bonk');}
   }else if(r<.9){f.st='hitf';f.fly={sx:B.H.x,sy:B.H.y,tx:B.H.x+(chance(.5)?-1:1)*rf(150,220),ty:B.H.y+rf(-40,10),t:0,dur:.8,h:40,foul:1};if(near)addFx(B.H.x,B.H.y-28,'Foul!','#cfd6e0',1.1);}
   else{f.st='hitf';f.fly={sx:B.H.x,sy:B.H.y,tx:B.H.x+rf(-80,80),ty:F.y0-80,t:0,dur:1.5,h:110,hr:1};f.runs++;f.run={pts:[B.B1,B.B2,B.B3,B.H,{x:bat.hx,y:bat.hy}],i:0};if(near){addFx(B.H.x,B.H.y-30,'HOME RUN!','#ffd23f',2);sfx('win');}}
  }
 }else if(f.st==='back'){const k=1-Math.max(0,f.tm)/.6;b.x=B.H.x+(pit.x-B.H.x)*k;b.y=B.H.y+(pit.y-B.H.y)*k;b.z=Math.sin(Math.PI*k)*18;if(f.tm<=0){f.st='wind';f.tm=rf(1.2,2.2);}}
 else if(f.st==='hitf'){
  const y=f.fly;y.t+=dt;const k=Math.min(1,y.t/y.dur);b.x=y.sx+(y.tx-y.sx)*k;b.y=y.sy+(y.ty-y.sy)*k;b.z=Math.sin(Math.PI*k)*y.h;
  if(k>=1){
   if(y.hr||y.foul){f.fly=null;f.st='wind';f.tm=y.hr?3.5:1.5;}
   else{const c=y.ch;if(c&&Math.hypot(c.x-y.tx,c.y-y.ty)<16&&near)addFx(c.x,c.y-24,'Gefangen!','#7bd86a',1.2);f.st='ret';f.tm=.7;f.rs={x:b.x,y:b.y};}
  }
 }else if(f.st==='ret'){const k=1-Math.max(0,f.tm)/.7;b.x=f.rs.x+(pit.x-f.rs.x)*k;b.y=f.rs.y+(pit.y-f.rs.y)*k;b.z=Math.sin(Math.PI*k)*30;if(f.tm<=0){f.fly=null;f.st='wind';f.tm=rf(1.5,2.5);}}
}
function drawSpBall(k,b){
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(b.x+2,b.y+3,k==='bs'?3:5,k==='bs'?2:3,0,0,6.283);ctx.fill();
 const y=b.y-(b.z||0);
 if(k==='fb'){ctx.fillStyle='#fff';circle(b.x,y,5);ctx.fillStyle='#222';const r=b.rot||0;circle(b.x+Math.cos(r)*2.2,y+Math.sin(r)*2.2,1.6);circle(b.x+Math.cos(r+2.1)*2.6,y+Math.sin(r+2.1)*2.6,1.2);circle(b.x+Math.cos(r+4.2)*2.6,y+Math.sin(r+4.2)*2.6,1.2);}
 else if(k==='bb'){ctx.fillStyle='#e0702a';circle(b.x,y,5.5);ctx.strokeStyle='#5a2a10';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(b.x-5.5,y);ctx.lineTo(b.x+5.5,y);ctx.moveTo(b.x,y-5.5);ctx.lineTo(b.x,y+5.5);ctx.stroke();}
 else{ctx.fillStyle='#fff';circle(b.x,y,3.4);ctx.strokeStyle='#e5504d';ctx.lineWidth=1;ctx.beginPath();ctx.arc(b.x-1,y,2,-.8,.8);ctx.stroke();}
}
function drawScore(x,y,txt,cols){
 ctx.font='bold 11px Arial';const w=ctx.measureText(txt).width+30;
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(x-w/2+3,y+3,w,18);ctx.fillStyle='#1a1d24';ctx.fillRect(x-w/2,y,w,18);
 ctx.fillStyle=cols[0];ctx.fillRect(x-w/2+3,y+4,8,10);ctx.fillStyle=cols[1];ctx.fillRect(x+w/2-11,y+4,8,10);
 ctx.fillStyle='#ffd23f';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,x,y+9.5);ctx.textAlign='start';ctx.textBaseline='alphabetic';
}
function drawWheel(x,y,R,a,rid){
 ctx.strokeStyle='#d8dde6';ctx.lineWidth=3;ctx.beginPath();ctx.arc(x,y,R,0,6.283);ctx.stroke();
 ctx.strokeStyle='#ff8fc8';ctx.lineWidth=2;ctx.beginPath();ctx.arc(x,y,R-7,0,6.283);ctx.stroke();
 ctx.strokeStyle='rgba(220,226,236,.85)';ctx.lineWidth=1.5;ctx.beginPath();
 for(let k=0;k<8;k++){const q=a+k*.7854;ctx.moveTo(x,y);ctx.lineTo(x+Math.cos(q)*R,y+Math.sin(q)*R);}ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='#ffd23f';circle(x,y,6);ctx.fillStyle='#e5504d';circle(x,y,2.5);
 const GC=['#e5504d','#2e86c1','#f1c40f','#27ae60','#8e44ad','#ff9a3c','#16a085','#ff5fd0'];
 for(let k=0;k<8;k++){const q=a+k*.7854,gx=x+Math.cos(q)*R,gy=y+Math.sin(q)*R;
  ctx.strokeStyle='#9aa0a8';ctx.beginPath();ctx.moveTo(gx,gy);ctx.lineTo(gx,gy+6);ctx.stroke();
  ctx.fillStyle=GC[k];ctx.fillRect(gx-8,gy+6,16,11);ctx.fillStyle='rgba(255,255,255,.4)';ctx.fillRect(gx-8,gy+6,16,3);
  if(rid&&rid[k]){ctx.fillStyle='#e8c39e';circle(gx-3,gy+11,2.4);circle(gx+3,gy+11,2.4);}}
}
function drawCityExtra(cx,cy){
 if(!SP)return;
 const iv=(x0,y0,x1,y1)=>x1>cx-40&&x0<cx+VW+40&&y1>cy-60&&y0<cy+VH+60;
 const R=SPF.rad;
 if(iv(R.x-R.R-20,R.y-R.R-20,R.x+R.R+20,R.y+R.R+40))drawWheel(R.x,R.y,R.R,cityWA,cityRid);
 ['fb','bb','bs'].forEach(k=>{
  const F=SPF[k],f=SP[k];
  if(!iv(F.x0,F.y0-40,F.x1,F.y1))return;
  const mgHere=MG&&MG.f===k;
  f.pl.forEach(p=>{if(mgHere&&(p.role==='bat'||(k==='fb'&&p.role==='gk'&&p.t===1)))return;const j=(k==='fb'&&f.cel>0)?-Math.abs(Math.sin(timeNow*10+p.x))*5:0;drawPerson(p.x,p.y+j,p.a,p.col,'ped',p.walk,p.jung?.74:.9);});
  if(!mgHere)drawSpBall(k,f.ball);
  if(f.occ){
   if(k==='fb')drawScore(F.x0+70,F.y0-30,(f.jung?'JUGEND  ':'')+f.sc[0]+' : '+f.sc[1],f.cols);
   else if(k==='bb')drawScore(F.x1-10,F.y0-30,f.sc[0]+' : '+f.sc[1],f.cols);
   else drawScore(F.x0+80,F.y0-30,'LÄUFE '+f.runs,f.cols);
  }
 });
 if(MG)drawMGWorld();
}
function drawSportsStatic(c){
 const L=(x0,y0,x1,y1)=>{c.beginPath();c.moveTo(x0,y0);c.lineTo(x1,y1);c.stroke();};
 let F=SPF.fb;const mx=(F.x0+F.x1)/2,my=(F.y0+F.y1)/2;
 for(let x=F.x0;x<F.x1;x+=32){c.fillStyle=((x-F.x0)/32)%2?'#4f8f3f':'#57a047';c.fillRect(x,F.y0,32,F.y1-F.y0);}
 c.strokeStyle='rgba(255,255,255,.85)';c.lineWidth=2;
 c.strokeRect(F.x0+4,F.y0+4,F.x1-F.x0-8,F.y1-F.y0-8);L(mx,F.y0+4,mx,F.y1-4);c.beginPath();c.arc(mx,my,38,0,6.283);c.stroke();
 c.strokeRect(F.x0+4,my-70,58,140);c.strokeRect(F.x1-62,my-70,58,140);
 c.fillStyle='#fff';circ2(c,mx,my,2.5);circ2(c,F.x0+44,my,2);circ2(c,F.x1-44,my,2);
 [F.x0-2,F.x1-10].forEach(gx=>{c.fillStyle='rgba(255,255,255,.18)';c.fillRect(gx,F.gy0,12,F.gy1-F.gy0);c.strokeStyle='rgba(255,255,255,.45)';c.lineWidth=1;for(let y=F.gy0;y<=F.gy1;y+=6)L(gx,y,gx+12,y);for(let x=gx;x<=gx+12;x+=4)L(x,F.gy0,x,F.gy1);c.strokeStyle='#fff';c.lineWidth=3;c.strokeRect(gx,F.gy0,12,F.gy1-F.gy0);});
 F=SPF.bb;const hx=(F.x0+F.x1)/2,hm=(F.y0+F.y1)/2;
 c.fillStyle='#b8573a';c.fillRect(F.x0,F.y0,F.x1-F.x0,F.y1-F.y0);
 c.fillStyle='#2f6fb5';c.fillRect(hx-40,F.y0+4,80,96);c.fillRect(hx-40,F.y1-100,80,96);
 c.strokeStyle='#fff';c.lineWidth=2;c.strokeRect(F.x0+4,F.y0+4,F.x1-F.x0-8,F.y1-F.y0-8);
 L(F.x0+4,hm,F.x1-4,hm);c.beginPath();c.arc(hx,hm,30,0,6.283);c.stroke();
 c.strokeRect(hx-40,F.y0+4,80,96);c.strokeRect(hx-40,F.y1-100,80,96);
 c.beginPath();c.arc(hx,F.y0+100,28,0,Math.PI);c.stroke();c.beginPath();c.arc(hx,F.y1-100,28,Math.PI,6.283);c.stroke();
 c.beginPath();c.arc(hx,F.y0+22,112,.12,Math.PI-.12);c.stroke();c.beginPath();c.arc(hx,F.y1-22,112,Math.PI+.12,6.283-.12);c.stroke();
 [[F.y0+8,1],[F.y1-8,-1]].forEach(q=>{c.fillStyle='rgba(0,0,0,.3)';c.fillRect(hx-20,q[0]-1,44,6);c.fillStyle='#f4f6f8';c.fillRect(hx-22,q[0]-3,44,6);c.strokeStyle='#ff7a1a';c.lineWidth=3;c.beginPath();c.arc(hx,q[0]+q[1]*14,9,0,6.283);c.stroke();c.strokeStyle='rgba(255,255,255,.75)';c.lineWidth=1;for(let k=-6;k<=6;k+=3)L(hx+k,q[0]+q[1]*14,hx+k*.6,q[0]+q[1]*24);});
 F=SPF.bs;const B=bsPts();
 for(let y=F.y0;y<F.y1;y+=32){c.fillStyle=((y-F.y0)/32)%2?'#4f8f3f':'#57a047';c.fillRect(F.x0,y,F.x1-F.x0,32);}
 c.fillStyle='#c9a46a';c.beginPath();c.moveTo(B.H.x,B.H.y+26);c.lineTo(B.B1.x+26,B.B1.y);c.lineTo(B.B2.x,B.B2.y-26);c.lineTo(B.B3.x-26,B.B3.y);c.closePath();c.fill();
 c.fillStyle='#57a047';c.beginPath();c.moveTo(B.H.x,B.H.y-24);c.lineTo(B.B1.x-24,B.B1.y);c.lineTo(B.B2.x,B.B2.y+24);c.lineTo(B.B3.x+24,B.B3.y);c.closePath();c.fill();
 c.fillStyle='#c9a46a';circ2(c,B.M.x,B.M.y,12);circ2(c,B.H.x,B.H.y,16);
 c.strokeStyle='#fff';c.lineWidth=2;L(B.H.x,B.H.y,B.H.x+185,B.H.y-185);L(B.H.x,B.H.y,B.H.x-185,B.H.y-185);
 c.fillStyle='#fff';[B.B1,B.B2,B.B3].forEach(p=>{c.save();c.translate(p.x,p.y);c.rotate(.785);c.fillRect(-5,-5,10,10);c.restore();});
 c.beginPath();c.moveTo(B.H.x-5,B.H.y-4);c.lineTo(B.H.x+5,B.H.y-4);c.lineTo(B.H.x+5,B.H.y+2);c.lineTo(B.H.x,B.H.y+6);c.lineTo(B.H.x-5,B.H.y+2);c.closePath();c.fill();
 c.fillRect(B.M.x-5,B.M.y-1,10,3);
 c.lineWidth=1.5;c.strokeRect(B.H.x-26,B.H.y-10,14,22);c.strokeRect(B.H.x+12,B.H.y-10,14,22);
 const R=SPF.rad,gy=56.5*TS;
 c.strokeStyle='#8a929c';c.lineWidth=5;L(R.x,R.y,R.x-64,gy);L(R.x,R.y,R.x+64,gy);c.lineWidth=2;L(R.x-46,gy-26,R.x+46,gy-26);
 c.fillStyle='#5a6470';c.fillRect(R.x-74,gy-3,148,8);c.fillStyle='#e8d8a8';c.fillRect(R.x-18,R.y+R.R+12,36,8);
 c.lineWidth=1;
}
function spMini(mc,S){
 mc.fillStyle='#57a047';[SPF.fb,SPF.bs].forEach(F=>mc.fillRect(F.x0/TS*S,F.y0/TS*S,(F.x1-F.x0)/TS*S,(F.y1-F.y0)/TS*S));
 const F=SPF.bb;mc.fillStyle='#b8573a';mc.fillRect(F.x0/TS*S,F.y0/TS*S,(F.x1-F.x0)/TS*S,(F.y1-F.y0)/TS*S);
 mc.fillStyle='#ff8fc8';mc.fillRect(64*S,49*S,8*S,8*S);
}
function sportMenu(k){
 if(!SP)return;const f=SP[k];
 if(k==='fb')mdl('Fußballplatz',f.occ?((f.jung?'Die Jugendmannschaften':pick(['Zwei Hobbyteams','Die Alten Herren','Ein Betriebsteam und der Kegelclub']))+' kicken gerade. Spielstand '+f.sc[0]+' : '+f.sc[1]+'. Der Ball gehört allen: Lauf einfach rein und schieß!'):'Der Platz ist gerade frei. Der Ball liegt am Anstoßpunkt. Lauf einfach dagegen, oder übe Elfmeter.',[['Elfmeterschießen (5 Schuss)','sp:elf'],f.occ?['Anfeuern','sp:cheer:fb']:['Meine Tore ansehen','sp:rek']]);
 else if(k==='bb'){const n=f.pl.length/2;mdl('Basketballplatz',f.occ?('Hier läuft gerade '+n+' gegen '+n+(f.jung?' mit der Jugend':'')+', Stand '+f.sc[0]+' : '+f.sc[1]+'. In der Pause darfst du an die Freiwurflinie.'):'Der Korb ist frei. Zeit für ein paar Freiwürfe.',[['Freiwürfe werfen (5 Bälle)','sp:frei'],f.occ?['Anfeuern','sp:cheer:bb']:['Meine Bilanz ansehen','sp:rek']]);}
 else mdl('Baseballfeld',f.occ?((f.jung?'Die Jugend':'Der Baseballclub Rhein-Eagles')+' trainiert. Läufe bisher: '+f.runs+'. Der Schlagmann macht dir gern kurz Platz.'):'Das Feld ist leer. An der Wurfmaschine kannst du Schlagtraining machen.',[['Schlagtraining (6 Bälle)','sp:schlag'],f.occ?['Anfeuern','sp:cheer:bs']:['Meine Bilanz ansehen','sp:rek']]);
}
function mgStart(k){
 if(MG||P.inCar||P.ride||P.sit||P.coast||ZONE||!SP)return;
 closeAll();
 const f=k==='elf'?'fb':k==='frei'?'bb':'bs',F=SPF[f];
 MG={k:k,f:f,i:0,n:k==='schlag'?6:5,hits:0,hr:0,ph:'aim',t:0,age:0,res:'',rc:'#fff',bx:0,by:0,bz:0,m:0};
 if(k==='elf'){P.x=F.x1-2.9*TS;P.y=(F.gy0+F.gy1)/2;P.a=0;MG.kx=F.x1-12;}
 else if(k==='frei'){P.x=(F.x0+F.x1)/2;P.y=F.y0+22+112;P.a=-Math.PI/2;}
 else{const B=bsPts();P.x=B.H.x-16;P.y=B.H.y+2;P.a=-Math.PI/2;}
 P.vx=0;P.vy=0;keys.left=keys.right=keys.up=keys.down=0;
 mgReset();sfx('ok');
 toast(k==='elf'?'Elfmeterschießen! Der gelbe Kreis wandert vor dem Tor hin und her. OK schießt.':k==='frei'?'Freiwürfe! Drück OK, wenn der Kraftbalken im grünen Feld steht.':'Schlagtraining! Drück OK, wenn der Ball im grünen Schlagfeld ist.');
}
function mgReset(){
 const F=SPF[MG.f];MG.t=0;MG.res='';
 if(MG.k==='elf'){MG.ph='aim';MG.bx=P.x+12;MG.by=P.y;MG.bz=0;MG.ky=(F.gy0+F.gy1)/2;MG.kt=MG.ky;}
 else if(MG.k==='frei'){MG.ph='aim';MG.bx=P.x;MG.by=P.y-10;MG.bz=10;}
 else{MG.ph='wind';const B=bsPts();MG.bx=B.M.x;MG.by=B.M.y-4;MG.bz=8;MG.m=0;}
}
function mgPrompt(){if(!MG)return '';if(MG.ph==='aim')return MG.k==='elf'?'OK: Schießen!':'OK: Werfen!';if(MG.ph==='pitch')return 'OK: Schlagen!';if(MG.ph==='wind')return 'Achtung, der Ball kommt ...';return '';}
function mgPress(){
 if(!MG)return;const F=SPF[MG.f];
 if(MG.k==='elf'&&MG.ph==='aim'){
  const y=MG.aim,kd=rnd(-1,1),kt=(F.gy0+F.gy1)/2+kd*(F.gy1-F.gy0)/3;
  MG.kt=kt;MG.sx=MG.bx;MG.sy=MG.by;MG.tx=F.x1-6;MG.ty=y;
  MG.res=(y<F.gy0+5||y>F.gy1-5)?'Daneben!':Math.abs(y-kt)<20?'Gehalten!':'TOR!';
  if(MG.res==='Daneben!')MG.tx=F.x1+10;
  MG.ph='fly';MG.t=0;sfx('bonk');
 }else if(MG.k==='frei'&&MG.ph==='aim'){
  const m=MG.m;let r;
  if(m>=.4&&m<=.6)r=pick(['Swish!','Korb!','Nichts als Netz!']);
  else if(m>=.3&&m<=.7)r=chance(.5)?'Ring ... und rein!':'Ring ... und raus!';
  else r=m<.3?'Zu kurz!':'Zu weit!';
  MG.res=r;MG.sx=MG.bx;MG.sy=MG.by;MG.tx=(F.x0+F.x1)/2;MG.ty=F.y0+22+(r==='Zu kurz!'?34:r==='Zu weit!'?-26:0);
  MG.ph='fly';MG.t=0;sfx('swish');
 }else if(MG.k==='schlag'&&MG.ph==='pitch'){
  const p=MG.t/MG.dur,e=Math.abs(p-.9),B=bsPts();
  MG.res=e<.035?'HOME RUN!':e<.09?'Treffer!':e<.15?'Foul!':'Strike!';
  MG.sx=MG.bx;MG.sy=MG.by;MG.ph='fly';MG.t=0;
  if(MG.res==='HOME RUN!'){MG.tx=B.H.x+rf(-60,60);MG.ty=F.y0-90;MG.fd=1.5;MG.fh=110;sfx('bonk');}
  else if(MG.res==='Treffer!'){MG.tx=rf(F.x0+30,F.x1-30);MG.ty=rf(F.y0+20,B.B2.y-10);MG.fd=1.1;MG.fh=60;sfx('bonk');}
  else if(MG.res==='Foul!'){MG.tx=B.H.x+(chance(.5)?-1:1)*rf(160,220);MG.ty=B.H.y+rf(-30,20);MG.fd=.8;MG.fh=40;sfx('bonk');}
  else{MG.tx=B.H.x;MG.ty=B.H.y+20;MG.fd=.2;MG.fh=0;sfx('swish');}
 }
}
function mgUpdate(dt){
 const F=SPF[MG.f];MG.t+=dt;MG.age+=dt;
 if(MG.age>.6&&(keys.left||keys.right||keys.up||keys.down)){mgEnd(true);return;}
 if(MG.k==='elf'){
  if(MG.ph==='aim'){MG.m=.5+.5*Math.sin(MG.t*(1.7+.3*MG.i));MG.aim=F.gy0-26+MG.m*(F.gy1-F.gy0+52);}
  else if(MG.ph==='fly'){const k=Math.min(1,MG.t/.42);MG.bx=MG.sx+(MG.tx-MG.sx)*k;MG.by=MG.sy+(MG.ty-MG.sy)*k;MG.bz=Math.sin(Math.PI*k)*10;MG.ky+=(MG.kt-MG.ky)*Math.min(1,dt*8);if(k>=1)mgLand();}
 }else if(MG.k==='frei'){
  if(MG.ph==='aim')MG.m=.5+.5*Math.sin(MG.t*(1.6+.25*MG.i));
  else if(MG.ph==='fly'){const k=Math.min(1,MG.t/.8);MG.bx=MG.sx+(MG.tx-MG.sx)*k;MG.by=MG.sy+(MG.ty-MG.sy)*k;MG.bz=10+Math.sin(Math.PI*k)*70;if(k>=1)mgLand();}
 }else{
  const B=bsPts();
  if(MG.ph==='wind'){MG.bx=B.M.x;MG.by=B.M.y-4;MG.bz=8;MG.m=0;if(MG.t>1.1){MG.ph='pitch';MG.t=0;MG.dur=.82-.04*MG.i;}}
  else if(MG.ph==='pitch'){const p=MG.t/MG.dur,q=Math.min(1.15,p);MG.bx=B.M.x+(B.H.x-B.M.x)*q;MG.by=B.M.y+(B.H.y-B.M.y)*q;MG.bz=8;MG.m=p;
   if(p>1.08){MG.res='Strike!';MG.sx=MG.bx;MG.sy=MG.by;MG.tx=B.H.x;MG.ty=B.H.y+20;MG.fd=.15;MG.fh=0;MG.ph='fly';MG.t=0;}}
  else if(MG.ph==='fly'){const k=Math.min(1,MG.t/MG.fd);MG.bx=MG.sx+(MG.tx-MG.sx)*k;MG.by=MG.sy+(MG.ty-MG.sy)*k;MG.bz=8+Math.sin(Math.PI*k)*MG.fh;if(k>=1)mgLand();}
 }
 if(MG&&MG.ph==='res'&&MG.t>1.3)mgNext();
}
function mgLand(){
 MG.ph='res';MG.t=0;const r=MG.res,good=['TOR!','Swish!','Korb!','Nichts als Netz!','Ring ... und rein!','HOME RUN!','Treffer!'].indexOf(r)>=0;
 if(good){MG.hits++;if(r==='HOME RUN!')MG.hr++;sfx(r==='HOME RUN!'?'win':'clap');}else sfx(r==='Gehalten!'?'aww':'pfft');
 MG.rc=good?'#ffd23f':'#cfd6e0';
 addFx(MG.bx,MG.by-30,r,MG.rc,1.4);
 if(SP&&SP[MG.f].occ&&good&&chance(.6))addFx(MG.bx+rf(-60,60),MG.by-50,pick(['Bravo!','Super!','Weiter so!']),'#fff2b0',1.4);
}
function mgNext(){MG.i++;if(MG.i>=MG.n){mgEnd(false);return;}mgReset();}
function mgEnd(cancel){
 const m=MG;MG=null;if(!m)return;
 if(cancel){toast('Aufgehört. Der Platz wartet auf dich.');return;}
 const h=m.hits,n=m.n;mood(3+h*2,'+'+(3+h*2)+' Sport');
 let t;
 if(m.k==='elf')t=h+' von '+n+' Elfmetern verwandelt. '+(h===n?'Elfmeterkönig! Der Torwart will ein Autogramm.':h>=3?'Stark! Der Torwart braucht jetzt eine Pause.':'Der Torwart hatte heute einfach seinen Tag.');
 else if(m.k==='frei')t=h+' von '+n+' Freiwürfen im Korb. '+(h===n?'Perfekt! Ab jetzt nennen dich alle nur noch Swish.':h>=3?'Starke Quote!':'Der Korb hängt heute irgendwie schief.');
 else t=h+' Treffer bei '+n+' Bällen'+(m.hr?', davon '+m.hr+' Home Run'+(m.hr>1?'s':''):'')+'. '+(m.hr?'Der Ball fliegt vermutlich noch.':h>=3?'Gutes Auge!':'Die Bälle waren heute besonders schnell.');
 if(h===n){G.resp++;t+=' +1 Respekt.';}
 G.sport=(G.sport||0)+1;
 showModal({title:m.k==='elf'?'Elfmeterschießen':m.k==='frei'?'Freiwürfe':'Schlagtraining',text:t,choices:[{label:'Nochmal!',a:'skA',p:'sp:'+m.k},{label:'Fertig',a:'mclose'}]});
}
function drawMGWorld(){
 const F=SPF[MG.f];
 if(MG.k==='elf'){drawPerson(MG.kx,MG.ky,Math.PI,'#2fbf4f','ped',0,.95);ctx.fillStyle='#f4f6f8';circle(MG.kx-7,MG.ky-6,2.6);circle(MG.kx-7,MG.ky+6,2.6);
  if(MG.ph==='aim'){ctx.strokeStyle='rgba(255,210,63,.95)';ctx.lineWidth=2;ctx.beginPath();ctx.arc(F.x1-6,MG.aim,6,0,6.283);ctx.stroke();ctx.lineWidth=1;}}
 if(MG.k==='schlag'){
  const B=bsPts();if(!SP.bs.occ){ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(B.M.x-8,B.M.y-4,20,14);ctx.fillStyle='#6a7380';ctx.fillRect(B.M.x-10,B.M.y-8,20,14);ctx.fillStyle='#ffd23f';ctx.fillRect(B.M.x-4,B.M.y+2,8,4);}
  const sw=MG.ph==='fly'||MG.ph==='res',ba=-Math.PI/2+(sw?1.5:-.5);ctx.strokeStyle='#8a5a2a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(P.x+5,P.y);ctx.lineTo(P.x+5+Math.cos(ba)*17,P.y+Math.sin(ba)*17);ctx.stroke();ctx.lineWidth=1;
 }
 drawSpBall(MG.f,{x:MG.bx,y:MG.by,z:MG.bz,rot:MG.t*8});
}
function drawMG(){
 const w=380,h=80,x=(VW-w)/2,y=VH-156;
 ctx.fillStyle='rgba(12,16,13,.88)';ctx.fillRect(x,y,w,h);ctx.strokeStyle='#f2b441';ctx.lineWidth=2;ctx.strokeRect(x+1,y+1,w-2,h-2);ctx.lineWidth=1;
 const nm=MG.k==='elf'?'Elfmeter':MG.k==='frei'?'Freiwurf':'Schlag';
 ctx.fillStyle='#ece6d6';ctx.font='bold 14px Arial';ctx.textAlign='left';ctx.textBaseline='middle';ctx.fillText(nm+' '+Math.min(MG.i+1,MG.n)+' / '+MG.n+'    Treffer: '+MG.hits,x+12,y+16);
 ctx.textAlign='right';ctx.fillStyle='#9aa593';ctx.font='11px Arial';ctx.fillText('Pfeiltaste: aufhören',x+w-10,y+16);
 const bx=x+16,bw=w-32,by=y+32,bh=16;
 ctx.fillStyle='#0b0f0c';ctx.fillRect(bx,by,bw,bh);
 let mk=MG.m;
 if(MG.k==='elf'){const F=SPF.fb,tot=F.gy1-F.gy0+52,p0=31/tot,p1=(26+F.gy1-F.gy0-5)/tot;ctx.fillStyle='#2f6a3a';ctx.fillRect(bx+bw*p0,by,bw*(p1-p0),bh);ctx.fillStyle='#fff';ctx.fillRect(bx+bw*p0-2,by-3,3,bh+6);ctx.fillRect(bx+bw*p1-1,by-3,3,bh+6);}
 else if(MG.k==='frei'){ctx.fillStyle='#7a3a2a';ctx.fillRect(bx,by,bw,bh);ctx.fillStyle='#b8862b';ctx.fillRect(bx+bw*.3,by,bw*.4,bh);ctx.fillStyle='#3f9a3f';ctx.fillRect(bx+bw*.4,by,bw*.2,bh);}
 else{const s=v=>bx+bw*Math.min(1,v/1.1);ctx.fillStyle='#3a4a6a';ctx.fillRect(bx,by,bw,bh);ctx.fillStyle='#b8862b';ctx.fillRect(s(.75),by,s(1.05)-s(.75),bh);ctx.fillStyle='#3f9a3f';ctx.fillRect(s(.81),by,s(.99)-s(.81),bh);ctx.fillStyle='#ffd23f';ctx.fillRect(s(.865),by,s(.935)-s(.865),bh);mk=Math.min(1,(MG.m||0)/1.1);}
 if(MG.ph==='aim'||MG.ph==='pitch'){const px=bx+bw*clamp(mk,0,1);ctx.fillStyle='#fff';ctx.fillRect(px-2,by-5,4,bh+10);ctx.beginPath();ctx.moveTo(px-6,by-8);ctx.lineTo(px+6,by-8);ctx.lineTo(px,by-2);ctx.closePath();ctx.fill();}
 ctx.textAlign='center';
 if(MG.res&&(MG.ph==='res'||MG.ph==='fly')){ctx.font='bold 16px Arial';ctx.fillStyle=MG.ph==='res'?MG.rc:'#9aa593';ctx.fillText(MG.ph==='res'?MG.res:'...',x+w/2,y+66);}
 else{ctx.font='bold 12px Arial';ctx.fillStyle='#f2b441';ctx.fillText(mgPrompt(),x+w/2,y+66);}
 ctx.textAlign='start';ctx.textBaseline='alphabetic';
}
function coastPt(s){const q=6.2832*s;return{x:32*TS+11*TS*Math.cos(q)+1.3*TS*Math.cos(3*q),y:6.6*TS+3.2*TS*Math.sin(q)+.9*TS*Math.sin(3*q+.6),h:.5+.5*Math.cos(2*q+1.2)};}
function coastAng(s){const a=coastPt(s),b=coastPt(s+.002);return Math.atan2(b.y-b.h*18-(a.y-a.h*18),b.x-a.x);}
function genFpark(z,H){
 const zs=H.zs,zg=H.zg,zf=H.zf,mk=H.mk,R=H.R,r=H.r,Tz=z.T;
 z.nogo={x0:0,y0:0,x1:ZW*TS,y1:ZH*TS,n:'Freizeitpark'};
 for(let i=0;i<ZW*ZH;i++)Tz[i]=SW;
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.8)zs(x,y,TR);}
 zf(4,2,11,10,GR);zf(18,2,28,10,GR);
 zs(7,10,BL);zs(11,10,BL);
 {const m=mk('rad','sk',9,12,'Riesenrad','Riesenrad fahren');m.sk='rad';m.col='#ffb347';}
 {const m=mk('bahn','sk',32,12,'Achterbahn Rheinblitz','Achterbahn fahren');m.sk='bahn';m.col='#ffb347';}
 for(let j=18;j<=22;j++)for(let i=10;i<=14;i++)if((i-12)*(i-12)+(j-20)*(j-20)<=4.5)zs(i,j,BL);
 {const m=mk('karu','sk',12,24,'Karussell','Karussell fahren');m.sk='karu';m.col='#ffb347';}
 zf(18,14,14,1,FN);zf(18,24,14,1,FN);zf(18,14,1,11,FN);zf(31,14,1,11,FN);zf(19,15,12,9,RD);zs(24,24,SW);zs(25,24,SW);
 const SC=['#e5504d','#2e86c1','#f1c40f','#27ae60','#8e44ad','#ff9a3c'];
 [[21,17],[24,19],[28,17],[22,21],[28,21],[25,16]].forEach((q,i)=>{const s=mkRide('scoot',q[0]*TS+16,q[1]*TS+16,r()*6.283);s.col=SC[i];s.rc=r()<.6?PCOL[i%PCOL.length]:null;s.v0=80+r()*50;z.rides.push(s);});
 zf(35,15,4,2,BL);z.BLD.push({x:35,y:15,w:4,h:2,c:'#e5504d',n:'DOSENWERFEN',k:'bude',hh:6});
 {const m=mk('dosen','sk',36,17,'Dosenwerfen','Dosenwerfen spielen');m.sk='dosen';m.col='#ffb347';}
 zf(40,15,3,2,BL);z.BLD.push({x:40,y:15,w:3,h:2,c:'#ff8fc8',n:'ZUCKERWATTE',k:'bude',hh:6});
 mk('zucker','buedchen',41,17,'Zuckerwatte-Stand','Zuckerwatte-Stand besuchen');
 zf(35,20,9,4,GR);[[36,21],[43,22],[39,23]].forEach(q=>zs(q[0],q[1],TR));
 zf(4,14,3,2,FD);zf(41,25,3,1,FD);
 [[16,26],[17,26],[30,26],[31,26],[37,24],[38,24]].forEach(q=>zs(q[0],q[1],LC));
 for(let i=0;i<10;i++){const x=R(3,44),y=R(13,27);if(zg(x,y)===SW&&!(x>=7&&x<=17&&y>=16&&y<=25)&&!(x>=17&&x<=32&&y>=13&&y<=25)&&!(x>=34&&x<=43&&y>=14&&y<=18)&&!(x<=8&&y>=23)&&!(x>=41&&y>=23))zs(x,y,TR);}
}
function fparkStatic(c){
 const N=240;c.lineCap='round';
 c.strokeStyle='rgba(0,0,0,.18)';c.lineWidth=9;c.beginPath();for(let i=0;i<=N;i++){const p=coastPt(i/N);if(i)c.lineTo(p.x+5,p.y+5);else c.moveTo(p.x+5,p.y+5);}c.stroke();
 c.strokeStyle='#8a929c';c.lineWidth=3;for(let i=0;i<N;i+=6){const p=coastPt(i/N);c.beginPath();c.moveTo(p.x,p.y+2);c.lineTo(p.x,p.y-p.h*18-4);c.stroke();}
 [['#6a1f2a',7],['#e5504d',4]].forEach(st=>{c.strokeStyle=st[0];c.lineWidth=st[1];c.beginPath();for(let i=0;i<=N;i++){const p=coastPt(i/N),y=p.y-p.h*18-4;if(i)c.lineTo(p.x,y);else c.moveTo(p.x,y);}c.stroke();});
 c.strokeStyle='rgba(255,255,255,.55)';c.lineWidth=1;c.beginPath();for(let i=0;i<=N;i++){const p=coastPt(i/N),y=p.y-p.h*18-5;if(i)c.lineTo(p.x,y);else c.moveTo(p.x,y);}c.stroke();
 c.lineCap='butt';
 const st=coastPt(.25),sy=st.y-st.h*18;
 c.fillStyle='#a8723f';c.fillRect(st.x-36,sy+4,72,12);
 c.fillStyle='#5a3416';c.fillRect(st.x-36,sy-22,4,28);c.fillRect(st.x+32,sy-22,4,28);
 for(let i=0;i<8;i++){c.fillStyle=i%2?'#ffd23f':'#e5504d';c.fillRect(st.x-40+i*10,sy-30,10,9);}
 c.font='bold 12px Arial';c.textAlign='center';c.textBaseline='middle';c.lineWidth=3;c.strokeStyle='rgba(0,0,0,.7)';c.strokeText('RHEINBLITZ',st.x,sy-40);c.fillStyle='#fff';c.fillText('RHEINBLITZ',st.x,sy-40);
 const W=FPK.rad,gy=W.y+W.R+30;
 c.strokeStyle='#8a929c';c.lineWidth=6;c.beginPath();c.moveTo(W.x,W.y);c.lineTo(W.x-62,gy);c.moveTo(W.x,W.y);c.lineTo(W.x+62,gy);c.stroke();
 c.lineWidth=3;c.beginPath();c.moveTo(W.x-44,gy-22);c.lineTo(W.x+44,gy-22);c.stroke();
 c.fillStyle='#5a6470';c.fillRect(W.x-74,gy-2,148,8);c.fillStyle='#e8d8a8';c.fillRect(W.x-20,W.y+W.R+12,40,10);
 const K=FPK.karu;
 c.fillStyle='rgba(0,0,0,.2)';c.beginPath();c.ellipse(K.x+4,K.y+6,K.R+4,K.R*.95,0,0,6.283);c.fill();
 c.fillStyle='#d8b878';c.beginPath();c.arc(K.x,K.y,K.R,0,6.283);c.fill();c.strokeStyle='#a8823a';c.lineWidth=3;c.stroke();
 c.fillStyle='#f4e8c8';c.beginPath();c.arc(K.x,K.y,K.R-9,0,6.283);c.fill();
 c.font='bold 13px Arial';c.lineWidth=3;c.strokeStyle='rgba(0,0,0,.75)';c.strokeText('AUTOSCOOTER',25*TS,14*TS-8);c.fillStyle='#5ff0ff';c.fillText('AUTOSCOOTER',25*TS,14*TS-8);
 c.lineWidth=1;c.textAlign='start';c.textBaseline='alphabetic';
}
function drawTrain(s,rid){
 for(let k=2;k>=0;k--){const ss=s-k*.014,p=coastPt(ss),a=coastAng(ss),y=p.y-p.h*18-7;
  ctx.fillStyle='rgba(0,0,0,.2)';ctx.beginPath();ctx.ellipse(p.x+5,p.y+5,10,6,0,0,6.283);ctx.fill();
  ctx.save();ctx.translate(p.x,y);ctx.rotate(a);
  ctx.fillStyle=['#2e86c1','#f1c40f','#e5504d'][k];ctx.fillRect(-11,-7,22,14);ctx.fillStyle='rgba(255,255,255,.4)';ctx.fillRect(-11,-7,22,3);
  if(k===0){ctx.fillStyle='#ffd23f';ctx.fillRect(9,-5,3,10);}
  if(rid&&rid[k]){ctx.fillStyle='#4a3a2a';circle(-4,-1,2.6);circle(4,-1,2.6);ctx.fillStyle='#e8c39e';circle(-4,-4,1.6);circle(4,-4,1.6);}
  ctx.restore();}
}
function drawKaru(a,ride){
 const K=FPK.karu,HC=['#ffffff','#f4d03f','#ff8fc8','#9fd8ff','#b58cff','#7bd86a'];
 for(let k=0;k<6;k++){const q=a+k*1.0472,x=K.x+Math.cos(q)*K.r,y=K.y+Math.sin(q)*K.r,b=Math.sin(timeNow*4+k)*3;
  ctx.strokeStyle='#d8b030';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x,y-24);ctx.lineTo(x,y+4);ctx.stroke();ctx.lineWidth=1;
  ctx.save();ctx.translate(x,y+b);ctx.rotate(q+Math.PI/2);ctx.fillStyle=HC[k];ctx.beginPath();ctx.ellipse(0,0,10,5,0,0,6.283);ctx.fill();circle(9,-3,4);ctx.fillStyle='#5a3416';ctx.fillRect(-13,-1,4,2);ctx.restore();
  if(!(ride&&k===0)&&k%3===0){ctx.fillStyle='#4a3a2a';circle(x,y+b-3,3.2);}}
 ctx.fillStyle='#d8b030';circle(K.x,K.y,7);
 ctx.lineWidth=9;for(let k=0;k<12;k++){ctx.strokeStyle=k%2?'rgba(229,80,77,.8)':'rgba(255,255,255,.8)';ctx.beginPath();ctx.arc(K.x,K.y-26,K.R*.9,k*.5236+a*.3,(k+1)*.5236+a*.3);ctx.stroke();}ctx.lineWidth=1;
 ctx.fillStyle='#ffd23f';circle(K.x,K.y-26,6);
}
function drawFlocke(d){
 const x=d.x,y=d.y,b=Math.sin((d.walk||0)*.6)*2;
 ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(x+2,y+4,14,5,0,0,6.283);ctx.fill();
 ctx.fillStyle='#fff';ctx.fillRect(x-7,y-6,4,9);ctx.fillRect(x+3,y-6,4,9);
 ctx.fillStyle='#ffb3e0';[[0,-22,13],[-10,-16,9],[10,-16,9],[-6,-31,8],[7,-31,8]].forEach(q=>circle(x+q[0],y+q[1]+b,q[2]));
 ctx.fillStyle='#222';circle(x-4,y-23+b,1.8);circle(x+4,y-23+b,1.8);
 ctx.strokeStyle='#a03a6a';ctx.lineWidth=1.5;ctx.beginPath();ctx.arc(x,y-19+b,4,.2,2.9);ctx.stroke();ctx.lineWidth=1;
 ctx.fillStyle='rgba(255,120,160,.6)';circle(x-8,y-20+b,2.2);circle(x+8,y-20+b,2.2);
 for(let i=0;i<3;i++){const bx=x+15+i*6,by=y-46-i*4+Math.sin(timeNow*2+i)*2;ctx.strokeStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.moveTo(x+10,y-14);ctx.lineTo(bx,by+7);ctx.stroke();ctx.fillStyle=BALC[i];ctx.beginPath();ctx.ellipse(bx,by,5,6.5,0,0,6.283);ctx.fill();}
}
function drawBal(x,y,col){const b=Math.sin(timeNow*2+x*.01)*2;ctx.strokeStyle='rgba(255,255,255,.75)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x+4,y-4);ctx.lineTo(x+9+b,y-30);ctx.stroke();ctx.fillStyle=col;ctx.beginPath();ctx.ellipse(x+9+b,y-37,6,7.5,0,0,6.283);ctx.fill();ctx.fillStyle='rgba(255,255,255,.5)';circle(x+7+b,y-40,1.8);}
function drawFpark(cx,cy){
 const z=ZONE,iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 const W=FPK.rad;if(iv(W.x,W.y,W.R+60))drawWheel(W.x,W.y,W.R,z.wa||0,z.rid);
 if(iv(32*TS,6.6*TS,560))drawTrain(z.ts||0,z.trid);
 const K=FPK.karu;if(iv(K.x,K.y,K.R+60))drawKaru(z.ka||0,P.coast&&P.coast.k==='karu');
 if(iv(25*TS,19*TS,300)&&chance(.3)){const L=RIDES.filter(q=>q.k==='scoot'&&Math.abs(q.sp)>40);if(L.length){const s=pick(L);FX.push({x:s.x-Math.cos(s.a)*8,y:s.y-Math.sin(s.a)*8-28,vx:rf(-20,20),vy:rf(-20,5),g:60,t:0,life:.35,dot:pick(['#5ff0ff','#fff','#ffd23f']),r:1.6});}}
}
function fpInit(z){if(z.wa!==undefined)return;z.wa=0;z.ka=0;z.ts=.3;z.rid=[0,1,2,3,4,5,6,7].map(()=>chance(.55));z.trid=[chance(.7),chance(.7),chance(.7)];z.rt=12;}
function fpScootSwap(){const S=RIDES.filter(q=>q.k==='scoot'&&P.ride!==q);if(!S.length)return;const s=pick(S);if(s.rc&&chance(.5))s.rc=null;else if(!s.rc){s.rc=pick(PCOL);s.v0=rf(80,130);}}
function fpTick(dt){
 const z=ZONE;fpInit(z);
 const c=P.coast;
 z.wa+=(c&&c.k==='rad'?.42:.3)*dt;z.ka+=(c&&c.k==='karu'?1.5:1.1)*dt;
 const h=coastPt(z.ts).h;z.ts+=(.07+.08*(1-h))*dt;if(!(c&&c.k==='bahn')&&z.ts>1)z.ts-=1;
 z.rt-=dt;if(z.rt<=0){z.rt=rf(10,20);const k=rnd(0,7);if(!(c&&c.k==='rad'&&k===0))z.rid[k]=!z.rid[k];if(!(c&&c.k==='bahn'))z.trid=[chance(.7),chance(.7),chance(.7)];fpScootSwap();}
 if(c){
  c.t+=dt;
  if(c.k==='bahn'){const p=coastPt(z.ts);P.x=p.x;P.y=p.y-p.h*18-9;P.a=coastAng(z.ts);if(p.h<.15)shake=Math.max(shake,.22);if(chance(dt*1.2))addFx(P.x,P.y-20,pick(['WUIIII!','AAAH!','Juhu!','Hände hoch!']),'#ffd23f',1);if(z.ts>=c.s0+2)fpRideEnd('bahn');}
  else if(c.k==='rad'){const W=FPK.rad,q=z.wa;P.x=W.x+Math.cos(q)*W.R;P.y=W.y+Math.sin(q)*W.R+9;P.a=-Math.PI/2;if(!c.top&&Math.sin(q)<-.97){c.top=1;mood(4,'+Aussicht');toast('Ganz oben! Du siehst den ganzen Park, die Achterbahn und ganz hinten glitzert der Rhein.');}if(z.wa>=c.a0+6.2832)fpRideEnd('rad');}
  else if(c.k==='karu'){const K=FPK.karu,q=z.ka;P.x=K.x+Math.cos(q)*K.r;P.y=K.y+Math.sin(q)*K.r+Math.sin(timeNow*4)*3-4;P.a=q+Math.PI/2;if(c.t>=11)fpRideEnd('karu');}
 }
 const S=RIDES.filter(q=>q.k==='scoot');
 S.forEach(s=>{
  if(s.bc>0)s.bc-=dt;
  if(P.ride===s)return;
  if(!s.rc){s.sp*=Math.exp(-3*dt);if(Math.abs(s.sp)>2)rideMove(s,Math.cos(s.a)*s.sp*dt,Math.sin(s.a)*s.sp*dt);return;}
  s.tt=(s.tt||0)-dt;if(s.tt<=0){s.tt=rf(.8,2.2);s.a+=rf(-1.2,1.2);}
  s.sp+=((s.v0||100)-s.sp)*Math.min(1,dt*2);
  rideMove(s,Math.cos(s.a)*s.sp*dt,Math.sin(s.a)*s.sp*dt);if(s.hx||s.hy){s.a+=Math.PI+rf(-.6,.6);s.sp*=.4;}
 });
 for(let i=0;i<S.length;i++)for(let j=i+1;j<S.length;j++){
  const a=S[i],b=S[j],dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy);
  if(d<24&&d>0){const o=(24-d)/2,nx=dx/d,ny=dy/d;rideMove(a,-nx*o,-ny*o);rideMove(b,nx*o,ny*o);
   if(!(a.bc>0)&&!(b.bc>0)){a.bc=.6;b.bc=.6;const me=P.ride===a||P.ride===b;
    if(me){shake=Math.max(shake,.3);mood(2,'+2 Bumm');sfx('bonk');addFx((a.x+b.x)/2,(a.y+b.y)/2-22,pick(['BUMM!','Rumms!','Hihi!','Boing!']),'#ffd23f',1);}
    else if(Math.hypot(P.x-a.x,P.y-a.y)<320&&chance(.5))addFx((a.x+b.x)/2,(a.y+b.y)/2-22,pick(['Bumm!','Boing!']),'#fff2b0',.9);
    a.sp*=-.5;b.sp*=-.5;if(P.ride!==a)a.a+=rf(1,2);if(P.ride!==b)b.a+=rf(1,2);}
  }}
 if(P.ride&&P.ride.k==='scoot'){P.x=P.ride.x;P.y=P.ride.y;}
 skl().forEach(d=>{if(d.k!=='flocke')return;if(d.cd2>0)d.cd2-=dt;leash(d,d.hx,d.hy,360);steerStep(d,dt,24);d.tk=(d.tk||3)-dt;if(d.tk<=0&&Math.hypot(P.x-d.x,P.y-d.y)<320){d.tk=rf(6,11);addFx(d.x,d.y-40,pick(['Huhu!','Zuckerwatte für alle!','Wer will Luftballons?','Achterbahn? Achterbahn!']),'#ffd6f2',1.8);}});
}
function fpMenu(k){
 if(P.coast)return;
 if(k==='bahn')mdl('Achterbahn Rheinblitz','Zwei Runden, drei Hügel und eine Kurve, die so tut, als wäre sie ein Looping. Bitte gut festhalten! Die Fahrt ist im Eintritt schon drin.',[['Einsteigen und losfahren','fp:bahn'],['Erst mal zuschauen','fp:watch']]);
 else if(k==='rad')mdl('Riesenrad','Die Gondeln schaukeln gemütlich. Von oben sieht man angeblich bis nach Amsterdam. Angeblich.',[['Einsteigen','fp:rad'],['Nach oben winken','fp:wink']]);
 else mdl('Karussell','Die Orgel spielt einen Walzer, die Pferde sind frisch lackiert, und eines hat ein Einhorn-Horn angeklebt.',[['Aufsteigen','fp:karu'],['Den Kindern zuwinken','fp:wink2']]);
}
function fpRideStart(k){
 const z=ZONE;if(!z||z.name!=='fpark'||P.coast)return;
 if(P.ride)leaveRide(true);
 closeAll();fpInit(z);P.vx=0;P.vy=0;keys.left=keys.right=keys.up=keys.down=0;
 const c={k:k,t:0,mx:P.x,my:P.y};
 if(k==='bahn'){z.ts=.25;c.s0=.25;z.trid[0]=false;toast('Bügel runter, Hände hoch! Der Rheinblitz rattert los ...');}
 else if(k==='rad'){z.wa=Math.PI/2;c.a0=z.wa;z.rid[0]=false;toast('Du steigst in die Gondel. Ganz langsam geht es nach oben.');}
 else toast('Du schwingst dich aufs weiße Pferd. Die Orgel spielt, die Welt dreht sich.');
 P.coast=c;sfx('ride');
}
function fpRideEnd(k){
 const c=P.coast;P.coast=null;const m=ZONE.MKS.find(q=>q.sk===k)||{x:c.mx,y:c.my},f=freeSpot(m.x,m.y-26);
 P.x=f.x;P.y=f.y;P.vx=0;P.vy=0;G.fahrten=(G.fahrten||0)+1;
 if(k==='bahn'){mood(14,'+14 Achterbahn');sfx('win');toast(pick(['Was für eine Fahrt! Deine Haare stehen in alle Richtungen, dein Grinsen auch.','Ausgestiegen. Die Beine zittern, das Herz jubelt. Nochmal?','Rheinblitz bezwungen! Das Foto an der Kasse zeigt dich mit weit offenem Mund.']));}
 else if(k==='rad'){mood(9,'+9 Riesenrad');sfx('magic');toast('Einmal rund um den Himmel. Unten wartet die Welt, ein bisschen kleiner als vorher.');}
 else{mood(7,'+7 Karussell');sfx('musik');toast(pick(['Ein bisschen schwindelig, sehr zufrieden. Das Pferd zwinkert dir zu.','Karussell fahren ist wie früher, nur dass du jetzt drüber lachst.']));}
 if(G.fahrten===10)toast('Zehn Fahrten im Freizeitpark! Du bekommst die goldene Jahreskarte. Sie ist aus Pappe, aber golden.');
}
function flockeHi(d){
 if(d.cd2>0){toast('Flocke verteilt gerade Luftballons an die Kinder. Gleich bist du dran!');return;}
 d.cd2=10;mood(6,'+6 Flocke');sfx('clap');addFx(d.x,d.y-40,'High Five!','#ffd23f',1.4);
 G.ballon=pick(BALC);G.balT=150;
 toast('Flocke, die Zuckerwatten-Wolke, klatscht dich ab und schenkt dir einen '+({'#ff4d7a':'pinken','#5ff0ff':'hellblauen','#ffd23f':'gelben','#7bd86a':'grünen','#b58cff':'lila','#ff9a3c':'orangen'}[G.ballon])+' Luftballon.');
}
function dosMenu(){mdl('Dosenwerfen','"Drei Bälle, sechs Dosen! Alle umgeworfen gibt den Hauptpreis!" Der Budenbesitzer zwirbelt seinen Schnurrbart. Drei Bälle kosten 2 €. Deine Preise bisher: '+(G.plusch||0)+'.',[['Spielen (2 €)','dw:go',G.cash<2]]);}
function dosShow(){const s=G.dw;showModal({title:'Dosenwerfen',text:'Stehende Dosen: '+s.st+' von 6 · Bälle übrig: '+s.b+(s.last?' · '+s.last:''),choices:[{label:'Werfen!',a:'skA',p:'dw:t'},{label:'Aufhören',a:'skA',p:'dw:x'}]});}
function skAct13(p){
 if(p==='sp:elf'){mgStart('elf');return true;}
 if(p==='sp:frei'){mgStart('frei');return true;}
 if(p==='sp:schlag'){mgStart('schlag');return true;}
 if(p.indexOf('sp:cheer:')===0){const f=SP&&SP[p.slice(9)];if(!f)return true;mood(4,'+4 Anfeuern');sfx('clap');f.pl.forEach(q=>{if(chance(.4))addFx(q.x,q.y-22,pick(['Danke!','Jaaa!','Hopp hopp!','Gib alles!']),'#fff2b0',1.4);});toast(pick(['Du feuerst an, als wäre es ein Finale. Die Spieler laufen plötzlich doppelt so schnell.','Deine Fangesänge sind schief, aber laut. Die Mannschaft liebt dich.','La-Ola mit einer Person. Es sieht seltsam aus, aber es wirkt!']));return true;}
 if(p==='sp:rek'){toast('Deine Tore im Sportpark: '+(G.tore||0)+'. Sportrunden insgesamt: '+(G.sport||0)+'.');return true;}
 if(p==='fp:bahn'||p==='fp:rad'||p==='fp:karu'){fpRideStart(p.slice(3));return true;}
 if(p==='fp:watch'){mood(2,'+2');toast('Der Zug rattert vorbei. Alle kreischen, einer isst dabei in aller Ruhe Zuckerwatte. Respekt.');return true;}
 if(p==='fp:wink'){mood(2,'+2');toast('Aus drei Gondeln winkt es zurück. Aus einer winkt sogar ein Hund.');return true;}
 if(p==='fp:wink2'){mood(2,'+2');toast('Die Kinder auf dem Karussell winken bei jeder Runde. Du winkst bei jeder Runde zurück. Es werden sehr viele Runden.');return true;}
 if(p==='dw:go'){if(G.cash<2){toast('Nicht genug Geld.');return true;}G.cash-=2;sfx('coin');G.dw={st:6,b:3,last:''};dosShow();return true;}
 if(p==='dw:t'){
  const s=G.dw;if(!s)return true;s.b--;const n=Math.min(s.st,pick([0,1,1,2,2,2,3,3,4]));s.st-=n;
  s.last=n?n+' Dose'+(n>1?'n':'')+' umgeworfen!':'Daneben! Der Ball verschwindet im Stofftier-Regal.';sfx(n?'crumble':'pfft');
  if(s.st<=0){G.dw=null;G.plusch=(G.plusch||0)+1;mood(10,'+10 Hauptpreis');sfx('win');showModal({title:'Hauptpreis!',text:'Alle sechs Dosen liegen! Du gewinnst '+pick(['einen Riesen-Plüschwal','ein Einhorn so groß wie ein Kühlschrank','eine Plüsch-Currywurst mit Gesicht','einen Teddy mit Sonnenbrille'])+'. Er passt in keinen Rucksack, aber in dein Herz.',choices:[{label:'Juhu!',a:'mclose'}]});return true;}
  if(s.b<=0){G.dw=null;mood(3,'+3');showModal({title:'Trostpreis',text:'Es stehen noch '+s.st+' Dose'+(s.st>1?'n':'')+'. Du bekommst einen Trostpreis: '+pick(['einen Plastikring mit Glitzerstein','ein Lineal mit Werbung','einen Mini-Flummi','eine Papierblume'])+'.',choices:[{label:'Nochmal (2 €)',a:'skA',p:'dw:go',off:G.cash<2},{label:'Fertig',a:'mclose'}]});return true;}
  dosShow();return true;
 }
 if(p==='dw:x'){G.dw=null;toast('Du gibst die restlichen Bälle zurück. Der Budenbesitzer nickt verständnisvoll.');return true;}
 return false;
}
function ext19Update(dt){
 if(!G)return;
 if(!ZONE){spTick(dt);if(MG)mgUpdate(dt);}
 else if(ZONE.name==='fpark')fpTick(dt);
 if(G.ballon){G.balT=(G.balT||0)-dt;if(G.balT<=0){G.ballon=null;toast('Dein Luftballon macht sich selbstständig und fliegt davon. Gute Reise!');}}
}
function mOX(){return ZONE?0:Math.floor((304-CITY.MW*2.5)/2);}
function miniDraw(x,big){
 const S=mS(),O=mOX(),r=big?4:3;
 x.drawImage(MM,O,0);
 MKS.forEach(m=>{x.fillStyle=m.kind==='hq'?'#6bcf63':m.kind==='willi'?'#e5604d':m.kind==='portal'?'#c06bff':m.kind==='buedchen'?'#46c2a0':m.kind==='scream'?'#ff5030':m.kind==='disco'?'#ff5fd0':'#f2b441';x.beginPath();x.arc(O+m.x/TS*S,m.y/TS*S,r,0,6.283);x.fill();});
 if(!G)return;
 if(!ZONE)G.active.forEach(m=>{const k=mTgt(m),mk=MKQ[k];if(!mk)return;x.strokeStyle='#fff';x.lineWidth=big?2:1.5;x.beginPath();x.arc(O+mk.x/TS*S,mk.y/TS*S,big?7:6,0,6.283);x.stroke();});
 aniMini(x,O,S,big);hideMini(x,O,S,big);
 thugs.forEach(u=>{if(u.loot&&u.ko<=0){x.fillStyle='#ff2d55';x.fillRect(O+u.x/TS*S-3,u.y/TS*S-3,6,6);x.strokeStyle='#fff';x.lineWidth=1;x.strokeRect(O+u.x/TS*S-3,u.y/TS*S-3,6,6);}});
 if(ZONE&&ZONE.whale){x.fillStyle='#8fc7ff';x.beginPath();x.ellipse(O+ZONE.whale.x/TS*S,ZONE.whale.y/TS*S,7,3,0,0,6.283);x.fill();}
 chasers.forEach(u=>{x.fillStyle=Math.floor(timeNow*4)%2?'#ff3030':'#3070ff';x.fillRect(O+u.x/TS*S-2,u.y/TS*S-2,4,4);});
 miniExtra(x,O,S,big);
 if(RACE){x.strokeStyle='#6bcf63';x.lineWidth=2;x.beginPath();x.arc(O+RACE.gx/TS*S,RACE.gy/TS*S,5,0,6.283);x.stroke();}
 x.fillStyle='#fff';x.beginPath();x.arc(O+P.x/TS*S,P.y/TS*S,big?4:3.5,0,6.283);x.fill();
 x.strokeStyle='#000';x.lineWidth=1;x.stroke();
}

let CAMP=null,campId=0;
const MUS=[
 {g:'Strand-Reggae',bpm:78,k:'reg',key:0,s:[['Sonnenbrand im Herzen',3],['Hängematte am Rhein',11]],p:[[48,0],[53,0],[55,0],[53,0]]},
 {g:'Schlager',bpm:124,k:'sch',key:0,s:[['Grillfürst von Rheinhanfen',5],['Wir tanzen, bis die Kohle glüht',17]],p:[[48,0],[55,0],[45,1],[53,0]]},
 {g:'Elektro',bpm:126,k:'ele',key:-3,s:[['Bass am Baggersee',7],['Neonlicht im Hafen',23]],p:[[45,1],[41,0],[48,0],[43,0]]},
 {g:'Lagerfeuer-Gitarre',bpm:88,k:'git',key:-5,s:[['Stockbrot-Ballade',2],['Sterne über Rheinhanfen',29]],p:[[43,0],[50,0],[52,1],[48,0]]},
 {g:'Rock',bpm:120,k:'roc',key:-3,s:[['Feierabend-Riff',13],['Vollgas im Van',31]],p:[[45,1],[48,0],[43,0],[50,0]]}
];
const SONGS=[];MUS.forEach((g,gi)=>g.s.forEach(q=>SONGS.push({gi:gi,t:q[0],seed:q[1]})));
function mf(m){return 440*Math.pow(2,(m-69)/12);}
function musStep(S,i,dl,V){
 const g=MUS[S.gi],bar=Math.floor(i/16),s=i%16,ch=g.p[bar%4],r=ch[0],c=[r+12,r+12+(ch[1]?3:4),r+19];
 const h=(Math.imul(S.seed+1,2654435761)^Math.imul((bar%8)*16+s+1,40503))>>>0,q=(h%1000)/1000;
 const PE=[0,2,4,7,9,12,14],mel=72+g.key+PE[(h>>5)%7];
 const N=(m,d,ty,v,o)=>tn(mf(m),d,ty,v*V,0,dl+(o||0));
 const kick=v=>tn(150,.18,'sine',v*V,42,dl),hat=v=>nz(.035,v*V,8000,'highpass',dl),snare=v=>nz(.13,v*V,1900,'bandpass',dl);
 if(g.k==='reg'){
  if(s===0||s===3||s===10)N(r-12+(s===10?7:0),.32,'triangle',.2);
  if(s===4||s===12)c.forEach(m=>N(m,.09,'square',.026));
  if(s===6||s===14)c.forEach(m=>N(m,.06,'square',.014));
  if(s===8){kick(.34);snare(.13);}
  if(s%2===0)hat(.035);
  if((s%4===0||s%4===3)&&q<.45&&bar%4<3)N(mel,.28,'sine',.08);
 }else if(g.k==='sch'){
  if(s%4===0)kick(.32);
  if(s===4||s===12)nz(.09,.1*V,1400,'bandpass',dl);
  if(s===0)N(r-12,.2,'triangle',.2);if(s===8)N(r-5,.2,'triangle',.2);
  if(s===4||s===12)c.forEach(m=>N(m,.1,'square',.022));
  if(s%4===2)hat(.03);
  if(s%2===0&&q<.6)N(mel,.16,'triangle',.08);
 }else if(g.k==='ele'){
  if(s%4===0)kick(.4);
  if(s%4===2)hat(.05);
  if(s===4||s===12)nz(.09,.09*V,1300,'bandpass',dl);
  if(s%4===2)N(r-12,.12,'sawtooth',.045);
  if(bar%8>=2)N(c[s%3]+12,.07,'square',.016);
  if(bar%8>=4&&s%4===0&&q<.5)N(mel,.22,'triangle',.07);
 }else if(g.k==='git'){
  if(s%2===0){const seq=[r,c[1],c[2],c[0]+12,c[2],c[1],c[0]+12,c[2]];N(seq[(s/2)%8],.5,'triangle',.1);}
  if(s===0)c.forEach((m,k)=>N(m,.6,'triangle',.05,k*.018));
  if(bar%8>=4&&s%8===0&&q<.65)N(mel,.55,'sine',.06);
 }else{
  if(s===0||s===6||s===8)kick(.36);
  if(s===4||s===12)snare(.17);
  if(s%2===0)hat(.03);
  if(s%2===0){const d=s===0?.35:.1;N(r,d,'sawtooth',.03);N(r+7,d,'sawtooth',.026);}
  if(bar%8>=4&&s%2===0&&q<.45)N(mel,.13,'square',.03);
 }
}
function musicTick(){
 const C=(CAMP&&CAMP.music)?CAMP:(ZONE&&ZONE.mus&&!fade)?ZONE.mus:null;
 if(CAMP&&!CAMP.music)CAMP.mt=0;
 if(!C||!C.music||!SND.on||!SND.c||SND.c.state!=='running'||!G){if(C)C.mt=0;return;}
 const ac=SND.c,now=ac.currentTime,S=SONGS[C.si],sd=60/MUS[S.gi].bpm/4;
 if(!C.mt||C.mt<now-.3)C.mt=now+.06;
 const d=Math.hypot(P.x-C.x,P.y-C.y),f=clamp(1-(d-90)/650,0,1),V=f*f*.7;
 while(C.mt<now+.22){if(V>.01)musStep(S,C.st,C.mt-now,V);C.st++;C.mt+=sd;}
}
function campTile(x,y){return tget(Math.floor(x/TS),Math.floor(y/TS));}
function campCan(){
 if(!G)return 'Gerade nicht.';
 if(P.inCar)return 'Steig erst aus dem Van aus.';
 if(P.ride||P.coast||MG||P.build||P.fish||P.fight)return 'Gerade nicht möglich.';
 if(wanted>0)return 'Mit der Polizei im Nacken? Erst mal abhauen!';
 if(ZONE&&ZONE.name==='fpark')return 'Im Freizeitpark wird nicht gepicknickt. Draußen in der Stadt, am Strand oder im Wald geht es.';
 const n=inNoGo(P.x,P.y);if(n)return 'Hier ist '+n.n+'. Such dir einen anderen Platz.';
 const t=campTile(P.x,P.y);
 if(t===RD)return 'Mitten auf der Straße? Lieber nicht.';
 if(t===SH||t===DP||isDeep(P.x,P.y))return 'Im Wasser wird die Decke nass.';
 if(t===DK||t===IC)return 'Hier ist es zu wackelig oder zu glatt.';
 if(hit(P.x,P.y,12))return 'Hier ist zu wenig Platz. Geh ein Stück ins Freie.';
 return '';
}
function campFireSpot(C){
 const OK=[GR,SA,SN,AS,CF,FD];let why='Auf Pflaster und Asphalt wird kein Feuer gemacht. Auf Wiese, Sand oder Schnee geht es.';
 const L=[[0,-44],[0,48],[-50,0],[50,0]];
 for(let k=0;k<L.length;k++){
  const x=C.x+L[k][0],y=C.y+L[k][1],tx=Math.floor(x/TS),ty=Math.floor(y/TS);
  if(OK.indexOf(tget(tx,ty))<0||hit(x,y,10))continue;
  let near=false;for(let j=ty-1;j<=ty+1;j++)for(let i=tx-1;i<=tx+1;i++){const v=tget(i,j);if(v===TR||v===BL)near=true;}
  if(near){why='Zu nah an Bäumen oder Häusern. Such dir eine freiere Stelle.';continue;}
  return{x:x,y:y};
 }
 return{why:why};
}
function campFireWhy(){
 const C=CAMP;if(!C)return '';
 if(wxType()==='rain')return 'Bei dem Regen geht kein Feuer an.';
 const s=campFireSpot(C);return s.why||'';
}
function campStart(){
 const w=campCan();if(w){toast(w);return false;}
 if(CAMP)campEnd(true);
 CAMP={id:++campId,x:P.x,y:P.y,zone:ZONE?ZONE.name:'',music:false,si:-1,mt:0,st:0,grill:null,fire:null,roast:null,guests:0,party:false,ct:2,storyCd:0,gx:P.x-36,gy:P.y+4,sx:P.x+30,sy:P.y-4,fx:0,fy:0};
 closeAll();
 sitDown({x:P.x,y:P.y,t:'decke'});
 toast('Du breitest die Decke aus und machst es dir gemütlich.'+(G.box?'':' Mit einem Bluetooth-Lautsprecher aus dem Büdchen gäbe es auch Musik.'));
 return true;
}
function campNear(){return !!(CAMP&&!P.sit&&!P.inCar&&!P.ride&&!P.coast&&!MG&&Math.hypot(P.x-CAMP.x,P.y-CAMP.y)<42);}
function campSit(){if(!CAMP)return;P.x=CAMP.x;P.y=CAMP.y;sitDown({x:CAMP.x,y:CAMP.y,t:'decke'});}
function campRefresh(){if(UI.screen==='sit'&&!UI.modal&&P.sit&&P.sit.t==='decke')render2();}
function campGuests(){const C=CAMP;return C?peds.filter(p=>p.st==='party'&&p.cid===C.id):[];}
function campEnd(silent,why){
 const C=CAMP;if(!C)return;CAMP=null;
 let g=0,nf=0;
 for(let i=peds.length-1;i>=0;i--){
  const p=peds[i];if(p.st!=='party'||p.cid!==C.id)continue;
  g++;if(!p.like&&chance(.7)){p.like=true;nf++;}
  p.st='walk';p.pd=0;p.arr=false;
  if(p.tmp){addFx(p.x,p.y-18,'Tschüss!','#fff2b0',1.4);peds.splice(i,1);}
 }
 if(G){G.freunde=(G.freunde||0)+nf;if(g>=6)G.resp++;if(g)G.partys=(G.partys||0)+1;}
 if(P.sit&&P.sit.t==='decke')P.sit=null;
 if(silent)return;
 const tail=g?' Was für ein Treffen: '+g+' Gäste'+(nf?', '+nf+' neue Freunde':'')+(g>=6?'. +1 Respekt.':'.'):'';
 toast((why==='far'?'Du bist weitergezogen. Decke, Lautsprecher und Grill sind eingepackt, das Feuer ist sicher aus.':'Alles eingepackt, das Feuer ist sicher aus.')+tail);
}
function campPed(p,dt){
 if(p.st!=='party')return false;
 const C=CAMP;if(!C||p.cid!==C.id){p.st='walk';p.pd=0;p.arr=false;return false;}
 if(!p.arr){
  const dx=p.tx-p.x,dy=p.ty-p.y,d=Math.hypot(dx,dy);
  if(d<4)p.arr=true;
  else{
   const s=Math.min(d,58*dt),ox=p.x,oy=p.y;moveE(p,dx/d*s,dy/d*s,6);p.a=Math.atan2(dy,dx);p.walk+=s*.15;
   if(Math.hypot(p.x-ox,p.y-oy)<s*.3){p.stuck=(p.stuck||0)+dt;if(p.stuck>2.5){p.x=p.tx;p.y=p.ty;p.arr=true;}}else p.stuck=0;
  }
 }
 if(p.arr){p.pd=C.music?1:0;p.a=Math.atan2(C.y-p.y,C.x-p.x);if(p.pd)p.walk+=dt*6;}
 return true;
}
function campInvite(){
 const C=CAMP;if(!C)return;
 if(C.party){toast('Die Party läuft schon!');return;}
 if(!C.music&&!C.grill&&!C.fire){toast('Ohne Musik, Grill oder Feuer kommt keiner. Mach erst etwas an!');return;}
 C.party=true;
 const L=peds.filter(p=>p.st==='walk'&&!p.snow&&!p.oma&&Math.hypot(p.x-C.x,p.y-C.y)<650).sort((a,b)=>Math.hypot(a.x-C.x,a.y-C.y)-Math.hypot(b.x-C.x,b.y-C.y)).slice(0,8);
 const need=Math.max(0,5-L.length);
 for(let i=0;i<need*3&&L.length<5;i++){
  const a=rf(0,6.283),f=freeSpot(C.x+Math.cos(a)*300,C.y+Math.sin(a)*300),t=campTile(f.x,f.y);
  if(hit(f.x,f.y,7)||t===SH||t===DP||t===RD||inNoGo(f.x,f.y))continue;
  const q=mkPed(f.x,f.y);q.tmp=true;q.like=chance(.4);peds.push(q);L.push(q);
 }
 const n=L.length,cy=C.y-6;
 L.forEach((p,i)=>{
  const a=-Math.PI/2+.75+(n>1?i/(n-1):.5)*(6.283-1.5),rr=rf(66,84);
  let x=C.x+Math.cos(a)*rr,y=cy+Math.sin(a)*rr;
  const nok=(xx,yy)=>hit(xx,yy,7)||[RD,SH,DP].indexOf(campTile(xx,yy))>=0;
  if(nok(x,y)){let f=null;for(let tr=1;tr<=10&&!f;tr++){const aa=a+(tr%2?1:-1)*Math.ceil(tr/2)*.35,xx=C.x+Math.cos(aa)*rr,yy=cy+Math.sin(aa)*rr;if(!nok(xx,yy))f={x:xx,y:yy};}if(!f)f=freeSpot(x,y);x=f.x;y=f.y;}
  p.st='party';p.cid=C.id;p.arr=false;p.pd=0;p.stuck=0;p.tx=x;p.ty=y;
 });
 const kids=L.some(p=>p.kid||p.teen);
 sfx('clap');
 toast(n?(n+' Leute kommen vorbei'+(kids?'. Kinder und Jugendliche sind dabei: Heute gibt es nur Limo!':'. Party!')):'Hier ist gerade niemand. Aber die Musik ist trotzdem gut.');
 campRefresh();
}
function campMus(){
 const C=CAMP;if(!C)return;
 if(!G.box){toast('Du hast noch keinen Bluetooth-Lautsprecher. Den gibt es im Büdchen unter „Grill & Musik“.');return;}
 sndWake();
 if(!C.music){if(C.si<0){const pref=C.fire?3:ZONE&&ZONE.name==='strand'?0:ZONE&&(ZONE.name==='berge'||ZONE.name==='maerchen'||ZONE.name==='feldweg')?3:pick([1,2,4]);C.si=SONGS.findIndex(q=>q.gi===pref);}C.music=true;}
 else C.si=(C.si+1)%SONGS.length;
 C.mt=0;C.st=0;
 const S=SONGS[C.si];
 toast('♪ Jetzt läuft: „'+S.t+'“ ('+MUS[S.gi].g+')'+(SND.on?'':'. Der Ton ist aus, die Leute tanzen trotzdem.'));
 campRefresh();
}
function campGrill(){
 const C=CAMP;if(!C)return;
 if(!G.grill){toast('Du hast noch keinen Grill. Einen Klappgrill gibt es im Büdchen.');return;}
 const g=C.grill;
 if(!g){C.grill={st:'heat',t:0};sfx('ok');toast('Du klappst den Grill auf und zündest die Kohle an ...');}
 else if(g.st==='hot'){if(!(G.stock.wurst>0)){toast('Kein Grillgut mehr. Grillpakete gibt es im Büdchen.');return;}G.stock.wurst--;g.st='cook';g.t=0;sfx('splash');toast('Würstchen, Maiskolben und Grillkäse kommen auf den Rost. Es zischt!');}
 else if(g.st==='done'){
  const L=campGuests().filter(p=>p.arr);g.st='hot';g.t=0;
  mood(10,'+10 Grillen');sfx('clap');needAdd(60,5);
  L.forEach(p=>{if(!p.like&&chance(.5))p.like=true;addFx(p.x,p.y-20,pick(['Lecker!','Mmmh!','Danke!','Bester Grillkäse!']),'#ffd23f',1.6);});
  G.grillt=(G.grillt||0)+1;
  toast(L.length?'Alle bekommen etwas ab. '+L.length+' Leute strahlen dich mit vollem Mund an.':'Du isst ganz allein auf deiner Decke. Schmeckt trotzdem großartig.');
 }else toast('Einen Moment, das dauert noch.');
 campRefresh();
}
function campFire(){
 const C=CAMP;if(!C)return;
 if(C.fire){toast('Das Feuer brennt schon.');return;}
 if(!(G.stock.holz>0)){toast('Kein Feuerholz. Das gibt es im Büdchen.');return;}
 if(wxType()==='rain'){toast('Bei dem Regen geht kein Feuer an.');return;}
 const s=campFireSpot(C);if(s.why){toast(s.why);return;}
 G.stock.holz--;C.fire={t:0,life:150};C.fx=s.x;C.fy=s.y;sfx('ok');
 toast('Knister, knister: Das Lagerfeuer brennt! Steine drumherum, Eimer Wasser daneben, alles sicher.');
 campRefresh();
}
function campRoast(){
 const C=CAMP;if(!C||!C.fire)return;if(C.roast){toast('Gleich fertig!');return;}
 C.roast={t:0};toast('Du hältst Stockbrot und Marshmallows ins Feuer ...');campRefresh();
}
function campStory(){
 const C=CAMP;if(!C||!C.fire)return;if(C.storyCd>0){toast('Alle müssen erst mal verdauen.');return;}
 C.storyCd=12;mood(5,'+5 Geschichte');sfx('clap');
 campGuests().forEach(p=>{if(p.arr&&chance(.7))addFx(p.x,p.y-20,pick(['Haha!','Uuuh!','Und dann?','Nicht wahr!','Nochmal!']),'#fff2b0',1.6);});
 toast(pick(['Du erzählst vom Miesepeter, der aus Versehen seine eigene Currywurst stibitzt hat. Alle lachen.','Du erzählst vom Wal, der in seinem Bauch Tee kocht. Keiner glaubt dir, alle wollen mehr hören.','Die Geschichte vom Dixi-Klo, das innen größer ist als außen. Gänsehaut am Lagerfeuer!','Du erzählst, wie der Van einmal rückwärts schneller war als vorwärts. Applaus!']));
 campRefresh();
}
function campWood(){
 const C=CAMP;if(!C||!C.fire)return;if(!(G.stock.holz>0)){toast('Kein Feuerholz mehr.');return;}
 G.stock.holz--;C.fire.life=Math.min(C.fire.t+300,C.fire.life+120);sfx('ok');toast('Holz nachgelegt. Die Funken fliegen.');campRefresh();
}
function campUpdate(dt){
 const C=CAMP;if(!C||!G)return;
 const d=Math.hypot(P.x-C.x,P.y-C.y);
 if(d>900&&!P.sit){campEnd(false,'far');return;}
 if(C.fire){
  C.fire.t+=dt;
  if(chance(dt*7))FX.push({x:C.fx+rf(-6,6),y:C.fy-12,vx:rf(-10,10),vy:rf(-60,-30),t:0,life:rf(.5,1),dot:pick(['#ffd23f','#ff9a3c','#fff2b0']),r:rf(1,2)});
  if(chance(dt*1.4))smokeFx(C.fx+rf(-4,4),C.fy-26);
  if(d<300&&chance(dt*2.5))nz(.03,.05*(1-d/300),3000,'highpass');
  if(C.fire.t>=C.fire.life){C.fire=null;C.roast=null;toast('Das Lagerfeuer ist heruntergebrannt und aus.');campRefresh();}
 }
 const g=C.grill;
 if(g){
  g.t+=dt;if(chance(dt*(g.st==='cook'?3:g.st==='heat'?1.5:.6)))smokeFx(C.gx+rf(-5,5),C.gy-14);
  if(g.st==='heat'&&g.t>=5){g.st='hot';g.t=0;toast('Die Kohle glüht. Jetzt kann das Grillgut drauf!');sfx('ok');campRefresh();}
  else if(g.st==='cook'){if(d<300&&chance(dt*3))nz(.25,.03*(1-d/300),5000,'highpass');if(g.t>=8){g.st='done';g.t=0;toast('Fertig gegrillt! Es duftet über den ganzen Platz.');sfx('ok');campRefresh();}}
 }
 if(C.roast){C.roast.t+=dt;if(C.roast.t>=3.5){const ok=chance(.7);C.roast=null;mood(ok?6:3,ok?'+6 Stockbrot':'+3');toast(ok?pick(['Goldbraun! Das Stockbrot ist perfekt, die Marshmallows auch.','Perfekt geröstet. Klebrige Finger inklusive.']):'Leicht verkohlt. Schmeckt trotzdem nach Lagerfeuer.');campRefresh();}}
 if(C.storyCd>0)C.storyCd-=dt;
 const gs=campGuests(),gn=gs.length;
 if(gn!==C.guests){C.guests=gn;campRefresh();}
 if(C.music){
  if(chance(dt*1.3))addFx(C.sx+rf(-4,4),C.sy-14,pick(['♪','♫']),pick(['#ff5fd0','#5ff0ff','#ffd23f']),1.6,-30);
  peds.forEach(p=>{if(p.st==='walk'&&!p.snow&&chance(dt*.12)&&Math.hypot(p.x-C.x,p.y-C.y)<200){p.st='dance';p.stT=rf(3,6);}});
 }
 if(d<260){const v=(C.music?.5:0)+(C.fire?.4:0)+(C.grill?.2:0)+Math.min(8,gn)*.15+(P.sit?.2:0);G.mood=clamp(G.mood+v*dt,0,100);}
 C.ct-=dt;
 if(C.ct<=0){C.ct=rf(2,4.5);const A=gs.filter(p=>p.arr);if(A.length){const p=pick(A);let L=['Schön, dass du da bist!','Was für ein Abend!','Das sollten wir öfter machen!','Prost, mit Limo!','Ich kenn hier fast keinen. Egal!'];if(C.music)L=L.concat(['Toller Song!','Lauter!','Den kenn ich!','Tanzen!']);if(C.fire)L=L.concat(['Schön warm hier.','Guck mal, die Sterne!','Noch ein Stockbrot?']);if(g&&g.st==='done')L=L.concat(['Riecht das gut!','Ist das Grillkäse?']);addFx(p.x,p.y-22,pick(L),'#fff2b0',1.8);}}
}
function drawCamp(cx,cy){
 const C=CAMP;if(!C)return;
 if(C.x<cx-220||C.x>cx+VW+220||C.y<cy-220||C.y>cy+VH+220)return;
 const x=C.x,y=C.y;
 ctx.fillStyle='rgba(0,0,0,.22)';ctx.fillRect(x-19,y-8,45,28);
 for(let i=0;i<5;i++)for(let j=0;j<3;j++){ctx.fillStyle=(i+j)%2?'#fff4e6':'#e5504d';ctx.fillRect(x-22+i*9,y-12+j*9,9,9);}
 ctx.fillStyle='rgba(255,255,255,.5)';ctx.fillRect(x-22,y+14,45,2);
 if(C.fire){
  const fx=C.fx,fy=C.fy,k=clamp((C.fire.life-C.fire.t)/20,.25,1);
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(fx+3,fy+4,17,9,0,0,6.283);ctx.fill();
  for(let i=0;i<9;i++){const a=i/9*6.283;ctx.fillStyle=i%2?'#8d8d92':'#a3a3a8';circle(fx+Math.cos(a)*14,fy+Math.sin(a)*8,4);}
  ctx.save();ctx.translate(fx,fy);ctx.fillStyle='#6b4423';ctx.rotate(.5);ctx.fillRect(-11,-2.5,22,5);ctx.rotate(-1);ctx.fillRect(-11,-2.5,22,5);ctx.restore();
  [['#e5504d',1,0],['#ff9a3c',.8,1],['#ffd23f',.55,2]].forEach(f=>{
   for(let i=-1;i<=1;i++){const h=(14+7*Math.sin(timeNow*13+i*2.1+f[2]))*f[1]*k,w=6*f[1]*k+2;
    ctx.fillStyle=f[0];ctx.beginPath();ctx.moveTo(fx+i*5-w,fy);ctx.quadraticCurveTo(fx+i*5-w*.4,fy-h*.6,fx+i*5+Math.sin(timeNow*9+i)*2,fy-h);ctx.quadraticCurveTo(fx+i*5+w*.4,fy-h*.6,fx+i*5+w,fy);ctx.closePath();ctx.fill();}
  });
  if(C.roast){ctx.strokeStyle='#8a5a2a';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x,y-6);ctx.lineTo(fx+4,fy-8);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#e8c38a';ctx.beginPath();ctx.ellipse(fx+4,fy-9,4,2.5,0,0,6.283);ctx.fill();ctx.fillStyle='#fff';circle(fx+9,fy-11,2.2);}
 }
 if(C.grill){
  const gx=C.gx,gy=C.gy,g=C.grill;
  ctx.strokeStyle='#3a3a3a';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(gx-9,gy+10);ctx.lineTo(gx-6,gy);ctx.moveTo(gx+9,gy+10);ctx.lineTo(gx+6,gy);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#2b2b2b';ctx.beginPath();ctx.ellipse(gx,gy-2,15,9,0,0,6.283);ctx.fill();
  const glow=g.st==='heat'?.35+.25*Math.min(1,g.t/5):.7;ctx.fillStyle='rgba(255,'+Math.floor(90+60*Math.sin(timeNow*5))+',30,'+glow+')';ctx.beginPath();ctx.ellipse(gx,gy-2,12,7,0,0,6.283);ctx.fill();
  ctx.strokeStyle='#bfc4cb';for(let i=-9;i<=9;i+=3){ctx.beginPath();ctx.moveTo(gx+i,gy-8);ctx.lineTo(gx+i,gy+4);ctx.stroke();}
  if(g.st==='cook'||g.st==='done'){const k=g.st==='done'?1:Math.min(1,g.t/8),wc='rgb('+Math.floor(220-90*k)+','+Math.floor(150-80*k)+','+Math.floor(130-90*k)+')';
   ctx.fillStyle=wc;ctx.fillRect(gx-10,gy-6,9,3);ctx.fillRect(gx-10,gy-1,9,3);ctx.fillStyle='#f4d03f';ctx.fillRect(gx+2,gy-6,8,4);ctx.fillStyle=k>.8?'#e8c070':'#f4ecd0';ctx.fillRect(gx+2,gy,7,4);}
 }
 if(G.box){
  const sx=C.sx,sy=C.sy;
  if(C.music){const S=SONGS[C.si],b=1-((timeNow*MUS[S.gi].bpm/60)%1);ctx.strokeStyle='rgba(255,95,208,'+(.5*b)+')';ctx.lineWidth=2;ctx.beginPath();ctx.arc(sx,sy,10+b*6,0,6.283);ctx.stroke();ctx.lineWidth=1;}
  ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(sx-6,sy-2,16,11);
  ctx.fillStyle='#22262e';ctx.fillRect(sx-8,sy-5,16,11);
  ctx.fillStyle='#4a5160';circle(sx-3,sy,3.2);circle(sx+3,sy,3.2);
  ctx.fillStyle=C.music?'#5ff0ff':'#3a6070';ctx.fillRect(sx-1,sy-5,2,2);
 }
}
function campGlow(cx,cy){
 const C=CAMP;if(!C||!C.fire)return;
 const x=C.fx-cx,y=C.fy-cy-8;if(x<-200||x>VW+200||y<-200||y>VH+200)return;
 const h=!ZONE?hour():12,nt=(ZONE&&ZONE.dark)?.3:(!ZONE&&(h>=20||h<6))?.24:.1,a=nt+.04*Math.sin(timeNow*11);
 ctx.save();ctx.globalCompositeOperation='lighter';
 const g=ctx.createRadialGradient(x,y,4,x,y,150);g.addColorStop(0,'rgba(255,150,60,'+a+')');g.addColorStop(1,'rgba(255,120,40,0)');
 ctx.fillStyle=g;ctx.fillRect(x-150,y-150,300,300);ctx.restore();
}
function campScreen(){
 const C=CAMP;
 if(!C)return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>Picknickdecke</h2></div>'+btn('Aufstehen','stand',null,{def:1})+'</div>'};
 const nz=inNoGo(P.x,P.y),why=nz?'Hier ist '+nz.n+': Kein Alkohol, kein Rauch!':noUse(),st=G.stock,bd=!!why||st.bier<1,jd=!!why||st.joint<1;
 const S=C.si>=0?SONGS[C.si]:null;
 let b='';
 if(!G.box)b+=btn('Musik: kein Lautsprecher','campMus',null,{off:1,why:'Einen Bluetooth-Lautsprecher gibt es im Büdchen unter Grill und Musik.'});
 else if(!C.music)b+=btn(S?'Musik an: „'+S.t+'“':'Musik an','campMus',null,{def:1});
 else b+=btn('Nächster Song (läuft: „'+S.t+'“)','campMus',null,{def:1})+btn('Musik aus','campMusOff');
 const g=C.grill;
 b+=btn(!G.grill?'Grillen: kein Grill':!g?'Grill anheizen':g.st==='heat'?'Grill heizt an ...':g.st==='hot'?'Grillgut auflegen ('+(st.wurst||0)+')':g.st==='cook'?'Grillgut brutzelt ...':'Essen verteilen!','campGrill',null,{off:!G.grill||(g&&(g.st==='heat'||g.st==='cook'))||(g&&g.st==='hot'&&!(st.wurst>0)),why:!G.grill?'Einen Klappgrill gibt es im Büdchen.':(g&&g.st==='hot')?'Kein Grillgut mehr. Grillpakete gibt es im Büdchen.':'Einen Moment, das dauert noch.'});
 if(!C.fire){const fw=!(st.holz>0)?'Kein Feuerholz. Das gibt es im Büdchen.':campFireWhy();b+=btn('Lagerfeuer anzünden (Holz: '+(st.holz||0)+')','campFire',null,{off:!!fw,why:fw});}
 else{
  b+=btn(C.roast?'Stockbrot röstet ...':'Stockbrot und Marshmallows rösten','campRoast',null,{off:!!C.roast,why:'Gleich fertig!'});
  b+=btn('Geschichten am Feuer erzählen','campStory',null,{off:C.storyCd>0,why:'Alle müssen erst mal verdauen.'});
  if(st.holz>0&&C.fire.life-C.fire.t<60)b+=btn('Holz nachlegen ('+st.holz+')','campWood');
 }
 b+=btn(C.party?'Party läuft: '+C.guests+' Gäste':'Leute einladen: Party!','campParty',null,{off:C.party||(!C.music&&!C.grill&&!C.fire),why:C.party?'Die Party läuft schon!':'Mach erst Musik, Grill oder Feuer an.'});
 b+=btn('Bier trinken ('+st.bier+')','drink',null,{off:bd,why:why||'Kein Bier mehr. Das Büdchen hat Nachschub.'});
 b+=btn('Joint rauchen ('+st.joint+')','smoke',null,{off:jd,why:why||'Kein Joint mehr. Das Büdchen hat Nachschub.'});
 if(st.gluehwein>0)b+=btn('Glühwein trinken ('+st.gluehwein+')','glue',null,{off:!!why,why:why});
 b+=fwBtn();
 b+=btn('Alles einpacken','campPack')+btn('Aufstehen (Decke bleibt liegen)','stand');
 const info=[];if(C.music&&S)info.push('♪ '+MUS[S.gi].g);if(C.fire)info.push('Feuer brennt');if(C.party)info.push(C.guests+' Gäste');
 return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>Picknickdecke</h2><div class="mu">Laune: <b>'+moodWord()+'</b>'+(info.length?' · '+info.join(' · '):'')+'</div>'+(why?'<div class="mu rd">'+why+'</div>':'')+'</div>'+b+'</div>'};
}
function campShopScreen(){
 const st=G.stock;
 let b=btn(G.box?'Bluetooth-Lautsprecher: hast du schon':'Bluetooth-Lautsprecher: 25 €','campBuy','box',{off:!!G.box,why:'Du hast schon einen. Der hält ewig.',def:G.box?0:1});
 b+=btn(G.grill?'Klappgrill: hast du schon':'Klappgrill: 15 €','campBuy','grill',{off:!!G.grill,why:'Ein Grill reicht.'});
 b+=btn('Grillpaket (Würstchen, Mais, Grillkäse): 4 € · hast '+(st.wurst||0),'campBuy','wurst',{def:G.box?1:0});
 b+=btn('Feuerholz für ein Lagerfeuer: 3 € · hast '+(st.holz||0),'campBuy','holz');
 b+=btn('Feuerwerks-Batterie (9 Raketen): 12 € · hast '+(st.fw||0),'campBuy','fw');
 b+=btn('Zurück','back');
 return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>Grill, Musik und Feuerwerk</h2><div class="mu">Bargeld <b class="gr">'+eur(G.cash)+'</b></div><div class="mu">Tipp: Im Rucksack breitest du überall die Decke aus.</div></div>'+b+'</div>'};
}
function campPackBtn(){return btn('Decke ausbreiten: Musik, Grill, Lagerfeuer','campStart')+fwBtn();}
const CAMPACT={
 campStart(){campStart();},
 campShop(){show('campshop');},
 campBuy(k){
  const pr={box:25,grill:15,wurst:4,holz:3,fw:12}[k];if(!pr)return;
  if(G.cash<pr){toast('Nicht genug Geld.');return;}
  if((k==='box'&&G.box)||(k==='grill'&&G.grill))return;
  if((k==='wurst'&&(G.stock.wurst||0)>=20)||(k==='holz'&&(G.stock.holz||0)>=20)||(k==='fw'&&(G.stock.fw||0)>=10)){toast('Mehr passt nicht in den Rucksack.');return;}
  G.cash-=pr;sfx('coin');
  if(k==='box'){G.box=true;toast('Bluetooth-Lautsprecher gekauft! Im Rucksack: Decke ausbreiten, dann Musik an.');}
  else if(k==='grill'){G.grill=true;toast('Klappgrill gekauft. Passt zusammengeklappt in jeden Rucksack.');}
  else if(k==='wurst'){G.stock.wurst=(G.stock.wurst||0)+1;toast('Ein Grillpaket: Würstchen, Maiskolben und Grillkäse. Reicht für alle.');}
  else if(k==='fw'){G.stock.fw=(G.stock.fw||0)+1;toast('Eine Feuerwerks-Batterie mit neun Raketen. Zünden im Rucksack oder auf der Decke, draußen und nicht bei den Kindern.');}
  else{G.stock.holz=(G.stock.holz||0)+1;toast('Ein Bündel Feuerholz, trocken und sauber gestapelt.');}
  render2();
 },
 campMus(){campMus();},
 campMusOff(){if(CAMP){CAMP.music=false;toast('Musik aus. Man hört wieder die Vögel.');}render2();},
 campGrill(){campGrill();},
 campFire(){campFire();},
 campRoast(){campRoast();},
 campStory(){campStory();},
 campWood(){campWood();},
 campParty(){campInvite();},
 campPack(){campEnd(false);closeAll();},
 fwFire(){fwOwn();}
};

function genExtras3(){
 clearBld(77,33,90,44);fillR(77,33,14,12,SW);
 addB(78,33,7,4,'#c0392b','FEUERWACHE','feuerwache',9);
 mkm('fw','','sk',81,37,'Feuerwache','#ff6a3c');{const m=MKS[MKS.length-1];m.sk='fw';m.act='Feuerwache: Feuerlöscher und Tipps';}
 addB(78,39,12,5,'#e4ebf0','KRANKENHAUS','kh',10);
 mkm('kh','','sk',83,44,'Krankenhaus St. Rheinhanfen','#ff6a3c');{const m=MKS[MKS.length-1];m.sk='kh';m.act='Krankenhaus besuchen';}
 [[87,33],[89,33],[89,36],[86,36]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
 putBK(88,35,[SW]);
 HYD.length=0;
 for(let r=0;r<4;r++)for(let c=0;c<6;c++){
  const b=blockOf(c,r),cand=[[b.x0,b.y0+3],[b.x1,b.y1-3],[b.x0+4,b.y1],[b.x1-4,b.y0],[b.x0,b.y1-2]];
  for(let i=0;i<cand.length;i++){const q=cand[i];if(T[q[1]*MW+q[0]]===SW&&!inNoGo(q[0]*TS+16,q[1]*TS+16)){HYD.push({x:q[0]*TS+16,y:q[1]*TS+12});break;}}
 }
}
const FIRE_X=['HANFBIER','KITA SONNENSCHEIN','KRANKENHAUS','FEUERWACHE','HANF-LABOR','VEREINSHEIM','BÜDCHEN'];
function fireCands(){return CITY.BLD.filter(b=>(b.k==='house'||b.k==='glass'||b.k==='barn')&&FIRE_X.indexOf(b.n)<0&&b.w>=2&&b.h>=2);}
function firePt(hp){const F=FIRE,r=F.rect;F.pts.push({x:r[0]+Math.random()*r[2],y:r[1]+Math.random()*r[3],hp:hp||35});}
function fireStart(b){
 if(FIRE||TRUCK||ZONE||!G)return false;
 if(!b){const L=fireCands().filter(q=>{const d=Math.hypot((q.x+q.w/2)*TS-P.x,(q.y+q.h/2)*TS-P.y);return d>280&&d<1200;});if(!L.length)return false;b=pick(L);}
 const rx=b.x*TS,ry=b.y*TS,rw=b.w*TS,rh=b.h*TS-b.hh;
 FIRE={k:'house',b:b,cx:rx+rw/2,cy:ry+rh/2,rect:[rx+8,ry+6,Math.max(4,rw-16),Math.max(4,rh-12)],pts:[],t:0,spawnT:0,pd:0,td:0,alarm:rf(22,30),max:Math.min(5,2+Math.floor(b.w*b.h/10)),st:'burn',outT:0,talk:2};
 firePt(40);
 toast('Feuer! In einem Haus in der Nähe brennt es. Die Feuerwehr ist alarmiert. Mit Feuerlöscher oder Hydranten-Schlauch kannst du helfen!');
 fireSiren(1);
 return true;
}
function fireTree(tx,ty,why){
 if(FIRE||TRUCK||ZONE||!G)return false;
 const x=tx*TS+16,y=ty*TS+12;
 FIRE={k:'tree',tx:tx,ty:ty,cx:x,cy:y,rect:[x-8,y-8,16,14],pts:[],t:0,spawnT:0,pd:0,td:0,alarm:rf(20,28),max:2,st:'burn',outT:0,talk:2};
 firePt(55);toast(why);fireSiren(1);
 return true;
}
function fireSiren(v){const V=.04*v;tn(880,.18,'square',V);tn(660,.18,'square',V,0,.2);tn(880,.18,'square',V,0,.4);tn(660,.18,'square',V,0,.6);}
function boltStrike(force){
 if(ZONE||FIRE||TRUCK||!G)return;
 if(!force&&!chance(.45))return;
 const x0=Math.floor(cam.x/TS),y0=Math.floor(cam.y/TS),L=[];
 for(let y=y0;y<y0+18;y++)for(let x=x0;x<x0+31;x++)if(tget(x,y)===TR&&!BURNT.some(b=>Math.abs(b.x-(x*TS+16))<4&&Math.abs(b.y-(y*TS+12))<4))L.push([x,y]);
 if(!L.length)return;
 const q=pick(L);BOLT={x:q[0]*TS+16,y:q[1]*TS+12,t:.4,j:[0,1,2,3,4,5].map(()=>rf(-18,18))};shake=Math.max(shake,.6);
 fireTree(q[0],q[1],'Blitzeinschlag! Ein Baum hat Feuer gefangen. Die Feuerwehr ist unterwegs.');
}
function roadNear(x,y){let best=null,bd=1e9;const tx=Math.floor(x/TS),ty=Math.floor(y/TS);for(let j=ty-9;j<=ty+9;j++)for(let i=tx-9;i<=tx+9;i++){if(tget(i,j)!==RD)continue;const d=Math.hypot(i*TS+16-x,j*TS+16-y);if(d<bd){bd=d;best={i:i,j:j};}}return best;}
function truckSpawn(){
 const F=FIRE,r=roadNear(F.cx,F.cy);if(!r){F.alarm=F.t+20;return;}
 const v=VR.find(q=>r.i===q||r.i===q+1),h=HR.find(q=>r.j===q||r.j===q+1);
 let tx,ty,sx,sy;
 if(v!==undefined){tx=(v+1)*TS;ty=r.j*TS+16;sy=ty-760>TS?ty-760:ty+760;sy=clamp(sy,TS,MH*TS-TS);sx=tx;}
 else{const hh=h!==undefined?h:r.j;ty=(hh+1)*TS;tx=r.i*TS+16;sx=tx-760>6*TS?tx-760:tx+760;sx=clamp(sx,6*TS,MW*TS-TS);sy=ty;}
 TRUCK={x:sx,y:sy,tx:tx,ty:ty,a:Math.atan2(ty-sy,tx-sx),st:'drive',men:[],t:0,sir:0};
}
function menSpawn(){
 const K=TRUCK,F=FIRE;if(!F)return;
 for(let i=0;i<3;i++){
  const m={x:K.x+rf(-12,12),y:K.y+rf(-12,12),a:0,walk:0,st:'run',hx:false,hy:false,stuck:0,i:i};
  menPlace(m,i);K.men.push(m);
 }
}
function menPlace(m,i){
 const F=FIRE;if(!F)return;
 const A=F.pts.filter(p=>p.hp>0);const p=A.length?A[i%A.length]:{x:F.cx,y:F.cy};
 const a=Math.atan2(TRUCK.y-p.y,TRUCK.x-p.x)+(i-1)*.55,d=rf(70,92);
 const f=freeSpot(p.x+Math.cos(a)*d,p.y+Math.sin(a)*d);m.sx=f.x;m.sy=f.y;m.st='run';m.stuck=0;
}
function manWalk(m,tx,ty,sp,dt){
 const dx=tx-m.x,dy=ty-m.y,d=Math.hypot(dx,dy);if(d<5)return true;
 const s=Math.min(d,sp*dt),ox=m.x,oy=m.y;moveE(m,dx/d*s,dy/d*s,6);m.a=Math.atan2(dy,dx);m.walk+=s*.15;
 if(Math.hypot(m.x-ox,m.y-oy)<s*.3){m.stuck+=dt;if(m.stuck>2.5){m.x=tx;m.y=ty;return true;}}else m.stuck=0;
 return false;
}
function truckUpdate(dt){
 const K=TRUCK;if(!K)return;K.t+=dt;
 K.sir-=dt;
 if(K.sir<=0&&(K.st==='drive'||(K.st==='park'&&K.t<6)||K.st==='leave'&&K.t<2)){K.sir=.9;const dd=Math.hypot(K.x-P.x,K.y-P.y),v=clamp(1-dd/1100,0,1)*.045;if(v>.003){tn(466,.42,'square',v);tn(622,.42,'square',v,0,.45);}}
 if(K.st==='drive'){
  const d=Math.hypot(K.tx-K.x,K.ty-K.y),sp=Math.min(270,50+d*1.3);
  if(d<4){K.x=K.tx;K.y=K.ty;K.st='park';K.t=0;menSpawn();if(Math.hypot(K.x-P.x,K.y-P.y)<800)toast('Tatü-tata! Die Feuerwehr ist da und rollt die Schläuche aus.');}
  else{K.x+=(K.tx-K.x)/d*sp*dt;K.y+=(K.ty-K.y)/d*sp*dt;}
 }else if(K.st==='park'){
  const F=FIRE,act=F&&F.st==='burn';
  K.men.forEach(m=>{
   if(!act&&m.st!=='in'&&m.st!=='back')m.st='back';
   if(m.st==='run'){if(manWalk(m,m.sx,m.sy,88,dt))m.st='spray';}
   else if(m.st==='spray'){
    let p=null,bd=1e9;F.pts.forEach(q=>{if(q.hp<=0)return;const d=Math.hypot(q.x-m.x,q.y-m.y);if(d<bd){bd=d;p=q;}});
    if(!p)return;
    if(bd>140){menPlace(m,m.i);return;}
    m.a=Math.atan2(p.y-m.y,p.x-m.x);m.tg=p;const dm=16*dt;p.hp-=dm;F.td+=dm;
    if(chance(dt*14))FX.push({x:m.x+Math.cos(m.a)*10,y:m.y+Math.sin(m.a)*10,vx:Math.cos(m.a)*rf(240,300)+rf(-20,20),vy:Math.sin(m.a)*rf(240,300)+rf(-20,20),t:0,life:bd/280,dot:'rgba(120,200,255,.9)',r:rf(1.5,2.4)});
    if(chance(dt*3))smokeFx(p.x+rf(-6,6),p.y-6);
   }else if(m.st==='back'){if(manWalk(m,K.x,K.y,90,dt))m.st='in';}
  });
  if(!act&&K.men.every(m=>m.st==='in')){K.st='leave';K.t=0;K.lx=K.x+Math.cos(K.a)*950;K.ly=K.y+Math.sin(K.a)*950;}
 }else if(K.st==='leave'){
  const d=Math.hypot(K.lx-K.x,K.ly-K.y),sp=Math.min(260,60+K.t*120);
  if(d<6)TRUCK=null;else{K.x+=(K.lx-K.x)/d*sp*dt;K.y+=(K.ly-K.y)/d*sp*dt;}
 }
}
function fireNearPt(R){const F=FIRE;if(!F||F.st!=='burn')return null;let b=null,bd=R;F.pts.forEach(p=>{if(p.hp<=0)return;const d=Math.hypot(p.x-P.x,p.y-P.y);if(d<bd){bd=d;b=p;}});return b;}
function sprayStart(){
 if(P.hose){P.spray={t:.6,k:'hose',a:P.a};sfx('squirt');return true;}
 if(!(G.ext>0))return false;
 G.ext=Math.max(0,G.ext-10);P.spray={t:.55,k:'ext',a:P.a};sfx('puff');
 if(G.ext<=0)toast('Der Feuerlöscher ist leer. In der Feuerwache wird er wieder aufgefüllt.');
 return true;
}
function sprayUpdate(dt){
 const S=P.spray;if(!S)return;S.t-=dt;if(S.t<=0){P.spray=null;return;}
 const R=S.k==='hose'?210:140,p=fireNearPt(R);
 S.a=p?Math.atan2(p.y-P.y,p.x-P.x):P.a;P.a=S.a;
 const ca=Math.cos(S.a),sa=Math.sin(S.a);
 if(p){const dm=(S.k==='hose'?75:55)*dt;p.hp-=dm;FIRE.pd+=dm;FIRE.td+=dm;if(chance(dt*6))smokeFx(p.x+rf(-6,6),p.y-6);}
 for(let i=0;i<2;i++)FX.push({x:P.x+ca*12,y:P.y+sa*12,vx:ca*rf(250,330)+rf(-24,24),vy:sa*rf(250,330)+rf(-24,24),t:0,life:(p?Math.hypot(p.x-P.x,p.y-P.y):R*.8)/300,dot:S.k==='hose'?'rgba(120,200,255,.9)':'rgba(245,247,250,.95)',r:rf(1.6,S.k==='hose'?2.6:3.4)});
 peds.forEach(q=>{
  if(q.snow||q.st==='lie')return;const d=Math.hypot(q.x-P.x,q.y-P.y);if(d>R)return;
  const da=Math.abs(((Math.atan2(q.y-P.y,q.x-P.x)-S.a)%6.283+9.425)%6.283-3.1416);
  if(da<.3&&!(q.wetCd>0)){q.wetCd=4;addFx(q.x,q.y-18,pick(q.kid?['Nochmal!','Hihi, nass!','Mehr!']:['Huch, nass!','Hey!','Erfrischend!','Mein Hemd!']),'#9fd8ff',1.3);if(chance(.5))mood(1,'+1');}
 });
}
function fireOut(forced){
 const F=FIRE;if(!F||F.st!=='burn')return;F.st='out';F.outT=0;
 const share=F.td>0?F.pd/F.td:0,early=!TRUCK||TRUCK.st==='drive';
 if(F.k==='tree'){BURNT.push({x:F.cx,y:F.cy});if(BURNT.length>24)BURNT.shift();}else F.b.soot=120;
 if(share>=.3&&!forced){
  const r=r10(60+share*140+(early?80:0));G.cash+=r;G.fwN=(G.fwN||0)+1;G.hero=(G.hero||0)+1;if(share>.6)G.resp++;
  mood(10,'+10 Held');sfx('win');
  toast((early?'Du warst schneller als die Feuerwehr! ':'')+'Feuer aus! '+(F.k==='tree'?'Der Baum ist gerettet, nur ein bisschen angekokelt.':'Alle sind wohlauf, nur das Dach ist rußig.')+' Die Feuerwehr bedankt sich mit '+eur(r)+' aus der Kaffeekasse'+(share>.6?' und +1 Respekt.':'.'));
 }else if(Math.hypot(F.cx-P.x,F.cy-P.y)<900)toast('Feuer aus! Die Feuerwehr hat alles im Griff. Niemand ist verletzt.');
}
function koHospital(txt){
 if(fade||!G)return;
 P.burn=0;P.hose=null;P.spray=null;
 if(P.sit)P.sit=null;if(P.ride)leaveRide(true);if(P.inCar)P.inCar=false;
 closeAll();
 startFade(txt,()=>{
  toCity();const m=MKQ.kh,f=freeSpot(m.x,m.y+22);P.x=f.x;P.y=f.y;P.vx=P.vy=0;
  const z=Math.min(G.cash,10);G.cash-=z;G.mood=Math.max(25,G.mood-10);G.kh=(G.kh||0)+1;
  cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
  toast(pick(['Du wachst im Krankenhaus auf. Ein bisschen Ruß im Gesicht, sonst alles gut. Zuzahlung: '+eur(z)+'.','Die Pflegerin lächelt: „Nur ein Schreck und ein Pflaster.“ Du darfst gleich wieder los. Zuzahlung: '+eur(z)+'.']));
 });
}
function fireReset(){P.hose=null;P.spray=null;P.burn=0;FIRE=null;TRUCK=null;BOLT=null;FIRESM.length=0;FWR.length=0;FWP.length=0;FWQ.length=0;FWS=null;}
function fireUpdate(dt){
 if(!G)return;
 if(P.hose&&(ZONE||P.inCar||P.ride||P.sit||P.coast))P.hose=null;
 if(P.hose){const dx=P.x-P.hose.x,dy=P.y-P.hose.y,d=Math.hypot(dx,dy);if(d>260){P.x=P.hose.x+dx/d*260;P.y=P.hose.y+dy/d*260;if(!P.hoseTip){P.hoseTip=1;toast('Der Schlauch ist zu Ende. Weiter geht es nicht.');}}}
 sprayUpdate(dt);
 if(P.tiny>0)P.tiny-=dt;
 if(BOLT){BOLT.t-=dt;if(BOLT.t<=0)BOLT=null;}
 for(let i=FIRESM.length-1;i>=0;i--){const s=FIRESM[i];s.t+=dt;s.x+=s.vx*dt;s.y+=s.vy*dt;if(s.t>=s.life)FIRESM.splice(i,1);}
 peds.forEach(q=>{if(q.wetCd>0)q.wetCd-=dt;});
 if(!ZONE){
  CITY.BLD.forEach(b=>{if(b.soot>0)b.soot-=dt;});
  fireT-=dt;if(fireT<=0){fireT=rf(150,260);if(!FIRE&&!TRUCK&&!fade&&wanted===0&&chance(.75))fireStart();}
 }
 truckUpdate(dt);
 const F=FIRE;
 if(!F){P.burn=Math.max(0,(P.burn||0)-dt);return;}
 F.t+=dt;
 if(F.st==='out'){F.outT+=dt;if(F.outT>15)FIRE=null;return;}
 const rain=wxType()==='rain';let alive=0;
 F.pts.forEach(p=>{
  if(p.hp<=0)return;alive++;
  p.hp=Math.min(100,p.hp+(F.k==='tree'&&rain?2.5:6)*dt);
  if(chance(dt*3.2)&&FIRESM.length<140)FIRESM.push({x:p.x+rf(-5,5),y:p.y-10,vx:rf(-6,10),vy:-rf(22,36),t:0,life:rf(2,3),r:rf(5,8)});
  if(chance(dt*4))FX.push({x:p.x+rf(-6,6),y:p.y-10,vx:rf(-14,14),vy:rf(-70,-40),t:0,life:rf(.5,.9),dot:pick(['#ffd23f','#ff9a3c']),r:rf(1,2)});
 });
 F.spawnT+=dt;if(F.spawnT>7&&alive>0&&alive<F.max){F.spawnT=0;firePt(30);}
 if(alive===0){fireOut(false);return;}
 if(F.t>240){F.pts.forEach(p=>{p.hp=0;});fireOut(true);return;}
 if(!TRUCK&&F.t>=F.alarm)truckSpawn();
 const d0=Math.hypot(F.cx-P.x,F.cy-P.y);
 if(d0<320&&chance(dt*2.2))nz(.04,.05*(1-d0/320),2600,'highpass');
 peds.forEach(q=>{if(q.st!=='walk'||q.snow)return;const d=Math.hypot(q.x-F.cx,q.y-F.cy);if(d<150){q.a=Math.atan2(q.y-F.cy,q.x-F.cx);q.t=2;}});
 F.talk-=dt;if(F.talk<=0){F.talk=rf(3,6);const L=peds.filter(q=>q.st==='walk'&&!q.snow&&Math.hypot(q.x-F.cx,q.y-F.cy)<340);if(L.length){const q=pick(L);addFx(q.x,q.y-20,pick(['Feuer!','Ruft die 112!','Da qualmt es!','Alle weg da!','Wo bleibt die Feuerwehr?']),'#ffb36a',1.6);}}
 let near=false;F.pts.forEach(p=>{if(p.hp>30&&Math.hypot(p.x-P.x,p.y-P.y)<26)near=true;});
 if(near&&!P.inCar){P.burn=(P.burn||0)+dt;if(chance(dt*3))addFx(P.x,P.y-20,pick(['Aua, heiß!','Heiß, heiß!','Weg vom Feuer!']),'#ff9a3c',1);if(P.burn>3)koHospital('Die Hitze war zu viel. Dir wird schwarz vor Augen ...');}
 else P.burn=Math.max(0,(P.burn||0)-dt*.5);
}
function drawFlame(x,y,s){
 [['#e5504d',1,0],['#ff9a3c',.78,1.3],['#ffd23f',.5,2.6]].forEach(f=>{
  for(let i=-1;i<=1;i++){const h=(s*1.4+s*.5*Math.sin(timeNow*13+i*2.1+f[2]+x))*f[1],w=s*.45*f[1]+1.5,ox=i*s*.4;
   ctx.fillStyle=f[0];ctx.beginPath();ctx.moveTo(x+ox-w,y);ctx.quadraticCurveTo(x+ox-w*.4,y-h*.6,x+ox+Math.sin(timeNow*9+i+x)*2,y-h);ctx.quadraticCurveTo(x+ox+w*.4,y-h*.6,x+ox+w,y);ctx.closePath();ctx.fill();}
 });
}
function drawSprayLine(x,y,a,len,col){
 ctx.strokeStyle=col;ctx.lineWidth=2;ctx.setLineDash([6,5]);ctx.lineDashOffset=-timeNow*80;
 for(let k=-1;k<=1;k++){const aa=a+k*.05;ctx.beginPath();ctx.moveTo(x+Math.cos(a)*10,y+Math.sin(a)*10);ctx.lineTo(x+Math.cos(aa)*len,y+Math.sin(aa)*len);ctx.stroke();}
 ctx.setLineDash([]);ctx.lineWidth=1;
}
function drawTruck(K){
 ctx.save();ctx.translate(K.x,K.y);ctx.rotate(K.a);
 ctx.fillStyle='rgba(0,0,0,.3)';ctx.fillRect(-30,-11,64,26);
 ctx.fillStyle='#c0392b';ctx.fillRect(-32,-13,64,26);
 ctx.fillStyle='#e5504d';ctx.fillRect(16,-12,15,24);
 ctx.fillStyle='#bfe3f5';ctx.fillRect(25,-10,5,20);
 ctx.fillStyle='#d8dde4';ctx.fillRect(-28,-5,40,3);ctx.fillRect(-28,2,40,3);for(let i=-26;i<12;i+=6)ctx.fillRect(i,-5,1.5,10);
 ctx.fillStyle='#f4f4f4';ctx.fillRect(-32,-13,64,2.5);ctx.fillRect(-32,10.5,64,2.5);
 const bl=Math.floor(timeNow*6)%2;ctx.fillStyle=bl?'#3f8cff':'#0b3a99';ctx.fillRect(18,-11,4,6);ctx.fillStyle=bl?'#0b3a99':'#3f8cff';ctx.fillRect(18,5,4,6);
 ctx.restore();
 if(TRUCK&&TRUCK.st!=='drive'&&Math.floor(timeNow*3)%2){ctx.fillStyle='rgba(63,140,255,.18)';circle(K.x,K.y,46);}
}
function drawFireWorld(cx,cy){
 const iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 CITY.BLD.forEach(b=>{if(!(b.soot>0)||!iv(b.x*TS,b.y*TS,300))return;const a=Math.min(1,b.soot/30)*.45;ctx.fillStyle='rgba(30,26,24,'+a+')';const x=b.x*TS,y=b.y*TS,w=b.w*TS,h=b.h*TS-b.hh;ctx.beginPath();ctx.ellipse(x+w*.4,y+h*.45,w*.32,h*.3,.3,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(x+w*.62,y+h*.55,w*.22,h*.22,0,0,6.283);ctx.fill();});
 BURNT.forEach(b=>{if(!iv(b.x,b.y,30))return;ctx.fillStyle='rgba(28,22,18,.78)';circle(b.x,b.y+4,13);ctx.fillStyle='rgba(70,60,50,.8)';circle(b.x-3,b.y+1,7);});
 HYD.forEach(h=>{if(!iv(h.x,h.y,20))return;ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(h.x+2,h.y+5,6,3,0,0,6.283);ctx.fill();ctx.fillStyle='#c0392b';ctx.fillRect(h.x-4,h.y-8,8,12);ctx.fillStyle='#e5504d';circle(h.x,h.y-8,4.5);ctx.fillStyle='#d8dde4';ctx.fillRect(h.x-7,h.y-4,3,3);ctx.fillRect(h.x+4,h.y-4,3,3);});
 if(G&&G.schatz&&iv(G.schatz.x,G.schatz.y,30)){const s=G.schatz;ctx.strokeStyle='#b03020';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(s.x-10,s.y-10);ctx.lineTo(s.x+10,s.y+10);ctx.moveTo(s.x+10,s.y-10);ctx.lineTo(s.x-10,s.y+10);ctx.stroke();ctx.lineWidth=1;if(Math.floor(timeNow*2)%2){ctx.fillStyle='#ffd23f';ctx.font='bold 11px Arial';ctx.textAlign='center';ctx.fillText('?',s.x,s.y-16);ctx.textAlign='start';}}
 if(P.hose){ctx.strokeStyle='#8a1f1f';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(P.hose.x,P.hose.y-4);ctx.quadraticCurveTo((P.hose.x+P.x)/2+12,(P.hose.y+P.y)/2+18,P.x,P.y);ctx.stroke();ctx.lineWidth=1;}
 const K=TRUCK;
 if(K){
  if(K.st==='park')K.men.forEach(m=>{if(m.st==='in')return;ctx.strokeStyle='#a83226';ctx.lineWidth=2.5;ctx.beginPath();ctx.moveTo(K.x,K.y);ctx.quadraticCurveTo((K.x+m.x)/2+10,(K.y+m.y)/2+16,m.x,m.y);ctx.stroke();ctx.lineWidth=1;});
  if(iv(K.x,K.y,80))drawTruck(K);
  K.men.forEach(m=>{if(m.st==='in'||!iv(m.x,m.y,30))return;drawPerson(m.x,m.y,m.a,'#2c3e50','ped',m.walk,.95);ctx.fillStyle='#f1c40f';circle(m.x,m.y,4.6);ctx.fillStyle='#c9a00c';circle(m.x-1,m.y,2);
   if(m.st==='spray'&&m.tg&&m.tg.hp>0)drawSprayLine(m.x,m.y,m.a,Math.hypot(m.tg.x-m.x,m.tg.y-m.y),'rgba(140,210,255,.85)');});
 }
 if(P.spray){const S=P.spray,p=fireNearPt(S.k==='hose'?210:140);drawSprayLine(P.x,P.y,S.a,p?Math.hypot(p.x-P.x,p.y-P.y):(S.k==='hose'?170:110),S.k==='hose'?'rgba(140,210,255,.9)':'rgba(250,250,252,.95)');}
 if(G&&G.ext>0&&!P.inCar&&!P.ride){ctx.fillStyle='#c0392b';ctx.fillRect(P.x+6,P.y+2,4,8);ctx.fillStyle='#222';ctx.fillRect(P.x+6,P.y+1,4,2);}
 FIRESM.forEach(s=>{if(!iv(s.x,s.y,40))return;const k=s.t/s.life;ctx.fillStyle='rgba(55,52,50,'+(.42*(1-k))+')';circle(s.x,s.y,s.r+k*16);});
 const F=FIRE;
 if(F&&F.st==='burn'){
  F.pts.forEach(p=>{if(p.hp>0&&iv(p.x,p.y,60))drawFlame(p.x,p.y,6+p.hp*.13);});
  const d=Math.hypot(F.cx-P.x,F.cy-P.y);
  if(d>300&&G){const a=Math.atan2(F.cy-P.y,F.cx-P.x);ctx.save();ctx.translate(P.x+Math.cos(a)*58,P.y+Math.sin(a)*58);ctx.rotate(a);ctx.fillStyle='#ff6a3c';ctx.strokeStyle='#000';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(11,0);ctx.lineTo(-6,-8);ctx.lineTo(-3,0);ctx.lineTo(-6,8);ctx.closePath();ctx.fill();ctx.stroke();ctx.restore();ctx.lineWidth=1;}
 }
 if(BOLT){const b=BOLT;ctx.strokeStyle='rgba(255,250,200,'+Math.min(1,b.t*3)+')';ctx.lineWidth=3;ctx.beginPath();let y=cy-20;ctx.moveTo(b.x+b.j[0],y);for(let i=1;i<6;i++){y=cy-20+(b.y-cy+20)*i/6;ctx.lineTo(b.x+b.j[i],y);}ctx.lineTo(b.x,b.y);ctx.stroke();ctx.lineWidth=1;}
}
function fireGlow(cx,cy){
 const F=FIRE;if(!F||F.st!=='burn'||ZONE)return;
 const h=hour(),nt=(h>=20||h<6)?.28:.12;
 ctx.save();ctx.globalCompositeOperation='lighter';
 F.pts.forEach(p=>{if(p.hp<=0)return;const x=p.x-cx,y=p.y-cy-8;if(x<-150||x>VW+150||y<-150||y>VH+150)return;const R=40+p.hp*.9,g=ctx.createRadialGradient(x,y,3,x,y,R);g.addColorStop(0,'rgba(255,140,50,'+(nt+.05*Math.sin(timeNow*9+p.x))+')');g.addColorStop(1,'rgba(255,100,30,0)');ctx.fillStyle=g;ctx.fillRect(x-R,y-R,2*R,2*R);});
 ctx.restore();
}
function hydNear(){let b=null,bd=34;HYD.forEach(h=>{const d=Math.hypot(h.x-P.x,h.y-P.y);if(d<bd){bd=d;b=h;}});return b;}
function firePromptEarly(){
 if(!G||P.inCar||P.ride||P.fish||P.fight)return '';
 if(P.hose){if(fireNearPt(210))return 'OK: Wasser marsch!';if(Math.hypot(P.hose.x-P.x,P.hose.y-P.y)<34)return 'OK: Schlauch abbauen';return 'OK: Spritzen';}
 if(G.ext>0&&fireNearPt(140))return 'OK: Löschen! (Feuerlöscher '+Math.round(G.ext)+' %)';
 return '';
}
function fireActEarly(){
 if(!G||P.inCar||P.ride||P.fish||P.fight||P.sit||P.build)return false;
 if(P.hose){if(!fireNearPt(210)&&Math.hypot(P.hose.x-P.x,P.hose.y-P.y)<34){P.hose=null;sfx('back');toast('Schlauch abgebaut und ordentlich aufgerollt.');return true;}sprayStart();return true;}
 if(G.ext>0&&fireNearPt(140)){sprayStart();return true;}
 return false;
}
function firePromptMid(){
 if(!G||ZONE||P.inCar||P.ride)return '';
 if(hydNear())return 'OK: Schlauch am Hydranten anschließen';
 if(G.schatz&&Math.hypot(G.schatz.x-P.x,G.schatz.y-P.y)<28)return 'OK: Schatz ausgraben';
 return '';
}
function fireActMid(){
 if(!G||ZONE||P.inCar||P.ride||P.sit||P.build)return false;
 const h=hydNear();
 if(h){P.hose={x:h.x,y:h.y};P.hoseTip=0;sfx('splash');toast(FIRE&&FIRE.st==='burn'?'Schlauch dran! Lauf zum Feuer und drück OK: Wasser marsch!':'Schlauch angeschlossen. OK spritzt, am Hydranten wieder abbauen.');return true;}
 if(G.schatz&&Math.hypot(G.schatz.x-P.x,G.schatz.y-P.y)<28){P.build={k:'dig',t:0,dur:2.2,fx:0};P.vx=P.vy=0;keys.left=keys.right=keys.up=keys.down=0;toast('Du gräbst ...');return true;}
 return false;
}
function digDone(){
 G.schatz=null;G.schatzN=(G.schatzN||0)+1;
 const r=pick([0,1,1,2,2,3]);
 if(r===0){mood(6,'+6');toast('Eine alte Truhe! Darin: ein Zettel. „Der wahre Schatz ist die Schatzsuche.“ Käpt\'n Klabauter, du Schlitzohr!');}
 else{const m=r10(rf(30,110)*r/2+20);G.cash+=m;mood(8,'+8 Schatz');sfx('coin');toast('Schatz gefunden! Eine kleine Truhe mit Schokotalern und '+eur(m)+' in alten Münzen. Arrr!');}
}
function schatzNeu(){
 for(let k=0;k<300;k++){const x=rnd(2,MW-3),y=rnd(2,MH-3),t=CITY.T[y*CITY.MW+x];if(t!==GR&&t!==SW)continue;const px=x*TS+16,py=y*TS+16;if(inNoGo(px,py)||hit(px,py,10))continue;if(CITY.MKS.some(m=>Math.hypot(m.x-px,m.y-py)<70))continue;const d=Math.hypot(px-P.x,py-P.y);if(d<600||d>1600)continue;G.schatz={x:px,y:py};return true;}
 return false;
}
function miniExtra(x,O,S,big){
 if(ZONE)return;
 if(FIRE&&FIRE.st==='burn'&&Math.floor(timeNow*4)%2){x.fillStyle='#ff6a3c';x.beginPath();x.arc(O+FIRE.cx/TS*S,FIRE.cy/TS*S,big?6:5,0,6.283);x.fill();}
 if(G&&G.schatz){x.strokeStyle='#ffd23f';x.lineWidth=2;const sx=O+G.schatz.x/TS*S,sy=G.schatz.y/TS*S;x.beginPath();x.moveTo(sx-4,sy-4);x.lineTo(sx+4,sy+4);x.moveTo(sx+4,sy-4);x.lineTo(sx-4,sy+4);x.stroke();x.lineWidth=1;}
}
function fwMenu(){
 mdl('Feuerwache','Die Feuerwehrleute polieren gerade das Löschfahrzeug. „Brennt es? Nein? Dann gibt es Kaffee!“ Dein Feuerlöscher: '+(G.ext>0?Math.round(G.ext)+' %':'keiner')+'. Gelöschte Brände mit dir: '+(G.fwN||0)+'.',[[G.ext>0?'Feuerlöscher auffüllen':'Feuerlöscher mitnehmen (Leihgabe)','fw:ext',G.ext>=100],['Wie lösche ich richtig?','fw:tip'],['Das Löschfahrzeug bestaunen','fw:auto']]);
}
function khMenu(){
 mdl('Krankenhaus St. Rheinhanfen','Am Empfang sitzt Schwester Hildegard und strickt Socken für die ganze Station. „Na, alles heil?“',[['Gesundheits-Check (gratis)','kh:check'],['Patienten besuchen und aufmuntern','kh:visit',(G.khCd||0)>timeNow],['Blumen für die Station (3 €)','kh:blumen',G.cash<3]]);
}
const FAIRY={
 schnee:{n:'Schneewittchen',p:'Schneewittchen begrüßen'},dorn:{n:'Dornröschen',p:'Dornröschen ansehen'},rapu:{n:'Rapunzel',p:'Zum Turm hochrufen'},
 merl:{n:'Merlin',p:'Merlin ansprechen'},alice:{n:'Alice',p:'Alice ansprechen'},kan:{n:'Weißes Kaninchen',p:'Kaninchen nach der Zeit fragen'},
 hut:{n:'Hutmacher',p:'Zur Teegesellschaft setzen'},mh:{n:'Märzhase',p:'Märzhase begrüßen'},kitz:{n:'Rehkitz Tupfi',p:'Rehkitz streicheln'},
 herk:{n:'Herkules',p:'Herkules ansprechen'},pirat:{n:'Käpt\'n Klabauter',p:'Käpt\'n Klabauter ansprechen'}
};
function fyNew(k,x,y,o){const f=freeSpot(x,y);const d={k:k,x:f.x,y:f.y,a:rf(0,6.28),walk:0,cd:0,steer:rf(1,3),say:rf(2,5)};return Object.assign(d,o||{});}
function fairyMaerchen(z){
 const S=(x,y)=>{z.T[y*ZW+x]=BL;};
 [[11,2],[12,2],[13,2],[14,2],[15,2],[11,3],[15,3],[12,3],[13,3],[14,3]].forEach(q=>S(q[0],q[1]));
 S(21,3);S(43,3);S(44,3);S(43,4);S(44,4);S(41,26);S(42,26);
 z.ska.push({k:'dorn',x:13*TS+16,y:3*TS+18,a:0,cd:0,wake:0,say:3,fix:1});
 z.ska.push({k:'rapu',x:44*TS,y:5*TS+6,a:0,cd:0,braid:0,bl:0,say:5,fix:1});
 z.ska.push({k:'merl',x:22*TS+24,y:4*TS+10,a:Math.PI,cd:0,say:4,fix:1,tries:0});
 z.ska.push({k:'hut',x:40*TS+14,y:26*TS+16,a:0,cd:0,say:3,fix:1});
 z.ska.push({k:'mh',x:43*TS+18,y:26*TS+16,a:Math.PI,cd:0,say:5,fix:1});
 z.ska.push(fyNew('kan',37*TS,25*TS,{hx:37*TS,hy:25.4*TS,ph:0,stop:0,pt:4}));
 z.ska.push(fyNew('alice',35*TS,25*TS));
 z.ska.push(fyNew('schnee',37*TS,19*TS+16,{hx:37*TS,hy:19*TS+16}));
 z.ska.push(fyNew('kitz',27*TS,4*TS,{hx:27*TS,hy:4*TS,run:0,hop:0}));
}
function fairyEvent(k,sp){
 if(k==='schnee'){
  const g=mkZwerge(sp.x,sp.y);g.forEach(d=>{d.a=sp.a;d.ev=1;});g[0].life=90;SKC.push.apply(SKC,g);
  SKC.push(fyNew('schnee',sp.x-150,sp.y,{fol:1,a:sp.a}));
  toast('Schneewittchen besucht mit den sieben Zwergen die Stadt. Sie singt, die Zwerge marschieren.');return true;
 }
 if(k==='alice'){
  SKC.push(fyNew('kan',sp.x,sp.y,{lead:true,life:80,stop:0,pt:4,a:sp.a}));SKC.push(fyNew('alice',sp.x-50,sp.y,{a:sp.a}));
  toast('Ein weißes Kaninchen mit Taschenuhr flitzt vorbei: „Zu spät, zu spät!“ Ein Mädchen rennt hinterher.');return true;
 }
 if(k==='merlin'){SKC.push(fyNew('merl',sp.x,sp.y,{lead:true,life:90,a:sp.a}));toast('Ein Zauberer im Sternenmantel spaziert durch Rheinhanfen. Das ist doch Merlin!');return true;}
 if(k==='herk'){SKC.push(fyNew('herk',sp.x,sp.y,{lead:true,life:80,a:sp.a}));toast('Herkules joggt durch die Stadt. Mit einem Baumstamm auf der Schulter. Zum Aufwärmen.');return true;}
 if(k==='pirat'){SKC.push(fyNew('pirat',sp.x,sp.y,{lead:true,life:110,a:sp.a}));toast('Käpt\'n Klabauter ist an Land gegangen und verkauft Schatzkarten. Arrr!');return true;}
 if(k==='kitz'){SKC.push(fyNew('kitz',sp.x,sp.y,{lead:true,life:70,run:0,hop:0,a:sp.a}));toast('Ein kleines Rehkitz hat sich in die Stadt verirrt. Ganz leise, sonst hüpft es weg!');return true;}
 return false;
}
function fyMove(d,tx,ty,sp,dt){
 const dx=tx-d.x,dy=ty-d.y,L=Math.hypot(dx,dy);if(L<2)return;
 d.a=Math.atan2(dy,dx);const s=Math.min(L,sp*dt),sx=Math.cos(d.a)*s,sy=Math.sin(d.a)*s;
 if(skOk(d.x+sx,d.y+sy)){d.x+=sx;d.y+=sy;d.walk+=dt*8;}else if(skOk(d.x+sx,d.y)){d.x+=sx;d.walk+=dt*8;}else if(skOk(d.x,d.y+sy)){d.y+=sy;d.walk+=dt*8;}
 else if(L>200){const f=freeSpot(tx,ty);d.x=f.x;d.y=f.y;}
}
function fairyUpdate(dt){
 const L=skl();if(!L.length)return;
 L.forEach(d=>{
  if(!FAIRY[d.k])return;
  const pd=Math.hypot(d.x-P.x,d.y-P.y);
  d.say-=dt;
  const sayIt=(arr,col)=>{if(d.say<=0){d.say=rf(5,9);if(pd<320)addFx(d.x,d.y-30,pick(arr),col||'#fff2b0',1.8);}};
  if(d.k==='schnee'){
   if(d.fol){const ld=L.filter(q=>q.k==='zw');const t=ld.length?ld[ld.length-1]:null;if(t&&Math.hypot(t.x-d.x,t.y-d.y)>30)fyMove(d,t.x,t.y,50,dt);}
   else{leash(d,d.hx,d.hy,140);steerStep(d,dt,22);}
   sayIt(['La la la ♪','Hallo, ihr Lieben!','Hat jemand die Zwerge gezählt?','Bitte keine Äpfel, danke!']);
  }else if(d.k==='dorn'){
   if(d.wake>0){d.wake-=dt;sayIt(['*gähn*','Wie spät ist es?','Noch fünf Minuten ...']);}
   else if(pd<300&&chance(dt*.7))addFx(d.x+rf(-6,6),d.y-16,pick(['z','Z','zZ']),'#cfe0ff',1.6,-18);
  }else if(d.k==='rapu'){
   if(d.braid>0)d.braid-=dt;
   d.bl+=((d.braid>0?1:0)-d.bl)*Math.min(1,dt*1.2);
   sayIt(['Laaa la laaa ♪','Hallo da unten!','Hier oben ist das WLAN gut.','Mein Zopf hat einen eigenen Friseurtermin.']);
  }else if(d.k==='merl'){
   if(!d.fix){steerStep(d,dt,24);}else if(pd<160)d.a=Math.atan2(P.y-d.y,P.x-d.x);
   if(chance(dt*2.5))FX.push({x:d.x+Math.cos(d.a)*12+rf(-4,4),y:d.y-16,vx:rf(-10,10),vy:rf(-30,-10),t:0,life:1,dot:pick(['#b58cff','#5ff0ff','#fff2b0']),r:1.6});
   sayIt(['Abrakadabra ... wo war ich?','Ich habe meine Brille weggezaubert.','Ein Zauberer kommt nie zu spät.','Hokuspokus, fertig ist der Krokus!'],'#d9c8ff');
  }else if(d.k==='kan'){
   if(d.stop>0){d.stop-=dt;}
   else if(d.hx!==undefined){d.ph+=dt*.9;const nx=d.hx+Math.cos(d.ph)*110,ny=d.hy+Math.sin(d.ph)*42;d.a=Math.atan2(ny-d.y,nx-d.x);d.x=nx;d.y=ny;d.walk+=dt*14;}
   else{steerStep(d,dt,80);d.walk+=dt*6;}
   d.pt-=dt;if(d.pt<=0){d.pt=rf(4,7);d.stop=1.3;if(pd<320)addFx(d.x,d.y-24,pick(['Zu spät! Zu spät!','Oh je, meine Uhr!','Die Herzogin wartet!']),'#ffffff',1.6);}
  }else if(d.k==='alice'){
   const rb=L.find(q=>q.k==='kan');if(pd<56){d.a=Math.atan2(P.y-d.y,P.x-d.x);if(rb&&rb.stop<.5)rb.stop=.6;}else if(rb&&Math.hypot(rb.x-d.x,rb.y-d.y)>34)fyMove(d,rb.x,rb.y,66,dt);
   sayIt(['Warte doch, Kaninchen!','Immer seltsamer und seltsamer!','Wohin führt dieser Weg?']);
  }else if(d.k==='hut'||d.k==='mh'){
   sayIt(d.k==='hut'?['Platz wechseln!','Noch Tee?','Es ist immer sechs Uhr!','Kein Platz! Kein Platz!']:['Mehr Tee!','Butter in die Uhr? Beste Butter!','Hihi!']);
  }else if(d.k==='kitz'){
   d.hop+=dt*9;
   const ps=Math.hypot(P.vx,P.vy);
   if(pd<100&&ps>70&&!(d.run>0)){d.run=1.2;d.a=Math.atan2(d.y-P.y,d.x-P.x);if(pd<200)addFx(d.x,d.y-20,'Hops!','#fff2b0',1);}
   if(d.run>0){d.run-=dt;const nx=d.x+Math.cos(d.a)*110*dt,ny=d.y+Math.sin(d.a)*110*dt;if(skOk(nx,ny)){d.x=nx;d.y=ny;}else d.a+=1.5;}
   else{if(d.hx!==undefined)leash(d,d.hx,d.hy,200);steerStep(d,dt,24);}
  }else if(d.k==='herk'){
   if(pd<56)d.a=Math.atan2(P.y-d.y,P.x-d.x);else{steerStep(d,dt,66);d.walk+=dt*4;}
   sayIt(['Hepp! Hepp!','Erst 12 Aufgaben, dann Frühstück!','Wer hebt mit?','Muskeln aus Marmor!']);
  }else if(d.k==='pirat'){
   steerStep(d,dt,28);
   sayIt(['Arrr!','Schatzkarten! Frische Schatzkarten!','Kiki, sag Hallo!','Pommes! Pommes!'],'#ffe08a');
  }
 });
}
let tagF=-1,tagD=null;
function tagNearest(){if(tagF===timeNow)return tagD;tagF=timeNow;let b=null,bd=130;skl().forEach(q=>{if(!FAIRY[q.k])return;const dd=Math.hypot(q.x-P.x,q.y-P.y);if(dd<bd){bd=dd;b=q;}});tagD=b;return b;}
function nameTag(d,n,off){if(tagNearest()===d){ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-off);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-off);ctx.lineWidth=1;ctx.textAlign='start';ctx.textBaseline='alphabetic';}}
function fig(x,y,a,o){
 const sc=o.sc||1;
 ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+2,y+4,8*sc,6*sc,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(x,y);ctx.scale(sc,sc);ctx.rotate(a);
 const sw=Math.sin(o.walk||0)*3,sk=o.skin||'#f0d2b4';
 if(o.cape){ctx.fillStyle=o.cape;ctx.beginPath();ctx.ellipse(-4,0,6,9,0,0,6.283);ctx.fill();}
 ctx.fillStyle=o.dress;ctx.beginPath();ctx.ellipse(0,0,o.sk||4.6,(o.sk||4.6)+3,0,0,6.283);ctx.fill();
 if(o.dot){ctx.fillStyle=o.dot;[[-2,-4],[1,3],[-3,4],[2,-2]].forEach(q=>circle(q[0],q[1],.9));}
 if(o.apron){ctx.fillStyle=o.apron;ctx.beginPath();ctx.ellipse(2.4,0,2.6,4.4,0,0,6.283);ctx.fill();}
 ctx.fillStyle=sk;circle(sw*.6+1,-7,2.1);circle(-sw*.6+1,7,2.1);
 if(o.hairLen){ctx.fillStyle=o.hair;ctx.beginPath();ctx.ellipse(-4,0,o.hairLen,3.4,0,0,6.283);ctx.fill();}
 if(o.beard){ctx.fillStyle=o.beard;ctx.beginPath();ctx.ellipse(4,0,4,2.8,0,0,6.283);ctx.fill();}
 ctx.fillStyle=sk;circle(.9,0,3.5);
 ctx.fillStyle=o.hair;circle(-1.1,0,3.7);
 if(o.hat){ctx.fillStyle=o.hat;circle(-.6,0,o.brim||5);if(o.hat2){ctx.fillStyle=o.hat2;circle(-.6,0,(o.brim||5)*.55);}}
 ctx.restore();
}
function drawFairy(d){
 const k=d.k,n=FAIRY[k].n;
 if(k==='schnee'){fig(d.x,d.y,d.a,{dress:'#2f7a4a',sk:6,apron:'#f4f4f4',hair:'#15110f',hairLen:6,skin:'#f6e6dc',walk:d.walk});ctx.fillStyle='#8a5a2a';circle(d.x+Math.cos(d.a+1.3)*9,d.y+Math.sin(d.a+1.3)*9,3.4);ctx.fillStyle='#d63a3a';circle(d.x+Math.cos(d.a+1.3)*9-1,d.y+Math.sin(d.a+1.3)*9-1,1.4);nameTag(d,n,20);}
 else if(k==='dorn'){
  if(d.wake>0){fig(d.x,d.y+6,Math.PI/2,{dress:'#b9a3e6',sk:5.5,hair:'#7a4a2a',hairLen:3});}
  else{ctx.fillStyle='#5f8a3a';ctx.beginPath();ctx.ellipse(d.x,d.y+2,24,11,0,0,6.283);ctx.fill();ctx.fillStyle='#fff7ee';ctx.beginPath();ctx.ellipse(d.x-16,d.y+1,6,5,0,0,6.283);ctx.fill();ctx.fillStyle='#b9a3e6';ctx.beginPath();ctx.ellipse(d.x+3,d.y+2,15,7,0,0,6.283);ctx.fill();ctx.fillStyle='#f3dcc8';circle(d.x-14,d.y,3.6);ctx.fillStyle='#7a4a2a';circle(d.x-16.5,d.y-.5,3.8);circle(d.x-15,d.y-3.2,2);}
  nameTag(d,n,22);
 }else if(k==='rapu'){
  const wx=d.x,wy=d.y-104;
  if(d.bl>.02){const L=(d.y+8-wy)*d.bl;ctx.strokeStyle='#e9c25a';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(wx,wy+4);for(let i=1;i<=12;i++){const yy=wy+4+L*i/12;ctx.lineTo(wx+Math.sin(i*1.3+timeNow*2)*2.2,yy);}ctx.stroke();ctx.strokeStyle='#c9a03a';ctx.lineWidth=1.5;for(let i=1;i<12;i+=2){const yy=wy+4+L*i/12;ctx.beginPath();ctx.moveTo(wx-2.5,yy);ctx.lineTo(wx+2.5,yy+3);ctx.stroke();}ctx.lineWidth=1;}
  ctx.fillStyle='#f0d2b4';circle(wx,wy-2,4);ctx.fillStyle='#e9c25a';circle(wx,wy-5,4.4);ctx.fillStyle='#6a8a3a';ctx.fillRect(wx-6,wy+2,12,4);
  if(tagNearest()===d){ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,wx,wy-16);ctx.fillStyle='#fff';ctx.fillText(n,wx,wy-16);ctx.lineWidth=1;ctx.textAlign='start';}
 }else if(k==='merl'){
  fig(d.x,d.y,d.a,{dress:'#3b2a5a',sk:6,dot:'#e6e6ff',hair:'#cfcfcf',beard:'#e2e2e2',hat:'#3b2a5a',hat2:'#5a4a8a',brim:5.6,walk:d.walk});
  const sx=d.x+Math.cos(d.a-1.2)*10,sy=d.y+Math.sin(d.a-1.2)*10;ctx.strokeStyle='#7a5a32';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(sx,sy+6);ctx.lineTo(sx,sy-14);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='rgba(95,240,180,'+(.6+.3*Math.sin(timeNow*4))+')';circle(sx,sy-15,3);
  nameTag(d,n,24);
 }else if(k==='alice'){fig(d.x,d.y,d.a,{dress:'#d64545',sk:5.2,apron:'#ffffff',hair:'#e6c36a',hairLen:5,walk:d.walk});nameTag(d,n,20);}
 else if(k==='kan'){
  const hp=d.stop>0?0:Math.abs(Math.sin(d.walk*.8))*3;
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+1,d.y+4,7,4,0,0,6.283);ctx.fill();
  ctx.save();ctx.translate(d.x,d.y-hp);ctx.rotate(d.a);
  ctx.fillStyle='#fafafa';ctx.beginPath();ctx.ellipse(0,0,7,4.6,0,0,6.283);ctx.fill();ctx.fillStyle='#c0392b';ctx.fillRect(-2,-4.4,5,8.8);
  ctx.fillStyle='#fafafa';circle(6,0,3.4);ctx.beginPath();ctx.ellipse(2,-3,5,1.6,-.4,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(2,3,5,1.6,.4,0,6.283);ctx.fill();
  ctx.fillStyle='#ffd23f';circle(1,3.6,1.6);ctx.fillStyle='#ff9ab0';circle(8.5,0,.9);
  ctx.restore();nameTag(d,'Weißes Kaninchen',18);
 }else if(k==='hut'){fig(d.x,d.y,d.a,{dress:'#3a6a4a',sk:5,hair:'#c96a2a',hat:'#2f4a3a',hat2:'#7a3a5a',brim:6.2});nameTag(d,n,22);}
 else if(k==='mh'){ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+1,d.y+4,8,5,0,0,6.283);ctx.fill();ctx.fillStyle='#a8784a';ctx.beginPath();ctx.ellipse(d.x,d.y,6.5,5.5,0,0,6.283);ctx.fill();circle(d.x-5,d.y,3.6);ctx.beginPath();ctx.ellipse(d.x-7,d.y-6,1.8,6,.3,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(d.x-3,d.y-7,1.8,6,-.2,0,6.283);ctx.fill();ctx.fillStyle='#e8c060';ctx.fillRect(d.x-8,d.y-11,6,1.5);nameTag(d,n,22);}
 else if(k==='kitz'){
  const hp=Math.abs(Math.sin(d.hop))*(d.run>0?5:1.5);
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+1,d.y+5,9,4,0,0,6.283);ctx.fill();
  ctx.save();ctx.translate(d.x,d.y-hp);ctx.rotate(d.a);
  ctx.fillStyle='#b5774a';ctx.beginPath();ctx.ellipse(0,0,9,5,0,0,6.283);ctx.fill();
  ctx.fillStyle='#f6ead8';[[-4,-2],[-1,1.5],[2,-1.5],[-6,1.5],[4,1.8]].forEach(q=>circle(q[0],q[1],1));
  ctx.fillStyle='#b5774a';circle(9,0,3.6);ctx.beginPath();ctx.ellipse(8,-3.6,1.4,3.2,-.6,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(8,3.6,1.4,3.2,.6,0,6.283);ctx.fill();
  ctx.fillStyle='#2a1a10';circle(12,0,1);ctx.fillStyle='#f6ead8';circle(-9,0,1.6);
  ctx.restore();nameTag(d,n,18);
 }else if(k==='herk'){
  fig(d.x,d.y,d.a,{dress:'#f2efe6',sk:5.4,cape:'#c8963c',hair:'#4a3020',skin:'#d9a878',sc:1.15,walk:d.walk});
  ctx.fillStyle='#8a5a1c';circle(d.x-Math.cos(d.a)*3,d.y-Math.sin(d.a)*3,5);
  const cx2=d.x+Math.cos(d.a+1.6)*8,cy2=d.y+Math.sin(d.a+1.6)*8;ctx.strokeStyle='#6a4020';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(cx2-Math.cos(d.a)*10,cy2-Math.sin(d.a)*10);ctx.lineTo(cx2+Math.cos(d.a)*12,cy2+Math.sin(d.a)*12);ctx.stroke();ctx.lineWidth=1;
  nameTag(d,n,24);
 }else if(k==='pirat'){
  fig(d.x,d.y,d.a,{dress:'#1f2a44',sk:5.4,dot:'#d4a017',hair:'#5a4030',beard:'#9a9a9a',hat:'#151515',hat2:'#d4a017',brim:6});
  const px=d.x+Math.cos(d.a+1.57)*7,py=d.y+Math.sin(d.a+1.57)*7-3;ctx.fillStyle='#2ecc71';circle(px,py,3);ctx.fillStyle='#e5504d';ctx.fillRect(px-1,py+2,2,4);ctx.fillStyle='#ffd23f';circle(px+2.5,py,1);
  nameTag(d,n,24);
 }
}
function drawMaerchen2(cx,cy){
 const iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 if(iv(13*TS,3*TS,140)){
  const rose=(x,y,s)=>{ctx.fillStyle='#2f6a2a';circle(x,y,s);ctx.fillStyle='#3f8a3a';circle(x-3,y-3,s*.6);[[0,-.5],[.6,.3],[-.5,.5],[.2,.8],[-.7,-.3]].forEach((q,i)=>{ctx.fillStyle=i%2?'#e5504d':'#ff8fb3';circle(x+q[0]*s*.8,y+q[1]*s*.8,2.2);});};
  for(let x=11;x<=15;x++)rose(x*TS+16,2*TS+16,16);rose(11*TS+16,3*TS+16,15);rose(15*TS+16,3*TS+16,15);
 }
 if(iv(44*TS,3*TS,200)){
  const bx=44*TS,by=5*TS,top=by-124;
  ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(bx+6,by+2,34,12,0,0,6.283);ctx.fill();
  ctx.fillStyle='#9a958c';ctx.fillRect(bx-28,top,56,by-top);
  ctx.fillStyle='#8a857c';for(let y=top+8;y<by;y+=12)for(let x=bx-28+((y/12)&1?0:9);x<bx+28;x+=18)ctx.fillRect(x,y,16,1.5);
  ctx.fillStyle='#b5b0a6';ctx.fillRect(bx-28,top,8,by-top);
  ctx.fillStyle='#b03a2e';ctx.beginPath();ctx.moveTo(bx-36,top+4);ctx.lineTo(bx+36,top+4);ctx.lineTo(bx,top-44);ctx.closePath();ctx.fill();
  ctx.fillStyle='#2a1f2a';ctx.beginPath();ctx.moveTo(bx-9,top+30);ctx.lineTo(bx-9,top+14);ctx.arc(bx,top+14,9,Math.PI,0);ctx.lineTo(bx+9,top+30);ctx.closePath();ctx.fill();
  ctx.fillStyle='#5a3a1a';ctx.fillRect(bx-10,by-26,20,26);
 }
 if(iv(21*TS,3*TS,80)){const x=21*TS+16,y=3*TS+18;ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(x+3,y+5,18,8,0,0,6.283);ctx.fill();ctx.fillStyle='#8d8d92';ctx.beginPath();ctx.ellipse(x,y,17,11,0,0,6.283);ctx.fill();ctx.fillStyle='#a3a3a8';ctx.beginPath();ctx.ellipse(x-4,y-3,9,5,0,0,6.283);ctx.fill();ctx.fillStyle='#c9ced6';ctx.fillRect(x-1.5,y-26,3,22);ctx.fillStyle='#d4a017';ctx.fillRect(x-7,y-8,14,3);ctx.fillRect(x-2,y-14,4,6);ctx.fillStyle='#ff4d7a';circle(x,y-15,1.6);}
 if(iv(41.5*TS,26*TS,90)){const x=41*TS,y=26*TS;ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(x+4,y+6,64,26);ctx.fillStyle='#f6f2ea';ctx.fillRect(x,y+2,64,26);ctx.fillStyle='#e5b8c8';for(let i=0;i<8;i++)ctx.fillRect(x+i*8,y+2,4,26);
  [[10,10,'#4a8ad8'],[26,18,'#e5504d'],[42,9,'#f1c40f'],[54,19,'#7bd86a']].forEach(q=>{ctx.fillStyle='#fff';circle(x+q[0],y+q[1],4);ctx.fillStyle=q[2];circle(x+q[0],y+q[1],2.6);});
  ctx.fillStyle='#b8862b';ctx.beginPath();ctx.ellipse(x+33,y+11,7,5.5,0,0,6.283);ctx.fill();ctx.fillStyle='#d8a84b';circle(x+31,y+9,3);if(Math.floor(timeNow*1.5)%2){ctx.fillStyle='rgba(255,255,255,.5)';circle(x+37,y+2,3);}}
}
function fairyOpen(d){
 UI.fy=d;const k=d.k;
 if(k==='schnee')mdl('Schneewittchen','„Hallo! Ich wohne bei sieben Zwergen. Sie sind laut, sie schnarchen und sie lieben mich. Ich koche, sie singen. Wir haben einen Deal.“',[['Plaudern','fy:schnee:talk'],['Mit den Zwergen tanzen','fy:schnee:tanz'],['Einen Apfel anbieten','fy:schnee:apfel']]);
 else if(k==='dorn')mdl('Dornröschen',d.wake>0?'Dornröschen reibt sich die Augen: „Hab ich was verpasst? Hundert Jahre oder so?“':'Hinter der Rosenhecke schläft Dornröschen tief und fest. Sie schnarcht ganz leise. Sehr königlich.',[['Den Wecker klingeln lassen','fy:dorn:wecker'],['Die Rosen gießen','fy:dorn:rosen'],['Ein Schlaflied summen','fy:dorn:lied']]);
 else if(k==='rapu')mdl('Rapunzel',d.bl>.6?'Der goldene Zopf hängt bis zum Boden. Rapunzel ruft: „Aber vorsichtig! Das ziept!“':'Hoch oben im Turm schaut Rapunzel aus dem Fenster und winkt.',d.bl>.6?[['Am Zopf hochklettern','fy:rapu:klettern'],['Lieber eine Leiter vorschlagen','fy:rapu:leiter']]:[['„Rapunzel, lass dein Haar herunter!“','fy:rapu:haar'],['Lieber eine Leiter vorschlagen','fy:rapu:leiter'],['Plaudern','fy:rapu:talk']]);
 else if(k==='merl'){const ch=[['Einen Zaubertrick wünschen','fy:merl:trick',d.cd>0],['Eine Weisheit hören','fy:merl:weis']];if(ZONE&&ZONE.name==='maerchen')ch.push(['Das Schwert aus dem Stein ziehen','fy:merl:schwert']);mdl('Merlin','Der Zauberer zupft an seinem Bart: „Ah, ein Besucher! Ich wusste, dass du kommst. Ich habe es vorhergesehen. Oder geträumt.“',ch);}
 else if(k==='alice')mdl('Alice','„Hast du ein weißes Kaninchen gesehen? Mit Weste und Taschenuhr? Es ist schrecklich in Eile!“',[['Fragen, wohin sie läuft','fy:alice:wohin'],['Aus dem Fläschchen „Trink mich“ probieren','fy:alice:trink'],['Mitlaufen','fy:alice:lauf']]);
 else if(k==='kan'){d.stop=2;const c=H.clock();addFx(d.x,d.y-24,'Zu spät!','#fff',1.4);toast('Das Kaninchen schaut auf die Taschenuhr: „Es ist '+c+'! Zu spät, viel zu spät!“ Und weg ist es.');mood(2,'+2');}
 else if(k==='hut'||k==='mh')mdl('Die verrückte Teegesellschaft','Der Hutmacher schenkt Tee ein, obwohl alle Tassen schon voll sind. Der Märzhase tunkt seine Uhr in den Tee. „Kein Platz! Kein Platz!“, rufen beide, obwohl jede Menge Platz ist.',[['Tee trinken','fy:hut:tee'],['Das Rätsel hören','fy:hut:raetsel'],['„Alle einen Platz weiterrücken!“','fy:hut:platz']]);
 else if(k==='kitz'){
  if(Math.hypot(P.vx,P.vy)>40||d.run>0){d.run=1.2;d.a=Math.atan2(d.y-P.y,d.x-P.x);toast('Hops! Das Kitz springt davon. Ganz langsam anschleichen!');return;}
  if(chance(.75)){mood(6,'+6 Kitz');sfx('aww');addFx(d.x,d.y-20,'♥','#ff4d7a',1.6);toast(pick(['Das Rehkitz schnuppert an deiner Hand. Sein Fell ist weich wie Samt.','Tupfi stupst dich mit der Nase an. Dein Herz schmilzt ein bisschen.']));}
  else{d.run=1.2;d.a=Math.atan2(d.y-P.y,d.x-P.x);toast('Fast! Das Kitz hüpft im letzten Moment weg.');}
 }
 else if(k==='herk')mdl('Herkules','„Grüß dich, Sterblicher! Ich bin Herkules. Halbgott, Held und seit Neuestem Fitnesstrainer.“',[['Armdrücken','fy:herk:arm'],['Von den zwölf Aufgaben hören','fy:herk:aufg'],['Um einen Kraftbeweis bitten','fy:herk:kraft']]);
 else if(k==='pirat')mdl('Käpt\'n Klabauter','„Ahoi, Landratte! Papagei Kiki und ich sind auf Landgang. Wir haben Karten, Geschichten und kaum Zähne.“ Kiki krächzt: „Pommes! Pommes!“',[[G.schatz?'Schatzkarte (hast du schon)':'Schatzkarte kaufen (5 €)','fy:pirat:karte',!!G.schatz||G.cash<5],['Seemannsgarn hören','fy:pirat:garn'],['Kiki begrüßen','fy:pirat:kiki']]);
}
function skAct14(p){
 if(p.indexOf('fw:')===0||p.indexOf('kh:')===0){
  if(p==='fw:ext'){G.ext=100;sfx('ok');toast('Feuerlöscher voll! Nahe am Feuer drückst du OK zum Löschen.');}
  else if(p==='fw:tip')showModal({title:'So löschst du richtig',text:'Feuerlöscher: Geh nah ans Feuer und drück OK. Ein voller Löscher reicht für zehn Stöße. Hydranten: Die roten Hydranten stehen an den Gehwegen. OK schließt den Schlauch an, dann zum Feuer laufen und OK drücken: Wasser marsch! Am Hydranten baust du ihn wieder ab. Nie ins Feuer laufen, sonst landest du im Krankenhaus.',choices:[{label:'Verstanden!',a:'mclose'}]});
  else if(p==='fw:auto'){mood(3,'+3');fireSiren(1.2);toast('Du darfst einmal auf den Knopf drücken. Tatü-tata! Alle Feuerwehrleute grinsen.');}
  else if(p==='kh:check'){G.drunk=Math.max(0,G.drunk-1);mood(2,'+2');toast(pick(['Alles bestens. Der Arzt empfiehlt: mehr Gemüse, weniger Konfetti.','Puls gut, Laune gut, Ohren sauber. Du darfst gehen.','Der Arzt klopft dir aufs Knie. Dein Bein tritt aus. Alles in Ordnung!']));}
  else if(p==='kh:visit'){G.khCd=timeNow+30;mood(6,'+6');G.hero=(G.hero||0)+.5;toast(pick(['Du erzählst Herrn Pohl auf Zimmer 3 einen Witz. Er lacht so sehr, dass die Schwester nachschaut.','Du spielst mit den Patienten Mensch ärgere dich nicht. Du verlierst. Alle sind glücklich.','Du bringst Oma Gerda die Zeitung und liest ihr das Horoskop vor. Heute: Glückstag!']));}
  else if(p==='kh:blumen'){if(G.cash<3)return true;G.cash-=3;mood(4,'+4');sfx('coin');toast('Ein bunter Strauß für die Station. Schwester Hildegard strahlt.');}
  return true;
 }
 if(p.indexOf('fy:')!==0)return false;
 const d=UI.fy,a=p.split(':')[2];
 if(p==='fy:schnee:talk'){mood(3,'+3');toast(pick(['„Die Zwerge putzen nie ihre Zipfelmützen. Ich hab aufgegeben.“','„Ein Spiegel hat mir mal gesagt, ich sei die Schönste. Seitdem rede ich nicht mehr mit Spiegeln.“','„Weißt du, was sieben Zwerge morgens essen? Alles.“']));}
 else if(p==='fy:schnee:tanz'){mood(6,'+6 Tanz');sfx('musik');skl().forEach(q=>{if(q.k==='zw')q.dn=5;});P.dance=4;toast('Schneewittchen klatscht den Takt, die Zwerge tanzen im Kreis, und du mittendrin.');}
 else if(p==='fy:schnee:apfel'){mood(3,'+3');toast('„Oh nein, danke! Ich hatte mal einen Apfel. Lange Geschichte. Hast du vielleicht Pommes?“');}
 else if(p==='fy:dorn:wecker'){if(d){d.wake=9;}sfx('ding');mood(4,'+4');toast('RRRRING! Dornröschen schreckt hoch: „Ist es schon Montag?“ Sie gähnt, schaut sich um und legt sich gleich wieder hin.');}
 else if(p==='fy:dorn:rosen'){mood(3,'+3');toast('Du gießt die Rosen. Sie duften so stark, dass sogar die Zwerge kurz stehen bleiben.');}
 else if(p==='fy:dorn:lied'){mood(4,'+4');if(d)d.wake=0;toast('Du summst ein Schlaflied. Dornröschen lächelt im Schlaf. Du gähnst auch. Ansteckend.');}
 else if(p==='fy:rapu:haar'){if(d)d.braid=14;sfx('magic');toast('„Na gut, aber nicht so fest ziehen!“ Ein goldener Zopf rollt den Turm herunter. Ganz schön lang!');}
 else if(p==='fy:rapu:klettern'){if(d)d.braid=0;startFade('Du kletterst Hand über Hand nach oben. „Aua! Aua! Das ziept!“ Oben gibt es Tee und eine Aussicht über den ganzen Märchenwald.',()=>{mood(9,'+9 Aussicht');G.hero=(G.hero||0)+.5;});}
 else if(p==='fy:rapu:leiter'){mood(3,'+3');toast('Rapunzel starrt dich an: „Eine ... Leiter? Darauf ist in all den Jahren noch niemand gekommen!“');}
 else if(p==='fy:rapu:talk'){mood(2,'+2');toast(pick(['„Ich wasche meine Haare jeden Sonntag. Das dauert bis Mittwoch.“','„Hier oben gibt es kein Treppenhaus. Dafür kein Treppenhaus-Putzplan!“']));}
 else if(p==='fy:merl:trick'){
  if(d)d.cd=15;const r=rnd(0,3);sfx('magic');
  for(let i=0;i<14;i++)FX.push({x:P.x+rf(-30,30),y:P.y+rf(-40,0),vx:rf(-30,30),vy:rf(-60,-20),t:0,life:1.4,dot:pick(['#b58cff','#5ff0ff','#ffd23f','#ff5fd0']),r:2});
  if(r===0){P.tiny=20;mood(5,'+5');toast('Simsalabim! Du schrumpfst auf Taschenformat. In 20 Sekunden bist du wieder groß. Hoffentlich.');}
  else if(r===1){G.mood=Math.min(100,G.mood+15);toast('Ein Laune-Zauber! Plötzlich findest du alles großartig. Sogar Montage.');}
  else if(r===2){mood(4,'+4');for(let i=0;i<20;i++)addFx(P.x+rf(-120,120),P.y+rf(-90,-10),pick(['★','✦','✧']),pick(['#ffd23f','#b58cff','#5ff0ff']),2,rf(-10,20));toast('Merlin lässt Sterne regnen. Ein paar landen in deiner Tasche. Sie kitzeln.');}
  else{mood(4,'+4');toast('Merlin zieht einen Hasen aus seinem Hut. Der Hase zieht einen kleineren Merlin aus seinem Hut. Alle sind verwirrt.');}
 }
 else if(p==='fy:merl:weis'){mood(2,'+2');toast(pick(['„Wer zu spät kommt, hat mehr Zeit zum Ankommen.“','„Der beste Zauber ist ein freundliches Wort. Der zweitbeste macht Pommes.“','„Auch ein Zauberer muss mal Pause machen. Ich mache seit 1.500 Jahren eine.“']));}
 else if(p==='fy:merl:schwert'){
  if(d)d.tries=(d.tries||0)+1;const n=d?d.tries:1;
  if(G.schwert){toast('Das Schwert hast du doch schon. Es liegt zu Hause in der Besteckschublade.');}
  else if(n<5){sfx('bonk');toast(pick(['Du ziehst mit aller Kraft. Nichts. Merlin hüstelt.','Du stemmst die Füße gegen den Stein. Das Schwert bleibt stur.','Nichts zu machen. Merlin: „Vielleicht vorher aufwärmen?“']));}
  else if(n<8){shake=.3;toast('Es wackelt! ... Nein. Doch nicht. Merlin macht sich Notizen.');}
  else{G.schwert=true;G.resp++;mood(12,'+12 Legende');sfx('win');toast('Mit einem Ruck ziehst du das Schwert heraus! Es ist ... ein Brotmesser. Merlin: „Oh. Falscher Stein. Aber trotzdem: Respekt!“');}
 }
 else if(p==='fy:alice:wohin'){mood(2,'+2');toast('„Dem Kaninchen nach, natürlich! Wohin, ist doch egal. Hauptsache, es ist seltsam.“');}
 else if(p==='fy:alice:trink'){P.tiny=20;mood(5,'+5');sfx('glug');toast('Du nimmst einen Schluck. Es schmeckt nach Kirsche, Vanille und Toast. Und du schrumpfst! In 20 Sekunden bist du wieder groß.');}
 else if(p==='fy:alice:lauf'){mood(4,'+4');P.heroT=Math.max(P.heroT||0,8);toast('Ihr rennt hinter dem Kaninchen her. Du bist plötzlich ganz flott unterwegs!');}
 else if(p==='fy:hut:tee'){mood(5,'+5 Tee');sfx('glug');toast('Der Tee schmeckt nach Mittwoch. Der Hutmacher nickt zufrieden: „Es ist immer Teezeit!“');}
 else if(p==='fy:hut:raetsel'){showModal({title:'Das Rätsel',text:'Der Hutmacher beugt sich vor: „Warum ist ein Rabe wie ein Schreibtisch?“',choices:[{label:'Weil beide Federn haben?',a:'skA',p:'fy:hut:antw'},{label:'Weil man auf beiden nicht sitzen sollte?',a:'skA',p:'fy:hut:antw'},{label:'Keine Ahnung!',a:'skA',p:'fy:hut:antw'}]});return true;}
 else if(p==='fy:hut:antw'){mood(4,'+4');toast('Der Hutmacher klatscht begeistert: „Ich habe auch keine Ahnung! Großartig! Noch Tee?“');}
 else if(p==='fy:hut:platz'){mood(3,'+3');toast('Alle rücken einen Platz weiter. Du sitzt jetzt vor einer leeren Tasse und einem schlafenden Siebenschläfer in der Teekanne.');}
 else if(p==='fy:herk:arm'){mood(5,'+5');sfx('bonk');toast(pick(['Du drückst mit aller Kraft. Herkules gähnt und lässt dich gewinnen. Glaubst du jedenfalls.','Unentschieden! Sagt Herkules. Mit einem Finger. Und einem Zwinkern.']));}
 else if(p==='fy:herk:aufg'){mood(3,'+3');toast('„Die neuen zwölf Aufgaben: Steuererklärung, Rasen mähen, IKEA-Schrank aufbauen, Socken sortieren, das WLAN-Passwort finden ... und sieben, über die ich nicht rede.“');}
 else if(p==='fy:herk:kraft'){mood(5,'+5');shake=.4;sfx('rumble');toast(ZONE?'Herkules hebt einen Felsbrocken, jongliert ihn kurz und stellt ihn sanft wieder ab.':'Herkules hebt deinen Van hoch, putzt den Unterboden und stellt ihn wieder ab. „Bitte. Gern geschehen.“');}
 else if(p==='fy:pirat:karte'){if(G.schatz||G.cash<5)return true;if(!schatzNeu()){toast('Kiki hat die Karte gefressen. Versuch es gleich nochmal.');return true;}G.cash-=5;sfx('coin');toast('Eine Schatzkarte! Ein goldenes X auf der Mini-Karte zeigt das Versteck. Dort OK: Schatz ausgraben.');}
 else if(p==='fy:pirat:garn'){mood(3,'+3');toast(pick(['„Einmal hab ich einen Wal gesehen, der Tee kocht! ... Was? Den kennst du? Hmpf.“','„Mein Holzbein? Hab ich beim Kartenspiel gewonnen. Mein echtes Bein ist noch dran, keine Sorge.“','„Die sieben Weltmeere? Ich kenn mindestens neun.“']));}
 else if(p==='fy:pirat:kiki'){mood(3,'+3');toast('Kiki legt den Kopf schief: „Hallo! Hallo! Pommes rot-weiß!“ Dann zwickt sie dich ganz sanft ins Ohr.');}
 return true;
}
function fwOwnWhy(){
 if(!G)return 'Gerade nicht.';
 if(!(G.stock.fw>0))return 'Keine Feuerwerks-Batterie. Die gibt es im Büdchen.';
 if(P.inCar||P.ride||P.coast)return 'Erst aussteigen.';
 if(ZONE&&['wal','hoehle','fpark','amt','zoo'].indexOf(ZONE.name)>=0)return 'Hier drin? Lieber nicht.';
 if(inNoGo(P.x,P.y))return 'Nicht da, wo Kinder spielen.';
 if(wanted>0)return 'Mit der Polizei im Nacken? Lieber nicht.';
 return '';
}
function fwOwn(){
 const w=fwOwnWhy();if(w){toast(w);return;}
 G.stock.fw--;const bx=P.x+Math.cos(P.a)*24,by=P.y+Math.sin(P.a)*24;
 for(let i=0;i<9;i++)FWQ.push({t:.8+i*.55,x:bx+rf(-8,8),y:by,ty:by-rf(150,260),own:1});
 closeAll();toast('Zündschnur an, drei Schritte zurück ... und: Feuerwerk!');
}
function fwShow(dur){FWS={t:dur,nx:.3};}
const FWC=['#ff4d7a','#ffd23f','#5ff0ff','#7bd86a','#b58cff','#ff9a3c','#ffffff'];
function fwSnd(k,x,y){
 const V=clamp(1-Math.hypot(x-P.x,y-P.y)/1000,.15,1);
 if(k==='launch')tn(520,.7,'sine',.022*V,1700);
 else{nz(.6,.2*V,260,'lowpass');for(let i=0;i<4;i++)nz(.04,.04*V,6000,'highpass',.25+i*.08);}
}
function fwRocket(x,y,ty,own){FWR.push({x:x,y:y,vx:rf(-16,16),vy:-rf(300,360),ty:ty,col:pick(FWC),col2:pick(FWC),k:pick(['ring','palm','crack','herz','ring']),own:own});fwSnd('launch',x,y);}
function fwBurst(r){
 const n=r.k==='crack'?44:r.k==='palm'?36:56;
 for(let i=0;i<n;i++){
  const a=i/n*6.283;let vx,vy;
  if(r.k==='herz'){const hx=16*Math.pow(Math.sin(a),3),hy=-(13*Math.cos(a)-5*Math.cos(2*a)-2*Math.cos(3*a)-Math.cos(4*a));vx=hx*5.5;vy=hy*5.5;}
  else if(r.k==='palm'){const s=rf(70,110);vx=Math.cos(a)*s*.8;vy=Math.sin(a)*s*.5-50;}
  else{const s=rf(80,125);vx=Math.cos(a)*s;vy=Math.sin(a)*s;}
  FWP.push({x:r.x,y:r.y,vx:vx,vy:vy,t:0,life:rf(1.2,1.9),col:i%3?r.col:r.col2,cr:r.k==='crack',sz:2.8});
 }
 if(FWP.length>900)FWP.splice(0,FWP.length-900);
 fwSnd('boom',r.x,r.y);
 if(G&&Math.hypot(r.x-P.x,r.y-P.y)<700){G.mood=Math.min(100,G.mood+1.2);const L=peds.filter(q=>q.st==='walk'&&!q.snow&&Math.hypot(q.x-P.x,q.y-P.y)<420);if(L.length&&chance(.6)){const q=pick(L);addFx(q.x,q.y-20,pick(['Ooooh!','Aaaah!','Wie schön!','Nochmal!']),'#fff2b0',1.6);}}
 if(r.own&&G&&!ZONE&&!FIRE&&!TRUCK&&chance(.04)){const tx=Math.floor(r.x/TS),ty=Math.floor((r.ty+200)/TS);for(let k=0;k<40;k++){const x=tx+rnd(-6,6),y=ty+rnd(-6,6);if(tget(x,y)===TR){fireTree(x,y,'Upps! Ein Funke hat einen Baum erwischt. Schnell löschen oder auf die Feuerwehr warten!');break;}}}
}
function fwUpdate(dt){
 if(!G)return;
 for(let i=FWQ.length-1;i>=0;i--){const q=FWQ[i];q.t-=dt;if(q.t<=0){fwRocket(q.x,q.y,q.ty,q.own);FWQ.splice(i,1);}}
 if(FWS){FWS.t-=dt;FWS.nx-=dt;if(FWS.nx<=0){FWS.nx=rf(.3,.85);const x=cam.x+rf(120,VW-120);fwRocket(x,cam.y+VH+30,cam.y+rf(60,VH*.5),0);}if(FWS.t<=0)FWS=null;G.mood=Math.min(100,G.mood+dt*.4);}
 for(let i=FWR.length-1;i>=0;i--){const r=FWR[i];r.x+=r.vx*dt;r.y+=r.vy*dt;if(chance(dt*30))FWP.push({x:r.x,y:r.y,vx:rf(-8,8),vy:rf(10,30),t:0,life:.4,col:'#ffd8a0',sz:1.3});if(r.y<=r.ty){fwBurst(r);FWR.splice(i,1);}}
 for(let i=FWP.length-1;i>=0;i--){const p=FWP[i];p.t+=dt;const k=Math.exp(-1.3*dt);p.vx*=k;p.vy=p.vy*k+38*dt;p.x+=p.vx*dt;p.y+=p.vy*dt;if(p.t>=p.life)FWP.splice(i,1);}
 if(ZONE&&ZONE.name==='fpark'){ZONE.fwT=(ZONE.fwT===undefined?25:ZONE.fwT)-dt;if(ZONE.fwT<=0){ZONE.fwT=150;fwShow(20);toast('Abendfeuerwerk im Freizeitpark! Alle schauen nach oben.');}}
 if(!ZONE&&G.day%3===0&&hour()>=22&&hour()<23&&G.fwDay!==G.day){G.fwDay=G.day;fwShow(30);toast('Großes Stadtfest-Feuerwerk über dem Rhein! Man sieht es in der ganzen Stadt.');}
}
function fwDraw(cx,cy){
 if(!FWP.length&&!FWR.length)return;
 ctx.save();ctx.globalCompositeOperation='lighter';
 FWP.forEach(p=>{const x=p.x-cx,y=p.y-cy;if(x<-20||x>VW+20||y<-20||y>VH+20)return;const k=p.t/p.life;if(p.cr&&k>.5&&Math.random()<.5)return;ctx.globalAlpha=Math.max(0,1-k*k);ctx.fillStyle=p.col;ctx.fillRect(x-p.sz/2,y-p.sz/2,p.sz,p.sz);if(p.sz>1.5){ctx.globalAlpha*=.3;ctx.fillRect(x-4,y-4,8,8);}});
 ctx.globalAlpha=1;FWR.forEach(r=>{ctx.fillStyle='#fff4d0';ctx.fillRect(r.x-cx-1.5,r.y-cy-1.5,3,3);});
 ctx.restore();
}
function fwBtn(){return G&&G.stock.fw>0?btn('Feuerwerk zünden ('+G.stock.fw+')','fwFire',null,{off:!!fwOwnWhy(),why:fwOwnWhy()}):'';}

function genWorld3(){
 fillR(5,64,MW-5,1,SW);fillR(5,65,MW-5,3,WT);
 fillR(114,0,1,65,SW);fillR(115,0,3,MH,WT);
 fillR(101,0,3,65,WT);
 [0,14,30,46,62].forEach(h=>fillR(101,h,3,2,DK));fillR(101,64,3,1,DK);
 fillR(95,37,17,3,WT);fillR(112,37,3,3,DK);
 const HC=['#8b3a2f','#c97b4a','#3a5a7a','#b8a45a','#6a4a7a','#4a7a5a'];let hi=0;
 const hs=(x,y,w,h)=>addB(x,y,w,h,HC[(hi++)%6],'','house',7);
 addB(95,3,5,5,'#c0392b','PIZZERIA','house',8);mkm('pizza','pizza','shop',97,8,'Pizzeria Bella Rheinhanfen','#f2b441');
 fillR(95,10,5,3,GR);tree(95,12);tree(99,12);putBK(97,11,[GR]);
 addB(105,3,6,5,'#b8862b','ASIA WOK','house',8);mkm('asia','asia','shop',107,8,'Asia Wok Glück','#f2b441');
 addB(105,10,6,3,'#7a2a4a','FLIMMERPALAST','house',9);mkm('kino','','sk',107,13,'Kino Flimmerpalast','#ff9ec7');{const m=MKS[MKS.length-1];m.sk='kino';m.act='Kino Flimmerpalast';}
 addB(95,17,5,4,'#e67e22','DÖNER','house',8);mkm('doener','doener','shop',97,21,'Döner-Palast','#f2b441');
 addB(95,24,5,4,'#2fa3d6','FREIBAD','house',8);mkm('freibad','','sk',97,28,'Freibad Planschbecken','#5fd0ff');{const m=MKS[MKS.length-1];m.sk='freibad';m.act='Freibad Planschbecken';}
 addB(105,17,6,5,'#2e86c1','TAVERNA','house',8);mkm('grieche','grieche','shop',107,22,'Taverna Olympia','#f2b441');
 addB(105,24,6,4,'#c9785a','WOHNGLÜCK','house',9);mkm('wohn','','sk',107,28,'Haus Wohnglück','#ff9ec7');{const m=MKS[MKS.length-1];m.sk='wohn';m.act='Haus Wohnglück: Wohnungen';}
 addB(95,33,5,3,'#16a085','CAFETERIA','house',7);mkm('cafe','cafe','shop',97,36,'Cafeteria Kanalblick','#f2b441');
 addB(105,33,4,3,'#2c3e50','BOOTE','house',7);mkm('boote','','sk',106,36,'Bootsverleih','#46c2a0');{const m=MKS[MKS.length-1];m.sk='boote';m.act='Bootsverleih: Boot mieten';}
 addB(109,33,2,3,'#3a2a6a','PIXEL','house',8);mkm('netz','','sk',110,36,'Netzcafé Pixelhöhle','#7af0ff');{const m=MKS[MKS.length-1];m.sk='netz';m.act='Netzcafé Pixelhöhle: Codes und Kurse';}
 addB(95,41,5,4,'#1e9e57','APOTHEKE','house',8);mkm('apo','apo','shop',97,45,'Rhein-Apotheke','#46e07a');addB(105,41,6,4,'#4f8a3a','TIERPARK','house',8);mkm('zoo','','sk',107,45,'Tierpark Rheinhanfen','#7ad35a');{const m=MKS[MKS.length-1];m.sk='zoo';m.act='Tierpark Rheinhanfen';}
 addB(105,49,6,10,'#2f6fb5','MEGAMARKT','house',10);mkm('mega','mega','shop',107,59,'MEGAMARKT','#f2b441');
 addB(95,49,5,4,'#2a6a8a','ELEKTRO','house',8);mkm('elektro','','sk',97,53,'Elektro-Ramsch','#7af0ff');{const m=MKS[MKS.length-1];m.sk='elektro';m.act='Elektro-Ramsch: Receiver, Antennen, Kabel';}fillR(95,54,5,6,GR);[[95,55],[99,55],[97,58],[95,59],[99,59]].forEach(t=>tree(t[0],t[1]));
 [[105,60],[110,60]].forEach(t=>{T[t[1]*MW+t[0]]=GR;tree(t[0],t[1]);});
}
function boatWaterT(t){return t===SH||t===DP||t===WT;}
function bridgeOK(i,j){
 const run=(dx,dy)=>{let x=i+dx,y=j+dy;for(let k=0;k<6;k++){const t=tget(x,y);if(t!==DK)return boatWaterT(t);x+=dx;y+=dy;}return false;};
 return (run(-1,0)&&run(1,0))||(run(0,-1)&&run(0,1));
}
function boatTileOK(i,j){if(i<0||j<0||i>=MW||j>=MH)return false;const t=tget(i,j);if(boatWaterT(t))return true;return t===DK&&bridgeOK(i,j);}
const BPTS=[[0,0],[1,0],[-1,0],[0,1],[0,-1],[.7,.7],[-.7,.7],[.7,-.7],[-.7,-.7]];
function boatFree(x,y){const r=10;for(let k=0;k<BPTS.length;k++){const p=BPTS[k];if(!boatTileOK(Math.floor((x+p[0]*r)/TS),Math.floor((y+p[1]*r)/TS)))return false;}return true;}
function boatNearFree(x,y){for(let d=4;d<=64;d+=4)for(let k=0;k<16;k++){const a=k/16*6.283,nx=x+Math.cos(a)*d,ny=y+Math.sin(a)*d;if(boatFree(nx,ny))return{x:nx,y:ny};}return null;}
function boatMove(R,dx,dy){
 R.hx=false;R.hy=false;
 if(!boatFree(R.x,R.y)){const f=boatNearFree(R.x,R.y);if(f){R.x=f.x;R.y=f.y;}}
 const nx=R.x+dx;
 if(boatFree(nx,R.y))R.x=nx;
 else if(dx!==0){
  let ok=false;const s=Math.min(6,Math.abs(dx)*1.6+.6);
  for(const off of[3,6,10,14]){for(const sg of[1,-1]){if(boatFree(nx,R.y+sg*off)&&boatFree(R.x,R.y+sg*s)){R.y+=sg*s;ok=true;break;}}if(ok)break;}
  if(boatFree(nx,R.y))R.x=nx;else R.hx=Math.abs(dx)>.15;
 }
 const ny=R.y+dy;
 if(boatFree(R.x,ny))R.y=ny;
 else if(dy!==0){
  let ok=false;const s=Math.min(6,Math.abs(dy)*1.6+.6);
  for(const off of[3,6,10,14]){for(const sg of[1,-1]){if(boatFree(R.x+sg*off,ny)&&boatFree(R.x+sg*s,R.y)){R.x+=sg*s;ok=true;break;}}if(ok)break;}
  if(boatFree(R.x,ny))R.y=ny;else R.hy=Math.abs(dy)>.15;
 }
 R.x=clamp(R.x,TS*.5,MW*TS-TS*.5);R.y=clamp(R.y,TS*.5,MH*TS-TS*.5);
}
function bridgeOver(){
 RIDES.forEach(R=>{
  if(R.k!=='boat'||R.x<cam.x-60||R.x>cam.x+VW+60||R.y<cam.y-60||R.y>cam.y+VH+60)return;
  const x0=Math.floor((R.x-24)/TS),x1=Math.floor((R.x+24)/TS),y0=Math.floor((R.y-24)/TS),y1=Math.floor((R.y+24)/TS);
  for(let j=y0;j<=y1;j++)for(let i=x0;i<=x1;i++)if(tget(i,j)===DK&&bridgeOK(i,j)){ctx.globalAlpha=.82;ctx.drawImage(WC,i*TS,j*TS,TS,TS,i*TS,j*TS,TS,TS);ctx.globalAlpha=1;ctx.fillStyle='rgba(0,0,0,.12)';ctx.fillRect(i*TS,j*TS+TS-5,TS,5);}
 });
}
const CBOAT=[[4.5,20.5],[4.5,52.5],[30,65.5],[70,65.5],[101.4,22],[101.4,52],[109.5,37.5],[115.4,10],[115.4,44]];
function cityBoats(){CBOAT.forEach(q=>{const R=mkRide('boat',q[0]*TS,q[1]*TS,q[1]>64?0:Math.PI/2);if(!boatFree(R.x,R.y)){const f=boatNearFree(R.x,R.y);if(f){R.x=f.x;R.y=f.y;}}RIDES.push(R);});}
function boatNearDock(){const m=MKQ.boote;if(!m)return null;let b=null,bd=110;RIDES.forEach(R=>{if(R.k!=='boat')return;const d=Math.hypot(R.x-m.x,R.y-m.y);if(d<bd){bd=d;b=R;}});return b;}
function rideLab(rd){return rd.oma&&!rd.stolen?'OK: Rollstuhl klauen':'OK: '+(XRD[rd.k]?(rd.stolen?XRS[rd.k]:XRL[rd.k]):({sled:'Rodeln',chair:'Rollstuhl nehmen',boat:'Boot besteigen',bike:'Fahrrad nehmen',scoot:'Autoscooter fahren',ski:'Ski anschnallen'}[rd.k]||'Einsteigen'));}
function boatCall(board){
 const tx=109.5*TS,ty=37.5*TS;
 if(P.ride){toast('Du sitzt doch schon in einem Boot.');return;}
 let b=null,bd=1e9;RIDES.forEach(R=>{if(R.k!=='boat')return;const d=Math.hypot(R.x-tx,R.y-ty);if(d<bd){bd=d;b=R;}});
 if(!b){toast('Alle Boote sind unterwegs.');return;}
 b.x=tx;b.y=ty;b.a=0;b.sp=0;sfx('wave');
 if(board){takeRide(b);toast('Leinen los! Du sitzt im Boot. Hoch gibt Gas, Links und Rechts lenken. Rund um die Stadt: Rhein, Südkanal, Grachten und Ostkanal. Unter allen Brücken durch!');return;}
 toast('Der Bootsverleiher pfeift, und ein Boot tuckert an den Anleger rechts neben dem Häuschen. Hin und OK drücken zum Einsteigen.');
}
const FOOD={
 pizza:{t:'Pizzeria Bella Rheinhanfen',x:'Der Pizzaiolo wirbelt den Teig über seinem Kopf. Einmal landet er fast an der Lampe.',m:[['Pizza Margherita',8,7,'Knusprig, käsig, perfekt. Der Chef singt dabei eine Arie.'],['Pizza Rheinhanfen mit allem',11,10,'Mit allem heißt hier wirklich alles. Sogar ein bisschen Konfetti.'],['Tiramisu',5,5,'So luftig, dass es fast vom Teller schwebt.']]},
 doener:{t:'Döner-Palast',x:'„Mit allem und scharf?“ Der Spieß dreht sich, das Messer blitzt.',m:[['Döner mit allem, scharf',7,7,'Scharf! Dein Kopf glüht, deine Laune auch.'],['Dürüm',7,7,'Eng gerollt und randvoll. Kein Krümel geht verloren.'],['Ayran',2,3,'Kalt, salzig, erfrischend. Der beste Durstlöscher der Stadt.']]},
 grieche:{t:'Taverna Olympia',x:'Blau-weiße Tischdecken, Sirtaki aus dem Radio. Der Wirt ruft: „Opa!“',m:[['Gyros-Teller mit Tzatziki',13,10,'Gyros, Pommes, Tzatziki. Morgen riechst du noch ein bisschen nach Knoblauch.'],['Bauernsalat',9,6,'Feta, Oliven, Tomaten. Schmeckt nach Urlaub.'],['Ouzo aufs Haus',0,4,'ouzo']]},
 asia:{t:'Asia Wok Glück',x:'Der Wok zischt, Flammen schlagen hoch. Am Fenster winkt eine goldene Katze.',m:[['Gebratene Nudeln',9,7,'Mit Gemüse, Ei und genau der richtigen Menge Knoblauch.'],['Sushi-Boot',15,11,'Das Sushi kommt auf einem kleinen Holzboot. Passend zu den Grachten draußen!'],['Glückskeks',1,2,'keks']]},
 cafe:{t:'Cafeteria Kanalblick',x:'Kaffeeduft, Kuchenvitrine und Fensterplätze mit Blick auf die Boote.',m:[['Kaffee und Kuchen',5,6,'Der Käsekuchen ist so hoch, dass du ihn von zwei Seiten anfangen musst.'],['Currywurst Pommes',6,6,'Ehrliche Kantinenküche. Die Soße ist ein Familienrezept.'],['Kakao mit Sahne',3,4,'Sahnebart inklusive.']]},
 mega:{t:'MEGAMARKT',x:'So groß, dass zwischen den Regalen Straßenschilder hängen. Am Probierstand lächelt eine Verkäuferin.',m:[['Probierstand: Käsewürfel',0,2,'Gratis! Du nimmst drei. Die Verkäuferin tut so, als hätte sie es nicht gesehen.'],['Einkaufswagen-Rennen im Gang 12',0,4,'Du flitzt mit dem Einkaufswagen durch den Gang. Ein Rentner applaudiert.'],['Grillpaket im Angebot (3 €)',3,1,'grill']]}
};
const KEKS=['Heute wirst du eine Pommes finden, die länger ist als alle anderen.','Wer im Boot sitzt, sollte nicht mit Steinen werfen.','Ein Lächeln kostet nichts. Ein Döner schon.','Du wirst bald eine Reise machen. Vermutlich zum Büdchen.','Glück ist, wenn der Glückskeks recht hat.'];
function eatMenu(k){
 const F=FOOD[k];if(!F)return;
 mdl(F.t,F.x,F.m.map((q,i)=>[q[0]+(q[1]?' ('+q[1]+' €)':' (gratis)'),'eat:'+k+':'+i,G.cash<q[1]]));
}
const ESK={buehne:1,malbar:1,haxn:1,souv:1,liege:1,boote:1};
function eMenu(k){
 if(k==='boote')mdl('Bootsverleih','„Moin! Boote gibt es hier gratis, solange du sie heil zurückbringst.“ Mit dem Boot kommst du über den Rhein, den Südkanal, durch die Grachten und den Ostkanal einmal rund um die Stadt. Unter allen Brücken durch!',[[boatNearDock()?'Einsteigen, das Boot liegt bereit':'Boot holen und gleich einsteigen','e:bootin'],['Boot nur an den Anleger holen','e:boot'],['Wie fahre ich Boot?','e:boottip']]);
 else if(k==='buehne')mdl('Schlagerbühne im Partyzelt','Auf der Bühne dreht ein DJ mit Sonnenbrille die Regler auf. Hunderte Arme sind in der Luft.',[['Mitsingen','e:sing'],['Polonaise starten!','e:polo',!!POLO],['Beim DJ einen Song wünschen','e:dj']]);
 else if(k==='malbar')mdl('Sangria-Bar','Eimer, Strohhalme, Sonnenbrand. Der Barkeeper trägt ein Hawaiihemd mit Flamingos.',[['Sangria-Eimer mit Strohhalmen (6 €)','e:sangria',G.cash<6],['Cocktail „Malle Sunrise“, ohne Alkohol (4 €)','e:cocktail',G.cash<4],['Wasser (1 €)','e:wasser',G.cash<1]]);
 else if(k==='haxn')mdl('Haxn-Hütte','Hier gibt es deutsche Küche, nur lauter. Die Haxe ist so groß wie ein Kopfkissen.',[['Schweinshaxe XXL (12 €)','e:haxe',G.cash<12],['Currywurst Malle-Style (6 €)','e:curry',G.cash<6],['Pommes rot-weiß (4 €)','e:pommes',G.cash<4]]);
 else if(k==='souv')mdl('Souvenir-Laden','Postkarten, Sonnenhüte, Shirts mit fragwürdigen Sprüchen und eine Muschel, die singt.',[['Sonnenhut (5 €)','e:hut',G.cash<5||!!G.hut],['Sonnencreme LSF 50 (4 €)','e:creme',G.cash<4],['Malle-Shirt (8 €)','e:shirt',G.cash<8],['Postkarte nach Hause (1 €)','e:karte',G.cash<1]]);
 else if(k==='liege')mdl('Liegestuhl am Strand','Ein freier Liegestuhl! Ein seltener Anblick. Daneben liegen schon drei Handtücher auf leeren Liegen.',[['Handtuch drauflegen und reservieren','e:handtuch'],['In der Sonne dösen','e:doesen']]);
}
function skAct15(p){
 if(p.indexOf('eat:')===0){
  const a=p.split(':'),F=FOOD[a[1]],q=F&&F.m[+a[2]];if(!q)return true;
  if(G.cash<q[1]){toast('Nicht genug Geld.');return true;}
  if(q[3]==='ouzo'){const w=noUse();if(w){mood(3,'+3');toast('Der Wirt zwinkert: „Für dich gibt es Traubensaft aufs Haus.“');return true;}G.drunk+=1;mood(4,'+4 Opa!');sfx('glug');toast('„Opa!“ Der Ouzo geht aufs Haus. Alle am Tisch prosten dir zu.');if(G.drunk>=6)blackout();return true;}
  if(q[3]==='grill'){if((G.stock.wurst||0)>=20){toast('Mehr passt nicht in den Rucksack.');return true;}G.cash-=3;G.stock.wurst=(G.stock.wurst||0)+1;sfx('coin');toast('Ein Grillpaket im Angebot. Fürs nächste Lagerfeuer!');return true;}
  G.cash-=q[1];needAdd(q[1]>=4?55:q[1]>=2?30:15,q[1]>=4?20:10);mood(q[2],'+'+q[2]+' Lecker');sfx(q[1]?'coin':'ok');G.drunk=Math.max(0,G.drunk-(q[1]>=6?1:0));G.essen=(G.essen||0)+1;
  toast(q[3]==='keks'?'Im Glückskeks steht: „'+pick(KEKS)+'“':q[3]);
  return true;
 }
 if(p.indexOf('e:')!==0)return false;
 const k=p.slice(2);
 const pay=n=>{if(G.cash<n){toast('Nicht genug Geld.');return false;}G.cash-=n;sfx('coin');return true;};
 if(k==='boot')boatCall(false);
 else if(k==='bootin')boatCall(true);
 else if(k==='boottip')showModal({title:'Bootfahren',text:'OK am Boot: einsteigen. Hoch gibt Gas, Runter bremst, Links und Rechts lenken. An Ufern gleitet das Boot entlang, unter Brücken fährst du einfach durch. Zum Aussteigen langsam ans Ufer fahren und OK drücken.',choices:[{label:'Leinen los!',a:'mclose'}]});
 else if(k==='sing'){mood(7,'+7 Schlager');sfx('musik');toast(pick(['Du singst den Refrain so laut mit, dass der DJ dir das Mikro reicht. Tosender Applaus!','Den Text kennst du nicht, aber das stört hier niemanden. Lalala, hey!','Du singst mit. Die Leute neben dir singen mit. Das ganze Zelt singt mit. Gänsehaut!']));}
 else if(k==='polo'){closeAll();poloStart();}
 else if(k==='dj'){if(ZONE&&ZONE.mus){const L=SONGS.map((q,i)=>i).filter(i=>SONGS[i].gi===1||SONGS[i].gi===2);const c=L.indexOf(ZONE.mus.si);ZONE.mus.si=L[(c+1)%L.length];ZONE.mus.st=0;ZONE.mus.mt=0;toast('Der DJ nickt: „Kommt sofort!“ Jetzt läuft: „'+SONGS[ZONE.mus.si].t+'“');}mood(3,'+3');}
 else if(k==='sangria'){const w=noUse();if(w){toast(w);return true;}if(!pay(6))return true;G.drunk+=1;mood(10,'+10 Sangria');sfx('glug');toast('Der Eimer hat zwölf Strohhalme. Nach zwei Minuten kennst du alle mit Vornamen.');if(G.drunk>=6)blackout();}
 else if(k==='cocktail'){if(!pay(4))return true;mood(6,'+6');sfx('glug');toast('Orange, Grenadine, ein Schirmchen und eine Wunderkerze. Ganz ohne Alkohol und trotzdem ein Fest.');}
 else if(k==='wasser'){if(!pay(1))return true;G.drunk=Math.max(0,G.drunk-1);sfx('glug');toast('Wasser! Der heimliche Held jeder Party.');}
 else if(k==='haxe'){if(!pay(12))return true;mood(9,'+9');G.drunk=Math.max(0,G.drunk-1);toast('Die Haxe ist riesig. Du brauchst drei Anläufe und eine Pause. Grandios.');}
 else if(k==='curry'){if(!pay(6))return true;mood(5,'+5');toast('Currywurst mit Meerblick. Fast wie zu Hause, nur mit mehr Sand.');}
 else if(k==='pommes'){if(!pay(4))return true;mood(4,'+4');toast('Pommes rot-weiß. Eine Möwe beobachtet dich sehr genau.');}
 else if(k==='hut'){if(!pay(5))return true;G.hut=true;mood(3,'+3');toast('Ein Sonnenhut mit Bommeln. Ab jetzt kein Sonnenbrand mehr!');}
 else if(k==='creme'){if(!pay(4))return true;G.cremeT=300;G.sunT=0;mood(2,'+2');toast('Eingecremt! Fünf Minuten bist du vor der Sonne sicher.');}
 else if(k==='shirt'){if(!pay(8))return true;mood(5,'+5');toast('Auf dem Shirt steht: „Ich war auf Malle und alles, was ich mitbrachte, war dieses Shirt und ein Sonnenbrand.“');}
 else if(k==='karte'){if(!pay(1))return true;mood(2,'+2');toast('Du schreibst: „Wetter super, Essen super, Polonaise super. Bis bald!“');}
 else if(k==='handtuch'){mood(3,'+3');toast('Handtuch drauf. Die Liege ist jetzt offiziell reserviert, bis übermorgen. Mindestens.');}
 else if(k==='doesen'){mood(5,'+5');if(!G.hut&&!(G.cremeT>0))G.sunT=(G.sunT||0)+50;toast('Du döst in der Sonne. Die Wellen rauschen, irgendwo läuft Schlager.');}
 return true;
}
let POLO=null;
function poloStart(){
 if(POLO){toast('Die Polonaise läuft schon!');return;}
 const L=peds.filter(p=>(p.st==='walk'||p.st==='dance')&&!p.snow&&Math.hypot(p.x-P.x,p.y-P.y)<380).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y)).slice(0,12);
 if(L.length<2){toast('Zu wenig Leute in der Nähe für eine Polonaise.');return;}
 POLO={t:45,n:L.length,trail:[]};for(let i=0;i<90;i++)POLO.trail.push({x:P.x,y:P.y});
 L.forEach((p,i)=>{p.st='polo';p.pi=i;});
 mood(8,'+8 Polonaise');sfx('clap');
 toast('Polonaise! Hände auf die Schultern und los! '+L.length+' Leute hängen sich hinter dich. Lauf einfach herum, alle folgen dir.');
}
function poloPed(p,dt){
 if(p.st!=='polo')return false;
 if(!POLO){p.st='walk';return false;}
 const tr=POLO.trail,t=tr[Math.max(0,tr.length-1-(p.pi+1)*6)];
 const dx=t.x-p.x,dy=t.y-p.y,d=Math.hypot(dx,dy);
 if(d>2){const s=Math.min(d,(d>60?220:150)*dt);p.x+=dx/d*s;p.y+=dy/d*s;p.a=Math.atan2(dy,dx);p.walk+=s*.15;}
 return true;
}
function poloEnd(){
 if(!POLO)return;const n=POLO.n;POLO=null;let f=0;
 peds.forEach(p=>{if(p.st==='polo'){p.st='walk';if(!p.like&&chance(.5)){p.like=true;f++;}}});
 mood(6,'+6');toast('Die Polonaise löst sich auf. Alle sind außer Puste und glücklich.'+(f?' '+f+' neue Freunde!':''));
}
function malleUpdate(dt){
 if(!G)return;
 if(POLO){
  POLO.t-=dt;const l=POLO.trail[POLO.trail.length-1];
  if(Math.hypot(P.x-l.x,P.y-l.y)>5){POLO.trail.push({x:P.x,y:P.y});if(POLO.trail.length>400)POLO.trail.shift();}
  G.mood=Math.min(100,G.mood+dt*.6);
  if(chance(dt*.9)){const f=peds.filter(p=>p.st==='polo');if(f.length){const p=pick(f);addFx(p.x,p.y-20,pick(['Polonaise!','Hey! Hey! Hey!','Hände hoch!','Juchhu!','Weiter, weiter!']),'#fff2b0',1.4);}}
  if(POLO.t<=0||P.inCar||P.ride)poloEnd();
 }
 if(G.cremeT>0)G.cremeT-=dt;
 if(ZONE&&ZONE.name==='malle'){
  G.mood=Math.min(100,G.mood+dt*.15);
  if(!G.hut&&!(G.cremeT>0)&&!P.ride){G.sunT=(G.sunT||0)+dt;if(G.sunT>=110){G.sunT=-150;mood(-6,'Sonnenbrand');toast('Autsch, Sonnenbrand! Du leuchtest wie ein Hummer. Sonnenhut oder Sonnencreme gibt es im Souvenir-Laden.');}}
  if(ZONE.mus&&chance(dt*1.2))addFx(ZONE.mus.x+rf(-90,90),ZONE.mus.y-40+rf(-10,10),pick(['♪','♫']),pick(['#ff5fd0','#5ff0ff','#ffd23f']),1.6,-30);
 }
}
function genMalle(z,H){
 const zs=H.zs,zf=H.zf,mk=H.mk,R=H.R,zg=H.zg;
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++)zs(x,y,y<6?DP:y<8?SH:y<16?SA:y<27?SW:SA);
 for(let x=0;x<ZW;x+=3){if(R(0,2))zs(x,28,TR);zs(x+1,29,TR);}
 const bd=(x,y,w,h,c,n,k)=>{zf(x,y,w,h,BL);z.BLD.push({x:x,y:y,w:w,h:h,c:c,n:n,k:k||'house',hh:6});};
 bd(4,18,6,4,'#e5504d','SANGRIA-BAR','bude');{const m=mk('malbar','sk',6,22,'Sangria-Bar','Sangria-Bar besuchen');m.sk='malbar';m.col='#ffb347';}
 bd(11,18,5,4,'#8a5a2a','HAXN-HÜTTE','bude');{const m=mk('haxn','sk',13,22,'Haxn-Hütte','Haxn-Hütte besuchen');m.sk='haxn';m.col='#ffb347';}
 bd(18,18,12,4,'#ff5fd0','PARTYZELT','bude');{const m=mk('buehne','sk',24,22,'Schlagerbühne','Zur Schlagerbühne');m.sk='buehne';m.col='#ff5fd0';}
 bd(32,18,5,4,'#2e86c1','SOUVENIRS','bude');{const m=mk('souv','sk',34,22,'Souvenir-Laden','Souvenirs anschauen');m.sk='souv';m.col='#ffb347';}
 bd(39,18,7,4,'#f4d58a','HOTEL PLAYA','house');
 bd(9,25,7,2,'#f0c8a0','APARTMENTS SOL','house');bd(29,25,9,2,'#a8d8e8','HOTEL BRISA','house');
 for(let i=0;i<9;i++){const x=R(2,ZW-4),y=R(9,13);if(zg(x,y)===SA&&zg(x+1,y)===SA){zs(x,y,UM);zs(x+1,y,LC);}}
 [[3,15],[16,15],[30,15],[45,15],[10,8],[40,8]].forEach(q=>{if(zg(q[0],q[1])===SA)zs(q[0],q[1],TR);});
 {const m=mk('liege','sk',22,12,'Freier Liegestuhl','Liegestuhl anschauen');m.sk='liege';m.col='#ffb347';}
 [[12,6],[34,6]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
 const si=SONGS.findIndex(q=>q.gi===1);
 z.mus={x:24*TS,y:20*TS,si:si<0?0:si,mt:0,st:0,music:true};
}
function mallePeds(z,add){
 add(8,[SA],q=>{q.st='lie';q.stT=1e9;q.tw=pick(['#e5604d','#2e86c1','#f1c40f','#27ae60','#8e44ad']);});
 add(8,[SW]);
 add(14,[SW],q=>{q.x=24*TS+rf(-170,170);q.y=23*TS+rf(0,90);q.st='dance';q.stT=1e9;});
}

function myBeer(){return ['b_pils','b_koelsch','b_alt'].find(g=>(G.inv[g]||0)>0)||null;}
function canSellPed(){return SELL.some(g=>(G.inv[g]||0)>0);}
function pedWish(p){if(!p.wish)p.wish=pick(p.teen?MENUS.concat(['b_frei']):MENUS.concat(BEERS));return p.wish;}
function pedWhy(p,g,ng,mn){
 if(p.kid)return 'Kinder bekommen nichts angedreht. Die haben Taschengeld für Eis.';
 if(p.sold)return p.nm+' hat schon etwas von dir.';
 if(ALC[g]||ILL[g]){
  if(p.teen)return 'Doch nicht an Jugendliche!';
  if(mn)return 'Jugendschutz: Ein Kind oder Jugendlicher ist in der Nähe.';
  if(ng)return 'Hier ist '+ng.n+': Kein Alkohol, kein Gras!';
 }
 if(ILL[g]&&ZONE)return 'Hier nicht. Gras verkaufst du, wenn überhaupt, nur in Rheinhanfen.';
 if(ILL[g]&&wanted>0)return 'Die Polizei ist hinter dir her. Erst mal abtauchen!';
 return '';
}
function pedOfferScreen(){
 const p=UI.ped;if(!p)return{cls:'c',hint:'',html:''};
 const ng=inNoGo(P.x,P.y),mn=minorNear(P.x,P.y,120),w=pedWish(p);
 let b='',df=0;
 SELL.forEach(g=>{
  const n=G.inv[g]||0;if(!n)return;
  const why=pedWhy(p,g,ng,mn),fav=g===w;
  b+=btn(GOODS[g].n+(ILL[g]?' (illegal)':'')+': '+eur(pedPrice(g))+(fav?' ♥':''),'pSell',g,{off:!!why,why:why,cls:ILL[g]?'d':'',def:(!why&&!df&&(fav||!ILL[g]))?(df=1):0,note:'Dabei: '+n+(ILL[g]?' · Zivilstreifen möglich, die Polizei wird aufmerksam':'')});
 });
 b+=btn('Doch nicht','pBack',null,{def:df?0:1});
 const tip=p.kid?'Kinder bekommen nichts.':p.teen?'Jugendliche bekommen nur Menüs und Alkoholfreies.':'Hat Lust auf: <b>'+GOODS[w].n+'</b>. Menüs und Getränke sind legal, Gras auf der Straße nicht.';
 return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+p.nm+' etwas anbieten</h2><div class="mu">'+tip+'</div></div>'+b+'</div>'};
}
function streetRisk(g){return Math.min(.6,((g==='c_str'?.16:g==='c_plant'?.12:.1)+G.heat/400)*evMult('street','*'));}
function pedSell(g){
 const p=UI.ped;if(!p||!GOODS[g])return;
 const why=pedWhy(p,g,inNoGo(P.x,P.y),minorNear(P.x,P.y,120));if(why){toast(why);return;}
 if((G.inv[g]||0)<1)return;
 if(ILL[g]){
  if(chance(streetRisk(g))){
   G.inv[g]--;p.sold=1;heat(15);closeAll();addFx(p.x,p.y-24,'POLIZEI!','#6fa8ff',2);
   startWanted('Zivilstreife! '+p.nm+' zückt eine Dienstmarke. Weg hier!');return;
  }
  if(chance(p.like?.15:.3)){
   p.sold=1;heat(3);closeAll();
   addFx(p.x,p.y-22,pick(['Nee, lass mal.','Ich hol mir das in der Apotheke.','Ich hab ein Rezept, danke!','Bist du verrückt?']),'#ffd23f',1.8);
   toast(p.nm+' will nichts. Ganz schön riskant, was du da machst.');return;
  }
  const pr=pedPrice(g);
  G.inv[g]--;G.cash+=pr;G.stats.earned+=pr;G.stats.street=(G.stats.street||0)+1;popAdd(-1);p.sold=1;heat(g==='c_str'?10:7);
  addFx(p.x,p.y-22,'+'+eur(pr),'#6bcf63',1.6);closeAll();
  if(copNear(P.x,P.y,260)&&wanted===0){startWanted('Ein Polizist hat den Deal gesehen! Weg hier!');return;}
  toast('Deal geklappt: +'+eur(pr)+'.'+(G.heat>=30?' Die Polizei hat dich jetzt auf dem Kieker!':' Die Polizei wird aber aufmerksamer.'));
  return;
 }
 const fav=pedWish(p)===g;
 if(!chance(fav?.92:.5)){
  p.sold=1;closeAll();
  addFx(p.x,p.y-22,pick(['Danke, bin satt!','Hab schon gegessen.','Vielleicht morgen!','Ich hätte eher Lust auf '+GOODS[pedWish(p)].n+'.']),'#ffd23f',1.8);
  toast(p.nm+' will gerade nicht. Probier es bei jemand anderem.');return;
 }
 const tip=fav?rnd(2,5):p.like?rnd(1,2):0,pr=pedPrice(g)+tip;
 G.inv[g]--;G.cash+=pr;G.stats.earned+=pr;p.sold=1;
 if(fav)p.like=true;
 mood(1,'+1');sfx('coin');
 addFx(p.x,p.y-22,pick(['Mmh, lecker!','Genau das!','Danke!','Prost!'])+' +'+eur(pr),'#6bcf63',1.8);
 closeAll();
 toast(gq(g,1)+' verkauft: +'+eur(pr)+(tip?' (mit '+eur(tip)+' Trinkgeld)':'')+'.');
}
function kalleMenu(){
 const p=price('c_str','kalle');
 showModal({title:'Hinterhof-Kalle',text:'"Psst ... Straßenware. Billig, aber keiner weiß genau, was drin ist. Und die Polizei guckt hier gern mal vorbei." Weiterverkauf ist illegal.',choices:[{label:'1 Tütchen ('+eur(p)+')',a:'kalleB',p:'1'},{label:'5 Tütchen ('+eur(p*5)+')',a:'kalleB',p:'5'},{label:'Lieber nicht',a:'mclose'}]});
}
function kalleBuy(q){
 UI.modal=null;
 if(minorNear(P.x,P.y,120)){toast('Nicht vor Kindern und Jugendlichen!');render2();return;}
 const r=buyAt('c_str',q,'kalle');
 if(r.ok&&chance(.06+G.heat/350)&&wanted===0){closeAll();startWanted('Razzia im Hinterhof! Kalle ist weg, und die Polizei sieht dich mit der Tüte. Lauf!');return;}
 res(r);
}
function hollBuy(q){
 if(minorNear(P.x,P.y,90)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht daneben.');return;}
 const r=buyAt('c_holl',q,'coffeeshop');
 if(r.ok)r.msg+=' In Rheinhanfen ist der Weiterverkauf illegal. Pass auf dich auf!';
 res(r);
}
function streetBust(){
 const n=(G.inv.c_holl||0)+(G.inv.c_str||0)+(G.inv.c_plant||0);
 if(n<=0)return '';
 G.inv.c_holl=0;G.inv.c_str=0;G.inv.c_plant=0;G.apoBan=G.day+2;
 return 'Beschlagnahmt: '+n+' Tütchen Gras. Die Rhein-Apotheke hat davon gehört: zwei Tage keine Rezept-Touren.';
}
function placeShop(mk){
 const k=mk.dist,sh=SHOP[k];let b='';
 const df=G.active.some(m=>canPickup(m)||(m.to===G.loc&&canDeliver(m)));
 const nd=needAt(k);let d1=!df;
 if(nd.length){b+=btn('Für deine Aufträge einkaufen','needBuy',null,{cls:'b',def:d1?1:0,note:nd.map(x=>gq(x[0],x[1])).join(', ')+' für '+eur(nd.reduce((s,x)=>s+x[1]*price(x[0],k),0))});d1=false;}
 if(sh){
  if(sh.length>1)b+=btn('Getränke einzeln kaufen','market',null,{def:d1?1:0,note:sh.map(g=>GOODS[g].n).join(', ')+', zum Weiterverkaufen an Leute auf der Straße'});
  else b+=btn('1× '+GOODS[sh[0]].n+' kaufen: '+eur(price(sh[0],k)),'buy',sh[0]+':1',{def:d1?1:0,note:'Dabei: '+(G.inv[sh[0]]||0)+' · zum Weiterverkaufen an Leute auf der Straße'});
  d1=false;
 }
 if(k==='apo'){
  const ban=G.apoBan&&G.day<G.apoBan;
  b+=btn('Rezept-Touren ansehen','apoMis',null,{def:d1?1:0,note:ban?'Gesperrt bis Tag '+G.apoBan+': Die Apothekerin hat von deinem Straßenhandel gehört.':(G.stats.apo||0)+' Rezepte zugestellt. Neue Touren stehen auch im Handy unter Aufträge.'});
  d1=false;
 }
 b+=aniPlaceBtns(k);
 b+=extPlaceBtns(k);
 if(k==='hafen')b+=btn('Hinterhof: Kalle macht „Psst“ …','kalle',null,{cls:'d',note:'Straßen-Gras, '+eur(price('c_str','kalle'))+' das Tütchen. Illegal!'});
 return b;
}
function tradeMarket(){
 const k=G.loc,L=SHOP[k]||[];let b='';
 L.forEach((t,i)=>{b+=btn(GOODS[t].n+' ('+GOODS[t].u+'): '+eur(price(t,k)),'buy',t+':1',{cls:'b',def:i===0?1:0,note:'Dabei: '+(G.inv[t]||0)+(ALC[t]?' · nur für Erwachsene':'')});});
 return{hint:'Pfeiltasten: wählen · OK: 1 kaufen · Zurück: zum Ort',html:'<div class="place"><div class="hd"><h2>'+DIST[k].n+'</h2><div class="mu">Bargeld <b class="gr">'+eur(G.cash)+'</b> · Tragen <b class="am">'+used()+' / '+cap()+'</b></div></div>'+b+btn('Fertig','back')+'</div>'};
}

const ANT={
 zebra:{n:'Zebra',art:'Das',e:'ein',zoo:1,names:['Zora','Zacharias','Zippo'],sp:34},
 giraffe:{n:'Giraffe',art:'Die',e:'eine',zoo:1,names:['Gisela','Gustav','Gina'],sp:30},
 lama:{n:'Lama',art:'Das',e:'ein',zoo:1,names:['Lothar','Lola','Lasse'],sp:32},
 kaenguru:{n:'Känguru',art:'Das',e:'ein',zoo:1,names:['Hüpfi','Kira','Kasimir'],sp:46},
 pinguin:{n:'Pinguin',art:'Der',e:'ein',zoo:1,names:['Pingo','Frack','Polly'],sp:24},
 flamingo:{n:'Flamingo',art:'Der',e:'ein',zoo:1,names:['Flora','Fridolin','Rosalie'],sp:26},
 schwein:{n:'Schwein',art:'Das',e:'ein',zoo:0,names:['Rosi','Borste','Trüffel'],sp:28},
 ziege:{n:'Ziege',art:'Die',e:'eine',zoo:0,names:['Zenzi','Meckerle','Heidi'],sp:34},
 schaf:{n:'Schaf',art:'Das',e:'ein',zoo:0,names:['Wolke','Bauschi','Flöckchen'],sp:26}
};
const ZOOK=['zebra','giraffe','lama','kaenguru','pinguin','flamingo'],FARMK=['schwein','ziege','schaf'];
const MASCK=['hq','pizza','doener','grieche','asia','cafe'];
const PETL={
 zebra:['Das Zebra lässt sich die Streifen kraulen. Schwarz auf Weiß oder Weiß auf Schwarz? Es verrät es nicht.'],
 giraffe:['Die Giraffe beugt sich weit herunter und schleckt dir einmal quer übers Gesicht. Bäh, aber süß.'],
 lama:['Das Lama summt zufrieden. Kein Spucken, versprochen.'],
 kaenguru:['Das Känguru boxt sanft in die Luft und hüpft dann einmal im Kreis. Applaus!'],
 pinguin:['Der Pinguin watschelt auf dich zu und verbeugt sich. Ein echter Gentleman im Frack.'],
 flamingo:['Der Flamingo steht auf einem Bein und guckt dich an, als wüsstest du nicht, wie Gleichgewicht geht.'],
 schwein:['Das Schwein grunzt glücklich und lässt sich am Bauch kraulen.'],
 ziege:['Die Ziege knabbert an deinem Ärmel. Das ist ihre Art, Hallo zu sagen.'],
 schaf:['Das Schaf ist so flauschig, dass deine Hand kurz darin verschwindet.']
};
let ANI=[],ANIT=60;ANI.g=null;
const MASCO={};
function aniList(){return ZONE?(ZONE.ani||[]):ANI;}
function aniNew(t,x,y,o){return Object.assign({t:t,nm:pick(ANT[t].names),x:x,y:y,a:rf(0,6.28),walk:0,steer:rf(1,3),fol:false,cd:0},o||{});}
function aniDesc(d){return d.nm+' ('+ANT[d.t].n+')';}
function aniLead(){if(ZONE)return null;return ANI.find(q=>q.fol)||null;}
function aniSpawn(silent){
 const t=chance(.7)?pick(ZOOK):pick(FARMK);
 const p=randTile([SW,GR],silent?260:420,1700,P.x,P.y);
 const d=aniNew(t,p.x,p.y);ANI.push(d);
 if(!silent)toast('Ausgebüxt! '+ANT[t].art+' '+ANT[t].n+' '+d.nm+' spaziert durch Rheinhanfen. '+(ANT[t].zoo?'Bring es zum Tierpark im Grachtenviertel!':'Es gehört aufs Landgut Hopfenhof.'));
 return d;
}
function aniRemove(d){const i=ANI.indexOf(d);if(i>=0)ANI.splice(i,1);}
function mascList(){
 if(ZONE||!G||!G.masc)return[];
 const L=[];
 Object.keys(G.masc).forEach(k=>{const m=MKQ[k],v=G.masc[k];if(!m||!v||!ANT[v.t])return;let o=MASCO[k];if(!o||o.t!==v.t){o=MASCO[k]={t:v.t,nm:v.nm,x:m.x+30,y:m.y+4,a:Math.PI/2,walk:0,cd:0,mas:k};}L.push(o);});
 return L;
}
function aniStep(d,dt){
 d.cd=Math.max(0,d.cd-dt);
 const sp=ANT[d.t].sp;
 if(d.fol&&!ZONE){
  if(P.inCar||P.ride)return;
  const dx=P.x-d.x,dy=P.y-d.y,dd=Math.hypot(dx,dy);
  if(dd>280){const f=freeSpot(P.x-Math.cos(P.a)*26,P.y-Math.sin(P.a)*26);d.x=f.x;d.y=f.y;return;}
  if(dd>30){const v=Math.min(dd*2.4,FOOT*(P.fast>0?1.9:1.25));d.a=Math.atan2(dy,dx);moveE(d,dx/dd*v*dt,dy/dd*v*dt,6);d.walk+=dt*v*.12;}
  return;
 }
 if(d.hx!==undefined)leash(d,d.hx,d.hy,d.lr||120);
 steerStep(d,dt,sp*.55);
}
function zooSig(){return ZOOK.map(k=>(G.zoo&&G.zoo[k])||0).join(',');}
function zooFill(z){
 z.ani=[];z.zsig=zooSig();
 (z.pens||[]).forEach(p=>{
  const n=Math.min(4,1+((G.zoo&&G.zoo[p.k])||0));
  for(let i=0;i<n;i++){
   let x=0,y=0;
   for(let k=0;k<60;k++){x=rf(p.x0+14,p.x1-14);y=rf(p.y0+14,p.y1-14);if(skOk(x,y))break;}
   z.ani.push(aniNew(p.k,x,y,{pen:1}));
  }
 });
}
function aniUpdate(dt){
 if(!G)return;
 if(ANI.g!==G){ANI.length=0;ANI.g=G;ANI.init=0;ANIT=rf(50,80);Object.keys(MASCO).forEach(k=>delete MASCO[k]);}
 if(ZONE){
  if(ZONE.name==='zoo'&&(!ZONE.ani||ZONE.zsig!==zooSig()))zooFill(ZONE);
  (ZONE.ani||[]).forEach(d=>aniStep(d,dt));
  return;
 }
 if(!ANI.init){ANI.init=1;for(let i=0;i<3;i++)aniSpawn(true);}
 ANIT-=dt;if(ANIT<=0){ANIT=rf(80,130);if(ANI.length<5&&wanted===0)aniSpawn(false);}
 ANI.forEach(d=>aniStep(d,dt));
 mascList().forEach(o=>{o.cd=Math.max(0,o.cd-dt);o.walk+=dt*.8;});
}
function nearAni(){
 if(P.inCar||P.sit||P.ride||P.build||P.fish||P.fight)return null;
 let b=null,bd=ZONE?50:36;
 aniList().concat(mascList()).forEach(d=>{if(d.fol)return;const dd=Math.hypot(d.x-P.x,d.y-P.y);if(dd<bd){bd=dd;b=d;}});
 return b;
}
function aniPrompt(d){return(ZONE||d.mas)?'OK: '+d.nm+' streicheln':'OK: '+aniDesc(d)+' anleinen';}
function aniOpen(d){
 if(ZONE||d.mas){
  if(d.cd>0){toast(d.nm+' ist gerade beschäftigt.');return;}
  d.cd=6;mood(4,'+4 Tierliebe');sfx('aww');addFx(d.x,d.y-18,'♥','#ff4d7a',1.4);
  toast(pick(PETL[d.t]));return;
 }
 const cur=aniLead();
 if(cur){toast('Du hast schon '+cur.nm+' an der Leine. Erst abgeben oder im Rucksack losbinden.');return;}
 d.fol=true;sfx('pick');addFx(d.x,d.y-18,'♥','#ff4d7a',1.2);
 toast(d.nm+' trottet brav hinter dir her. '+(ANT[d.t].zoo?'Ab zum Tierpark im Grachtenviertel':'Ab zum Landgut Hopfenhof')+'. Oder ein Lokal nimmt '+d.nm+' als Maskottchen.');
}
function aniGive(w){
 const d=aniLead();if(!d)return{ok:false,msg:'Du hast kein Tier an der Leine.'};
 const A=ANT[d.t];
 if(w==='zoo'){
  if(!A.zoo)return{ok:false,msg:'Frieda lacht: "'+A.e.charAt(0).toUpperCase()+A.e.slice(1)+' '+A.n+'? Das gehört aufs Landgut Hopfenhof!"'};
  G.zoo=G.zoo||{};G.zoo[d.t]=(G.zoo[d.t]||0)+1;popAdd(3);xpAdd(15);
  const r=rnd(50,80);G.cash+=r;G.stats.earned+=r;G.hero=(G.hero||0)+1;addHeroE(20);aniRemove(d);sfx('win');
  return{ok:true,msg:d.nm+' ist wieder im Gehege! Frieda strahlt: Finderlohn '+eur(r)+' und +1 Heldenpunkt. Im Tierpark kannst du '+d.nm+' besuchen.'};
 }
 if(w==='land'){
  if(A.zoo)return{ok:false,msg:'Der Bauer kratzt sich am Kopf: "'+A.e.charAt(0).toUpperCase()+A.e.slice(1)+' '+A.n+'? Bring das lieber in den Tierpark."'};
  G.farm=(G.farm||0)+1;popAdd(2);xpAdd(10);const r=rnd(35,55);G.cash+=r;G.stats.earned+=r;G.hero=(G.hero||0)+.5;aniRemove(d);sfx('win');
  return{ok:true,msg:d.nm+' ist zurück im Stall. Der Bauer gibt dir '+eur(r)+' und erzählt, wie '+d.nm+' schon dreimal ausgebüxt ist.'};
 }
 if(w.indexOf('masc:')===0){
  const k=w.slice(5);G.masc=G.masc||{};
  if(MASCK.indexOf(k)<0)return{ok:false,msg:'Hier sucht niemand ein Maskottchen.'};
  if(G.masc[k])return{ok:false,msg:'Hier gibt es schon ein Maskottchen.'};
  G.masc[k]={t:d.t,nm:d.nm};popAdd(1);xpAdd(8);const r=70;G.cash+=r;G.stats.earned+=r;aniRemove(d);sfx('coin');
  return{ok:true,msg:DIST[k].n+' nimmt '+d.nm+' als Maskottchen für '+eur(r)+'. '+d.nm+' bekommt einen Schattenplatz, eine Wasserschale und ein Namensschild. Bestellungen von hier bringen jetzt 15 % mehr.'};
 }
 return{ok:false,msg:'Das geht hier nicht.'};
}
function aniPlaceBtns(k){
 const d=aniLead();let b='';
 if(G.masc&&G.masc[k]&&ANT[G.masc[k].t])b+='<div class="mu" style="margin:.3rem 0">Maskottchen: '+G.masc[k].nm+' ('+ANT[G.masc[k].t].n+') ♥ · Bestellungen von hier bringen 15 % mehr</div>';
 if(!d)return b;
 if(k==='land')b+=btn('In den Stall bringen: '+aniDesc(d),'aniGive','land',{cls:'m',note:ANT[d.t].zoo?'Ein Zootier gehört eigentlich in den Tierpark':'Finderlohn vom Bauern'});
 if(MASCK.indexOf(k)>=0&&!(G.masc&&G.masc[k]))b+=btn('Als Maskottchen verkaufen: '+aniDesc(d),'aniGive','masc:'+k,{cls:'m',note:'70 € · danach bringen Bestellungen von hier 15 % mehr'});
 return b;
}
function aniTrk(){
 const d=aniLead();if(!d)return '';
 return '<div class="b"><b>'+aniDesc(d)+'</b> an der Leine · '+(ANT[d.t].zoo?'Tierpark im Grachtenviertel':'Landgut Hopfenhof')+' oder als Maskottchen ins Lokal</div>';
}
function aniMini(x,O,S,big){
 if(ZONE)return;
 ANI.forEach(d=>{x.fillStyle=d.fol?'#ffd23f':'#c9955a';x.beginPath();x.arc(O+d.x/TS*S,d.y/TS*S,big?4:3,0,6.283);x.fill();x.strokeStyle='#3a2a1a';x.lineWidth=1;x.stroke();});
 if(MKQ.zoo){x.fillStyle='#7ad35a';x.beginPath();x.arc(O+MKQ.zoo.x/TS*S,MKQ.zoo.y/TS*S,big?5:4,0,6.283);x.fill();}
}
function aE(x,y,rx,ry){ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,6.283);ctx.fill();}
function drawAni(d){
 const t=d.t,sw=Math.sin(d.walk||0)*1.8,hop=t==='kaenguru'?Math.abs(Math.sin((d.walk||0)*.6))*5:0;
 ctx.fillStyle='rgba(0,0,0,.24)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+5,t==='giraffe'?15:11,6,0,0,6.283);ctx.fill();
 ctx.save();ctx.translate(d.x,d.y-hop);ctx.rotate(d.a);
 const legs=(c,L)=>{ctx.fillStyle=c;L.forEach((q,i)=>{circle(q[0]+(i%2?sw:-sw),q[1],1.8);});};
 if(t==='zebra'){
  legs('#222',[[-7,-5],[-7,5],[6,-5],[6,5]]);
  ctx.strokeStyle='#222';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(-10,0);ctx.lineTo(-15,Math.sin(timeNow*5)*2);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#f6f6f6';aE(0,0,11,6);aE(12,0,5,3);
  ctx.save();ctx.beginPath();ctx.ellipse(0,0,11,6,0,0,6.283);ctx.ellipse(12,0,5,3,0,0,6.283);ctx.clip();ctx.fillStyle='#1a1a1a';for(let i=-10;i<=17;i+=3.2)ctx.fillRect(i,-7,1.4,14);ctx.restore();
  ctx.fillStyle='#1a1a1a';ctx.fillRect(5,-.8,9,1.6);circle(16.6,0,1.8);ctx.fillStyle='#f6f6f6';aE(11,-2.6,1.4,1);aE(11,2.6,1.4,1);
 }else if(t==='giraffe'){
  legs('#7a4a1a',[[-7,-5],[-7,5],[6,-5],[6,5]]);
  ctx.strokeStyle='#e8b04a';ctx.lineWidth=4.4;ctx.beginPath();ctx.moveTo(7,0);ctx.lineTo(21,0);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#e8b04a';aE(0,0,10,6);aE(23,0,4.2,2.8);
  ctx.fillStyle='#9a5a22';[[-5,-2],[0,2.5],[4,-2.4],[-3,3],[12,0],[17,0],[-7,1]].forEach(q=>circle(q[0],q[1],1.7));
  ctx.fillStyle='#5a3a1a';circle(21.6,-1.6,1);circle(21.6,1.6,1);circle(27,0,.9);
 }else if(t==='lama'){
  legs('#6a5a4a',[[-6,-4.5],[-6,4.5],[5,-4.5],[5,4.5]]);
  ctx.fillStyle='#efe3c8';[[-4,-2],[-4,2],[0,-3],[0,3],[3,0],[-1,0]].forEach(q=>circle(q[0],q[1],3.6));
  ctx.fillStyle='#d64545';ctx.fillRect(-3,-4,5,8);ctx.fillStyle='#ffd23f';ctx.fillRect(-3,-4,5,1.2);ctx.fillRect(-3,2.8,5,1.2);
  ctx.strokeStyle='#efe3c8';ctx.lineWidth=3.6;ctx.beginPath();ctx.moveTo(4,0);ctx.lineTo(11,0);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#efe3c8';aE(13,0,3.6,2.6);ctx.fillStyle='#d8c8a8';aE(11.6,-2.6,1.2,1.8);aE(11.6,2.6,1.2,1.8);ctx.fillStyle='#3a2a1a';circle(16.2,0,.8);
 }else if(t==='kaenguru'){
  ctx.strokeStyle='#9a6a3a';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(-6,0);ctx.quadraticCurveTo(-13,0,-18,Math.sin(timeNow*3)*1.5);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#8a5a2a';aE(-3,-4.4,3.4,1.8);aE(-3,4.4,3.4,1.8);
  ctx.fillStyle='#b07a4a';aE(0,0,8,5);ctx.fillStyle='#d8b088';aE(2,0,3.6,3);
  ctx.fillStyle='#b07a4a';circle(9,0,3.4);aE(7.6,-2.8,2,1.1);aE(7.6,2.8,2,1.1);ctx.fillStyle='#3a2a1a';circle(12,0,.9);
 }else if(t==='pinguin'){
  ctx.fillStyle='#ff9a3c';aE(-5,-2.2,1.6,1.2);aE(-5,2.2,1.6,1.2);
  ctx.fillStyle='#1b1d22';aE(0,0,6,5);aE(0,-5.4+sw*.3,2,1.2);aE(0,5.4-sw*.3,2,1.2);
  ctx.fillStyle='#f4f4f4';aE(1.4,0,3.8,3.6);
  ctx.fillStyle='#1b1d22';circle(5,0,3);ctx.fillStyle='#ffb347';ctx.beginPath();ctx.moveTo(7.4,-1.1);ctx.lineTo(10.6,0);ctx.lineTo(7.4,1.1);ctx.closePath();ctx.fill();
 }else if(t==='flamingo'){
  ctx.fillStyle='#ff8fb3';aE(0,0,7,4.6);ctx.fillStyle='#ff6f9d';aE(-1,0,4.4,3.2);ctx.fillStyle='#3a2a2a';aE(-6.6,0,1.4,2.4);
  ctx.strokeStyle='#ff8fb3';ctx.lineWidth=2.2;ctx.beginPath();ctx.moveTo(5,0);ctx.quadraticCurveTo(10,-5,13,0);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#ff8fb3';circle(13.6,0,2.4);ctx.strokeStyle='#2a2a2a';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(15.4,0);ctx.lineTo(17.6,1.8);ctx.stroke();ctx.lineWidth=1;
 }else if(t==='schwein'){
  legs('#d8899a',[[-6,-5],[-6,5],[5,-5],[5,5]]);
  ctx.strokeStyle='#e58aa0';ctx.lineWidth=1.2;ctx.beginPath();ctx.arc(-11.5,0,1.8,0,5);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#f3a6b8';aE(0,0,10,7);ctx.fillStyle='#e58aa0';circle(10.4,0,3);ctx.fillStyle='#b8607a';circle(11.4,-1,.7);circle(11.4,1,.7);
  ctx.fillStyle='#e58aa0';ctx.beginPath();ctx.moveTo(6,-4);ctx.lineTo(9,-6.5);ctx.lineTo(8,-2.6);ctx.fill();ctx.beginPath();ctx.moveTo(6,4);ctx.lineTo(9,6.5);ctx.lineTo(8,2.6);ctx.fill();
 }else if(t==='ziege'){
  legs('#6a6a6a',[[-6,-4.5],[-6,4.5],[5,-4.5],[5,4.5]]);
  ctx.fillStyle='#e8e2d6';aE(0,0,9,5.4);aE(10,0,4,2.8);
  ctx.strokeStyle='#6a5a3a';ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(8.6,-1.8);ctx.lineTo(5,-4.4);ctx.moveTo(8.6,1.8);ctx.lineTo(5,4.4);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#bfb6a6';aE(13.4,0,1.6,1.2);ctx.fillStyle='#3a2a1a';circle(10.6,-1.2,.6);circle(10.6,1.2,.6);
 }else if(t==='schaf'){
  legs('#2a2a2a',[[-6,-4.5],[-6,4.5],[5,-4.5],[5,4.5]]);
  ctx.fillStyle='#f6f4ee';[[-5,-3],[-5,3],[0,-4],[0,4],[4,-2.6],[4,2.6],[-1,0],[-7,0]].forEach(q=>circle(q[0],q[1],3.8));
  ctx.fillStyle='#2a2a2a';aE(9.4,0,3.6,2.8);aE(8,-3.2,1.6,.9);aE(8,3.2,1.6,.9);
 }
 ctx.restore();
}
function drawAnimals(cx,cy){
 const iv=(x,y)=>x>cx-60&&x<cx+VW+60&&y>cy-60&&y<cy+VH+60;
 const lead=aniLead();
 if(lead&&iv(lead.x,lead.y)){ctx.strokeStyle='#c0392b';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(P.x,P.y);ctx.quadraticCurveTo((P.x+lead.x)/2,(P.y+lead.y)/2+10,lead.x+Math.cos(lead.a)*8,lead.y+Math.sin(lead.a)*8);ctx.stroke();ctx.lineWidth=1;}
 mascList().forEach(o=>{
  if(!iv(o.x,o.y))return;
  ctx.fillStyle='#5aa0d8';circle(o.x+14,o.y+8,4);ctx.fillStyle='#8fd0ff';circle(o.x+14,o.y+8,2.6);
  o.a=Math.PI/2+Math.sin(o.walk)*.3;drawAni(o);
 });
 aniList().forEach(d=>{if(iv(d.x,d.y))drawAni(d);});
 let nb=null,nd=80;aniList().concat(mascList()).forEach(d=>{const q=Math.hypot(d.x-P.x,d.y-P.y);if(q<nd||d.fol&&!nb){nd=q;nb=d;}});
 if(nb&&iv(nb.x,nb.y)){ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';const s=aniDesc(nb);ctx.strokeText(s,nb.x,nb.y-20);ctx.fillStyle='#fff';ctx.fillText(s,nb.x,nb.y-20);ctx.lineWidth=1;ctx.textAlign='start';}
}
const XNPC={druid:{n:'Druidin Brennnessel'},gal:{n:'Gallier'},zent:{n:'Zenturio Paragraphus'},rom:{n:'Legionär'},roem:{n:'Legionär Gähnus'},pfleg:{n:'Tierpflegerin Frieda'},kraut:{n:'Zauberkraut'}};
const GALV=[
 {n:'Korbflechterin Weidenzopf',dress:'#7a9a3a',hair:'#b5652a',len:6,item:'korb'},
 {n:'Käsemacherin Molke',dress:'#d8c07a',hair:'#6a4a2a',len:5,apron:'#f4f0e0',item:'kaese'},
 {n:'Holzfäller Eichenarm',dress:'#8a3a2a',hair:'#3a2a1a',beard:'#3a2a1a',item:'holz'},
 {n:'Imkerin Summsi',dress:'#e0b030',hair:'#e8d080',len:4,item:'honig'},
 {n:'Schäfer Wollbert',dress:'#5a6a8a',hair:'#9a8a6a',beard:'#c8c8c8',item:'stab'}
];
const GALS=[
 ['Körbe! Frisch geflochten!','Weide biegt sich, ich nicht.','Wer braucht noch einen Korb für Kräuter?'],
 ['Käse! Er riecht, also lebt er.','Der hier ist drei Monde alt.','Probieren ist gratis, Nasezuhalten auch.'],
 ['Holz! Holz! Holz!','Einen Baum fällen, zwei pflanzen. So geht das.','Ich hab heute schon zwölf Holzscheite gezählt.'],
 ['Summ, summ, summ!','Meine Bienen sind fleißiger als jede Legion.','Honig macht alles besser.'],
 ['Määäh! Äh, das war ein Schaf.','Eins, zwei, drei ... wo ist Flöckchen?','Schafe zählen ist mein Beruf, nicht mein Hobby.']
];
function xnName(d){return d.k==='gal'?GALV[d.v].n:XNPC[d.k].n;}
function xnPrompt(d){return d.k==='kraut'?'OK: Zauberkraut pflücken':d.k==='rom'?'OK: Legionär ansprechen':'OK: '+xnName(d)+' ansprechen';}
let xnTF=-1,xnTD=null;
function xnNearest(){if(xnTF===timeNow)return xnTD;xnTF=timeNow;let b=null,bd=110;skl().forEach(q=>{if(!XNPC[q.k]||q.k==='rom')return;const dd=Math.hypot(q.x-P.x,q.y-P.y);if(dd<bd){bd=dd;b=q;}});xnTD=b;return b;}
function xnTag(d,off){if(xnNearest()!==d)return;const n=xnName(d);ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-off);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-off);ctx.lineWidth=1;ctx.textAlign='start';}
function xnHand(d,c,fn){const x=d.x+Math.cos(d.a+1.2)*9,y=d.y+Math.sin(d.a+1.2)*9;ctx.fillStyle=c;fn(x,y);}
function romFig(d,cent){
 fig(d.x,d.y,d.a,{dress:'#b8302a',cape:cent?'#7a1a1a':null,hair:'#3a2a1a',hat:'#a9b2bb',hat2:'#d0d6dc',brim:4.4,sk:cent?5.2:4.8,walk:d.walk});
 ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);
 ctx.fillStyle='#d63a3a';if(cent)aE(-.6,0,1.8,6.6);else aE(-.6,0,5.2,1.5);
 if(!cent){ctx.fillStyle='#a8231f';ctx.fillRect(-4.5,5.6,9,3.4);ctx.fillStyle='#e8c040';ctx.fillRect(-4.5,5.6,9,.8);ctx.fillRect(-4.5,8.2,9,.8);circle(0,7.3,1.1);}
 else{ctx.strokeStyle='#7a5a32';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(2,-6);ctx.lineTo(9,-8);ctx.stroke();ctx.lineWidth=1;}
 ctx.restore();
}
function xnDraw(d){
 const k=d.k;
 if(k==='kraut'){
  const g=.25+.15*Math.sin(timeNow*3+d.x);ctx.fillStyle='rgba(120,255,160,'+g+')';circle(d.x,d.y,12);
  ctx.fillStyle='#3f9a4f';for(let i=0;i<5;i++){const a=i/5*6.283+.3;ctx.beginPath();ctx.ellipse(d.x+Math.cos(a)*4,d.y+Math.sin(a)*4,4.4,1.8,a,0,6.283);ctx.fill();}
  ctx.fillStyle='#f4f4ff';circle(d.x,d.y,1.6);circle(d.x+3,d.y-3,1.1);circle(d.x-3,d.y+2,1.1);
  return;
 }
 if(k==='druid'){
  fig(d.x,d.y,d.a,{dress:'#eef0e6',cape:'#2f6a3a',hair:'#c8c8d0',hairLen:6,sk:5.2,walk:d.walk});
  ctx.strokeStyle='#3f8a3a';ctx.lineWidth=2;ctx.beginPath();ctx.arc(d.x,d.y,4.8,0,6.283);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#f4f4ff';for(let i=0;i<5;i++){const a=i/5*6.283;circle(d.x+Math.cos(a)*4.8,d.y+Math.sin(a)*4.8,.9);}
  const sx=d.x+Math.cos(d.a-1.2)*10,sy=d.y+Math.sin(d.a-1.2)*10;ctx.strokeStyle='#7a5a32';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(sx,sy+6);ctx.lineTo(sx,sy-12);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#d8352f';ctx.beginPath();ctx.ellipse(sx,sy-13,4.4,3,0,Math.PI,0);ctx.fill();ctx.fillStyle='#fff';circle(sx-1.6,sy-14.4,.8);circle(sx+1.4,sy-15,.8);
  xnTag(d,26);return;
 }
 if(k==='gal'){
  const v=GALV[d.v];
  fig(d.x,d.y,d.a,{dress:v.dress,apron:v.apron,hair:v.hair,hairLen:v.len,beard:v.beard,sk:5,walk:d.walk});
  ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.strokeStyle='rgba(0,0,0,.22)';ctx.beginPath();ctx.moveTo(-3,-6);ctx.lineTo(-3,6);ctx.moveTo(1,-7);ctx.lineTo(1,7);ctx.moveTo(-5,-2.5);ctx.lineTo(4,-2.5);ctx.moveTo(-5,2.5);ctx.lineTo(4,2.5);ctx.stroke();ctx.restore();
  if(v.item==='korb')xnHand(d,'#a8783a',(x,y)=>{circle(x,y,3.8);ctx.fillStyle='#d8a85a';circle(x,y,2.2);});
  else if(v.item==='kaese')xnHand(d,'#f2c84a',(x,y)=>{ctx.beginPath();ctx.moveTo(x,y);ctx.arc(x,y,3.6,.6,6);ctx.closePath();ctx.fill();});
  else if(v.item==='holz')xnHand(d,'#7a5230',(x,y)=>{ctx.fillRect(x-5,y-1.8,10,3.6);ctx.fillStyle='#c8a070';circle(x+5,y,1.8);});
  else if(v.item==='honig')xnHand(d,'#e8a020',(x,y)=>{circle(x,y,3);ctx.fillStyle='#8a5a2a';ctx.fillRect(x-2.4,y-3.4,4.8,1.6);});
  else if(v.item==='stab'){const x=d.x+Math.cos(d.a+1.2)*9,y=d.y+Math.sin(d.a+1.2)*9;ctx.strokeStyle='#7a5a32';ctx.lineWidth=1.8;ctx.beginPath();ctx.moveTo(x,y+6);ctx.lineTo(x,y-10);ctx.arc(x+2.6,y-10,2.6,Math.PI,0);ctx.stroke();ctx.lineWidth=1;}
  xnTag(d,24);return;
 }
 if(k==='zent'){romFig(d,true);xnTag(d,26);return;}
 if(k==='roem'){romFig(d,false);xnTag(d,24);return;}
 if(k==='rom'){
  if(d.down>0){
   ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+3,14,6,d.a+1.57,0,6.283);ctx.fill();
   ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a+1.57);
   ctx.fillStyle='#f0d2b4';aE(-11,-2,2,1.4);aE(-11,2,2,1.4);
   ctx.fillStyle='#b8302a';aE(0,0,10,4.6);ctx.fillStyle='#a8231f';ctx.fillRect(-4,-4,9,8);ctx.fillStyle='#e8c040';circle(.5,0,1.3);
   ctx.fillStyle='#f0d2b4';circle(11,0,3.4);ctx.fillStyle='#a9b2bb';circle(12,0,3.8);ctx.fillStyle='#d63a3a';aE(12,0,1.4,4.4);
   ctx.restore();
   for(let i=0;i<3;i++){const a=timeNow*4+i*2.09;ctx.fillStyle='#ffd23f';circle(d.x+Math.cos(a)*8,d.y-14+Math.sin(a)*2.6,1.5);}
   return;
  }
  romFig(d,false);return;
 }
 if(k==='pfleg'){
  fig(d.x,d.y,d.a,{dress:'#3f7a3a',hair:'#8a5a2a',hairLen:4,hat:'#c8b078',hat2:'#b09a60',brim:5.4,sk:5,walk:d.walk});
  xnHand(d,'#9aa3ad',(x,y)=>{circle(x,y,3.4);ctx.fillStyle='#c8e0f0';circle(x,y,2);});
  xnTag(d,26);return;
 }
}
const LEGW=[[31,23],[45,23],[45,27],[31,27]];
let LEGP=null;
function legAt(s){
 if(!LEGP){const pts=LEGW.map(q=>[q[0]*TS,q[1]*TS]);let L=0;const seg=[];for(let i=0;i<pts.length;i++){const a=pts[i],b=pts[(i+1)%pts.length],l=Math.hypot(b[0]-a[0],b[1]-a[1]);seg.push({a:a,b:b,l:l,s:L});L+=l;}LEGP={seg:seg,L:L};}
 s=((s%LEGP.L)+LEGP.L)%LEGP.L;
 for(const g of LEGP.seg){if(s<=g.s+g.l){const f=(s-g.s)/g.l;return{x:g.a[0]+(g.b[0]-g.a[0])*f,y:g.a[1]+(g.b[1]-g.a[1])*f,a:Math.atan2(g.b[1]-g.a[1],g.b[0]-g.a[0])};}}
 return{x:LEGP.seg[0].a[0],y:LEGP.seg[0].a[1],a:0};
}
function legSlot(s,row,col){const q=legAt(s-row*26),nx=-Math.sin(q.a),ny=Math.cos(q.a),o=col===0?-11:col===1?11:0;return{x:q.x+nx*o,y:q.y+ny*o,a:q.a};}
function xnNew(k,tx,ty,o){return Object.assign({k:k,x:tx*TS,y:ty*TS,hx:tx*TS,hy:ty*TS,a:rf(0,6.28),walk:0,steer:rf(1,3),say:rf(2,6),cd:0},o||{});}
function herbSpots(z){
 z.ska=z.ska.filter(d=>d.k!=='kraut');
 [[28,5],[29,9],[27,17],[29,25],[12,26],[36,25],[42,25],[18,27],[33,1.6],[2.6,14]].forEach(q=>{const f=freeSpot(q[0]*TS+16,q[1]*TS+16);z.ska.push({k:'kraut',x:f.x,y:f.y,a:0,walk:0});});
 z.herbDay=G?G.day:0;
}
function galSka(z){
 z.ska=[];
 z.ska.push(xnNew('druid',10.5,9.2,{fix:1,a:Math.PI/2}));
 [[8,8.6],[11.5,8.6],[19.5,8.6],[6.5,19.5],[22,26.3]].forEach((q,i)=>z.ska.push(xnNew('gal',q[0],q[1],{v:i,lr:i===4?80:110})));
 z.ska.push(xnNew('zent',36.5,17.5,{fix:1,a:Math.PI/2}));
 z.leg={s:0,hold:0,cd:0,said:0};
 for(let i=0;i<6;i++){const sl=legSlot(0,Math.floor(i/2),i%2);z.ska.push({k:'rom',row:Math.floor(i/2),col:i%2,x:sl.x,y:sl.y,a:sl.a,walk:0,down:0});}
 herbSpots(z);
 z.ani=[];[[20,26.6],[23.6,27],[25,26]].forEach((q,i)=>z.ani.push(aniNew(i===2?'ziege':'schaf',q[0]*TS,q[1]*TS,{hx:22*TS,hy:26.6*TS,lr:90})));
}
function zooSka(z){z.ska=[xnNew('pfleg',24,14.2,{lr:160})];}
function genGallien(z,H){
 const zs=H.zs,zf=H.zf,mk=H.mk,r=H.r;
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++)zs(x,y,GR);
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.85)zs(x,y,TR);}
 zf(30,22,16,2,SW);zf(30,26,16,2,SW);zf(30,22,2,6,SW);zf(44,22,2,6,SW);
 zf(14,4,2,21,SA);zf(4,12,22,2,SA);zf(14,24,2,3,SA);zf(26,12,4,2,SA);zf(28,12,2,10,SA);
 for(let x=3;x<=26;x++){zs(x,3,FN);zs(x,24,FN);}for(let y=3;y<=24;y++){zs(3,y,FN);zs(26,y,FN);}
 zs(14,24,SA);zs(15,24,SA);zs(26,12,SA);zs(26,13,SA);
 z.huts=[[5,4],[10,4],[18,4],[22,8],[5,16],[19,17],[9,20],[21,20]];
 z.huts.forEach(h=>zf(h[0],h[1],3,3,BL));
 z.dhut=[5,8];zf(5,8,3,3,BL);
 {const m=mk('kessel','sk',9,10,'Zauberkessel','Zum Zauberkessel');m.sk='kessel';m.col='#5ff0a0';}
 for(let x=31;x<=45;x++){zs(x,3,FN);zs(x,19,FN);}for(let y=3;y<=19;y++){zs(31,y,FN);zs(45,y,FN);}
 zs(37,19,SW);zs(38,19,SW);zf(37,15,2,4,SW);zf(37,20,2,2,SW);
 z.tents=[[33,5],[36,5],[39,5],[42,5],[33,9],[42,9]];
 z.tents.forEach(t=>zf(t[0],t[1],2,2,BL));
 zf(39,12,5,3,BL);z.BLD.push({x:39,y:12,w:5,h:3,c:'#b8865a',n:'LAGER-AMT',k:'house',hh:7});
}
function genZoo(z,H){
 const zs=H.zs,zf=H.zf,r=H.r;
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++)zs(x,y,SW);
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.85)zs(x,y,TR);}
 z.pens=[];
 [[4,3,'zebra'],[18,3,'giraffe'],[32,3,'lama'],[4,17,'kaenguru'],[18,17,'pinguin'],[32,17,'flamingo']].forEach(q=>{
  const x=q[0],y=q[1],w=11,h=9,k=q[2];
  zf(x+1,y+1,w-2,h-2,k==='kaenguru'||k==='pinguin'?SA:GR);
  if(k==='pinguin'){zf(x+3,y+2,5,4,SH);zf(x+4,y+3,3,2,DP);}
  if(k==='flamingo'){zf(x+4,y+3,4,3,SH);}
  for(let i=x;i<x+w;i++){zs(i,y,FN);zs(i,y+h-1,FN);}for(let j=y;j<y+h;j++){zs(x,j,FN);zs(x+w-1,j,FN);}
  z.pens.push({k:k,x0:(x+1)*TS,y0:(y+1)*TS,x1:(x+w-1)*TS,y1:(y+h-1)*TS,sx:(x+w/2)*TS,sy:(q[1]<10?(y+h)*TS+4:y*TS-4),top:q[1]<10});
 });
 z.nogo={x0:0,y0:0,x1:ZW*TS,y1:ZH*TS,n:'der Tierpark'};
}
function fenceZG(c,nm,px,py,g,x,y){
 const l=g(x-1,y)===FN,rr=g(x+1,y)===FN,u=g(x,y-1)===FN,d=g(x,y+1)===FN;
 if(nm==='zoo'){
  c.fillStyle='rgba(0,0,0,.22)';if(l||rr)c.fillRect(px-16,py+3,32,5);if(u||d)c.fillRect(px+1,py-16,5,32);
  c.fillStyle='#9a6a3a';if(l||rr){c.fillRect(px-16,py-5,32,3);c.fillRect(px-16,py+1,32,3);}if(u||d){c.fillRect(px-5,py-16,3,32);c.fillRect(px+1,py-16,3,32);}
  c.fillStyle='#6a4520';c.fillRect(px-3,py-3,6,6);
 }else{
  const st=(a,b)=>{c.fillStyle='rgba(0,0,0,.25)';c.beginPath();c.arc(a+2,b+2,5.6,0,6.283);c.fill();c.fillStyle='#7a5230';c.beginPath();c.arc(a,b,5.6,0,6.283);c.fill();c.fillStyle='#b08050';c.beginPath();c.arc(a,b,3.6,0,6.283);c.fill();c.fillStyle='#8a6038';c.beginPath();c.arc(a,b,1.4,0,6.283);c.fill();};
  if(l||rr||!(u||d)){st(px-10,py);st(px,py);st(px+10,py);}
  if(u||d){st(px,py-10);st(px,py+10);if(!(l||rr))st(px,py);}
 }
}
function zgStatic(c,z){
 const T2=TS;
 if(z.name==='gallien'){
  const hut=(h,dr)=>{const x=(h[0]+1.5)*T2,y=(h[1]+1.5)*T2;
   c.fillStyle='rgba(0,0,0,.3)';c.beginPath();c.ellipse(x+5,y+7,T2*1.5,T2*1.25,0,0,6.283);c.fill();
   c.fillStyle='#d9c9a0';c.beginPath();c.arc(x,y,T2*1.48,0,6.283);c.fill();
   c.fillStyle='#4a3020';c.fillRect(x-7,y+T2*1.1,14,T2*.42);
   c.fillStyle='#c9a04a';c.beginPath();c.arc(x,y-3,T2*1.36,0,6.283);c.fill();
   c.strokeStyle='#a8802e';c.lineWidth=2;for(let r=10;r<T2*1.36;r+=9){c.beginPath();c.arc(x,y-3,r,0,6.283);c.stroke();}
   c.strokeStyle='rgba(120,80,30,.45)';c.lineWidth=1;for(let i=0;i<20;i++){const a=i/20*6.283;c.beginPath();c.moveTo(x+Math.cos(a)*8,y-3+Math.sin(a)*8);c.lineTo(x+Math.cos(a)*T2*1.32,y-3+Math.sin(a)*T2*1.32);c.stroke();}
   c.fillStyle=dr?'#3f8a3a':'#8a6030';c.beginPath();c.arc(x,y-3,7,0,6.283);c.fill();
   if(dr){c.fillStyle='#f4f4ff';[[0,-6],[5,-1],[-5,-1],[3,3],[-3,3]].forEach(q=>{c.beginPath();c.arc(x+q[0],y-3+q[1],1.3,0,6.283);c.fill();});}
  };
  z.huts.forEach(h=>hut(h,false));hut(z.dhut,true);
  z.tents.forEach(t=>{const x=t[0]*T2+3,y=t[1]*T2+3,w=2*T2-6,h=2*T2-6;
   c.fillStyle='rgba(0,0,0,.28)';c.fillRect(x+4,y+5,w,h);
   c.fillStyle='#d8c098';c.fillRect(x,y,w/2,h);c.fillStyle='#b89a6a';c.fillRect(x+w/2,y,w/2,h);
   c.strokeStyle='#7a5a32';c.lineWidth=2;c.beginPath();c.moveTo(x+w/2,y);c.lineTo(x+w/2,y+h);c.stroke();c.lineWidth=1;
   c.fillStyle='#a8231f';c.fillRect(x,y+h-4,w,4);});
  const board=(x,y,t,col)=>{c.fillStyle='#5a3a1f';c.fillRect(x-2,y,4,16);c.fillStyle='#e8d8b0';c.fillRect(x-46,y-12,92,18);c.strokeStyle='#5a3a1f';c.lineWidth=2;c.strokeRect(x-46,y-12,92,18);c.lineWidth=1;c.fillStyle=col;c.font='bold 10px Arial';c.textAlign='center';c.textBaseline='middle';c.fillText(t,x,y-3);c.textAlign='start';};
  board(13*T2,25.6*T2,'GALLIERDORF','#2f6a3a');board(40.5*T2,20.6*T2,'RÖMERLAGER','#a8231f');board(37*T2,24.8*T2,'RÖMERSTRASSE','#5a5a6a');
 }else if(z.name==='zoo'){
  z.pens.forEach(p=>{
   const x=p.sx,y=p.sy;c.fillStyle='#5a3a1f';c.fillRect(x-2,p.top?y-2:y-12,4,14);
   c.fillStyle='#f4efe0';c.fillRect(x-40,y-9+(p.top?6:-6),80,16);c.strokeStyle='#2f6a3a';c.lineWidth=2;c.strokeRect(x-40,y-9+(p.top?6:-6),80,16);c.lineWidth=1;
   c.fillStyle='#2f6a3a';c.font='bold 9px Arial';c.textAlign='center';c.textBaseline='middle';c.fillText(ANT[p.k].n.toUpperCase(),x,y-1+(p.top?6:-6));c.textAlign='start';
  });
  [[10,14.2],[24,15.8],[38,14.2]].forEach(q=>{const x=q[0]*T2,y=q[1]*T2;c.fillStyle='rgba(0,0,0,.25)';c.fillRect(x-18,y+2,40,10);c.fillStyle='#8a5a2a';c.fillRect(x-20,y-4,40,4);c.fillRect(x-20,y+2,40,4);c.fillStyle='#5a3a1f';c.fillRect(x-18,y+6,3,5);c.fillRect(x+15,y+6,3,5);});
 }
}
function drawZG(cx,cy){
 const z=ZONE;if(!z)return;
 if(z.name==='gallien'){
  const m=z.MKS.find(q=>q.id==='kessel');
  if(m&&m.x>cx-60&&m.x<cx+VW+60&&m.y>cy-60&&m.y<cy+VH+60){
   const x=m.x,y=m.y-4;
   for(let i=0;i<3;i++){ctx.fillStyle=['#ff9a3c','#ffd23f','#e5504d'][i];ctx.beginPath();ctx.moveTo(x-12+i*8,y+14);ctx.lineTo(x-8+i*8,y+5-Math.sin(timeNow*9+i)*3);ctx.lineTo(x-4+i*8,y+14);ctx.closePath();ctx.fill();}
   ctx.fillStyle='#1b1d22';circle(x,y,15);ctx.fillStyle='#3fe08f';circle(x,y,11.5);
   for(let i=0;i<4;i++){const a=timeNow*1.3+i*1.6,r=(timeNow*7+i*3)%9;ctx.fillStyle='rgba(220,255,230,.75)';circle(x+Math.cos(a)*r*.8,y+Math.sin(a)*r*.6,1.6+((timeNow*3+i)%1)*1.4);}
   if(chance(.08))FX.push({x:x+rf(-6,6),y:y-10,vx:rf(-6,6),vy:rf(-26,-14),t:0,life:1.2,dot:'rgba(200,255,220,.5)',r:rf(2.5,4.5)});
  }
  const fx=35*TS,fy=11*TS;
  if(fx>cx-60&&fx<cx+VW+60&&fy>cy-80&&fy<cy+VH+40){
   ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(fx+2,fy-2,3,26);ctx.fillStyle='#7a5a32';ctx.fillRect(fx-1,fy-30,3,52);
   const wv=Math.sin(timeNow*3)*2;ctx.fillStyle='#a8231f';ctx.beginPath();ctx.moveTo(fx+2,fy-30);ctx.lineTo(fx+26,fy-30+wv);ctx.lineTo(fx+26,fy-12+wv);ctx.lineTo(fx+2,fy-12);ctx.closePath();ctx.fill();
   ctx.fillStyle='#e8c040';ctx.font='bold 7px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('SPQR',fx+14,fy-21+wv/2);ctx.textAlign='start';
  }
 }else if(z.name==='zoo'){
  const x=6*TS,y=12.6*TS;
  if(x>cx-120&&x<cx+VW+120&&y>cy-60&&y<cy+VH+60){
   const n=ZOOK.reduce((s,k)=>s+((G.zoo&&G.zoo[k])||0),0);
   ctx.fillStyle='#2f6a3a';ctx.fillRect(x-60,y-14,120,22);ctx.strokeStyle='#ffd23f';ctx.lineWidth=2;ctx.strokeRect(x-60,y-14,120,22);ctx.lineWidth=1;
   ctx.fillStyle='#fff';ctx.font='bold 8px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('TIERPARK RHEINHANFEN',x,y-7);ctx.fillStyle='#ffd23f';ctx.fillText('Zurückgebracht: '+n,x,y+2);ctx.textAlign='start';
  }
 }
}
function potTick(dt){
 if(P.fast>0){P.fast-=dt;if(Math.hypot(P.vx,P.vy)>40&&chance(dt*20))FX.push({x:P.x+rf(-5,5),y:P.y+rf(-3,6),vx:rf(-10,10),vy:rf(-10,5),t:0,life:.5,dot:pick(['#fff2b0','#9ff5c0']),r:1.8});if(P.fast<=0)toast('Der Flinktrank lässt nach. Du bist wieder normal schnell.');}
 if(P.big>0){P.big-=dt;if(chance(dt*.5)){const q=peds.find(p=>Math.hypot(p.x-P.x,p.y-P.y)<90);if(q)addFx(q.x,q.y-20,pick(['Wow, ein Riese!','Huch, bist du groß!','Wie ist das Wetter da oben?']),'#fff2b0',1.6);}if(P.big<=0)toast('Plopp! Du schrumpfst wieder auf Normalgröße.');}
 if(P.kich>0){P.kich-=dt;if(chance(dt*2.5)){const q=peds.filter(p=>!p.snow&&Math.hypot(p.x-P.x,p.y-P.y)<200);if(q.length){const p=pick(q);addFx(p.x,p.y-20,pick(['Hihi!','Haha!','Hohoho!','Kicher!']),'#ffd23f',1.2);if(p.st==='walk'){p.st='dance';p.stT=2;}}}if(P.kich<=0)toast('Das Kichern verfliegt. Alle wischen sich Lachtränen aus den Augen.');}
}
function galUpdate(dt){
 if(!G)return;
 potTick(dt);
 if(!ZONE||ZONE.name!=='gallien')P.march=0;
 if(!ZONE)return;
 const z=ZONE,L=skl();
 const say=(d,arr,col)=>{d.say=(d.say||0)-dt;if(d.say<=0){d.say=rf(6,11);if(Math.hypot(d.x-P.x,d.y-P.y)<320)addFx(d.x,d.y-28,pick(arr),col||'#fff2b0',1.8);}};
 if(z.name==='amt'){L.forEach(d=>{if(d.k==='roem')say(d,['Ich brauche nur einen Stempel ...','Seit Stunden. Oder Jahrhunderten.','Straße nach Rom: Antrag läuft.']);});return;}
 if(z.name==='zoo'){L.forEach(d=>{if(d.k==='pfleg'){leash(d,d.hx,d.hy,d.lr);steerStep(d,dt,20);say(d,['Fütterungszeit!','Wer hat das Lama gesehen?','Bitte nicht an die Scheibe klopfen. Wir haben keine Scheibe.'],'#d8ffd0');}});return;}
 if(z.name!=='gallien')return;
 if(z.herbDay!==G.day)herbSpots(z);
 L.forEach(d=>{
  if(d.k==='gal'){leash(d,d.hx,d.hy,d.lr||110);steerStep(d,dt,18);say(d,GALS[d.v]);}
  else if(d.k==='druid'){if(Math.hypot(P.x-d.x,P.y-d.y)<160)d.a=Math.atan2(P.y-d.y,P.x-d.x);say(d,['Blubb, blubb ... der Kessel ruft!','Drei Kräuter, ein Trank, kein Kater.','Hast du Zauberkräuter dabei?'],'#c8ffd8');if(chance(dt*2))FX.push({x:d.x+rf(-6,6),y:d.y-16,vx:rf(-8,8),vy:rf(-24,-10),t:0,life:.9,dot:pick(['#9ff5c0','#fff2b0']),r:1.5});}
  else if(d.k==='zent'){say(d,['Links! Zwo! Drei! Vier!','Formation halten!','Schild hoch, Kinn hoch, Laune hoch!'],'#ffd0c0');if(Math.hypot(P.x-d.x,P.y-d.y)<140)d.a=Math.atan2(P.y-d.y,P.x-d.x);}
 });
 const lg=z.leg,R=L.filter(d=>d.k==='rom'),anyDown=R.some(d=>d.down>0);
 lg.cd=Math.max(0,lg.cd-dt);
 if(!anyDown)lg.s+=dt*36;
 R.forEach(d=>{
  if(d.down>0){d.down-=dt;if(d.down<=0)addFx(d.x,d.y-20,pick(['Formation!','Mein Helm!','Weiter geht es!','Hat das jemand gesehen?']),'#ffd23f',1.4);return;}
  const sl=legSlot(lg.s,d.row,d.col);d.x+=(sl.x-d.x)*Math.min(1,dt*6);d.y+=(sl.y-d.y)*Math.min(1,dt*6);d.a=sl.a;if(!anyDown)d.walk+=dt*7;
 });
 if(!anyDown&&lg.cd<=0&&chance(dt*.35)){const d=R[0];if(d&&Math.hypot(d.x-P.x,d.y-P.y)<360)addFx(d.x,d.y-26,pick(['Links! Zwo! Drei! Vier!','Hepp! Hepp!','Römerstraße, Runde sieben!']),'#ffd0c0',1.4);}
 if(P.march>0){
  P.march-=dt;const sl=legSlot(lg.s,3,2);P.x=sl.x;P.y=sl.y;P.a=sl.a;P.vx=P.vy=0;P.walk+=dt*7;
  if(P.march<=0){mood(8,'+8 Marsch');G.hero=(G.hero||0)+.3;toast('Runde beendet. Zenturio Paragraphus nickt: "Gut marschiert, Bürger! Fast wie ein Römer."');}
  return;
 }
 if(lg.cd<=0)R.forEach(d=>{
  if(d.down>0)return;
  const dd=Math.hypot(d.x-P.x,d.y-P.y);
  if(P.big>0&&dd<28){
   const S=R.filter(q=>q.down<=0).sort((a,b)=>Math.hypot(a.x-d.x,a.y-d.y)-Math.hypot(b.x-d.x,b.y-d.y));
   S.forEach((q,i)=>{q.down=3+i*.18;addFx(q.x,q.y-18,pick(['Hoppla!','Huch!','Uiii!','Nicht schubsen!']),'#ffd23f',1.2);});
   lg.cd=6;shake=.35;sfx('bonk');mood(5,'+5 Domino');G.hero=(G.hero||0)+.2;
   toast(pick(['Du bist so riesig, dass die ganze Legion wie Dominosteine umkippt. Keiner tut sich weh, nur die Helme rollen.','Klonk, klonk, klonk! Die Formation liegt flach und zählt Sterne. Gleich marschieren sie weiter.']));
  }else if(P.big<=0&&dd<20){
   const a=Math.atan2(P.y-d.y,P.x-d.x);moveE(P,Math.cos(a)*90*dt,Math.sin(a)*90*dt,7);
   if(lg.cd<=0&&chance(dt*3)){lg.cd=3;addFx(d.x,d.y-22,pick(['Bitte Abstand zur Formation!','Platz da, Bürger!','Wir marschieren nach Vorschrift!']),'#ffd0c0',1.4);}
  }
 });
}
function druidMenu(){
 const h=G.herb||0;
 mdl('Druidin Brennnessel','"Willkommen im Gallierdorf! Bring mir Zauberkräuter, dann braue ich dir einen Trank. Drei Kräuter pro Trank, und keiner macht betrunken, versprochen." Kräuter dabei: '+h+'.',[
  ['Flinktrank brauen (3 Kräuter): schneller laufen','gx:br:flink',h<3],['Riesentrank brauen (3 Kräuter): riesengroß werden','gx:br:riese',h<3],['Kichertrank brauen (3 Kräuter): alle lachen','gx:br:kicher',h<3],
  ['Wo finde ich Zauberkräuter?','gx:dr:wo'],['Eine Weisheit hören','gx:dr:weis']]);
}
function galMenu(d){
 UI.gx=d;const v=GALV[d.v];
 const A=[['Korb flechten helfen','Dir was erzählen lassen'],['Käse probieren','Dir was erzählen lassen'],['Wettsägen','Dir was erzählen lassen'],['Honig naschen','Dir was erzählen lassen'],['Schafe zählen helfen','Dir was erzählen lassen']][d.v];
 const T0=['„Ich flechte Körbe für das ganze Dorf. Für Kräuter, für Käse und für Leute, die gern Körbe tragen.“','„Mein Käse ist berühmt. Man riecht ihn bis ins Römerlager. Die halten deshalb immer Abstand.“','„Ich mache Holz. Für Hütten, für Feuer und für den Kessel der Druidin.“','„Meine Bienen sammeln Honig, ich sammle Bienenstiche. Ist ein fairer Tausch.“','„Ich passe auf die Schafe auf. Und die Schafe auf mich, glaube ich.“'][d.v];
 mdl(v.n,T0,[[A[0],'gx:g'+d.v+':a'],[A[1],'gx:g'+d.v+':b']]);
}
function zentMenu(){mdl('Zenturio Paragraphus','„Halt! Wer da? Ach, ein Bürger. Bitte Abstand zur Formation, wir marschieren nach Vorschrift. Vorschrift 7, Absatz Links-Zwo-Drei-Vier.“',[['Eine Runde mitmarschieren','gx:ze:march',P.march>0],['Einen Antrag stellen','gx:ze:antrag'],['Nach dem Weg fragen','gx:ze:weg']]);}
function roemMenu(){mdl('Legionär Gähnus','„Ich stehe hier für einen Stempel an. Wir bauen eine Straße, und das Amt will dafür ein Formular für das Formular.“',[['Woher kommst du?','gx:ro:her'],['Wie lange wartest du schon?','gx:ro:lang'],['Soll ich dir den Platz freihalten?','gx:ro:platz']]);}
function pflegMenu(){mdl('Tierpflegerin Frieda','„Willkommen im Tierpark! Ein paar Tiere sind ausgebüxt. Wenn du welche in der Stadt findest: Leine dran und ab zum grünen Tor im Grachtenviertel!“',[['Beim Füttern helfen','gx:pf:feed'],['Wer ist noch ausgebüxt?','gx:pf:list'],['Tierpark-Wissen','gx:pf:fact']]);}
function zooMenu(){
 const d=aniLead(),n=ZOOK.reduce((s,k)=>s+((G.zoo&&G.zoo[k])||0),0);
 const ch=[];
 if(d)ch.push(['Abgeben: '+aniDesc(d),'zo:give']);
 ch.push(['Tierpark besuchen (Eintritt frei)','zo:visit'],['Wer ist ausgebüxt?','zo:list']);
 mdl('Tierpark Rheinhanfen','Tierpflegerin Frieda lehnt am grünen Tor: "'+(d?'Oh, wen hast du denn da? '+d.nm+'!':'Ein paar Tiere sind ausgebüxt. Leine dran und her damit!')+'" Schon zurückgebracht: '+n+'.',ch);
}
function aniListTxt(){const L=ANI.filter(q=>!q.fol);return L.length?'Gerade ausgebüxt: '+L.map(aniDesc).join(', ')+'. Auf der Karte sind sie braune Punkte.':'Gerade ist niemand ausgebüxt. Aber das ändert sich schnell!';}
function xnOpen(d){
 const k=d.k;
 if(k==='kraut'){
  if((G.herb||0)>=9){toast('Deine Taschen sind voller Kräuter (9). Erst etwas brauen lassen.');return;}
  G.herb=(G.herb||0)+1;const z=ZONE;if(z)z.ska=z.ska.filter(q=>q!==d);sfx('pick');addFx(d.x,d.y-14,'+1 Kraut','#9ff5c0',1.2);
  toast('Zauberkraut gepflückt ('+G.herb+'). Die Druidin braut aus drei Kräutern einen Trank.');return;
 }
 if(k==='druid'){druidMenu();return;}
 if(k==='gal'){galMenu(d);return;}
 if(k==='zent'){zentMenu();return;}
 if(k==='rom'){toast(pick(['„Nicht stören, wir marschieren! Links, zwo, drei, vier!“','„Ich darf während des Marschierens nicht reden. Das hier zählt nicht.“','„Hallo! Äh, ich meine: Formation!“']));return;}
 if(k==='roem'){roemMenu();return;}
 if(k==='pfleg'){pflegMenu();return;}
}
function trankBtns(){
 const t=G.tr||{};let b='';
 [['flink','Flinktrank'],['riese','Riesentrank'],['kicher','Kichertrank']].forEach(q=>{if(t[q[0]]>0)b+=btn(q[1]+' trinken ('+t[q[0]]+')','trank',q[0]);});
 const d=aniLead();if(d)b+=btn('Leine lösen: '+aniDesc(d),'aniFree');
 return b;
}
function drinkTrank(k){
 G.tr=G.tr||{};if(!(G.tr[k]>0))return;
 G.tr[k]--;sfx('magic');closeAll();
 if(k==='flink'){P.fast=45;toast('Der Flinktrank prickelt bis in die Zehen. 45 Sekunden lang bist du blitzschnell!');}
 else if(k==='riese'){P.big=40;toast('Der Riesentrank schmeckt nach Wald und Pfefferminz. Du wächst und wächst ... 40 Sekunden lang bist du riesig!');}
 else if(k==='kicher'){P.kich=30;mood(8,'+8 Kichern');toast('Der Kichertrank kitzelt im Bauch. Wer in deiner Nähe ist, muss mitlachen!');}
}
function skAct16(p){
 if(p.indexOf('gx:')!==0&&p.indexOf('zo:')!==0)return false;
 const a=p.split(':');
 if(a[0]==='zo'){
  if(a[1]==='give'){const r=aniGive('zoo');toast(r.msg);render2();}
  else if(a[1]==='list')toast(aniListTxt());
  else if(a[1]==='visit'){const m=MKQ.zoo;if(!ZONE&&m)G.ret={x:m.x,y:m.y+32};const d=aniLead();startFade('Frieda öffnet das grüne Tor. Es riecht nach Heu, Fisch und Abenteuer: Willkommen im Tierpark!'+(d?' '+d.nm+' wartet so lange draußen.':''),()=>enterZone('zoo'));}
  return true;
 }
 if(a[1]==='br'){
  const k=a[2];if((G.herb||0)<3){toast('Dafür brauchst du drei Zauberkräuter.');return true;}
  G.herb-=3;G.tr=G.tr||{};G.tr[k]=(G.tr[k]||0)+1;mood(4,'+4');sfx('magic');
  const nm={flink:'Flinktrank',riese:'Riesentrank',kicher:'Kichertrank'}[k];
  const m=ZONE&&ZONE.MKS.find(q=>q.id==='kessel');if(m)for(let i=0;i<14;i++)FX.push({x:m.x+rf(-10,10),y:m.y-8,vx:rf(-30,30),vy:rf(-60,-20),g:40,t:0,life:1.1,dot:pick(['#3fe08f','#9ff5c0','#fff2b0']),r:rf(1.5,3)});
  toast('Der Kessel blubbert grün, es riecht nach Wald und Pfefferminz. Du bekommst einen '+nm+'. Trinken kannst du ihn im Rucksack, wann du willst.');
  return true;
 }
 if(a[1]==='dr'){
  if(a[2]==='wo')toast('Zauberkräuter leuchten grün. Sie wachsen draußen vor der Palisade, am Waldrand und an der Römerstraße. Jeden Tag wachsen neue nach.');
  else{mood(3,'+3');toast('Brennnessel: „'+pick(['Ein Trank ist nur so gut wie die Laune dessen, der ihn trinkt.','Wer im Kreis marschiert, kommt nie zu spät, aber auch nie an.','Die Mistel wächst oben, die Weisheit unten. Bück dich ruhig mal.','Brennnesseln brennen nur die, die es eilig haben.'])+'“');}
  return true;
 }
 if(a[1].charAt(0)==='g'&&a[1].length===2){
  const v=+a[1].charAt(1),d=UI.gx;
  if(a[2]==='a'){
   if(v===0){mood(4,'+4');toast('Du flichtst mit. Dein Korb sieht aus wie ein Vogelnest nach einem Sturm. Weidenzopf nennt ihn „modern“.');}
   else if(v===1){mood(4,'+4');sfx('crunch');toast(pick(['Der Käse ist würzig, cremig und riecht nach drei Wochen Abenteuer. Lecker!','Du probierst den Ältesten. Er probiert dich zurück. Molke lacht.']));}
   else if(v===2){mood(4,'+4');toast(pick(['Ihr sägt um die Wette. Eichenarm gewinnt, aber du bekommst den Ehrenspan.','Schrrr, schrrr, schrrr! Gleichstand. Eichenarm schlägt dir auf die Schulter, du sinkst ein Stück in den Boden.']));}
   else if(v===3){if(d&&d.day===G.day){toast('Summsi lächelt: „Morgen gibt es wieder Honig. Die Bienen brauchen Pause.“');}else{if(d)d.day=G.day;G.herb=Math.min(9,(G.herb||0)+1);mood(5,'+5');sfx('crunch');toast('Waldhonig auf frischem Brot! Summsi schenkt dir einen Honigkräuterzweig: +1 Zauberkraut.');}}
   else if(v===4){mood(3,'+3');toast('Eins, zwei, drei ... bei elf schläfst du fast ein. Wollbert grinst: „Siehst du, deshalb mach ich das hauptberuflich.“');}
  }else{mood(2,'+2');toast(xnName(d||{k:'gal',v:v})+': „'+pick(GALS[v])+'“');}
  return true;
 }
 if(a[1]==='ze'){
  if(a[2]==='march'){P.march=22;closeAll();toast('Du reihst dich hinten ein. Links, zwo, drei, vier! Eine Runde auf der Römerstraße.');}
  else if(a[2]==='antrag'){mood(3,'+3');toast('Paragraphus reicht dir eine Wachstafel: „Antrag auf Erlaubnis, einen Antrag zu stellen.“ Er siegelt ihn zweimal, zur Sicherheit, und legt ihn dann ins Archiv. Das Archiv ist ein Eimer.');}
  else{mood(2,'+2');toast('„Alle Wege führen nach Rom, sagt man. Unserer führt im Kreis. Wir sind trotzdem immer pünktlich.“');}
  return true;
 }
 if(a[1]==='ro'){
  if(a[2]==='her'){mood(3,'+3');toast('„Aus dem Römerlager beim Gallierdorf. Europa-Karte, ganz im Westen. Dort braut eine Druidin Tränke. Wir halten Abstand, nach Vorschrift.“');}
  else if(a[2]==='lang'){mood(2,'+2');toast('„Seit Tag eins. Welches Jahr, weiß ich nicht mehr. Meine Sandalen sind inzwischen Hausschuhe.“');}
  else{mood(4,'+4');G.hero=(G.hero||0)+.3;toast('„Du würdest für mich warten? Bürger, du bist ein Held!“ Gähnus salutiert so zackig, dass sein Helmbusch wackelt.');}
  return true;
 }
 if(a[1]==='pf'){
  if(a[2]==='feed'){mood(5,'+5');sfx('aww');toast(pick(['Du wirfst den Pinguinen Fische zu. Einer fängt ihn mit einer Verbeugung.','Die Giraffe frisst dir Salat aus der Hand. Ihre Zunge ist blau und sehr lang.','Das Lama summt beim Kauen. Frieda sagt, das ist Lama für „Danke“.','Die Erdmännchen-Nachbarn schauen neidisch zu. Die Zebras schmatzen Heu.']));}
  else if(a[2]==='list')toast(aniListTxt());
  else{mood(2,'+2');toast(pick(['Zebras haben unter dem Fell dunkle Haut.','Flamingos werden rosa, weil sie kleine Krebse und Algen fressen.','Giraffen schlafen oft nur ein paar Minuten am Stück.','Kängurus können kaum rückwärts laufen.','Lamas summen, wenn sie zufrieden sind oder sich unterhalten.','Pinguine haben Knie, man sieht sie nur nicht.']));}
  return true;
 }
 return false;
}

GOODS.c_plant={n:'Plantagen-Gras',u:'Tütchen',base:16};
TRADE.push('c_plant');SELL.push('c_plant');WEED.push('c_plant');ILL.c_plant=1;
function popLike(){return clamp(.3+((G&&G.pop)||0)/250,.03,.75);}
function popAdd(v){if(!G)return;G.pop=clamp((G.pop===undefined?10:G.pop)+v,-100,100);}
function popWord(){const p=G.pop===undefined?10:G.pop;return p>=60?'Stadtliebling':p>=25?'beliebt':p>=-10?'bekannt':p>=-50?'unbeliebt':'total unbeliebt bei allen';}
function lvlNeed(l){return 100+(l-1)*60;}
function xpAdd(v){
 if(!G)return;G.xp=(G.xp||0)+v;G.lvl=G.lvl||1;
 let up=false;while(G.xp>=lvlNeed(G.lvl)){G.xp-=lvlNeed(G.lvl);G.lvl++;up=true;}
 if(up){sfx('win');const im=IMMO.find(q=>q.lv===G.lvl);toast('Stufe '+G.lvl+' erreicht!'+(im?' Beim Makler in Willis Kontor ist jetzt frei: '+im.n+'.':' Weiter so!'));}
}
const IMMO=[
 {k:'garten',z:'feldweg',n:'Schrebergarten am Feldweg',p:2000,i:25,lv:1,d:'Gartenhäuschen mit Gartenzwerg-Ehrengarde.'},
 {k:'strand',z:'strand',n:'Strandhaus',p:6000,i:70,lv:2,d:'Hängematte, Meerblick und Feriengäste.'},
 {k:'huette',z:'berge',n:'Berghütte',p:9000,i:100,lv:3,d:'Kamin, Kuckucksuhr und Glühwein für Wanderer.'},
 {k:'boot',z:'amsterdam',n:'Hausboot in Amsterdam',p:12000,i:130,lv:4,d:'Schaukelt sanft, Tulpen auf dem Dach.'},
 {k:'wein',z:'portugal',n:'Weinberg in Portugal',p:16000,i:170,lv:5,d:'Sonne, Reben und ein Esel namens Sancho.'},
 {k:'finca',z:'malle',n:'Finca auf Mallorca',p:22000,i:240,lv:6,d:'Pool, Palmen, Schlager aus der Ferne.'},
 {k:'alm',z:'oesterreich',n:'Alm in Österreich',p:28000,i:300,lv:7,d:'Kühe mit Glocken, Käse mit Löchern.'},
 {k:'dorf',z:'gallien',n:'Rundhütte im Gallierdorf',p:35000,i:380,lv:8,d:'Die Druidin ist deine Nachbarin.'},
 {k:'insel',z:'rhein',n:'Eigene Rheininsel',p:60000,i:650,lv:10,d:'Mit Leuchtturm und Hängebrücke.'},
 {k:'schloss',z:'bayern',n:'Märchenschloss in Bayern',p:120000,i:1300,lv:12,d:'Zu groß, zu weiß, zu schön. Genau richtig.'}
];
function ownCount(){return IMMO.filter(q=>G.own&&G.own[q.k]).length;}
function ownWorth(){return IMMO.reduce((s,q)=>s+((G.own&&G.own[q.k])?q.p*.8:0),0);}
function immoBuy(k){
 const q=IMMO.find(x=>x.k===k);if(!q)return{ok:false,msg:'Unbekannt.'};
 G.own=G.own||{};if(G.own[k])return{ok:false,msg:'Gehört dir schon.'};
 if((G.lvl||1)<q.lv)return{ok:false,msg:'Erst ab Stufe '+q.lv+'.'};
 if(G.cash<q.p)return{ok:false,msg:'Dafür fehlen dir '+eur(q.p-G.cash)+'.'};
 G.cash-=q.p;G.own[k]=G.day;popAdd(3);xpAdd(40);sfx('win');
 return{ok:true,msg:'Glückwunsch! '+q.n+' gehört jetzt dir. Jeden Morgen kommen +'+eur(q.i)+' rein. Schau vorbei: Dort steht dein Schild.'};
}
function dayHook(L){
 let inc=0;IMMO.forEach(q=>{if(G.own&&G.own[q.k])inc+=q.i;});
 if(inc>0){G.cash+=inc;G.stats.earned+=inc;L.push('Einnahmen aus deinen Landschaften: +'+eur(inc)+'.');}
 G.clean=clamp((G.clean===undefined?40:G.clean)-6,0,100);
 if(G.pop!==undefined)G.pop=G.pop*.97;
}
function immoDraw(cx,cy){
 const z=ZONE;if(!z||!G||!G.own)return;
 const q=IMMO.find(x=>x.z===z.name&&G.own[x.k]);if(!q)return;
 const x=z.spawn.x+70,y=z.spawn.y-46;
 if(x<cx-120||x>cx+VW+120||y<cy-80||y>cy+VH+60)return;
 ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(x-20,y-6,46,34);
 ctx.fillStyle='#f4e2b8';ctx.fillRect(x-22,y-10,44,30);ctx.fillStyle='#c0392b';ctx.beginPath();ctx.moveTo(x-26,y-10);ctx.lineTo(x,y-28);ctx.lineTo(x+26,y-10);ctx.closePath();ctx.fill();
 ctx.fillStyle='#6a4a2a';ctx.fillRect(x-5,y+6,10,14);ctx.fillStyle='#8fd0ff';ctx.fillRect(x-17,y-4,9,8);ctx.fillRect(x+8,y-4,9,8);
 const tx='GEHÖRT DIR: '+q.n.toUpperCase();ctx.font='bold 8px Arial';const hw=ctx.measureText(tx).width/2+8;
 ctx.fillStyle='#2f6a3a';ctx.fillRect(x-hw,y+24,hw*2,16);ctx.strokeStyle='#ffd23f';ctx.lineWidth=2;ctx.strokeRect(x-hw,y+24,hw*2,16);ctx.lineWidth=1;
 ctx.fillStyle='#ffd23f';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(tx,x,y+32);ctx.textAlign='start';
}
function immoScreen(){
 const lv=G.lvl||1;let b='';
 IMMO.forEach(q=>{
  const own=G.own&&G.own[q.k],lock=lv<q.lv,poor=G.cash<q.p;
  b+=btn((own?'✓ ':'')+q.n+(own?' (gehört dir)':': '+eur(q.p)),'immo',q.k,{off:!!(own||lock||poor),why:own?'Gehört dir schon.':lock?'Erst ab Stufe '+q.lv+'. Du bist auf Stufe '+lv+'.':'Dafür fehlen dir '+eur(q.p-G.cash)+'.',note:q.d+' · +'+eur(q.i)+' pro Tag'+(lock&&!own?' · ab Stufe '+q.lv:'')});
 });
 return{hint:'Pfeiltasten: wählen · OK: kaufen · Zurück: zu Willi',html:'<div class="place" style="max-width:46rem"><div class="hd"><h2>Makler Grundgut</h2><div class="mu">„Landschaft ist das neue Gold!“ Bargeld <b class="gr">'+eur(G.cash)+'</b> · Stufe <b class="am">'+lv+'</b> · Besitz '+ownCount()+' / '+IMMO.length+'</div></div>'+b+btn('Zurück','back',null,{def:1})+'</div>'};
}
let HIDES=null;
const HTN={tonne:'in der Mülltonne',karton:'im Pappkarton',container:'im Altkleider-Container',busch:'in der Hecke'};
const HTA={tonne:'in die Mülltonne',karton:'in den Pappkarton',container:'in den Altkleider-Container',busch:'in die Hecke'};
function hideGen(){
 HIDES=[];if(!CITY)return;
 const T0=CITY.T,W=CITY.MW,H0=CITY.MH,C=[];
 for(let y=2;y<H0-2;y++)for(let x=2;x<W-2;x++){
  const t=T0[y*W+x];
  if(t===SW&&T0[(y-1)*W+x]===BL&&T0[(y+1)*W+x]===SW)C.push([x,y,'s']);
  else if(t===GR&&T0[(y-1)*W+x]===TR)C.push([x,y,'g']);
 }
 const rr=zrng(4711);
 for(let i=C.length-1;i>0;i--){const j=Math.floor(rr()*(i+1));const t=C[i];C[i]=C[j];C[j]=t;}
 C.forEach(c=>{
  if(HIDES.length>=18)return;
  const x=c[0]*TS+16,y=c[1]*TS+(c[2]==='s'?8:12);
  if(HIDES.some(h=>Math.hypot(h.x-x,h.y-y)<420))return;
  if(inNoGo(x,y)||inYard(x,y))return;
  const t=c[2]==='g'?'busch':pick(['tonne','tonne','karton','container']);
  HIDES.push({x:x,y:y,t:t,burn:0});
 });
}
function nearHide(){
 if(ZONE||wanted<=0||P.inCar||P.ride||P.sit||P.hide)return null;
 if(!HIDES)hideGen();
 let b=null,bd=34;HIDES.forEach(h=>{const d=Math.hypot(h.x-P.x,h.y-P.y);if(d<bd){bd=d;b=h;}});return b;
}
function doHide(h){
 P.hide={h:h,t:0};P.x=h.x;P.y=h.y;P.vx=P.vy=0;keys.left=keys.right=keys.up=keys.down=0;
 chasers.forEach(u=>{u.sT=0;});
 sfx('pat');
 toast(h.burn>timeNow?'Du versteckst dich '+HTN[h.t]+'. Aber die Polizei kennt dieses Versteck schon ...':pick(['Rein '+HTA[h.t]+' und ganz still sein ...','Du machst dich ganz klein '+HTN[h.t]+'. Es riecht nach Bananenschale.','Psst! Du bist jetzt ein Teil der Stadtmöblierung.']));
}
function unhide(found){
 const h=P.hide&&P.hide.h;P.hide=null;if(!h)return;
 P.y=h.y+20;const f=freeSpot(P.x,P.y);P.x=f.x;P.y=f.y;
 h.burn=timeNow+120;
 if(found){addFx(h.x,h.y-20,'Kuckuck!','#6fa8ff',1.6);sfx('bonk');toast('Gefunden! Ein Polizist hebt den Deckel: „Kuckuck!“ Lauf!');escapeT=0;}
 else if(wanted>0)toast('Du kletterst raus. Die Polizei sucht noch, also leise!');
 else{mood(-1);toast(pick(['Du kletterst raus und schüttelst eine Bananenschale vom Kopf.','Frei! Du riechst ein bisschen nach Mülltonne, aber frei.']));}
}
function hideChase(dt){
 const h=P.hide.h;P.hide.t+=dt;bustT=0;
 let minD=1e9;const burn=h.burn>timeNow;
 for(const u of chasers){
  u.sT=(u.sT||0)-dt;
  if(u.sT<=0||u.sx===undefined||Math.hypot(u.sx-u.x,u.sy-u.y)<20){const a=rf(0,6.283),r=burn?rf(30,160):rf(140,420);u.sx=h.x+Math.cos(a)*r;u.sy=h.y+Math.sin(a)*r;u.sT=rf(3,6);}
  const car=u.kind==='car',sp=car?150:72,dx=u.sx-u.x,dy=u.sy-u.y,l=Math.hypot(dx,dy)||1;
  u.a=Math.atan2(dy,dx);moveE(u,dx/l*sp*dt,dy/l*sp*dt,car?12:7);
  const d=Math.hypot(u.x-h.x,u.y-h.y);minD=Math.min(minD,d);
  if(!car&&d<60&&chance(dt*(burn?.9:.2))){unhide(true);return;}
 }
 escapeT+=dt*(minD>220?1.5:.8);
 if(escapeT>7){h.burn=timeNow+120;endWanted(pick(['Die Polizei zieht ratlos ab. Du riechst nach Bananenschale, aber du bist frei.','Die Streife funkt: „Nichts gefunden außer einer Katze.“ Du bist frei!','Alles still. Die Polizei hat aufgegeben. Bleib noch kurz drin, nur zur Sicherheit.']));}
}
function hideDraw(cx,cy){
 if(ZONE)return;if(!HIDES)hideGen();
 HIDES.forEach(h=>{
  if(h.x<cx-40||h.x>cx+VW+40||h.y<cy-40||h.y>cy+VH+40)return;
  const me=P.hide&&P.hide.h===h,x=h.x,y=h.y;
  ctx.fillStyle='rgba(0,0,0,.28)';
  if(h.t==='busch'){ctx.beginPath();ctx.ellipse(x+3,y+6,18,9,0,0,6.283);ctx.fill();ctx.fillStyle='#2f7a3f';circle(x-7,y,10);circle(x+7,y,10);circle(x,y-5,11);ctx.fillStyle='#3f9a4f';circle(x-4,y-6,6);circle(x+6,y-3,5);}
  else if(h.t==='tonne'){ctx.fillRect(x-9,y-6,22,18);ctx.fillStyle='#2f5a3a';ctx.fillRect(x-11,y-9,22,18);ctx.fillStyle='#3f7a4a';ctx.fillRect(x-11,y-9,22,5);ctx.fillStyle='#1f3a26';ctx.fillRect(x-11,y-4,22,1.5);ctx.fillStyle='#222';circle(x-8,y+9,2);circle(x+8,y+9,2);}
  else if(h.t==='karton'){ctx.fillRect(x-9,y-7,22,18);ctx.fillStyle='#c49a5a';ctx.fillRect(x-11,y-10,22,18);ctx.fillStyle='#a8783a';ctx.fillRect(x-11,y-1.5,22,3);ctx.fillStyle='#e8d090';ctx.fillRect(x-2,y-10,4,18);ctx.fillStyle='#6a4a2a';ctx.font='bold 5px Arial';ctx.textAlign='center';ctx.fillText('ZERBRECHLICH',x,y+5);ctx.textAlign='start';}
  else{ctx.fillRect(x-13,y-9,30,22);ctx.fillStyle='#3a6ab0';ctx.fillRect(x-15,y-12,30,22);ctx.fillStyle='#2a4a80';ctx.fillRect(x-15,y-12,30,4);ctx.fillStyle='#f4f4f4';ctx.font='bold 5px Arial';ctx.textAlign='center';ctx.fillText('ALTKLEIDER',x,y+2);ctx.textAlign='start';}
  if(me){const bl=Math.floor(timeNow*1.5)%4===0;ctx.fillStyle='#fff';if(!bl){circle(x-3,y-8,1.8);circle(x+3,y-8,1.8);ctx.fillStyle='#222';circle(x-3,y-8,.9);circle(x+3,y-8,.9);}}
  else if(wanted>0&&Math.hypot(h.x-P.x,h.y-P.y)<220){ctx.strokeStyle='rgba(255,210,63,'+(.5+.4*Math.sin(timeNow*6))+')';ctx.lineWidth=2;ctx.beginPath();ctx.arc(x,y,20,0,6.283);ctx.stroke();ctx.lineWidth=1;}
 });
}
function hideMini(x,O,S,big){if(ZONE||wanted<=0)return;if(!HIDES)hideGen();x.fillStyle='#ffd23f';HIDES.forEach(h=>{x.fillRect(O+h.x/TS*S-1.5,h.y/TS*S-1.5,3,3);});}
function litterCap(){return Math.round(50-((G&&G.clean!==undefined)?G.clean:40)*.35);}
function pfandBtn(){
 const n=(G.ammo&&G.ammo.dose)||0;
 return btn('Pfandautomat: '+n+' Dosen abgeben','pfand',null,{off:n<1,why:'Sammel erst leere Dosen auf der Straße.',note:'25 Cent pro Dose · macht die Stadt sauber · Rheinhanfen sauber: '+Math.round(G.clean===undefined?40:G.clean)+' %'});
}
function fmtC(v){return v.toFixed(2).replace('.',',')+' €';}
function pfandGive(){
 const n=(G.ammo&&G.ammo.dose)||0;if(n<1){toast('Keine Dosen dabei. Auf der Straße liegen genug!');return;}
 G.ammo.dose=0;if(G.sel==='dose')G.sel='';
 const v=n*.25;G.cash=Math.round((G.cash+v)*100)/100;G.stats.earned+=v;
 const before=G.pfand||0;G.pfand=before+n;G.clean=clamp((G.clean===undefined?40:G.clean)+n*.9,0,100);popAdd(n*.15);xpAdd(n);sfx('coin');
 let bonus='';if(Math.floor(G.pfand/100)>Math.floor(before/100)){G.cash+=20;bonus=' Die Stadtreinigung verleiht dir die Goldene Greifzange: +20 € Bonus!';}
 toast('Klong, klong, klong! '+n+' Dosen im Pfandautomaten: +'+fmtC(v)+'. Insgesamt '+G.pfand+' Dosen, Rheinhanfen ist zu '+Math.round(G.clean)+' % sauber.'+bonus);
 render2();
}
const PLN=['Hanni','Nanni','Gustav','Grüni','Paula','Herbert','Wanda','Blattina','Knospe','Fritzi'];
function atHome(){return !ZONE&&MKQ.hq&&Math.hypot(P.x-MKQ.hq.x,P.y-MKQ.hq.y)<140;}
function plantNeeds(p){const L=[];if(p.st>=3)L.push('erntereif');if(p.w<25)L.push('durstig');if(p.f<20)L.push('hungrig');if(p.l<20)L.push('einsam');return L;}
function plantTick(dt){
 if(!G||!G.plants)return;
 G.plants.forEach(p=>{
  p.w=Math.max(0,p.w-dt*.55);p.f=Math.max(0,p.f-dt*.3);p.l=Math.max(0,p.l-dt*.4);
  if(p.st<3){
   const ok=p.w>10&&p.f>10,rate=ok?(.55+.45*p.l/100)*((p.w>40&&p.f>40)?1:.7):.04;
   p.g+=dt*rate/80;p.tt=(p.tt||0)+dt;p.care=(p.care||0)+dt*((p.w>30&&p.f>30?.6:0)+(p.l>50?.4:0));
   if(p.g>=1){p.g=0;p.st++;if(p.st===3)toast(p.nm+' ist erntereif! Ab nach Hause in den Imbiss.');else toast(p.nm+' wächst! Jetzt: '+PST[p.st]+'.');}
  }
  if(p.w<25&&!p.aw){p.aw=1;toast(p.nm+' hat Durst! Zu Hause im Imbiss gießen.');}
  if(p.w>=25)p.aw=0;
 });
}
const PST=['Keimling','Jungpflanze','Blüte','erntereif'];
function plantSVG(p){
 const face=!p?'':p.w<25?'thirsty':(p.f<20||p.l<20)?'sad':'happy';
 let s='<svg viewBox="0 0 110 130" width="100%" height="100%" style="max-height:9rem">';
 s+='<ellipse cx="55" cy="124" rx="34" ry="5" fill="rgba(0,0,0,.25)"/>';
 s+='<polygon points="25,86 85,86 78,122 32,122" fill="#c96a3a"/><rect x="21" y="80" width="68" height="9" rx="2" fill="#d97a48"/><rect x="24" y="80" width="62" height="4" fill="#5a3a22"/>';
 if(p){
  const drop=p.w<25,col=p.w<25?'#9aa64a':'#3f9a4f',col2=p.w<25?'#b8b860':'#57b862',h=[10,30,46,56][p.st];
  const leaf=(x,y,sc,rot)=>{let o='<g transform="translate('+x+' '+y+') rotate('+rot+') scale('+sc+')">';[-60,-30,0,30,60].forEach((a,i)=>{const L=i===2?15:i===1||i===3?12:8;o+='<ellipse cx="0" cy="'+(-L/2)+'" rx="2.2" ry="'+(L/2)+'" fill="'+(i%2?col2:col)+'" transform="rotate('+a+')"/>';});return o+'</g>';};
  s+='<line x1="55" y1="81" x2="55" y2="'+(81-h)+'" stroke="#4f8a3a" stroke-width="'+(2+p.st*.6)+'"/>';
  const droop=p.w<25?25:0;
  if(p.st===0){s+=leaf(52,78-h,.5,-40+droop)+leaf(58,78-h,.5,40-droop);}
  else{for(let k=0;k<=p.st;k++){const y=81-h*(.35+k*.22);s+=leaf(53,y,.7+k*.08,-55+droop)+leaf(57,y,.7+k*.08,55-droop);}s+=leaf(55,81-h,.8,0);}
  if(p.st>=2){[[55,81-h-4],[48,81-h*.62],[62,81-h*.62],[50,81-h*.84],[60,81-h*.84]].forEach(q=>{s+='<circle cx="'+q[0]+'" cy="'+q[1]+'" r="'+(p.st===3?3.4:2.2)+'" fill="'+(p.st===3?'#dff0b0':'#a8d878')+'"/>';if(p.st===3)s+='<circle cx="'+(q[0]+1)+'" cy="'+(q[1]-1)+'" r="1" fill="#fff"/>';});}
  s+='<circle cx="45" cy="100" r="3" fill="#fff"/><circle cx="65" cy="100" r="3" fill="#fff"/><circle cx="45" cy="'+(face==='sad'?101:100)+'" r="1.6" fill="#222"/><circle cx="65" cy="'+(face==='sad'?101:100)+'" r="1.6" fill="#222"/>';
  if(face==='happy')s+='<path d="M46 108 Q55 116 64 108" stroke="#222" stroke-width="2" fill="none"/><circle cx="38" cy="106" r="3" fill="#ff9ab0" opacity=".6"/><circle cx="72" cy="106" r="3" fill="#ff9ab0" opacity=".6"/>';
  else if(face==='sad')s+='<path d="M46 112 Q55 105 64 112" stroke="#222" stroke-width="2" fill="none"/>';
  else s+='<ellipse cx="55" cy="110" rx="3" ry="4" fill="#222"/>';
  if(drop)s+='<path d="M80 60 Q84 68 80 72 Q76 68 80 60Z" fill="#5ab0f0"/>';
  if(p.st===3)s+='<text x="55" y="16" font-size="11" text-anchor="middle" fill="#ffd23f" font-family="Arial" font-weight="bold">ERNTE!</text>';
 }else{s+='<ellipse cx="55" cy="84" rx="28" ry="3" fill="#3a2a1a"/><text x="55" y="60" font-size="9" text-anchor="middle" fill="#9aa3ad" font-family="Arial">leerer Topf</text>';}
 return s+'</svg>';
}
function growScreen(){
 const P0=G.plants=G.plants||[],home=atHome();
 let sel=UI.gs===undefined?0:UI.gs;if(sel>2)sel=0;UI.gs=sel;
 let cards='';
 for(let i=0;i<3;i++){
  const p=P0[i],bar=(v,c)=>'<div style="height:.35rem;background:#2a2f38;border-radius:.2rem;margin:.12rem 0"><div style="height:100%;width:'+Math.round(v)+'%;background:'+c+';border-radius:.2rem"></div></div>';
  cards+='<div class="f card" data-a="gsel" data-p="'+i+'" style="flex:1;min-width:0;text-align:center;'+(i===sel?'border-color:var(--am);':'')+'">'+plantSVG(p)+
   '<b>'+(p?p.nm:'Freier Platz')+'</b><div class="mu" style="font-size:.75rem">'+(p?PST[p.st]+(p.st<3?' · '+Math.round(p.g*100)+' %':''):'Samen pflanzen?')+'</div>'+
   (p?'<div style="font-size:.65rem;text-align:left">Wasser'+bar(p.w,'#5ab0f0')+'Dünger'+bar(p.f,'#c9a04a')+'Liebe'+bar(p.l,'#ff7aa8')+'</div>':'')+'</div>';
 }
 const p=P0[sel],why=home?'':'Pflegen geht nur zu Hause im Imbiss. Das hier ist die Pflanzen-Cam.';
 let b='';
 if(!p)b+=btn('Samen pflanzen: 5 €','gplant',null,{off:!home||G.cash<5||P0.length>=3,why:why||(G.cash<5?'Nicht genug Geld.':'Mehr als drei Pflanzen sind nicht erlaubt.'),def:1,note:'Erlaubt sind drei Pflanzen, nur für Erwachsene und nur für dich selbst'});
 else{
  if(p.st>=3)b+=btn('Ernten: '+p.nm,'gharv',null,{off:!home,why:why,def:1,cls:'b',note:'Wird zu Joints in deinem Vorrat, nur für dich selbst'});
  b+=btn('Gießen','gwater',null,{off:!home,why:why,def:p.st<3?1:0,note:'Wasser: '+Math.round(p.w)+' %'});
  b+=btn('Düngen: 2 €','gfood',null,{off:!home||G.cash<2,why:why||'Nicht genug Geld.',note:'Dünger: '+Math.round(p.f)+' %'});
  b+=btn('Vorsingen und plaudern','glove',null,{off:!home,why:why,note:'Liebe: '+Math.round(p.l)+' %. Glückliche Pflanzen wachsen schneller'});
 }
 b+=btn('Zurück','back',null,{def:b?0:1});
 return{hint:'Pfeiltasten: Pflanze wählen · OK: bestätigen · Zurück: schließen',html:'<div class="place" style="max-width:52rem"><div class="hd"><h2>Deine Pflanzen ('+P0.length+' / 3)</h2><div class="mu">'+(home?'Zu Hause im Hinterzimmer vom Imbiss.':'Pflanzen-Cam: nur anschauen.')+' Eigenanbau ist in Deutschland für Erwachsene erlaubt: drei Pflanzen, nur für dich selbst, nichts weiterverkaufen.</div></div><div style="display:flex;gap:.5rem;margin:.3rem 0">'+cards+'</div>'+b+'</div>'};
}
function growAct(a){
 const P0=G.plants=G.plants||[],i=UI.gs||0,p=P0[i];
 if(!atHome()){toast('Das geht nur zu Hause im Imbiss.');return;}
 if(a==='plant'){
  if(P0.length>=3){toast('Mehr als drei Pflanzen sind nicht erlaubt.');return;}
  if(G.cash<5){toast('Nicht genug Geld für Samen.');return;}
  G.cash-=5;const nm=pick(PLN.filter(n=>!P0.some(q=>q.nm===n)));P0.push({nm:nm,st:0,g:0,w:70,f:70,l:60,care:0,tt:0});UI.gs=P0.length-1;sfx('pick');
  toast('Du drückst einen Samen in die Erde. Das ist jetzt '+nm+'. Gieß, dünge und sing ihr was vor!');
 }else if(!p)return;
 else if(a==='water'){if(p.w>85){p.l=Math.max(0,p.l-8);toast(p.nm+' blubbert: „Nicht ertränken!“ Zu viel Wasser mag niemand.');}else{p.w=100;sfx('splash');toast(p.nm+' trinkt gierig und reckt die Blätter.');}}
 else if(a==='food'){if(G.cash<2){toast('Nicht genug Geld.');return;}G.cash-=2;p.f=100;toast(p.nm+' bekommt Dünger. Mjam!');}
 else if(a==='love'){p.l=Math.min(100,p.l+35);mood(2,'+2');sfx('musik');toast(pick(['Du singst '+p.nm+' ein Lied vor. Die Blätter wippen im Takt.','Du erzählst '+p.nm+' von deinem Tag. Sie hört geduldig zu, wie immer.','Du spielst '+p.nm+' Musik aus dem Handy vor. Sie dreht sich zum Lautsprecher.']));}
 else if(a==='harv'){
  if(p.st<3)return;
  const q=p.tt>0?p.care/p.tt:.5,n=Math.max(3,Math.round(3+q*7+(p.l>70?2:0)));
  G.stock.joint=Math.min(40,(G.stock.joint||0)+n);P0.splice(i,1);UI.gs=0;mood(6,'+6 Ernte');xpAdd(25);sfx('win');
  G.stats.ernte=(G.stats.ernte||0)+1;
  toast('Ernte! '+p.nm+' schenkt dir '+n+' Joints für deinen Vorrat'+(q>.7?'. Super gepflegt!':q>.4?'. Gut gemacht.':'. Mit mehr Pflege wird es mehr.')+' Der Topf ist wieder frei.');
 }
 render2();
}
function plantTrk(){
 if(!G||!G.plants||!G.plants.length)return '';
 const L=[];G.plants.forEach(p=>{const n=plantNeeds(p);if(n.length)L.push(p.nm+' '+n.join(', '));});
 return L.length?'<div class="b"><b>Pflanzen</b> · '+L.join(' · ')+'</div>':'';
}
const PZ={gate:[10,14],tunnel:[38,27],tin:[38.5,24.4],zaun:[38,22]};
const WACHW=[[[11.5,4.5],[22.5,4.5],[22.5,13.5],[11.5,13.5]],[[22.5,13.5],[33.5,13.5],[33.5,23.6],[22.5,23.6]],[[33.5,4.5],[43.5,4.5],[43.5,23.6],[33.5,23.6]]];
function genPlantage(z,H){
 const zs=H.zs,zf=H.zf,mk=H.mk,r=H.r;
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++)zs(x,y,GR);
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){if((x<2||x>ZW-3||y<2||y>ZH-3)&&r()<.85)zs(x,y,TR);}
 zf(2,14,8,2,SW);zf(2,26,44,2,SA);
 for(let x=10;x<=44;x++){zs(x,3,FN);zs(x,25,FN);}for(let y=3;y<=25;y++){zs(10,y,FN);zs(44,y,FN);}
 zf(11,4,33,21,SW);
 const field=(x0,y0,x1,y1)=>{zf(x0+1,y0+1,x1-x0-1,y1-y0-1,FD);for(let x=x0;x<=x1;x++){zs(x,y0,FN);zs(x,y1,FN);}for(let y=y0;y<=y1;y++){zs(x0,y,FN);zs(x1,y,FN);}};
 field(13,5,20,12);field(24,5,31,12);field(35,5,42,12);field(13,15,20,22);field(24,15,31,22);field(35,15,42,22);
 zf(2,22,2,3,GR);
 [[44,28],[46,24],[46,8],[5,4],[7,22]].forEach(q=>{if(q[0]<ZW&&q[1]<ZH)zs(q[0],q[1],TR);});
 for(let x=33;x<=43;x++){if(r()<.5)zs(x,28,TR);}
 if(G&&G.tunnel===2)zs(PZ.zaun[0],PZ.zaun[1],FD);
 {const m=mk('pfoertner','sk',8,13,'Pförtnerhaus','Zum Pförtner');m.sk='pfoertner';m.col='#ffb347';}
 {const m=mk('ausgang','sk',12,14,'Ausgang mit Taschenkontrolle','Zum Ausgang');m.sk='ausgang';m.col='#ffb347';}
 zf(5,10,3,3,BL);z.BLD.push({x:5,y:10,w:3,h:3,c:'#8a9aa8',n:'PFORTE',k:'house',hh:7});
}
function plantageSka(z){
 z.ska=[];
 WACHW.forEach((W,i)=>z.ska.push({k:'wache',i:i,s:rf(0,400),x:W[0][0]*TS,y:W[0][1]*TS,a:0,walk:0,al:0,say:rf(3,8)}));
 z.ska.push({k:'kamera',x:43.6*TS,y:13.5*TS,a0:Math.PI,sw:.7,a:Math.PI,al:0,r:160},{k:'kamera',x:33.6*TS,y:23.2*TS,a0:0,sw:.6,a:0,al:0,r:120},{k:'kamera',x:21.6*TS,y:4.4*TS,a0:Math.PI/2,sw:.8,a:Math.PI/2,al:0,r:150});
 z.ska.push({k:'loch',x:PZ.tunnel[0]*TS+16,y:PZ.tunnel[1]*TS+16,a:0,walk:0});
 z.ska.push({k:'tunnel2',x:PZ.tin[0]*TS,y:PZ.tin[1]*TS,a:0,walk:0});
 z.ska.push({k:'zaun',x:PZ.zaun[0]*TS+16,y:PZ.zaun[1]*TS+16,a:0,walk:0});
 [[37,19],[39.5,17],[40,20.4]].forEach(q=>z.ska.push({k:'beet',x:q[0]*TS+16,y:q[1]*TS+16,a:0,walk:0,left:1}));
}
function wachPos(W,s){
 const pts=W.map(q=>[q[0]*TS,q[1]*TS]);let L=0;const seg=[];for(let i=0;i<pts.length;i++){const a=pts[i],b=pts[(i+1)%pts.length],l=Math.hypot(b[0]-a[0],b[1]-a[1]);seg.push([a,b,l,L]);L+=l;}
 s=((s%L)+L)%L;for(const g of seg){if(s<=g[3]+g[2]){const f=(s-g[3])/g[2];return{x:g[0][0]+(g[1][0]-g[0][0])*f,y:g[0][1]+(g[1][1]-g[0][1])*f,a:Math.atan2(g[1][1]-g[0][1],g[1][0]-g[0][0])};}}
 return{x:pts[0][0],y:pts[0][1],a:0};
}
function inPlantFence(x,y){return x>10.9*TS&&x<44*TS&&y>3.9*TS&&y<25*TS;}
function inField(x,y){return tget(Math.floor(x/TS),Math.floor(y/TS))===FD;}
function sees(o,range,half){
 const dx=P.x-o.x,dy=P.y-o.y,d=Math.hypot(dx,dy);if(d>range)return false;
 let da=Math.atan2(dy,dx)-o.a;while(da>Math.PI)da-=6.283;while(da<-Math.PI)da+=6.283;if(Math.abs(da)>half)return false;
 if(inField(P.x,P.y)&&d>50)return false;
 for(let t=12;t<d;t+=10){const x=o.x+dx/d*t,y=o.y+dy/d*t,tt=tget(Math.floor(x/TS),Math.floor(y/TS));if(tt===BL||tt===TR)return false;}
 return true;
}
function plantUpdate(dt){
 plantTick(dt);popTick(dt);
 if(!G||!ZONE||ZONE.name!=='plantage')return;
 const z=ZONE,L=skl(),sneak=!G.shift&&!(G.med&&G.med.tower===2)&&inPlantFence(P.x,P.y);
 let seen=null;
 L.forEach(d=>{
  if(d.k==='wache'){
   const W=WACHW[d.i];d.s+=dt*(d.al>.3?10:30);const q=wachPos(W,d.s);d.x=q.x;d.y=q.y;
   const look=Math.sin(timeNow*.9+d.i*2)*.5;d.a=q.a+look;d.walk+=dt*6;
   if(sneak&&sees(d,140,.55)){d.al+=dt*1.6;seen=d;}else d.al=Math.max(0,d.al-dt*.6);
   d.say-=dt;if(d.say<=0){d.say=rf(7,13);if(Math.hypot(d.x-P.x,d.y-P.y)<300)addFx(d.x,d.y-24,pick(G.shift?['Fleißig, fleißig!','Starkes Signal heute.','Taschenkontrolle am Ausgang nicht vergessen!']:['Alles ruhig ...','Hat da was geraschelt?','Rundgang Nummer 48.']),'#cfe0ff',1.6);}
  }else if(d.k==='kamera'){
   d.a=d.a0+Math.sin(timeNow*.7+d.x)*d.sw;
   if(sneak&&sees(d,d.r||160,.32)){d.al+=dt*2;seen=d;}else d.al=Math.max(0,d.al-dt*.8);
  }
 });
 if(seen&&seen.al>=1){plantCaught();return;}
 if(seen&&!z.warn){z.warn=1;addFx(seen.x,seen.y-26,'?','#ffd23f',1.2);}
 if(!seen)z.warn=0;
}
function plantCaught(){
 const n=G.med?G.med.loot||0:0;if(G.med)medLootTake();G.planBan=G.day+1;if(G.tunnel===1||G.tunnel===2)G.tunnel=3;
 popAdd(-12);sfx('bonk');
 const txt='Erwischt! Der Sicherheitsdienst hält dich am Kragen fest'+(n?' und nimmt dir die geklaute Technik ab':'')+'. Der Tunnel wird zugeschüttet, die Polizei holt dich ab.';
 toast(txt);
 const m=MKQ.land;G.ret=m?{x:m.x,y:m.y+32}:G.ret;
 leaveZone(true);arrest();
}
function shiftTargets(z){
 const S=[[14,13.5],[27,13.5],[38,13.5],[16,4.5],[28,4.5],[39,4.5],[17,23.6],[28,23.6],[23,9],[34,18]];
 for(let i=S.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));const t=S[i];S[i]=S[j];S[j]=t;}
 z.ska=z.ska.filter(d=>d.k!=='ernte');S.slice(0,5).forEach(q=>z.ska.push({k:'ernte',x:q[0]*TS,y:q[1]*TS,a:0,walk:0}));
}
function pfoertnerMenu(){
 if(G.shift&&!inPlantFence(P.x,P.y))G.shift=null;
 const ban=G.planBan&&G.day<G.planBan,M=G.med||{};
 if(M.tower===2){mdl('Pförtner Bollmann','„Guten Tag, Chef! Der Turm sendet, das Lager ist voll, die Wachleute grüßen.“',[['Ins Lager und Sendezentrum','px:chef']]);return;}
 const ch=[['Schicht als Techniker: 90 € Lohn','px:job',!!ban||!!G.shift]];
 if(G.tunnel===1)ch.push(['(Du kennst da einen Tunnel ...)','px:tip']);
 const can=medRankI()>=4;
 ch.push([can?'Den Turm übernehmen: 80.000 €':'Den Turm übernehmen (ab Rang Sender-Boss)','px:buy',!can||G.cash<80000]);
 mdl('Pförtner Bollmann','„Fernsehturm Rheinhanfen. Hier sendet die GlotzKonzern AG, und im Lager stehen Receiver, Antennen, Kabel und Fernseher. Zaun, Kameras, Wachleute. Mitarbeiter werden am Ausgang kontrolliert.“'+(ban?' Er schaut dich streng an: „Du hast hier bis Tag '+G.planBan+' Hausverbot.“':''),ch.concat([['Warum so viel Sicherheit?','px:why']]));
}
function ausgangMenu(){
 if(!G.shift){if(G.med&&G.med.tower===2){plantTeleport(7*TS,15*TS);toast('Der Wachmann salutiert: „Schönen Feierabend, Chef!“');return;}toast('Der Ausgang ist nur für Mitarbeiter.');return;}
 const done=G.shift.n>=G.shift.need;
 mdl('Ausgang mit Taschenkontrolle',done?'Schicht geschafft! Ein Wachmann tastet dich freundlich ab: „Alles sauber.“':'Noch '+(G.shift.need-G.shift.n)+' Kisten bis Feierabend.',done?[['Lohn abholen und gehen','px:out']]:[['Schicht abbrechen (kein Lohn)','px:quit']]);
}
function ernteMenu(d){UI.er=d;mdl('Wartungsstation','Ein Regal voller Receiver, ein blinkender Verteiler. Die Kamera über dem Gang blinkt rot.',[['Warten: Kabel prüfen und Receiver einräumen','px:ernte'],['Heimlich einen Receiver einstecken','px:klau']]);}
function plantTeleport(x,y){P.x=x;P.y=y;P.vx=P.vy=0;cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);}
function plantOpen(d){
 const k=d.k;
 if(k==='wache'){toast(G.shift?'„Fleißig weiter, die Technik wartet!“':'Der Wachmann leuchtet dir ins Gesicht. Besser nicht hier herumstehen.');return;}
 if(k==='kamera'){toast('Eine Kamera. Sie macht genau das, was Kameras machen.');return;}
 if(k==='ernte'){ernteMenu(d);return;}
 if(k==='loch'){
  if(G.tunnel===3){toast('Hier war mal ein Tunnel. Jetzt ist er eingestürzt und zugeschüttet. Das war es.');return;}
  if(!G.tunnel){G.tunnel=1;sfx('magic');mdl('Lockere Erde','Unter einem Busch ist die Erde ganz locker. Du schiebst Äste weg: Ein alter Kaninchen-Tunnel, groß genug für dich! Er führt unter dem Zaun durch. Einmal benutzen, dann hält er vermutlich nicht mehr.',[['Durchkriechen','px:crawl'],['Später','px:later']]);return;}
  mdl('Der Tunnel','Der alte Tunnel unter dem Zaun. Ein Mal, vielleicht zwei Mal hält er noch.',[['Durchkriechen','px:crawl']]);return;
 }
 if(k==='tunnel2'){mdl('Tunnelausgang','Das Loch führt zurück nach draußen.',[['Zurückkriechen','px:back']]);return;}
 if(k==='zaun'){
  if(G.tunnel===2){toast('Der Zaun ist schon offen. Schnell rein, schnell raus!');return;}
  mdl('Zaun am Feld','Ein Stück Zaun hängt locker. Du könntest es einmal leise aufbiegen. Danach merkt es bestimmt jemand.',[['Zaun leise aufbiegen','px:zaun',G.tunnel!==1]]);return;
 }
 if(k==='beet'){
  if(!d.left){toast('Hier ist nichts mehr.');return;}
  medLoot(d);return;
 }
}
function skAct17(p){
 if(p.indexOf('px:')!==0)return false;
 const a=p.slice(3),z=ZONE;
 if(a==='job'){
  if(G.planBan&&G.day<G.planBan){toast('Hausverbot bis Tag '+G.planBan+'.');return true;}
  G.shift={n:0,need:5};if(z)shiftTargets(z);plantTeleport(12.5*TS,15*TS);sfx('ok');
  toast('Blaumann an, Werkzeugkoffer in die Hand! Erledige 5 Wartungen an den leuchtenden Stationen, dann zum Ausgang. Klauen ist zwecklos: Kameras überall.');
 }else if(a==='chef'){plantTeleport(12.5*TS,15*TS);sfx('ok');toast('Willkommen im Sendezentrum, Chef! Im Lager nimmst du dir, was du brauchst: Jeden Morgen kommt frische Technik.');
 }else if(a==='buy'){medTowerBuy();
 }else if(a==='why')toast('„Weil hier die teuerste Technik der Stadt lagert. Bei uns kommt keiner rein und keiner mit was raus. Na gut, neulich haben Kaninchen unten am Südzaun gebuddelt. Das schütten wir irgendwann zu.“');
 else if(a==='tip')toast('Du sagst lieber nichts. Der Pförtner pfeift ein Lied und schaut in die andere Richtung.');
 else if(a==='ernte'){
  const d=UI.er;if(!G.shift||!d)return true;
  z.ska=z.ska.filter(q=>q!==d);G.shift.n++;sfx('pick');addFx(d.x,d.y-16,'+1 Wartung','#9ff5c0',1.2);
  toast(G.shift.n>=G.shift.need?'Fünf Wartungen! Feierabend, ab zum Ausgang.':'Wartung '+G.shift.n+' von '+G.shift.need+' erledigt.');
 }else if(a==='klau'){
  G.klau=(G.klau||0)+1;
  if(G.klau%2===1){toast('Piep! Die Kamera zoomt auf dich. Der Vorarbeiter ruft: „Mitarbeiter nehmen hier nichts mit! Letzte Warnung!“');popAdd(-1);}
  else{G.shift=null;G.planBan=G.day+2;popAdd(-3);plantTeleport(7*TS,15*TS);toast('Taschenkontrolle! Der Receiver in deiner Jacke wird gefunden. Du bist für zwei Tage rausgeflogen, ohne Lohn.');}
 }else if(a==='out'){
  if(!G.shift||G.shift.n<G.shift.need)return true;
  G.shift=null;G.cash+=90;G.stats.earned+=90;fameAdd(1);popAdd(1);xpAdd(20);G.stats.schicht=(G.stats.schicht||0)+1;plantTeleport(7*TS,15*TS);sfx('coin');
  toast('Taschenkontrolle: alles sauber. Lohn: 90 €. Der Turm sendet weiter, dank dir.');
 }else if(a==='quit'){G.shift=null;plantTeleport(7*TS,15*TS);toast('Schicht abgebrochen. Kein Lohn heute.');}
 else if(a==='crawl'){
  if(G.tunnel===3)return true;
  plantTeleport(PZ.tin[0]*TS,PZ.tin[1]*TS-4);sfx('pat');
  toast('Du kriechst durch den Tunnel ... und kommst hinter dem Zaun wieder raus. Wachen und Kameras im Blick behalten! Zwischen den Regalen sieht dich keiner.');
 }else if(a==='back'){
  if(G.med){G.med.loot=0;G.med.lootHw={};G.med.lootC=[];}
  plantTeleport(PZ.tunnel[0]*TS+16,PZ.tunnel[1]*TS-12);
  if(G.tunnel===2){G.tunnel=3;sfx('rumble');toast('Du kriechst raus, hinter dir rieselt Erde. Der Tunnel ist eingestürzt. Das war es mit dem Trick.');}
  else toast('Du kriechst zurück nach draußen.');
 }else if(a==='zaun'){
  if(G.tunnel!==1)return true;
  G.tunnel=2;const x=PZ.zaun[0],y=PZ.zaun[1];z.T[y*z.MW+x]=FD;
  const c=z.WC.getContext('2d');c.fillStyle='#4a3a22';c.fillRect(x*TS,y*TS,TS,TS);
  z.ska=z.ska.filter(q=>q.k!=='zaun');sfx('pat');
  toast('Quietsch ... ganz leise biegst du den Zaun auf. Das geht nur dieses eine Mal. Schnell zu den Lagerregalen!');
 }
 return true;
}
function plantPrompt(d){
 const k=d.k;
 return k==='wache'?'OK: Wachmann ansprechen':k==='kamera'?'OK: Kamera ansehen':k==='ernte'?'OK: Warten':k==='loch'?(G.tunnel?'OK: Zum Tunnel':'OK: Lockere Erde untersuchen'):k==='tunnel2'?'OK: Zurück in den Tunnel':k==='zaun'?'OK: Zaun untersuchen':k==='beet'?'OK: Lagerkiste öffnen':'';
}
const PSK={wache:1,kamera:1,ernte:1,loch:1,tunnel2:1,zaun:1,beet:1};
function plantDraw(d){
 const k=d.k;
 if(k==='loch'){if(Math.hypot(d.x-P.x,d.y-P.y)>90&&!G.tunnel)return;ctx.fillStyle=G.tunnel===3?'#6a5a3a':'#3a2a1a';ctx.beginPath();ctx.ellipse(d.x,d.y,12,7,0,0,6.283);ctx.fill();if(G.tunnel!==3){ctx.fillStyle='#120c06';ctx.beginPath();ctx.ellipse(d.x,d.y+1,8,4.4,0,0,6.283);ctx.fill();}return;}
 if(k==='tunnel2'){ctx.fillStyle='#3a2a1a';ctx.beginPath();ctx.ellipse(d.x,d.y,11,6,0,0,6.283);ctx.fill();ctx.fillStyle='#120c06';ctx.beginPath();ctx.ellipse(d.x,d.y+1,7,3.6,0,0,6.283);ctx.fill();return;}
 if(k==='zaun'){if(G.tunnel===1){ctx.strokeStyle='rgba(255,210,63,'+(.4+.3*Math.sin(timeNow*5))+')';ctx.lineWidth=2;ctx.strokeRect(d.x-15,d.y-15,30,30);ctx.lineWidth=1;}return;}
 if(k==='beet'){if(!d.left)return;ctx.fillStyle='rgba(160,255,180,'+(.18+.12*Math.sin(timeNow*4+d.x))+')';circle(d.x,d.y,14);return;}
 if(k==='ernte'){const g=.3+.2*Math.sin(timeNow*4+d.x);ctx.fillStyle='rgba(255,210,63,'+g+')';circle(d.x,d.y,13);ctx.fillStyle='#2a3444';ctx.fillRect(d.x-8,d.y-5,16,10);ctx.fillStyle='#7ad35a';ctx.fillRect(d.x+3,d.y-3,3,2);ctx.fillStyle='#5fd0ff';ctx.fillRect(d.x-6,d.y-3,7,2);return;}
 if(k==='kamera'||k==='wache'){
  const R=k==='kamera'?(d.r||160):140,hf=k==='kamera'?.32:.55,on=d.al>.05;
  ctx.fillStyle=on?'rgba(255,80,60,'+(.14+d.al*.2)+')':'rgba(255,240,150,.13)';ctx.beginPath();ctx.moveTo(d.x,d.y);ctx.arc(d.x,d.y,R,d.a-hf,d.a+hf);ctx.closePath();ctx.fill();
  if(k==='kamera'){ctx.fillStyle='#5a5f68';ctx.fillRect(d.x-2,d.y-2,4,4);ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.fillStyle='#2b2f38';ctx.fillRect(-4,-4,12,8);ctx.fillStyle=Math.floor(timeNow*2)%2?'#ff3030':'#661010';circle(9,0,1.8);ctx.restore();}
  else{fig(d.x,d.y,d.a,{dress:'#2b3a4a',hair:'#1a1a1a',hat:'#1b2530',hat2:'#2b3a4a',brim:4.8,sk:5.2,walk:d.walk});ctx.fillStyle='#ffd23f';circle(d.x+Math.cos(d.a)*9,d.y+Math.sin(d.a)*9,2);}
  if(d.al>.3){ctx.fillStyle='#ffd23f';ctx.font='bold 14px Arial';ctx.textAlign='center';ctx.fillText(d.al>.7?'!':'?',d.x,d.y-24);ctx.textAlign='start';}
 }
}
function plantStatic(c,z){
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){
  if(z.T[y*ZW+x]!==FD)continue;
  const px=x*TS,py=y*TS;c.fillStyle='#3a3f48';c.fillRect(px,py,TS,TS);c.fillStyle='#5a6270';c.fillRect(px+2,py+3,TS-4,TS-6);
  for(let k=0;k<3;k++){const by=py+5+k*8;c.fillStyle=['#2e86c1','#e5504d','#f1c40f','#7ad35a','#e8edf2'][(x*3+y+k)%5];c.fillRect(px+4,by,TS-8,6);c.fillStyle='rgba(0,0,0,.25)';c.fillRect(px+4,by+5,TS-8,1);}
  if((x+y)%3===0){c.fillStyle=(x+y)%2?'#7ad35a':'#ff5f5f';c.fillRect(px+TS-7,py+4,3,3);}
 }
 const sign=(x,y,t)=>{c.fillStyle='#5a3a1f';c.fillRect(x-2,y,4,14);c.font='bold 8px Arial';const sw=Math.max(116,Math.ceil(c.measureText(t).width)+14);c.fillStyle='#f4f4f4';c.fillRect(x-sw/2,y-12,sw,16);c.strokeStyle='#c0392b';c.lineWidth=2;c.strokeRect(x-sw/2,y-12,sw,16);c.lineWidth=1;c.fillStyle='#c0392b';c.font='bold 8px Arial';c.textAlign='center';c.textBaseline='middle';c.fillText(t,x,y-4);c.textAlign='start';};
 sign(6.5*TS,16.6*TS,'FERNSEHTURM RHEINHANFEN');sign(26*TS,27.3*TS,'BETRETEN VERBOTEN · KAMERAS');
}
function fencePlant(c,px,py,g,x,y){
 const l=g(x-1,y)===FN,rr=g(x+1,y)===FN,u=g(x,y-1)===FN,d=g(x,y+1)===FN;
 c.strokeStyle='rgba(200,210,220,.55)';c.lineWidth=1;
 if(l||rr){for(let i=-16;i<16;i+=5){c.beginPath();c.moveTo(px+i,py-6);c.lineTo(px+i+5,py+4);c.moveTo(px+i+5,py-6);c.lineTo(px+i,py+4);c.stroke();}c.fillStyle='#8a929c';c.fillRect(px-16,py-7,32,2);c.fillRect(px-16,py+3,32,2);}
 if(u||d){for(let i=-16;i<16;i+=5){c.beginPath();c.moveTo(px-6,py+i);c.lineTo(px+4,py+i+5);c.moveTo(px+4,py+i);c.lineTo(px-6,py+i+5);c.stroke();}c.fillStyle='#8a929c';c.fillRect(px-7,py-16,2,32);c.fillRect(px+3,py-16,2,32);}
 c.fillStyle='#5a5f68';c.fillRect(px-3,py-3,6,6);c.fillStyle='#c0392b';c.fillRect(px-1,py-1,2,2);
}
let POPT=5;
function popTick(dt){
 POPT-=dt;if(POPT>0||!G)return;POPT=rf(6,10);
 const p=G.pop===undefined?10:G.pop;if(p>-30&&p<45)return;
 const q=peds.filter(x=>!x.snow&&!x.kid&&Math.hypot(x.x-P.x,x.y-P.y)<200);if(!q.length)return;
 const d=pick(q);addFx(d.x,d.y-22,p>=45?pick(['Hallo, Held!','Da ist ja unser Liebling!','Ein Autogramm, bitte!']):pick(['Buh!','Der schon wieder!','Pfui!','Ach nee, du ...']),p>=45?'#9ff5c0':'#ff8a65',1.6);
}
function extPlaceBtns(k){
 let b='';
 if(k==='land')b+=btn('Zum Fernsehturm','toPlant',null,{note:'Hightech-Fernsehturm der GlotzKonzern AG, streng bewacht. Am Pförtner gibt es Schichten als Techniker'});
 if(k==='mega')b+=pfandBtn();
 if(k==='hq')b+=btn('Hacker-PC im Hinterzimmer','medPC',null,{note:'Codes knacken, Scraper starten, Filme schauen'})+btn('Medien-Zentrale','medS',null,{note:medSum()});
 if(k==='hq')b+=btn('Deine Pflanzen ('+((G.plants||[]).length)+' / 3)','growS',null,{note:(G.plants||[]).map(p=>p.nm+': '+(plantNeeds(p).join(', ')||'glücklich')).join(' · ')||'Drei Pflanzen für dich selbst sind erlaubt'});
 return b;
}

function needCol(v){return v>=60?'var(--gr)':v>=30?'var(--am)':'var(--rd)';}
function needAdd(h,d){if(!G)return;G.hun=clamp((G.hun===undefined?80:G.hun)+h,0,100);G.dur=clamp((G.dur===undefined?80:G.dur)+d,0,100);}
function needTick(dt){
 if(!G)return;
 if(G.hun===undefined)G.hun=80;if(G.dur===undefined)G.dur=80;
 const hot=wxType()==='heat'||(ZONE&&(ZONE.name==='vulkan'||ZONE.name==='malle'||ZONE.name==='strand'));
 G.hun=Math.max(0,G.hun-dt*.14);G.dur=Math.max(0,G.dur-dt*(hot?.3:.19));
 if(G.hun<25&&!G.hunW){G.hunW=1;toast('Dein Magen knurrt! Iss was: ein Menü im Lokal, etwas vom Büdchen oder ein Menü aus dem Rucksack.');}
 if(G.hun>=35)G.hunW=0;
 if(G.dur<25&&!G.durW){G.durW=1;toast('Du hast Durst! Wasser oder Limo vom Büdchen, oder Alkoholfreies aus dem Rucksack.');}
 if(G.dur>=35)G.durW=0;
 if(G.hun<20)G.mood=Math.max(0,G.mood-dt*.12);
 if(G.dur<20)G.mood=Math.max(0,G.mood-dt*.15);
}
const SHOPN={brezn:[35,0],nata:[25,0],sardine:[35,0],waffel:[30,0],panhas:[35,0],schmarrn:[45,0],strudel:[30,0],hahn:[35,0],himmel:[40,0],honig:[25,0],hbroet:[30,0],zucker:[12,0],popcorn:[18,0],lherz:[12,0],wasser:[0,45],limo:[0,35],brause:[0,35],melange:[5,25],tea:[0,30]};
function selfBtns(){
 let b='';const m=MENUS.find(g=>(G.inv[g]||0)>0);
 if(m)b+=btn('Selbst essen: '+GOODS[m].n+' ('+G.inv[m]+')','selfEat',m,{note:'Macht satt. Essen: '+Math.round(G.hun===undefined?80:G.hun)+' %'});
 if((G.inv.b_frei||0)>0)b+=btn('Alkoholfreies trinken ('+G.inv.b_frei+')','selfDrink',null,{note:'Löscht den Durst. Trinken: '+Math.round(G.dur===undefined?80:G.dur)+' %'});
 return b;
}
function selfEat(g){
 if(!G.inv[g]){return;}G.inv[g]--;needAdd(55,10);mood(4,'+4 Lecker');sfx('crunch');closeAll();
 toast(pick(['Du setzt dich kurz an den Rand und futterst '+GOODS[g].n+'. Eigentlich war es für die Kundschaft. Egal, lecker!','Mmh, '+GOODS[g].n+'! Lieferfahrer müssen auch mal essen.']));
}
function selfDrink(){
 if(!G.inv.b_frei){return;}G.inv.b_frei--;needAdd(0,50);mood(2,'+2');sfx('glug');closeAll();
 toast('Ein kühles Alkoholfreies. Zisch! Der Durst ist weg, der Kopf bleibt klar.');
}

function unstuck(){
 if(P.inCar||P.ride)return false;
 if(!hit(P.x,P.y,6))return false;
 const f=freeSpot(P.x,P.y);
 if(!hit(f.x,f.y,6)){P.x=f.x;P.y=f.y;return true;}
 for(let r=40;r<=400;r+=24)for(let k=0;k<16;k++){const a=k/16*6.283,x=P.x+Math.cos(a)*r,y=P.y+Math.sin(a)*r;if(!hit(x,y,8)){P.x=x;P.y=y;return true;}}
 return false;
}
function unstuckTick(){if(P.inCar||P.ride||P.hide||P.sit){P.stk=0;return;}if(hit(P.x,P.y,6)){P.stk=(P.stk||0)+(fdt||.016);if(P.stk>.35){P.stk=0;unstuck();}}else P.stk=0;}
function freeMe(){
 closeAll();
 if(P.ride){P.ride.sp=0;leaveRide(true);}
 if(P.hide)unhide(false);
 if(P.sit)standUp();
 let moved=unstuck();
 if(!moved){const f=freeSpot(P.x+rf(-40,40),P.y+rf(-40,40));if(!hit(f.x,f.y,7)){P.x=f.x;P.y=f.y;moved=true;}}
 if(!moved&&!ZONE){P.x=GATE.x;P.y=GATE.y;}
 P.vx=P.vy=0;
 toast(pick(['Ruck, zuck, frei! Du schüttelst dir die Blätter aus den Haaren.','Mit einem beherzten Hüpfer bist du wieder frei.','Befreit! Der Baum wirkt ein bisschen beleidigt.']));
}
let RWT=0;
function rideWet(R,x,y){
 if(R.k==='boat'||R.k==='sled')return false;
 const r=RP[R.k].r,x0=Math.floor((x-r)/TS),x1=Math.floor((x+r)/TS),y0=Math.floor((y-r)/TS),y1=Math.floor((y+r)/TS);
 for(let j=y0;j<=y1;j++)for(let i=x0;i<=x1;i++){const t=tget(i,j);if(t===DP||t===WT){
  if(timeNow-RWT>6){RWT=timeNow;toast(R.k==='bike'&&ZONE&&ZONE.name==='amsterdam'?'Fast in die Gracht! Fahrräder schwimmen nicht, nicht mal in Holland.':pick(['Halt! Da ist Wasser. Dein '+RN[R.k]+' ist kein U-Boot.','Platsch, fast! Über Wasser fährt hier nur das Boot.']));}
  return true;}}
 return false;
}
Object.assign(RP,{escoot:{mx:290,ac:300,br:460,dr:120,tn:3.2,r:7,g:0},cart:{mx:220,ac:260,br:300,dr:60,tn:2.6,r:9,g:0},mower:{mx:120,ac:140,br:300,dr:160,tn:2.4,r:11,g:0},rutsch:{mx:150,ac:200,br:300,dr:150,tn:3.6,r:8,g:0},sofa:{mx:165,ac:150,br:260,dr:110,tn:2,r:12,g:0}});
Object.assign(RN,{escoot:'E-Scooter',cart:'Einkaufswagen',mower:'Aufsitzmäher',rutsch:'Rutschauto',sofa:'Motorsofa'});
Object.assign(RMSG,{
 escoot:['Der E-Scooter piept empört: „Bitte zuerst die App herunterladen!“ Du fährst trotzdem los.','Surrrr! Der E-Scooter ist geklaut und schneller als gedacht.'],
 cart:['Einkaufswagen geklaut! Im Griff steckt noch ein Pfand-Chip. Das Rad vorne links quietscht wie immer.','Du springst in den Einkaufswagen und rollst los. Rattern, rattern, Freiheit!'],
 mower:['Gärtner Günther ruft: „Mein Rasenmäher!“ Zu spät. Du mähst dir jetzt einen Weg durch die Stadt.','Brumm, brumm! Wo du langfährst, ist der Rasen danach gemäht. Gern geschehen.'],
 rutsch:['Ein Papa ruft: „Das ist das Rutschauto von meinem Sohn!“ Du passt kaum rein, aber es fährt.','Die Knie bis zu den Ohren, das Rutschauto quietscht. Wroom!'],
 sofa:['Opa Heinz ruft: „Mein Motorsofa! Mit dem fahr ich sonntags zum Bäcker!“ Jetzt fährst du damit.','Das Motorsofa tuckert los. Gemütlicher bist du noch nie geflüchtet.']
});
const XRD={escoot:1,cart:1,mower:1,rutsch:1,sofa:1};
const XRL={escoot:'E-Scooter klauen',cart:'Einkaufswagen klauen',mower:'Aufsitzmäher klauen',rutsch:'Rutschauto klauen',sofa:'Motorsofa klauen'};
const XRS={escoot:'Aufsteigen',cart:'Reinspringen',mower:'Aufsteigen',rutsch:'Reinquetschen',sofa:'Hinsetzen und losfahren'};
function xRides(){
 const put=(k,types,n,near)=>{for(let i=0;i<n;i++){let p=null;for(let t=0;t<60;t++){const q=near?{x:near.x+rf(-90,90),y:near.y+rf(10,70)}:randTile(types,0,0);const tt=tget(Math.floor(q.x/TS),Math.floor(q.y/TS));if(types.indexOf(tt)>=0&&!inNoGo(q.x,q.y)&&!hit(q.x,q.y,12)&&!inYard(q.x,q.y)){p=q;break;}}if(p)RIDES.push(mkRide(k,p.x,p.y,rf(0,6.283)));}};
 put('escoot',[SW],5);put('cart',[SW],2,MKQ.mega);put('mower',[GR],2);put('rutsch',[SW],1);put('sofa',[SW],1);
}
function xrSteal(R){
 R.stolen=true;heat(3);popAdd(-1);mood(6,'Frechheit siegt');sfx('honk');
 addFx(R.x,R.y-30,{escoot:'PIEP PIEP!',cart:'Mein Wagen!',mower:'MEIN RASENMÄHER!',rutsch:'Das ist meins!',sofa:'MEIN SOFA!'}[R.k],'#ff8a65',2);
 if(!ZONE&&copNear(P.x,P.y,170)&&chance(.4)&&wanted===0)setTimeout(()=>{if(wanted===0)startWanted('Ein Polizist hat gesehen, wie du das '+RN[R.k]+' geklaut hast!');},600);
}
function xrDraw(R){
 const k=R.k,mv=Math.abs(R.sp)>20;
 if(k==='escoot'){
  ctx.fillStyle='#222';circle(-10,0,2.6);circle(10,0,2.6);
  ctx.fillStyle='#3a3f48';ctx.fillRect(-10,-2.6,18,5.2);ctx.fillStyle='#7ad35a';ctx.fillRect(-8,-2.6,14,1.4);
  ctx.strokeStyle='#2b2f38';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(8,0);ctx.lineTo(10,0);ctx.moveTo(10,-6.5);ctx.lineTo(10,6.5);ctx.stroke();ctx.lineWidth=1;
 }else if(k==='cart'){
  ctx.fillStyle='#222';[[-10,-7],[-10,7],[8,-7],[8,7]].forEach(q=>circle(q[0],q[1],1.8));
  ctx.strokeStyle='#c8ced6';ctx.lineWidth=1.2;ctx.strokeRect(-10,-8,18,16);for(let i=-6;i<8;i+=4){ctx.beginPath();ctx.moveTo(i,-8);ctx.lineTo(i,8);ctx.stroke();}for(let j=-4;j<8;j+=4){ctx.beginPath();ctx.moveTo(-10,j);ctx.lineTo(8,j);ctx.stroke();}
  ctx.fillStyle='#d63a3a';ctx.fillRect(-13,-8,2.4,16);ctx.lineWidth=1;
 }else if(k==='mower'){
  ctx.fillStyle='#222';[[-9,-9],[-9,9],[8,-8],[8,8]].forEach(q=>{ctx.fillRect(q[0]-3,q[1]-2,6,4);});
  ctx.fillStyle='#2f8a3a';ctx.fillRect(-11,-8,22,16);ctx.fillStyle='#3fae4f';ctx.fillRect(2,-6,9,12);ctx.fillStyle='#1b1d22';ctx.fillRect(-8,-5,7,10);
  ctx.strokeStyle='#ffd23f';ctx.lineWidth=1.6;ctx.beginPath();ctx.arc(6,0,3.4,0,6.283);ctx.stroke();ctx.lineWidth=1;
  if(mv&&chance(.3))FX.push({x:R.x-Math.cos(R.a)*12+rf(-4,4),y:R.y-Math.sin(R.a)*12+rf(-4,4),vx:rf(-20,20),vy:rf(-20,20),t:0,life:.5,dot:'#7ad35a',r:1.5});
 }else if(k==='rutsch'){
  ctx.fillStyle='#222';[[-6,-6],[-6,6],[6,-6],[6,6]].forEach(q=>circle(q[0],q[1],2.4));
  ctx.fillStyle='#d63a3a';ctx.beginPath();ctx.ellipse(0,0,10,5.6,0,0,6.283);ctx.fill();ctx.fillStyle='#f4f4f4';circle(8,-2,1.4);circle(8,2,1.4);ctx.fillStyle='#222';circle(8.4,-2,.7);circle(8.4,2,.7);
  ctx.fillStyle='#ffd23f';ctx.fillRect(-2,-5.6,3,11.2);
 }else if(k==='sofa'){
  ctx.fillStyle='#222';[[-10,-10],[-10,10],[10,-10],[10,10]].forEach(q=>circle(q[0],q[1],2.2));
  ctx.fillStyle='#b5603a';ctx.fillRect(-12,-11,24,22);ctx.fillStyle='#8a4a2a';ctx.fillRect(-12,-11,7,22);ctx.fillRect(-12,-11,24,4);ctx.fillRect(-12,7,24,4);
  ctx.fillStyle='#d08050';ctx.fillRect(-4,-6,13,5.6);ctx.fillRect(-4,.6,13,5.6);
  if(mv&&chance(.25))FX.push({x:R.x-Math.cos(R.a)*14,y:R.y-Math.sin(R.a)*14,vx:rf(-6,6),vy:rf(-24,-8),t:0,life:1,dot:'rgba(200,200,200,.6)',r:rf(2,3.5)});
 }
}
function mowTick(){
 const R=P.ride;if(!R||R.k!=='mower'||ZONE||Math.abs(R.sp)<15)return;
 const i=Math.floor(R.x/TS),j=Math.floor(R.y/TS);if(tget(i,j)!==GR)return;
 const c=WC.getContext('2d');c.save();c.translate(R.x,R.y);c.rotate(R.a);c.fillStyle='rgba(190,240,150,.16)';c.fillRect(-3,-10,6,20);c.restore();
 G.mowed=(G.mowed||0)+1;if(G.mowed%900===0){G.cash+=15;toast('Die Stadtgärtnerei winkt: Schön gemäht! +15 € fürs Rasenmähen.');}
}
const BEPS=[
 {who:{dress:'#5a6a8a',hair:'#3a2a1a'},it:'sofa',m:'stop',say:['Puh ...','Kurze Pause.'],t:'Ein Mann trägt ein Sofa vorbei. Er setzt sich kurz drauf, ruht sich aus und trägt es dann weiter.'},
 {who:{dress:'#c96a9a',hair:'#e6c36a',hairLen:5},it:'fisch',m:'pass',say:['Bei Fuß, Blubbi!'],t:'Jemand führt einen Goldfisch im Glas auf Rädern Gassi. Der Goldfisch wirkt sehr zufrieden.'},
 {it:'taube',m:'fly',say:['Gurr.'],t:'Eine Taube landet neben dir, schaut dich lange an und nickt. Dann fliegt sie weiter. Ihr habt euch verstanden.'},
 {who:{dress:'#2e86c1',hair:'#8a5a2a'},it:'ballon',m:'pass',say:['Meine Ballons!','Huiii!'],t:'Ein Luftballonverkäufer stolpert. Er hält sich am letzten Ballon fest und hebt kurz ab. Dann landet er sanft und verbeugt sich.'},
 {it:'drohne',m:'fly',say:['Lieferung für ... falsche Bank.'],t:'Eine Pizza-Drohne schwebt heran, scannt dich und surrt: „Falsche Bank.“ Sie fliegt beleidigt weiter.'},
 {who:{dress:'#6a6a7a',hair:'#4a4a4a'},it:'wolke',m:'pass',say:['Montag.'],t:'Ein Mann mit einer eigenen kleinen Regenwolke über dem Kopf schlurft vorbei. Er sagt nur: „Montag.“'},
 {it:'zwerg',m:'pass',say:['...'],t:'Ein Gartenzwerg läuft allein vorbei. Er tut so, als hättest du nichts gesehen. Du tust auch so.'},
 {who:{dress:'#e8a020',hair:'#3a2a1a'},it:'leiter',m:'stop',say:['Links!','Nein, DEIN Links!'],t:'Zwei Leute mit einer langen Leiter drehen sich vor dir im Kreis, wie im Stummfilm. Dann gehen sie in die falsche Richtung weiter.'},
 {who:{dress:'#7a7a9a',hair:'#d8d8d8'},it:'wagen',m:'pass',say:['Möööp!','Platz da!'],t:'Ein Opa schiebt einen Einkaufswagen voller Kuscheltiere vorbei und hupt mit dem Mund: „Möööp!“'},
 {who:{dress:'#3a3a3a',hair:'#bbbbbb',beard:'#bbbbbb'},it:'',m:'sit',say:['Hmmm ...'],t:'Ein Bank-Philosoph setzt sich neben dich: „Wenn eine Bank im Park steht und niemand sitzt drauf, ist sie dann trotzdem bequem?“ Er geht, bevor du antworten kannst.'},
 {who:{dress:'#e5504d',hair:'#3a2a1a'},it:'',m:'back',say:['Hallo!','Rückwärts ist gesünder!'],t:'Ein Jogger joggt vorbei. Rückwärts. Er winkt dir freundlich zu.'},
 {who:{dress:'#8e44ad',hair:'#e8d080',hairLen:4},it:'tuba',m:'stop',say:['Trööööt.'],t:'Eine Tubaspielerin bleibt stehen und spielt dir ein einzelnes, sehr tiefes Ständchen. Dann geht sie wortlos weiter.'},
 {who:{dress:'#4a7a5a',hair:'#6a4a2a'},it:'kaktus',m:'pass',say:['Er beißt nicht.','Er sticht.'],t:'Ein Mann führt einen Kaktus an der Leine spazieren. „Er beißt nicht“, sagt er. „Er sticht.“'},
 {who:{dress:'#f1c40f',hair:'#c96a2a'},it:'karte',m:'stop',say:['Wo ist Rheinhanfen?'],t:'Ein Tourist mit riesiger Karte fragt dich nach dem Weg nach Rheinhanfen. Du sagst ihm, er steht mittendrin. Er ist begeistert und macht ein Foto von dir.'},
 {who:{dress:'#27ae60',hair:'#e6c36a'},it:'surf',m:'stop',say:['Wo ist das Meer?'],t:'Ein Surfer mit Brett fragt: „Wo ist hier das Meer?“ Du zeigst auf eine Pfütze. Er nickt ernst und paddelt los.'},
 {it:'tauben',m:'pass',say:['Gurr, zwo, drei, vier!'],t:'Eine Tauben-Gang marschiert im Gleichschritt vorbei. Gurr, zwo, drei, vier. Der Anführer trägt einen Kronkorken als Helm.'},
 {who:{dress:'#c0392b',hair:'#2a2a2a'},it:'pizza',m:'stop',say:['Die ist für dich!','Hab mich verwählt.'],t:'Ein Pizzabote drückt dir eine Pizza in die Hand: „Bestellt ist bestellt!“ Wer sie bestellt hat, weiß keiner. Lecker ist sie trotzdem.',fx:'pizza'},
 {it:'eichhorn',m:'pass',say:['...'],t:'Ein Eichhörnchen rennt mit einer ganzen Brezel vorbei, die doppelt so groß ist wie es selbst. Respekt.'},
 {z:'strand',it:'moewe',m:'fly',say:['Kreisch!'],t:'Eine Möwe stibitzt einem Urlauber die Pommes, setzt sich auf seinen Kopf und isst sie dort in Ruhe auf.'},
 {z:'berge',who:{dress:'#2e86c1',hair:'#3a2a1a'},it:'ski',m:'pass',say:['Wo ist der Schnee?'],t:'Ein Skifahrer stapft auf Skiern über die Wiese und sucht den Schnee. „Gestern war er noch da!“'},
 {z:'amsterdam',who:{dress:'#ff7a1a',hair:'#e6c36a'},it:'rad2',m:'pass',say:['Dag!'],t:'Ein Holländer schiebt ein Fahrrad, auf dem ein zweites Fahrrad liegt, auf dem ein drittes liegt. „Für den Notfall“, sagt er.'},
 {z:'malle',who:{dress:'#e5504d',hair:'#f4d58a'},it:'',m:'pass',say:['Polonääääse!'],t:'Ein einsamer Mann tanzt Polonaise. Allein. Mit voller Hingabe. Nach und nach hängen sich drei Leute dran.'},
 {z:'bayern',it:'dackel',m:'pass',say:['Wuff!'],t:'Ein Dackel in Lederhose spaziert vorbei, und zwar ganz allein. Er grüßt mit einem Bellen, das klingt wie „Servus“.'}
];
let BEA=null,BET=8,SEPT=120;
function bepPick(){const zn=ZONE?ZONE.name:'city';const L=BEPS.filter(e=>!e.z||e.z===zn);const Z=L.filter(e=>e.z===zn);return(Z.length&&chance(.5))?pick(Z):pick(L.filter(e=>!e.z));}
function bepStart(street){
 const e=bepPick(),dir=chance(.5)?1:-1,fly=e.m==='fly';
 const y=P.y+(fly?-46:street?rf(-50,50):34);
 BEA={e:e,x:P.x-dir*300,y:y,dir:dir,t:0,st:'go',stop:0,said:0,walk:0,street:!!street,tx:P.x+(e.m==='sit'?26*dir:0)};
}
function bepUpdate(dt){
 if(!G)return;
 if(BEA){
  const b=BEA,e=b.e;b.t+=dt;
  if(b.st==='go'){
   b.x+=b.dir*(e.m==='fly'?110:62)*dt;b.walk+=dt*8;
   const near=Math.abs(b.x-P.x)<(e.m==='sit'?30:44);
   if((e.m==='stop'||e.m==='sit')&&near&&!b.stopped){b.stopped=1;b.st='stop';b.stop=e.m==='sit'?4.5:3;if(e.m==='sit'){b.x=P.x+26*b.dir;b.y=P.y;}}
   if(!b.said&&Math.abs(b.x-P.x)<90){b.said=1;addFx(b.x,b.y-30,pick(e.say),'#fff2b0',2);toast(e.t);mood(4,'+4 Hihi');if(e.fx==='pizza'){needAdd(40,0);}}
   if(Math.abs(b.x-P.x)>420&&b.t>2){BEA=null;}
  }else{b.stop-=dt;if(b.stop<=0){b.st='go';if(e.m==='sit')b.y=P.y+34;}}
  if(b.t>18)BEA=null;
 }
 if(P.sit&&!BEA&&wanted===0){BET-=dt;if(BET<=0){BET=rf(10,18);bepStart(false);}}
 else if(!P.sit)BET=Math.min(BET,rf(4,7));
 if(!ZONE&&!P.sit&&!P.inCar&&!P.ride&&!BEA&&wanted===0&&!SKC.length){SEPT-=dt;if(SEPT<=0){SEPT=rf(90,160);bepStart(true);}}
}
function bepDraw(cx,cy){
 const b=BEA;if(!b)return;const e=b.e;
 if(b.x<cx-80||b.x>cx+VW+80||b.y<cy-80||b.y>cy+VH+80)return;
 const a=e.m==='back'?(b.dir>0?Math.PI:0):(b.dir>0?0:Math.PI),it=e.it,x=b.x,y=b.y;
 const hold=(dx,dy,fn)=>{ctx.save();ctx.translate(x,y);ctx.rotate(a);fn(dx,dy);ctx.restore();};
 if(it==='taube'||it==='moewe'){const f=Math.sin(timeNow*16)*4;ctx.fillStyle=it==='moewe'?'#f4f4f4':'#8a8f9a';ctx.beginPath();ctx.ellipse(x,y,6,3.4,0,0,6.283);ctx.fill();ctx.beginPath();ctx.moveTo(x-8,y-f);ctx.lineTo(x,y);ctx.lineTo(x+8,y-f);ctx.lineWidth=2.4;ctx.strokeStyle=ctx.fillStyle;ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#ffb347';circle(x+6*b.dir,y,1.4);if(it==='moewe'){ctx.fillStyle='#ffd23f';ctx.fillRect(x-2,y+3,4,5);}return;}
 if(it==='drohne'){ctx.fillStyle='#2b2f38';ctx.fillRect(x-7,y-3,14,6);[[-10,-6],[10,-6],[-10,6],[10,6]].forEach(q=>{ctx.fillStyle='rgba(200,220,255,'+(.4+.3*Math.sin(timeNow*40))+')';circle(x+q[0],y+q[1],4);});ctx.fillStyle='#d9a560';ctx.fillRect(x-6,y+5,12,10);ctx.fillStyle='#c0392b';ctx.fillRect(x-4,y+8,8,2);return;}
 if(it==='tauben'){for(let i=0;i<5;i++){const xx=x-i*12*b.dir,yy=y+(i%2)*6,s=Math.sin(b.walk+i)*1.2;ctx.fillStyle='#8a8f9a';ctx.beginPath();ctx.ellipse(xx,yy+s,5,3.6,0,0,6.283);ctx.fill();ctx.fillStyle='#6a7080';circle(xx+4*b.dir,yy-1+s,2.4);ctx.fillStyle='#ffb347';circle(xx+6.4*b.dir,yy-1+s,.9);if(i===0){ctx.fillStyle='#c8a040';circle(xx+4*b.dir,yy-2.6,2);}}return;}
 if(it==='eichhorn'){ctx.fillStyle='#c0602a';ctx.beginPath();ctx.ellipse(x,y,5,3.4,0,0,6.283);ctx.fill();ctx.beginPath();ctx.ellipse(x-7*b.dir,y-3,4,5,0,0,6.283);ctx.fill();ctx.strokeStyle='#c8893a';ctx.lineWidth=3;ctx.beginPath();ctx.arc(x+8*b.dir,y,6,0,6.283);ctx.stroke();ctx.lineWidth=1;return;}
 if(it==='zwerg'){drawGnom({x:x,y:y,a:a,walk:b.walk});return;}
 if(it==='dackel'){ctx.fillStyle='#8a4a1a';ctx.beginPath();ctx.ellipse(x,y,11,4,0,0,6.283);ctx.fill();circle(x+11*b.dir,y,3.4);ctx.fillStyle='#5a7a3a';ctx.fillRect(x-7,y-4,12,8);ctx.fillStyle='#ffd23f';ctx.fillRect(x-1,y-4,1.6,8);return;}
 if(e.m==='back'){P0fig(x,y,a,e.who,b.walk);return;}
 if(it==='sofa')hold(0,0,()=>{ctx.fillStyle='#b5603a';ctx.fillRect(-10,-16,22,32);ctx.fillStyle='#8a4a2a';ctx.fillRect(-10,-16,22,5);ctx.fillRect(-10,11,22,5);});
 P0fig(x,y,a,e.who,b.st==='go'?b.walk:0);
 if(it==='fisch')hold(0,0,()=>{ctx.strokeStyle='#7a5a32';ctx.beginPath();ctx.moveTo(4,4);ctx.lineTo(18,6);ctx.stroke();ctx.fillStyle='#222';circle(16,2,1.6);circle(16,10,1.6);ctx.fillStyle='rgba(120,190,255,.7)';circle(20,6,6);ctx.fillStyle='#ff8a2a';ctx.beginPath();ctx.ellipse(20+Math.sin(timeNow*3)*2,6,2.4,1.4,0,0,6.283);ctx.fill();});
 else if(it==='ballon'){const up=b.st==='go'&&b.said?Math.max(0,8-Math.abs(b.x-P.x)/10):0;['#e5504d','#2e86c1','#f1c40f','#27ae60','#d35bb5'].forEach((c,i)=>{const bx=x+(i-2)*6,by=y-30-up-(i%2)*6;ctx.strokeStyle='rgba(255,255,255,.6)';ctx.beginPath();ctx.moveTo(x,y-6);ctx.lineTo(bx,by);ctx.stroke();ctx.fillStyle=c;circle(bx,by,5);});}
 else if(it==='wolke'){ctx.fillStyle='rgba(120,130,150,.85)';circle(x-6,y-26,7);circle(x+4,y-28,8);circle(x+11,y-25,6);ctx.strokeStyle='rgba(140,190,255,.8)';for(let i=0;i<4;i++){const rx=x-8+i*6,ry=y-18+((timeNow*60+i*7)%14);ctx.beginPath();ctx.moveTo(rx,ry);ctx.lineTo(rx-1,ry+4);ctx.stroke();}}
 else if(it==='leiter')hold(0,0,()=>{ctx.save();ctx.rotate(b.st==='stop'?timeNow*2.5:0);ctx.fillStyle='#c8a070';ctx.fillRect(-40,-2,80,4);for(let i=-36;i<40;i+=8)ctx.fillRect(i,-4,2,8);ctx.restore();});
 else if(it==='wagen')hold(0,0,()=>{ctx.strokeStyle='#c8ced6';ctx.strokeRect(8,-7,16,14);['#ff9ab0','#9ed8ff','#ffe08a','#b9f0c0'].forEach((c,i)=>{ctx.fillStyle=c;circle(12+(i%2)*7,-3+Math.floor(i/2)*6,3);});});
 else if(it==='tuba')hold(0,0,()=>{ctx.strokeStyle='#e8c040';ctx.lineWidth=2.4;ctx.beginPath();ctx.arc(4,6,6,0,6.283);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#e8c040';circle(10,10,4);});
 else if(it==='kaktus')hold(0,0,()=>{ctx.strokeStyle='#c0392b';ctx.beginPath();ctx.moveTo(4,4);ctx.lineTo(22,4);ctx.stroke();ctx.fillStyle='#3f8a3a';ctx.beginPath();ctx.ellipse(26,4,5,4,0,0,6.283);ctx.fill();ctx.fillStyle='#fff';[[24,1],[28,2],[26,7]].forEach(q=>ctx.fillRect(q[0],q[1],1,1));});
 else if(it==='karte')hold(0,0,()=>{ctx.fillStyle='#f4efe0';ctx.fillRect(6,-10,10,20);ctx.strokeStyle='#c0392b';ctx.beginPath();ctx.moveTo(8,-6);ctx.lineTo(14,2);ctx.lineTo(9,6);ctx.stroke();});
 else if(it==='surf')hold(0,0,()=>{ctx.fillStyle='#5ff0ff';ctx.beginPath();ctx.ellipse(0,9,14,3.4,0,0,6.283);ctx.fill();ctx.fillStyle='#ff5fd0';ctx.fillRect(-2,6,4,6);});
 else if(it==='pizza')hold(0,0,()=>{ctx.fillStyle='#d9a560';ctx.fillRect(6,-6,12,12);ctx.fillStyle='#c0392b';ctx.fillRect(8,-1,8,2);});
 else if(it==='ski')hold(0,0,()=>{ctx.fillStyle='#e5504d';ctx.fillRect(-10,-4,24,2);ctx.fillRect(-10,2,24,2);});
 else if(it==='rad2')hold(0,0,()=>{ctx.strokeStyle='#222';ctx.lineWidth=1.6;for(let k=0;k<3;k++){ctx.beginPath();ctx.arc(10+k*2,8-k*4,3.4,0,6.283);ctx.arc(24+k*2,8-k*4,3.4,0,6.283);ctx.stroke();}ctx.lineWidth=1;});
 if(b.st==='stop'&&e.m==='sit'){ctx.fillStyle='#fff2b0';ctx.font='bold 12px Arial';ctx.textAlign='center';ctx.fillText('…',x,y-24);ctx.textAlign='start';}
}
function P0fig(x,y,a,w,walk){w=w||{dress:'#888',hair:'#444'};fig(x,y,a,{dress:w.dress,hair:w.hair,hairLen:w.hairLen,beard:w.beard,sk:5,walk:walk});}
const QSK={asche:1,schuh:1,spiegel:1,mammut:1,ente:1,kueken:1,alien:1,ufo:1};
function qMaerchen(z){
 const f=freeSpot(15*TS,24*TS);z.ska.push({k:'asche',x:f.x,y:f.y,hx:f.x,hy:f.y,a:0,walk:0,steer:2,say:rf(3,7),cd:0});
 const s=freeSpot(28*TS,8*TS);z.ska.push({k:'spiegel',x:s.x,y:s.y,a:0,walk:0,cd:0});
}
function qBerge(z){const f=freeSpot(30*TS,20*TS);z.ska.push({k:'mammut',x:f.x,y:f.y,hx:f.x,hy:f.y,a:0,walk:0,steer:2,say:rf(3,7),cd:0});}
function qEvent(){
 const sp=skSpawn();if(!sp)return false;
 const k=pick(['ente','alien','schuh'].filter(q=>q!==SKL&&!(q==='schuh'&&(G.schuh||G.ball))));
 if(!k)return false;SKL=k;
 if(k==='ente'){
  const a=sp.a;SKC.push({k:'ente',x:sp.x,y:sp.y,a:a,walk:0,lead:true,life:70,steer:3,say:2});
  for(let i=1;i<=4;i++)SKC.push({k:'kueken',i:i,x:sp.x-Math.cos(a)*i*14,y:sp.y-Math.sin(a)*i*14,a:a,walk:0});
  toast('Eine Entenmama mit vier Küken watschelt durch Rheinhanfen. Alle bleiben stehen und schauen zu.');
 }else if(k==='alien'){
  SKC.push({k:'ufo',x:sp.x,y:sp.y,a:0,walk:0,fly:0});
  const f=freeSpot(sp.x+30,sp.y+10);SKC.push({k:'alien',x:f.x,y:f.y,a:0,walk:0,lead:true,life:140,say:2,cd:0});
  toast('Rumms! Ein kleines Ufo ist notgelandet. Daneben steht jemand Grünes und kratzt sich am Kopf.');
 }else{
  SKC.push({k:'schuh',x:sp.x,y:sp.y,a:0,walk:0,lead:true,life:150});
  toast('Auf dem Gehweg funkelt etwas: ein gläserner Schuh! Wem der wohl gehört?');
 }
 sfx('arrive');return true;
}
function qPrompt(d){
 const k=d.k;
 return k==='asche'?'OK: Aschenputtel ansprechen':k==='schuh'?'OK: Gläsernen Schuh aufheben':k==='spiegel'?'OK: Zauberspiegel befragen':k==='mammut'?'OK: Mammut Mampfred ansprechen':k==='ente'?'OK: Entenmama begrüßen':k==='kueken'?'OK: Entenfamilie begrüßen':k==='alien'?'OK: Außerirdischen ansprechen':k==='ufo'?'OK: Ufo und Außerirdischen ansehen':'';
}
function qOpen(d){
 const k=d.k;UI.qd=d;
 if(k==='schuh'){G.schuh=1;SKC.length=0;sfx('magic');toast('Du hebst den gläsernen Schuh vorsichtig auf. Er ist winzig und glitzert. Im Märchenwald sucht ihn bestimmt jemand.');return;}
 if(k==='kueken'){addFx(d.x,d.y-12,'Piep!','#ffe08a',1);const m=skl().find(q=>q.k==='ente');if(m){qOpen(m);return;}mood(3,'+3 Piep');sfx('aww');toast('Das Küken piept dich an und rennt dann schnell hinter Mama her.');return;}
 if(k==='ufo'){const al=skl().find(q=>q.k==='alien'&&!q.board);if(al&&!d.fly){qOpen(al);return;}toast(d.fly>0?'Das Ufo hebt ab!':'Das Ufo qualmt ein bisschen. Auf der Seite steht: „Made in Krümel“.');return;}
 if(k==='ente'){mdl('Entenmama Quaktrud','Die Entenmama bleibt stehen, die vier Küken purzeln hintereinander gegen sie. „Quak!“',[['Weg frei machen','qx:en:weg'],['Brot anbieten','qx:en:brot'],['Erbsen anbieten','qx:en:erbs']]);return;}
 if(k==='alien'){const n=(G.ammo&&G.ammo.dose)||0;mdl('Blubb vom Planeten Krümel','„Blubb! Hallo, Erdling. Mein Ufo braucht Alu. Ihr nennt es Dose. Zehn Stück, und ich kann heim.“ Er zeigt auf eine Delle. Und auf deine Taschen.',[['10 Dosen für das Ufo geben ('+n+' dabei)','qx:al:dose',n<10],['Ihm Rheinhanfen erklären','qx:al:erkl'],['Fragen, wie es da oben ist','qx:al:oben']]);return;}
 if(k==='asche'){mdl('Aschenputtel','Aschenputtel sortiert Linsen, zwei Tauben helfen. „Die guten ins Töpfchen, die schlechten ins Kröpfchen.“'+(G.schuh?' Sie schaut auf deine Hände und strahlt.':''),[['Beim Linsensortieren helfen','qx:as:linse'],[G.schuh?'Den gläsernen Schuh zurückgeben':'Fragen, was ihr fehlt','qx:as:schuh'],['Über die Stiefschwestern plaudern','qx:as:plausch']]);return;}
 if(k==='spiegel'){mdl('Der Zauberspiegel','In einem goldenen Rahmen erscheint ein Gesicht mit hochgezogener Augenbraue. „Spieglein, Spieglein an der Wand? Ja, ja. Was willst du?“',[['Wer ist der Schönste im ganzen Land?','qx:sp:schoen'],['Sag mir was Nettes','qx:sp:nett'],['Bist du wirklich böse?','qx:sp:boese']]);return;}
 if(k==='mammut'){mdl('Mammut Mampfred','Ein Mammut, frisch aus dem Eis getaut. Es zittert, niest und hat einen Eiszapfen am Rüssel. „Wie lange hab ich geschlafen?“',[['Glühwein anbieten ('+((G.stock&&G.stock.gluehwein)||0)+')','qx:ma:glue',!(G.stock&&G.stock.gluehwein>0)],['Kuscheln und wärmen','qx:ma:kuschel'],['Erzählen, was es Neues gibt','qx:ma:news']]);return;}
}
function skAct18(p){
 if(p.indexOf('qx:')!==0)return false;
 const a=p.split(':'),w=a[1],o=a[2],d=UI.qd;
 if(w==='en'){
  if(o==='weg'){mood(5,'+5');G.hero=(G.hero||0)+.3;popAdd(1);toast('Du hältst die Hand hoch wie ein Schülerlotse. Die Autos warten, die Entenfamilie watschelt sicher rüber. Applaus vom Gehweg!');}
  else if(o==='brot'){toast('Die Entenmama schüttelt den Kopf. Stimmt: Brot ist für Enten ungesund, es quillt im Bauch auf.');}
  else{mood(6,'+6');sfx('aww');toast('Erbsen! Die Küken flippen aus vor Freude. Aufgetaute Erbsen sind für Enten ein Festmahl.');}
  return true;
 }
 if(w==='al'){
  if(o==='dose'){
   if(((G.ammo&&G.ammo.dose)||0)<10){toast('Dafür brauchst du zehn Dosen.');return true;}
   G.ammo.dose-=10;const r=120;G.cash+=r;G.stats.earned+=r;G.hero=(G.hero||0)+1;popAdd(3);xpAdd(25);mood(10,'+10 Blubb!');sfx('magic');
   const u=SKC.find(q=>q.k==='ufo');if(u)u.fly=.01;const al=SKC.find(q=>q.k==='alien');if(al){al.board=1;}
   toast('Blubb klopft die Dosen ans Ufo. Es piept, blinkt und schwebt! Zum Dank gibt er dir einen Krümel-Kristall, den der Pfandautomat für 120 € nimmt. „Blubb!“');
  }else if(o==='erkl'){mood(4,'+4');toast('Du erklärst Rheinhanfen: Apotheke, Pfand, Miesepeter, Gallier. Blubb macht sich Notizen. „Und ihr nennt das normal?“');}
  else{mood(3,'+3');toast('„Da oben ist es ruhig. Keiner hupt, keiner hat Montag. Aber es gibt keine Currywurst.“ Er seufzt sehr außerirdisch.');}
  return true;
 }
 if(w==='as'){
  if(o==='linse'){mood(6,'+6');sfx('magic');if(d)for(let i=0;i<6;i++)FX.push({x:d.x+rf(-20,20),y:d.y-10,vx:rf(-30,30),vy:rf(-40,-10),t:0,life:1,dot:'#f4f4f4',r:2});toast('Du sortierst mit. Die Tauben picken die schlechten raus, du die guten. Nach einer Minute ist alles fertig. Aschenputtel klatscht in die Hände.');}
  else if(o==='schuh'){
   if(G.schuh){G.schuh=0;G.ball=1;G.cash+=50;G.stats.earned+=50;G.hero=(G.hero||0)+1;popAdd(2);xpAdd(20);mood(15,'+15 Märchen');sfx('win');toast('„Mein Schuh! Den hab ich auf der Schlosstreppe verloren, typisch Mitternacht.“ Sie gibt dir 50 € Finderlohn und eine Einladung zum Ball.');}
   else toast('„Ich habe einen gläsernen Schuh verloren. Wenn du ihn in Rheinhanfen findest, bring ihn mir bitte!“');
  }else{mood(3,'+3');toast(pick(['„Meine Stiefschwestern haben gestern versucht, Linsen zu sortieren. Jetzt sind die Linsen beleidigt.“','„Die Stiefschwestern wollten in meinen Schuh. Er hat Nein gesagt.“']));}
  return true;
 }
 if(w==='sp'){
  mood(3,'+3');
  if(o==='schoen'){
   const L=[];
   if((G.drunk||0)>=2)L.push('„Du jedenfalls nicht, du schielst ja.“');
   if((G.hun||80)<30)L.push('„Iss erst mal was. Hungrig ist niemand schön.“');
   if((G.high||0)>30)L.push('„Du? Du lächelst seit zehn Minuten eine Laterne an.“');
   if(G.mood>=80)L.push('„Heute du. Mit dem Grinsen. Aber sag es nicht weiter.“');
   L.push('„Ich. Ich bin ein Spiegel, ich sehe mich die ganze Zeit.“','„Hinter den sieben Bergen gibt es eine, die ist schöner. Aber die hat keinen Lieferdienst.“','„Der Gartenzwerg in der Ecke. Fünf Punkte für die Mütze.“');
   toast(pick(L));
  }else if(o==='nett')toast(pick(['„Deine Schuhe passen gut zu ... deinen anderen Schuhen.“','„Du hast heute fast gar nichts falsch gemacht.“','„Von hinten siehst du aus wie jemand Berühmtes.“']));
  else toast(pick(['„Böse? Ich bin nur ehrlich. Das ist für die meisten dasselbe.“','„Nur montags. Und wenn jemand mit fettigen Fingern auf mich tippt.“']));
  return true;
 }
 if(w==='ma'){
  if(o==='glue'){if(!(G.stock&&G.stock.gluehwein>0)){toast('Du hast keinen Glühwein dabei.');return true;}G.stock.gluehwein--;mood(8,'+8');sfx('glug');toast('Mampfred schlürft den Glühwein mit dem Rüssel. Der Eiszapfen schmilzt. „Jetzt fühl ich mich nur noch wie zehntausend!“');}
  else if(o==='kuschel'){mood(10,'+10 Kuschel');sfx('aww');toast('Du kuschelst dich ins Mammutfell. Es ist warm, riecht nach Heu und ein bisschen nach Steinzeit.');}
  else{mood(4,'+4');toast(pick(['Du erzählst vom Handy. Mampfred fragt, ob man damit Mammuts anrufen kann. Du sagst: noch nicht.','Du erzählst von der Heizung. Mampfred weint ein bisschen vor Rührung.']));}
  return true;
 }
 return false;
}
function qUpdate(dt){
 const L=skl();if(!L.length)return;
 const say=(d,arr,col)=>{d.say=(d.say||0)-dt;if(d.say<=0){d.say=rf(6,11);if(Math.hypot(d.x-P.x,d.y-P.y)<320)addFx(d.x,d.y-28,pick(arr),col||'#fff2b0',1.8);}};
 let prev=null;
 L.forEach(d=>{
  if(!QSK[d.k])return;
  if(d.k==='asche'){leash(d,d.hx,d.hy,70);steerStep(d,dt,14);say(d,['Die guten ins Töpfchen ...','Wo ist nur mein Schuh?','Danke, ihr Tauben!']);}
  else if(d.k==='mammut'){leash(d,d.hx,d.hy,150);steerStep(d,dt,16);say(d,['Hatschi!','Brrr, kalt!','Mampf.'],'#cfe0ff');}
  else if(d.k==='spiegel'){if(Math.hypot(d.x-P.x,d.y-P.y)<200)say(d,['Na?','Ich seh dich.','Spieglein, Spieglein ... ja, ja.'],'#ffe08a');}
  else if(d.k==='ente'){steerStep(d,dt,30);d.walk+=dt*4;say(d,['Quak!','Quak, quak!'],'#ffe08a');prev=d;}
  else if(d.k==='kueken'){const t=L.find(q=>(q.k==='kueken'&&q.i===d.i-1)||(d.i===1&&q.k==='ente'));if(t){const dx=t.x-d.x,dy=t.y-d.y,l=Math.hypot(dx,dy);if(l>13){d.x+=dx/l*Math.min(l-13,60*dt);d.y+=dy/l*Math.min(l-13,60*dt);d.a=Math.atan2(dy,dx);d.walk+=dt*10;}}}
  else if(d.k==='alien'){if(d.board){const u=L.find(q=>q.k==='ufo');if(u){const dx=u.x-d.x,dy=u.y-d.y,l=Math.hypot(dx,dy);if(l>4){d.x+=dx/l*60*dt;d.y+=dy/l*60*dt;}else d.gone=1;}}else{if(Math.hypot(P.x-d.x,P.y-d.y)<160)d.a=Math.atan2(P.y-d.y,P.x-d.x);say(d,['Blubb?','Hat jemand Alu?','Ihr habt hier komische Bänke.'],'#b8ffb0');}}
  else if(d.k==='ufo'){if(d.fly>0){const al=L.find(q=>q.k==='alien');if(!al||al.gone){d.fly+=dt;if(d.fly>3.2){const i=SKC.indexOf(d);SKC.length=0;}}}}
 });
}
function qDraw(d){
 const k=d.k;
 if(k==='schuh'){const g=.3+.2*Math.sin(timeNow*5);ctx.fillStyle='rgba(180,230,255,'+g+')';circle(d.x,d.y,12);ctx.fillStyle='rgba(220,245,255,.9)';ctx.beginPath();ctx.ellipse(d.x,d.y,7,3,0,0,6.283);ctx.fill();ctx.fillStyle='rgba(160,210,255,.9)';ctx.fillRect(d.x+3,d.y-1,2,5);ctx.fillStyle='#fff';circle(d.x-3,d.y-1,1);return;}
 if(k==='asche'){fig(d.x,d.y,d.a,{dress:'#8a7a6a',apron:'#c8b8a0',hair:'#e8c87a',hairLen:5,hat:'#6a5a4a',brim:3.6,sk:5,walk:d.walk});ctx.fillStyle='#5a4a3a';[[-3,-2],[2,3]].forEach(q=>ctx.fillRect(d.x+q[0],d.y+q[1],2,2));for(let i=0;i<2;i++){const a=timeNow*1.3+i*3,x=d.x+Math.cos(a)*16,y=d.y+Math.sin(a)*10;ctx.fillStyle='#f4f4f4';ctx.beginPath();ctx.ellipse(x,y,4,2.6,a,0,6.283);ctx.fill();}xnTagQ(d,'Aschenputtel',24);return;}
 if(k==='spiegel'){ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(d.x+3,d.y+14,14,5,0,0,6.283);ctx.fill();ctx.fillStyle='#d8a838';ctx.beginPath();ctx.ellipse(d.x,d.y-10,14,19,0,0,6.283);ctx.fill();ctx.fillStyle='#bfe0f0';ctx.beginPath();ctx.ellipse(d.x,d.y-10,10,15,0,0,6.283);ctx.fill();const n=Math.hypot(d.x-P.x,d.y-P.y)<200;if(n){ctx.fillStyle='rgba(60,40,90,.7)';circle(d.x-4,d.y-14,1.8);circle(d.x+4,d.y-14,1.8);ctx.strokeStyle='rgba(60,40,90,.7)';ctx.beginPath();ctx.moveTo(d.x-6,d.y-18);ctx.lineTo(d.x-2,d.y-17);ctx.moveTo(d.x+2,d.y-19);ctx.lineTo(d.x+6,d.y-17);ctx.stroke();ctx.beginPath();ctx.arc(d.x,d.y-6,4,.2,2.9);ctx.stroke();}ctx.fillStyle='#ffd23f';circle(d.x,d.y-30,2.6);xnTagQ(d,'Zauberspiegel',38);return;}
 if(k==='mammut'){ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+3,d.y+8,22,10,0,0,6.283);ctx.fill();ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.fillStyle='#6a4a2a';[[-10,-9],[-10,9],[8,-9],[8,9]].forEach(q=>circle(q[0]+Math.sin(d.walk+q[0])*1.5,q[1],4));ctx.fillStyle='#8a5a32';ctx.beginPath();ctx.ellipse(0,0,18,12,0,0,6.283);ctx.fill();ctx.fillStyle='#9a6a3a';for(let i=0;i<8;i++)circle(-12+i*3.4,(i%2?-6:5),3.4);ctx.fillStyle='#7a4a2a';circle(16,0,8);ctx.strokeStyle='#f4efe0';ctx.lineWidth=2.4;ctx.beginPath();ctx.arc(20,-6,7,1.2,2.6);ctx.stroke();ctx.beginPath();ctx.arc(20,6,7,-2.6,-1.2);ctx.stroke();ctx.strokeStyle='#7a4a2a';ctx.lineWidth=3.4;ctx.beginPath();ctx.moveTo(22,0);ctx.quadraticCurveTo(30,Math.sin(timeNow*2)*5,27,8);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#cfefff';ctx.beginPath();ctx.moveTo(27,8);ctx.lineTo(28,15);ctx.lineTo(26,8);ctx.fill();ctx.restore();xnTagQ(d,'Mammut Mampfred',30);return;}
 if(k==='ente'||k==='kueken'){const s=k==='ente'?1:.55,w=Math.sin(d.walk*2)*.25;ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a+w);ctx.scale(s,s);ctx.fillStyle='rgba(0,0,0,.2)';ctx.beginPath();ctx.ellipse(1,3,9,5,0,0,6.283);ctx.fill();ctx.fillStyle=k==='ente'?'#a8865a':'#ffe08a';ctx.beginPath();ctx.ellipse(0,0,8,5.4,0,0,6.283);ctx.fill();ctx.fillStyle=k==='ente'?'#8a6a3a':'#ffd23f';ctx.beginPath();ctx.ellipse(-1,0,5,3.4,0,0,6.283);ctx.fill();ctx.fillStyle=k==='ente'?'#a8865a':'#ffe08a';circle(7,0,3.6);ctx.fillStyle='#ff9a3c';ctx.beginPath();ctx.ellipse(11,0,2.6,1.6,0,0,6.283);ctx.fill();ctx.fillStyle='#222';circle(8,-1.6,.8);circle(8,1.6,.8);ctx.restore();if(k==='ente')xnTagQ(d,'Entenmama Quaktrud',18);return;}
 if(k==='alien'){if(d.gone)return;fig(d.x,d.y,d.a,{dress:'#5ad85a',hair:'#3fae3f',skin:'#8aff8a',sk:4.6,walk:d.walk});ctx.strokeStyle='#3fae3f';ctx.beginPath();ctx.moveTo(d.x-2,d.y-3);ctx.lineTo(d.x-6,d.y-12);ctx.moveTo(d.x+2,d.y-3);ctx.lineTo(d.x+6,d.y-12);ctx.stroke();ctx.fillStyle='#ff5fd0';circle(d.x-6,d.y-12,1.8);circle(d.x+6,d.y-12,1.8);xnTagQ(d,'Blubb vom Planeten Krümel',24);return;}
 if(k==='ufo'){const h=d.fly>0?d.fly*d.fly*40:0,sc=1+(d.fly>0?d.fly*.1:0);ctx.fillStyle='rgba(0,0,0,'+Math.max(0,.3-h/400)+')';ctx.beginPath();ctx.ellipse(d.x+4,d.y+10,22,8,0,0,6.283);ctx.fill();ctx.save();ctx.translate(d.x,d.y-h);ctx.scale(sc,sc);ctx.fillStyle='#9aa3ad';ctx.beginPath();ctx.ellipse(0,0,22,9,0,0,6.283);ctx.fill();ctx.fillStyle='#7ae0ff';ctx.beginPath();ctx.ellipse(0,-4,10,7,0,Math.PI,0);ctx.fill();for(let i=0;i<5;i++){ctx.fillStyle=Math.floor(timeNow*6+i)%2?'#ffd23f':'#ff5fd0';circle(-16+i*8,2,1.8);}ctx.restore();if(!d.fly&&chance(.06))FX.push({x:d.x+rf(-8,8),y:d.y-6,vx:rf(-6,6),vy:rf(-20,-8),t:0,life:1,dot:'rgba(160,160,160,.6)',r:rf(2,4)});return;}
}
let xqF=-1,xqD=null;
function xnTagQ(d,n,off){if(xqF!==timeNow){xqF=timeNow;let b=null,bd=110;skl().forEach(q=>{if(!QSK[q.k]||q.k==='kueken'||q.k==='ufo'||q.k==='schuh')return;const dd=Math.hypot(q.x-P.x,q.y-P.y);if(dd<bd){bd=dd;b=q;}});xqD=b;}if(xqD!==d)return;ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-off);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-off);ctx.lineWidth=1;ctx.textAlign='start';}

const HOMES={
 imbiss:{n:'Feldbett im Imbiss-Lager',s:'Imbiss-Lager',r:0,lv:1,m:4,f:0,h:0,d:'Zwischen Frittenkisten und Ketchup-Kanistern. Gratis, aber die Fritteuse brummt die ganze Nacht.'},
 wg:{n:'WG-Zimmer bei Ole und Paula',s:'WG-Zimmer',r:60,lv:1,m:14,f:25,h:0,d:'Ole beschriftet alles im Kühlschrank, Paula singt unter der Dusche. Manchmal gibt es Frühstück für alle.'},
 camp:{n:'Dauerplatz auf Camping Tulpenwiese',s:'Camping Tulpenwiese',r:35,lv:1,m:18,f:20,h:-4,d:'Käse-Wohnwagen „Gouda“ mit Vorzelt und Gartenzwerg, in Holland. Hin geht es über die Europa-Karte.'},
 altbau:{n:'Altbauwohnung mit Balkon',s:'Altbauwohnung',r:150,lv:2,m:22,f:45,h:-2,d:'Hohe Decken, knarzende Dielen und ein Balkon mit Blick auf die Gracht. Frühstück aus dem eigenen Kühlschrank.'},
 loft:{n:'Loft am Hafen',s:'Loft am Hafen',r:300,lv:4,m:28,f:65,h:-6,d:'Backsteinwände, Riesenfenster und eine Feuerwehrstange statt Treppe. Hier findet dich so schnell keiner.'},
 pent:{n:'Penthouse am Rhein',s:'Penthouse',r:700,lv:6,m:40,f:100,h:-10,d:'Dachterrasse, Whirlpool und eine Möwe, die sich für den Hausmeister hält. Mehr Luxus gibt es in Rheinhanfen nicht.'}
};
const HORD=['wg','camp','altbau','loft','pent'];
const HANEK={
 imbiss:['Hanfred schnarcht im Nebenraum wie eine Fritteuse auf Stufe drei.','Du wachst mit dem Gesicht auf einer Pommesgabel auf. Sie war bequemer als gedacht.','Ein Ketchup-Kanister ist umgefallen. Es sieht schlimm aus, riecht aber nach Grillparty.','Eine Maus hat sich eine Fritte geholt und winkt dir zum Abschied.'],
 wg:['Ole hat einen Zettel an deine Tür geklebt: „Wer hat meinen Joghurt gegessen?“ Darunter Paula: „Der Joghurt selbst. Er war sehr alt.“','Paula singt unter der Dusche eine Oper über Spülmaschinen. Ole klatscht.','Ole und Paula haben Frühstück gemacht: Rührei in Herzform, leicht angebrannt, sehr lecker.','Im Flur steht ein neuer Putzplan. Du bist für „Stimmung“ eingeteilt.'],
 camp:['Herbert mäht um sieben Uhr seinen Rasen. Mit der Nagelschere.','Eine Ente sitzt auf deinem Vorzelt und quakt den Sonnenaufgang an.','Oma Truus klopft ans Fenster und bringt Brötchen: „Lekker!“','Dein Gartenzwerg steht heute anders herum. Niemand weiß, warum.'],
 altbau:['Die Nachbarin über dir übt Tuba. Um sechs Uhr. Es klingt wie ein trauriger Elefant.','Die Dielen knarzen so laut, dass du dich in Zeitlupe zum Kühlschrank schleichst.','Auf dem Balkon sitzt eine Taube und schaut dich an, als würdest du bei ihr wohnen.'],
 loft:['Du rutschst die Feuerwehrstange runter zum Frühstück. Bester Start in den Tag!','Die Morgensonne knallt durch die Riesenfenster. Kein Vorhang der Welt ist so groß.','Ein Containerschiff tutet vor dem Fenster. Du tutest zurück.'],
 pent:['Die Möwe sitzt im Whirlpool und guckt dich vorwurfsvoll an. Es ist jetzt ihr Whirlpool.','Der Butler-Roboter bringt Kaffee und verbeugt sich so tief, dass er umkippt.','Von der Dachterrasse siehst du bis nach Holland. Fast.']
};
function homeK(){return(G&&G.home&&HOMES[G.home])?G.home:'imbiss';}
function homeShort(){return HOMES[homeK()].s;}
function homeDay(L){
 const k=homeK();if(k==='imbiss')return;
 const h=HOMES[k];
 if(G.cash>=h.r){G.cash-=h.r;L.push('Miete für '+h.s+': '+eur(h.r)+'.');}
 else{G.home='imbiss';popAdd(-2);L.push('Die Miete für '+h.s+' fehlt. Der Vermieter schließt freundlich, aber bestimmt ab. Du schläfst wieder im Imbiss-Lager.');}
}
function homeWake(k){
 const h=HOMES[k],L=[];
 mood(h.m,'+'+h.m+' ausgeschlafen');
 if(h.f)needAdd(h.f,h.f);
 if(h.h)heat(h.h);
 L.push(pick(HANEK[k]));
 if(k==='camp'&&G.broet){G.broet=0;needAdd(30,30);L.push('Die bestellten Brötchen hängen in einer Tüte an deinem Vorzelt. Lekker!');}
 else if(h.f)L.push(k==='camp'?'Frühstück vor dem Vorzelt: Brötchen und Kakao.':'Frühstück zu Hause: Essen und Trinken sind wieder gut gefüllt.');
 G.duschT=0;
 return L;
}
function kSleep(k,title,extra){
 if(wanted>0){toast('Erst die Polizei abschütteln, dann schlafen.');return;}
 if(P.ride)leaveRide(true);
 P.coast=null;
 const L=sleepTo(6,true);
 const W=homeWake(k);
 saveAll();UI.screen=null;
 showModal({title:title||'Guten Morgen',text:'Tag '+G.day+', 06:00 Uhr. '+(extra||'Du hast gut geschlafen, die Fahndung sinkt.'),lines:W.concat(L),choices:[{label:'Weiter',a:'mclose'}]});
}
function homeMenu(){
 const k=homeK(),h=HOMES[k],ch=[];
 let t;
 if(k==='imbiss')t='Frau Schlüsselbund von der Hausverwaltung rückt ihre Brille zurecht: „Sie wohnen im Imbiss? Zwischen den Fritten? Da hab ich was Besseres für Sie!“';
 else if(k==='camp')t='Frau Schlüsselbund: „Sie wohnen auf einem Campingplatz in Holland? Mutig! Falls Sie mal ein Dach ohne Reißverschluss wollen …“';
 else t='Willkommen zu Hause! Du wohnst im Haus Wohnglück: '+h.n+'. Miete: '+eur(h.r)+' pro Tag, sie wird jeden Morgen abgebucht.';
 if(k!=='imbiss'&&k!=='camp'){
  ch.push(['Hacker-PC','yk:mi:pc'],['Schlafen bis zum Morgen','yk:ho:sleep'],[k==='pent'?'Duschen und ab in den Whirlpool':'Duschen','yk:ho:dusch'],['Pflanzen-Cam','yk:ho:grow'],['Wohnung wechseln','yk:ho:list']);
 }else ch.push(['Wohnungen ansehen','yk:ho:list']);
 if(k!=='imbiss')ch.push(['Kündigen und zurück ins Imbiss-Lager','yk:ho:quit']);
 mdl('Haus Wohnglück',t,ch);
}
function homesScreen(){
 const k0=homeK(),lv=G.lvl||1;let b='',df=false;
 HORD.forEach(k=>{
  const h=HOMES[k],cur=k===k0,lock=lv<h.lv,need=h.r*2,poor=G.cash<need,off=cur||lock||poor;
  b+=btn((cur?'✓ ':'')+h.n+': '+eur(h.r)+' pro Tag','homeTake',k,{off:off,def:!off&&!df,why:cur?'Hier wohnst du schon.':lock?'Erst ab Stufe '+h.lv+'. Du bist auf Stufe '+lv+'.':'Zum Einzug brauchst du '+eur(need)+' (zwei Tagesmieten).',note:h.d});
  if(!off)df=true;
 });
 b+=btn('Zurück','back',null,{def:!df});
 return{hint:'Pfeiltasten: wählen · OK: einziehen · Zurück: schließen',html:'<div class="place" style="max-width:46rem"><div class="hd"><h2>Hausverwaltung Wohnglück</h2><div class="mu">Jetzt: <b>'+HOMES[k0].n+'</b> · Bargeld <b class="gr">'+eur(G.cash)+'</b> · Stufe '+lv+'</div><div class="mu">Einzug kostet zwei Tagesmieten. Danach wird die Miete jeden Morgen abgebucht. Ohne Geld geht es zurück ins Imbiss-Lager.</div></div>'+b+'</div>'};
}
function homeTake(k){
 const h=HOMES[k];if(!h||k==='imbiss')return{ok:false};
 if(homeK()===k)return{ok:false,msg:'Hier wohnst du schon.'};
 if((G.lvl||1)<h.lv)return{ok:false,msg:'Erst ab Stufe '+h.lv+'.'};
 if(G.cash<h.r*2)return{ok:false,msg:'Zum Einzug fehlen dir '+eur(h.r*2-G.cash)+'.'};
 G.cash-=h.r*2;G.home=k;popAdd(2);xpAdd(12);sfx('win');
 return{ok:true,msg:k==='camp'?'Dein Dauerplatz auf der Tulpenwiese gehört dir: Käse-Wohnwagen Gouda mit Vorzelt. Hin geht es über die Europa-Karte.':'Schlüssel abgeholt! Du wohnst jetzt im '+h.n+'. Schlafen kannst du ab sofort hier im Haus Wohnglück.'};
}
function kEll(H,cx,cy,rx,ry,v){for(let j=Math.floor(cy-ry)-1;j<=cy+ry+1;j++)for(let i=Math.floor(cx-rx)-1;i<=cx+rx+1;i++){const dx=(i-cx)/rx,dy=(j-cy)/ry;if(dx*dx+dy*dy<=1)H.zs(i,j,v);}}
function kAng(a,b){let d=a-b;while(d>Math.PI)d-=6.2832;while(d<-Math.PI)d+=6.2832;return d;}
function kpBuild(pts){const p=pts.map(q=>[q[0]*TS,q[1]*TS]);const seg=[];let L=0;for(let i=0;i<p.length-1;i++){const a=p[i],b=p[i+1],l=Math.max(1,Math.hypot(b[0]-a[0],b[1]-a[1]));seg.push({a:a,b:b,l:l,s:L});L+=l;}return{seg:seg,L:L};}
function kpAt(pa,s){s=clamp(s,0,pa.L);for(let i=0;i<pa.seg.length;i++){const g=pa.seg[i];if(s<=g.s+g.l||i===pa.seg.length-1){const f=clamp((s-g.s)/g.l,0,1);return{x:g.a[0]+(g.b[0]-g.a[0])*f,y:g.a[1]+(g.b[1]-g.a[1])*f,a:Math.atan2(g.b[1]-g.a[1],g.b[0]-g.a[0]),i:i};}}return{x:0,y:0,a:0,i:0};}
function kpStart(o){
 if(fade&&!o.force)return;
 UI.screen=null;UI.modal=null;render2();
 if(P.ride)leaveRide(true);
 P.sit=null;P.vx=P.vy=0;keys.left=keys.right=keys.up=keys.down=0;MG=null;
 const pa=kpBuild(o.pts),q=kpAt(pa,0);
 P.coast={k:'kp',o:o,pa:pa,s:0,v:o.v0||100,t:0,i:0,la:q.a,gx:q.x,gy:q.y,h:0};
 P.x=q.x;P.y=q.y;P.a=q.a;
 sfx(o.snd||'ride');if(o.msg)toast(o.msg);
}
function kpTick(dt){
 const c=P.coast;if(!c||c.k!=='kp')return;
 const o=c.o;c.t+=dt;
 if(o.mode==='const')c.v=o.v0;
 else{let a=o.acc||0;if(o.ctl){if(keys.up)a+=(o.acc||0)*.7;if(keys.down)a=-320;}c.v=clamp(c.v+a*dt,o.vmin||40,o.vmax||420);}
 c.s+=c.v*dt;
 const q=kpAt(c.pa,c.s);
 if(q.i!==c.i){const da=Math.abs(kAng(q.a,c.la));if(o.curve&&da>.45){c.v*=Math.max(.6,1-da*(keys.down?.3:keys.up?.12:.2));if(chance(.7))addFx(q.x,q.y-24,pick(o.curve),'#ffd23f',.9);shake=Math.max(shake,.15);}c.i=q.i;}
 c.la=q.a;c.gx=q.x;c.gy=q.y;
 const h=o.hf?o.hf(Math.min(1,c.s/c.pa.L)):0;c.h=h;
 P.x=q.x;P.y=q.y-h;P.a=o.face!==undefined?o.face:q.a;
 if(o.trail&&c.v>120&&chance(dt*22))FX.push({x:q.x+rf(-5,5),y:q.y+rf(-5,5),vx:rf(-18,18),vy:rf(-18,4),t:0,life:.45,dot:o.trail,r:rf(1.5,3)});
 if(o.shout&&chance(dt*.9))addFx(P.x,P.y-24,pick(o.shout),'#ffd23f',.9);
 if(c.s>=c.pa.L){P.coast=null;P.x=q.x;P.y=q.y;if(o.end)o.end(c);}
}
function kSplash(x,y,n){sfx('splash');for(let i=0;i<n;i++)FX.push({x:x+rf(-6,6),y:y+rf(-4,4),vx:rf(-70,70),vy:rf(-120,-30),g:260,t:0,life:rf(.5,.9),dot:pick(['rgba(210,240,255,.95)','rgba(150,210,250,.9)','#fff']),r:rf(1.5,3.4)});}
const FBS=[
 {n:'Blitz-Rutsche',c:'#f1c40f',pts:[[6.2,4.2],[9.6,4.3],[12.8,5.6],[16.6,8.4]],v0:160,acc:360,vmax:540},
 {n:'Looping-Schlange',c:'#2e86c1',pts:[[4.6,6],[2.4,7.8],[6.4,9.4],[2.4,11.4],[5.4,13.8],[10,13.8],[12.6,12],[16.6,11.2]],v0:110,acc:210,vmax:420},
 {n:'Reifenrutsche',c:'#e5504d',pts:[[6,5.8],[9.4,7.4],[6.8,9.2],[9.8,11.2],[8.2,16],[11.6,17],[13.8,15],[16.6,13.6]],v0:90,acc:150,vmax:330}
];
const FBJ={1:22.6,3:23.6,5:24.6,10:25.6};
const FBRS=[['WUIII!','Schneller!','Huiii!'],['Kurve!','Schlangenlinie!','Mir wird schwindelig!'],['Quietsch!','Gummi-Ente voraus!','Juhu!']];
function genFreibad(z,H){
 const zs=H.zs,zg=H.zg,zf=H.zf,mk=H.mk,R=H.R;
 zf(0,0,ZW,ZH,SW);
 zf(0,0,12,18,GR);zf(0,18,ZW,12,GR);
 zf(14,6,20,10,SH);zf(15,7,18,8,DP);
 zf(36,7,9,6,SH);zs(40,9,BL);
 zf(3,3,3,3,BL);z.BLD.push({x:3,y:3,w:3,h:3,c:'#2fa3d6',n:'',k:'house',hh:7});
 zf(22,3,5,2,BL);
 zf(37,14,5,3,BL);z.BLD.push({x:37,y:14,w:5,h:3,c:'#e5604d',n:'POMMES',k:'house',hh:6});
 zs(34,11,BL);
 for(let i=0;i<16;i++){const x=R(2,44),y=R(20,28);if(zg(x,y)===GR&&zg(x+1,y)===GR&&Math.hypot(x-45,y-27)>3&&Math.hypot(x-2,y-16)>4){zs(x,y,UM);zs(x+1,y,LC);}}
 [[1,1],[10,1],[1,9],[10,16],[46,19],[13,28],[30,29]].forEach(q=>{if(zg(q[0],q[1])===GR)zs(q[0],q[1],TR);});
 {const m=mk('fbrutsch','sk',4,7,'Rutschenturm','Rutschen!');m.sk='fbrutsch';m.col='#5fd0ff';}
 {const m=mk('fbturm','sk',20,5,'Sprungturm','Sprungturm hochklettern');m.sk='fbturm';m.col='#5fd0ff';}
 mk('pommes','buedchen',39,17,'Pommes-Bude','Pommes-Bude besuchen');
 z.nogo={x0:0,y0:0,x1:ZW*TS,y1:ZH*TS,n:'das Freibad'};
 z.fbs=[];for(let i=0;i<6;i++)z.fbs.push({x:(16+i*2.6)*TS,y:(7.8+i*1.1)*TS,d:i%2?1:-1,sp:rf(26,46),col:pick(['#e5504d','#f1c40f','#2ecc71','#ff7fb0','#ffffff','#9b59b6']),w:0});
 z.kids=[[37.5,8.5],[39,10.6],[41.5,8.2],[43,11]].map(q=>({x:q[0]*TS,y:q[1]*TS,p:rf(0,6),col:pick(['#ff7fb0','#f1c40f','#5fd0ff','#7ad35a'])}));
 z.jury={t:0,sc:[0,0,0]};
}
function genCamping(z,H){
 const zs=H.zs,zg=H.zg,zf=H.zf,mk=H.mk;
 zf(0,0,ZW,ZH,GR);
 zf(1,9,46,2,SW);zf(24,11,2,18,SW);
 kEll(H,38,23,8.6,5,SH);kEll(H,38,23.4,6.6,3.6,DP);
 zf(3,3,6,4,BL);z.BLD.push({x:3,y:3,w:6,h:4,c:'#e07a3a',n:'REZEPTION',k:'house',hh:6});
 zf(11,3,5,3,BL);z.BLD.push({x:11,y:3,w:5,h:3,c:'#5a9ad6',n:'SANITÄR',k:'house',hh:5});
 zf(18,3,5,3,BL);z.BLD.push({x:18,y:3,w:5,h:3,c:'#e8c14a',n:'FRIETJE',k:'house',hh:5});
 zf(30,2,3,3,BL);
 z.cmp=[{t:'herb',x:5,y:12,w:4,h:2},{t:'gouda',x:12,y:12,w:3,h:2},{t:'iglu',x:18,y:12,w:2,h:2},{t:'tipi',x:4,y:20,w:2,h:2},{t:'tulpe',x:9,y:20,w:2,h:2},{t:'pyra',x:14,y:21,w:2,h:2},{t:'schuh',x:28,y:12,w:4,h:2},{t:'bus',x:34,y:12,w:3,h:2},{t:'burg',x:40,y:12,w:3,h:2}];
 z.cmp.forEach(o=>zf(o.x,o.y,o.w,o.h,BL));
 [[1,1],[2,16],[11,17],[21,16],[27,17],[45,17],[1,27],[20,28],[22,19],[46,1],[37,7],[15,8],[45,8]].forEach(q=>{if(zg(q[0],q[1])===GR)zs(q[0],q[1],TR);});
 {const m=mk('cmrez','sk',6,7,'Rezeption','Rezeption besuchen');m.sk='cmrez';m.col='#ffb347';}
 {const m=mk('cmsan','sk',13,6,'Sanitärhaus','Ins Sanitärhaus');m.sk='cmsan';m.col='#5fd0ff';}
 mk('frietje','buedchen',20,6,'Snackbar Frietje','Snackbar Frietje besuchen');
 {const m=mk('cmgouda','sk',13,14,'Käse-Wohnwagen Gouda','Zum Wohnwagen Gouda');m.sk='cmgouda';m.col='#ffd23f';}
 {const m=mk('cmplatz','sk',18,25,'Zeltwiese','Zeltwiese: Platz suchen');m.sk='cmplatz';m.col='#7ad35a';}
 {const m=mk('cmfeuer','sk',28,20,'Lagerfeuer','Ans Lagerfeuer setzen');m.sk='cmfeuer';m.col='#ff9a3c';}
 [[7,8],[8,8],[9,8]].forEach(q=>z.rides.push(mkRide('bike',q[0]*TS+16,q[1]*TS+16,0)));
 [[35,23],[40,24]].forEach(q=>z.rides.push(mkRide('boat',q[0]*TS+16,q[1]*TS+16,0)));
 z.nogo={x0:0,y0:0,x1:ZW*TS,y1:ZH*TS,n:'der Familien-Campingplatz'};
 z.wim={pop:0,t:rf(8,16)};z.ma=0;
}
const RODEL=[[44,5.5],[36,6.5],[30,8.5],[33,11],[40,12],[36,15],[30,16.5],[36,18],[43,18.2]];
const RODLIFT=[[45.6,19.2],[46.2,6.2],[44.4,5.5]];
function kLineTiles(H,pts,r,v,keep){for(let i=0;i<pts.length-1;i++){const a=pts[i],b=pts[i+1],n=Math.ceil(Math.hypot(b[0]-a[0],b[1]-a[1])*2);for(let k=0;k<=n;k++){const x=a[0]+(b[0]-a[0])*k/n,y=a[1]+(b[1]-a[1])*k/n;for(let j=Math.floor(y-r);j<=Math.floor(y+r);j++)for(let i2=Math.floor(x-r);i2<=Math.floor(x+r);i2++){const t=H.zg(i2,j);if(keep.indexOf(t)<0)H.zs(i2,j,v);}}}}
function kBerge(z,H){
 kLineTiles(H,RODEL,1,SN,[RK,BL,IC]);kLineTiles(H,RODLIFT,1,SN,[RK,BL,IC]);
 const m=H.mk('rodel','sk',45,20,'Rodelbahn Gamsblitz','Rodelbahn Gamsblitz');m.sk='rodel';m.col='#5fd0ff';
}
const SKIG=[[8.5,12.2],[13,14.6],[8,17],[12.5,19.4]];
const SKILIFT=[[11.5,21.4],[10.5,8.6]];
function kOesi(z,H){
 for(let x=0;x<=18;x++)for(let y=0;y<=21;y++){const t=H.zg(x,y);if(t!==RK&&t!==BL)H.zs(x,y,SN);}
 for(let y=0;y<=21;y++){const t=H.zg(19,y);if(t===TR)H.zs(19,y,GR);}
 const m=H.mk('lift','sk',12,22,'Sessellift Gipfelglück','Sessellift Gipfelglück');m.sk='lift';m.col='#5fd0ff';
}
const YK={herb:{n:'Dauercamper Herbert'},wim:{n:'Wurfzelt-Wim'},truus:{n:'Oma Truus'},bade:{n:'Bademeister Günni'},sepp:{n:'Skilehrer Sepp-Bert'}};
function kSka(z){
 if(z.name==='freibad'){z.ska=[{k:'bade',x:24*TS,y:16.6*TS,hx:24*TS,hy:16.6*TS,a:0,walk:0,steer:2,say:rf(3,6),cd:0}];}
 else if(z.name==='camping'){z.ska=[{k:'herb',x:7*TS,y:14.7*TS,a:Math.PI/2,walk:0,say:rf(3,6),cd:0},{k:'wim',x:21.5*TS,y:23.6*TS,hx:21.5*TS,hy:23.6*TS,a:0,walk:0,steer:2,say:rf(3,6),cd:0},{k:'truus',x:24.5*TS,y:16*TS,hx:24.5*TS,hy:18*TS,a:Math.PI/2,walk:0,steer:2,say:rf(4,8),cd:0}];}
}
function kSkaOesi(z){z.ska.push({k:'sepp',x:14*TS,y:22.5*TS,hx:14*TS,hy:22.5*TS,a:Math.PI,walk:0,steer:2,say:rf(3,6),cd:0});}
const YKS={
 herb:['Seit 31 Jahren derselbe Platz!','Udo, du stehst schief!','Hier ist Ruhezone. Ab 13 Uhr.','Das Wetter war früher besser.'],
 wim:['Hoi! Mein Zelt baut sich selbst auf!','Zusammenlegen? Seit Dienstag!','Wer kann Origami?'],
 truus:['Hoi! Ich bin 84!','Vierzig Kilometer vor dem Frühstück!','Mein Wohnwagen ist klein, aber fein!'],
 bade:['Nicht rennen!','Nicht vom Beckenrand springen!','Erst duschen, dann schwimmen!','Pfeif!'],
 sepp:['Pizza bremst, Pommes fährt!','Knie weich, Lächeln hart!','Servus! Ski Heil!']
};
function ykDraw(d){
 const k=d.k;
 if(MEDYK[k]){medYkDraw(d);return;}
 if(KEVK[k]){kEvDraw(d);return;}
 if(k==='ruebe')ruebeDraw(d);
 if(k==='herb'){
  ctx.fillStyle='#2e86c1';ctx.fillRect(d.x-8,d.y-6,16,13);ctx.fillStyle='#1f5f8a';ctx.fillRect(d.x-8,d.y-9,16,4);
  fig(d.x,d.y,d.a,{dress:'#e9e3d0',hair:'#c8c8c8',beard:'#9a9a9a',sk:5.6});
  ctx.fillStyle='#d63a3a';ctx.fillRect(d.x-12,d.y+2,3,6);ctx.fillStyle='#fff';circle(d.x-10.5,d.y+1,1.6);
 }else if(k==='wim'){
  fig(d.x,d.y,d.a,{dress:'#ff9a3c',hair:'#f4d03f',hairLen:2,sk:5,walk:d.walk});
 }else if(k==='truus'){
  const bx=d.x-Math.cos(d.a)*20,by=d.y-Math.sin(d.a)*20;
  ctx.fillStyle='#f4f0e6';ctx.save();ctx.translate(bx,by);ctx.rotate(d.a);ctx.fillRect(-9,-6,14,12);ctx.fillStyle='#8fd0ff';ctx.fillRect(-6,-4,4,3);ctx.fillStyle='#e5604d';ctx.fillRect(-9,-6,14,2);ctx.fillStyle='#222';ctx.fillRect(-3,-7,3,2);ctx.fillRect(-3,5,3,2);ctx.restore();
  ctx.strokeStyle='#555';ctx.beginPath();ctx.moveTo(bx,by);ctx.lineTo(d.x,d.y);ctx.stroke();
  ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.strokeStyle='#222';ctx.lineWidth=2;ctx.beginPath();ctx.arc(-8,0,4.5,0,6.283);ctx.stroke();ctx.beginPath();ctx.arc(8,0,4.5,0,6.283);ctx.stroke();ctx.strokeStyle='#2e86c1';ctx.beginPath();ctx.moveTo(-8,0);ctx.lineTo(8,0);ctx.stroke();ctx.lineWidth=1;ctx.restore();
  fig(d.x,d.y,d.a,{dress:'#9b59b6',hair:'#eeeeee',hairLen:3,sk:4.8,sc:.92});
 }else if(k==='bade'){
  fig(d.x,d.y,d.a,{dress:'#e5504d',hair:'#3a2a1a',sk:5.6,walk:d.walk});
  ctx.fillStyle='#f1c40f';circle(d.x+Math.cos(d.a)*6,d.y+Math.sin(d.a)*6,1.6);
 }else if(k==='sepp'){
  fig(d.x,d.y,d.a,{dress:'#d63a3a',hair:'#5a3a1a',hat:'#2e86c1',hat2:'#fff',brim:4.2,sk:5.2,walk:d.walk});
  ctx.strokeStyle='#888';ctx.beginPath();ctx.moveTo(d.x-8,d.y+4);ctx.lineTo(d.x-8,d.y-10);ctx.moveTo(d.x+8,d.y+4);ctx.lineTo(d.x+8,d.y-10);ctx.stroke();
 }
 if(Math.hypot(d.x-P.x,d.y-P.y)<110){const n=YK[k].n;ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-24);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-24);ctx.lineWidth=1;ctx.textAlign='start';}
}
function ykPrompt(d){const k=d.k;if(k==='rasa'||k==='astro')return 'OK: Zur Raumkapsel';if(k==='ratte'||k==='taube')return 'OK: Rattenfänger ansprechen';if(k==='moritz')return 'OK: Max und Moritz ansprechen';if(k==='maxm')return 'OK: Max und Moritz ansprechen';return 'OK: '+YK[k].n+' ansprechen';}
function ykOpen(d){
 const k=d.k;
 if(MEDYK[k]){medYkOpen(d);return;}
 if(KEVK[k]||k==='ruebe'){kEvOpen(d);return;}
 if(k==='herb')mdl('Dauercamper Herbert','Herbert sitzt im Klappstuhl vor seinem Wohnwagen, umringt von Gartenzwergen: „Seit 31 Jahren derselbe Platz. Die Zwerge sind meine Nachbarn. Der mit der Angel heißt Udo.“',[['Gartenzwerge zählen','yk:hb:zwerg'],['Eine Grillwurst schnorren','yk:hb:wurst'],['Übers Wetter meckern','yk:hb:wetter']]);
 else if(k==='wim')mdl('Wurfzelt-Wim','„Hoi! Mein Wurfzelt ist in zwei Sekunden aufgebaut. Das Zusammenlegen dauert seit Dienstag.“',[['Beim Zusammenlegen helfen','yk:wm:help'],['Das Zelt aufploppen lassen','yk:wm:pop']]);
 else if(k==='truus')mdl('Oma Truus','Oma Truus hält mit ihrem Fahrrad an. Hinten hängt ein Mini-Wohnwagen: „Ich bin 84 und fahre jeden Tag vierzig Kilometer. In Holland ist das normal.“',[['Ein Wettrennen vorschlagen','yk:tr:race'],['Nach dem Mini-Wohnwagen fragen','yk:tr:wagen']]);
 else if(k==='bade')mdl('Bademeister Günni','Günni schiebt die Sonnenbrille hoch und lässt die Trillerpfeife baumeln: „Hier wird nicht gerannt. Hier wird gerutscht, gesprungen und geplanscht. In dieser Reihenfolge.“',[['Seepferdchen-Prüfung ablegen','yk:bm:pferd'],['Nach dem Rutschen-Rekord fragen','yk:bm:rek'],['Gemeinsam pfeifen','yk:bm:pfeif']]);
 else if(k==='sepp')mdl('Skilehrer Sepp-Bert','„Servus! Merk dir zwei Wörter: Pizza heißt bremsen, Pommes heißt fahren. Mehr braucht kein Mensch.“ Mit dem Sessellift geht es hoch, oben warten Leih-Ski.',[['Pizza üben','yk:se:pizza'],['Pommes üben','yk:se:pommes'],['Nach meiner Bestzeit fragen','yk:se:rek']]);
}
function kTime(s){return s.toFixed(1).replace('.',',')+' s';}
function fbSlide(i){
 const f=FBS[i];
 kpStart({pts:f.pts,v0:f.v0,acc:f.acc,vmax:f.vmax,trail:'rgba(200,235,255,.9)',shout:FBRS[i],msg:f.n+': Arme verschränken, Beine zusammen und los!',end:c=>{
  kSplash(P.x,P.y,22);addFx(P.x,P.y-26,'PLATSCH!','#9fd8ff',1.4);
  G.rutsch=(G.rutsch||0)+1;mood(10,'+10 Rutschen');xpAdd(3);
  const t=c.t,rk='r'+i;G.fbRec=G.fbRec||{};const old=G.fbRec[rk];
  if(!old||t<old)G.fbRec[rk]=t;
  toast(f.n+' in '+kTime(t)+'! '+(old&&t<old?'Neuer Rekord!':old?'Rekord: '+kTime(old)+'.':'Das war die erste Fahrt.')+' '+pick(['Du tauchst prustend auf. Die Badehose sitzt noch, fast.','Ein Kind am Beckenrand ruft: „Nochmal!“ Gute Idee.','Günni pfeift anerkennend.']));
  if(G.rutsch===10)toast('Zehn Rutschfahrten! Günni überreicht dir den goldenen Schwimmflügel.');
 }});
}
function fbJump(m){
 const z=ZONE;
 if(m===10&&chance(.45)){
  mood(4,'+4 Vernunft');sfx('clap');z.jury={t:4,sc:[10,10,10]};
  toast('Du stehst oben auf dem Zehner und schaust runter. Ganz schön hoch! Du kletterst wieder runter. Die Rentner-Jury applaudiert: zehn Punkte für Vernunft.');
  return;
 }
 const H0={1:12,3:26,5:40,10:62}[m],dur={1:.7,3:.9,5:1.1,10:1.5}[m];
 const bx=FBJ[m],pts=[[bx,5.4],[bx,9.6]],L=4.2*TS;
 kpStart({pts:pts,mode:'const',v0:L/dur,face:Math.PI/2,hf:p=>H0*(1-p)+Math.sin(p*Math.PI)*(10+m*1.5),msg:{1:'Kopfsprung vom Einer!',3:'Arschbombe vom Dreier!',5:'Salto vom Fünfer!',10:'Der Zehner! Augen zu und ab!'}[m],end:c=>{
  let sc,txt,big=m>=3;
  if(m===1){sc=[rnd(5,8),rnd(5,8),rnd(5,8)];txt=pick(['Ein sauberer Kopfsprung. Opa Heinz nickt, Oma Grete schreibt eine Acht, malt dann aber ein Herz dazu.','Plopp! Kaum Spritzer. Die Jury ist beeindruckt und ein bisschen enttäuscht.']);mood(6,'+6 Sprung');}
  else if(m===3){sc=[rnd(6,10),rnd(6,10),rnd(7,10)];txt='Die Fontäne der Arschbombe trifft die Jury. Opa Heinz\' Thermoskanne ist jetzt eine Wasserkanne. Trotzdem: Höchstnoten!';mood(10,'+10 Arschbombe');}
  else if(m===5){if(chance(.5)){sc=[rnd(1,4),rnd(1,4),rnd(2,5)];txt='Autsch! Der Salto wird zum Bauchklatscher. Dein Bauch ist rot wie eine Tomate, die Jury gibt Mitleidspunkte.';mood(3,'+3 Autsch');}else{sc=[rnd(8,10),rnd(8,10),rnd(8,10)];txt='Ein echter Salto! Halb gedreht, halb gefallen, voll bejubelt.';mood(12,'+12 Salto');}}
  else{sc=[rnd(9,10),10,rnd(9,10)];txt='Vom Zehner! Du fliegst, du schreist, du tauchst. Die Rentner-Jury steht auf und klatscht, Oma Grete wirft ihren Sonnenhut.';mood(16,'+16 Mut');xpAdd(8);}
  kSplash(P.x,P.y,big?40:16);addFx(P.x,P.y-28,big?'PLATSCH!':'Plopp!','#9fd8ff',1.4);
  z.jury={t:5,sc:sc};G.spruenge=(G.spruenge||0)+1;xpAdd(3);
  toast(txt+' Punkte: '+sc.join(' · '));
 }});
}
function rodelGo(){
 const z=ZONE;if(!z||z.name!=='berge')return;
 kpStart({pts:RODLIFT,mode:'const',v0:120,face:-Math.PI/2,lift:'t',msg:'Der Schlepplift zieht dich gemütlich nach oben. Ruckel, ruckel.',end:()=>{
  kpStart({pts:RODEL,v0:60,acc:170,vmax:430,ctl:true,sled:true,trail:'#fff',curve:['Kurve!','Steilwand!','Huiii!','Festhalten!'],msg:'Oben! Hoch: anschieben und ducken, Runter: bremsen. Los geht es!',end:c=>{
   const t=c.t,old=G.rodelRec;if(!old||t<old)G.rodelRec=t;
   G.rodel=(G.rodel||0)+1;mood(12,'+12 Rodeln');xpAdd(4);sfx('win');
   for(let i=0;i<12;i++)FX.push({x:P.x+rf(-8,8),y:P.y+rf(-6,6),vx:rf(-60,60),vy:rf(-80,-10),g:160,t:0,life:.7,dot:'#fff',r:rf(1.5,3)});
   toast('Ziel! Gamsblitz in '+kTime(t)+'. '+(old&&t<old?'Neuer Bahnrekord!':old?'Dein Rekord: '+kTime(old)+'.':'Deine erste Fahrt, gleich der Rekord!')+' '+pick(['Deine Wangen sind rot, dein Grinsen ist breit.','Ein Murmeltier hält eine Tafel hoch: Haltungsnote 10.','Die Mütze ist weg. Egal, nochmal!']));
  }});
 }});
}
function skiGo(){
 const z=ZONE;if(!z||z.name!=='oesterreich')return;
 for(let i=RIDES.length-1;i>=0;i--)if(RIDES[i].k==='ski')RIDES.splice(i,1);
 z.skiRun=null;
 kpStart({pts:SKILIFT,mode:'const',v0:90,face:-Math.PI/2,lift:'s',msg:'Der Sessellift schaukelt nach oben. Unter dir: Schnee, Tannen und eine Kuh, die ein Selfie macht.',end:()=>{
  const R=mkRide('ski',10.5*TS,9.4*TS,Math.PI/2);R.stolen=true;RIDES.push(R);
  P.x=R.x;P.y=R.y;takeRide(R);
  z.skiRun={t:0,n:0,done:[],py:R.y};
  toast('Ski an, Brille runter! Links und Rechts lenken, Hoch gibt Schuss, Runter bremst (Pizza!). Fahr durch die vier Fahnentore.');
 }});
}
function skiTick(dt){
 const z=ZONE;if(!z||z.name!=='oesterreich'||!z.skiRun)return;
 const r=z.skiRun,R=P.ride;
 if(!R||R.k!=='ski'){z.skiRun=null;return;}
 r.t+=dt;
 SKIG.forEach((g,i)=>{const gy=g[1]*TS;if(!r.done[i]&&r.py<gy&&R.y>=gy){r.done[i]=1;if(Math.abs(R.x-g[0]*TS)<1.6*TS){r.n++;addFx(R.x,R.y-26,'Tor '+(i+1)+'!','#7ad35a',1);sfx('ding');}else addFx(R.x,R.y-26,'Tor verpasst!','#ff8a65',1);}});
 r.py=R.y;
 if(R.y>20.6*TS){
  z.skiRun=null;G.ski=(G.ski||0)+1;
  const t=r.t,sc=r.n*100-Math.round(t*10),old=G.skiRec;
  if(!old||sc>old.sc)G.skiRec={sc:sc,n:r.n,t:t};
  mood(8+r.n*2,'+'+(8+r.n*2)+' Abfahrt');xpAdd(3+r.n);sfx(r.n===4?'win':'clap');
  toast('Abschwung! '+r.n+' von 4 Toren in '+kTime(t)+'. '+(r.n===4?'Sepp-Bert jodelt vor Freude.':r.n>=2?'Nicht schlecht für einen Flachländer!':'Die Tore standen im Weg, oder?')+(old&&sc>old.sc?' Neue Bestleistung!':''));
 }
}
function skiDraw(R){
 ctx.fillStyle='#d63a3a';ctx.fillRect(-15,-5.5,30,2.6);ctx.fillRect(-15,3,30,2.6);
 ctx.fillStyle='#f1c40f';ctx.fillRect(13,-5.5,3,2.6);ctx.fillRect(13,3,3,2.6);
 ctx.strokeStyle='#666';ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(-4,-10);ctx.lineTo(4,-8);ctx.moveTo(-4,10);ctx.lineTo(4,8);ctx.stroke();ctx.lineWidth=1;
}
const KSHOP={
 pommes:{p:3,h:40,d:0,m:3,t:'Pommes rot-weiß in der Pappschale. Die Mayo kommt von oben, das Ketchup von der Seite.'},
 eis:{p:2,h:10,d:15,m:5,t:'Ein Wassereis in Raketenform. Es tropft schneller, als du lecken kannst.'},
 brause:{p:2,h:0,d:35,m:2,t:'Waldmeister-Brause, giftgrün und eiskalt.'},
 patat:{p:3,h:40,d:0,m:3,t:'Patat met mayo! Die Holländer nehmen dreimal so viel Mayo wie du gedacht hättest.'},
 frikandel:{p:3,h:35,d:0,m:3,t:'Eine Frikandel speciaal mit Zwiebeln und Curry-Soße. Niemand weiß genau, was drin ist, aber alle mögen sie.'},
 stroop:{p:2,h:15,d:0,m:4,t:'Eine Stroopwafel, warm über den Kakao gelegt. Der Sirup zieht Fäden bis zum Kinn.'},
 kakao:{p:2,h:5,d:30,m:2,t:'Ein heißer Kakao mit Sahnehaube. Lekker!'}
};
const KSHOPZ={
 freibad:()=>btn('Pommes rot-weiß: 3 €','kBuy','pommes',{def:1})+btn('Wassereis-Rakete: 2 €','kBuy','eis')+btn('Waldmeister-Brause: 2 €','kBuy','brause'),
 camping:()=>btn('Patat met mayo: 3 €','kBuy','patat',{def:1})+btn('Frikandel speciaal: 3 €','kBuy','frikandel')+btn('Stroopwafel: 2 €','kBuy','stroop')+btn('Heißer Kakao: 2 €','kBuy','kakao')
};
function kBuy(k){
 const s=KSHOP[k];if(!s)return;
 if(G.cash<s.p){toast('Nicht genug Geld.');return;}
 G.cash-=s.p;sfx('coin');needAdd(s.h,s.d);mood(s.m,'+'+s.m);toast(s.t);render2();
}
function fbEntry(mk){
 UI.mkRet={x:mk.x,y:mk.y+30};
 mdl('Freibad Planschbecken','Kassenwart Kurt sitzt im Häuschen und isst ein Eis: „Eintritt drei Euro. Drei Rutschen, ein Sprungturm, Pommes rot-weiß. Und nicht vom Beckenrand springen!“',[['Eintritt zahlen: 3 €','yk:fb:go',G.cash<3],['Durch den Zaun gucken','yk:fb:peek']]);
}
function liftMenu(){
 const r=G.skiRec;
 mdl('Sessellift Gipfelglück','Ein Sessellift, zwei Sitze, null Eile. Oben gibt es Leih-Ski, unten Kaiserschmarrn im Kaffeehaus. Die Liftkarte kostet 2 €, die Ski sind inklusive.'+(r?' Deine Bestleistung: '+r.n+' von 4 Toren in '+kTime(r.t)+'.':''),[['Liftkarte kaufen und hochfahren: 2 €','yk:sk:go',G.cash<2]]);
}
function rodelMenu(){
 const r=G.rodelRec,g=G.gbRec;
 mdl('Rodelbahn Gamsblitz','Der Bahnwart, ein Murmeltier mit Mütze, verteilt Schlitten. Die große Gamsblitz-Bahn startet oben am Gipfel, die Gondel fährt von hier. Gleich daneben liegt die kleine Übungsbahn mit Schlepplift.'+(g?' Rekord große Bahn: '+kTime(g)+'.':'')+(r?' Rekord Übungsbahn: '+kTime(r)+'.':''),[['Große Gamsblitz-Bahn: Gondel zum Gipfel','yk:gb:go'],['Kleine Übungsbahn mit Schlepplift','yk:ro:go']]);
}
function cmMenu(k){
 const hc=homeK()==='camp';
 if(k==='cmrez')mdl('Rezeption Tulpenwiese','Famke hinter dem Tresen: „Hoi! Willkommen auf der Tulpenwiese. Zelt, Wohnwagen oder gleich ein Dauerplatz?“'+(hc?' Du hast hier deinen Dauerplatz: Wohnwagen Gouda.':''),[[hc?'Dein Dauerplatz: Wohnwagen Gouda ('+eur(HOMES.camp.r)+' pro Tag)':'Dauerplatz mieten: '+eur(HOMES.camp.r)+' pro Tag (dein neues Zuhause)','yk:cm:dauer',hc||G.cash<HOMES.camp.r*2],['Brötchen für morgen bestellen: 2 €','yk:cm:broet',!!G.broet||G.cash<2],['Was ist hier los?','yk:cm:info']]);
 else if(k==='cmsan')mdl('Sanitärhaus','Vor den Duschen steht eine Schlange aus Kulturbeuteln. Die Menschen dazu sind irgendwo in der Nähe.',[['Duschen: 50 Cent','yk:cm:dusch',G.cash<.5],['Zähne putzen und Leute grüßen','yk:cm:zahn']]);
 else if(k==='cmgouda')mdl('Käse-Wohnwagen Gouda','Ein gelber Wohnwagen mit runden Fenstern, die aussehen wie Käselöcher. Am Vorzelt hängt eine Lichterkette in Tulpenform.'+(hc?' Er gehört dir!':''),[[hc?'Im Wohnwagen schlafen (Dauerplatz)':'Eine Nacht im Käse-Wohnwagen: 18 €','yk:cm:gouda',!hc&&G.cash<18],['Durchs Käseloch-Fenster gucken','yk:cm:peek']]);
 else if(k==='cmplatz')mdl('Zeltwiese','Freie Plätze, weiches Gras und ein Schild: „Heringe bitte nicht in die Enten stecken.“',[['Wurfzelt aufbauen und übernachten: 8 €','yk:cm:zelt',G.cash<8],['Luftmatratze aufpumpen','yk:cm:luft']]);
 else if(k==='cmfeuer')mdl('Lagerfeuer','Das Feuer knistert, die Funken tanzen, jemand hat Stockbrot-Teig mitgebracht.',[['Stockbrot grillen','yk:cm:stock'],['Gruselgeschichte erzählen','yk:cm:grusel'],['Lieder singen','yk:cm:sing']]);
}
const KSKM={gbahn:()=>gbMenu(),wohn:()=>homeMenu(),freibad:mk=>fbEntry(mk),lift:()=>liftMenu(),rodel:()=>rodelMenu(),
 fbrutsch:()=>mdl('Rutschenturm','Drei Rutschen, ein Ziel: das Becken. Die Schlange davor besteht aus elf Kindern und einem Opa mit Schwimmflügeln.'+(G.rutsch?' Deine Rutschfahrten: '+G.rutsch+'.':''),[['Blitz-Rutsche (gelb, steil und schnell)','yk:fb:r0'],['Looping-Schlange (blau, lang und kurvig)','yk:fb:r1'],['Reifenrutsche (rot, mit Gummi-Ente)','yk:fb:r2']]),
 fbturm:()=>mdl('Sprungturm','Bretter auf 1, 3, 5 und 10 Metern. Am Rand sitzt die Rentner-Jury mit Punktetafeln und Thermoskanne.',[['1 Meter: Kopfsprung','yk:fb:j1'],['3 Meter: Arschbombe','yk:fb:j3'],['5 Meter: Salto (Versuch)','yk:fb:j5'],['10 Meter: Mutprobe','yk:fb:j10']]),
 cmrez:()=>cmMenu('cmrez'),cmsan:()=>cmMenu('cmsan'),cmgouda:()=>cmMenu('cmgouda'),cmplatz:()=>cmMenu('cmplatz'),cmfeuer:()=>cmMenu('cmfeuer')};
function skAct19(p){
 if(p.indexOf('yk:')!==0)return false;
 const q=p.slice(3);UI.modal=null;render2();
 if(q==='ho:sleep'){kSleep(homeK(),'Guten Morgen');return true;}
 if(q==='ho:dusch'){
  if(G.duschT>0){toast('Du bist noch ganz frisch. Mehr Duschen macht nur schrumpelig.');return true;}
  G.duschT=1;const pe=homeK()==='pent';mood(pe?10:5,pe?'+10 Whirlpool':'+5 Frisch');sfx('splash');
  toast(pe?'Dusche, dann Whirlpool. Die Möwe rückt widerwillig ein Stück zur Seite.':pick(['Heißes Wasser, gute Laune. Du singst laut und falsch.','Duschen! Danach fühlst du dich wie neu, nur nasser.']));return true;
 }
 if(q==='ho:grow'){UI.growFrom='';show('grow');return true;}
 if(q==='ho:list'){show('homes');return true;}
 if(q==='ho:quit'){const h=HOMES[homeK()];G.home='imbiss';toast('Gekündigt. Du gibst die Schlüssel für '+h.s+' ab und ziehst zurück aufs Feldbett im Imbiss-Lager. Hanfred freut sich.');return true;}
 if(q==='fb:go'){
  if(G.cash<3){toast('Nicht genug Geld.');return true;}
  G.cash-=3;sfx('coin');if(!ZONE)G.ret=UI.mkRet||{x:P.x,y:P.y};
  startFade('Du gehst durchs Drehkreuz. Es riecht nach Chlor, Sonnencreme und Pommes. Freibad!',()=>enterZone('freibad'));return true;
 }
 if(q==='fb:peek'){mood(2,'+2');toast(pick(['Hinter dem Zaun rutscht gerade ein Opa in Badekappe die gelbe Rutsche runter. Er schreit vor Glück.','Du siehst die Rentner-Jury am Sprungturm. Sie hält gerade eine Zwölf hoch. Die Skala geht nur bis zehn.']));return true;}
 if(q.indexOf('fb:r')===0){fbSlide(+q.slice(4));return true;}
 if(q.indexOf('fb:j')===0){fbJump(+q.slice(4));return true;}
 if(q==='ro:go'){rodelGo();return true;}
 if(q==='gb:go'){gbFromAlps();return true;}
 if(q==='gb:again'){if(!ZONE||ZONE.name!=='gamsbahn')return true;kpStart({pts:GBLIFT,mode:'const',v0:170,face:-Math.PI/2,lift:'s',msg:'Die Gondel schaukelt nach oben. Unten winken die Zuschauer.',end:()=>gbRide()});return true;}
 if(q==='sk:go'){if(G.cash<2){toast('Nicht genug Geld.');return true;}G.cash-=2;sfx('coin');skiGo();return true;}
 if(q==='cm:dauer'){const r=homeTake('camp');toast(r.msg||'');return true;}
 if(q==='cm:broet'){if(G.cash<2)return true;G.cash-=2;G.broet=1;sfx('coin');toast('Famke schreibt dich auf die Brötchenliste: „Morgen früh hängen sie an deinem Zelt oder Wohnwagen.“');return true;}
 if(q==='cm:info'){toast(pick(['Famke: „Herbert ist seit 31 Jahren hier. Wim versucht seit Dienstag, sein Zelt zusammenzulegen. Und Oma Truus fährt mit ihrem Wohnwagen am Fahrrad durch die Gegend.“','Famke: „Am Lagerfeuer gibt es Stockbrot, am See Boote, an der Rezeption Fahrräder. Und der Holzschuh-Wohnwagen gehört meinem Onkel.“']));return true;}
 if(q==='cm:dusch'){if(G.cash<.5)return true;G.cash-=.5;mood(5,'+5 Frisch');sfx('splash');toast(pick(['Die Dusche läuft genau so lange, wie die Münze reicht. Shampoo im Haar, Wasser weg. Klassiker.','Eiskalt! Du kreischst. Die ganze Wiese weiß jetzt, dass du wach bist.','Warmes Wasser! Hinter dir in der Schlange applaudiert jemand.']));return true;}
 if(q==='cm:zahn'){mood(3,'+3');toast(pick(['Neben dir putzt ein Holländer seine Zähne und erzählt dabei von seinem Wohnwagen. Du verstehst nur „Schaum“.','Zähneputzen mit Blick auf die Windmühle. Urlaubsgefühl in Minzgeschmack.']));return true;}
 if(q==='cm:gouda'){
  const hc=homeK()==='camp';
  if(!hc){if(G.cash<18){toast('Nicht genug Geld.');return true;}G.cash-=18;sfx('coin');}
  kSleep('camp','Guten Morgen, Camper!',hc?'Du schläfst in deinem eigenen Käse-Wohnwagen.':'Du hast eine Nacht im Käse-Wohnwagen verbracht. Es riecht leicht nach Gouda.');return true;
 }
 if(q==='cm:peek'){mood(2,'+2');toast(pick(['Drinnen: ein Bett, eine Kochnische und ein Kissen in Käseform. Gemütlich!','Auf dem Tisch liegt eine Karte von Holland. Jemand hat alle Käsereien rot eingekreist.']));return true;}
 if(q==='cm:zelt'){
  if(G.cash<8){toast('Nicht genug Geld.');return true;}
  G.cash-=8;sfx('puff');
  const r=Math.random();
  const ex=r<.35?'Das Wurfzelt ploppt auf, fliegt einmal über die Wiese und landet im See. Eine Ente zieht ein. Du schläfst unter freiem Himmel, die Sterne sind gratis.':r<.7?'Das Wurfzelt ploppt auf und steht. Sofort. Perfekt. Du bist misstrauisch, schläfst aber trotzdem gut.':'Das Zelt ploppt auf und reißt Herberts Gartenzwerg Udo um. Herbert verzeiht dir, aber erst nach dem Frühstück.';
  kSleep('camp','Guten Morgen, Camper!',ex);return true;
 }
 if(q==='cm:luft'){mood(3,'+3');sfx('pfft');toast(pick(['Pumpen, pumpen, pumpen. Nach zehn Minuten ist die Luftmatratze halb voll und du ganz leer.','Die Luftmatratze ist prall. Zu prall. Sie quietscht beim Hinlegen wie ein Gummihuhn.']));return true;}
 if(q==='cm:stock'){needAdd(25,0);mood(5,'+5 Stockbrot');toast(pick(['Dein Stockbrot ist außen schwarz und innen roh. Genau richtig fürs Lagerfeuer.','Goldbraun! Herbert ruft rüber: „Anfängerglück!“']));return true;}
 if(q==='cm:grusel'){mood(5,'+5 Grusel');toast(pick(['Du erzählst vom Wohnwagen, der nachts von selbst Gouda isst. Die Kinder kreischen, Herbert auch.','„Und dann … ploppte das Zelt auf!“ Wim fällt vor Schreck vom Klappstuhl.']));return true;}
 if(q==='cm:sing'){mood(6,'+6 Singen');sfx('musik');toast('Alle singen ein Lied über Tulpen, Käse und Fahrräder. Niemand kennt den Text, alle singen trotzdem mit.');return true;}
 if(q==='hb:zwerg'){mood(3,'+3');toast('Du zählst 23 Gartenzwerge. Herbert korrigiert: „24. Der Udo steht hinten beim Grill.“');return true;}
 if(q==='hb:wurst'){needAdd(30,0);mood(4,'+4 Wurst');toast('Herbert reicht dir eine Grillwurst im Brötchen: „Aber nicht weitersagen, sonst wollen alle eine.“');return true;}
 if(q==='hb:wetter'){mood(4,'+4');toast('Ihr meckert gemeinsam über das Wetter. Es ist sonnig, 24 Grad, leichter Wind. Herbert: „Viel zu perfekt. Da stimmt was nicht.“');return true;}
 if(q==='wm:help'){
  if(chance(.3)){mood(10,'+10 Geschafft');xpAdd(6);sfx('win');toast('Ihr habt es geschafft! Das Zelt ist zusammengelegt, ein perfekter Kreis. Wim weint vor Glück und schenkt dir 5 €.');G.cash+=5;}
  else{if(ZONE&&ZONE.wim)ZONE.wim.pop=1.2;mood(4,'+4');sfx('puff');toast(pick(['Fast! Dann ploppt das Zelt wieder auf und wirft euch beide ins Gras.','Ihr faltet, dreht, drückt … PLOPP. Das Zelt steht wieder. Wim: „Morgen vielleicht.“']));}
  return true;
 }
 if(q==='wm:pop'){if(ZONE&&ZONE.wim)ZONE.wim.pop=1.2;mood(4,'+4 Plopp');sfx('puff');toast('PLOPP! Das Zelt springt auf, hüpft einen Meter hoch und landet auf Wims Kopf. Er lacht trotzdem.');return true;}
 if(q==='tr:race'){if(chance(.25)){mood(8,'+8 Sieg');toast('Du gewinnst knapp! Oma Truus: „Morgen trainiere ich doppelt.“');}else{mood(5,'+5');toast('Oma Truus zieht mit Wohnwagen am Gepäckträger an dir vorbei und klingelt dabei zweimal. Respekt.');}return true;}
 if(q==='tr:wagen'){mood(3,'+3');toast('„Da drin ist ein Bett, ein Gaskocher und mein Kater Pim. Pim fährt gern mit.“ Aus dem Fenster schaut ein sehr entspannter Kater.');return true;}
 if(q==='bm:pferd'){if(G.pferd){toast('Günni: „Du hast doch schon dein Seepferdchen! Willst du jetzt den Freischwimmer? Dann aber ohne Gummi-Ente.“');return true;}G.pferd=1;mood(8,'+8 Seepferdchen');xpAdd(5);sfx('win');toast('Du springst ins Becken, holst einen Ring vom Boden und schwimmst eine Bahn. Günni näht dir das Seepferdchen-Abzeichen persönlich auf das Handtuch.');return true;}
 if(q==='bm:rek'){const r=G.fbRec||{};const L=FBS.map((f,i)=>f.n+': '+(r['r'+i]?kTime(r['r'+i]):'noch nie'));toast('Günni zückt sein Klemmbrett. Deine Rekorde: '+L.join(' · ')+'. Sprünge: '+(G.spruenge||0)+'.');return true;}
 if(q==='bm:pfeif'){mood(4,'+4');sfx('ding');toast('Ihr pfeift gleichzeitig. Alle im Becken bleiben stehen. Dann lachen alle. Günni: „Wollte ich schon immer mal machen.“');return true;}
 if(q==='se:pizza'){mood(4,'+4');toast('Du stellst die Füße zur Pizza. Sepp-Bert: „Bravo! Und jetzt mit Salami!“ Du weißt nicht, was er meint, nickst aber.');return true;}
 if(q==='se:pommes'){mood(4,'+4');toast('Füße parallel: Pommes! Sepp-Bert: „Perfekt! Mit Mayo oder ohne?“');return true;}
 if(q==='se:rek'){const r=G.skiRec;toast(r?'Sepp-Bert blättert im Büchlein: „Bestleistung: '+r.n+' von 4 Toren in '+kTime(r.t)+'. Ski Heil!“':'Sepp-Bert: „Noch keine Abfahrt? Ab in den Lift!“');return true;}
 return true;
}
function kStatic(c,z){
 const nm=z.name;
 if(nm==='feldweg'){felderStatic(c);medFeldStatic(c);return;}
 const R=(x,y,w,h,col)=>{c.fillStyle=col;c.fillRect(x,y,w,h);};
 const C=(x,y,r,col)=>{c.fillStyle=col;c.beginPath();c.arc(x,y,r,0,6.283);c.fill();};
 const E=(x,y,rx,ry,col)=>{c.fillStyle=col;c.beginPath();c.ellipse(x,y,rx,ry,0,0,6.283);c.fill();};
 const T=(t,x,y,col,f)=>{c.font=f||'bold 9px Arial';c.textAlign='center';c.textBaseline='middle';c.lineWidth=3;c.strokeStyle='rgba(0,0,0,.45)';c.strokeText(t,x,y);c.fillStyle=col||'#fff';c.fillText(t,x,y);c.lineWidth=1;c.textAlign='start';};
 const PL=(pts,w,col,dash)=>{c.strokeStyle=col;c.lineWidth=w;c.lineCap='round';c.lineJoin='round';if(dash)c.setLineDash(dash);c.beginPath();pts.forEach((q,i)=>{const x=q[0]*TS,y=q[1]*TS;if(i)c.lineTo(x,y);else c.moveTo(x,y);});c.stroke();c.setLineDash([]);c.lineWidth=1;c.lineCap='butt';};
 if(nm==='freibad'){
  c.strokeStyle='rgba(255,255,255,.55)';c.lineWidth=2;for(let j=0;j<4;j++){const y=(8.3+j*1.8)*TS;c.setLineDash([10,8]);c.beginPath();c.moveTo(15.4*TS,y);c.lineTo(32.6*TS,y);c.stroke();}c.setLineDash([]);c.lineWidth=1;
  R(14*TS,6*TS,20*TS,3,'#f4f8fb');R(14*TS,16*TS-3,20*TS,3,'#f4f8fb');R(14*TS,6*TS,3,10*TS,'#f4f8fb');R(34*TS-3,6*TS,3,10*TS,'#f4f8fb');
  FBS.slice().reverse().forEach(f=>{PL(f.pts,16,'rgba(0,0,0,.18)');PL(f.pts,13,f.c);PL(f.pts,5,'rgba(255,255,255,.45)');});
  R(3*TS,3*TS,3*TS,3*TS,'#2fa3d6');R(3*TS+6,3*TS+6,3*TS-12,3*TS-12,'#8fd8f8');C(4.5*TS,4.5*TS,14,'#f4f8fb');T('RUTSCHEN',4.5*TS,4.5*TS,'#2e86c1','bold 8px Arial');
  R(22*TS+4,3*TS+6,5*TS,2*TS,'rgba(0,0,0,.25)');R(22*TS,3*TS,5*TS,2*TS,'#9aa6b2');R(22*TS+4,3*TS+4,5*TS-8,2*TS-8,'#b8c2cc');
  for(let i=0;i<6;i++)R(22*TS+8,3*TS+8+i*9,10,3,'#6a7682');
  [[22.6,1.2,'1'],[23.6,1.7,'3'],[24.6,2.2,'5'],[25.6,2.8,'10']].forEach(q=>{const x=q[0]*TS,l=q[1]*TS;R(x-6+4,5*TS+4,12,l,'rgba(0,0,0,.2)');R(x-6,5*TS-4,12,l,'#2e86c1');R(x-6,5*TS-4+l-5,12,5,'#1f5f8a');T(q[2],x,5*TS+l/2-4,'#fff','bold 9px Arial');});
  T('SPRUNGTURM',24.5*TS,3.6*TS,'#2e86c1','bold 9px Arial');
  R(27.4*TS,3.6*TS,4*TS,22,'#5a6a7a');T('JURY',29.4*TS,3.6*TS+11,'#ffd23f','bold 8px Arial');
  C(40.5*TS,9.5*TS,20,'#e5604d');C(40.5*TS,9.5*TS,7,'#fff');[0,1,2,3,4,5].forEach(k=>{const a=k*1.05;C(40.5*TS+Math.cos(a)*14,9.5*TS+Math.sin(a)*14,3,'#fff');});
  R(34*TS+8,11*TS-18,16,34,'#f4f4f4');R(34*TS+4,11*TS-22,24,8,'#e5504d');T('GÜNNI',34.5*TS,11*TS+20,'#e5504d','bold 7px Arial');
  for(let y=19;y<29;y++)for(let x=1;x<47;x++){if(hash(x,y)%23===0&&z.T[y*ZW+x]===GR){R(x*TS+4,y*TS+6,22,12,pick(['#e5604d','#f1c40f','#2e86c1','#ff7fb0','#7ad35a']));R(x*TS+4,y*TS+9,22,2,'rgba(255,255,255,.6)');}}
  R(0,17.6*TS,ZW*TS,4,'rgba(255,255,255,.35)');
  T('FREIBAD PLANSCHBECKEN',24*TS,2.3*TS,'#2e86c1','bold 11px Arial');
  T('NICHTSCHWIMMER',40.5*TS,6.5*TS,'#2e86c1','bold 8px Arial');
 }else if(nm==='camping'){
  const H=z.cmp;
  c.strokeStyle='#8a5a3a';c.lineWidth=2;c.beginPath();for(let x=4.6*TS;x<=9.4*TS;x+=8){c.moveTo(x,11.6*TS);c.lineTo(x+8,11.6*TS-8);c.moveTo(x+8,11.6*TS);c.lineTo(x,11.6*TS-8);}c.stroke();
  c.beginPath();for(let y=11.6*TS;y<=15.6*TS;y+=8){c.moveTo(4.6*TS,y);c.lineTo(4.6*TS-8,y+8);c.moveTo(9.6*TS,y);c.lineTo(9.6*TS+8,y+8);}c.stroke();c.lineWidth=1;
  H.forEach(o=>{
   const x=o.x*TS,y=o.y*TS,w=o.w*TS,h=o.h*TS;
   E(x+w/2+4,y+h-2,w/2,10,'rgba(0,0,0,.22)');
   if(o.t==='herb'){
    R(x+4,y+6,w-8,h-14,'#f4f0e6');R(x+4,y+22,w-8,6,'#8a5a3a');R(x+12,y+12,18,10,'#8fd0ff');R(x+40,y+12,18,10,'#8fd0ff');R(x+70,y+10,14,30,'#c9b28a');
    R(x,y+h-12,w,12,'#e5604d');for(let i=0;i<w;i+=16)R(x+i,y+h-12,8,12,'#fff');
    C(x+w-16,y+4,9,'#d8d8d8');C(x+w-16,y+4,4,'#888');
    for(let i=0;i<8;i++){const gx=x+6+i*15,gy=y+h+18;E(gx,gy+3,3,2,'rgba(0,0,0,.25)');R(gx-3,gy-2,6,6,['#2e86c1','#2ecc71','#9b59b6','#e67e22'][i%4]);C(gx,gy-4,3,'#f0d2b4');c.fillStyle='#d63a3a';c.beginPath();c.moveTo(gx-4,gy-5);c.lineTo(gx,gy-13);c.lineTo(gx+4,gy-5);c.fill();C(gx,gy-2,1.6,'#fff');}
   }else if(o.t==='gouda'){
    c.fillStyle='#f6c945';c.beginPath();c.moveTo(x+6,y+h-6);c.lineTo(x+6,y+16);c.quadraticCurveTo(x+6,y+4,x+22,y+4);c.lineTo(x+w-16,y+4);c.quadraticCurveTo(x+w-4,y+4,x+w-4,y+18);c.lineTo(x+w-4,y+h-6);c.closePath();c.fill();
    [[18,18,5],[40,14,4],[60,24,6],[78,16,4],[30,34,4],[70,40,3]].forEach(q=>C(x+q[0],y+q[1],q[2],'#d9a520'));
    C(x+46,y+30,7,'#8fd0ff');C(x+46,y+30,7.5,'rgba(0,0,0,0)');R(x+w-24,y+20,10,26,'#c0392b');
    R(x+2,y+h-8,w-4,4,'#555');T('GOUDA',x+w/2,y+h-14,'#c0392b','bold 8px Arial');
   }else if(o.t==='iglu'){
    C(x+w/2,y+h/2+4,26,'#f4f8fb');c.strokeStyle='#bcd4e6';c.lineWidth=1.5;for(let r=8;r<26;r+=7){c.beginPath();c.arc(x+w/2,y+h/2+4,r,Math.PI,0);c.stroke();}c.lineWidth=1;
    R(x+w/2-6,y+h/2+10,12,14,'#3a4a5a');
   }else if(o.t==='tipi'){
    c.fillStyle='#e8d6a8';c.beginPath();c.moveTo(x+w/2,y-12);c.lineTo(x+w-2,y+h-4);c.lineTo(x+2,y+h-4);c.closePath();c.fill();
    c.strokeStyle='#c0392b';c.lineWidth=3;c.beginPath();c.moveTo(x+14,y+h-16);c.lineTo(x+w-14,y+h-16);c.stroke();c.strokeStyle='#2e86c1';c.beginPath();c.moveTo(x+20,y+h-28);c.lineTo(x+w-20,y+h-28);c.stroke();c.lineWidth=1;
    c.strokeStyle='#6a4a2a';c.lineWidth=2;c.beginPath();c.moveTo(x+w/2-8,y-20);c.lineTo(x+w/2+4,y-4);c.moveTo(x+w/2+8,y-20);c.lineTo(x+w/2-4,y-4);c.stroke();c.lineWidth=1;
    c.fillStyle='#5a3a1a';c.beginPath();c.moveTo(x+w/2,y+h-26);c.lineTo(x+w/2+9,y+h-4);c.lineTo(x+w/2-9,y+h-4);c.closePath();c.fill();
   }else if(o.t==='tulpe'){
    R(x+w/2-2,y+h-14,4,14,'#2f8a3a');
    [['#ff5f9e',-14],['#ff7fb0',14],['#ff3f88',0]].forEach(q=>{c.fillStyle=q[0];c.beginPath();c.ellipse(x+w/2+q[1]*.8,y+h/2-2,16,24,q[1]*.03,0,6.283);c.fill();});
    R(x+w/2-5,y+h-22,10,10,'#7a1a4a');
   }else if(o.t==='pyra'){
    R(x+4,y+4,w-8,h-8,'#7ad35a');c.fillStyle='#5aa83a';c.beginPath();c.moveTo(x+4,y+4);c.lineTo(x+w/2,y+h/2);c.lineTo(x+4,y+h-4);c.closePath();c.fill();c.fillStyle='#9ae37a';c.beginPath();c.moveTo(x+w-4,y+4);c.lineTo(x+w/2,y+h/2);c.lineTo(x+w-4,y+h-4);c.closePath();c.fill();
    C(x+w/2,y+h/2,3,'#3a6a2a');
   }else if(o.t==='schuh'){
    c.fillStyle='#d9a54a';c.beginPath();c.moveTo(x+4,y+h-6);c.lineTo(x+4,y+18);c.quadraticCurveTo(x+6,y+4,x+30,y+6);c.lineTo(x+w-30,y+10);c.quadraticCurveTo(x+w+4,y+18,x+w-6,y+h-8);c.closePath();c.fill();
    c.strokeStyle='#a8722f';c.lineWidth=2;c.stroke();c.lineWidth=1;
    E(x+26,y+22,12,8,'#6a4a2a');R(x+56,y+16,16,10,'#8fd0ff');R(x+82,y+18,12,10,'#8fd0ff');
    [[48,34],[64,38],[90,32]].forEach(q=>{C(x+q[0],y+q[1],3,'#e5504d');C(x+q[0],y+q[1],1.2,'#ffd23f');});
   }else if(o.t==='bus'){
    R(x+4,y+6,w-8,h-12,'#ff8c2a');R(x+w-18,y+10,10,h-20,'#8fd0ff');R(x+4,y+h/2-3,w-8,6,'#f4f0e6');
    R(x+12,y+2,w-40,h-4,'#2ecc71');c.strokeStyle='#1f8a4a';c.beginPath();c.moveTo(x+12,y+2);c.lineTo(x+w-28,y+h-2);c.moveTo(x+w-28,y+2);c.lineTo(x+12,y+h-2);c.stroke();
    C(x+14,y+h-4,5,'#222');C(x+w-16,y+h-4,5,'#222');
   }else if(o.t==='burg'){
    R(x+6,y+12,w-12,h-14,'#f4f0e6');for(let i=0;i<w-12;i+=12)R(x+6+i,y+10,8,6,'#e5504d');
    [[6,4],[w-18,4]].forEach(q=>{R(x+q[0],y+q[1],12,h-6,'#e5504d');R(x+q[0],y+q[1],12,4,'#c0392b');R(x+q[0]+5,y+q[1]-12,2,12,'#555');c.fillStyle='#f1c40f';c.beginPath();c.moveTo(x+q[0]+7,y+q[1]-12);c.lineTo(x+q[0]+15,y+q[1]-9);c.lineTo(x+q[0]+7,y+q[1]-6);c.fill();});
    c.fillStyle='#6a4a2a';c.beginPath();c.arc(x+w/2,y+h-4,9,Math.PI,0);c.fill();
   }
  });
  C(27.5*TS,19.5*TS,16,'#6a6a6a');C(27.5*TS,19.5*TS,11,'#3a2a1a');
  for(let k=0;k<6;k++){const a=k*1.05;E(27.5*TS+Math.cos(a)*24,19.5*TS+Math.sin(a)*18,8,4,'#8a5a3a');}
  R(29.4*TS,0.6*TS,3.2*TS,4.4*TS,'#8a5a3a');R(29.6*TS,0.8*TS,2.8*TS,4*TS,'#a8723f');R(30.6*TS,3.4*TS,1*TS,1.4*TS,'#5a3a1a');T('MOLEN',31*TS,2.2*TS,'#fff','bold 8px Arial');
  T('CAMPING TULPENWIESE',12*TS,0.7*TS,'#ffd23f','bold 11px Arial');
  for(let i=0;i<40;i++){const x=(1+(hash(i,7)%46))*TS+((hash(i,9)%20)),y=(16+(hash(i,3)%12))*TS+(hash(i,5)%20);if(z.T[Math.floor(y/TS)*ZW+Math.floor(x/TS)]===GR){R(x,y,2,6,'#2f8a3a');C(x+1,y-1,3,pick(['#ff5f9e','#ffd23f','#e5504d','#ffffff','#9b59b6']));}}
 }else if(nm==='berge'){
  PL(RODLIFT,4,'rgba(0,0,0,.25)',[2,10]);PL(RODLIFT,2,'#4a4a4a');
  RODLIFT.forEach((q,i)=>{if(i<2){const n=6;for(let k=0;k<=n;k++){const a=RODLIFT[i],b=RODLIFT[i+1];const x=(a[0]+(b[0]-a[0])*k/n)*TS,y=(a[1]+(b[1]-a[1])*k/n)*TS;R(x-2,y-2,4,4,'#6a6a6a');}}});
  PL(RODEL,30,'rgba(80,110,140,.35)');PL(RODEL,26,'#e8f2fa');PL(RODEL,18,'#bfe2f6');PL(RODEL,4,'rgba(255,255,255,.7)',[6,10]);
  R(43*TS,4*TS,2.4*TS,1.1*TS,'#8a5a35');R(43*TS,4*TS,2.4*TS,6,'#5a3a1a');T('START',44.2*TS,4.6*TS,'#ffd23f','bold 8px Arial');
  R(44.4*TS,18.6*TS,2.4*TS,1*TS,'#8a5a35');R(44.4*TS,18.6*TS,2.4*TS,6,'#5a3a1a');T('ZIEL',45.6*TS,19.1*TS,'#ffd23f','bold 8px Arial');
  T('ÜBUNGSBAHN',38*TS,4.2*TS,'#2e86c1','bold 9px Arial');
 }else if(nm==='gamsbahn'){
  PL(GBLIFT,4,'rgba(0,0,0,.25)',[2,10]);PL(GBLIFT,2,'#4a4a4a');
  for(let y=4;y<27;y+=3)R(1.4*TS-3,y*TS-3,6,6,'#6a6a6a');
  PL(GBP,32,'rgba(80,110,140,.35)');PL(GBP,27,'#e8f2fa');PL(GBP,19,'#bfe2f6');PL(GBP,4,'rgba(255,255,255,.7)',[6,10]);
  GBBUMP.forEach(b=>{const pa=kpBuild(GBP),q=kpAt(pa,pa.L*b);c.save();c.translate(q.x,q.y);c.rotate(q.a);c.fillStyle='rgba(255,255,255,.9)';c.fillRect(-14,-11,28,22);c.fillStyle='rgba(120,160,200,.35)';c.fillRect(-14,-11,10,22);c.restore();T('SPRUNGHÜGEL',q.x,q.y-20,'#e5504d','bold 8px Arial');});
  R(2*TS,2.4*TS,3*TS,1*TS,'#8a5a35');R(2*TS,2.4*TS,3*TS,6,'#5a3a1a');T('START',3.5*TS,2.9*TS,'#ffd23f','bold 9px Arial');
  R(1.6*TS,26.9*TS,3.4*TS,1*TS,'#8a5a35');R(1.6*TS,26.9*TS,3.4*TS,6,'#5a3a1a');T('ZIEL',3.3*TS,27.4*TS,'#ffd23f','bold 9px Arial');
  GBY.slice(0,5).forEach((y,i)=>{const x=(i%2===0?GBR+2.6:GBL-2.6)*TS;T(i%2===0?'HAARNADEL':'STEILKURVE',x,(y+2.25)*TS,'#2e86c1','bold 7px Arial');});
  T('GROSSE GAMSBLITZ-BAHN',24*TS,1.7*TS,'#2e86c1','bold 11px Arial');
 }else if(nm==='oesterreich'){
  const a=SKILIFT[0],b=SKILIFT[1];
  c.strokeStyle='#4a4a4a';c.lineWidth=2;c.beginPath();c.moveTo(a[0]*TS-6,a[1]*TS);c.lineTo(b[0]*TS-6,b[1]*TS);c.moveTo(a[0]*TS+6,a[1]*TS);c.lineTo(b[0]*TS+6,b[1]*TS);c.stroke();c.lineWidth=1;
  for(let k=0;k<=5;k++){const x=(a[0]+(b[0]-a[0])*k/5)*TS,y=(a[1]+(b[1]-a[1])*k/5)*TS;R(x-3,y-3,6,6,'#6a6a6a');}
  R(9.2*TS,7.4*TS,2.6*TS,1*TS,'#8a5a35');R(9.2*TS,7.4*TS,2.6*TS,6,'#5a3a1a');T('BERGSTATION',10.5*TS,7.9*TS,'#ffd23f','bold 7px Arial');
  R(10.2*TS,21.2*TS,2.6*TS,0.9*TS,'#8a5a35');R(10.2*TS,21.2*TS,2.6*TS,6,'#5a3a1a');T('TALSTATION',11.5*TS,21.6*TS,'#ffd23f','bold 7px Arial');
  SKIG.forEach((g,i)=>{const col=i%2?'#2e86c1':'#e5504d';[-1.6,1.6].forEach(d=>{const x=(g[0]+d)*TS,y=g[1]*TS;R(x-1,y-14,2,16,'#555');c.fillStyle=col;c.beginPath();c.moveTo(x+1,y-14);c.lineTo(x+11,y-10);c.lineTo(x+1,y-6);c.fill();});T(String(i+1),g[0]*TS,g[1]*TS-4,col,'bold 9px Arial');});
  T('SKIPISTE',4*TS,9*TS,'#2e86c1','bold 10px Arial');
 }
}
function kDraw(cx,cy){
 const z=ZONE;if(!z)return;
 const iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 if(z.name==='freibad'){
  if(z.fbs)z.fbs.forEach(s=>{if(iv(s.x,s.y,30))drawSwim(s.x,s.y,s.d>0?0:Math.PI,s.col,s.w);});
  if(z.kids)z.kids.forEach(k=>{if(!iv(k.x,k.y,30))return;const b=Math.sin(timeNow*4+k.p)*2;ctx.fillStyle='rgba(255,255,255,.5)';ctx.beginPath();ctx.ellipse(k.x,k.y+3,9,4,0,0,6.283);ctx.fill();ctx.fillStyle='#f0d2b4';circle(k.x,k.y+b,4);ctx.fillStyle=k.col;ctx.beginPath();ctx.arc(k.x,k.y+b,4.4,Math.PI,0);ctx.fill();ctx.fillStyle='#ff9a3c';ctx.fillRect(k.x-8,k.y+b-1,3,4);ctx.fillRect(k.x+5,k.y+b-1,3,4);});
  const jx=[28,29.4,30.8];
  jx.forEach((x,i)=>{fig(x*TS,4.9*TS,Math.PI/2,{dress:['#9b59b6','#2e86c1','#e67e22'][i],hair:'#dddddd',hairLen:i===1?0:3,sk:4.8,hat:i===2?'#f4f0d0':null,brim:5});});
  if(z.jury&&z.jury.t>0){jx.forEach((x,i)=>{const X=x*TS,Y=4.9*TS-26;ctx.fillStyle='#fff';ctx.fillRect(X-9,Y-9,18,14);ctx.strokeStyle='#333';ctx.strokeRect(X-9,Y-9,18,14);ctx.fillStyle='#c0392b';ctx.font='bold 10px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(String(z.jury.sc[i]),X,Y-2);ctx.textAlign='start';});}
  const c=P.coast;
  if(c&&c.k==='kp'&&c.o.hf){ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(c.gx,c.gy+4,8,4,0,0,6.283);ctx.fill();}
  if(c&&c.k==='kp'&&c.o.shout===FBRS[2]){ctx.fillStyle='#222';ctx.beginPath();ctx.arc(P.x,P.y,12,0,6.283);ctx.fill();ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.arc(P.x,P.y,12,0,6.283);ctx.arc(P.x,P.y,7,0,6.283,true);ctx.fill();}
 }else if(z.name==='camping'){
  const mx=31*TS,my=1.4*TS;
  if(iv(mx,my,90)){ctx.save();ctx.translate(mx,my);ctx.rotate(z.ma||0);for(let k=0;k<4;k++){ctx.rotate(1.5708);ctx.fillStyle='#f4f0e6';ctx.fillRect(4,-5,44,10);ctx.strokeStyle='#8a5a3a';ctx.strokeRect(4,-5,44,10);ctx.beginPath();for(let i=10;i<48;i+=8){ctx.moveTo(i,-5);ctx.lineTo(i,5);}ctx.stroke();}ctx.fillStyle='#5a3a1a';circle(0,0,5);ctx.restore();}
  const w=z.wim;if(w&&iv(20.5*TS,21.5*TS,60)){const hp=w.pop>0?Math.abs(Math.sin(w.pop*6))*22:0,s=w.pop>0?1+Math.sin(w.pop*9)*.15:1;const x=20.5*TS,y=21.6*TS;ctx.fillStyle='rgba(0,0,0,.22)';ctx.beginPath();ctx.ellipse(x+3,y+12,22,7,0,0,6.283);ctx.fill();ctx.fillStyle='#ff9a3c';ctx.beginPath();ctx.ellipse(x,y-hp,22*s,16/s,0,0,6.283);ctx.fill();ctx.strokeStyle='#c0602a';ctx.lineWidth=1.5;ctx.beginPath();ctx.ellipse(x,y-hp,22*s,16/s,0,0,6.283);ctx.moveTo(x-22*s,y-hp);ctx.lineTo(x+22*s,y-hp);ctx.moveTo(x,y-hp-16/s);ctx.lineTo(x,y-hp+16/s);ctx.stroke();ctx.lineWidth=1;}
  if(iv(27.5*TS,19.5*TS,40)){for(let i=0;i<3;i++){const f=Math.sin(timeNow*9+i*2)*3;ctx.fillStyle=['#ffd23f','#ff9a3c','#e5504d'][i];ctx.beginPath();ctx.moveTo(27.5*TS-8+i*8,19.5*TS+5);ctx.lineTo(27.5*TS-4+i*4,19.5*TS-12-f-i*2);ctx.lineTo(27.5*TS+i*4,19.5*TS+5);ctx.fill();}if(chance(.15))FX.push({x:27.5*TS+rf(-6,6),y:19.5*TS-10,vx:rf(-10,10),vy:rf(-50,-25),t:0,life:.8,dot:'#ffb347',r:1.4});}
 }else if(z.name==='berge'||z.name==='oesterreich'||z.name==='gamsbahn'){
  if(z.fans)z.fans.forEach(f=>{if(!iv(f.x,f.y,40))return;const j=f.j>0?Math.abs(Math.sin(f.j*12))*6:0;
   if(f.k==='gams'){ctx.fillStyle='rgba(0,0,0,.2)';ctx.beginPath();ctx.ellipse(f.x+2,f.y+6,12,5,0,0,6.283);ctx.fill();ctx.fillStyle='#8a5a35';ctx.beginPath();ctx.ellipse(f.x,f.y-j,11,7,0,0,6.283);ctx.fill();ctx.fillStyle='#6a4325';circle(f.x+10,f.y-5-j,5);ctx.strokeStyle='#222';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(f.x+9,f.y-9-j);ctx.quadraticCurveTo(f.x+8,f.y-16-j,f.x+5,f.y-15-j);ctx.moveTo(f.x+12,f.y-9-j);ctx.quadraticCurveTo(f.x+12,f.y-16-j,f.x+9,f.y-16-j);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#fff';ctx.fillRect(f.x-8,f.y-26-j,16,11);ctx.fillStyle='#c0392b';ctx.font='bold 8px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('10',f.x,f.y-20-j);ctx.textAlign='start';}
   else{fig(f.x,f.y-j,Math.PI/2,{dress:f.col,hair:'#5a3a1a',hat:f.hat,hat2:'#fff',brim:4.4,sk:5});ctx.strokeStyle='#7a5a32';ctx.beginPath();ctx.moveTo(f.x+8,f.y-j);ctx.lineTo(f.x+8,f.y-18-j);ctx.stroke();ctx.fillStyle=f.col;ctx.fillRect(f.x+8,f.y-18-j,10,6);}});
  const L=z.name==='berge'?RODLIFT:z.name==='gamsbahn'?GBLIFT:SKILIFT,pa=z.kLiftPa||(z.kLiftPa=kpBuild(L));
  for(let k=0;k<7;k++){const s=((timeNow*(z.name==='berge'?40:30)+k*pa.L/7)%pa.L),q=kpAt(pa,s);if(!iv(q.x,q.y,30))continue;
   if(z.name!=='berge'){ctx.fillStyle='#3a4a5a';ctx.fillRect(q.x-9,q.y-4,18,8);ctx.fillStyle='#e5504d';ctx.fillRect(q.x-9,q.y-4,18,3);}
   else{ctx.strokeStyle='#5a5a5a';ctx.beginPath();ctx.moveTo(q.x-7,q.y);ctx.lineTo(q.x+7,q.y);ctx.moveTo(q.x,q.y-6);ctx.lineTo(q.x,q.y);ctx.stroke();}}
  const c=P.coast;
  if(c&&c.k==='kp'&&c.h>1){ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(c.gx,c.gy+4,12,5,0,0,6.283);ctx.fill();}
  if(c&&c.k==='kp'){
   if(c.o.lift==='s'){ctx.fillStyle='#3a4a5a';ctx.fillRect(P.x-11,P.y-2,22,10);ctx.fillStyle='#e5504d';ctx.fillRect(P.x-11,P.y-2,22,3);}
   else if(c.o.sled){ctx.save();ctx.translate(P.x,P.y);ctx.rotate(P.a);ctx.fillStyle='#777';ctx.fillRect(-15,-9,30,2.5);ctx.fillRect(-15,6.5,30,2.5);ctx.fillStyle='#b5651d';ctx.fillRect(-12,-7,24,14);ctx.fillStyle='#e5604d';ctx.fillRect(-12,-7,24,3);ctx.restore();}
  }
 }
}
function kUpdate(dt){
 if(!G)return;
 pActTick(dt);kEvTick(dt);
 if(G.dayS!==DAY_S){if(!G.dayS&&G.t<=150.5)G.t=G.t*DAY_S/150;G.dayS=DAY_S;}
 G.offT=(G.offT||0)+dt;if(G.offT>50){G.offT=0;G.offers=G.offers.filter(o=>o.dl>=G.day);fillOffers();}
 kpTick(dt);
 const z=ZONE;if(!z)return;
 if(z.fans){const c=P.coast;z.fans.forEach(f=>{if(f.j>0)f.j-=dt;if(f.cd>0)f.cd-=dt;if(c&&c.k==='kp'&&f.cd<=0&&Math.hypot(f.x-P.x,f.y-P.y)<120){f.cd=4;f.j=1;addFx(f.x,f.y-30,pick(f.k==='gams'?['Mäh!','Määäh!']:['Hopp hopp!','Schneller!','Bravo!','Juhu!']),'#ffd23f',1.2);}});}
 skiTick(dt);
 if(z.jury&&z.jury.t>0)z.jury.t-=dt;
 if(z.name==='freibad'){
  if(z.fbs)z.fbs.forEach(s=>{s.x+=s.d*s.sp*dt;s.w+=dt*6;if(s.x<15.8*TS){s.x=15.8*TS;s.d=1;}if(s.x>32.2*TS){s.x=32.2*TS;s.d=-1;}});
  if(z.kids&&chance(dt*1.5)){const k=pick(z.kids);for(let i=0;i<5;i++)FX.push({x:k.x+rf(-4,4),y:k.y,vx:rf(-40,40),vy:rf(-70,-20),g:200,t:0,life:.5,dot:'rgba(210,240,255,.9)',r:rf(1.2,2.4)});if(chance(.3)&&Math.hypot(k.x-P.x,k.y-P.y)<300)addFx(k.x,k.y-14,pick(['Platsch!','Hihi!','Guck mal!','Nochmal!']),'#fff2b0',1);}
 }
 if(z.name==='camping'){z.ma=(z.ma||0)+dt*.7;const w=z.wim;if(w){if(w.pop>0)w.pop-=dt;w.t-=dt;if(w.t<=0){w.t=rf(14,26);w.pop=1.2;if(Math.hypot(20.5*TS-P.x,21.6*TS-P.y)<320){addFx(20.5*TS,21.6*TS-30,'PLOPP!','#ffd23f',1.2);sfx('puff');}}}}
 skl().forEach(d=>{
  if(!YK[d.k])return;
  if(d.cd>0&&!KEVK[d.k])d.cd-=dt;
  d.say=(d.say||4)-dt;if(d.say<=0){d.say=rf(7,12);if(YKS[d.k]&&Math.hypot(d.x-P.x,d.y-P.y)<300&&!(d.k==='rasa'))addFx(d.x,d.y-30,pick(YKS[d.k]),'#fff2b0',1.8);}
  if(d.k==='herb'||KEVK[d.k])return;
  const near=Math.hypot(d.x-P.x,d.y-P.y)<44;
  if(near){d.a=Math.atan2(P.y-d.y,P.x-d.x);return;}
  const r=d.k==='truus'?420:d.k==='bade'?260:70,sp=d.k==='truus'?52:d.k==='bade'?26:16;
  leash(d,d.hx,d.hy,r);if(d.k==='bade'&&d.y>17.3*TS){d.a=-Math.PI/2;d.steer=1.5;}steerStep(d,dt,sp);
 });
}
Object.assign(RP,{ski:{mx:300,ac:90,br:280,dr:22,tn:2.6,r:8,g:100}});
Object.assign(RN,{ski:'Ski'});
Object.assign(RMSG,{ski:['Ski angeschnallt! Hoch gibt Schuss, Runter bremst (Pizza!), Links und Rechts lenken.','Bindung klickt, Brille runter. Ab geht die Post!']});
IMMO.forEach(q=>{q.i=q.i*20;});
function felderStatic(c){
 const x0=3*TS,x1=20*TS,y0=4*TS,y1=13*TS+20;
 for(let x=x0+12;x<x1;x+=40){
  c.fillStyle='rgba(0,0,0,.18)';c.fillRect(x+3,y0+8,3,y1-y0);
  c.strokeStyle='#6a4a2a';c.lineWidth=3;c.beginPath();c.moveTo(x,y0);c.lineTo(x,y1);c.stroke();
  c.strokeStyle='#3f9a3f';c.lineWidth=5;c.beginPath();
  for(let y=y0;y<y1;y+=4){const o=Math.sin(y*.09+x)*6;if(y===y0)c.moveTo(x+o,y);else c.lineTo(x+o,y);}
  c.stroke();c.lineWidth=1;
  for(let y=y0+16;y<y1-6;y+=26){const o=Math.sin(y*.09+x)*6,sd=((y/26)|0)%2?1:-1;c.fillStyle='#a8d86a';c.beginPath();c.ellipse(x+o+sd*8,y+4,3.4,5.6,0,0,6.283);c.fill();c.fillStyle='#2f8a3a';c.beginPath();c.ellipse(x+o-sd*7,y-4,6,3.4,sd*.5,0,6.283);c.fill();}
 }
 const h0=28*TS,h1=45*TS;
 for(let x=h0+14;x<h1;x+=36)for(let y=y0+22;y<y1;y+=40){
  c.fillStyle='rgba(0,0,0,.15)';c.beginPath();c.ellipse(x+3,y+4,10,4,0,0,6.283);c.fill();
  c.lineCap='round';
  c.strokeStyle='#3a8a3a';c.lineWidth=4;c.beginPath();for(let k=-2;k<=2;k++){c.moveTo(x,y);c.lineTo(x+k*8,y-20+Math.abs(k)*5);}c.stroke();
  c.strokeStyle='#5cb85c';c.lineWidth=1.5;c.beginPath();for(let k=-2;k<=2;k++){c.moveTo(x,y);c.lineTo(x+k*8,y-20+Math.abs(k)*5);}c.stroke();
  c.lineCap='butt';c.lineWidth=1;
 }
}
const GBY=[3.6,8.1,12.6,17.1,21.6,26.1],GBL=6,GBR=43;
function gbPath(){
 const p=[[3.4,3.6]];
 GBY.forEach((y,i)=>{
  const dir=i%2===0?1:-1,xs=dir>0?GBL:GBR,xe=dir>0?GBR:GBL;
  for(let k=0;k<=19;k++){const x=xs+(xe-xs)*k/19,f=(x-GBL)/(GBR-GBL);p.push([x,y+.7*Math.sin(f*Math.PI*4)]);}
  if(i<GBY.length-1){const cy=y+2.25,r=2.25;for(let k=1;k<6;k++){const a=-Math.PI/2+k*Math.PI/6;p.push(dir>0?[xe+Math.cos(a)*r*.9,cy+Math.sin(a)*r]:[xe-Math.cos(a)*r*.9,cy+Math.sin(a)*r]);}}
 });
 p.push([3.4,26.6]);
 return p;
}
const GBP=gbPath();
const GBLIFT=[[2.3,27.6],[1.4,26],[1.4,3.2],[3.4,3.6]];
const GBFANS=[[14,5.6],[30,5.6],[22,10.1],[12,14.6],[34,14.6],[26,19.1],[16,23.6],[36,23.6]];
const GBBUMP=[.31,.64];
function genGamsbahn(z,H){
 const zs=H.zs,zg=H.zg,zf=H.zf,mk=H.mk,R=H.R;
 zf(0,0,ZW,ZH,SN);
 for(let x=0;x<ZW;x++){const h=1+Math.round(Math.abs(Math.sin(x*.5))*1.2);for(let y=0;y<h;y++)zs(x,y,RK);}
 for(let i=0;i<320;i++){const x=R(1,ZW-2),y=R(3,ZH-2);if(zg(x,y)===SN)zs(x,y,TR);}
 kLineTiles(H,GBP,1.2,SN,[RK]);kLineTiles(H,GBLIFT,1,SN,[RK]);
 GBFANS.forEach(q=>{for(let j=-1;j<=1;j++)for(let i=-1;i<=1;i++)if(zg(Math.floor(q[0])+i,Math.floor(q[1])+j)===TR)zs(Math.floor(q[0])+i,Math.floor(q[1])+j,SN);});
 for(let j=26;j<ZH;j++)for(let i=0;i<14;i++)if(zg(i,j)===TR)zs(i,j,SN);
 {const m=mk('gbahn','sk',4,28,'Gondel Gamsblitz','Gondel: nochmal hoch');m.sk='gbahn';m.col='#5fd0ff';}
 z.fans=GBFANS.map((q,i)=>({x:q[0]*TS,y:q[1]*TS,col:pick(['#e5504d','#2e86c1','#f1c40f','#9b59b6','#2ecc71']),hat:pick(['#e5504d','#fff','#2e86c1']),cd:0,j:0,k:i%3===0?'gams':'fan'}));
}
function gbRide(force){
 kpStart({force:!!force,pts:GBP,v0:70,acc:170,vmax:440,ctl:true,sled:true,trail:'#fff',curve:['Haarnadel!','Steilkurve!','Huiii!','Festhalten!','Kurve!'],shout:['WUIII!','Juhu!','Schneller!'],
  hf:p=>{for(const b of GBBUMP){const d=(p-b)/.008;if(Math.abs(d)<1)return(1-d*d)*30;}return 0;},
  msg:'Gamsblitz! Hoch: anschieben und ducken, Runter: bremsen. Sechs Geraden, fünf Haarnadeln, zwei Sprunghügel!',end:c=>{
  const t=c.t,old=G.gbRec;if(!old||t<old)G.gbRec=t;
  G.rodel=(G.rodel||0)+1;mood(16,'+16 Gamsblitz');xpAdd(8);sfx('win');
  for(let i=0;i<16;i++)FX.push({x:P.x+rf(-8,8),y:P.y+rf(-6,6),vx:rf(-70,70),vy:rf(-90,-10),g:160,t:0,life:.8,dot:'#fff',r:rf(1.5,3)});
  const f=freeSpot(4*TS+16,27*TS);P.x=f.x;P.y=f.y;
  toast('Ziel! Die große Gamsblitz-Bahn in '+kTime(t)+'. '+(old&&t<old?'Neuer Bahnrekord!':old?'Dein Rekord: '+kTime(old)+'.':'Deine erste Fahrt, gleich der Rekord!')+' Die Gams am Ziel hält eine Zehn hoch.');
 }});
}
function gbMenu(){
 const r=G.gbRec;
 mdl('Gondel Gamsblitz','Die Gondel bringt dich in fünf Minuten auf den Gipfel. Oder in zwanzig Sekunden, wenn der Gondelfahrer gut drauf ist. Schlitten gibt es oben.'+(r?' Dein Rekord: '+kTime(r)+'.':''),[['Mit der Gondel hoch und nochmal runter','yk:gb:again']]);
}
function gbFromAlps(){
 if(fade)return;
 startFade('Die Gondel schwebt über verschneite Tannen zum Gipfel. Oben wartet die große Gamsblitz-Bahn.',()=>{enterZone('gamsbahn');UI.modal=null;gbRide(true);});
}
const PACT={
 kaffee:{s:['Mmh, Kaffee!','Mein dritter heute. Oder vierter?','Hafermilch, extra Schaum!','Ohne Kaffee geht hier nix.'],c:'„Guten Kaffee noch!“ wünschen',r:['„Danke! Der ist mit extra Liebe gebrüht.“','„Willst du mal riechen? Nur riechen!“'],sip:1},
 bier:{s:['Prost!','Feierabendbier!','Ein Schlückchen in Ehren.','Hopfen und Malz!'],c:'„Prost!“ sagen',r:['„Prost! Auf Rheinhanfen!“','„Prösterchen! Und auf die Tauben.“'],sip:1},
 doener:{s:['Mit alles und scharf!','Döner macht schöner.','Die Soße läuft bis zum Ellbogen.'],c:'„Guten Appetit!“ wünschen',r:['„Danke! Willst du abbeißen? War nur Spaß.“','„Mmpf! Mmpf mmpf!“ Das heißt wohl Danke.'],sip:1},
 eis:{s:['Erdbeer-Vanille!','Es tropft schon wieder!','Hirnfrost! Hirnfrost!'],c:'„Lecker Eis!“ sagen',r:['„Drei Kugeln! Eine für jede Laune.“','„Die Waffel ist das Beste.“'],sip:1},
 brezel:{s:['Frisch vom Bäcker!','Das Salz ist das Beste.','Knusper, knusper!'],c:'„Guten Appetit!“ wünschen',r:['„Danke! Die ist noch warm.“'],sip:1},
 uhr:{s:['Guck mal, meine neue Uhr!','Sie zeigt sogar die Zeit an!','Wasserdicht bis zur Badewanne!','Die zählt meine Schritte. Ich bin bei zwölf.'],c:'Die neue Uhr bewundern',r:['„Danke! Sie geht sieben Minuten vor. Absichtlich.“','„Die leuchtet sogar im Dunkeln. Und im Hellen.“']},
 outfit:{s:['Neue Jacke! Wie findest du sie?','Die Schuhe sind neu. Sie quietschen noch.','Sonnenbrille! Auch drinnen.','Der Hut ist von Oma.'],c:'Das neue Outfit loben',r:['„Endlich merkt es mal jemand!“','„Alles aus dem Angebot! Fühlt sich trotzdem teuer an.“']},
 zeitung:{s:['Steht nix drin. Wie immer.','Hier: Ente gewinnt Wahl!','Das Horoskop sagt: Pommes.'],c:'Nach den Neuigkeiten fragen',r:['„Ein Wal wurde im Kanal gesichtet. Er hat nach dem Weg gefragt.“','„Aliens haben im Büdchen Pils gekauft. Kistenweise!“','„Der Bürgermeister hat seinen Hut verloren. Der Hut ist jetzt Bürgermeister.“']},
 handy:{s:['Moment, Selfie!','Kein Empfang. Typisch.','Akku drei Prozent!'],c:'Für ein Selfie posieren',r:['Klick! „Du hast die Augen zu. Nochmal!“ Klick! „Perfekt.“']},
 hund:{s:['Bello, bei Fuß!','Er will nur spielen!','Wer ist ein guter Junge?'],c:'Den Hund streicheln',r:['Der Hund wedelt so doll, dass er fast abhebt.','Der Hund legt sich auf den Rücken. Bauchkraulen!']},
 tueten:{s:['Alles im Angebot!','Ich wollte nur Milch kaufen.','Shoppen macht hungrig.'],c:'Nach den Schnäppchen fragen',r:['„Drei Gummienten zum Preis von zwei! Wer kann da Nein sagen?“']},
 blumen:{s:['Für meine Liebste!','Hoffentlich gefallen sie ihr.','Die duften!'],c:'„Schöne Blumen!“ sagen',r:['„Danke! Willst du eine? Hier, die gelbe.“']},
 ballon:{s:['Mein Ballon!','Guck mal, ein Ballon!'],c:'Den Ballon bewundern',r:['„Der ist von Flocke aus dem Freizeitpark!“']}
};
const PSIP={kaffee:1,bier:1,doener:1,eis:1,brezel:1};
const KCHAT=[
 ['Neue Uhr?','Ja! Sie geht nach, aber mit Stil.'],['Schönes Wetter heute!','Hab ich extra bestellt.'],['Hast du gehört? Die Enten streiken.','Für mehr Brotkrümel?'],
 ['Ist das ein neues Hemd?','Nein, das alte, nur gebügelt!'],['Was gibt es zum Mittag?','Currywurst. Wie seit 1987.'],['Kaffee oder Tee?','Ja.'],
 ['Ich hab ein Ufo gesehen!','War das nicht das Pizzataxi?'],['Gehst du ins Freibad?','Nur wenn die Rentner-Jury nicht da ist.'],['Wo ist dein Hund?','Mit dem Rattenfänger unterwegs.'],
 ['Schicke Schuhe!','Danke, die laufen von allein.'],['Weißt du, wie spät es ist?','Kurz nach jetzt.'],['Ich geh joggen.','Bis zum Büdchen?'],
 ['Hast du Hanfred gesehen?','Der schläft im Imbiss. Wie immer.'],['Mein Wellensittich spricht Holländisch.','Echt? Was sagt er?'],['Morgen kommt die Raumkapsel wieder.','Ich stell schon mal Bier kalt.'],
 ['Neue Frisur?','Nein, Wind.'],['Ich hab im Lotto gewonnen!','Wie viel?','Ein Los.'],['Der Baron war wieder da.','Auf der Kanonenkugel?']
];
let KBUB=3,KCHT=6,KQ=[];
function pActPick(p){
 if(p.kid)return pick(['eis','eis','ballon','none']);
 if(p.teen)return pick(['handy','handy','eis','outfit','none']);
 let k=pick(['kaffee','kaffee','doener','eis','brezel','uhr','uhr','outfit','outfit','zeitung','handy','hund','tueten','blumen','bier','none','none']);
 if(k==='bier'&&(inNoGo(p.x,p.y)||minorNear(p.x,p.y,180)||ZONE))k='kaffee';
 return k;
}
function pActTick(dt){
 KBUB-=dt;KCHT-=dt;
 for(let i=KQ.length-1;i>=0;i--){const q=KQ[i];q.t-=dt;if(q.t<=0){addFx(q.p.x,q.p.y-28,q.txt,'#fff2b0',2.2,-14);KQ.splice(i,1);}}
 const n=peds.length;let cand=[];
 for(let i=0;i<n;i++){
  const p=peds[i];if(p.snow||p.st==='lie')continue;
  p.actT=(p.actT===undefined?rf(5,40):p.actT)-dt;
  if(p.act===undefined||p.actT<=0){p.act=pActPick(p);p.actT=rf(40,80);if(p.act==='ballon')p.bcol=pick(['#ff4d7a','#5ff0ff','#ffd23f','#7bd86a']);if(p.act==='outfit')p.ov=rnd(0,2);}
  if(p.act==='none')continue;
  if(p.act==='bier'&&(inNoGo(p.x,p.y)||minorNear(p.x,p.y,160)))p.act='kaffee';
  if(PSIP[p.act]&&p.st==='walk'){p.sipT=(p.sipT||rf(3,9))-dt;if(p.sipT<=0){p.sipT=rf(6,12);p.st='sip';p.stT=1.3;}}
  const d=Math.hypot(p.x-P.x,p.y-P.y);
  if(d<330)cand.push(p);
 }
 if(KBUB<=0&&cand.length){KBUB=rf(2.5,5);const p=pick(cand);addFx(p.x,p.y-26,pick(PACT[p.act].s),'#fff2b0',1.9,-14);if(p.act==='hund'&&chance(.5))setTimeout(()=>addFx(p.x-Math.cos(p.a)*16,p.y-Math.sin(p.a)*16-12,'Wuff!','#ffe08a',1.2),700);}
 for(let i=0;i<n;i++){const p=peds[i],m=p.meet;if(!m)continue;
  p.meetT-=dt;
  if((p.st!=='walk'&&p.st!=='sip')||(m.st!=='walk'&&m.st!=='sip')||p.meetT<=0||m.meet!==p){p.meet=null;continue;}
  const dd=Math.hypot(m.x-p.x,m.y-p.y);p.a=Math.atan2(m.y-p.y,m.x-p.x);
  if(dd<44){const c=pick(KCHAT);p.st='chat';m.st='chat';p.stT=m.stT=2.2*c.length+1.4;m.a=p.a+Math.PI;p.meet=null;m.meet=null;c.forEach((t,k)=>KQ.push({p:k%2?m:p,txt:t,t:.2+k*2.1}));}
 }
 if(KCHT<=0){
  KCHT=1.5;
  const L=peds.filter(p=>!p.kid&&!p.snow&&!p.meet&&p.st==='walk'&&Math.hypot(p.x-P.x,p.y-P.y)<480);
  outer:for(let i=0;i<L.length;i++)for(let j=i+1;j<L.length;j++){
   const a=L[i],b=L[j],ab=Math.hypot(a.x-b.x,a.y-b.y);if(ab>170||!kWalkLine(a,b))continue;
   a.meet=b;b.meet=a;a.meetT=b.meetT=10;a.sipT=b.sipT=12;KCHT=rf(5,9);
   break outer;
  }
 }
}
function kWalkLine(a,b){const n=Math.ceil(Math.hypot(b.x-a.x,b.y-a.y)/12);for(let i=1;i<n;i++){const x=a.x+(b.x-a.x)*i/n,y=a.y+(b.y-a.y)*i/n,tx=Math.floor(x/TS),ty=Math.floor(y/TS),t=tget(tx,ty);if(t===RD||t===DK||isSolid(tx,ty))return false;}return true;}
function pActDraw(p){
 const k=p.act;if(!k||k==='none'||p.snow||p.st==='lie'||p.st==='dance'||p.st==='dazed'||p.st==='polo'||p.st==='party')return;
 const sc=p.kid?.72:p.teen?.88:1,a=p.a,sip=p.st==='sip';
 const hx=p.x+Math.cos(a+(sip?.35:1.15))*(sip?7:9)*sc,hy=p.y+Math.sin(a+(sip?.35:1.15))*(sip?7:9)*sc;
 if(k==='kaffee'){ctx.fillStyle='#f4f4f4';ctx.fillRect(hx-2.6,hy-3.2,5.2,6.4);ctx.fillStyle='#6a3a1a';ctx.fillRect(hx-2.2,hy-3.2,4.4,1.6);ctx.fillStyle='#c0392b';ctx.fillRect(hx-2.6,hy-.4,5.2,1.6);const s=(timeNow*.8+p.x*.01)%1;ctx.fillStyle='rgba(255,255,255,'+(.6*(1-s))+')';circle(hx+Math.sin(s*6)*1.5,hy-5-s*8,1.5);}
 else if(k==='bier'){ctx.fillStyle='#7a4a12';ctx.fillRect(hx-1.7,hy-3.6,3.4,7.2);ctx.fillRect(hx-.9,hy-6.6,1.8,3.2);ctx.fillStyle='#f4f0d8';ctx.fillRect(hx-1.7,hy-1.4,3.4,2.4);}
 else if(k==='doener'){ctx.fillStyle='#e8c88a';ctx.beginPath();ctx.ellipse(hx,hy,3.2,4.8,a,0,6.283);ctx.fill();ctx.fillStyle='#4a9a3a';circle(hx-1,hy-2,1.2);ctx.fillStyle='#d63a3a';circle(hx+1,hy-1,1);ctx.fillStyle='#f4f4f4';circle(hx,hy-3,1);}
 else if(k==='eis'){ctx.fillStyle='#d9a560';ctx.beginPath();ctx.moveTo(hx-2.4,hy-1);ctx.lineTo(hx+2.4,hy-1);ctx.lineTo(hx,hy+5);ctx.closePath();ctx.fill();ctx.fillStyle=p.kid?'#ff9ec7':'#f8e8c8';circle(hx,hy-2.4,2.8);ctx.fillStyle='#ff6f9e';circle(hx+.6,hy-4.6,2);}
 else if(k==='brezel'){ctx.strokeStyle='#a8622a';ctx.lineWidth=1.8;ctx.beginPath();ctx.arc(hx-1.6,hy,2.2,0,6.283);ctx.arc(hx+1.6,hy,2.2,0,6.283);ctx.stroke();ctx.lineWidth=1;}
 else if(k==='uhr'){const wx=p.x+Math.cos(a-1.15)*9*sc,wy=p.y+Math.sin(a-1.15)*9*sc;ctx.fillStyle='#e8c040';circle(wx,wy,2);ctx.fillStyle='#fff';circle(wx,wy,1.1);if(Math.sin(timeNow*3+p.x)>.93){ctx.fillStyle='#fff';ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.fillText('✦',wx+3,wy-4);ctx.textAlign='start';}}
 else if(k==='outfit'){ctx.save();ctx.translate(p.x,p.y);ctx.scale(sc,sc);ctx.rotate(a);if(p.ov===0){ctx.fillStyle='#111';ctx.fillRect(1.6,-3.4,1.8,6.8);ctx.fillStyle='rgba(120,200,255,.6)';ctx.fillRect(1.8,-3,1.2,2.4);}else if(p.ov===1){ctx.fillStyle='#e5504d';circle(-.6,0,5.6);ctx.fillStyle='#ffd23f';circle(-.6,0,3);}else{ctx.fillStyle='#9b59b6';ctx.fillRect(-5,-6.4,9,2.2);ctx.fillRect(-5,4.2,9,2.2);}ctx.restore();}
 else if(k==='zeitung'){const zx=p.x+Math.cos(a)*7*sc,zy=p.y+Math.sin(a)*7*sc;ctx.save();ctx.translate(zx,zy);ctx.rotate(a);ctx.fillStyle='#f4f0e6';ctx.fillRect(-2,-6,4,12);ctx.fillStyle='#9a9a9a';ctx.fillRect(-1.4,-4.6,2.8,1);ctx.fillRect(-1.4,-2,2.8,1);ctx.fillRect(-1.4,.6,2.8,1);ctx.fillRect(-1.4,3.2,2.8,1);ctx.restore();}
 else if(k==='handy'){ctx.fillStyle='#1a1a1a';ctx.fillRect(hx-1.8,hy-3,3.6,6);ctx.fillStyle='rgba(120,220,255,'+(.6+.3*Math.sin(timeNow*5+p.y))+')';ctx.fillRect(hx-1.2,hy-2.4,2.4,4.4);}
 else if(k==='hund'){const dx=p.x-Math.cos(a)*16+Math.sin(timeNow*4+p.x)*1.5,dy=p.y-Math.sin(a)*16;ctx.strokeStyle='#c0392b';ctx.beginPath();ctx.moveTo(hx,hy);ctx.lineTo(dx,dy);ctx.stroke();ctx.save();ctx.translate(dx,dy);ctx.rotate(a);ctx.fillStyle=p.col===PCOL[0]?'#f4f4f4':'#8a5a2a';ctx.beginPath();ctx.ellipse(0,0,5.6,3.4,0,0,6.283);ctx.fill();circle(5.6,0,2.8);ctx.fillStyle='#3a2a1a';circle(7.6,0,1);ctx.fillRect(3.6,-3.6,2,2);ctx.fillRect(3.6,1.6,2,2);ctx.fillStyle=ctx.fillStyle;ctx.restore();}
 else if(k==='tueten'){const bx=p.x+Math.cos(a-1.15)*9*sc,by=p.y+Math.sin(a-1.15)*9*sc;ctx.fillStyle='#e5604d';ctx.fillRect(hx-3,hy-2,6,6);ctx.fillStyle='#2e86c1';ctx.fillRect(bx-3,by-2,6,6);ctx.fillStyle='#fff';ctx.fillRect(hx-1,hy-2,2,1);ctx.fillRect(bx-1,by-2,2,1);}
 else if(k==='blumen'){ctx.strokeStyle='#2f8a3a';ctx.beginPath();ctx.moveTo(hx,hy+3);ctx.lineTo(hx,hy-3);ctx.stroke();['#ff5f9e','#ffd23f','#e5504d'].forEach((c,i)=>{ctx.fillStyle=c;circle(hx-2+i*2,hy-4-(i%2)*1.5,1.8);});}
 else if(k==='ballon'){drawBal(p.x,p.y,p.bcol||'#ff4d7a');}
}
const KEVK={rasa:1,astro:1,muench:1,lore:1,ratt:1,ratte:1,taube:1,maxm:1,moritz:1,till:1};
Object.assign(YK,{rasa:{n:'Raumkapsel Hopfen 1'},astro:{n:'Astronautin'},muench:{n:'Baron Münchhausen'},lore:{n:'Loreley'},ratt:{n:'Der Rattenfänger'},ratte:{n:'Ratte'},taube:{n:'Taube'},maxm:{n:'Max'},moritz:{n:'Moritz'},till:{n:'Till Eulenspiegel'},ruebe:{n:'Rübezahl'}});
Object.assign(YKS,{muench:['Alles wahr! Fast.','Ich war schon auf dem Mond!','Eine Kugel, ein Baron!'],lore:['♪ Lalala ♪','♪ Ich weiß nicht, was soll es bedeuten ♪','Hat jemand meinen Kamm gesehen?'],ratt:['♪ Düdeldü ♪','Links, zwo, drei, vier!','Wir räumen auf!'],maxm:['Hihi!','Pssst!','Das wird ein Spaß!'],till:['Ich nehme alles wörtlich!','Spieglein, Spieglein!','Huhu, sagt die Eule.'],ruebe:['Achtundzwanzig, neunundzwanzig ...','Wer stört meine Rüben?','Hohoho!'],astro:['Houston, wir haben Durst!','Noch drei Kisten!','Für Planet Krümel!']});
let KET=40,KEL='';
const MUST=['„Ich bin einmal auf einer Kanonenkugel ins feindliche Lager geflogen. Auf halbem Weg kam eine Kugel zurück, da bin ich umgestiegen. Bequemer.“','„Ich steckte mit meinem Pferd im Sumpf. Da habe ich mich am eigenen Schopf herausgezogen. Das Pferd gleich mit.“','„Ich habe einmal zwölf Enten mit einer einzigen Schnur gefangen. Dann sind sie losgeflogen und haben mich nach Hause getragen.“','„Mein Pferd wurde einmal in der Mitte durchgeteilt. Die hintere Hälfte graste gemütlich weiter. Wir haben es wieder zusammengenäht, mit Lorbeerzweigen.“','„Ich bin an einer Bohnenranke auf den Mond geklettert. Dort trinken alle Pils. Das wissen nur die Astronauten.“'];
const TIRAT=['„Du willst wissen, wie man schneller ans Ziel kommt? Lauf nicht so weit weg davon.“','„Du suchst dein Glück? Schau unter der Bank nach. Da liegt meistens wenigstens eine Dose.“','„Wie du reich wirst? Erst Geld verdienen, dann nicht ausgeben. Ich hab nur den zweiten Teil geschafft.“','„Was du gegen Regen tun kannst? Warten. Er hört immer irgendwann auf. Außer in Wuppertal.“'];
const LOREW=['Sie singt ein Lied über einen Schiffer, der zu sehr auf ihre Frisur geachtet hat. Er ist gegen den Felsen gefahren. Mit dem Tretboot. Nichts passiert.','Sie singt ein Lied über den Rhein, der eigentlich Rheinhanf heißen müsste. Die Tauben klatschen mit den Flügeln.','Sie singt dir ein Ständchen. Ein Radfahrer guckt zu lange hin und fährt in eine Hecke. Ihm geht es gut, er summt mit.'];
function kEvent(fk){
 const sp=skSpawn();if(!sp)return;
 const k=fk||pick(['rasa','muench','lore','ratt','maxm','till'].filter(q=>q!==KEL));KEL=k;
 const L=SKC;
 if(k==='rasa'){
  let sx=sp.x+96,sy=sp.y+6;if(!skOk(sx,sy)){sx=sp.x-96;}if(!skOk(sx,sy)){sx=sp.x;sy=sp.y+70;}
  L.push({k:'rasa',lead:true,life:150,x:sp.x,y:sp.y,a:0,st:'land',t:0,h:460,help:0,sx:sx,sy:sy,cd:0,cn:-1});
  L.push({k:'astro',i:0,x:sp.x,y:sp.y,a:0,walk:0,cd:0,say:rf(4,8)});L.push({k:'astro',i:1,x:sp.x,y:sp.y,a:0,walk:0,cd:0,say:rf(6,10)});
  sfx('rumble');toast('Achtung! Eine Raumkapsel der RASA, der Rheinhanfener Astronauten-Service-Agentur, setzt zur Landung an!');
 }else if(k==='muench'){
  L.push({k:'muench',lead:true,life:90,x:sp.x,y:sp.y,hx:sp.x,hy:sp.y,fx0:sp.x-620,fy0:sp.y-140,a:0,walk:0,steer:2,st:'fly',t:0,h:240,cd:0,say:5,lift:0});
  sfx('power');toast('Eine Kanonenkugel fliegt über die Dächer. Darauf sitzt ein Herr mit Perücke und winkt. Der Baron Münchhausen!');
 }else if(k==='lore'){
  L.push({k:'lore',lead:true,life:75,x:sp.x,y:sp.y,a:Math.PI/2,walk:0,cd:0,say:2});
  sfx('magic');toast('Auf einem Felsen mitten auf dem Gehweg sitzt eine Frau mit goldenem Haar und singt. Die Loreley! Ihr Felsen am Rhein wird gerade renoviert.');
 }else if(k==='ratt'){
  const d={k:'ratt',lead:true,life:90,x:sp.x,y:sp.y,hx:sp.x,hy:sp.y,a:sp.a,walk:0,steer:2,cd:0,say:2,n:0};L.push(d);
  for(let i=0;i<9;i++)L.push({k:i%3===2?'taube':'ratte',i:i,x:sp.x-Math.cos(sp.a)*(i+1)*13,y:sp.y-Math.sin(sp.a)*(i+1)*13,a:sp.a,walk:rf(0,6)});
  sfx('musik');toast('Ein Mann im bunten Mantel spielt Flöte. Hinter ihm marschieren Ratten und Tauben im Gleichschritt und sammeln Dosen ein. Der Rattenfänger räumt auf!');
 }else if(k==='maxm'){
  L.push({k:'maxm',lead:true,minor:1,life:80,x:sp.x,y:sp.y,hx:sp.x,hy:sp.y,a:sp.a,walk:0,steer:2,cd:0,say:3,pr:6,run:0});
  L.push({k:'moritz',minor:1,x:sp.x-16,y:sp.y,a:sp.a,walk:0,cd:0});
  sfx('pfft');toast('Zwei Lausbuben mit Strubbelfrisur schleichen durch die Stadt und kichern. Max und Moritz sind unterwegs!');
 }else{
  L.push({k:'till',lead:true,life:85,x:sp.x,y:sp.y,hx:sp.x,hy:sp.y,a:sp.a,walk:0,steer:2,cd:0,say:3,pr:8});
  sfx('ding');toast('Ein Narr mit Schellenkappe, einer Eule auf der Schulter und einem Spiegel in der Hand spaziert vorbei. Till Eulenspiegel!');
 }
}
function kSkaBerge(z){z.ska.push({k:'ruebe',x:26*TS,y:26*TS,hx:26*TS,hy:26*TS,a:0,walk:0,steer:2,say:rf(3,6),cd:0});}
function kEvTick(dt){
 if(ZONE)return;
 if(!SKC.length&&wanted===0&&!P.inCar&&!P.coast){KET-=dt;if(KET<=0){KET=rf(60,120);kEvent();}}
 if(!SKC.length)return;
 const ld=SKC.find(d=>d.lead);if(!ld||!KEVK[ld.k])return;
 let end=false;
 SKC.forEach(d=>{
  if(!KEVK[d.k])return;
  if(d.cd>0)d.cd-=dt;
  const near=Math.hypot(d.x-P.x,d.y-P.y)<44;
  if(d.k==='rasa'){
   d.t+=dt;d.life=Math.max(d.life,30);
   const fl=()=>{for(let i=0;i<2;i++)FX.push({x:d.x+rf(-6,6),y:d.y-d.h+rf(-2,4),vx:rf(-30,30),vy:rf(20,90),t:0,life:.4,dot:pick(['#ffd23f','#ff9a3c','#e5504d','#fff']),r:rf(2,4)});};
   if(d.st==='land'){d.h=Math.max(0,d.h-dt*140);fl();if(d.h<=0){d.st='load';d.t=0;shake=Math.max(shake,.4);sfx('bonk');for(let i=0;i<14;i++)FX.push({x:d.x+rf(-20,20),y:d.y+rf(-4,8),vx:rf(-60,60),vy:rf(-30,10),t:0,life:.9,sm:1,r:rf(3,6)});toast('Zwei Astronauten steigen aus, winken und schleppen Bierkisten aus dem Büdchen in die Kapsel. Für die Aliens auf Planet Krümel!');}}
   else if(d.st==='load'){d.cr=Math.min(12,Math.floor(d.t*.36)+d.help);if(d.cr>=12||d.t>45){d.st='count';d.t=0;d.cn=4;toast('Alles verladen! Countdown läuft.');}}
   else if(d.st==='count'){const n=3-Math.floor(d.t);if(n!==d.cn&&n>=0){d.cn=n;addFx(d.x,d.y-70,n>0?String(n):'Zündung!','#ffd23f',1);sfx(n>0?'tick':'power');}if(d.t>=3.6){d.st='lift';d.t=0;}}
   else if(d.st==='lift'){d.h+=dt*(80+d.t*260);fl();shake=Math.max(shake,.15);if(d.h>900){end=true;mood(5,'+5 Abflug');toast('Die Raumkapsel düst davon. Ganz oben blinkt sie dreimal. Das heißt auf Alien: Prost!');}}
  }else if(d.k==='astro'){
   const r=SKC.find(q=>q.k==='rasa');if(!r)return;
   if(r.st!=='load'){d.x=r.x+(d.i?14:-14);d.y=r.y+16;d.car=0;return;}
   const ph=((r.t*.18)+d.i*.5)%1,go=ph<.5,f=go?ph*2:(1-ph)*2,ax=r.sx,ay=r.sy,bx=r.x+(d.i?14:-14),by=r.y+14;
   const nx=ax+(bx-ax)*f,ny=ay+(by-ay)*f;d.a=Math.atan2(ny-d.y,nx-d.x);d.x=nx;d.y=ny;d.walk+=dt*8;d.car=go;
  }else if(d.k==='muench'){
   d.t+=dt;
   if(d.st==='fly'){const f=Math.min(1,d.t/3);d.x=d.fx0+(d.hx-d.fx0)*f;d.y=d.fy0+(d.hy-d.fy0)*f;d.h=240*(1-f)+Math.sin(f*Math.PI)*60;if(f>=1){d.st='walk';d.h=0;sfx('bonk');shake=Math.max(shake,.3);for(let i=0;i<10;i++)FX.push({x:d.x+rf(-14,14),y:d.y+rf(-4,6),vx:rf(-50,50),vy:rf(-30,10),t:0,life:.8,sm:1,r:rf(3,6)});addFx(d.x,d.y-30,'Gelandet!','#ffd23f',1.2);}}
   else if(d.st==='leave'){const f=Math.min(1,d.t/2.5);d.x=d.hx+700*f;d.y=d.hy-260*f;d.h=Math.sin(f*Math.PI)*80+f*200;if(f>=1)end=true;}
   else{if(d.lift>0)d.lift-=dt;if(near){d.a=Math.atan2(P.y-d.y,P.x-d.x);}else if(d.lift<=0){leash(d,d.hx,d.hy,220);steerStep(d,dt,26);}}
  }else if(d.k==='lore'){
   if(chance(dt*2.5)&&Math.hypot(d.x-P.x,d.y-P.y)<420)addFx(d.x+rf(-16,16),d.y-46,pick(['♪','♫','♪']),'#ffe08a',1.6,-24);
   peds.forEach(p=>{if(p.st==='walk'&&Math.hypot(p.x-d.x,p.y-d.y)<150&&chance(dt*.15)){p.st='dazed';p.stT=1.4;addFx(p.x,p.y-20,pick(['Hach …','Wie schön!','Seufz.']),'#ffb0d0',1.4);}});
  }else if(d.k==='ratt'){
   if(near)d.a=Math.atan2(P.y-d.y,P.x-d.x);else{leash(d,d.hx,d.hy,380);steerStep(d,dt,30);}
   if(chance(dt*2)&&Math.hypot(d.x-P.x,d.y-P.y)<420)addFx(d.x+Math.cos(d.a)*10,d.y-26,pick(['♪','♫']),'#ffe08a',1.2,-24);
  }else if(d.k==='ratte'||d.k==='taube'){
   const pr=d.i===0?ld:SKC.find(q=>(q.k==='ratte'||q.k==='taube')&&q.i===d.i-1);if(!pr)return;
   const dx=pr.x-d.x,dy=pr.y-d.y,L2=Math.hypot(dx,dy);
   if(L2>200){d.x=pr.x;d.y=pr.y;}else if(L2>13){d.a=Math.atan2(dy,dx);d.x+=dx/L2*(L2-13)*Math.min(1,dt*6);d.y+=dy/L2*(L2-13)*Math.min(1,dt*6);d.walk+=dt*12;}
   if(d.k==='ratte'){for(let j=PICKS.length-1;j>=0;j--){const q=PICKS[j];if(Math.hypot(q.x-d.x,q.y-d.y)<20){PICKS.splice(j,1);ld.n=(ld.n||0)+1;G.clean=clamp((G.clean===undefined?40:G.clean)+.6,0,100);if(Math.hypot(d.x-P.x,d.y-P.y)<360)addFx(d.x,d.y-14,'Pieps! Pfand!','#d8f0a0',1);break;}}}
  }else if(d.k==='maxm'){
   const dp=Math.hypot(d.x-P.x,d.y-P.y);
   if(d.run>0){d.run-=dt;const a=Math.atan2(d.y-P.y,d.x-P.x);d.a=a;const nx=d.x+Math.cos(a)*84*dt,ny=d.y+Math.sin(a)*84*dt;if(skOk(nx,ny)){d.x=nx;d.y=ny;}d.walk+=dt*12;}
   else{leash(d,d.hx,d.hy,320);steerStep(d,dt,36);if(dp<60&&d.cd<=0&&!UI.modal){d.run=2.2;d.cd=8;addFx(d.x,d.y-24,pick(['Lauf, Moritz!','Hihi, weg hier!']),'#ffd23f',1.2);}}
   d.pr-=dt;if(d.pr<=0){d.pr=rf(10,16);const p=peds.find(q=>q.st==='walk'&&!q.kid&&Math.hypot(q.x-d.x,q.y-d.y)<170);if(p){p.st='dazed';p.stT=1.8;addFx(p.x,p.y-22,pick(['Meine Schnürsenkel!','Ein Frosch im Hut!','Juckpulver!','Wer hat mein Brot geklaut?']),'#ff8a65',1.6);addFx(d.x,d.y-24,'Hihi!','#ffd23f',1.2);}}
  }else if(d.k==='moritz'){
   const m=SKC.find(q=>q.k==='maxm');if(!m)return;const dx=m.x-d.x,dy=m.y-d.y,L2=Math.hypot(dx,dy);if(L2>160){d.x=m.x;d.y=m.y;}else if(L2>16){d.a=Math.atan2(dy,dx);d.x+=dx/L2*(L2-16)*Math.min(1,dt*6);d.y+=dy/L2*(L2-16)*Math.min(1,dt*6);d.walk+=dt*10;}
  }else if(d.k==='till'){
   if(near)d.a=Math.atan2(P.y-d.y,P.x-d.x);else{leash(d,d.hx,d.hy,340);steerStep(d,dt,30);}
   d.pr-=dt;if(d.pr<=0){d.pr=rf(9,15);const p=peds.find(q=>q.st==='walk'&&Math.hypot(q.x-d.x,q.y-d.y)<150);if(p){p.st='sip';p.stT=2;p.a=Math.atan2(d.y-p.y,d.x-p.x);addFx(p.x,p.y-22,pick(['Wer ist dieser schöne Mensch?','Hab ich da Petersilie im Zahn?','Oh! Ich seh ja aus wie ich!']),'#fff2b0',1.8);}}
  }
 });
 if(end)SKC.length=0;
}
function kEvDraw(d){
 const k=d.k;
 const tag=(n,off)=>{if(Math.hypot(d.x-P.x,d.y-P.y)<110){ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-off);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-off);ctx.lineWidth=1;ctx.textAlign='start';}};
 if(k==='rasa'){
  const h=d.h||0,x=d.x,y=d.y-h;
  ctx.fillStyle='rgba(0,0,0,'+Math.max(.08,.3-h/2000)+')';ctx.beginPath();ctx.ellipse(d.x+3,d.y+6,22+h*.03,8+h*.01,0,0,6.283);ctx.fill();
  if(d.st==='load'||d.st==='count'){const n=Math.max(0,12-(d.cr||0));for(let i=0;i<n;i++){const cx=d.sx+(i%3)*10-10,cy=d.sy-Math.floor(i/3)*6;ctx.fillStyle='#8a5a2a';ctx.fillRect(cx-5,cy-4,10,8);ctx.fillStyle='#e8c040';ctx.fillRect(cx-4,cy-3,8,2);}}
  if(d.st!=='load'){ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.moveTo(x-8,y+4);ctx.lineTo(x,y+18+Math.random()*12);ctx.lineTo(x+8,y+4);ctx.fill();ctx.fillStyle='#ff9a3c';ctx.beginPath();ctx.moveTo(x-5,y+4);ctx.lineTo(x,y+12+Math.random()*6);ctx.lineTo(x+5,y+4);ctx.fill();}
  ctx.fillStyle='#d63a3a';ctx.beginPath();ctx.moveTo(x-13,y);ctx.lineTo(x-22,y+8);ctx.lineTo(x-13,y-10);ctx.fill();ctx.beginPath();ctx.moveTo(x+13,y);ctx.lineTo(x+22,y+8);ctx.lineTo(x+13,y-10);ctx.fill();
  ctx.fillStyle='#f4f4f4';ctx.fillRect(x-13,y-44,26,46);ctx.fillStyle='#d63a3a';ctx.beginPath();ctx.moveTo(x-13,y-44);ctx.lineTo(x,y-66);ctx.lineTo(x+13,y-44);ctx.fill();
  ctx.fillStyle='#2e86c1';ctx.fillRect(x-13,y-10,26,4);ctx.fillStyle='#7fc8f0';circle(x,y-30,7);ctx.fillStyle='#7ad35a';circle(x,y-29,4.4);ctx.fillStyle='#111';circle(x-1.6,y-30,1);circle(x+1.6,y-30,1);
  ctx.fillStyle='#2e86c1';ctx.font='bold 8px Arial';ctx.textAlign='center';ctx.fillText('RASA',x,y-15);ctx.textAlign='start';
  tag('RASA-Kapsel „Hopfen 1“',84);
 }else if(k==='astro'){
  const r=SKC.find(q=>q.k==='rasa');if(r&&(r.st==='land'||r.st==='lift'||r.st==='count'))return;
  fig(d.x,d.y,d.a,{dress:'#f4f4f4',hair:'#e8e8e8',sk:5.4,walk:d.walk});
  ctx.fillStyle='rgba(80,150,220,.85)';circle(d.x+Math.cos(d.a)*1.5,d.y+Math.sin(d.a)*1.5,3);
  if(d.car){const cx=d.x+Math.cos(d.a)*9,cy=d.y+Math.sin(d.a)*9;ctx.fillStyle='#8a5a2a';ctx.fillRect(cx-5,cy-4,10,8);ctx.fillStyle='#e8c040';ctx.fillRect(cx-4,cy-3,8,2);}
  tag(d.i?'Kommandant Kometenkorn':'Major Malzbier',22);
 }else if(k==='muench'){
  const h=d.h||0,lf=d.lift>0?Math.abs(Math.sin(d.lift*5))*14+6:0;
  ctx.fillStyle='rgba(0,0,0,.22)';ctx.beginPath();ctx.ellipse(d.x+2,d.y+5,10,5,0,0,6.283);ctx.fill();
  if(d.st==='fly'||d.st==='leave'){ctx.fillStyle='#222';circle(d.x,d.y-h,9);ctx.fillStyle='rgba(255,255,255,.4)';circle(d.x-3,d.y-h-3,2.6);fig(d.x,d.y-h-10,Math.PI/2,{dress:'#8a1f2a',hair:'#eeeeee',hairLen:4,hat:'#1a1a1a',brim:5.6,sk:4.8,sc:.9});return;}
  fig(d.x,d.y-lf,d.a,{dress:'#8a1f2a',hair:'#eeeeee',hairLen:4,hat:'#1a1a1a',brim:5.6,sk:5,walk:d.walk});
  if(lf){ctx.strokeStyle='#eee';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(d.x-2,d.y-lf-4);ctx.lineTo(d.x-2,d.y-lf-14);ctx.stroke();ctx.lineWidth=1;}
  tag('Baron Münchhausen',28+lf);
 }else if(k==='lore'){
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(d.x+4,d.y+12,30,10,0,0,6.283);ctx.fill();
  ctx.fillStyle='#7d8590';ctx.beginPath();ctx.ellipse(d.x,d.y+4,28,16,0,0,6.283);ctx.fill();ctx.fillStyle='#9aa2ad';ctx.beginPath();ctx.ellipse(d.x-6,d.y-2,18,9,0,0,6.283);ctx.fill();ctx.fillStyle='#5a7a3a';circle(d.x+18,d.y+8,4);circle(d.x-20,d.y+10,3);
  fig(d.x,d.y-6,d.a,{dress:'#2e86c1',hair:'#f4d03f',hairLen:9,sk:5.4,skin:'#f6e6dc'});
  if(Math.sin(timeNow*2)>0){ctx.fillStyle='#e8c040';ctx.fillRect(d.x-10,d.y-12+Math.sin(timeNow*4)*3,6,2);}
  tag('Loreley',34);
 }else if(k==='ratt'){
  fig(d.x,d.y,d.a,{dress:'#e5504d',cape:'#f1c40f',hair:'#5a3a1a',hat:'#2e86c1',hat2:'#e5504d',brim:5.4,sk:5,walk:d.walk});
  ctx.strokeStyle='#c8a060';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(d.x+Math.cos(d.a)*4,d.y+Math.sin(d.a)*4);ctx.lineTo(d.x+Math.cos(d.a)*14,d.y+Math.sin(d.a)*14);ctx.stroke();ctx.lineWidth=1;
  tag('Der Rattenfänger',26);
 }else if(k==='ratte'){
  ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.fillStyle='#8a8f9a';ctx.beginPath();ctx.ellipse(0,0,5,3,0,0,6.283);ctx.fill();circle(5,0,2.2);ctx.fillStyle='#ffb0c0';circle(7,0,.9);circle(4,-2.2,1.1);circle(4,2.2,1.1);ctx.strokeStyle='#ffb0c0';ctx.beginPath();ctx.moveTo(-5,0);ctx.quadraticCurveTo(-9,Math.sin(d.walk)*4,-12,0);ctx.stroke();ctx.restore();
 }else if(k==='taube'){
  const b=Math.sin(d.walk*1.5)*1.5;ctx.save();ctx.translate(d.x,d.y);ctx.rotate(d.a);ctx.fillStyle='#8a8f9a';ctx.beginPath();ctx.ellipse(0,0,5,3.6,0,0,6.283);ctx.fill();ctx.fillStyle='#6a7080';circle(4+b,0,2.4);ctx.fillStyle='#e8a040';ctx.fillRect(6+b,-.5,2,1);ctx.restore();
 }else if(k==='maxm'||k==='moritz'){
  fig(d.x,d.y,d.a,{dress:k==='maxm'?'#2e86c1':'#e67e22',hair:k==='maxm'?'#f4d03f':'#3a2a1a',sk:4.6,walk:d.walk,sc:.74});
  ctx.fillStyle=k==='maxm'?'#f4d03f':'#3a2a1a';for(let i=0;i<3;i++)circle(d.x-2+Math.cos(d.a+Math.PI+(i-1)*.7)*4,d.y+Math.sin(d.a+Math.PI+(i-1)*.7)*4,1.4);
  if(k==='maxm'){ctx.strokeStyle='#7a5a32';ctx.beginPath();ctx.moveTo(d.x+Math.cos(d.a+1)*6,d.y+Math.sin(d.a+1)*6);ctx.lineTo(d.x+Math.cos(d.a+.5)*20,d.y+Math.sin(d.a+.5)*20);ctx.stroke();}
  else{ctx.fillStyle='rgba(180,230,255,.7)';circle(d.x+Math.cos(d.a+1.1)*7,d.y+Math.sin(d.a+1.1)*7,3);ctx.fillStyle='#4a9a3a';circle(d.x+Math.cos(d.a+1.1)*7,d.y+Math.sin(d.a+1.1)*7,1.4);}
  tag(k==='maxm'?'Max':'Moritz',20);
 }else if(k==='till'){
  fig(d.x,d.y,d.a,{dress:'#f1c40f',cape:'#e5504d',hair:'#8a5a2a',sk:5,walk:d.walk});
  ctx.fillStyle='#2ecc71';ctx.beginPath();ctx.moveTo(d.x-3,d.y-3);ctx.lineTo(d.x-9,d.y-9);ctx.lineTo(d.x+1,d.y-4);ctx.fill();ctx.fillStyle='#e5504d';ctx.beginPath();ctx.moveTo(d.x-3,d.y+3);ctx.lineTo(d.x-9,d.y+9);ctx.lineTo(d.x+1,d.y+4);ctx.fill();ctx.fillStyle='#ffd23f';circle(d.x-9,d.y-9,1.6);circle(d.x-9,d.y+9,1.6);
  const ox=d.x+Math.cos(d.a-1.6)*7,oy=d.y+Math.sin(d.a-1.6)*7;ctx.fillStyle='#8a5a2a';circle(ox,oy,3.4);ctx.fillStyle='#fff';circle(ox-1.2,oy-1,1.2);circle(ox+1.2,oy-1,1.2);ctx.fillStyle='#111';circle(ox-1.2,oy-1,.5);circle(ox+1.2,oy-1,.5);
  const mx=d.x+Math.cos(d.a+1.1)*9,my=d.y+Math.sin(d.a+1.1)*9;ctx.fillStyle='#c8ced6';circle(mx,my,3.2);ctx.fillStyle='rgba(255,255,255,.8)';circle(mx-1,my-1,1.2);
  tag('Till Eulenspiegel',26);
 }
}
function ruebeDraw(d){fig(d.x,d.y,d.a,{dress:'#5a6a3a',cape:'#3a4a2a',hair:'#9a9a9a',beard:'#f0f0f0',sk:6,walk:d.walk,sc:1.35});ctx.fillStyle='#c0602a';circle(d.x+Math.cos(d.a+1.1)*12,d.y+Math.sin(d.a+1.1)*12,3);ctx.fillStyle='#4a9a3a';circle(d.x+Math.cos(d.a+1.1)*15,d.y+Math.sin(d.a+1.1)*15,1.8);}
function kEvOpen(d){
 const k=d.k;
 if(k==='rasa'||k==='astro'){const r=SKC.find(q=>q.k==='rasa');if(!r)return;if(r.st!=='load'){toast(r.st==='land'?'Abstand halten! Die Kapsel landet gerade.':'Abstand halten! Gleich geht es nach oben.');return;}
  mdl('RASA-Kapsel „Hopfen 1“','Major Malzbier klopft gegen ihren Helm: „Wir holen Nachschub für Planet Krümel. Die Aliens dort lieben Pils, kistenweise. Blubb hat Geburtstag!“ Verladen: '+(r.cr||0)+' von 12 Kisten.',[['Kisten schleppen helfen (+15 €)','yk:ra:help'],['Fragen: Warum ausgerechnet Bier?','yk:ra:why'],['Den Countdown sprechen','yk:ra:count']]);return;}
 if(k==='muench'){if(d.st!=='walk'){toast('Der Baron ist gerade in der Luft. Winken!');return;}mdl('Baron Münchhausen','Ein Herr mit Perücke, Dreispitz und rotem Rock verbeugt sich: „Baron von Münchhausen. Alles, was ich erzähle, ist wahr. Fast immer.“',[['Eine Geschichte hören','yk:mu:story'],['Den Schopf-Trick zeigen lassen','yk:mu:schopf'],['Fragen, ob du mitfliegen darfst','yk:mu:fly']]);return;}
 if(k==='lore'){mdl('Loreley','Sie kämmt ihr goldenes Haar mit einem goldenen Kamm und summt eine Melodie, bei der sogar die Tauben stehen bleiben.',[['Zuhören','yk:lo:hear'],['Ein Lied wünschen','yk:lo:wish'],['Den Kamm halten','yk:lo:kamm']]);return;}
 if(k==='ratt'||k==='ratte'||k==='taube'){const r=SKC.find(q=>q.k==='ratt');mdl('Der Rattenfänger','Bunter Mantel, Flöte, und hinter ihm marschieren Ratten und Tauben im Gleichschritt: „Wir räumen auf! Die Ratten sind die Müllabfuhr, die Tauben die Kontrolle.“ Eingesammelt: '+((r&&r.n)||0)+(((r&&r.n)||0)===1?' Dose.':' Dosen.'),[['Mitmarschieren und tanzen','yk:rf:dance'],['Fragen, wohin es geht','yk:rf:wohin'],['Eine Ratte streicheln','yk:rf:ratte']]);return;}
 if(k==='maxm'||k==='moritz'){mdl('Max und Moritz','Zwei Lausbuben mit Strubbelfrisur grinsen dich an. Max hält eine Angelschnur, Moritz ein Glas mit einem Frosch.',[['Ermahnen','yk:mm:ermahn'],['Fragen, was der nächste Streich ist','yk:mm:next'],['Den Frosch freilassen','yk:mm:frosch']]);return;}
 if(k==='till'){mdl('Till Eulenspiegel','Ein Narr mit Schellenkappe, auf der Schulter eine Eule, in der Hand ein Spiegel: „Eule und Spiegel, daher mein Name. Frag mich was, ich nehme alles wörtlich.“',[['Um einen Rat fragen','yk:te:rat'],['In den Spiegel schauen','yk:te:spiegel'],['Die Eule streicheln','yk:te:eule']]);return;}
 if(k==='ruebe'){mdl('Rübezahl','Ein riesiger Berggeist mit Bart bis zu den Knien hockt über einem Haufen Rüben: „Siebenundzwanzig, achtundzwanzig … Jetzt hab ich mich schon wieder verzählt!“',[['Beim Rübenzählen helfen','yk:rz:zaehl'],['Nach dem Wetter fragen','yk:rz:wetter'],['Fragen, warum er Rübezahl heißt','yk:rz:name']]);return;}
}
function skAct20(p){
 if(p.indexOf('yk:')!==0)return false;
 const q=p.slice(3),pre=q.slice(0,3);
 if(['ra:','mu:','lo:','rf:','mm:','te:','rz:'].indexOf(pre)<0)return false;
 UI.modal=null;render2();
 const r=SKC.find(x=>x.k==='rasa'),mu=SKC.find(x=>x.k==='muench'),ra=SKC.find(x=>x.k==='ratt');
 if(q==='ra:help'){if(!r||r.st!=='load')return true;r.help+=3;G.cash+=15;G.stats.earned+=15;mood(5,'+5 Kisten');xpAdd(4);sfx('coin');toast(pick(['Du schleppst drei Kisten in die Kapsel. Major Malzbier salutiert: „Du hast das Zeug zum Astronauten!“','Drei Kisten verladen. Durch das Fenster winkt ein kleines grünes Gesicht: Blubb!']));return true;}
 if(q==='ra:why'){mood(3,'+3');toast(pick(['„Auf Planet Krümel gibt es kein Wasser, nur Krümel. Da braucht man was zum Runterspülen.“','„Die Aliens haben auf dem Mond eine Kneipe eröffnet: Zum Krater. Die läuft super.“','„Raketentreibstoff ist teurer. Und schmeckt schlechter.“','„Das Pfand gibt es auf Planet Krümel doppelt zurück!“']));return true;}
 if(q==='ra:count'){if(!r||r.st!=='load')return true;r.help=12;r.st='count';r.t=0;r.cn=4;mood(8,'+8 Countdown');xpAdd(5);toast('Du sprichst den Countdown! Kommandant Kometenkorn reckt den Daumen hoch.');return true;}
 if(q==='mu:story'){mood(5,'+5 Geschichte');sfx('clap');toast(pick(MUST));return true;}
 if(q==='mu:schopf'){if(mu){mu.lift=2.4;}mood(6,'+6 Staunen');sfx('magic');toast('Der Baron packt sich am eigenen Zopf, zieht kräftig, und schwebt tatsächlich eine Handbreit über dem Boden. „Siehst du? Alles wahr!“');return true;}
 if(q==='mu:fly'){if(mu&&mu.st==='walk'){mu.st='leave';mu.t=0;mu.hx=mu.x;mu.hy=mu.y;}mood(4,'+4');sfx('power');toast('„Die Kugel ist leider nur für einen. Aber pass auf, so geht das!“ Er pfeift, eine Kanonenkugel kommt angeflogen, er springt auf und ist weg.');return true;}
 if(q==='lo:hear'){mood(8,'+8 Hach');sfx('musik');toast(pick(LOREW));return true;}
 if(q==='lo:wish'){mood(5,'+5');sfx('musik');toast(pick(['Du wünschst dir ein Lied über Currywurst. Sie singt es so schön, dass Hanfred im Imbiss zu weinen beginnt.','Du wünschst dir etwas Fröhliches. Sie singt ein Lied über Enten, die Tretboot fahren. Alle schunkeln.','Du wünschst dir ein Lied über Pfandflaschen. Sie macht daraus eine Ballade. Großes Kino.']));return true;}
 if(q==='lo:kamm'){mood(4,'+4');toast('Du hältst den goldenen Kamm, während sie ihre Haare zum Zopf flicht. Der Zopf ist so lang, dass er bis zum nächsten Büdchen reicht.');return true;}
 if(q==='rf:dance'){mood(7,'+7 Marsch');sfx('musik');P.dance=3;toast('Du marschierst mit! Die Ratten machen Platz, die Tauben nicken im Takt. Eine Ratte reicht dir eine Dose.');if(G.ammo&&G.ammo.dose<40)G.ammo.dose++;return true;}
 if(q==='rf:wohin'){mood(3,'+3');toast(pick(['„Zum Pfandautomaten! Die Ratten wollen sich ein Eis kaufen.“','„Einmal durch die ganze Stadt und zurück. Danach ist alles sauber, versprochen.“']));return true;}
 if(q==='rf:ratte'){mood(5,'+5 Süß');toast('Die Ratte heißt Rüdiger, hat einen kleinen Hut und lässt sich gern hinter den Ohren kraulen.');return true;}
 if(q==='mm:ermahn'){popAdd(1);mood(3,'+3');toast('„Na gut, na gut.“ Max gibt einem Herrn sein Brot zurück, Moritz bindet zwei Schnürsenkel wieder auf. Dann kichern sie und rennen weg.');const m=SKC.find(x=>x.k==='maxm');if(m){m.run=2.4;m.cd=12;}return true;}
 if(q==='mm:next'){mood(3,'+3');toast(pick(['„Wird nicht verraten!“ Moritz zeigt auf den Frosch und zwinkert.','„Wir wollen dem Bademeister Günni die Trillerpfeife mit Seifenblasenwasser füllen!“','„Wir legen Furzkissen auf alle Bänke im Park!“']));return true;}
 if(q==='mm:frosch'){mood(5,'+5 Frosch');toast('Du lässt den Frosch frei. Er quakt dankbar und hüpft Richtung Kanal. Max und Moritz sind beleidigt, aber nur kurz.');return true;}
 if(q==='te:rat'){mood(4,'+4');toast(pick(TIRAT));return true;}
 if(q==='te:spiegel'){mood(5,'+5');toast(pick(['Im Spiegel siehst du dich. Dann zwinkert dein Spiegelbild, obwohl du nicht gezwinkert hast. Till grinst.','Du schaust in den Spiegel. „Siehst gut aus“, sagt das Spiegelbild. Till: „Der lügt nie.“']));return true;}
 if(q==='te:eule'){mood(4,'+4');toast('Die Eule heißt Professor Uhu. Sie dreht den Kopf einmal ganz herum und sagt: „Huhu.“ Mehr hat sie nicht zu sagen, aber das sehr überzeugend.');return true;}
 if(q==='rz:zaehl'){mood(6,'+6 Rüben');xpAdd(3);toast('Ihr zählt gemeinsam: 77 Rüben! Rübezahl freut sich so, dass es oben am Gipfel kurz schneit. Er schenkt dir eine Rübe.');needAdd(15,0);return true;}
 if(q==='rz:wetter'){mood(3,'+3');toast(pick(['„Morgen Schnee. Übermorgen Schnee. Danach mache ich Urlaub und es gibt Schnee.“','„Sonne! Aber nur, wenn keiner meine Rüben zählt.“']));return true;}
 if(q==='rz:name'){mood(4,'+4');toast('„Weil ich Rüben zähle! Eigentlich hasse ich den Namen. Ich wollte Herbert heißen, aber den gibt es schon auf dem Campingplatz.“');return true;}
 return true;
}
const KBEPS=[
 {who:{dress:'#2e86c1',hair:'#3a2a1a'},m:'stop',say:['Neue Uhr!','Wasserdicht!'],t:'Ein Mann bleibt stehen und zeigt dir stolz seine neue Uhr. Sie ist wasserdicht, stoßfest und geht genau sieben Minuten vor. „Absichtlich“, sagt er.'},
 {who:{dress:'#c96a9a',hair:'#e6c36a',hairLen:5},m:'pass',say:['Nicht verschütten!'],t:'Eine Frau balanciert sechs Kaffeebecher übereinander. Sie verschüttet keinen Tropfen. Eine Taube applaudiert.'},
 {who:{dress:'#ff5fd0',hair:'#3a2a1a'},m:'stop',say:['Neue Jacke!','Wie findest du sie?'],t:'Jemand dreht sich vor dir einmal im Kreis: neue Jacke, neue Schuhe, neue Sonnenbrille. „Alles im Angebot!“ Du nickst anerkennend.'},
 {who:{dress:'#8a5a2a',hair:'#c8c8c8',beard:'#c8c8c8'},m:'sit',fx:'pizza',say:['Mahlzeit!'],t:'Ein Opa setzt sich neben dich, packt eine Stulle aus, teilt sie in zwei Hälften und gibt dir eine. „Mahlzeit!“'},
 {who:{dress:'#5a6a8a',hair:'#3a2a1a'},m:'stop',say:['Psst, nicht wackeln!'],t:'Ein Mann baut auf der Bank einen Turm aus Bierdeckeln. Bei 48 Deckeln niest er. Neustart.'},
 {who:{dress:'#6a6a7a',hair:'#4a4a4a'},m:'pass',say:['Mein Hut!'],t:'Ein Herr rennt seinem Hut hinterher. Der Hut ist schneller. Er sieht aus, als hätte er einen wichtigen Termin.'},
 {who:{dress:'#f1c40f',hair:'#8a5a2a',hairLen:4},m:'pass',say:['Es tropft!'],t:'Eine Frau isst ein Eis mit sieben Kugeln. Die oberste springt ab und landet genau in der Waffel ihres Mannes. Perfekte Teamarbeit.'},
 {who:{dress:'#f4f4f4',hair:'#dddddd'},m:'pass',say:['Training für den Mond!'],t:'Ein Astronaut im Raumanzug joggt vorbei. „Training für den Mond!“, keucht er. „Da oben ist alles leichter.“'},
 {who:{dress:'#2ecc71',hair:'#3a2a1a',hairLen:3},m:'stop',say:['Selfie!'],t:'Jemand macht ein Selfie mit dir im Hintergrund, dann eins mit dir im Vordergrund. Dann zeigt er es dir: Du siehst super aus.'},
 {who:{dress:'#4a4a5a',hair:'#c8c8c8'},m:'sit',say:['Unerhört!'],t:'Ein älterer Herr liest Zeitung und schimpft über jede Seite. Beim Kreuzworträtsel wird er ganz ruhig: „Fluss in Rheinhanfen, vier Buchstaben?“'},
 {who:{dress:'#9b59b6',hair:'#f4f4f4',hairLen:4},it:'dackel',m:'pass',say:['Bei Fuß!'],t:'Eine Frau mit weißer Föhnfrisur führt einen Dackel Gassi, der exakt dieselbe Föhnfrisur hat. Beide schauen dich gleichzeitig an.'},
 {who:{dress:'#e67e22',hair:'#3a2a1a'},m:'stop',say:['Die Uhr ist neu!'],t:'Zwei Leute vergleichen ihre neuen Uhren. Die eine zeigt 14:02, die andere 14:03. Sie streiten, bis es 14:05 ist.'}
];
KBEPS.forEach(e=>BEPS.push(e));

const MHW={rec:{n:'Receiver',p:40,d:'Für jeden Anschluss einen (oder eine TV-Box)'},box:{n:'TV-Box',p:60,d:'Smart und schnell: +20 % Abo-Gebühr'},ant:{n:'Antenne',p:25,d:'Aufs Dach: schnell, aber Spürwagen können sie entdecken'},kab:{n:'Kabelrolle',p:15,d:'Heimlich verlegt: unsichtbar, nachts ohne Risiko'},tv:{n:'Fernseher',p:150,d:'Manche Kunden haben nur einen Röhrenfernseher'},tarn:{n:'Tarnset',p:30,d:'Macht aus einer Antenne einen Wäscheständer mit Socken'}};
const MHWK=['rec','box','ant','kab','tv','tarn'];
const MCT={m3u:{n:'M3U-Liste',p:50,s:3,d:3,ban:.3,k:'M3U'},stk:{n:'Stalker-Portal-Code',p:120,s:5,d:5,ban:.15,k:'STK'},xtr:{n:'Xtream-Code',p:220,s:10,d:6,ban:.1,k:'XTR'},eig:{n:'Selbst geknackt',s:4,d:5,ban:.12,k:'EIG'},mst:{n:'Master-Code',s:15,d:6,ban:.05,k:'MST'},turm:{n:'Turm-Code',s:60,d:9999,ban:0,k:'TURM'}};
const MRANK=[[0,'Kabelsalat-Azubi'],[20,'Antennen-Andi'],[60,'Code-Knacker'],[130,'Receiver-Royal'],[250,'Sender-Boss'],[450,'Entertain Master']];
const MHN=['Familie Krause','Opa Heinz','WG Chaos','Frau Becker','Familie Yilmaz','Sportbar Anpfiff','Kegelclub Alle Neune','Herr Novak','Tante Gerda','Familie Schmitz','Studenten-WG Dosenpfand','Frau Albers','Herr Petersen','Familie Kowalski','Friseur Schnittig','Oma Hilde','Familie Nguyen','Herr Özdemir','Pension Rheinblick','Familie Weber','Kiosk-Opa Erwin','Frau Lindner','Familie Rossi','Musiker-WG Bassbude','Herr Bröselmann','Familie Jansen','Frau Pinkepank','Herr Wuschel','Familie Brösel','Tierarzt Dr. Fell'];
const MWISH=['Fußball','Kochshows','Tierdokus','Krimis','Quizshows','Liebesfilme','Schlagerparty','Seifenkistenrennen','Serien am Stück','Zeichentrick für die Enkel','Wetterkanal (24 Stunden)','Heimwerker-Shows','Gartenzwerg-Weltmeisterschaft'];
const FILMS=[
 {ti:'Die Rache der Gartenzwerge',g:'Action',e:'action',p:'Udo und seine Zwergen-Gang erobern einen Baumarkt zurück. Mit Rasenmäher-Verfolgungsjagd!'},
 {ti:'Liebe in Zeiten der Currywurst',g:'Liebe',e:'liebe',p:'Eine Imbisswirtin verliebt sich in einen Lieferboten, der jeden Tag die Mayo vergisst.'},
 {ti:'Planet der Gummienten',g:'Sci-Fi',e:'froh',p:'Astronauten landen auf einem Planeten, auf dem Badeenten das Sagen haben. Quietsch!'},
 {ti:'Der Fluch des Wohnwagens',g:'Grusel',e:'grusel',p:'Ein Wohnwagen quietscht nachts. Am Ende war es nur ein Gartenzwerg mit Schluckauf.'},
 {ti:'Pommes Royale',g:'Komödie',e:'lach',p:'Ein Kartoffelbauer wird aus Versehen König von Rheinhanfen und führt die Pommespflicht ein.'},
 {ti:'Die Taube, die zu viel wusste',g:'Krimi',e:'action',p:'Eine Brieftaube löst den größten Kekskrümel-Raub der Stadtgeschichte.'},
 {ti:'Herzschmerz am Pfandautomaten',g:'Drama',e:'traurig',p:'Zwei Leergutsammler, eine letzte Flasche. Taschentücher bereithalten.'},
 {ti:'Der Wal im Kanal',g:'Familie',e:'froh',p:'Ein Wal verirrt sich in die Grachten, findet Freunde und lernt Tretboot fahren.'},
 {ti:'Sieben Minuten zu früh',g:'Komödie',e:'lach',p:'Ein Mann mit einer Uhr, die immer vorgeht. Er kommt überall zu früh, sogar zu seiner eigenen Überraschungsparty.'},
 {ti:'Mission: Mayo',g:'Action',e:'action',p:'Ein Geheimagent muss die letzte Tube Mayo der Welt beschützen. Explosionen aus Ketchup.'},
 {ti:'Die Loreley-Verschwörung',g:'Thriller',e:'grusel',p:'Warum bleiben alle Tretboote am Felsen stehen? Eine Reporterin ermittelt.'},
 {ti:'Käseritter 2: Die Rückkehr des Gouda',g:'Abenteuer',e:'action',p:'Der Käseritter reitet wieder, diesmal auf einem Holzschuh mit Turbo.'},
 {ti:'Oma Truus fährt nach Rom',g:'Komödie',e:'lach',p:'Eine 84-Jährige radelt mit Mini-Wohnwagen über die Alpen. Der Kater fährt mit.'},
 {ti:'Schneemann ohne Karotte',g:'Drama',e:'traurig',p:'Ein Schneemann sucht seine Nase. Als er sie findet, ist Frühling.'},
 {ti:'Hanfred: Der Film',g:'Doku',e:'froh',p:'Zwei Stunden Imbissleben. Die Fritteuse bekommt einen eigenen Abspann.'},
 {ti:'Brausepulver-Blues',g:'Musik',e:'liebe',p:'Eine Band aus Rheinhanfen will groß raus. Ihr einziger Hit heißt „Prickel, prickel“.'},
 {ti:'Die Nacht der tanzenden Laternen',g:'Fantasy',e:'froh',p:'Um Mitternacht tanzen alle Laternen der Stadt Walzer. Nur eine hat Rhythmus.'},
 {ti:'Abschied am Büdchen',g:'Drama',e:'traurig',p:'Der Büdchen-Opa geht in Rente. Die ganze Straße weint in die Brausetüten.'},
 {ti:'Kabelsalat (Staffel 1)',g:'Krimiserie',e:'action',s:1,p:'Zwei Kabelverleger arbeiten nachts im Geheimen. Jede Folge endet mit einem Knoten.'},
 {ti:'Die Gartenzwerge von nebenan (Staffel 2)',g:'Sitcom',e:'lach',s:1,p:'Udo zieht zu Herbert. Nichts geht gut, alles ist lustig.'},
 {ti:'WG Chaos (Staffel 4)',g:'Sitcom',e:'lach',s:1,p:'Wer hat den Joghurt gegessen? Staffel vier bringt endlich die Antwort. Fast.'},
 {ti:'Grachten-Cops (Staffel 1)',g:'Krimiserie',e:'action',s:1,p:'Zwei Polizisten im Tretboot jagen Fahrraddiebe durch die Kanäle.'},
 {ti:'Das Imperium der Tauben (Staffel 3)',g:'Fantasy-Serie',e:'grusel',s:1,p:'Die Tauben übernehmen den Marktplatz. Brotkrümel sind die neue Währung.'},
 {ti:'Pommes oder Liebe (Staffel 1)',g:'Datingshow',e:'liebe',s:1,p:'Zehn Singles, eine Fritteuse. Wer bekommt die letzte Rose aus Kartoffelstärke?'}
];
const EMO={
 lach:{m:12,w:'Du lachst Tränen!',f:'Hahaha!'},froh:{m:10,w:'Du bist glücklich und summst den Abspann mit.',f:'Hach, schön!'},
 traurig:{m:-6,w:'Schnief. Du bist traurig, aber auf die schöne Art. Taschentuch?',f:'Schnief …'},grusel:{m:5,w:'Gänsehaut! Du schaust dich auf dem Heimweg zweimal um.',f:'Huch!'},
 action:{m:8,w:'Adrenalin! Du möchtest sofort über ein Auto springen. Lieber nicht.',f:'Wumms!'},liebe:{m:0,w:'',f:'Seufz …'}
};
const MQUAL={CAM:{n:'CAM',f:.5,t:'(Man sieht einen Kopf vor der Leinwand.)'},HD:{n:'HD',f:1,t:''},'4K':{n:'4K',f:1.3,t:'(Gestochen scharf. Du siehst jede Pore des Gartenzwergs.)'}};
const INSTL=['sieht zum ersten Mal Fußball in Farbe und ruft: „Der Rasen ist ja grün!“','schaltet durch 800 Sender und bleibt beim Wetterkanal hängen.','umarmt den Receiver. Dann dich. Dann wieder den Receiver.','backt dir aus Dankbarkeit einen Kuchen in Fernbedienungs-Form.','ruft sofort die Nachbarn an. Morgen wollen die auch.','fragt, ob es einen Sender nur mit Katzenvideos gibt. Gibt es.'];
let MHS=null,HK=null,HKI=null,MPAY=0,MPAYN=0;
function medInit(){
 if(!G)return;
 if(!G.med)G.med={hw:{rec:1,box:0,ant:1,kab:1,tv:0,tarn:0},codes:[],films:[],subs:[],off:[],act:[],nid:1,skill:0,lic:{},fame:0,vids:[],neu:[],scr:0,hackT:0,tower:0,kino:0,auto:0,dreh:0,hr:-1,mark:null,loot:0};
 const M=G.med;
 if(!M.codes.length&&!M.started){M.codes.push(mkCode('m3u'));M.films.push({f:4,q:'HD'});}
 M.started=1;
 if(!M.neu.length)medNeu();
 MHWK.forEach(k=>{if(M.hw[k]===undefined)M.hw[k]=0;});
}
function hex4(){return Math.floor(Math.random()*65536).toString(16).toUpperCase().padStart(4,'0');}
function mkCode(t){const c=MCT[t];return{id:G.med.nid++,t:t,n:c.k+'-'+hex4()+'-'+pick(['HOPF','HANF','KÄSE','GOUDA','RHEIN','PIXL','MAYO','ENTE']),s:c.s+(t==='eig'?(G.med.skill||0)*2:0),d:c.d+(t==='eig'?(G.med.skill||0):0),ban:false};}
function medHouses(){
 if(MHS)return MHS;
 const B=CITY.BLD,T=CITY.T,W=CITY.MW,out=[];
 B.forEach(b=>{if(b.k!=='house'||b.n)return;const dx=Math.floor(b.x+b.w/2),dy=b.y+b.h;if(T[dy*W+dx]!==SW)return;const x=dx*TS+16,y=dy*TS+14;if(out.length>=30||out.some(o=>Math.hypot(o.x-x,o.y-y)<4*TS))return;out.push({id:dx+'_'+dy,x:x,y:y,b:b});});
 out.forEach((h,i)=>{h.n=MHN[i%MHN.length];});
 MHS=out;return out;
}
function mHouse(id){return medHouses().find(h=>h.id===id);}
function mCode(id){return G.med.codes.find(c=>c.id===id);}
function mUsed(c){return G.med.subs.filter(s=>s.c===c.id).length;}
function mCodeOk(c){return c&&!c.ban&&c.d>0;}
function medFreeCode(){let best=null;G.med.codes.forEach(c=>{if(!mCodeOk(c)||mUsed(c)>=c.s)return;if(!best||c.t==='turm'||(best.t!=='turm'&&c.d>best.d))best=c;});return best;}
function mSlots(){let f=0,t=0;G.med.codes.forEach(c=>{if(mCodeOk(c)){t+=c.s;f+=Math.max(0,c.s-mUsed(c));}});return{f:f,t:t};}
function medFame(){return Math.floor((G&&G.med&&G.med.fame)||0);}
function medRankI(){const f=medFame();let i=0;MRANK.forEach((r,k)=>{if(f>=r[0])i=k;});return i;}
function medRank(){return MRANK[medRankI()][1];}
function medRankPct(){const i=medRankI();if(i>=MRANK.length-1)return 100;const a=MRANK[i][0],b=MRANK[i+1][0];return Math.round((medFame()-a)/(b-a)*100);}
function fameAdd(v){if(!G.med)return;const r0=medRankI();G.med.fame=Math.max(0,(G.med.fame||0)+v);const r1=medRankI();if(r1>r0){sfx('win');toast('Neuer Rang: '+MRANK[r1][1]+'! '+(r1===MRANK.length-1?'Du bist der Entertain Master! In Hollyhanf wartet dein Stern auf dem Walk of Fame.':'Ganz Rheinhanfen redet über dich.'));if(r1===MRANK.length-1)G.med.star=1;}}
function medSubsOk(){return G.med.subs.filter(s=>s.ok).length;}
function medDayFee(){return G.med.subs.reduce((a,s)=>a+(s.ok?s.fee:0),0);}
function medSum(){if(!G||!G.med)return '';const n=G.med.subs.length,b=n-medSubsOk();return n+' Kunden'+(b?' ('+b+' mit Störung)':'')+' · '+eur(medDayFee())+' pro Tag';}
function medNeu(){const L=FILMS.map((f,i)=>i).filter(i=>!FILMS[i].s);const out=[];while(out.length<3){const i=pick(L);if(out.indexOf(i)<0)out.push(i);}G.med.neu=out;}
function medHasFilm(f){return G.med.films.find(x=>x.f===f);}
function medAddFilm(f,q){const o=medHasFilm(f),r={CAM:0,HD:1,'4K':2};if(o){if(r[q]>r[o.q])o.q=q;return false;}G.med.films.push({f:f,q:q});return true;}
function medSync(){
 const M=CITY.MKS;for(let i=M.length-1;i>=0;i--)if(M[i].med)M.splice(i,1);
 if(!G||!G.med)return;
 const add=(h,col,act)=>M.push({id:'tv_'+h.id,dist:'',kind:'sk',sk:'tvh',hid:h.id,med:1,x:h.x,y:h.y+2,n:h.n,col:col,act:act});
 const seen={};
 G.med.act.forEach(j=>{const h=mHouse(j.h);if(h&&!seen[h.id]){seen[h.id]=1;add(h,j.t==='film'?'#c08aff':j.t==='legal'?'#7ad35a':'#5fd0ff',h.n+': '+(j.t==='film'?'Film bringen':'Fernsehen einrichten'));}});
 G.med.subs.forEach(s=>{if(s.ok||seen[s.h])return;const h=mHouse(s.h);if(h){seen[h.id]=1;add(h,'#ff5f5f',h.n+': Bild weg!');}});
 if(G.med.mark&&!seen[G.med.mark]){const h=mHouse(G.med.mark);if(h)add(h,'#ffd23f',h.n+': Kunde besuchen');}
}
function medMkOffer(){
 const M=G.med,H=medHouses();
 const busy=new Set(M.subs.map(s=>s.h).concat(M.act.map(j=>j.h),M.off.map(o=>o.h)));
 const lic=M.lic.f||M.lic.s||M.lic.l;
 let t=pick(['neu','neu','neu','film','film'].concat(lic?['legal','legal']:[]));
 const pool=t==='film'?H.filter(h=>!M.act.some(j=>j.h===h.id)&&!M.off.some(o=>o.h===h.id)):H.filter(h=>!busy.has(h.id));
 if(!pool.length)return null;
 const h=pick(pool),o={id:M.nid++,t:t,h:h.id,w:pick(MWISH),dl:G.day+rnd(1,2)};
 if(t==='neu'){o.fee=r5(rnd(50,100)+medFame()*.08);o.rw=r5(rnd(60,140));o.tv=chance(.25);}
 else if(t==='legal'){o.fee=r5(rnd(80,140));o.rw=r5(rnd(140,240));o.w=pick(['Live-Fußball für die Kneipe','Alle Serien für das Wartezimmer','Filme für den Seniorentreff','Live-TV für das Vereinsheim']);}
 else{const f=chance(.65)?pick(M.neu):rnd(0,FILMS.length-1);o.f=f;o.rw=r5(rnd(30,60)+(M.neu.indexOf(f)>=0?35:0));}
 return o;
}
function medFill(){const M=G.med;M.off=M.off.filter(o=>o.dl>=G.day);let n=0;while(M.off.length<4&&n++<10){const o=medMkOffer();if(o)M.off.push(o);}}
function medOfferTxt(o){const h=mHouse(o.h),n=h?h.n:'Jemand';
 if(o.t==='film')return n+' will den Film „'+FILMS[o.f].ti+'“ auf einem Stick. Lohn '+eur(o.rw)+'.';
 if(o.t==='legal')return n+' will legal: '+o.w+'. Einrichten '+eur(o.rw)+', danach '+eur(o.fee)+' pro Tag. Braucht eine Lizenz.';
 return n+' will alle Sender, vor allem '+o.w+'. Einrichten '+eur(o.rw)+', danach '+eur(o.fee)+' pro Tag'+(o.tv?'. Hat nur einen Röhrenfernseher.':'.');}
function medAccept(id){
 const M=G.med;if(M.act.length>=4)return{ok:false,msg:'Du kannst nur 4 Medien-Aufträge gleichzeitig führen.'};
 const i=M.off.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:'Angebot nicht mehr da.'};
 const o=M.off.splice(i,1)[0];M.act.push(o);medSync();
 return{ok:true,msg:'Angenommen! '+(mHouse(o.h)||{n:''}).n+' ist jetzt auf der Karte markiert.'};
}
function medAbandon(id){const M=G.med,i=M.act.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:''};M.act.splice(i,1);popAdd(-1);medSync();return{ok:true,msg:'Auftrag abgesagt. Die Kundschaft ist enttäuscht (-1 Beliebtheit).'};}
function medNeed(j,typ){
 const hw=G.med.hw,L=[];
 if(hw.rec+hw.box<1)L.push('Receiver oder TV-Box');
 if(typ==='ant'&&hw.ant<1)L.push('Antenne');
 if(typ==='kab'&&hw.kab<1)L.push('Kabelrolle');
 if(typ==='leg'){if(!(G.med.lic.f||G.med.lic.s||G.med.lic.l))L.push('eine Lizenz');if(hw.ant+hw.kab<1)L.push('Antenne oder Kabel');}
 else if(!medFreeCode())L.push('einen Code mit freiem Platz');
 return L;
}
function medHouseMenu(hid){
 const h=mHouse(hid);if(!h)return;
 const M=G.med,j=M.act.find(o=>o.h===hid),s=M.subs.find(o=>o.h===hid);
 UI.mh=hid;
 if(j&&(j.t==='neu'||j.t==='legal')){
  const na=medNeed(j,'ant'),nk=medNeed(j,'kab'),nl=medNeed(j,'leg'),night=hour()>=20||hour()<6;
  const ch=[];
  if(j.t==='neu'){ch.push(['Antenne aufs Dach: schnell, aber auffällig'+(na.length?' (fehlt: '+na.join(', ')+')':''),'yk:mi:ant',na.length>0]);ch.push(['Kabel heimlich verlegen: unsichtbar'+(night?', nachts ohne Risiko':', tagsüber etwas riskant')+(nk.length?' (fehlt: '+nk.join(', ')+')':''),'yk:mi:kab',nk.length>0]);}
  ch.push(['Legal anschließen mit Lizenz: kein Risiko, weniger Geld'+(nl.length?' (fehlt: '+nl.join(', ')+')':''),'yk:mi:leg',nl.length>0]);
  mdl(h.n,h.n+' wünscht sich '+(j.t==='legal'?j.w:'alle Sender, vor allem '+j.w)+'.'+(j.tv?' Im Wohnzimmer steht ein Röhrenfernseher von 1983. Ein neuer Fernseher bringt Bonus.':'')+' Lager: '+medHwLine()+'.',ch);return;
 }
 if(j&&j.t==='film'){
  const f=medHasFilm(j.f);
  mdl(h.n,h.n+' hat Chips und Kissen bereit und wartet auf „'+FILMS[j.f].ti+'“.'+(f?' Du hast ihn in '+f.q+'.':' Den Film hast du noch nicht: Scraper, Tauschbörse im Netzcafé oder Ferdi fragen.'),[['Film-Stick übergeben','yk:mi:film',!f],['Kurz mitgucken','yk:mi:mitguck',!f]]);return;
 }
 if(s&&!s.ok){
  const c=mCode(s.c),need=s.why==='code'&&!s.legal,fc=medFreeCode();
  mdl(h.n,h.n+' steht vor dem Fernseher und zeigt auf das Rauschen: „Bild weg! Mitten im Finale!“ '+(need?'Der alte Code ist gesperrt oder abgelaufen.':'Die Box hängt.'),[[need?'Neuen Code einspielen'+(fc?'':' (kein freier Code)'):'Box neu starten','yk:mi:fix',need&&!fc]]);return;
 }
 if(s){
  const ch=[['Hallo sagen und Kaffee trinken','yk:mi:hallo']];
  if(s.typ==='ant'&&!s.tarn&&!s.legal)ch.push(['Antenne tarnen (Tarnset)'+(M.hw.tarn?'':' (fehlt: Tarnset)'),'yk:mi:tarn',!M.hw.tarn]);
  if(s.typ==='ant'&&!s.box&&M.hw.box)ch.push(['Auf TV-Box umrüsten (+20 %)','yk:mi:box']);
  mdl(h.n,h.n+' ist Kunde seit Tag '+s.since+'. '+(s.legal?'Alles legal.':s.typ==='kab'?'Per Kabel angeschlossen, unsichtbar.':s.tarn?'Antenne getarnt als Wäscheständer.':'Antenne gut sichtbar auf dem Dach.')+' Zahlt '+eur(s.fee)+' pro Tag.',ch);return;
 }
 toast(h.n+' winkt freundlich aus dem Fenster.');
}
function medHwLine(){const hw=G.med.hw;return MHWK.filter(k=>hw[k]).map(k=>hw[k]+' '+MHW[k].n).join(', ')||'leer';}
function medWorkPath(h,typ){const x=h.x/TS,y=h.y/TS;return typ==='ant'?[[x,y],[x,y-1.6],[x+.4,y-1.6],[x,y]]:[[x-1.4,y],[x+1.4,y],[x-1.4,y+.1]];}
function medInstallStart(typ){
 const M=G.med,j=M.act.find(o=>o.h===UI.mh),h=mHouse(UI.mh);if(!j||!h)return;
 if(medNeed(j,typ).length){toast('Dir fehlt noch: '+medNeed(j,typ).join(', ')+'.');return;}
 P.x=h.x;P.y=h.y;
 kpStart({pts:medWorkPath(h,typ==='ant'?'ant':'kab'),mode:'const',v0:typ==='ant'?55:45,face:-Math.PI/2,med:1,msg:typ==='ant'?'Leiter an die Wand, rauf aufs Dach, Antenne festschrauben …':typ==='leg'?'Ganz offiziell mit Warnweste und Lizenz-Ausweis …':'Du schleichst mit der Kabelrolle an der Hauswand entlang …',end:()=>medInstallDone(j,typ)});
}
function medInstallDone(j,typ){
 const M=G.med,h=mHouse(j.h),hw=M.hw,legal=typ==='leg';
 if(medNeed(j,typ).length){toast('Hoppla, dir fehlt plötzlich was.');return;}
 const box=hw.box>0;if(box)hw.box--;else hw.rec--;
 let ct=typ;if(legal){if(hw.kab>0){hw.kab--;ct='kab';}else{hw.ant--;ct='ant';}}else if(typ==='ant')hw.ant--;else hw.kab--;
 let tvb=0;if(j.tv){if(hw.tv>0){hw.tv--;tvb=60;}}
 const code=legal?null:medFreeCode();
 const fee=Math.round(j.fee*(box?1.2:1)*(legal?.8:1)*(j.tv&&!tvb?.8:1));
 M.subs.push({h:j.h,c:legal?'legal':code.id,typ:ct,fee:fee,ok:true,box:box,tarn:false,legal:legal,since:G.day});
 M.act=M.act.filter(o=>o!==j);
 const rw=j.rw+tvb;G.cash+=rw;G.stats.earned+=rw;fameAdd(legal?4:3);xpAdd(8);popAdd(1);sfx('coin');
 let risk='';
 if(!legal){
  const night=hour()>=20||hour()<6,cop=copNear(P.x,P.y,260),sp=traffic.some(c=>c.spuer&&Math.hypot(c.x-P.x,c.y-P.y)<240);
  if(typ==='ant'){if(cop){heat(26);risk=' Aber ein Polizist hat dich auf dem Dach gesehen!';}else if(sp){heat(14);risk=' Ein Spürwagen piepst in der Nähe. Fahndung steigt.';}else heat(3);}
  else if(!night){if(cop){heat(12);risk=' Ein Polizist wundert sich über dein Kabel.';}else heat(2);}
 }
 medSync();
 toast('Fertig! '+h.n+' '+pick(INSTL)+' +'+eur(rw)+(tvb?' (mit neuem Fernseher)':'')+', ab jetzt '+eur(fee)+' pro Tag.'+risk);
}
function medFix(){
 const M=G.med,s=M.subs.find(o=>o.h===UI.mh),h=mHouse(UI.mh);if(!s||s.ok)return;
 if(s.why==='code'&&!s.legal){const c=medFreeCode();if(!c){toast('Du brauchst einen Code mit freiem Platz: Netzcafé Pixelhöhle oder am Hacker-PC selbst knacken.');return;}s.c=c.id;}
 s.ok=true;s.why='';const tip=rnd(10,25);G.cash+=tip;G.stats.earned+=tip;fameAdd(1);sfx('ok');medSync();
 toast(pick(['Bild ist wieder da! '+h.n+' jubelt, als hätte der eigene Verein gewonnen.','Läuft wieder! '+h.n+' gibt dir '+eur(tip)+' Trinkgeld und ein Stück Kuchen.','Du drückst auf den Knopf, die Box piept, das Bild ist zurück. '+h.n+' hält dich für ein Genie.'])+(tip?' +'+eur(tip):''));
}
function medBreak(s,why){if(!s.ok)return;s.ok=false;s.why=why;s.bd=G.day;}
function medDay(L){
 if(!G.med)return;const M=G.med;
 M.codes.forEach(c=>{if(c.t==='turm')return;c.d--;const b=Math.max(.02,MCT[c.t].ban-(M.skill||0)*.02);if(!c.ban&&c.d>0&&chance(b))c.ban=true;});
 const dead=M.codes.filter(c=>!mCodeOk(c));
 dead.forEach(c=>{const n=M.subs.filter(s=>s.c===c.id);n.forEach(s=>medBreak(s,'code'));if(n.length)L.push(MCT[c.t].n+' '+c.n+(c.ban?' wurde gesperrt':' ist abgelaufen')+'. Bei '+n.length+' Kunden ist das Bild weg!');});
 M.codes=M.codes.filter(c=>mCodeOk(c)||M.subs.some(s=>s.c===c.id&&s.ok));
 const gone=M.subs.filter(s=>!s.ok&&s.bd!==undefined&&G.day-s.bd>=2);
 gone.forEach(s=>{const h=mHouse(s.h);L.push((h?h.n:'Ein Kunde')+' hat gekündigt: zu lange kein Bild.');popAdd(-1);});
 M.subs=M.subs.filter(s=>gone.indexOf(s)<0);
 let inc=0,txt=[];
 if(M.kino){const v=Math.round(500*(1+.4*((M.lic.f?1:0)+(M.lic.s?1:0)+(M.lic.l?1:0)))+(M.kinoSchwarz?300:0));inc+=v;txt.push('Kino '+eur(v));if(M.kinoSchwarz){heat(5);if(chance(.15)){inc-=800;txt.push('Razzia im Kino: -800 € Strafe');}}}
 if(M.auto){const v=Math.round(350*(1+.3*((M.lic.f?1:0)+(M.lic.s?1:0))));inc+=v;txt.push('Autokino '+eur(v));}
 M.vids.forEach(v=>{const age=G.day-v.day;v.v=Math.round(age<3?v.v+v.st*v.st*60:v.v*.82);const e=Math.round(v.v*.04);inc+=e;});
 if(M.vids.length)txt.push('Videos '+eur(Math.round(M.vids.reduce((a,v)=>a+v.v*.04,0))));
 if(inc){G.cash+=inc;G.stats.earned+=Math.max(0,inc);L.push('Medien-Einnahmen: '+txt.join(', ')+'.');}
 if(M.tower===2){MHWK.forEach(k=>{if(k!=='tarn'&&k!=='tv')M.hw[k]=Math.min(30,M.hw[k]+3);});M.hw.tv=Math.min(10,M.hw.tv+1);fameAdd(5);L.push('Das Lager im Fernsehturm wurde aufgefüllt.');}
 medNeu();M.off=[];medFill();medSync();
 L.push('Neu im Kino: '+M.neu.map(i=>FILMS[i].ti).join(', ')+'.');
}
function medTick(dt){
 if(!G)return;medInit();
 const M=G.med;
 if(!traffic.some(c=>c.spuer)){traffic.filter(c=>!c.cop).slice(0,2).forEach(c=>{c.spuer=true;c.col='#6c7a89';});}
 if(!M.sync){M.sync=1;medFill();if(!ZONE)medSync();}
 if(M.hackT>0)M.hackT-=dt;
 if(M.scr>0){M.scr-=dt;if(M.scr<=0){M.scr=0;medScrDone();}}
 const hr=Math.floor((G.t||0)/(DAY_S/24));
 if(M.hr<0)M.hr=hr;
 if(hr!==M.hr){
  M.hr=hr;
  const f=Math.round(medDayFee()/24);if(f>0){G.cash+=f;G.stats.earned+=f;MPAY+=f;MPAYN++;}
  if(MPAYN>=3&&MPAY>0){toast('Abo-Kasse: +'+eur(MPAY)+' von '+medSubsOk()+' Kunden.');MPAY=0;MPAYN=0;}
  if(M.subs.length&&chance(.05)){const s=pick(M.subs.filter(x=>x.ok));if(s){medBreak(s,'box');const h=mHouse(s.h);toast('Störung: Bei '+(h?h.n:'einem Kunden')+' hängt die Box. Bild weg!');if(!ZONE)medSync();}}
  G.offT2=(G.offT2||0)+1;if(G.offT2>=1){G.offT2=0;medFill();}
 }
 if(!ZONE){
  traffic.forEach(c=>{if(!c.spuer)return;
   if(Math.hypot(c.x-P.x,c.y-P.y)<300&&chance(dt*.5))addFx(c.x,c.y-20,'Piep … piep …','#9fd8ff',.9);
   M.subs.forEach(s=>{if(s.typ!=='ant'||s.tarn||s.legal)return;const h=mHouse(s.h);if(!h||Math.hypot(h.x-c.x,h.y-c.y)>130)return;if(chance(dt*.06)){M.subs=M.subs.filter(x=>x!==s);heat(6);popAdd(-1);medSync();toast('Ein Signal-Spürwagen hat die Antenne bei '+h.n+' entdeckt und abgebaut. Kunde futsch! (Tipp: Tarnset)');}});
  });
 }
}
function medScrDone(){
 const M=G.med,n=rnd(1,2)+(M.skill>=3?1:0),got=[];
 for(let i=0;i<n;i++){const f=chance(.6)?pick(M.neu):rnd(0,FILMS.length-1);const r=Math.random();const q=M.skill>=4&&r<.4?'4K':r<.55-M.skill*.1?'CAM':'HD';if(medAddFilm(f,q))got.push('„'+FILMS[f].ti+'“ ('+q+')');}
 sfx('ding');toast(got.length?'Scraper fertig! Neu in deiner Sammlung: '+got.join(', ')+'.':'Scraper fertig, aber nur Filme gefunden, die du schon hast.');
}
function medWatch(f,q,where){
 const F=FILMS[f],Q=MQUAL[q]||MQUAL.HD;
 startFade(where==='kino'?'Licht aus, Handys aus, Popcorn auf den Schoß. Film ab: „'+F.ti+'“':where==='auto'?'Die Leinwand flackert, die Grillen zirpen. Film ab: „'+F.ti+'“':'Sofa, Decke, Knabberzeug. Film ab: „'+F.ti+'“',()=>{
  let e=EMO[F.e],m=e.m,w=e.w;
  if(F.e==='liebe'){if(chance(.5)){m=10;w='Du bist ganz verliebt in die Geschichte und grinst den ganzen Abspann lang.';}else{m=-4;w='Herzschmerz! Das Ende hat dich erwischt. Schnief.';}}
  m=Math.round(m*(m>0?Q.f:1));mood(m,(m>=0?'+':'')+m+' Film');addFx(P.x,P.y-26,m<0?'Schnief …':e.f,m<0?'#9fc8ff':'#ffd23f',1.6);
  G.med.watched=(G.med.watched||0)+1;fameAdd(.5);
  showModal({title:F.ti,text:F.g+' · '+Q.n+'. '+F.p+' '+Q.t,lines:[w,m>=0?'Laune +'+m:'Laune '+m+' (aber schön traurig)'],choices:[{label:'Weiter',a:'mclose'}]});
 });
}
const MEDS={med:1,medjobs:1,medsubs:1,medcodes:1,medfilms:1,medpc:1,hack:1,medshop:1,netz:1,kino:1};
function medBack(s){
 if(s==='hack'){medHackStop();show('medpc');return;}
 if(s==='medjobs'||s==='medsubs'||s==='medcodes'){show('med');return;}
 if(s==='medfilms'){show(UI.filmFrom||'med');return;}
 if(s==='med'||s==='medpc'){const f=UI.medFrom;UI.medFrom=null;if(f==='pause')show('pause');else if(f==='place')show('place');else if(f==='netz')show('netz');else closeAll();return;}
 closeAll();
}
function medOpen(s){if(s==='med'||s==='medpc')UI.medFrom=UI.screen==='pause'?'pause':UI.screen==='place'?'place':UI.screen==='netz'?'netz':null;show(s);}
function mHd(t,sub){return '<div class="hd"><h2>'+t+'</h2>'+(sub?'<div class="mu">'+sub+'</div>':'')+'</div>';}
const MEDSCR={
 med(){
  const M=G.med,sl=mSlots(),ri=medRankI();
  const sub='Rang: <b class="am">'+medRank()+'</b> · Ruhm '+medFame()+(ri<MRANK.length-1?' (nächster Rang ab '+MRANK[ri+1][0]+')':'')+'<br>'+medSum()+'<br>Codes: '+sl.f+' freie von '+sl.t+' Plätzen · Hacker-Wissen Stufe '+M.skill+(M.lic.f||M.lic.s||M.lic.l?' · Lizenzen: '+['f','s','l'].filter(k=>M.lic[k]).map(k=>({f:'Film',s:'Serien',l:'Live-TV'})[k]).join(', '):'')+'<br>Lager: '+medHwLine();
  let b=btn('Medien-Aufträge ('+M.act.length+' / 4 aktiv, '+M.off.length+' neu)','medGo','medjobs',{def:1})+btn('Kunden ('+M.subs.length+')','medGo','medsubs')+btn('Codes ('+M.codes.length+')','medGo','medcodes')+btn('Filme und Serien ('+M.films.length+')','medFilms','med');
  b+='<div class="b" style="opacity:.8">Hacker-PC: im Imbiss-Hinterzimmer, in deiner Wohnung oder im Netzcafé. Hardware: Elektro-Ramsch. Codes und Hacker-Kurse: Netzcafé Pixelhöhle.</div>';
  return{hint:'Pfeiltasten: wählen · OK: öffnen · Zurück: schließen',html:'<div class="place" style="max-width:48rem">'+mHd('Medien-Zentrale',sub)+b+btn('Zurück','back')+'</div>'};
 },
 medjobs(){
  const M=G.med;let b='';
  M.act.forEach(o=>{b+=btn('✓ '+medOfferTxt(o),'medAb',o.id,{note:'Aktiv. Auf der Karte markiert. OK: absagen'});});
  M.off.forEach((o,i)=>{b+=btn(medOfferTxt(o),'medAcc',o.id,{def:i===0,off:M.act.length>=4,why:'Du hast schon 4 Aufträge.'});});
  if(!b)b='<div class="b">Gerade keine Anfragen. Bald melden sich neue Leute.</div>';
  return{hint:'OK: annehmen oder absagen · Zurück',html:'<div class="place" style="max-width:52rem">'+mHd('Medien-Aufträge','Neukunden, Film-Wünsche und legale Anschlüsse. Höchstens 4 gleichzeitig.')+b+btn('Zurück','back')+'</div>'};
 },
 medsubs(){
  const M=G.med;let b='';
  M.subs.forEach((s,i)=>{const h=mHouse(s.h),c=mCode(s.c);b+=btn((s.ok?'':'⚠ ')+(h?h.n:'?')+': '+eur(s.fee)+' pro Tag','medMark',s.h,{def:i===0,note:(s.ok?'Läuft':'Bild weg! '+(s.why==='code'?'Neuer Code nötig':'Box hängt'))+' · '+(s.legal?'legal':s.typ==='kab'?'Kabel':s.tarn?'Antenne getarnt':'Antenne sichtbar')+(c?' · '+c.n:'')+' · OK: auf der Karte markieren'});});
  if(!b)b='<div class="b">Noch keine Kunden. Nimm einen Medien-Auftrag an!</div>';
  return{hint:'OK: Kunde auf der Karte markieren · Zurück',html:'<div class="place" style="max-width:48rem">'+mHd('Deine Kunden',medSum())+b+btn('Zurück','back')+'</div>'};
 },
 medcodes(){
  const M=G.med;let b='';
  M.codes.forEach(c=>{b+='<div class="b"><b>'+c.n+'</b> · '+MCT[c.t].n+' · '+mUsed(c)+' von '+c.s+' Plätzen belegt · '+(c.ban?'<span class="rd">gesperrt</span>':c.t==='turm'?'läuft für immer':'noch '+c.d+' Tag'+(c.d===1?'':'e'))+'</div>';});
  if(!M.codes.length)b='<div class="b">Keine Codes. Kauf welche im Netzcafé Pixelhöhle oder knack selbst welche am Hacker-PC.</div>';
  return{hint:'Zurück: schließen',html:'<div class="place" style="max-width:48rem">'+mHd('Codes','Alle Codes sind ausgedacht. Sie laufen ab oder werden gesperrt, dann ist bei den Kunden das Bild weg.')+b+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 medfilms(){
  const M=G.med,can=UI.filmFrom==='medpc';let b='';
  M.films.forEach((x,i)=>{const F=FILMS[x.f];b+=btn('„'+F.ti+'“ · '+x.q,'medWatchI',i,{off:!can,why:'Schauen kannst du am Hacker-PC, im Kino oder im Autokino.',def:i===0&&can,note:F.g+(M.neu.indexOf(x.f)>=0?' · NEU IM KINO':'')});});
  if(!b)b='<div class="b">Noch keine Filme. Starte den Scraper am Hacker-PC oder tausch im Netzcafé.</div>';
  return{hint:'OK: Film schauen · Zurück',html:'<div class="place" style="max-width:48rem">'+mHd('Filme und Serien','Neu im Kino: '+M.neu.map(i=>FILMS[i].ti).join(', ')+'. Alles ausgedachte Titel.')+b+btn('Zurück','back',null,{def:!can||!M.films.length})+'</div>'};
 },
 medpc(){
  const M=G.med;
  let b=btn(M.skill<1?'Code knacken (erst Hacker-Kurs im Netzcafé)':M.hackT>0?'Code knacken (Lüfter kühlt noch '+Math.ceil(M.hackT)+' s)':'Code knacken (Minispiel)','hackGo',null,{off:M.skill<1||M.hackT>0,def:M.skill>=1&&M.hackT<=0,why:M.skill<1?'Lern erst bei Pixel-Paule im Netzcafé.':'Der PC muss abkühlen.',note:'Drei Mal genau im grünen Feld drücken. Daneben: Alarm, Fahndung steigt'});
  b+=btn(M.scr>0?'Scraper läuft … noch '+Math.ceil(M.scr)+' s':'Scraper starten: sucht neue Filme und Serien','medScr',null,{off:M.scr>0,why:'Der Scraper läuft schon.',def:M.skill<1,note:'Dauert etwa anderthalb Minuten, läuft im Hintergrund'});
  b+=btn('Film schauen ('+M.films.length+')','medFilms','medpc');
  b+=btn('Medien-Zentrale','medGo','med');
  return{hint:'Pfeiltasten: wählen · OK · Zurück',html:'<div class="place" style="max-width:44rem">'+mHd('Hacker-PC','Ein brummender Rechner mit drei Bildschirmen und einem Aufkleber: „Hier wird nur Gutes gehackt.“')+b+btn('Zurück','back')+'</div>'};
 },
 hack(){
  const z=HK;if(!z)return{html:''};
  return{hint:'OK: genau im grünen Feld drücken · Zurück: abbrechen',html:'<div class="place" style="max-width:40rem">'+mHd('Code knacken','Runde '+(z.hits+1)+' von 3 · Hacker-Wissen Stufe '+G.med.skill)+'<div style="position:relative;height:2.4rem;background:#14202c;border:2px solid var(--ln);border-radius:.4rem;margin:1rem 0;overflow:hidden"><div style="position:absolute;left:'+(z.a*100)+'%;width:'+((z.b-z.a)*100)+'%;top:0;bottom:0;background:rgba(122,211,90,.55)"></div><div id="hkcur" style="position:absolute;left:'+(z.pos*100)+'%;top:0;bottom:0;width:.55rem;background:#ffd23f;box-shadow:0 0 .5rem #ffd23f"></div></div><pre style="font-size:.85rem;color:#7ad35a;min-height:4rem;white-space:pre-wrap;margin:0 0 .6rem">'+z.log+'</pre>'+btn('Jetzt!','hackHit',null,{def:1})+'</div>'};
 },
 medshop(){
  const M=G.med;let b='';
  MHWK.forEach((k,i)=>{b+=btn(MHW[k].n+': '+eur(MHW[k].p)+' (hast '+M.hw[k]+')','medBuy',k,{def:i===0,off:G.cash<MHW[k].p||M.hw[k]>=30,why:G.cash<MHW[k].p?'Nicht genug Geld.':'Mehr passt nicht ins Lager.',note:MHW[k].d});});
  return{hint:'OK: kaufen · Zurück',html:'<div class="place" style="max-width:46rem">'+mHd('Elektro-Ramsch','Rudi hinter der Theke trägt drei Brillen übereinander: „Alles original, alles mit Garantie, Garantie bis zur Tür.“ Bargeld '+eur(G.cash))+b+btn('Zurück','back')+'</div>'};
 },
 netz(){
  const M=G.med;let b='';
  ['m3u','stk','xtr'].forEach((t,i)=>{const c=MCT[t];b+=btn(c.n+': '+eur(c.p),'medCode',t,{def:i===0,off:G.cash<c.p,why:'Nicht genug Geld.',note:c.s+' Kunden, etwa '+c.d+' Tage, Sperr-Risiko '+(c.ban>=.3?'hoch':c.ban>=.15?'mittel':'gering')});});
  const L=[150,300,600,1000,1600];
  if(M.skill<5)b+=btn('Hacker-Kurs Stufe '+(M.skill+1)+': '+eur(L[M.skill]),'medKurs',null,{off:G.cash<L[M.skill],why:'Nicht genug Geld.',note:M.skill<1?'Danach kannst du am Hacker-PC selbst Codes knacken':'Weniger Sperren, bessere Codes, schärferer Scraper'});
  else b+='<div class="b">Hacker-Wissen: Meisterstufe. Pixel-Paule nennt dich jetzt „Chef“.</div>';
  b+=btn('PC mieten: 5 € (Hacker-PC)','medRent',null,{off:G.cash<5,why:'Nicht genug Geld.'});
  b+=btn('Film tauschen bei Ferdi ('+M.films.length+(M.films.length===1?' Film)':' Filme)'),'medTausch',null,{off:!M.films.length,why:'Du hast nichts zum Tauschen.',note:'Ferdi gibt dir einen anderen Film für einen von deinen'});
  return{hint:'OK: kaufen · Zurück',html:'<div class="place" style="max-width:46rem">'+mHd('Netzcafé Pixelhöhle','Pixel-Paule hat einen Bart bis zur Tastatur: „Codes, Kurse, Kaffee. Alles erfunden, nichts davon funktioniert im echten Leben. Nur der Kaffee.“ Bargeld '+eur(G.cash))+b+btn('Zurück','back')+'</div>'};
 },
 kino(){
  const M=G.med;let b='';
  M.neu.forEach((f,i)=>{b+=btn('„'+FILMS[f].ti+'“ · '+FILMS[f].g+': 8 €','kinoW',f,{def:i===0,off:G.cash<8,why:'Nicht genug Geld.',note:FILMS[f].p});});
  b+=btn('Popcorn und Brause: 5 €','kinoPop',null,{off:G.cash<5,why:'Nicht genug Geld.'});
  if(!M.kino)b+=btn('Kino kaufen: 40.000 €','kinoBuy',null,{off:G.cash<40000,why:'Nicht genug Geld.',note:'Bringt jeden Tag Geld, mit Lizenzen mehr'});
  else b+=btn(M.kinoSchwarz?'Programm: Schwarzvorführungen (umstellen auf legal)':'Programm: legal (umstellen auf Schwarzvorführungen)','kinoMode',null,{note:M.kinoSchwarz?'Mehr Geld, aber Fahndung und Razzia-Gefahr':'Sicher, mit Lizenzen mehr Geld'});
  return{hint:'OK: Film schauen · Zurück',html:'<div class="place" style="max-width:48rem">'+mHd('Kino Flimmerpalast',(M.kino?'Dein Kino! ':'')+'Rote Samtsitze, klebriger Boden, und der Vorführer schläft bei jedem Film ein. Neu im Kino:')+b+btn('Zurück','back')+'</div>'};
 }
};
function medHackStart(){
 const s=G.med.skill;HK={hits:0,pos:0,dir:1,sp:.55,a:0,b:0,log:'> Verbinde mit dem Großrechner der GlotzKonzern AG …\n> Hopfen-Firewall gefunden.'};
 medHackZone();show('hack');
 clearInterval(HKI);HKI=setInterval(()=>{if(UI.screen!=='hack'||!HK){medHackStop();return;}HK.pos+=HK.dir*HK.sp*.03;if(HK.pos>.98){HK.pos=.98;HK.dir=-1;}if(HK.pos<0){HK.pos=0;HK.dir=1;}const e=document.getElementById('hkcur');if(e)e.style.left=(HK.pos*100)+'%';},30);
}
function medHackZone(){const w=Math.max(.08,.2+G.med.skill*.03-HK.hits*.04);HK.a=rf(.08,.9-w);HK.b=HK.a+w;}
function medHackStop(){clearInterval(HKI);HKI=null;}
function medHackHit(){
 const z=HK;if(!z)return;
 if(z.pos+.012>=z.a&&z.pos<=z.b){
  z.hits++;sfx('tick');z.log+='\n> '+pick(['Käse-Verschlüsselung geknackt.','Passwort war „passwort“. Peinlich.','Wachhund-Programm mit Wurst abgelenkt.','Server in Wuppertal umgeleitet.','Firewall hat Feierabend.']);
  if(z.hits>=3){medHackStop();const c=mkCode('eig');G.med.codes.push(c);G.med.hackT=120;fameAdd(3);xpAdd(10);sfx('win');HK=null;show('medpc');showModal({title:'Geknackt!',text:'Neuer Code: '+c.n+' für '+c.s+' Kunden, etwa '+c.d+' Tage. Natürlich alles nur ausgedacht.',choices:[{label:'Weiter',a:'mclose'}]});return;}
  z.sp+=.25;medHackZone();render2();
 }else{
  medHackStop();HK=null;G.med.hackT=60;heat(12);sfx('bonk');show('medpc');toast('ALARM! Rückverfolgung läuft! Du ziehst den Stecker. Die Fahndung steigt.');
 }
}
function medTausch(){
 const M=G.med;if(!M.films.length)return;
 const i=rnd(0,M.films.length-1),give=M.films[i];
 const cand=FILMS.map((f,k)=>k).filter(k=>!medHasFilm(k));if(!cand.length){toast('Ferdi: „Du hast ja schon alles! Respekt.“');return;}
 const want=M.act.filter(j=>j.t==='film'&&!medHasFilm(j.f)).map(j=>j.f);
 const k=want.length&&chance(.7)?pick(want):pick(cand);
 M.films.splice(i,1);medAddFilm(k,give.q==='CAM'?'HD':give.q);sfx('ok');
 toast('Ferdi tauscht „'+FILMS[give.f].ti+'“ gegen „'+FILMS[k].ti+'“. Er flüstert: „Der Abspann ist das Beste.“');render2();
}
function medBuyHw(k){const c=MHW[k];if(!c||G.cash<c.p||G.med.hw[k]>=30)return;G.cash-=c.p;G.med.hw[k]++;sfx('coin');render2();}
function medBuyCode(t){const c=MCT[t];if(!c||G.cash<c.p)return;G.cash-=c.p;const x=mkCode(t);G.med.codes.push(x);sfx('coin');toast('Pixel-Paule schiebt dir einen Zettel rüber: '+x.n+'. „Und nicht weitersagen. Ist eh ausgedacht.“');render2();}
function medKurs(){
 const L=[150,300,600,1000,1600],M=G.med;if(M.skill>=5||G.cash<L[M.skill])return;
 G.cash-=L[M.skill];M.skill++;xpAdd(10);fameAdd(2);sfx('win');
 toast(pick(['Lektion '+M.skill+': „Das Passwort ist nie 1234. Außer bei Herbert.“','Lektion '+M.skill+': Pixel-Paule zeigt dir, wie man mit drei Bildschirmen gleichzeitig wichtig aussieht.','Lektion '+M.skill+': „Ein guter Hacker trinkt Kaffee. Ein sehr guter Hacker trinkt zwei.“']));render2();
}
function kinoBuy(){if(G.cash<40000||G.med.kino)return;G.cash-=40000;G.med.kino=1;fameAdd(20);sfx('win');toast('Der Flimmerpalast gehört dir! Der Vorführer wacht auf, sieht dich und schläft beruhigt wieder ein.');render2();}
function medFeld(z,H){
 for(let y=22;y<=27;y++)for(let x=33;x<=46;x++){const t=H.zg(x,y);if(t===TR)H.zs(x,y,GR);}
 const m=H.mk('autokino','sk',40,27,'Autokino Sternenhimmel','Autokino Sternenhimmel');m.sk='autokino';m.col='#c08aff';
}
function medFeldStatic(c){
 const x0=35*TS,y0=22.6*TS,w=10*TS,h=2.2*TS;
 c.fillStyle='rgba(0,0,0,.3)';c.fillRect(x0+6,y0+8,w,h);
 c.fillStyle='#4a4a52';c.fillRect(x0+w*.2,y0+h,6,40);c.fillRect(x0+w*.8,y0+h,6,40);
 c.fillStyle='#f4f4f4';c.fillRect(x0,y0,w,h);c.strokeStyle='#2a2a30';c.lineWidth=4;c.strokeRect(x0,y0,w,h);c.lineWidth=1;
 for(let i=0;i<4;i++){const cx=36*TS+i*2.6*TS,cy=26*TS;c.fillStyle=['#c0392b','#2e86c1','#f1c40f','#27ae60'][i];c.fillRect(cx,cy,40,22);c.fillStyle='#8fd0ff';c.fillRect(cx+6,cy+3,14,16);}
 c.font='bold 10px Arial';c.textAlign='center';c.fillStyle='#ffd23f';c.fillText('AUTOKINO STERNENHIMMEL',x0+w/2,y0-6);c.textAlign='start';
}
const VGEN=['Action','Komödie','Liebe','Sci-Fi','Grusel','Tierfilm'];
const VSTAR=['Herbert Klappstuhl','Oma Truus','Major Malzbier','Baron Münchhausen','Desirée Glitzer','Du selbst'];
const VSYN={'Herbert Klappstuhl':{Komödie:2,Grusel:1},'Oma Truus':{Action:2,Komödie:1},'Major Malzbier':{'Sci-Fi':2,Action:1},'Baron Münchhausen':{Action:1,'Sci-Fi':1,Komödie:1},'Desirée Glitzer':{Liebe:2,Grusel:1},'Du selbst':{}};
const VTIT={Action:['Explosion im Imbiss','Die Rasenmäher-Jagd','Turbo-Tretboot','Mission Mayo 2'],Komödie:['Chaos im Vorzelt','Der Joghurt-Dieb','Pommes für alle','Zu früh, zu spät, zu lustig'],Liebe:['Verliebt im Freibad','Zwei Herzen, ein Wohnwagen','Kuss am Pfandautomaten'],'Sci-Fi':['Aliens lieben Pils','Planet Krümel','Raumkapsel Hopfen 2'],Grusel:['Das Quietschen im Keller','Der Zwerg im Schrank','Nacht im Fernsehturm'],Tierfilm:['Die Tauben von Rheinhanfen','Ente gut, alles gut','Der Dackel mit der Föhnfrisur']};
const VKRIT=['„Ein Film. Er hat angefangen und aufgehört.“','„Solide. Die Gartenzwerge haben Talent.“','„Lustig, rührend, ein bisschen zu laut. Gefällt mir!“','„Großes Kino! Ich habe zweimal gelacht und einmal geweint.“','„Ein Meisterwerk! Die Tauben im Hintergrund verdienen einen Preis.“'];
function vdStart(){UI.vd={};mdl('Studio 1: Video drehen','Regisseurin Lola Klappe klatscht in die Hände: „Wir drehen! Erst das Genre.“',VGEN.map(g=>[g,'yk:vd:g:'+g]));}
function vdStep(a,v){
 const d=UI.vd||(UI.vd={});
 if(a==='g'){d.g=v;mdl('Studio 1: Star wählen','„'+v+'? Hervorragend! Und wer spielt die Hauptrolle?“',VSTAR.filter(s=>s!=='Desirée Glitzer'||G.med.diva).map(s=>[s,'yk:vd:s:'+s]));return;}
 if(a==='s'){d.s=v;mdl('Studio 1: Budget','„Und wie viel Geld verbrennen wir?“',[['Kleines Budget: 200 €','yk:vd:b:0',G.cash<200],['Mittleres Budget: 1.000 €','yk:vd:b:1',G.cash<1000],['Blockbuster: 5.000 €','yk:vd:b:2',G.cash<5000]]);return;}
 if(a==='b'){
  const b=+v,cost=[200,1000,5000][b];if(G.cash<cost){toast('Nicht genug Geld.');return;}
  G.cash-=cost;sfx('coin');
  const syn=((VSYN[d.s]||{})[d.g]||0)+(G.med.stunt&&d.g==='Action'?1:0);
  const st=clamp(Math.round(1+rf(0,1.8)+syn*.8+b*.7+(G.med.dreh||0)*.4),1,5);
  const ti=pick(VTIT[d.g])+(chance(.3)?' '+rnd(2,4):'');
  startFade('Klappe, die erste! '+d.s+' gibt alles. Kamera läuft … und Action!',()=>{
   G.med.vids.push({ti:ti,g:d.g,s:d.s,st:st,v:Math.round(st*st*150*(1+b)),day:G.day});
   if(G.med.vids.length>12)G.med.vids.shift();
   fameAdd(st*3);xpAdd(6);mood(st*3,'+'+st*3+' Film');sfx(st>=4?'win':'clap');
   showModal({title:'Premiere: „'+ti+'“',text:d.g+' mit '+d.s+'. '+'★'.repeat(st)+'☆'.repeat(5-st),lines:['Kritik: '+VKRIT[st-1],'Dein Video bringt jetzt jeden Tag Geld, je mehr Sterne, desto mehr Zuschauer.'],choices:[{label:'Weiter',a:'mclose'}]});
  });
 }
}
function genHolly(z,H){
 const zs=H.zs,zg=H.zg,zf=H.zf,mk=H.mk,R=H.R;
 zf(0,0,ZW,ZH,SW);zf(0,0,ZW,6,GR);
 for(let x=0;x<ZW;x++){if(x%3===0)zs(x,6,TR);if(x%4===1)zs(x,ZH-2,TR);}
 zf(2,22,44,3,GR);
 [[4,8,8,5,'#c9a24a','STUDIO 1'],[15,8,8,5,'#a8823a','STUDIO 2'],[27,8,8,5,'#5a3a7a','GLANZ & GLORIA'],[38,8,8,5,'#8a1f2a','PREMIERE']].forEach(q=>{zf(q[0],q[1],q[2],q[3],BL);z.BLD.push({x:q[0],y:q[1],w:q[2],h:q[3],c:q[4],n:q[5],k:'house',hh:8});});
 {const m=mk('studio','sk',8,13,'Studio 1','Video drehen');m.sk='studio';m.col='#ffd23f';}
 {const m=mk('casting','sk',19,13,'Studio 2: Casting','Als Statist arbeiten');m.sk='casting';m.col='#ffd23f';}
 {const m=mk('rechte','sk',31,13,'Rechteagentur Glanz & Gloria','Lizenzen kaufen');m.sk='rechte';m.col='#7ad35a';}
 {const m=mk('premiere','sk',42,13,'Premierenkino','Zum roten Teppich');m.sk='premiere';m.col='#ff5f9e';}
 mk('hotdog','buedchen',24,20,'Hotdog-Stand','Hotdog-Stand besuchen');
}
const MEDYK={lola:{n:'Regisseurin Lola Klappe'},diva:{n:'Filmdiva Desirée Glitzer'},stunt:{n:'Stuntman Stefan Sturz'}};
Object.assign(YK,MEDYK);
Object.assign(YKS,{lola:['Und … Action!','Cut! Nochmal!','Mehr Gefühl, bitte!'],diva:['Darling!','Wo ist mein Spiegel?','Nur Fotos von links!'],stunt:['Autsch! Nochmal!','Ich falle gern!','Alles gestellt!']});
function medSka(z){z.ska=[{k:'lola',x:10*TS,y:14.5*TS,hx:10*TS,hy:14.5*TS,a:0,walk:0,steer:2,say:rf(3,6),cd:0},{k:'diva',x:24*TS,y:16*TS,hx:24*TS,hy:16.5*TS,a:0,walk:0,steer:2,say:rf(3,6),cd:0},{k:'stunt',x:34*TS,y:18*TS,hx:34*TS,hy:18*TS,a:0,walk:0,steer:2,say:rf(4,8),cd:0,fall:0}];}
function medYkDraw(d){
 const k=d.k,fl=d.fall>0;
 if(k==='lola'){fig(d.x,d.y,d.a,{dress:'#1a1a1a',hair:'#c0392b',hairLen:4,hat:'#2a2a2a',brim:5,sk:5,walk:d.walk});ctx.fillStyle='#f4f4f4';ctx.fillRect(d.x+6,d.y-8,10,7);ctx.fillStyle='#111';for(let i=0;i<3;i++)ctx.fillRect(d.x+6+i*3.4,d.y-8,1.8,2.4);}
 else if(k==='diva'){fig(d.x,d.y,d.a,{dress:'#ff5f9e',hair:'#f4d03f',hairLen:7,sk:5.4,walk:d.walk});ctx.fillStyle='#111';ctx.fillRect(d.x+1,d.y-3,3,6);if(Math.sin(timeNow*3)>.8){ctx.fillStyle='#fff';ctx.font='bold 10px Arial';ctx.fillText('✦',d.x+6,d.y-8);}}
 else if(k==='stunt'){if(fl){ctx.save();ctx.translate(d.x,d.y);ctx.rotate(1.4);fig(0,0,0,{dress:'#e67e22',hair:'#3a2a1a',sk:5});ctx.restore();}else fig(d.x,d.y,d.a,{dress:'#e67e22',hair:'#3a2a1a',hat:'#f4f4f4',brim:4.2,sk:5,walk:d.walk});}
 if(Math.hypot(d.x-P.x,d.y-P.y)<110){const n=YK[k].n;ctx.font='bold 9px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,0,0,.6)';ctx.strokeText(n,d.x,d.y-24);ctx.fillStyle='#fff';ctx.fillText(n,d.x,d.y-24);ctx.lineWidth=1;ctx.textAlign='start';}
}
function medYkOpen(d){
 const k=d.k;
 if(k==='lola')mdl('Regisseurin Lola Klappe','„Ich habe schon mit Gartenzwergen, Tauben und einem Wal gedreht. Alle Profis. Der Wal hatte Lampenfieber.“',[['Regie-Kurs: 300 € (bessere Videos)','yk:ho2:regie',(G.med.dreh||0)>=3||G.cash<300],['Nach einem Tipp fragen','yk:ho2:tipp']]);
 else if(k==='diva')mdl('Filmdiva Desirée Glitzer','Sie schiebt die riesige Sonnenbrille hoch: „Darling! Ein Autogramm? Oder willst du mich für deinen Film?“',[['Autogramm holen','yk:ho2:auto'],[G.med.diva?'Sie spielt schon für dich':'Für deinen Film casten: 800 €','yk:ho2:diva',!!G.med.diva||G.cash<800]]);
 else if(k==='stunt')mdl('Stuntman Stefan Sturz','„Ich falle beruflich hin. Seit 22 Jahren. Am liebsten über Gartenstühle.“',[['Stunt-Training','yk:ho2:train'],[G.med.stunt?'Er ist schon gebucht':'Für Action-Videos buchen: 600 €','yk:ho2:stunt',!!G.med.stunt||G.cash<600]]);
}
function medStatic(c,z){
 const nm=z.name;
 if(nm==='plantage'){
  const cx=27.5*TS,cy=13.9*TS;
  c.fillStyle='rgba(0,0,0,.28)';c.beginPath();c.ellipse(cx+10,cy+10,46,18,0,0,6.283);c.fill();
  c.fillStyle='#7a8594';c.fillRect(cx-14,cy-260,28,262);c.fillStyle='#9aa6b4';c.fillRect(cx-14,cy-260,10,262);
  c.fillStyle='#c8d0d8';c.beginPath();c.ellipse(cx,cy-190,44,14,0,0,6.283);c.fill();c.fillStyle='#e5504d';c.fillRect(cx-44,cy-196,88,6);
  c.fillStyle='#d8dee6';c.beginPath();c.ellipse(cx,cy-205,30,10,0,0,6.283);c.fill();
  c.fillStyle='#5a6270';c.fillRect(cx-3,cy-330,6,70);c.fillStyle='#e5504d';c.beginPath();c.arc(cx,cy-332,5,0,6.283);c.fill();
  [[-60,-120],[60,-140],[-55,-60]].forEach(q=>{c.fillStyle='#e8edf2';c.beginPath();c.ellipse(cx+q[0],cy+q[1],16,10,-.4,0,6.283);c.fill();c.strokeStyle='#5a6270';c.beginPath();c.moveTo(cx+q[0],cy+q[1]);c.lineTo(cx+q[0]+(q[0]<0?14:-14),cy+q[1]+4);c.stroke();});
  c.fillStyle='#2a3444';c.fillRect(cx-40,cy-8,80,16);c.font='bold 9px Arial';c.textAlign='center';c.fillStyle='#ffd23f';c.fillText('GLOTZKONZERN AG',cx,cy+3);c.textAlign='start';
 }
 if(nm==='holly'){
  const L='HOLLYHANF';c.font='bold 34px Arial';c.textAlign='center';
  for(let i=0;i<L.length;i++){const x=(9+i*3.6)*TS,y=3.6*TS+Math.sin(i*.9)*10;c.fillStyle='rgba(0,0,0,.25)';c.fillText(L[i],x+4,y+4);c.fillStyle='#f4f4f4';c.fillText(L[i],x,y);c.fillStyle='#6a5a4a';c.fillRect(x-2,y+2,4,14);}
  c.textAlign='start';
  const N=['Herbert Klappstuhl','Oma Truus','Major Malzbier','Hanfred Hanfbier','Bademeister Günni','Rübezahl','Loreley','Desirée Glitzer','Wurfzelt-Wim','Udo (Gartenzwerg)'];
  for(let i=0;i<N.length;i++){const x=(3+i*4.3)*TS,y=16.5*TS;c.fillStyle='#6a1a2a';c.fillRect(x-22,y-10,44,20);c.fillStyle='#ffd23f';c.font='bold 13px Arial';c.textAlign='center';c.fillText('★',x,y+1);c.font='bold 6px Arial';c.fillStyle='#ffe8a0';c.fillText(N[i],x,y+8);c.textAlign='start';}
  c.fillStyle='#c0182a';c.fillRect(41*TS,13.5*TS,2*TS,6*TS);for(let i=0;i<6;i++){c.fillStyle='#d8b030';c.fillRect(40.6*TS,(14+i)*TS,4,8);c.fillRect(43.3*TS,(14+i)*TS,4,8);}
  c.font='bold 11px Arial';c.textAlign='center';c.fillStyle='#ffd23f';c.fillText('WALK OF FAME',24*TS,15.4*TS);c.textAlign='start';
 }
}
function medZDraw(cx,cy){
 const z=ZONE;if(!z)return;
 if(z.name==='feldweg'&&Math.hypot(40*TS-P.x,24*TS-P.y)<700){const x0=35*TS+6,y0=22.6*TS+6,w=10*TS-12,h=2.2*TS-12,t=timeNow;ctx.fillStyle='#1a2a3a';ctx.fillRect(x0,y0,w,h);for(let i=0;i<5;i++){ctx.fillStyle=['#e5504d','#ffd23f','#5fd0ff','#7ad35a','#ff9ec7'][i];const px=x0+((t*40+i*70)%w),py=y0+h/2+Math.sin(t*2+i)*h*.3;ctx.beginPath();ctx.arc(px,py,8+i,0,6.283);ctx.fill();}ctx.fillStyle='rgba(255,255,255,.08)';ctx.fillRect(x0,y0,w,h);}
 if(z.name==='holly'&&G.med&&G.med.star){const x=(3+10*4.3)*TS,y=16.5*TS;if(x>cx-40&&x<cx+VW+40){ctx.fillStyle='#8a1f2a';ctx.fillRect(x-22,y-10,44,20);ctx.fillStyle='#ffd23f';ctx.font='bold 13px Arial';ctx.textAlign='center';ctx.fillText('★',x,y+1);ctx.font='bold 6px Arial';ctx.fillText('ENTERTAIN MASTER',x,y+8);ctx.textAlign='start';}}
 if(z.name==='holly'){skl().forEach(d=>{if(d.k==='stunt'){d.fallT=(d.fallT||rf(6,10))-fdt;if(d.fall>0)d.fall-=fdt;if(d.fallT<=0){d.fallT=rf(8,14);d.fall=1.6;if(Math.hypot(d.x-P.x,d.y-P.y)<400)addFx(d.x,d.y-24,pick(['Autsch!','Plumps!','Alles gestellt!']),'#ffd23f',1.2);}}});}
}
function medDraw(cx,cy){
 if(!G||!G.med)return;
 const iv=(x,y)=>x>cx-60&&x<cx+VW+60&&y>cy-80&&y<cy+VH+60;
 G.med.subs.forEach(s=>{const h=mHouse(s.h);if(!h||!iv(h.x,h.y))return;
  const b=h.b,rx=(b.x+b.w/2)*TS,ry=b.y*TS+8;
  if(s.typ==='ant'){
   if(s.tarn){ctx.strokeStyle='#ddd';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(rx-10,ry);ctx.lineTo(rx-10,ry-16);ctx.moveTo(rx+10,ry);ctx.lineTo(rx+10,ry-16);ctx.moveTo(rx-12,ry-14);ctx.lineTo(rx+12,ry-14);ctx.stroke();ctx.lineWidth=1;['#e5504d','#2e86c1','#f1c40f'].forEach((c,i)=>{ctx.fillStyle=c;ctx.fillRect(rx-8+i*6,ry-13,4,7);});}
   else{ctx.strokeStyle='#4a4a52';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(rx,ry);ctx.lineTo(rx,ry-26);ctx.moveTo(rx-10,ry-22);ctx.lineTo(rx+10,ry-22);ctx.moveTo(rx-7,ry-16);ctx.lineTo(rx+7,ry-16);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#e8edf2';ctx.beginPath();ctx.ellipse(rx+12,ry-6,7,5,-.5,0,6.283);ctx.fill();}
  }else{ctx.strokeStyle='#222';ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(h.x-14,h.y+2);ctx.lineTo(h.x-14,(b.y+b.h)*TS-6);ctx.stroke();ctx.setLineDash([]);}
  if(!s.ok){ctx.fillStyle=Math.floor(timeNow*3)%2?'#ff5f5f':'#ffd23f';ctx.font='bold 14px Arial';ctx.textAlign='center';ctx.fillText('!',rx,ry-30);ctx.textAlign='start';}
 });
}
function medVanDraw(c){ctx.save();ctx.translate(c.x,c.y);ctx.rotate(c.a);ctx.fillStyle='#e8edf2';ctx.beginPath();ctx.ellipse(-2,0,8,6,0,0,6.283);ctx.fill();ctx.strokeStyle='#5a6270';ctx.beginPath();ctx.moveTo(-2,0);ctx.lineTo(6,-4);ctx.stroke();ctx.fillStyle=Math.floor(timeNow*4)%2?'#ff3030':'#ffd23f';ctx.beginPath();ctx.arc(8,-6,2,0,6.283);ctx.fill();ctx.restore();}
function medHud(){if(!G||!G.med)return '';const n=G.med.subs.length,b=n-medSubsOk();return '<div class="chip t"><small>KUNDEN'+(b?' · <span class="rd">'+b+' STÖRUNG</span>':'')+'</small><b>'+n+'</b><span class="sub">Tragen '+used()+' / '+cap()+'</span></div>';}
function medLoot(d){
 const M=G.med;if(!d.left){toast('Hier ist nichts mehr.');return;}
 if((M.loot||0)>=3){toast('Mehr passt nicht unauffällig in deine Jacke. Raus hier!');return;}
 d.left=0;M.loot=(M.loot||0)+1;M.lootHw=M.lootHw||{};M.lootC=M.lootC||[];
 const g=pick([['rec',2],['box',1],['ant',2],['kab',3],['tv',1],['box',2]]);
 M.hw[g[0]]=Math.min(30,M.hw[g[0]]+g[1]);M.lootHw[g[0]]=(M.lootHw[g[0]]||0)+g[1];
 let x='';if(chance(.35)){const c=mkCode('mst');M.codes.push(c);M.lootC.push(c.id);x=' Und ein Zettel mit einem Master-Code: '+c.n+'!';}
 heat(4);sfx('pick');addFx(d.x,d.y-16,'+'+g[1]+' '+MHW[g[0]].n,'#9ff5c0',1.4);
 toast('Du steckst '+g[1]+' '+MHW[g[0]].n+' ein.'+x+' Jetzt leise zurück zum Tunnel!');
}
function medLootTake(){const M=G.med;Object.keys(M.lootHw||{}).forEach(k=>{M.hw[k]=Math.max(0,M.hw[k]-M.lootHw[k]);});M.codes=M.codes.filter(c=>(M.lootC||[]).indexOf(c.id)<0);M.loot=0;M.lootHw={};M.lootC=[];}
function medTowerBuy(){
 const M=G.med;if(medRankI()<4||G.cash<80000||M.tower===2)return;
 G.cash-=80000;M.tower=2;G.shift=null;M.codes.push(mkCode('turm'));fameAdd(50);sfx('win');
 toast('Der Fernsehturm gehört dir! Die GlotzKonzern AG zieht beleidigt nach Wuppertal. Ab jetzt: Turm-Code für 60 Kunden, der nie gesperrt wird, und jeden Morgen frische Technik im Lager.');
}
function skAct21(p){
 if(p.indexOf('yk:')!==0)return false;
 const q=p.slice(3),pre=q.slice(0,3);
 if(['mi:','vd:','ho2','hl:'].indexOf(pre)<0)return false;
 UI.modal=null;render2();
 const M=G.med;
 if(q==='mi:pc'){UI.medFrom=null;show('medpc');return true;}
 if(q==='mi:ant'||q==='mi:kab'||q==='mi:leg'){medInstallStart(q.slice(3));return true;}
 if(q==='mi:fix'){medFix();return true;}
 if(q==='mi:film'){
  const j=M.act.find(o=>o.h===UI.mh&&o.t==='film'),h=mHouse(UI.mh);if(!j)return true;const f=medHasFilm(j.f);if(!f)return true;
  const rw=Math.round(j.rw*(f.q==='CAM'?.6:f.q==='4K'?1.3:1));G.cash+=rw;G.stats.earned+=rw;fameAdd(2);xpAdd(5);sfx('coin');M.act=M.act.filter(o=>o!==j);medSync();
  toast(h.n+' steckt den Stick ein: „'+FILMS[j.f].ti+'“ in '+f.q+'! +'+eur(rw)+(f.q==='CAM'?' (Gemecker wegen des Kopfs vor der Leinwand)':'')+'.');return true;
 }
 if(q==='mi:mitguck'){const j=M.act.find(o=>o.h===UI.mh&&o.t==='film');if(j){const f=medHasFilm(j.f);if(f)medWatch(j.f,f.q,'home');}return true;}
 if(q==='mi:hallo'){mood(4,'+4 Kaffee');toast(pick(['Ihr trinkt Kaffee und schaut zehn Minuten Wetterkanal. Herrlich langweilig.','Die Kundschaft zeigt dir stolz die neue Senderliste. Sender 412 zeigt nur ein Aquarium. Alle lieben es.','Du bekommst Kekse und musst dir drei Folgen „WG Chaos“ erklären lassen.']));return true;}
 if(q==='mi:tarn'){const s=M.subs.find(o=>o.h===UI.mh);if(!s||!M.hw.tarn)return true;M.hw.tarn--;s.tarn=true;sfx('ok');toast('Die Antenne ist jetzt ein Wäscheständer mit drei Socken. Kein Spürwagen der Welt kommt darauf.');return true;}
 if(q==='mi:box'){const s=M.subs.find(o=>o.h===UI.mh);if(!s||!M.hw.box)return true;M.hw.box--;M.hw.rec++;s.box=true;s.fee=Math.round(s.fee*1.2);sfx('ok');toast('TV-Box eingebaut! Jetzt auch mit Mediathek, Wetter-App und einem Spiel, in dem man Tauben füttert. Gebühr +20 %.');return true;}
 if(pre==='vd:'){const a=q.split(':');vdStep(a[1],a.slice(2).join(':'));return true;}
 if(q==='ho2:regie'){if(G.cash<300||(M.dreh||0)>=3)return true;G.cash-=300;M.dreh=(M.dreh||0)+1;sfx('win');toast('Lola bringt dir bei: „Wenn keiner weiß, was passiert, nenn es Kunst.“ Regie-Stufe '+M.dreh+'.');return true;}
 if(q==='ho2:tipp'){toast(pick(['„Herbert ist in Komödien unschlagbar. Er weiß es nur nicht.“','„Oma Truus macht ihre Stunts selbst. Mit 84!“','„Major Malzbier in einem Weltraumfilm? Garantierter Erfolg.“','„Mehr Budget heißt mehr Sterne. Meistens.“']));return true;}
 if(q==='ho2:auto'){mood(6,'+6 Autogramm');toast('Desirée schreibt „Für meinen größten Fan, Darling“ auf deinen Arm. Mit Glitzerstift. Geht nie wieder ab.');return true;}
 if(q==='ho2:diva'){if(G.cash<800||M.diva)return true;G.cash-=800;M.diva=1;sfx('win');toast('Desirée spielt ab jetzt in deinen Videos mit. Besonders stark in Liebesfilmen und Grusel.');return true;}
 if(q==='ho2:train'){mood(5,'+5');toast('Stefan zeigt dir, wie man elegant über einen Gartenstuhl fällt. Du fällst nicht elegant, aber laut.');return true;}
 if(q==='ho2:stunt'){if(G.cash<600||M.stunt)return true;G.cash-=600;M.stunt=1;sfx('win');toast('Stefan Sturz ist gebucht: Deine Action-Videos bekommen mehr Sterne.');return true;}
 if(q==='hl:cast'){startFade('Du spielst „Passant Nr. 4“ und läufst dreimal durchs Bild. Beim vierten Mal winkst du in die Kamera.',()=>{G.cash+=80;G.stats.earned+=80;fameAdd(1);mood(4,'+4');toast('Statisten-Gage: 80 €. Lola sagt: „Das Winken schneiden wir raus. Oder auch nicht.“');});return true;}
 if(q==='hl:lic:f'||q==='hl:lic:s'||q==='hl:lic:l'){const k=q.slice(7),P2={f:6000,s:4000,l:9000};if(M.lic[k]||G.cash<P2[k])return true;G.cash-=P2[k];M.lic[k]=1;fameAdd(10);sfx('win');toast('Lizenz gekauft! Ab jetzt kannst du Kunden legal anschließen, und Kino und Autokino bringen mehr Geld. Herr Glanz stempelt dreimal, Frau Gloria applaudiert.');return true;}
 if(q==='hl:prem'){if(!M.vids.length)return true;const v=M.vids[M.vids.length-1];mood(10,'+10 Premiere');fameAdd(3);sfx('clap');toast('Roter Teppich für „'+v.ti+'“! Blitzlichter, Jubel, und '+v.s+' gibt Autogramme. Ein Kritiker flüstert: „'+'★'.repeat(v.st)+'“.');return true;}
 if(q==='hl:autoW'){if(G.cash<6)return true;G.cash-=6;const f=pick(M.neu);medWatch(f,'HD','auto');return true;}
 if(q==='hl:autoB'){if(G.cash<25000||M.auto)return true;G.cash-=25000;M.auto=1;fameAdd(15);sfx('win');toast('Das Autokino gehört dir! Auf der Leinwand steht jetzt dein Name. Ganz klein, unten rechts.');return true;}
 return true;
}
Object.assign(KSKM,{
 tvh:mk=>medHouseMenu(mk.hid),
 netz:()=>{UI.medFrom=null;show('netz');},
 elektro:()=>show('medshop'),
 kino:()=>show('kino'),
 autokino:()=>mdl('Autokino Sternenhimmel','Grillen zirpen, die Leinwand flackert, und wer kein Auto hat, bekommt einen Klappstuhl. Heute: „'+FILMS[G.med.neu[0]].ti+'“.'+(G.med.auto?' Das Autokino gehört dir.':''),[['Film schauen: 6 €','yk:hl:autoW',G.cash<6],[G.med.auto?'Gehört dir schon':'Autokino kaufen: 25.000 €','yk:hl:autoB',!!G.med.auto||G.cash<25000]]),
 studio:()=>vdStart(),
 casting:()=>mdl('Studio 2: Casting','Eine Schlange aus Statisten wartet. Alle tragen Hüte, keiner weiß warum.',[['Als Statist arbeiten: 80 €','yk:hl:cast']]),
 rechte:()=>{const L=G.med.lic;mdl('Rechteagentur Glanz & Gloria','Herr Glanz und Frau Gloria sitzen hinter einem goldenen Schreibtisch: „Lizenzen, Darling! Damit ist alles legal und du schläfst nachts ruhig.“',[[L.f?'Filmlizenz: gekauft':'Filmlizenz: 6.000 €','yk:hl:lic:f',!!L.f||G.cash<6000],[L.s?'Serienlizenz: gekauft':'Serienlizenz: 4.000 €','yk:hl:lic:s',!!L.s||G.cash<4000],[L.l?'Live-TV und Sport: gekauft':'Live-TV und Sport: 9.000 €','yk:hl:lic:l',!!L.l||G.cash<9000]]);},
 premiere:()=>mdl('Premierenkino','Roter Teppich, Absperrkordeln, Fotografen.'+(G.med.vids.length?' Dein neuester Film: „'+G.med.vids[G.med.vids.length-1].ti+'“.':' Du hast noch keinen eigenen Film. Ab ins Studio 1!'),[['Premiere feiern','yk:hl:prem',!G.med.vids.length]])
});
function medRegister(){
Object.assign(SCREENS,MEDSCR);
Object.assign(ACT,{
 medS(){medOpen('med');},medPC(){medOpen('medpc');},medGo(s){show(s);},
 medFilms(from){UI.filmFrom=from;show('medfilms');},
 medAcc(id){res(medAccept(+id));},medAb(id){res(medAbandon(+id));},
 medMark(h){G.med.mark=h;medSync();const x=mHouse(h);toast((x?x.n:'Kunde')+' ist auf der Karte gelb markiert.');},
 medWatchI(i){const x=G.med.films[+i];if(!x)return;UI.screen=null;render2();medWatch(x.f,x.q,'home');},
 medScr(){if(G.med.scr>0)return;G.med.scr=90;sfx('ok');toast('Der Scraper rattert los. Er durchsucht das ausgedachte Internet nach Filmen und Serien.');render2();},
 hackGo(){if(G.med.skill<1||G.med.hackT>0)return;medHackStart();},hackHit(){medHackHit();},
 medBuy(k){medBuyHw(k);},medCode(t){medBuyCode(t);},medKurs(){medKurs();},
 medRent(){if(G.cash<5)return;G.cash-=5;sfx('coin');UI.medFrom='netz';show('medpc');},
 medTausch(){medTausch();},
 kinoW(f){if(G.cash<8)return;G.cash-=8;sfx('coin');UI.screen=null;render2();medWatch(+f,'4K','kino');},
 kinoPop(){if(G.cash<5)return;G.cash-=5;needAdd(25,25);mood(3,'+3 Popcorn');sfx('coin');toast('Popcorn und Brause! Die Hälfte landet auf dem Boden, wie es sich gehört.');},
 kinoBuy(){kinoBuy();},kinoMode(){G.med.kinoSchwarz=!G.med.kinoSchwarz;render2();}
});
window.HHM={medInit:medInit,medHouses:medHouses,medSync:medSync,medFill:medFill,medAccept:medAccept,medHouseMenu:medHouseMenu,medInstallStart:medInstallStart,medFix:medFix,medDay:medDay,medTick:medTick,mkCode:mkCode,medFreeCode:medFreeCode,medRank:medRank,medRankI:medRankI,fameAdd:fameAdd,FILMS:FILMS,medWatch:medWatch,medHackStart:medHackStart,medHackHit:medHackHit,HK:()=>HK,medTausch:medTausch,vdStart:vdStart,medScrDone:medScrDone,medLoot:medLoot,medTowerBuy:medTowerBuy,medBreak:medBreak,BLD:()=>CITY.BLD,skAct21:skAct21};
}


const CPAD={t:0,b:0,l:0,r:0,s:1,cv:null,mm:null,n:0,ft:0,h:false};
let MMPREF='normal';try{MMPREF=localStorage.getItem('hh_mm')||'normal';}catch(e){}
if(['normal','klein','aus'].indexOf(MMPREF)<0)MMPREF='normal';
function mmApply(){mm.classList.toggle('mmk',MMPREF==='klein');mm.classList.toggle('mmoff',MMPREF==='aus');if(MMPREF==='aus')mm.style.display='none';else if(G&&!UI.title)mm.style.display='block';CPAD.n=0;}
function camPad(){
 try{
  const cr=cv.getBoundingClientRect();if(!cr.width)return;const s=VW/cr.width;CPAD.s=s;CPAD.cv=cr;
  const hd=document.getElementById('hud'),hr=hd?hd.getBoundingClientRect():null;
  CPAD.t=hr&&hr.height>0&&hr.bottom>cr.top?Math.min(VH*.3,(hr.bottom-cr.top)*s+4):0;
  const mr=MMPREF!=='aus'?mm.getBoundingClientRect():null;
  CPAD.mm=mr&&mr.width>0?mr:null;
  CPAD.b=CPAD.mm&&cr.bottom>mr.top?Math.min(VH*.35,(cr.bottom-mr.top)*s+4):0;
  let r=0;
  if(document.body.classList.contains('touch')){const b=document.getElementById('tBk'),br=b?b.getBoundingClientRect():null;if(br&&br.width>0)r=Math.min(VW*.2,(cr.right-br.left)*s+4);}
  CPAD.r=r;
 }catch(e){}
}
function camX(v){return clamp(v,-CPAD.l,MW*TS-VW+CPAD.r);}
function camY(v){return clamp(v,-CPAD.t,MH*TS-VH+CPAD.b);}
function drawWC(cx,cy){
 const W=WC.width,H2=WC.height;
 if(cx>=0&&cy>=0&&cx+VW<=W&&cy+VH<=H2){ctx.drawImage(WC,cx,cy,VW,VH,0,0,VW,VH);return;}
 ctx.fillStyle='#0b0f0c';ctx.fillRect(0,0,VW,VH);
 const sx=Math.max(0,cx),sy=Math.max(0,cy),sw=Math.min(W,cx+VW)-sx,sh=Math.min(H2,cy+VH)-sy;
 if(sw>0&&sh>0){ctx.drawImage(WC,sx,sy,sw,sh,sx-cx,sy-cy,sw,sh);ctx.strokeStyle='rgba(242,180,65,.35)';ctx.lineWidth=2;ctx.strokeRect(sx-cx-1,sy-cy-1,sw+2,sh+2);}
}
function mmFade(cx,cy){
 if((CPAD.n++)%60===0)camPad();
 CPAD.ft-=fdt;if(CPAD.ft>0)return;CPAD.ft=.15;
 const mr=CPAD.mm,cr=CPAD.cv;if(!mr||!cr)return;
 const k=1/CPAD.s,inR=(x,y,m)=>{const X=cr.left+(x-cx)*k,Y=cr.top+(y-cy)*k;return X>mr.left-m&&X<mr.right+m&&Y>mr.top-m&&Y<mr.bottom+m;};
 let h=false;
 if(G&&!UI.title){h=inR(P.x,P.y,48)||MKS.some(m=>inR(m.x,m.y,14))||!!(G.schatz&&!ZONE&&inR(G.schatz.x,G.schatz.y,14));}
 if(h!==CPAD.h){CPAD.h=h;mm.classList.toggle('fade',h);}
}

const H={
 G:()=>G,champOk,champHint,startsN,bumpStarts,newGame,saveAll,hasSave,loadAll,GOODS,TRADE,DIST,MARKETS,UPS,BRAU_CAP,HAUS_CAP,SHOP,eur,price,sellP,pedPrice,cap,used,worth,rank,clock,hour,buyAt,needAt,buyNeeded,gq,
 mTitle,mLine,canPickup,canDeliver,whyNot,accept,abandon,pickup,deliver,buy,sell,startBrew,startGrow,collect,buyUp,payDebt,loan,
 callVan,sleepHome,startWanted,wanted:()=>wanted,
 setCb:(m,b)=>{msgCb=m;busted=b;}
};

const $=s=>document.querySelector(s);
const UI={screen:null,modal:null,fk:null,fkm:{},mk:null,toastT:null,title:true,hudS:'',trkS:'',pS:''};
function btn(label,a,p,o){
 o=o||{};
 return '<div class="f btn'+(o.cls?' '+o.cls:'')+(o.off?' off':'')+'" data-a="'+a+'" data-p="'+(p===undefined||p===null?'':p)+'"'+(o.why?' data-why="'+o.why+'"':'')+(o.def?' data-def="1"':'')+'>'+label+(o.note?'<small>'+o.note+'</small>':'')+'</div>';
}
function toast(t){
 const e=$('#toast');e.textContent=t;e.style.display='block';
 clearTimeout(UI.toastT);UI.toastT=setTimeout(()=>{e.style.display='none';},3200);
}
function res(r){if(r&&r.msg)toast(r.msg);render2();}

function moodCol(){const m=G.mood;return m>=65?'var(--gr)':m>=45?'var(--tx)':m>=25?'var(--am)':'var(--rd)';}
function hudHtml(){
 const g=G;let st='';
 for(let i=0;i<3;i++)st+=i<wanted?'★':'☆';
 const night=hour()>=20||hour()<6;
 const m=(lab,v,col,word,warn)=>'<div class="wm"><small'+(warn?' class="rd blink"':'')+'>'+lab+'</small><div class="hb"><i style="width:'+Math.round(clamp(v,0,100))+'%;background:'+col+'"></i></div><em style="color:'+col+'">'+word+'</em></div>';
 const hun=g.hun===undefined?80:g.hun,dur=g.dur===undefined?80:g.dur,dr=clamp((g.drunk||0)/6*100,0,100),hi=clamp((g.high||0)/150*100,0,100);
 return '<div class="chip"><small>TAG '+g.day+(night&&!ZONE?' · NACHT':'')+(wxLabel()?' · '+wxLabel():'')+'</small><b class="am">'+H.clock()+'</b></div>'+
  '<div class="chip"><small>BARGELD</small><b class="gr">'+eur(g.cash)+'</b><span class="sub">'+(g.debt>0?'Vorschuss <span class="rd">'+eur(g.debt)+'</span>':'schuldenfrei')+'</span></div>'+
  '<div class="chip h"><small>'+(wanted?'POLIZEI':'RANG · '+medFame()+' RUHM')+'</small><b class="'+(wanted?'rd':'am')+'">'+(wanted?st:((g.heroE||0)>=100?'SUPER-KONFETTI!':medRank()))+'</b><div class="hb" style="height:.32rem;margin-top:.1rem"><i style="width:'+Math.round(g.heroE||0)+'%;background:#ffd23f"></i></div></div>'+
  '<div class="chip wb">'+
   m('LAUNE',g.mood,moodCol(),moodWord(),g.mood<25)+
   m(hun<25?'HUNGER!':'ESSEN',hun,needCol(hun),hun>=70?'satt':hun>=40?'geht so':hun>=20?'hungrig':'Bärenhunger',hun<25)+
   m(dur<25?'DURST!':'TRINKEN',dur,needCol(dur),dur>=70?'erfrischt':dur>=40?'geht so':dur>=20?'durstig':'ausgedörrt',dur<25)+
   m('PROMILLE',dr,'#f2b441',(g.drunk||0)<.3?'nüchtern':g.drunk<2?'beschwipst':g.drunk<4?'angeheitert':'betrunken',(g.drunk||0)>=5)+
   m('BEKIFFT',hi,'#7ad35a',hi<=0?'klar':hi<35?'leicht':hi<70?'bekifft':'total breit',false)+
  '</div>'+
  medHud();
}
function promptText(){
 if(UI.screen||UI.modal||fade||P.sit||P.build)return '';
 if(MG)return mgPrompt();
 if(P.coast)return '';
 {const fp=firePromptEarly();if(fp)return fp;}
 if(P.fight)return 'OK: DRÜCKEN! Ringen!';
 if(P.fish)return P.fish.st==='bite'?'OK: JETZT ANZIEHEN!':'Warten ... (Richtung drücken: Leine einholen)';
 if(P.ride){if(nearWhale())return 'OK: Dem Wal Hallo sagen';return Math.abs(P.ride.sp)<110?'OK: Absteigen':'';}
 const mk=nearMarker();
 const lab=m=>'OK: '+(m.act||(m.kind==='hq'?'Hanfred Hanfbier':m.kind==='willi'?'Chefin Willi':m.n));
 if(P.inCar){
  if(mk&&Math.abs(V.sp)<80)return lab(mk);
  return Math.abs(V.sp)<60?'OK: Aussteigen':'';
 }
 if(P.hide)return 'OK: Aus dem Versteck klettern';
 {const hd=nearHide();if(hd)return 'OK: Verstecken '+HTN[hd.t];}
 if(nearThug())return G.heroE>=100?'OK: SUPER-KONFETTI!':'OK: Konfetti werfen';
 if(nearWhale())return 'OK: Dem Wal Hallo sagen';
 if(nearShark())return 'OK: Hai ringen!';
 {const q0=nearSk();if(q0&&(QSK[q0.k]||YK[q0.k]))return skPrompt(q0);}
 {const rd0=nearRide();if(rd0&&(!mk||Math.hypot(rd0.x-P.x,rd0.y-P.y)<Math.hypot(mk.x-P.x,mk.y-P.y)-4))return rideLab(rd0);}
 if(mk)return lab(mk);
 {const fm=firePromptMid();if(fm)return fm;}
 if(!ZONE){const an0=nearAni();if(an0)return aniPrompt(an0);}
 if(campNear())return 'OK: Zurück auf die Decke';
 if(nearSeat())return 'OK: Hinsetzen';
 const rd=nearRide();if(rd)return rideLab(rd);
 const sk=nearSk();if(sk)return skPrompt(sk);
 const an=nearAni();if(an)return aniPrompt(an);
 const pd=nearPed();if(pd)return 'OK: '+pd.nm+' ansprechen'+(pd.like?' ♥':'');
 if(nearSnowman())return 'OK: Schneemann umkicken';
 if(nearCastle())return 'OK: Sandburg kaputt treten';
 if(nearVan())return 'OK: Einsteigen';
 if(waterAhead()&&!aimBest(130,false))return 'OK: Angeln';
 const cb=ctxBuild();if(cb&&!aimBest(130,false))return cb==='castle'?'OK: Sandburg bauen':'OK: Schneemann bauen';
 const t=curAmmo();if(t&&!(ZONE&&ZONE.name==='fpark'&&t!=='wasser'))return 'OK: '+AMN[t]+(t==='wasser'?' spritzen ('+Math.floor(G.tank)+')':' werfen ('+G.ammo[t]+')');
 return '';
}
function hudUpdate(){
 const hudEl=$('#hud'),trk=$('#trk'),pr=$('#prompt'),mmEl=$('#mm');
 if(!G||UI.title){hudEl.style.display='none';trk.style.display='none';pr.style.display='none';mmEl.style.display='none';return;}
 hudEl.style.display='flex';trk.style.display='block';mmEl.style.display=MMPREF==='aus'?'none':'block';
 const h=hudHtml();if(h!==UI.hudS){UI.hudS=h;hudEl.innerHTML=h;}
 let t='';
 G.active.forEach(m=>{
  const c=m.t==='kurier'?'k':m.t==='rezept'?'b':'';
  let s=m.t==='kurier'?(m.got?'Paket zu: '+DIST[m.to].n:'Paket holen: '+DIST[m.from].n):m.t==='rezept'?(m.got?'Rezept zu: '+DIST[m.to].n:'Rezept holen: Rhein-Apotheke'):gq(m.item,m.q)+' ('+Math.min(G.inv[m.item]||0,m.q)+' dabei) → '+DIST[m.to].n;
  t+='<div class="'+c+'"><b>'+mTitle(m)+'</b> · '+s+' · Tag '+m.dl+'</div>';
 });
 thugs.forEach(u=>{if(u.loot&&u.ko<=0)t+='<div class="r"><b>Miesepeter</b> · hat '+gq(u.loot.g,u.loot.q)+' stibitzt · rote Punkte auf der Karte</div>';});
 t+=aniTrk();t+=plantTrk();
 if(G.pistol&&curAmmo()==='wasser')t+='<div class="r"><b>Wasserpistole</b> · Tank '+Math.floor(G.tank)+' / 30</div>';
 if(RACE)t+='<div class="r"><b>Wettrennen</b> · gegen '+RACE.p.nm+' · noch '+Math.max(0,Math.ceil(RACE.max-RACE.t))+' s</div>';
 if(t!==UI.trkS){UI.trkS=t;trk.innerHTML=t;}
 let p=promptText();
 if(p!==UI.pS){UI.pS=p;pr.textContent=p;pr.style.display=p?'block':'none';}
}

const SCREENS={
 title(){
  return{hint:'Pfeiltasten: wählen · OK: bestätigen',cls:'t',html:'<div class="title"><h1>ENTERTAIN <span>·</span> MASTER</h1><p>Rheinhanfen · Codes, Kabel, Kino &amp; Quatsch</p><div class="menu">'+
   btn('Neues Spiel','new',null,{def:1})+(H.hasSave()?btn('Spiel fortsetzen','cont'):'')+btn('Anleitung','help')+btn('Beenden','quit')+'</div></div>'};
 },
 help(){
  return{hint:'Hoch und Runter: blättern · OK oder Zurück: schließen',html:'<div class="place" style="max-width:46rem;display:flex;flex-direction:column;overflow:hidden"><h2>So geht\'s</h2><div class="panel" style="flex:1 1 auto">'+
   '<p><b class="am">Worum geht\'s?</b> Du fängst in Rheinhanfen ganz klein an: Feldbett im Imbiss von Hanfred Hanfbier, alter Hacker-PC im Hinterzimmer. Die Leute wollen alle Sender, die neuesten Filme und Serien. Besorg Codes, schraub Antennen aufs Dach, verleg heimlich Kabel und lass dich nicht von den Spürwagen erwischen.</p>'+
   '<p><b class="am">Dein Ziel:</b> Werde der Entertain Master! Mehr Kunden bringen Geld und Ruhm. Kauf Kino und Autokino, dreh in Hollyhanf eigene Videos, hol dir Lizenzen und übernimm am Ende den Fernsehturm. Verlieren kannst du nicht, höchstens pleite und unbeliebt sein.</p>'+
   '<p><b class="am">Und zwischendurch:</b> Lieferdienst und Apotheke bleiben kleine Nebenjobs, Bier und Gras sind nur noch zum Genießen. Eigene Wohnung, Camping in Holland, Freibad, Rodelbahn, Skifahren: Überall passiert etwas Lustiges.</p>'+
   '<p><b class="am">Steuerung:</b> Pfeiltasten laufen und lenken. OK macht das, was unten am Bildrand steht. Zurück öffnet das Menü mit Medien-Zentrale, Rucksack, Karte und Europa-Karte.</p>'+
   '<p><b class="am">Gut zu wissen:</b> Essen und Trinken nicht vergessen, die Leiste oben zeigt, wie es dir geht. Alkohol und Gras nur für Erwachsene und nie in der Nähe von Kindern. Sucht dich die Polizei, versteck dich. Niemand stirbt, alles ist Fiktion: Codes, Sender und Filme sind ausgedacht.</p>'+
   '</div><div style="margin-top:.5rem">'+btn('Alles klar!','back',null,{def:1})+'</div></div>'};
 },

 pause(){
  const g=G,w=H.worth();
  let ns='';g.events.forEach(e=>{ns+='<div class="news">'+e.t+'</div>';});
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: weiterspielen',html:'<div class="pmenu"><div class="hd"><h2>Menü</h2><div class="mu">Laune: '+moodWord()+' · Vermögen '+eur(w)+' · Respekt '+g.resp+' · Rang: '+H.rank(w)+'</div><div class="mu">Held: '+heroRank()+' ('+Math.floor(g.hero||0)+' Punkte) · Fänge '+(g.fang||0)+' · Haizähne '+(g.zahn||0)+' · Mitmachen '+(g.mm||0)+'</div><div class="mu">Stufe '+(g.lvl||1)+' ('+Math.floor(g.xp||0)+' / '+lvlNeed(g.lvl||1)+' EP) · Beliebtheit: '+popWord()+' · Stadt sauber: '+Math.round(g.clean===undefined?40:g.clean)+' % · Besitz: '+ownCount()+' Landschaften · Zuhause: '+homeShort()+'</div>'+ns+'</div>'+
   btn('Weiterspielen','back',null,{def:1})+btn('Medien-Zentrale: '+medSum(),'medS')+btn('Handy: Nebenjobs ('+g.active.length+'/4)','missions')+btn('Rucksack','inv')+btn('Feststecken? Befreien','freeMe')+btn('Pflanzen-Cam ('+((g.plants||[]).length)+' / 3)','growS')+btn('Karte','map')+btn('Europa-Karte','euro')+btn('Van rufen (25 €)','vanCall')+btn('Ton: '+(SND.on?'an':'aus'),'snd')+btn('Minikarte: '+MMPREF,'mmpref')+btn('Touch-Tasten: '+({auto:'automatisch',off:'aus',on:'an'}[TPREF]),'tpref')+btn('Anleitung','help')+btn('Speichern und zum Titel','saveExit')+btn('Beenden','quit')+'</div>'};
 },
 euro(){
  const cur=ZONE?ZONE.name:'city',dk=cur==='bayern'?'city':'bayern';
  let h='<div class="hd"><h2>Europa-Karte</h2><div class="mu">Jedes Land hat sein eigenes Bier, seine eigenen Spezialitäten und seine eigenen Sketche. Wohin soll die Reise gehen?</div></div>';
  h+='<div style="position:relative;width:min(100%,calc(50vh*1.6));aspect-ratio:1.6/1;margin:.3rem auto;border:2px solid var(--ln);border-radius:.5rem;overflow:hidden">'+EUSVG;
  Object.keys(EURO).forEach(k=>{
   const e=EURO[k];
   h+='<div class="f btn'+(e.off?' off':'')+'" data-a="trav" data-p="'+k+'"'+(e.off?' data-why="'+e.why+'"':'')+(k===dk?' data-def="1"':'')+' style="position:absolute;left:'+(e.x/1.6)+'%;top:'+e.y+'%;transform:translate(-50%,-50%);margin:0;padding:.3rem .7rem;font-size:.9rem;white-space:nowrap">'+(k===cur?'● ':'')+e.n+(e.off?' (bald)':'')+'</div>';
  });
  h+='</div><div style="max-width:14rem">'+btn('Zurück','back')+'</div>';
  return{hint:'Pfeiltasten: Reiseziel wählen · OK: losreisen · Zurück: schließen',html:h};
 },
 map(){
  return{hint:'Zurück: schließen',html:'<div class="hd"><h2>Karte von Rheinhanfen</h2><div class="mu">Gelb: Läden · Grün: Imbiss · Türkis: Büdchen · Lila: Portale · Weiße Ringe: Auftragsziele · Braun: ausgebüxte Tiere</div></div><canvas id="bigmap" width="304" height="192" style="width:100%;max-height:78%;border:2px solid var(--ln);border-radius:.4rem;image-rendering:pixelated"></canvas><div style="max-width:14rem">'+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 place(){
  const g=G,mk=UI.mk,d=DIST[mk.dist]||{n:mk.n,sub:'',d:''};let b='',df=0;
  g.active.forEach(m=>{if(m.to===g.loc&&H.canDeliver(m)){b+=btn('Abgeben: '+H.mTitle(m),'deliver',m.id,{cls:'d',def:df?0:1,note:H.mLine(m)+' Belohnung '+eur(m.rw)});df=1;}});
  g.active.forEach(m=>{if(H.canPickup(m)){b+=btn((m.t==='rezept'?'Rezept abholen: ':'Paket abholen: ')+H.mTitle(m),'pickup',m.id,{cls:'m',def:df?0:1,note:'Liefern an: '+DIST[m.to].n});df=1;}});
  b+=placeShop(mk);
  if(d.food)b+=btn(d.food==='mega'?'Probierstand und Angebote':'Selbst essen (Laune)','eat');
  g.active.forEach(m=>{if(m.to===g.loc&&!H.canDeliver(m))b+=btn('Abgeben: '+H.mTitle(m),'deliver',m.id,{cls:'d',off:1,why:H.whyNot(m),note:H.mLine(m)});});
  if(mk.kind==='hq'){b+=btn('Ausbauten','ups');b+=btn('Schlafen bis zum Morgen','sleep');}
  b+=btn('Zurück zur Straße','back');
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: schließen',html:'<div class="place"><div class="hd"><h2>'+d.n+'</h2><div class="mu">'+d.sub+' · Bargeld <b class="gr">'+eur(G.cash)+'</b> · Tragen <b class="am">'+used()+' / '+cap()+'</b></div><p>'+d.d+'</p></div>'+b+'</div>'};
 },
 market(){return tradeMarket();},
 missions(){
  const g=G;
  const tag=o=>'<span class="tg '+(o.t==='lieferung'?'l':o.t==='rezept'?'b':'k')+'">'+({lieferung:'BESTELLUNG',rezept:'APOTHEKE',kurier:'KURIER'}[o.t]||o.t.toUpperCase())+'</span>';
  let l='',r='';
  g.offers.forEach(o=>{l+='<div class="f card" data-a="accept" data-p="'+o.id+'">'+tag(o)+'<b>'+H.mTitle(o)+'</b><div>'+H.mLine(o)+'</div><div class="rw">Belohnung '+eur(o.rw)+' · bis Tag '+o.dl+'</div></div>';});
  g.active.forEach(m=>{
   const st=pk(m)?(m.got?'Päckchen dabei':'Noch abzuholen: '+DIST[m.from].n):'Dabei: '+Math.min(g.inv[m.item]||0,m.q)+' / '+m.q;
   r+='<div class="f card" data-a="abandonAsk" data-p="'+m.id+'">'+tag(m)+'<b>'+H.mTitle(m)+'</b><div>'+H.mLine(m)+'</div><div class="rw">'+eur(m.rw)+' · bis Tag '+m.dl+' · '+st+'</div></div>';
  });
  if(!l)l='<div class="mu">Heute keine neuen Angebote.</div>';
  if(!r)r='<div class="mu">Du hast keine laufenden Aufträge.</div>';
  return{hint:'Links OK: annehmen · Rechts OK: abbrechen · Zurück: schließen',html:'<div class="two" style="height:calc(100% - 3.2rem)"><div class="panel"><h3>Angebote ('+g.offers.length+')</h3><div class="sc">'+l+'</div></div><div class="panel"><h3>Laufend ('+g.active.length+'/4)</h3><div class="sc">'+r+'</div></div></div><div style="max-width:14rem">'+btn('Zurück','back',null,{def:g.offers.length+g.active.length?0:1})+'</div>'};
 },
 prod(){
  const g=G,b=g.prod.brau,h=g.prod.haus,o=g.prod.out;
  const bm=Math.min(BRAU_CAP[g.up.brau],g.inv.zutat),hm=Math.min(HAUS_CAP[g.up.haus],g.inv.zutat);
  const bs=b.n>0?'In der Pfanne: <b>'+b.n+'</b> Ansätze, fertig in '+b.left+' Tag'+(b.left>1?'en':''):'Die Küche ist leer.';
  const hs=h.n>0?'In der Eismaschine: <b>'+h.n+'</b> Ansätze, fertig in '+h.left+' Tag'+(h.left>1?'en':''):'Die Eismaschine ist leer.';
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: zum Ort',html:'<div class="hd"><h2>Imbiss: Küche</h2><div class="mu">Ein Tag dauert 2,5 Minuten. Schlafen überspringt die Nacht.</div></div><div class="prodgrid">'+
   '<div class="panel"><h3>Imbissküche (Stufe '+(g.up.brau+1)+')</h3><p>1 Zutaten = 2 Currywurst, 2 Tage. Kapazität: '+BRAU_CAP[g.up.brau]+' Ansätze.</p><p>'+bs+'</p>'+
    (b.n>0?'':btn('Kochen: 1 Ansatz','brew','1',{off:bm<1,why:'Du brauchst Zutaten dabei.'})+btn('Kochen: Maximum ('+bm+')','brew','max',{off:bm<1,why:'Du brauchst Zutaten dabei.'}))+'</div>'+
   '<div class="panel"><h3>Eismanufaktur (Stufe '+(g.up.haus+1)+')</h3><p>1 Zutaten = 3 Eis, 3 Tage. Kapazität: '+HAUS_CAP[g.up.haus]+' Ansätze.</p><p>'+hs+'</p>'+
    (h.n>0?'':btn('Eis machen: 1 Ansatz','grow','1',{off:hm<1,why:'Du brauchst Zutaten dabei.'})+btn('Eis machen: Maximum ('+hm+')','grow','max',{off:hm<1,why:'Du brauchst Zutaten dabei.'}))+'</div></div>'+
   '<div class="panel" style="margin-top:.6rem"><h3>Lager</h3><p>Abholbereit: <b>'+o.curry+'</b> Currywurst, <b>'+o.eis+'</b> Eis.</p>'+btn('Alles einpacken','collect',null,{off:o.curry+o.eis<1,why:'Nichts abzuholen.',def:o.curry+o.eis>0?1:0})+'</div>'+
   '<div style="max-width:14rem">'+btn('Zurück','back',null,{def:o.curry+o.eis>0?0:1})+'</div>'};
 },
 ups(){
  let c='';
  Object.keys(UPS).forEach(k=>{
   const u=UPS[k],l=G.up[k],mx=l>=u.cost.length;
   c+='<div class="f card" data-a="up" data-p="'+k+'"><b>'+u.n+'</b> · Stufe '+l+' / '+u.cost.length+'<div>'+(mx?'<span class="gr">Höchststufe erreicht</span>':u.eff(l+1)+' <span class="am">für '+eur(u.cost[l])+'</span>')+'</div></div>';
  });
  return{hint:'Pfeiltasten: wählen · OK: kaufen · Zurück: zum Ort',html:'<div class="hd"><h2>Imbiss: Ausbauten</h2></div><div class="place" style="max-width:44rem;margin:0;height:calc(100% - 3rem)">'+c+btn('Zurück','back')+'</div>'};
 },
 willi(){
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: schließen',html:'<div class="place"><div class="hd"><h2>Chefin Willi</h2><p>"Ein Vorschuss ist wie Ketchup: Nur die richtige Menge hilft." Die Chefin verlangt 2% Zinsen pro Tag.</p><p>Vorschuss: <b class="rd">'+eur(G.debt)+'</b> · Bargeld: <b class="gr">'+eur(G.cash)+'</b></p></div>'+
   btn('100 € zurückzahlen','pay','100')+btn('500 € zurückzahlen','pay','500')+btn('Alles zurückzahlen, was geht','pay','all')+btn('Vorschuss: 500 €','loan','500',{note:'Limit 8.000 € insgesamt'})+btn('Makler: Landschaften kaufen','makler',null,{note:'Eigene Landschaften bringen jeden Tag Geld. Neue gibt es mit jeder Stufe'})+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 campshop(){return campShopScreen();},
 sit(){
  if(P.sit&&P.sit.t==='decke')return campScreen();
  const nz=inNoGo(P.x,P.y),why=nz?'Hier ist '+nz.n+': Kein Alkohol, kein Rauch!':noUse();
  const st=G.stock,bd=!!why||st.bier<1,jd=!!why||st.joint<1;
  let b=btn('Bier trinken ('+st.bier+')','drink',null,{off:bd,why:why||'Kein Bier mehr. Das Büdchen hat Nachschub.',def:bd?0:1});
  b+=btn('Joint rauchen ('+st.joint+')','smoke',null,{off:jd,why:why||'Kein Joint mehr. Das Büdchen hat Nachschub.',def:(bd&&!jd)?1:0});
  if(st.gluehwein>0||wxType()==='snow'||(ZONE&&ZONE.name==='berge'))b+=btn('Glühwein trinken ('+(st.gluehwein||0)+')','glue',null,{off:!!why||!(st.gluehwein>0),why:why||'Kein Glühwein mehr. Die Glühwein-Hütte hat Nachschub.'});
  if(ZONE&&ZONE.name==='wal')b+=btn('Tee trinken (gratis)','tea');
  b+=btn('Einfach die Aussicht genießen','chill',null,{def:(bd&&jd&&!(st.gluehwein>0))?1:0});
  b+=btn('Aufstehen','stand');
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+(P.sit&&P.sit.t===LC?(ZONE&&ZONE.name==='wal'?'Wal-Sofa':'Liegestuhl'):'Parkbank')+'</h2><div class="mu">Laune: <b>'+moodWord()+'</b>'+(G.high>0?' · bekifft':'')+(G.drunk>=2?' · angeheitert':'')+'</div>'+(why?'<div class="mu rd">'+why+'</div>':'')+'</div>'+b+'</div>'};
 },
 ped(){
  const p=UI.ped,ng=inNoGo(P.x,P.y),m=G.mood;
  let b=btn('Abklatschen','pHi',null,{def:1});
  if(canSellPed())b+=btn('Etwas anbieten …','pOffer',null,{note:p.kid?'Kinder bekommen nichts.':'Hat Lust auf: '+GOODS[pedWish(p)].n});
  b+=btn('Umarmen','pHug',null,{off:m<35,why:'Du bist zu mies drauf für Umarmungen.'});
  b+=btn('Zusammen tanzen','pDance');
  b+=btn('Wettrennen!','pRace',null,{off:wanted>0||!!RACE,why:'Gerade nicht möglich.'});
  if(p.act&&PACT[p.act])b+=btn(PACT[p.act].c,'pAct');
  b+=btn('Zunge rausstrecken','pTongue');
  b+=btn('Schubsen','pPush',null,{off:m>=70||!!ng||!!(p.kid||p.teen),why:(p.kid||p.teen)?'Doch nicht bei Kindern und Jugendlichen!':ng?'Nicht hier, hier spielen Kinder!':'Du bist viel zu gut drauf zum Schubsen.'});
  b+=btn('Schlagen (Dampf ablassen)','pHit',null,{off:m>=45||!!ng||!!(p.kid||p.teen),why:(p.kid||p.teen)?'Doch nicht bei Kindern und Jugendlichen!':ng?'Nicht hier, hier spielen Kinder!':'Dafür bist du viel zu gut drauf.'});
  b+=btn('Weitergehen','back');
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+p.nm+(p.like?' <span class="rd">♥</span>':'')+'</h2><div class="mu">'+p.jb+'</div><div class="mu">'+(p.like?'Mag dich. Strahlt dich an.':'Guckt dich neutral an.')+'</div></div>'+b+'</div>'};
 },
 buedchen(){
  const mk=UI.mk,st=G.stock;
  let b=(ZONE&&ZONE.name==='wal')?btn('Tee trinken (gratis)','tea',null,{def:1})+btn('Joint kaufen: 6 €','shopB','joint'):btn('Bier kaufen: 3 €','shopB','bier',{def:1})+btn('Joint kaufen: 6 €','shopB','joint');
  if(ZONE&&ZONE.name==='bayern')b=btn('Maß Bier: 5 € (zwei Bier)','shopB','mass',{def:1})+btn('Brezn: 2 €','shopB','brezn');
  else if(ZONE&&ZONE.name==='portugal')b=btn('Pastel de Nata: 2 €','shopB','nata',{def:1})+btn('Sardine vom Grill: 3 €','shopB','sardine')+btn('Cerveja, kaltes Lagerbier: 3 €','shopB','cerveja');
  else if(ZONE&&ZONE.name==='wuppertal')b=btn('Hausbräu vom Fass: 4 €','shopB','hausbr',{def:1})+btn('Bergische Waffel mit Kirschen: 2 €','shopB','waffel')+btn('Panhas mit Apfelmus: 2 €','shopB','panhas');
  else if(ZONE&&ZONE.name==='oesterreich')b=btn('Melange: 3 €','shopB','melange',{def:1})+btn('Kaiserschmarrn: 4 €','shopB','schmarrn')+btn('Apfelstrudel: 3 €','shopB','strudel')+btn('Bier vom Fass: 3 €','shopB','bier');
  else if(ZONE&&ZONE.name==='koeln')b=btn('Kölsch (Stange): 3 €','shopB','koelsch',{def:1})+btn('Halver Hahn: 3 €','shopB','hahn')+btn('Himmel un Ääd: 3 €','shopB','himmel');
  else if(ZONE&&ZONE.name==='feldweg')b=btn('Hopfen-Limo ohne Alkohol: 2 €','shopB','limo',{def:1})+btn('Hanfsamen-Brötchen: 2 €','shopB','hbroet')+btn('Honigbrot: 2 €','shopB','honig');
  else if(ZONE&&ZONE.name==='fpark')b=btn('Zuckerwatte: 2 €','shopB','zucker',{def:1})+btn('Popcorn: 2 €','shopB','popcorn')+btn('Lebkuchenherz: 3 €','shopB','lherz')+btn('Brause ohne Alkohol: 2 €','shopB','brause');
  else if(ZONE&&KSHOPZ[ZONE.name])b=KSHOPZ[ZONE.name]();
  if(ZONE&&ZONE.name==='amsterdam')b+=btn('Coffeeshop-Ware mitnehmen: 1 Tütchen ('+eur(price('c_holl','coffeeshop'))+')','holl','1',{note:'Coffeeshop-Qualität. In Rheinhanfen ist der Weiterverkauf illegal!'})+btn('5 Tütchen ('+eur(5*price('c_holl','coffeeshop'))+')','holl','5');
  if((wxType()==='snow'||(ZONE&&ZONE.name==='berge'))&&!(ZONE&&ZONE.name==='fpark'))b+=btn('Glühwein kaufen: 3 €','shopB','gluehwein');
  if(ZONE&&ZONE.name==='strand'&&!G.pistol)b+=btn('Wasserpistole kaufen: 5 €','shopB','pistol');
  if(!(ZONE&&(ZONE.name==='fpark'||ZONE.name==='freibad'||ZONE.name==='camping')))b+=btn('Grill, Musik und Feuerwerk …','campShop');
  if(!ZONE)b+=pfandBtn();
  b+=btn('Wasser kaufen: 1 € (macht nüchterner)','shopB','wasser')+btn('Plausch halten','chat')+btn('Tschüss','back');
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+mk.n+'</h2><div class="mu">Bargeld <b class="gr">'+eur(G.cash)+'</b>'+((ZONE&&ZONE.name==='fpark')?'':' · Bier '+st.bier+' · Joints '+st.joint+((st.gluehwein>0)?' · Glühwein '+st.gluehwein:''))+'</div></div>'+b+'</div>'};
 },
 pack(){
  const L=[];TRADE.forEach(t=>{if(G.inv[t])L.push(GOODS[t].n+': <b>'+G.inv[t]+'</b>');});if(G.inv.koffer)L.push('Geheimrezept: <b>'+G.inv.koffer+'</b>');
  const st=G.stock,am=G.ammo,cur=curAmmo(),why=noUse();
  const b=btn('Bier trinken ('+st.bier+')','drink',null,{off:!!why||st.bier<1,why:why||'Kein Bier mehr.'})+
   btn('Joint rauchen ('+st.joint+')','smoke',null,{off:!!why||st.joint<1,why:why||'Kein Joint mehr.'})+
   btn('Glühwein trinken ('+(st.gluehwein||0)+')','glue',null,{off:!!why||!(st.gluehwein>0),why:why||'Kein Glühwein mehr.'})+
   btn('Sixpack selbst trinken: +6 Bier im Vorrat','tap',null,{off:!myBeer(),why:'Du hast kein Sixpack mit Alkohol dabei.'})+
   btn('Wurfobjekt: '+(cur?AMN[cur]+' ('+(cur==='wasser'?Math.floor(G.tank)+' Tank':am[cur])+')':'nichts'),'sel',null,{off:!(am.dose+am.stein+am.schnee+(am.ei||0)+(G.pistol?1:0)),why:'Such erst Dosen, Steine oder Schneebälle.'})+
   selfBtns()+trankBtns()+campPackBtn()+btn('Zurück','back',null,{def:1});
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>Rucksack ('+used()+' / '+cap()+')</h2><div class="mu">Waren: '+(L.length?L.join(' · '):'keine')+'</div><div class="mu">Vorrat: Bier <b>'+st.bier+'</b> · Joints <b>'+st.joint+'</b> · Dosen <b>'+am.dose+'</b> · Steine <b>'+am.stein+'</b> · Schneebälle <b>'+am.schnee+'</b></div></div>'+b+'</div>'};
 },
 over(){return{hint:'',html:''};}
};

function modalHtml(){
 const m=UI.modal;let c='';
 (m.choices||[]).forEach((x,i)=>{c+='<div class="f btn'+(x.off?' off':'')+'" data-a="'+(x.a||'mclose')+'" data-p="'+(x.p!==undefined?x.p:i)+'">'+x.label+'</div>';});
 let ls='';if(m.lines&&m.lines.length){ls='<ul>';m.lines.forEach(x=>{ls+='<li>'+x+'</li>';});ls+='</ul>';}
 return '<div class="mb"><h2>'+m.title+'</h2><div class="mt">'+(m.text||'')+'</div>'+ls+'<div class="mc">'+c+'</div></div>';
}
function showModal(m){UI.modal=m;render2();}
function closeModal(){UI.modal=null;render2();}
function focusables(){return Array.prototype.slice.call(document.querySelectorAll(UI.modal?'#modal .f':'#ovc .f'));}
function fkey(el){return el.dataset.a+'|'+(el.dataset.p||'');}
function setFocus(el){
 if(!el)return;
 const o=document.querySelector('.focus');if(o)o.classList.remove('focus');
 el.classList.add('focus');
 if(!UI.modal){UI.fk=fkey(el);UI.fkm[UI.screen]=UI.fk;}
 try{el.scrollIntoView({block:'nearest',inline:'nearest'});}catch(e){}
}
function render2(){
 const ov=$('#ov'),m=$('#modal');
 if(UI.screen){
  const s=SCREENS[UI.screen]();
  $('#ovc').innerHTML=s.html;$('#hint').textContent=s.hint;$('#hint').style.display=s.cls==='t'?'none':'block';
  ov.style.display='block';ov.className=s.cls||'';
  if(UI.screen==='map'){const bc=$('#bigmap');if(bc){const bx=bc.getContext('2d');bx.clearRect(0,0,304,192);miniDraw(bx,true);}}
 }else{ov.style.display='none';}
 if(UI.modal){m.innerHTML=modalHtml();m.style.display='flex';}else{m.innerHTML='';m.style.display='none';}
 const list=focusables();
 if(!list.length)return;
 let t=UI.modal?(list.find(e=>e.dataset.def)||list[0]):list.find(e=>fkey(e)===UI.fk);
 if(!t)t=list.find(e=>e.dataset.def)||list[0];
 setFocus(t);
}
function show(s){UI.screen=s;UI.fk=UI.fkm[s]||null;render2();}
function closeAll(){UI.screen=null;UI.modal=null;render2();}
function menuActive(){return !!(UI.screen||UI.modal);}
function nav(dx,dy){
 sfx('tick');
 const list=focusables(),cur=document.querySelector('.focus');
 if(!cur||list.indexOf(cur)<0){if(dy&&kScroll(dy))return;setFocus(list[0]);return;}
 const a=cur.getBoundingClientRect();
 let best=null;
 [1.4,1e9].forEach(function(cone){
  if(best)return;
  let bs=1e12;
  list.forEach(function(el){
   if(el===cur)return;
   const r=el.getBoundingClientRect();
   const vx=(r.left+r.width/2)-(a.left+a.width/2),vy=(r.top+r.height/2)-(a.top+a.height/2);
   const prim=dx?vx*dx:vy*dy;
   if(prim<=2)return;
   let sec=dx?Math.abs(vy):Math.abs(vx);
   const ov=dx?(r.top<a.bottom&&r.bottom>a.top):(r.left<a.right&&r.right>a.left);
   if(ov)sec=sec*.15;
   if(sec>prim*cone)return;
   const sc=prim+sec*2.2;
   if(sc<bs){bs=sc;best=el;}
  });
 });
 if(best)setFocus(best);else if(dy)kScroll(dy);
}
function kScroll(dy){
 const L=Array.prototype.slice.call(document.querySelectorAll(UI.modal?'#modal .mb':'#ovc .panel, #ovc .place, #ovc .sitp, #ovc .pmenu'));
 for(const el of L){if(el.scrollHeight>el.clientHeight+4){const b=el.scrollTop;el.scrollTop+=dy*Math.max(48,el.clientHeight*.45);if(el.scrollTop!==b)return true;}}
 return false;
}
function fire(el){
 if(el.classList.contains('off')){toast(el.dataset.why||'Das geht gerade nicht.');return;}
 sfx('ok');const f=ACT[el.dataset.a];if(f)f(el.dataset.p);
}
function openMarker(mk){
 if(mk.kind==='portal'){usePortal(mk);return;}
 if(mk.kind==='buedchen'){UI.mk=mk;show('buedchen');return;}
 if(mk.kind==='sk'){skMarker(mk);return;}
 if(mk.kind==='scream'){doScream(mk);return;}
 if(mk.kind==='disco'){doDisco(mk);return;}
 if(wanted>0&&mk.kind!=='hq'){toast('Zu heiß! Die Polizei ist hinter dir.');return;}
 G.loc=mk.dist;UI.mk=mk;
 if(mk.kind==='willi'){show('willi');return;}
 show('place');
}
function doAction(){
 if(UI.title||!G||fade)return;
 if(MG){mgPress();return;}
 if(fireActEarly())return;
 if(P.coast){toast(pick(['Gut festhalten! Gleich ist die Fahrt vorbei.','Hände an den Bügel! Aussteigen geht erst am Ende.']));return;}
 if(P.fight){sharkPress();return;}
 if(P.fish){fishPull();return;}
 if(P.inCar){if(Math.abs(V.sp)<60){const mk=nearMarker();if(mk&&Math.hypot(mk.x-V.x,mk.y-V.y)<44){openMarker(mk);return;}if(!exitVan())toast('Hier ist kein Platz zum Aussteigen.');}return;}
 if(P.ride){if(nearWhale()){swallow();return;}leaveRide(false);return;}
 if(P.hide){unhide(false);return;}
 if(P.sit||P.build)return;
 {const hd=nearHide();if(hd){doHide(hd);return;}}
 if(nearThug()){punch();return;}
 if(nearWhale()){swallow();return;}
 const sk=nearShark();
 if(sk){startFight(sk);return;}
 {const q0=nearSk();if(q0&&(QSK[q0.k]||YK[q0.k])){skOpen(q0);return;}}
 const mk=nearMarker();
 {const rd0=nearRide();if(rd0&&(!mk||Math.hypot(rd0.x-P.x,rd0.y-P.y)<Math.hypot(mk.x-P.x,mk.y-P.y)-4)){takeRide(rd0);return;}}
 if(mk){openMarker(mk);return;}
 if(fireActMid())return;
 if(!ZONE){const an0=nearAni();if(an0){aniOpen(an0);return;}}
 if(campNear()){campSit();return;}
 const st=nearSeat();
 if(st){sitDown(st);return;}
 const rd=nearRide();
 if(rd){takeRide(rd);return;}
 const sk7=nearSk();
 if(sk7){skOpen(sk7);return;}
 const an=nearAni();
 if(an){aniOpen(an);return;}
 const pd=nearPed();
 if(pd){UI.ped=pd;show('ped');return;}
 const sm=nearSnowman();
 if(sm){kickSnowman(sm);return;}
 const cs=nearCastle();
 if(cs){kickCastle(cs);return;}
 if(nearVan()){enterVan();return;}
 if(waterAhead()&&!aimBest(130,false)){startFish();return;}
 const cb=ctxBuild();
 if(cb&&!aimBest(130,false)){startBuild(cb);return;}
 throwIt();
}
function pauseGame(){if(UI.title||!G)return;show('pause');}

const ACT={
 new(){
  toCity();H.newGame();UI.fkm={};UI.title=false;UI.hudS=null;UI.trkS=null;cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);
  UI.screen=null;
  showModal({title:'Willkommen bei Entertain Master',text:'Hanfred Hanfbier hat dir ein Feldbett im Imbiss und einen brummenden Hacker-PC im Hinterzimmer überlassen. Im Lager: ein Receiver, eine Antenne, eine Kabelrolle und ein wackeliger M3U-Code. Die Leute in Rheinhanfen wollen alle Sender, die neuesten Filme und Serien. Im Menü findest du die Medien-Zentrale mit den ersten Anfragen. Hardware gibt es bei Elektro-Ramsch, Codes und Hacker-Kurse im Netzcafé Pixelhöhle. Vorsicht vor den Spürwagen mit der Schüssel auf dem Dach! Lieferdienst und Rhein-Apotheke laufen nebenbei weiter. Werde der Entertain Master!',choices:[{label:'Los geht\'s',a:'mclose'}]});
 },
 cont(){if(H.loadAll()){UI.fkm={};UI.title=false;UI.hudS=null;UI.trkS=null;cam.x=camX(P.x-VW/2);cam.y=camY(P.y-VH/2);closeAll();toast(G.migr?'Spielstand geladen. Der Handel ist neu: Deine alten Waren wurden mit '+eur(G.migr)+' gutgeschrieben.':'Spielstand geladen.');G.migr=0;}else toast('Kein Spielstand gefunden.');},
 help(){UI.helpFrom=UI.screen;show('help');},
 quit(){try{window.close();}catch(e){}try{history.back();}catch(e){}},
 back(){back();},
 mclose(){closeModal();},
 market(){show('market');},prod(){show('prod');},ups(){show('ups');},willi(){show('willi');},
 missions(){show('missions');},
 map(){show('map');},
 euro(){UI.euroFrom='pause';show('euro');},
 trav(p){
  if(fade)return;
  if(P.inCar){toast('Steig erst aus dem Van aus.');return;}
  const e=EURO[p],cur=ZONE?ZONE.name:'city';
  if(!e||e.off)return;
  if(cur===p){toast('Da bist du schon. Ein schönes Fleckchen, oder?');return;}
  if(P.sit)standUp();
  if(P.ride)leaveRide(true);
  closeAll();
  if(!ZONE)G.ret={x:P.x,y:P.y};
  if(p==='city')startFade(e.warp,()=>leaveZone(false));
  else startFade(e.warp,()=>enterZone(p));
 },
 inv(){show('pack');},
 inv_old(){
  const L=[];
  TRADE.forEach(t=>{if(G.inv[t])L.push(GOODS[t].n+': '+G.inv[t]);});
  if(G.inv.koffer)L.push('Geheimrezept: '+G.inv.koffer);
  showModal({title:'Rucksack ('+used()+' / '+cap()+')',text:L.length?'':'Du hast nichts dabei.',lines:L,choices:[{label:'Schließen',a:'mclose'}]});
 },
 vanCall(){const r=H.callVan();closeAll();toast(r.msg);},
 saveExit(){H.saveAll();toCity();UI.title=true;UI.screen='title';UI.modal=null;render2();},
 buy(p){const x=p.split(':');if((ALC[x[0]]||ILL[x[0]])&&minorNear(P.x,P.y,120)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht in der Nähe, Alkohol gibt es nur für Erwachsene.');return;}res(H.buy(x[0],x[1]));},
 sell(p){
  const x=p.split(':');if(ALC[x[0]]&&minorNear(P.x,P.y,120)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht in der Nähe, Alkohol gibt es nur für Erwachsene.');return;}const r=H.sell(x[0],x[1]);
  if(r.ok&&r.witness){const near=cops.some(c=>Math.hypot(c.x-P.x,c.y-P.y)<260)||traffic.some(c=>c.cop&&Math.hypot(c.x-P.x,c.y-P.y)<260);if(near){closeAll();startWanted('Ein Polizist hat den Deal gesehen! Weg hier!');return;}}
  res(r);
 },
 brew(p){res(H.startBrew(p));},grow(p){res(H.startGrow(p));},collect(){res(H.collect());},
 up(k){res(H.buyUp(k));},pay(p){res(H.payDebt(p));},loan(p){res(H.loan(+p));},
 accept(id){res(H.accept(+id));},pickup(id){res(H.pickup(+id));},deliver(id){const m=G.active.find(o=>o.id===+id);if(m&&ALC[m.item]&&minorNear(P.x,P.y,120)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht in der Nähe, Alkohol gibt es nur für Erwachsene.');return;}res(H.deliver(+id));checkWin();},
 abandonAsk(id){showModal({title:'Auftrag abbrechen?',text:'Das kostet 1 Respekt.',choices:[{label:'Behalten',a:'mclose'},{label:'Abbrechen',a:'abandon',p:id}]});},
 abandon(id){UI.modal=null;res(H.abandon(+id));},
 sleep(){
  const L=H.sleepHome();closeAll();
  showModal({title:'Guten Morgen',text:'Tag '+G.day+', 06:00 Uhr. Du hast dich ausgeruht, die Fahndung sinkt.',lines:L,choices:[{label:'Weiter',a:'mclose'}]});
 },
 pwin(){closeModal();},
 drink(){doDrink();render2();},
 smoke(){doSmoke();render2();},
 chill(){mood(2,'+2');toast(pick(['Eine Taube setzt sich neben dich. Ihr schweigt vertraut.','Du schaust den Wolken beim Ziehen zu.','Ein Hund guckt dich an. Du guckst zurück. Respekt.','Die Welt ist gerade ziemlich okay.']));render2();},
 glue(){doGluehwein();render2();},
 tea(){teaBonus();render2();},
 skA(p){skAct(p);},
 snd(){toggleSnd();render2();},
 mmpref(){MMPREF=MMPREF==='normal'?'klein':MMPREF==='klein'?'aus':'normal';try{localStorage.setItem('hh_mm',MMPREF);}catch(e){}mmApply();render2();toast(MMPREF==='aus'?'Minikarte ist aus. Die große Karte gibt es weiter im Menü.':MMPREF==='klein'?'Minikarte ist jetzt klein.':'Minikarte ist wieder normal groß.');},
 tpref(){TPREF=TPREF==='auto'?'off':TPREF==='off'?'on':'auto';try{localStorage.setItem('hh_touch',TPREF);}catch(e){}setTouch(TPREF==='on');render2();toast(TPREF==='auto'?'Touch-Tasten erscheinen nur bei Berührung.':TPREF==='off'?'Touch-Tasten sind aus. Nur Fernbedienung und Tastatur.':'Touch-Tasten sind immer an.');},
 stand(){const dk=P.sit&&P.sit.t==='decke';standUp();closeAll();if(dk&&CAMP&&!G.dkTip){G.dkTip=1;toast('Die Decke bleibt liegen. OK an der Decke: wieder hinsetzen. Dort kannst du auch alles einpacken.');}},
 tap(){const g=myBeer();if(!g)return;G.inv[g]--;G.stock.bier=Math.min(40,G.stock.bier+6);toast('Sixpack '+GOODS[g].n+' aufgemacht: +6 Bier im Vorrat.');render2();},
 sel(){const o=['schnee','stein','dose','ei'],have=o.filter(k=>G.ammo[k]>0);if(G.pistol)have.push('wasser');if(!have.length)return;const i=have.indexOf(curAmmo());G.sel=have[(i+1)%have.length];render2();},
 shopB(k){
  const pr={limo:2,hbroet:2,honig:2,koelsch:3,hahn:3,himmel:3,melange:3,schmarrn:4,strudel:3,hausbr:4,waffel:2,panhas:2,bier:3,joint:6,wasser:1,gluehwein:3,pistol:5,mass:5,brezn:2,nata:2,sardine:3,cerveja:3,zucker:2,popcorn:2,lherz:3,brause:2}[k];
  if((k==='bier'||k==='joint'||k==='gluehwein'||k==='mass'||k==='cerveja'||k==='hausbr'||k==='koelsch')&&minorNear(P.x,P.y,90)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht daneben: kein Verkauf von Alkohol und Cannabis.');return;}
  if(G.cash<pr){toast('Nicht genug Geld.');return;}
  if((k==='bier'&&G.stock.bier>=40)||(k==='joint'&&G.stock.joint>=40)||(k==='gluehwein'&&G.stock.gluehwein>=40)||(k==='mass'&&G.stock.bier>=39)||(k==='cerveja'&&G.stock.bier>=40)||(k==='hausbr'&&G.stock.bier>=40)||(k==='koelsch'&&G.stock.bier>=40)){toast('Dein Rucksack ist randvoll.');return;}
  G.cash-=pr;sfx('coin');
  if(k==='bier'){G.stock.bier++;toast('Ein kaltes Bier für 3 €.');}
  else if(k==='joint'){G.stock.joint++;toast('Ein sauber gedrehter Joint für 6 €.');}
  else if(k==='gluehwein'){G.stock.gluehwein++;toast('Ein dampfender Glühwein für 3 €. Prost, Winter!');}
  else if(k==='mass'){G.stock.bier+=2;toast(pick(['Eine ordentliche Maß für 5 €. Zwei Bier im Rucksack, ein Lächeln im Gesicht. Ozapft is!','Die Kellnerin trägt sechs Maß gleichzeitig und stellt dir eine hin. Respekt, Prost!']));}
  else if(k==='brezn'){G.drunk=Math.max(0,G.drunk-1);mood(3,'+3 Brezn');toast('Eine riesige, knusprige Brezn mit viel Salz. Dein Magen sagt Danke.');}
  else if(k==='nata'){mood(3,'+3 Nata');toast('Ein Pastel de Nata, noch warm, mit Zimt obendrauf. Der Teig knistert wie ein Lagerfeuer.');}
  else if(k==='sardine'){mood(3,'+3 Sardine');toast('Eine Sardine frisch vom Grill, dazu Brot. So schmeckt das Meer, wenn es sich Mühe gibt.');}
  else if(k==='cerveja'){G.stock.bier++;toast('Eine Cerveja, eiskalt. Saúde!');}
  else if(k==='limo'){mood(3,'+3 Limo');toast('Hopfen-Limo, komplett ohne Alkohol: herb, prickelnd und überraschend erfrischend.');}
  else if(k==='hbroet'){mood(3,'+3 Brötchen');toast('Ein Brötchen mit Hanfsamen. Nussig, knusprig und rein als Essen gedacht.');}
  else if(k==='honig'){mood(3,'+3 Honigbrot');toast('Honigbrot mit Honig von den Bienen nebenan. Süß, goldgelb und ein bisschen klebrig.');}
  else if(k==='koelsch'){G.stock.bier++;toast('Ein Kölsch in der schlanken Stange, goldgelb und frisch. Der Köbes bringt gleich das nächste, ob du willst oder nicht.');}
  else if(k==='hahn'){mood(3,'+3 Halver Hahn');toast('Ein Halver Hahn: Roggenbrötchen mit Käse. Kein halbes Huhn! Das weiß nur nicht jeder, der es zum ersten Mal bestellt.');}
  else if(k==='himmel'){mood(3,'+3 Himmel un Ääd');toast('Himmel un Ääd: Kartoffelbrei und Apfelmus. Himmel und Erde auf einem Teller, und beide sind lecker.');}
  else if(k==='melange'){G.drunk=Math.max(0,G.drunk-1);mood(3,'+3 Melange');toast('Eine Melange mit Milchschaum und einem Glas Wasser daneben. Du sitzt gerade ein bisschen aufrechter.');}
  else if(k==='schmarrn'){mood(4,'+4 Schmarrn');toast('Kaiserschmarrn: zerrupfter Pfannkuchen, Puderzucker, Zwetschgenmus. Ein Schmarrn, aber ein göttlicher.');}
  else if(k==='strudel'){mood(3,'+3 Strudel');toast('Warmer Apfelstrudel mit Vanillesoße. Der Teig ist so dünn, dass man die Zeitung dadurch lesen könnte.');}
  else if(k==='hausbr'){G.stock.bier++;toast('Hausbräu frisch vom Fass, goldgelb und mit perfekter Schaumkrone. Der Braumeister nickt stolz.');}
  else if(k==='waffel'){mood(3,'+3 Waffel');toast('Eine knusprige Bergische Waffel mit heißen Kirschen und Sahne. Die Kirschen sind heißer als dein Humor.');}
  else if(k==='panhas'){mood(3,'+3 Panhas');toast('Panhas mit Apfelmus. Rustikal, kräftig und überraschend lecker. Du fragst nicht, was drin ist.');}
  else if(k==='zucker'){mood(4,'+4 Zuckerwatte');toast(pick(['Eine rosa Zuckerwatte, so groß wie dein Kopf. Klebt überall, schmeckt nach Kindheit.','Zuckerwatte! Nach drei Bissen ist sie weg, das Grinsen bleibt.']));}
  else if(k==='popcorn'){mood(3,'+3 Popcorn');toast('Eine Tüte warmes Popcorn, halb süß, halb salzig. Die Tauben folgen dir ab jetzt.');}
  else if(k==='lherz'){mood(5,'+5 Lebkuchenherz');toast('Ein Lebkuchenherz mit der Aufschrift „Rheinhanfen ist super“. Viel zu schön zum Essen. Fast.');}
  else if(k==='brause'){mood(3,'+3 Brause');toast('Eine Waldmeister-Brause, quietschgrün und ganz ohne Alkohol. Es prickelt bis in die Ohren.');}
  else if(k==='pistol'){G.pistol=true;G.tank=30;G.sel='wasser';toast('Wasserpistole gekauft! Der Tank füllt sich im Wasser. OK spritzt.');}
  else{G.drunk=Math.max(0,G.drunk-2);toast('Wasser! Der Kopf wird klarer.');}
  render2();
 },
 chat(){mood(2,'+2');toast(pick(['Der Besitzer erzählt vom Wetter. Es war schon mal besser. Oder schlechter.','Du erfährst den neuesten Tratsch: Die Tauben haben eine Gewerkschaft.','Ein Stammgast erklärt dir die Weltlage anhand von Pfandflaschen.']));},
 pHi(){const p=UI.ped;closeAll();if(!p)return;sfx('clap');p.st='hug';p.stT=1.3;P.a=Math.atan2(p.y-P.y,p.x-P.x);const v=p.like?7:4;mood(v,'+'+v);addFx(p.x,p.y-18,'Klatsch!','#ffd23f');toast(pick(p.like?HIL:HIN));},
 pHug(){const p=UI.ped;closeAll();if(!p)return;sfx('aww');p.st='hug';p.stT=2.2;P.a=Math.atan2(p.y-P.y,p.x-P.x);const v=p.like?10:5;mood(v,'+'+v+' ♥');addFx(p.x,p.y-18,'♥','#ff4d7a',1.6);toast(p.like?'Eine herzliche Umarmung. '+p.nm+' strahlt wie ein Kühlschrank.':'Eine etwas steife Umarmung. Aber sie war ehrlich.');},
 pDance(){const p=UI.ped;closeAll();if(!p)return;sfx('disco');p.st='dance';p.stT=4;P.dance=4;mood(8,'+8 ♪');for(let i=0;i<5;i++)addFx(p.x+rf(-24,24),p.y+rf(-20,10),pick(['♪','♫']),pick(['#ff5fd0','#5ff0ff','#ffd23f']),1.6,-30);toast('Ihr tanzt einfach drauflos. Niemand hält euch auf.');},
 pRace(){const p=UI.ped;closeAll();if(!p)return;const r=startRace(p);toast(r.msg);},
 pTongue(){const p=UI.ped;closeAll();if(!p)return;sfx('pfft');if(chance(.5)){p.st='laugh';p.stT=2;mood(4,'+4');addFx(p.x,p.y-18,'Haha!','#6bcf63');toast(p.nm+' prustet vor Lachen. Frechheit siegt.');}else{p.st='angry';p.stT=2.5;mood(2,'+2');addFx(p.x,p.y-18,'#!?*','#e5604d');toast(p.nm+' ist empört und marschiert davon.');}},
 pPush(){const p=UI.ped;closeAll();if(!p||inNoGo(P.x,P.y))return;sfx('bonk');const a=Math.atan2(p.y-P.y,p.x-P.x);P.a=a;moveE(p,Math.cos(a)*26,Math.sin(a)*26,7);p.st='dazed';p.stT=2;mood(4,'+4');heat(2);popAdd(-2);addFx(p.x,p.y-18,'Hoppla!','#ffd23f');toast(pick(['Ups! '+p.nm+' sitzt auf dem Hosenboden.','Ein kleiner Schubser. '+p.nm+' dreht sich dreimal im Kreis.']));},
 pHit(){
  const p=UI.ped;closeAll();if(!p||inNoGo(P.x,P.y))return;sfx('hit');
  const a=Math.atan2(p.y-P.y,p.x-P.x);P.a=a;
  moveE(p,Math.cos(a)*34,Math.sin(a)*34,7);
  p.st='dazed';p.stT=3;G.stats.fights++;
  for(let i=0;i<4;i++)FX.push({x:p.x,y:p.y-8,vx:rf(-34,34),vy:rf(-46,-12),t:0,life:.9,txt:'★',col:'#ffd23f'});
  addFx(p.x,p.y-18,pick(['AUA!','Hey!','Uff!','Meine Brille!']),'#ffd23f');
  mood(10,'Dampf abgelassen');heat(6);popAdd(-3);
  if(copNear(P.x,P.y,230)){startWanted('Ein Polizist hat dich beim Prügeln gesehen! Lauf!');}
  else toast(pick(['Er rappelt sich beleidigt wieder auf. Niemand ist ernsthaft verletzt.','Peng! Das tat gut. '+p.nm+' sieht dich nur vorwurfsvoll an.','Dampf abgelassen. '+p.nm+' klopft sich den Staub ab und trollt sich.']));
 }
};
function back(){
 if(UI.modal){if(UI.modal.noBack)return;closeModal();return;}
 const s=UI.screen;
 if(s==='help'){if(UI.title)show('title');else if(UI.helpFrom==='pause')show('pause');else closeAll();return;}
 if(MEDS[s]){medBack(s);return;}
 if(s==='sit'){standUp();closeAll();return;}
 if(s==='pack'){show('pause');return;}
 if(s==='campshop'){show('buedchen');return;}
 if(s==='market'||s==='prod'||s==='ups'){show('place');return;}
 if(s==='immo'){show('willi');return;}
 if(s==='grow'){if(UI.growFrom==='place')show('place');else if(UI.growFrom==='pause')show('pause');else closeAll();return;}
 if(s==='missions'&&UI.misFrom==='place'){UI.misFrom=null;show('place');return;}
 if(s==='offer'){show('ped');return;}
 if(s==='missions'||s==='map'){show('pause');return;}
 if(s==='euro'){if(UI.euroFrom==='pause')show('pause');else closeAll();return;}
 if(s==='title')return;
 closeAll();
}
H.setCb(function(m){
 if(m.indexOf('__win')===0){const v=+(m.split(':')[1]||15000);showModal({title:'Meilenstein: '+eur(v)+'!',text:'Du hast '+eur(v)+' Vermögen erreicht. Rang: '+rank(worth())+'. Das Spiel geht endlos weiter: Kauf dir Landschaften beim Makler in Willis Kontor, steig Stufen auf und werde die Legende von Rheinhanfen.',choices:[{label:'Weiterspielen',a:'mclose'}]});return;}
 toast(m);
},function(lines){
 UI.screen=null;
 showModal({title:'Festnahme!',text:'Die Polizei hat dich erwischt.',lines:lines,choices:[{label:'Weiter',a:'mclose'}]});
});

const held={};
function keyDown(e){
 if(fade){e.preventDefault();return;}
 const k=e.key,c=e.keyCode;
 if((k==='m'||k==='M')&&!menuActive()&&!UI.title&&G){toggleSnd();toast('Ton '+(SND.on?'an':'aus'));e.preventDefault();return;}
 if((k==='k'||k==='K')&&!menuActive()&&!UI.title&&G){UI.euroFrom='';show('euro');e.preventDefault();return;}
 let dir=null;
 if(k==='ArrowLeft'||c===21||k==='a'||k==='A')dir='left';
 else if(k==='ArrowRight'||c===22||k==='d'||k==='D')dir='right';
 else if(k==='ArrowUp'||c===19||k==='w'||k==='W')dir='up';
 else if(k==='ArrowDown'||c===20||k==='s'||k==='S')dir='down';
 const act=(k==='Enter'||k===' '||c===23||c===13);
 const bk=(k==='Escape'||k==='Backspace'||k==='GoBack'||c===4||c===27||c===8);
 if(menuActive()){
  if(dir==='left')nav(-1,0);else if(dir==='right')nav(1,0);else if(dir==='up')nav(0,-1);else if(dir==='down')nav(0,1);
  else if(act){const f=document.querySelector('.focus');if(f)fire(f);}
  else if(bk)back();
  else return;
  e.preventDefault();return;
 }
 if(dir){keys[dir]=1;e.preventDefault();return;}
 if(act){if(!e.repeat)doAction();e.preventDefault();return;}
 if(bk){pauseGame();e.preventDefault();}
}
function keyUp(e){
 const k=e.key,c=e.keyCode;
 if(k==='ArrowLeft'||c===21||k==='a'||k==='A')keys.left=0;
 else if(k==='ArrowRight'||c===22||k==='d'||k==='D')keys.right=0;
 else if(k==='ArrowUp'||c===19||k==='w'||k==='W')keys.up=0;
 else if(k==='ArrowDown'||c===20||k==='s'||k==='S')keys.down=0;
}
let TPREF='auto';try{TPREF=localStorage.getItem('hh_touch')||'auto';}catch(e){}
function setTouch(on){CPAD.n=0;
 if(TPREF==='off')on=false;else if(TPREF==='on')on=true;
 document.body.classList.toggle('touch',!!on);
}
setTouch(false);mmApply();
document.addEventListener('keydown',function(e){if(e.isTrusted)setTouch(false);});
document.addEventListener('keydown',keyDown);
document.addEventListener('keyup',keyUp);
document.addEventListener('pointerdown',function(e){if((e.pointerType==='touch'||e.pointerType==='pen')&&(navigator.maxTouchPoints||0)>0)setTouch(true);},true);
(function(){
 const map={tUp:'ArrowUp',tLf:'ArrowLeft',tRt:'ArrowRight',tDn:'ArrowDown',tOk:'Enter',tBk:'Escape'};
 Object.keys(map).forEach(function(id){
  const el=document.getElementById(id),key=map[id];
  const mk=function(){return{key:key,keyCode:0,repeat:false,preventDefault:function(){}};};
  const on=function(e){e.preventDefault();e.stopPropagation();try{el.setPointerCapture(e.pointerId);}catch(x){}el.classList.add('on');keyDown(mk());};
  const off=function(e){e.preventDefault();if(!el.classList.contains('on'))return;el.classList.remove('on');keyUp(mk());};
  el.addEventListener('pointerdown',on);
  el.addEventListener('pointerup',off);
  el.addEventListener('pointercancel',off);
  el.addEventListener('lostpointercapture',off);
  el.addEventListener('contextmenu',function(e){e.preventDefault();});
 });
})();
window.addEventListener('blur',function(){keys.left=keys.right=keys.up=keys.down=0;});
document.addEventListener('mouseover',function(e){
 const el=e.target.closest?e.target.closest('.f'):null;
 if(el&&focusables().indexOf(el)>=0&&!el.classList.contains('focus'))setFocus(el);
});
document.addEventListener('click',function(e){
 const el=e.target.closest?e.target.closest('.f'):null;
 if(el&&focusables().indexOf(el)>=0){setFocus(el);fire(el);}
});
function fit(){
 const w=window.innerWidth,h=window.innerHeight;
 const nv=Math.max(540,Math.min(1400,Math.round(540*w/h/2)*2));
 if(nv!==VW){VW=nv;cv.width=VW;cv.height=VH;}
 CPAD.n=0;
 const cw=Math.min(w,h*VW/VH);
 cv.style.width=cw+'px';cv.style.height=(cw*VH/VW)+'px';
 document.documentElement.style.fontSize=(Math.min(w,h*16/9)/77)+'px';
}
function isFS(){return !!(document.fullscreenElement||document.webkitFullscreenElement);}
function goFS(){
 if(isFS())return;
 const d=document.documentElement,f=d.requestFullscreen||d.webkitRequestFullscreen||d.webkitRequestFullScreen;
 if(!f)return;
 try{
  const r=f.call(d);
  const after=function(){
   try{if(navigator.keyboard&&navigator.keyboard.lock)navigator.keyboard.lock(['Escape']).catch(function(){});}catch(e){}
   try{if(screen.orientation&&screen.orientation.lock)screen.orientation.lock('landscape').catch(function(){});}catch(e){}
  };
  if(r&&r.then)r.then(after).catch(function(){});else after();
 }catch(e){}
}
['keydown','pointerdown','touchend','click'].forEach(function(n){document.addEventListener(n,goFS,true);});
document.addEventListener('fullscreenchange',fit);
document.addEventListener('webkitfullscreenchange',fit);
window.addEventListener('orientationchange',function(){setTimeout(fit,200);});
window.addEventListener('resize',fit);fit();

renderWorld();
cam.x=14*TS;cam.y=4*TS;
let last=performance.now(),hudT=0,titleT=0;
function frame(now){
 const dt=Math.min(.05,(now-last)/1000);last=now;fdt=dt;
 if(fade){fade.t+=dt;if(!fade.done&&fade.t>=fade.dur*.5){fade.done=true;fade.cb();}if(fade.t>=fade.dur)fade=null;}
 else if(UI.title||!G){
  titleT+=dt;
  const px=(MW*TS-VW)/2+Math.cos(titleT*.12)*(MW*TS-VW)/2.2,py=(MH*TS-VH)/2+Math.sin(titleT*.17)*(MH*TS-VH)/2.2;
  cam.x=clamp(px,0,MW*TS-VW);cam.y=clamp(py,0,MH*TS-VH);
  trafficUpdate(dt);pedsUpdate(dt);spTick(dt);
 }else if(!menuActive()||(UI.screen==='sit'&&!UI.modal))update(dt);
 render();musicTick();
 hudT+=dt;if(hudT>.1){hudT=0;hudUpdate();if(G&&!UI.title)renderMini();}
 requestAnimationFrame(frame);
}
resetEntities();
UI.screen='title';
render2();
requestAnimationFrame(frame);
Object.assign(ACT,CAMPACT);
Object.assign(ACT,{eat(){eatMenu(UI.mk&&UI.mk.dist);}});
{const _sb=ACT.shopB;ACT.shopB=function(k){const c=G.cash;_sb.call(ACT,k);if(G.cash<c&&SHOPN[k])needAdd(SHOPN[k][0],SHOPN[k][1]);};}
Object.assign(ACT,{selfEat(g){selfEat(g);},selfDrink(){selfDrink();}});
Object.assign(ACT,{freeMe(){freeMe();},homeTake(k){res(homeTake(k));},kBuy(k){kBuy(k);},pAct(){const p=UI.ped;closeAll();if(!p||!p.act||!PACT[p.act])return;const A=PACT[p.act];p.like=true;popAdd(1);mood(4,'+4 Nett');sfx('clap');addFx(p.x,p.y-22,'♥','#ff7fb0',1.4);toast(p.nm+': '+pick(A.r));}});
Object.assign(SCREENS,{homes(){return homesScreen();}});
{const _sl=ACT.sleep;ACT.sleep=function(){_sl.call(ACT);if(UI.modal&&UI.modal.title==='Guten Morgen'){const W=homeWake('imbiss');UI.modal.lines=W.concat(UI.modal.lines||[]);render2();}};}
medRegister();
window.HHC={CPAD:CPAD,camPad:camPad,dims:()=>({MW:MW,MH:MH,VW:VW,VH:VH,TS:TS}),cam:()=>({x:cam.x,y:cam.y})};
window.HHK={HOMES:HOMES,homeK:homeK,homeTake:homeTake,homeDay:homeDay,kSleep:kSleep,skAct19:skAct19,fbSlide:fbSlide,fbJump:fbJump,rodelGo:rodelGo,skiGo:skiGo,FBS:FBS,SKIG:SKIG,RODEL:RODEL,GBP:GBP,GBLIFT:GBLIFT,kpAt:kpAt,kpBuild:kpBuild,KSKM:KSKM,kBuy:kBuy,newDay:newDay,kEvent:kEvent,KEL:()=>KEL,setKEL:v=>{KEL=v;},PACT:PACT,pActPick:pActPick,KBEPS:KBEPS,skAct20:skAct20,show:show,closeAll:closeAll,openMarker:openMarker,render2:render2};
window.HHJ={unstuck:unstuck,freeMe:freeMe,BEPS:BEPS,bepStart:bepStart,BEA:()=>BEA,qEvent:qEvent,skAct18:skAct18,xrSteal:xrSteal,rideWet:rideWet,XRD:XRD,pushOut:pushOut};
Object.assign(SCREENS,{offer(){return pedOfferScreen();},immo(){return immoScreen();},grow(){return growScreen();}});
Object.assign(ACT,{makler(){show('immo');},immo(k){res(immoBuy(k));},growS(){UI.growFrom=UI.screen;show('grow');},gsel(i){UI.gs=+i;render2();},gplant(){growAct('plant');},gwater(){growAct('water');},gfood(){growAct('food');},glove(){growAct('love');},gharv(){growAct('harv');},pfand(){pfandGive();},toPlant(){const m=MKQ.land;if(!ZONE&&m)G.ret={x:m.x,y:m.y+32};closeAll();startFade('Du läufst über die Felder hinter dem Landgut. Hohe Zäune, Kameras, ein Pförtnerhaus: die Hanfplantage Rheinhanfen.',()=>enterZone('plantage'));}});
window.HHP={hideGen:hideGen,HIDES:()=>HIDES,nearHide:nearHide,doHide:doHide,unhide:unhide,pfandGive:pfandGive,growAct:growAct,plantTick:plantTick,immoBuy:immoBuy,xpAdd:xpAdd,popAdd:popAdd,popWord:popWord,IMMO:IMMO,skAct17:skAct17,plantCaught:plantCaught,sees:sees,wachPos:wachPos,PZ:PZ,dayHook:dayHook,checkWin:checkWin,rank:rank};
Object.assign(ACT,{trank(k){drinkTrank(k);},aniFree(){const d=aniLead();if(!d)return;d.fol=false;closeAll();toast(d.nm+' bleibt stehen und schnuppert an einer Laterne. OK holt '+d.nm+' wieder an die Leine.');},aniGive(w){res(aniGive(w));}});
window.HHA={ANI:()=>ANI,ANT:ANT,aniSpawn:aniSpawn,aniLead:aniLead,aniGive:aniGive,nearAni:nearAni,aniOpen:aniOpen,mascList:mascList,zooFill:zooFill,legAt:legAt,drinkTrank:drinkTrank,skAct16:skAct16,xnOpen:xnOpen,nearVan:nearVan};
Object.assign(ACT,{needBuy(){res(buyNeeded(G.loc));},apoMis(){UI.misFrom='place';show('missions');},kalle(){kalleMenu();},kalleB(q){kalleBuy(q);},holl(q){hollBuy(q);},pOffer(){show('offer');},pBack(){show('ped');},pSell(g){pedSell(g);}});
window.HHT={SHOP:SHOP,MENUS:MENUS,BEERS:BEERS,GOODS:GOODS,mkOffer:mkOffer,buyAt:buyAt,needAt:needAt,buyNeeded:buyNeeded,pedSell:pedSell,pedPrice:pedPrice,streetRisk:streetRisk,illegal:illegal,mTgt:mTgt,nearSrc:nearSrc,arrest:arrest,newDay:newDay,price:price};
window.HHE={boatFree:boatFree,bridgeOK:bridgeOK,boatMove:boatMove,cityBoats:cityBoats,boatCall:boatCall,eatMenu:eatMenu,eMenu:eMenu,skAct15:skAct15,poloStart:poloStart,POLO:()=>POLO,FOOD:FOOD,CBOAT:CBOAT};
window.HHF={FIRE:()=>FIRE,TRUCK:()=>TRUCK,HYD:HYD,fireStart:fireStart,fireTree:fireTree,boltStrike:boltStrike,fireCands:fireCands,koHospital:koHospital,fwOwn:fwOwn,fwShow:fwShow,FWP:()=>FWP,FWR:()=>FWR,FWQ:()=>FWQ,BURNT:BURNT,fairyEvent:fairyEvent,FAIRY:FAIRY,schatzNeu:schatzNeu,skAct14:skAct14,fairyOpen:fairyOpen,skSpawn:skSpawn,SKC:()=>SKC,hydNear:hydNear,fireNearPt:fireNearPt};
window.HHS={SP:()=>SP,MG:()=>MG,SPF:SPF,FPK:FPK,mgStart:mgStart,mgPress:mgPress,mgEnd:mgEnd,spRoll:spRoll,spTick:spTick,fbGoal:fbGoal,fpRideStart:fpRideStart,fpTick:fpTick,skAct13:skAct13,sportMenu:sportMenu,fpMenu:fpMenu,dosMenu:dosMenu,coastPt:coastPt,flockeHi:flockeHi,miniDraw:miniDraw,minorNear:minorNear,bsPts:bsPts,campStart:campStart,campEnd:campEnd,CAMP:()=>CAMP,campCan:campCan,campInvite:campInvite,campMus:campMus,campGrill:campGrill,campFire:campFire,campRoast:campRoast,campStory:campStory,musicTick:musicTick,SONGS:SONGS,MUS:MUS,campFireSpot:campFireSpot,campNear:campNear};
window.HHW={H:H,G:()=>G,P:P,V:V,keys:keys,update:update,UI:UI,ACT:ACT,world:{T:T,MKS:MKS,MKQ:MKQ,MW:MW,MH:MH,TS:TS,isSolid:isSolid,YARD:YARD},ents:()=>({traffic:traffic,peds:peds,cops:cops,thugs:thugs,chasers:chasers,wanted:wanted}),
 doAction:doAction,computeFlow:computeFlow,startWanted:startWanted,renderFrame:render,hudUpdate:hudUpdate,cam:cam,Z:()=>ZONE,enterZone:enterZone,leaveZone:leaveZone,WORLDS:WORLDS,PICKS:()=>PICKS,FX:()=>FX,PR:()=>PR,peds:()=>peds,kids:()=>kids,startRace:startRace,throwIt:throwIt,mood:mood,doDrink:doDrink,doSmoke:doSmoke,nearSeat:nearSeat,sitDown:sitDown,standUp:standUp,NOGO:NOGO,WXC:WXC,fadeNow:()=>fade,toCity:toCity,startFade:startFade,pickZone:pickZone,genZone:genZone,SOL:SOL,tget:tget,RIDES:()=>RIDES,CAS:()=>CAS,SND:SND,sfx:sfx,takeRide:takeRide,leaveRide:leaveRide,nearRide:nearRide,ctxBuild:ctxBuild,startBuild:startBuild,stealChair:stealChair,doGluehwein:doGluehwein,shootWater:shootWater,rideDrive:rideDrive,promptText:promptText,isDeep:isDeep};
['keydown','pointerdown','touchstart','click'].forEach(function(ev){document.addEventListener(ev,sndWake,true);});
})();
</script>
<script>
(function(){
 var trap=0,bk=0,quitting=0;
 function pushTrap(){if(trap)return;try{history.pushState({hh:1},'');trap=1}catch(e){}}
 function closeGame(){try{if(window.parent!==window){window.parent.history.back();return}}catch(e){}if(history.length>1)history.back();else location.href='/ui/'}
 function quit(){try{if(window.HHW&&HHW.G()&&!HHW.UI.title)HHW.H.saveAll()}catch(e){}quitting=1;if(trap)history.back();else closeGame()}
 document.addEventListener('keydown',function(e){if(!e.isTrusted)return;var k=e.key,c=e.keyCode;if(k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack'||c===4||c===27||c===8)bk=Date.now()},true);
 addEventListener('popstate',function(){
  if(!trap)return;trap=0;
  if(quitting){closeGame();return}
  var U=window.HHW&&HHW.UI;
  if(!U||(U.title&&U.screen==='title'&&!U.modal)){closeGame();return}
  pushTrap();
  if(Date.now()-bk<350)return;
  document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true,cancelable:true}));
 });
 if(window.HHW&&HHW.ACT)HHW.ACT.quit=quit;
 pushTrap();
})();
</script>
</body>
</html>
"""
