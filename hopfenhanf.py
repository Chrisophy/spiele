# -*- coding: utf-8 -*-
# Hopfen & Hanf
# IT('s) Possible
# 2026.11.21

EXT_ID = 'hopfenhanf'
EXT_NAME = 'Hopfen & Hanf'
EXT_DESCRIPTION = '🍺 Open-World-Spiel in Rheinhafen: Du arbeitest in der Rhein-Apotheke, braust, baust an, lieferst Aufträge aus und bist nebenbei Superheld. Mit Strand, Bergen, Wal, Märchenwald, Schlaraffenland und Amsterdam. Fernbedienung und Touch. Alles Fiktion, Jugendschutz inklusive.'
EXT_LINKS = [('Hopfen & Hanf', 'index')]
EXT_SETTINGS = []


def register(api):
    api.route('index', lambda req: PAGE)
    api.widget('Hopfen & Hanf', lambda: {'text': 'Hopfen & Hanf', 'sub': 'Open-World in Rheinhafen', 'icon': '🍺'}, ttl=3600, icon='🍺')


PAGE = r"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#000000">
<title>Hopfen &amp; Hanf – Rheinhafen</title>
<style>
:root{--bg:#0c100d;--p:#161c17;--p2:#1e2620;--ln:#2f3b31;--tx:#ece6d6;--mu:#9aa593;--am:#f2b441;--gr:#6bcf63;--rd:#e5604d;--bl:#6fb3e0}
*{box-sizing:border-box}
html,body{height:100%;margin:0;overflow:hidden;background:#000;color:var(--tx);font-family:"Trebuchet MS","Segoe UI",Roboto,Arial,sans-serif;-webkit-user-select:none;user-select:none}
#stage{position:fixed;left:0;top:0;width:100%;height:100%;background:#000;overflow:hidden}
#cv{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:100%;height:100%;background:#0c100d;image-rendering:pixelated}
#hud{position:absolute;left:0;right:0;top:0;display:flex;gap:.4rem;padding:.4rem .5rem;pointer-events:none}
.chip{flex:1;background:rgba(12,16,13,.78);border:1px solid var(--ln);border-radius:.45rem;padding:.2rem .5rem;min-width:0}
.chip small{display:block;font-size:.58rem;letter-spacing:.08em;color:var(--mu);white-space:nowrap}
.chip b{font-size:.95rem;white-space:nowrap}
.am{color:var(--am)}.gr{color:var(--gr)}.rd{color:var(--rd)}.bl{color:var(--bl)}.mu{color:var(--mu)}
.hb{height:.55rem;background:#0b0f0c;border-radius:.4rem;margin-top:.25rem;overflow:hidden;border:1px solid var(--ln)}
.hb i{display:block;height:100%}
#trk{position:absolute;left:.5rem;bottom:.5rem;max-width:30%;pointer-events:none}
#trk div{background:rgba(12,16,13,.78);border:1px solid var(--ln);border-left:.3rem solid var(--am);border-radius:.4rem;padding:.2rem .5rem;margin-top:.25rem;font-size:.7rem;line-height:1.25}
#trk div.k{border-left-color:var(--rd)}#trk div.b{border-left-color:var(--bl)}
#prompt{position:absolute;left:50%;bottom:7%;transform:translateX(-50%);background:rgba(12,16,13,.85);border:2px solid var(--am);border-radius:.6rem;padding:.3rem .9rem;font-size:.95rem;display:none;white-space:nowrap}
#mm{position:absolute;right:.5rem;bottom:.5rem;width:16rem;height:10.1rem;border:2px solid var(--ln);border-radius:.4rem;background:#000;pointer-events:none}
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
#hud{right:76px}
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
let ZONE=null;let VW=960,MW=76,MH=48;const TS=32,VH=540,DAY_S=150,FOOT=104;
const VR=[6,24,42,60,74],HR=[0,14,30,46];
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
 for(let r=0;r<3;r++)for(let c=0;c<4;c++){const b=blockOf(c,r);fillR(b.x0,b.y0,b.x1-b.x0+1,b.y1-b.y0+1,SW);}
 let b=blockOf(0,0);
 fillR(10,4,12,8,SW);
 fillR(10,4,12,1,FN);fillR(10,11,12,1,FN);fillR(10,4,1,8,FN);fillR(21,4,1,8,FN);
 fillR(15,11,2,1,SW);
 addB(11,5,5,4,'#8a8f98','APOTHEKE','house',8);
 addB(17,5,4,4,'#bfe6e0','HANF-LABOR','glass',6);
 fillR(11,10,2,1,CR);
 [[9,3],[22,3],[9,12],[22,12],[13,12],[18,12]].forEach(t=>tree(t[0],t[1]));
 mkm('hq','hq','hq',16,9,'Apotheke','#6bcf63');
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
}
genExtras();
const MKQ={};MKS.forEach(m=>{MKQ[m.id]=m;});
function mdist(a,b){const p=MKQ[a],q=MKQ[b];return Math.hypot(p.x-q.x,p.y-q.y)/TS;}
const ZONES=[{x:73.5*TS,y:12.5*TS},{x:73.5*TS,y:28.5*TS},{x:23.5*TS,y:38.5*TS}];
const YARD={x0:11*TS,y0:5*TS,x1:21*TS,y1:11*TS};
const GATE={x:16*TS+16,y:10*TS+16},VAN0={x:13*TS+16,y:10*TS+16};

const GOODS={
 hopfen:{n:'Hopfen',base:18},malz:{n:'Malz',base:14},samen:{n:'Hanfsamen',base:38},
 bier:{n:'Fassbier',base:70},gras:{n:'Cannabis',base:115},koffer:{n:'Rezept-Paket',base:0}
};
const TRADE=['hopfen','malz','samen','bier','gras'];
const DIST={
 hq:{n:'Rhein-Apotheke',sub:'Dein Arbeitsplatz',d:'Hier arbeitest du. Bestellt, gebraut, angebaut, verkauft und geliefert wird alles legal und mit Lizenz. Abends ist hier alles sicher.'},
 villen:{n:'Villa Blumenthal',sub:'Villenviertel',mod:{hopfen:1.5,malz:1.5,samen:1.5,bier:1.5,gras:1.9},d:'Wohlhabende Kundschaft zahlt gut und bestellt gern nach.'},
 uni:{n:'Mensa-Hinterhof',sub:'Uni-Viertel',mod:{hopfen:1.3,malz:1.3,samen:1.4,bier:1.15,gras:1.5},d:'Chronisch pleite, chronisch durstig. Verkauf nur an Volljährige mit Ausweis.'},
 altstadt:{n:'Zum goldenen Fass',sub:'Altstadt',mod:{hopfen:1.2,malz:1.2,samen:1.3,bier:1.45,gras:1.1},d:'Die längste Theke der Stadt. Wirte zahlen gut für Fassbier.'},
 land:{n:'Landgut Hopfenhof',sub:'Landgut',mod:{hopfen:.7,malz:.65,samen:.85,bier:1,gras:.8},d:'Hopfen und Malz direkt vom Feld. Der Bauer winkt freundlich.'},
 club:{n:'Club Neon',sub:'Clubmeile',mod:{hopfen:1.4,malz:1.4,samen:1.5,bier:1.25,gras:1.65},d:'Bass, Nebel und volle Taschen. Die Türsteher kontrollieren Ausweise: erst ab 18!'},
 hafen:{n:'Hafen-Großhandel',sub:'Hafen',mod:{hopfen:.75,malz:.8,samen:.7,bier:.85,gras:.9},d:'Billige Ware, raue Typen. Wer hier einkauft, lebt günstig.'},
 stadion:{n:'Stadionkiosk',sub:'Stadion',mod:{hopfen:1.2,malz:1.2,samen:1.3,bier:1.6,gras:.85},d:'90 Minuten Durst. An Spieltagen kennt der Bierpreis keine Grenzen.'}
};
const MARKETS=Object.keys(DIST).filter(k=>DIST[k].mod);
const BRAU_CAP=[3,5,8,12],HAUS_CAP=[2,4,6,9];
const UPS={
 brau:{n:'Brauerei',cost:[600,1400,3000],eff:l=>'Sud fasst '+BRAU_CAP[l]+' Ansätze (je 2 Fass)'},
 haus:{n:'Gewächshaus',cost:[900,2000,4200],eff:l=>'Beet fasst '+HAUS_CAP[l]+' Ansätze (je 3 Gras)'},
 trunk:{n:'Laderaum',cost:[400,900,1800],eff:l=>'Du trägst '+(30+15*l)+' Einheiten'},
 tuning:{n:'Getunter Van',cost:[700,1600],eff:l=>'Van fährt '+(l*25)+' km/h-Punkte schneller'},
 leib:{n:'Leibwächter',cost:[500,1200,2500],eff:l=>'Überfälle werden zu '+(l*20)+'% abgewehrt'},
 anwalt:{n:'Anwalt',cost:[800,1800],eff:l=>l===1?'Festnahme kostet weniger, Fahndung sinkt schneller':'Noch geringere Strafen'}
};
const NAMES={
 lieferung:['Wirt Harald','Schützenverein','Kleingärtner-Club','Hochzeitsgesellschaft','Fußball-Fanclub','Burschenschaft','Kegelclub Alle Neune','Tante Gerdas Imbiss'],
 beschaffung:['Brauer Alois','Gärtner Kevin','Hobby-Brauerei Schmitz','Biergarten Rosi','Dr. Hopfen'],
 kurier:['Klinik St. Rhein','Hausarzt Dr. Brandt','Seniorenheim Abendsonne','Frau Müller (Rezept)']
};
const EVT=[
 {t:'Stadtfest in der Altstadt: Bier ist gefragt wie nie.',m:[['bier','altstadt',1.5]]},
 {t:'Heimspiel im Stadion: Die Fans sind durstig.',m:[['bier','stadion',1.7],['bier','altstadt',1.2]]},
 {t:'Semesterstart: Die Uni feiert.',m:[['gras','uni',1.4],['bier','uni',1.3]]},
 {t:'Hopfenmangel: Hopfen kostet überall das Doppelte.',m:[['hopfen','*',2]]},
 {t:'Rekordernte: Cannabis und Samen sind überall günstig.',m:[['gras','*',.65],['samen','*',.8]]},
 {t:'Brauerei-Streik: Bier wird knapp.',m:[['bier','*',1.35]]},
 {t:'Betriebsfeier im Villenviertel: Man will anstoßen.',m:[['bier','villen',1.4]]},
 {t:'Hitzewelle: Alle wollen ein kaltes Bier.',m:[['bier','*',1.25]]}
];

let G=null;
let notify=function(){};
function cap(){return 30+15*G.up.trunk;}
function used(){return TRADE.reduce((s,g)=>s+G.inv[g],0)+G.inv.koffer;}
function heat(v){G.heat=clamp(G.heat+v,0,100);}
function evMult(g,d){let m=1;G.events.forEach(e=>{(e.m||[]).forEach(x=>{if((x[0]===g||x[0]==='*')&&(x[1]===d||x[1]==='*'))m*=x[2];});});return m;}
function price(g,d){const imp=clamp((G.imp[d+g]||0)*.006,-.2,.2);return Math.max(1,Math.round(GOODS[g].base*DIST[d].mod[g]*G.mkt[g]*(G.noise[d+g]||1)*evMult(g,d)*(1-imp)));}
function sellP(g,d){return Math.max(1,Math.round(price(g,d)*.85));}
function rollMarket(){
 TRADE.forEach(g=>{G.mkt[g]=clamp(G.mkt[g]*(1+(Math.random()-.5)*.26)+(1-G.mkt[g])*.2,.8,1.3);});
 MARKETS.forEach(d=>{TRADE.forEach(g=>{G.noise[d+g]=.92+Math.random()*.16;});});
 Object.keys(G.imp).forEach(k=>{G.imp[k]*=.5;if(Math.abs(G.imp[k])<.5)delete G.imp[k];});
}
function mkOffer(){
 const w=[['lieferung',4],['beschaffung',3],['kurier',3]];
 let r=Math.random()*10,t='lieferung';
 for(let i=0;i<w.length;i++){if(r<w[i][1]){t=w[i][0];break;}r-=w[i][1];}
 const sc=1+G.resp*.04;
 const o={id:G.nid++,t:t,got:false,cl:rnd(0,99),dl:G.day+rnd(3,6)};
 if(t==='lieferung'){
  o.item=chance(.8)?'bier':'gras';
  o.q=Math.round((o.item==='bier'?rnd(5,14):rnd(3,8))*sc);
  o.to=pick(MARKETS);
  o.rw=r5(o.q*GOODS[o.item].base*rf(1.3,1.7));
 }else if(t==='beschaffung'){
  o.item=pick(['hopfen','malz','samen']);
  o.q=Math.round(rnd(6,16)*sc);
  o.to=pick(Object.keys(DIST));
  o.rw=r5(o.q*GOODS[o.item].base*rf(2.1,2.9));
 }else{
  o.from=pick(Object.keys(DIST));
  do{o.to=pick(Object.keys(DIST));}while(o.to===o.from);
  o.rw=r10(rnd(350,650)+mdist(o.from,o.to)*8+G.resp*20);
  o.dl=G.day+rnd(2,4);
 }
 return o;
}
function offerTarget(){return Math.min(7,4+Math.floor(G.resp/6));}
function fillOffers(){while(G.offers.length<offerTarget())G.offers.push(mkOffer());}
function mTitle(o){return NAMES[o.t][o.cl%NAMES[o.t].length];}
function mLine(o){
 if(o.t==='kurier')return 'Rezept-Paket abholen: '+DIST[o.from].n+'. Übergabe: '+DIST[o.to].n+'.';
 if(o.t==='lieferung')return 'Liefere '+o.q+' '+GOODS[o.item].n+' zu: '+DIST[o.to].n+'.';
 return 'Besorge '+o.q+' '+GOODS[o.item].n+' für: '+DIST[o.to].n+'.';
}
function canPickup(m){return m.t==='kurier'&&!m.got&&G.loc===m.from;}
function canDeliver(m){if(G.loc!==m.to)return false;if(m.t==='kurier')return m.got;return G.inv[m.item]>=m.q;}
function whyNot(m){
 if(m.t==='kurier')return m.got?'':'Du hast das Paket noch nicht abgeholt.';
 return 'Dir fehlen noch '+Math.max(0,m.q-G.inv[m.item])+' '+GOODS[m.item].n+'.';
}
function accept(id){
 if(G.active.length>=4)return{ok:false,msg:'Du kannst nur 4 Aufträge gleichzeitig führen.'};
 const i=G.offers.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:'Angebot nicht mehr da.'};
 const o=G.offers.splice(i,1)[0];G.active.push(o);
 return{ok:true,msg:'Auftrag angenommen: '+mTitle(o)+'.'};
}
function failM(m){if(m.t==='kurier'&&m.got)G.inv.koffer=Math.max(0,G.inv.koffer-1);}
function abandon(id){
 const i=G.active.findIndex(o=>o.id===id);if(i<0)return{ok:false,msg:'Auftrag nicht gefunden.'};
 const m=G.active.splice(i,1)[0];failM(m);G.resp=Math.max(0,G.resp-1);
 return{ok:true,msg:'Auftrag abgebrochen (-1 Respekt).'};
}
function pickup(id){
 const m=G.active.find(o=>o.id===id);if(!m||!canPickup(m))return{ok:false,msg:'Hier gibt es nichts abzuholen.'};
 if(used()>=cap())return{ok:false,msg:'Du kannst nichts mehr tragen.'};
 m.got=true;G.inv.koffer++;heat(6);
 return{ok:true,msg:'Du übernimmst das Rezept-Paket. Alles legal, alles plombiert.'};
}
function deliver(id){
 const m=G.active.find(o=>o.id===id);if(!m||!canDeliver(m))return{ok:false,msg:m?whyNot(m):'Auftrag nicht gefunden.'};
 if(m.t==='kurier')G.inv.koffer--;else G.inv[m.item]-=m.q;
 if(m.item==='gras')heat(m.q*.4);
 G.active.splice(G.active.indexOf(m),1);
 G.cash+=m.rw;G.stats.earned+=m.rw;G.stats.done++;
 const rp=m.t==='kurier'?2:1;G.resp+=rp;
 return{ok:true,msg:'Auftrag erledigt: +'+eur(m.rw)+' und +'+rp+' Respekt.'};
}
function buy(g,q){
 const d=G.loc;if(!DIST[d]||!DIST[d].mod)return{ok:false,msg:'Hier gibt es keinen Markt.'};
 const p=price(g,d),room=cap()-used(),aff=Math.floor(G.cash/p);
 const n=q==='max'?Math.min(room,aff):Math.min(+q,room,aff);
 if(n<=0)return{ok:false,msg:aff<1?'Nicht genug Geld.':'Du kannst nicht mehr tragen.'};
 G.cash-=n*p;G.inv[g]+=n;G.imp[d+g]=(G.imp[d+g]||0)-n;
 if(g==='gras')heat(n*.3);
 return{ok:true,msg:n+' '+GOODS[g].n+' gekauft für '+eur(n*p)+'.'};
}
function sell(g,q){
 const d=G.loc;if(!DIST[d]||!DIST[d].mod)return{ok:false,msg:'Hier gibt es keinen Markt.'};
 const have=G.inv[g],n=q==='all'?have:Math.min(+q,have);
 if(n<=0)return{ok:false,msg:'Davon hast du nichts dabei.'};
 const p=sellP(g,d);G.cash+=n*p;G.inv[g]-=n;G.imp[d+g]=(G.imp[d+g]||0)+n;
 if(g==='gras')heat(n*.6);else if(g==='bier')heat(n*.05);
 return{ok:true,msg:n+' '+GOODS[g].n+' verkauft für '+eur(n*p)+'.',witness:false};
}
function startBrew(q){
 const p=G.prod.brau;if(p.n>0)return{ok:false,msg:'Der Sud läuft noch.'};
 const m=Math.min(BRAU_CAP[G.up.brau],G.inv.hopfen,G.inv.malz);
 const n=q==='max'?m:Math.min(+q,m);
 if(n<1)return{ok:false,msg:'Du brauchst Hopfen und Malz dabei.'};
 G.inv.hopfen-=n;G.inv.malz-=n;p.n=n;p.left=2;
 return{ok:true,msg:n+' Ansätze angesetzt. Fertig in 2 Tagen.'};
}
function startGrow(q){
 const p=G.prod.haus;if(p.n>0)return{ok:false,msg:'Die Beete sind noch belegt.'};
 const m=Math.min(HAUS_CAP[G.up.haus],G.inv.samen);
 const n=q==='max'?m:Math.min(+q,m);
 if(n<1)return{ok:false,msg:'Du brauchst Hanfsamen dabei.'};
 G.inv.samen-=n;p.n=n;p.left=3;
 return{ok:true,msg:n+' Ansätze ausgesät. Ernte in 3 Tagen.'};
}
function collect(){
 const got=[];
 ['bier','gras'].forEach(g=>{const t=Math.min(G.prod.out[g],cap()-used());if(t>0){G.prod.out[g]-=t;G.inv[g]+=t;got.push(t+' '+GOODS[g].n);}});
 if(!got.length)return{ok:false,msg:G.prod.out.bier+G.prod.out.gras>0?'Du kannst nicht mehr tragen.':'Nichts abzuholen.'};
 return{ok:true,msg:'Eingepackt: '+got.join(' und ')+'.'};
}
function buyUp(k){
 const u=UPS[k],l=G.up[k];
 if(l>=u.cost.length)return{ok:false,msg:'Schon auf Höchststufe.'};
 if(G.cash<u.cost[l])return{ok:false,msg:'Dafür fehlt dir das Geld.'};
 G.cash-=u.cost[l];G.up[k]++;
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
function cargoVal(){return TRADE.reduce((s,g)=>s+G.inv[g]*GOODS[g].base,0)+G.inv.koffer*300;}
function illegal(){return 0;}
function loseGoods(frac){let n=0;TRADE.forEach(g=>{const l=Math.ceil(G.inv[g]*frac);G.inv[g]-=l;n+=l;});return n;}
function newDay(slept){
 const L=[];
 G.day++;
 if(G.debt>0){const a=Math.round(G.debt*.02);G.debt+=a;L.push('Chefin Willi rechnet '+eur(a)+' Zinsen auf den Vorschuss.');}
 [['brau','bier',2,'Das Bier ist fertig gebraut'],['haus','gras',3,'Die Ernte ist reif']].forEach(x=>{
  const p=G.prod[x[0]];
  if(p.n>0){p.left--;if(p.left<=0){const a=p.n*x[2];G.prod.out[x[1]]+=a;L.push(x[3]+': '+a+' '+GOODS[x[1]].n+' warten im Apotheken-Lager.');p.n=0;p.left=0;}}
 });
 heat(slept?-8:-3);
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
 G.offers=G.offers.filter(o=>o.dl>=G.day);
 fillOffers();
 try{gangHeist(L);}catch(e){}
 return L;
}
function worth(){
 let w=G.cash-G.debt;
 TRADE.forEach(g=>{w+=(G.inv[g]+(G.prod.out[g]||0))*GOODS[g].base*.8;});
 return Math.round(w);
}
function rank(w){
 if(w<3000)return'Praktikant';
 if(w<8000)return'Pharmazeut';
 if(w<16000)return'Filialleiter';
 if(w<30000)return'Chef-Apotheker';
 return'Apotheken-Legende';
}
function clock(){const h=G.t/DAY_S*24,hh=Math.floor(h),mm=Math.floor((h-hh)*60);return(hh<10?'0':'')+hh+':'+(mm<10?'0':'')+mm;}
function hour(){return G.t/DAY_S*24;}
function newGame(){
 G={day:1,t:8/24*DAY_S,cash:900,debt:2500,heat:5,resp:0,loc:'',
  inv:{hopfen:0,malz:0,samen:0,bier:0,gras:0,koffer:0},
  up:{brau:0,haus:0,trunk:0,tuning:0,leib:0,anwalt:0},
  prod:{brau:{n:0,left:0},haus:{n:0,left:0},out:{bier:0,gras:0}},
  mkt:{hopfen:1,malz:1,samen:1,bier:1,gras:1},noise:{},imp:{},events:[],offers:[],active:[],nid:1,won:false,mood:62,drunk:0,high:0,stock:{bier:3,joint:2,gluehwein:0},ammo:{dose:0,stein:0,schnee:0},sel:'',ret:null,pistol:false,tank:0,wet:0,hero:0,heroE:0,fang:0,zahn:0,teaT:0,
  stats:{done:0,earned:0,arrests:0,fights:0}};
 rollMarket();fillOffers();
 resetEntities();
 gangHeist([],true);
}

const SK='hh_welt_save_v1';
function saveAll(){try{localStorage.setItem(SK,JSON.stringify({G:G,P:{x:(ZONE&&G.ret?G.ret:P).x,y:(ZONE&&G.ret?G.ret:P).y},V:{x:V.x,y:V.y,a:V.a}}));}catch(e){}}
function hasSave(){try{return !!localStorage.getItem(SK);}catch(e){return false;}}
function fixG(){
 if(G.mood===undefined)G.mood=62;
 if(G.drunk===undefined)G.drunk=0;
 if(G.hero===undefined)G.hero=0;
 if(G.heroE===undefined)G.heroE=0;
 if(G.fang===undefined)G.fang=0;
 if(G.zahn===undefined)G.zahn=0;
 G.teaT=0;
 if(G.high===undefined)G.high=0;
 if(!G.stock)G.stock={bier:3,joint:2};
 if(!G.ammo)G.ammo={dose:0,stein:0,schnee:0};
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
  G=s.G;G.loc='';fixG();toCity();resetEntities();
  P.x=s.P.x;P.y=s.P.y;V.x=s.V.x;V.y=s.V.y;V.a=s.V.a;
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
 traffic=[];for(let i=0;i<12;i++)traffic.push(mkCar(false));for(let i=0;i<2;i++)traffic.push(mkCar(true));
 peds=[];for(let i=0;i<26;i++){const p=randTile([SW,GR],0,0);peds.push(mkPed(p.x,p.y));}
 addTeens();
 cops=[];for(let i=0;i<5;i++){const p=randTile([SW],0,0);cops.push({x:p.x,y:p.y,a:rf(0,6.28),t:rf(.5,3),sp:30,alert:0,hx:false,hy:false,hx0:p.x,hy0:p.y});}
 thugs=[];ZONES.forEach(z=>{for(let i=0;i<2;i++)thugs.push({x:z.x+rf(-20,20),y:z.y+rf(-20,20),a:rf(0,6.28),t:rf(.5,2),hx0:z.x,hy0:z.y,st:'idle',cool:0,ko:0,hp:2,stun:0,hx:false,hy:false});});
 chasers=[];wanted=0;escapeT=0;bustT=0;
 kids=[];NOGO.forEach(n=>{const c=n.n==='Kita-Spielplatz'?5:3;for(let i=0;i<c;i++){let x=n.x0+60,y=n.y0+60;for(let k=0;k<30;k++){x=rf(n.x0+30,n.x1-30);y=rf(n.y0+30,n.y1-30);if(!hit(x,y,6))break;}kids.push({x:x,y:y,a:rf(0,6.28),t:rf(.5,2),col:pick(['#ff6b9d','#ffd23f','#4dd0e1','#9ccc65','#ff8a65']),walk:0,z:n});}});
 PICKS=[];for(let i=0;i<34;i++)spawnPick(true);FX=[];PR=[];RACE=null;P.sit=null;P.dance=0;P.ride=null;P.build=null;CAS=[];mkCityRides();
 P.x=GATE.x;P.y=GATE.y;P.vx=0;P.vy=0;P.inCar=false;P.ride=null;P.build=null;P.stun=0;
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
 G.stats.arrests++;
 const lost=G.inv.gras+G.inv.koffer;
 const frac=G.up.anwalt>0?(G.up.anwalt>1?.15:.22):.35,loss=Math.round(G.cash*frac);
 G.cash-=loss;G.inv.gras=0;
 for(let i=G.active.length-1;i>=0;i--){const m=G.active[i];if(m.t==='kurier'&&m.got){G.active.splice(i,1);G.resp=Math.max(0,G.resp-1);}}
 G.inv.koffer=0;G.heat=Math.min(G.heat,35);
 wanted=0;chasers=[];escapeT=0;bustT=0;
 P.x=GATE.x;P.y=GATE.y;P.vx=0;P.vy=0;P.inCar=false;P.ride=null;P.build=null;V.x=VAN0.x;V.y=VAN0.y;V.a=0;V.sp=0;
 const L=sleepTo(6,false);
 busted(['Beschlagnahmt: '+lost+' illegale Einheiten.','Geldstrafe: '+eur(loss)+'.','Du verbringst die Nacht in der Zelle.'].concat(L));
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
 if(chance(G.up.leib*.2)){msgCb('Dein Leibwächter hält die Gangster auf.');u.st='cool';u.cool=20;return;}
 const c=Math.min(G.cash,Math.round(G.cash*.15+40)),l=loseGoods(.25);
 G.cash-=c;u.st='cool';u.cool=25;P.stun=.8;
 msgCb('Überfall! Die Park-Gang nimmt dir '+eur(c)+(l?' und '+l+' Ware':'')+' ab.');
}
function pushOut(e,r){
 traffic.forEach(c=>{
  const dx=e.x-c.x,dy=e.y-c.y,d=Math.hypot(dx,dy),m=r+12;
  if(d<m&&d>0){e.x+=dx/d*(m-d);e.y+=dy/d*(m-d);}
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
  if(pedExt(p,dt))return;
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
 const ill=illegal()>0&&wanted===0;
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
   if(d<170&&(val>=150||G.cash>600)&&wanted===0&&!inYard(px,py)){u.st='chase';u.chaseT=0;if(Math.hypot(P.x-u.x,P.y-u.y)<200&&!P.inCar)msgCb('Die Park-Gang hat dich entdeckt!');}
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
function mkPed(x,y){return{x:x,y:y,a:rf(0,6.28),t:rf(.5,3),col:pick(PCOL),sp:rf(25,45),walk:0,hx:false,hy:false,like:chance(.3),st:'walk',stT:0,nm:pick(PN),jb:pick(PJ)};}
const AMN={dose:'Dose',stein:'Stein',schnee:'Schneeball',wasser:'Wasserpistole'};
const HITL={dose:['DONG!','Meine Dose!','Das war Pfand!'],stein:['AUA!','Mein Zeh!','Ein Stein!'],schnee:['PFFF!','Kalt!','Schneeballschlacht!']};
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
 if(WXC.type==='rain'&&flash<=0&&chance(dt*.03)){flash=.7;sfx('thunder');addFx(P.x+rf(-100,100),P.y-30,'BUMM!','#fff3a0',1.2);}
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
 if(ng&&!noGoIn){toast(ng.n+': Kein Alkohol, kein Rauch, keine Prügelei. Hier spielen Kinder!');}
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
function curAmmo(){const o=['schnee','stein','dose'];if(G.sel==='wasser'&&G.pistol)return 'wasser';if(G.sel&&G.sel!=='wasser'&&G.ammo[G.sel]>0)return G.sel;for(let i=0;i<3;i++)if(G.ammo[o[i]]>0)return o[i];return G.pistol?'wasser':'';}
function copNear(x,y,r){
 if(ZONE)return false;
 return cops.some(c=>Math.hypot(c.x-x,c.y-y)<r)||traffic.some(c=>c.cop&&Math.hypot(c.x-x,c.y-y)<r);
}
function throwIt(){
 const t=curAmmo();if(!t)return false;
 if(t==='wasser')return shootWater();
 if(inNoGo(P.x,P.y)){toast('Auf dem Spielplatz wird nichts geworfen!');return true;}
 let a=P.a;const best=aimBest(240,false);
 if(best)a=Math.atan2(best.y-P.y,best.x-P.x);
 G.ammo[t]--;P.a=a;
 PR.push({x:P.x,y:P.y,vx:Math.cos(a)*340,vy:Math.sin(a)*340,t:0,type:t});
 sfx('throw');
 return true;
}
function dropAmmo(b){
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
  else if(isSolid(tx,ty)){dropAmmo(b);done=true;}
  else{
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
   if(Math.hypot(k.x-P.x,k.y-P.y)<15&&G.ammo[k.t]<9){
    G.ammo[k.t]++;PICKS.splice(i,1);addFx(P.x,P.y-16,'+'+AMN[k.t],'#cfe9ff');
    if(!tipShown){tipShown=true;toast('Aufgehoben! OK wirft es auf Passanten. Im Rucksack wählst du, was.');}
   }
  }
 }
 pickT-=dt;
 if(pickT<=0){pickT=9;if(PICKS.length<(ZONE?ZONE.pickCap:34))spawnPick(false);}
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
 G.stock.bier--;G.drunk+=1;sfx('glug');
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
 const m=G.mood,w={strand:m>=65?6:1.2,vulkan:m<=35?6:1,berge:2.2,hoehle:2.2,amsterdam:1.6,maerchen:1.8,schlaraff:1.2,bayern:1.4,portugal:1.4,wuppertal:1.4};
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
 if(mk.home&&ZONE&&(ZONE.name==='bayern'||ZONE.name==='portugal'||ZONE.name==='wuppertal')){UI.euroFrom='';show('euro');return;}
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
 let z=WORLDS[name];
 if(!z){z=genZone(name);renderZone(z);WORLDS[name]=z;}
 if(!ZONE)CITYENT={traffic:traffic,peds:peds,cops:cops,thugs:thugs,chasers:chasers,kids:kids,picks:PICKS,rides:RIDES};
 if(RACE){RACE.p.st='walk';RACE=null;}
 ZONE=z;useWorld(z);skEnter(z);
 traffic=[];cops=[];thugs=[];chasers=[];kids=[];peds=zonePeds(z);PICKS=[];RIDES=z.rides;CAS=[];P.ride=null;P.build=null;P.fish=null;P.fight=null;G.wet=0;
 for(let i=0;i<10;i++)spawnPick(true);
 PR=[];FX=[];wanted=0;escapeT=0;bustT=0;
 P.x=z.spawn.x;P.y=z.spawn.y;P.vx=P.vy=0;P.inCar=false;P.sit=null;
 if(z.spawnRide){const R=z.rides[0];R.x=z.spawn.x;R.y=z.spawn.y;R.a=0;R.sp=0;P.ride=R;}
 sfx('arrive');
 cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);
 UI.hudS=null;UI.trkS=null;
 renderMini();
 toast(z.title+': '+z.hint);
}
function leaveZone(silent){
 if(!ZONE)return;
 if(RACE){RACE.p.st='walk';RACE=null;}
 ZONE=null;useWorld(CITY);
 traffic=CITYENT.traffic;peds=CITYENT.peds;cops=CITYENT.cops;thugs=CITYENT.thugs;chasers=CITYENT.chasers;kids=CITYENT.kids;PICKS=CITYENT.picks;RIDES=CITYENT.rides;CAS=[];P.ride=null;P.build=null;
 PR=[];FX=[];wanted=0;chasers=[];escapeT=0;bustT=0;
 const r=G.ret||{x:GATE.x,y:GATE.y},q=freeSpot(r.x,r.y);
 P.x=q.x;P.y=q.y;P.vx=P.vy=0;P.inCar=false;P.sit=null;
 cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);
 UI.hudS=null;UI.trkS=null;
 renderMini();
 if(!silent)toast('Zurück in Rheinhafen. Alles beim Alten, nur du bist besser drauf.');
}
function toCity(){if(ZONE)leaveZone(true);}
function zonePeds(z){
 const out=[];
 const rt=types=>{for(let k=0;k<200;k++){const x=rnd(2,ZW-3),y=rnd(2,ZH-3);if(types.indexOf(z.T[y*ZW+x])>=0)return{x:x*TS+16,y:y*TS+16};}return null;};
 const add=(n,types,fn)=>{for(let i=0;i<n;i++){const p=rt(types);if(!p)continue;const q=mkPed(p.x,p.y);if(fn)fn(q);out.push(q);}};
 if(z.name==='strand'){add(4,[SA,SH],q=>{q.gun=chance(.55);q.gc=pick(GUNC);});strandKids(z,out);add(5,[SA],q=>{q.st='lie';q.stT=1e9;q.tw=pick(['#e5604d','#2e86c1','#f1c40f','#27ae60','#8e44ad']);});}
 else if(z.name==='vulkan'){add(4,[AS]);}
 else if(z.name==='berge'){add(4,[SN,IC]);[[14,12],[28,11],[40,16]].forEach(s=>{const q=mkPed(s[0]*TS+16,s[1]*TS+16);q.snow=true;q.hp=0;out.push(q);});}
 else if(z.name==='hoehle')add(3,[CF]);else if(z.name==='wal'){let ji=0;add(3,[CF],q=>{if(ji++===0){q.nm='Jonas';q.jb='Wohnt hier. Seit Kurzem. Oder seit der Bibel.';}});}else if(z.name==='maerchen')add(3,[GR,SW]);else if(z.name==='schlaraff')add(4,[GR]);else if(z.name==='bayern')add(7,[GR]);else if(z.name==='portugal')add(8,[SW,SA]);else if(z.name==='wuppertal')add(8,[SW]);else if(z.name==='rhein')add(5,[GR]);else if(z.name==='amsterdam')add(10,[SW],q=>{if(chance(.5))q.col='#ff7a1a';});
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
 const sitting=!!P.sit||!!P.build||!!P.fish||!!P.fight;
 const ax=sitting?0:(keys.right?1:0)-(keys.left?1:0),ay=sitting?0:(keys.down?1:0)-(keys.up?1:0);
 P.stun=Math.max(0,P.stun-dt);
 if(P.ride){rideDrive(dt,ax,ay);}
 else if(P.inCar){drive(dt,ax,ay);P.x=V.x;P.y=V.y;}
 else if(!sitting){
  const load=used()/cap();
  const wet=tget(Math.floor(P.x/TS),Math.floor(P.y/TS))===SH;
  const sp=FOOT*(1-.35*load)*(P.stun>0?.3:1)*(wet?.6:1)*(isDeep(P.x,P.y)?.55:1)*(G.high>0?.88:1)*(P.heroT>0?1.3:1);
  let tx=ax,ty=ay;const l=Math.hypot(tx,ty);
  if(l>0){
   tx=tx/l*sp;ty=ty/l*sp;P.a=Math.atan2(ty,tx);
   if(G.drunk>=2){const k=(G.drunk-1)*13;tx+=Math.sin(timeNow*2.3)*k;ty+=Math.cos(timeNow*1.9)*k;}
  }
  P.vx+=(tx-P.vx)*Math.min(1,dt*14);P.vy+=(ty-P.vy)*Math.min(1,dt*14);
  moveE(P,P.vx*dt,P.vy*dt,7);pushOut(P,7);
  P.walk+=Math.hypot(P.vx,P.vy)*dt*.12;
  if(wet&&l>0){splashT-=dt;if(splashT<=0){splashT=.25;addFx(P.x,P.y+4,'~','#9fd8ff',.6,-8);}}
 }
 if((wanted>0||thugs.some(u=>u.st==='chase'))&&flowAge>.3){computeFlow();flowAge=0;}
 trafficUpdate(dt);pedsUpdate(dt);copsUpdate(dt);chasersUpdate(dt);thugsUpdate(dt);
 kidsUpdate(dt);projUpdate(dt);picksUpdate(dt);raceUpdate(dt);moodTick(dt);wxUpdate(dt);fxUpdate(dt);zoneUpdate(dt);extUpdate(dt);
 MKS.forEach(m=>{if(m.cd>0)m.cd-=dt;});
 saveT+=dt;if(saveT>45&&wanted===0){saveT=0;saveAll();}
 const RR=P.ride;const tx=P.x+(P.inCar?Math.cos(V.a)*V.sp*.3:RR?Math.cos(RR.a)*RR.sp*.28:0)-VW/2,ty=P.y+(P.inCar?Math.sin(V.a)*V.sp*.3:RR?Math.sin(RR.a)*RR.sp*.28:0)-VH/2;
 cam.x+=(tx-cam.x)*Math.min(1,dt*6);cam.y+=(ty-cam.y)*Math.min(1,dt*6);
 cam.x=clamp(cam.x,0,MW*TS-VW);cam.y=clamp(cam.y,0,MH*TS-VH);
}
function checkWin(){if(G&&!G.won&&worth()>=30000){G.won=true;msgCb('__win');}}
function nearMarker(){
 let b=null,bd=38;
 MKS.forEach(m=>{const d=Math.hypot(m.x-P.x,m.y-P.y);if(d<bd){bd=d;b=m;}});
 return b;
}
function nearVan(){return !P.inCar&&Math.hypot(V.x-P.x,V.y-P.y)<56;}
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
 const mc=MM.getContext('2d'),S=4;
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){
  const t=T[y*MW+x];
  mc.fillStyle=t===RD?'#555a62':t===BL?'#8a6a5a':t===WT?'#255d86':t===TR?'#2b5a2b':t===GR?'#3f6b3a':t===FD?'#7a9a3a':t===DK?'#8a6a44':t===CR?'#7f6f4f':t===BK?'#7a5a3a':t===PG?'#c06a3a':t===SD?'#d9c27a':'#9d9d96';
  mc.fillRect(x*S,y*S,S,S);
 }
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
  if(b.k==='glass'){
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
 strand:{title:'Strand',hint:'Sonne, Sand und Sorglosigkeit. Sandburgen, Wasserpistolen, Boote!',swim:true,wx:'sun',gain:.4,base:SA,walk:[SA],picks:['stein','dose','stein'],cap:12},
 vulkan:{title:'Vulkan',hint:'Heiß, laut und herrlich ungemütlich. Hier darfst du schreien.',wx:'ash',gain:0,base:AS,walk:[AS],picks:['stein','stein','stein'],cap:18},
 berge:{title:'Berge',hint:'Schnee bis zum Horizont. Glühwein, Schneemänner, Rodeln!',wx:'snow',gain:.3,base:SN,walk:[SN],picks:['stein','dose'],cap:8},
 hoehle:{title:'Höhle',hint:'Dunkel, feucht und leuchtende Pilze. Irgendwo tropft es.',swim:true,wx:'none',gain:.15,base:CF,walk:[CF],picks:['stein','dose'],cap:10},
 rhein:{title:'Rhein',hint:'Volle Fahrt! Immer flussabwärts, bis Amsterdam. Hoch fährt, Links und Rechts lenkt.',wx:'sun',gain:.35,base:GR,walk:[GR],picks:['stein','dose'],cap:8,swim:true},
 amsterdam:{title:'Amsterdam',hint:'Grachten, Fahrräder, Tulpen. Willkommen in Holland!',wx:'sun',gain:.3,base:SW,walk:[SW],picks:['stein','dose'],cap:10,swim:true},
 wal:{title:'Wal-Bauch',hint:'Warm, wabbelig und überraschend gemütlich. Sofa, Tee, Joint ...',wx:'none',gain:.6,base:CF,walk:[CF],picks:['dose'],cap:3,swim:true},
 maerchen:{title:'Märchenwald',hint:'Lebkuchenhaus, Frau Holle, sieben Zwerge ... Hier ist alles ein bisschen verzaubert.',wx:'none',gain:.5,base:GR,walk:[GR],picks:['dose','stein'],cap:6},
 schlaraff:{title:'Schlaraffenland',hint:'Pudding-Berge, ein Milchsee und Brathähnchen im Anflug. Mund auf!',wx:'none',gain:.6,base:GR,walk:[GR],picks:['dose'],cap:3},
 bayern:{title:'Bayern',hint:'Berge, Biergarten, Blasmusik und ein Schloss wie aus dem Bilderbuch. Servus!',swim:true,wx:'sun',gain:.5,base:GR,walk:[GR],picks:['stein','dose'],cap:8},
 portugal:{title:'Portugal',hint:'Gelbe Tram, Fado und Sardinen. Das Meer rauscht. Olá!',swim:true,wx:'sun',gain:.5,base:SW,walk:[SW,SA],picks:['stein','dose'],cap:8},
 wuppertal:{title:'Wuppertal',hint:'Die Schwebebahn schwebt, die Wupper plätschert und im Brauhaus zischt das Bier. Glück auf!',swim:true,wx:'none',gain:.5,base:SW,walk:[SW],picks:['stein','dose'],cap:8}
};
const ZPO={
 strand:{home:['strandkorb','Strandkorb','Strandkorb zuklappen','Du kuschelst dich in den Strandkorb und klappst ihn zu. Wenn du ihn öffnest: zu Hause.'],wild:['surfbrett','Surfbrett','Aufs Surfbrett steigen','Eine Riesenwelle! Du surfst direkt aus dem Bild.']},
 vulkan:{home:['notausgang','Notausgang','Notausgang nehmen','Du nimmst den grünen Notausgang. Er riecht nach Pizza.'],wild:['lavalampe','Lava-Lampe','In die Lava-Lampe springen','Du hüpfst in die Lava-Lampe. Glibber, glibber, plopp!']},
 berge:{home:['huette','Hütten-Tür','Hütten-Tür öffnen','Die Tür knarzt. Dahinter ist es überraschend städtisch.'],wild:['schlitten','Rodelschlitten','Losrodeln','Du rodelst los. Und rodelst. Und rodelst. Und rodelst ...']},
 hoehle:{home:['leiter','Leiter nach oben','Leiter hochklettern','Du kletterst Sprosse für Sprosse zurück in die Stadt.'],wild:['tropf','Tropfsteinloch','Ins Loch kriechen','Du zwängst dich durchs Loch. Schmatz!']},
 rhein:{home:['anleger','Anleger Düsseldorf','Zurück nach Düsseldorf','Du legst am Düsseldorfer Rheinufer an. Alles noch da.'],wild:['anleger','Anleger Amsterdam','Weiterfahren nach Amsterdam','Immer der Strömung nach. Moment, das sind schon Grachten!','amsterdam']},
 amsterdam:{home:['anleger','Boot nach Düsseldorf','Boot zurück nehmen','Du tuckerst den Rhein hinauf. Düsseldorf, hier bin ich wieder.'],wild:['tulpe','Riesen-Tulpe','In die Tulpe klettern','Du kletterst in die Riesen-Tulpe. Es riecht nach Frühling, dann nach Neuland.']},
 wal:{home:['blasloch','Blasloch','Durchs Blasloch hinaus','Der Wal niest kräftig. Du fliegst in hohem Bogen hinaus ins Meer!','strand'],wild:['tee','Leuchtender Tee','Den Leuchttee probieren','Ein seltsam leuchtender Tee. Du trinkst, und die Welt dreht sich weiter.']},
 maerchen:{home:['buch','Märchenbuch','Märchenbuch zuklappen','Ende gut, alles gut. Du klappst das Märchenbuch zu, und Rheinhafen ist wieder da.'],wild:['brunnen','Brunnen','In den Brunnen springen','Du springst in den Brunnen. Plumps! Du fällst und fällst, und unten ist es überraschend hell.']},
 schlaraff:{home:['loeffel','Riesenlöffel','Löffel zurück nehmen','Du setzt dich auf den Riesenlöffel und rutschst zurück in den Märchenwald.','maerchen'],wild:['kuchen','Zuckerkuchen','In den Kuchen beißen','Du beißt in den Kuchen. Die Füllung trägt dich fort.']},
 bayern:{home:['bahn','Bahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Auf der Anzeigetafel steht: Alle Ziele.'],wild:['kuckuck','Kuckucksuhr','Die Kuckucksuhr aufziehen','Der Kuckuck ruft dreizehn Mal. Dann wird alles anders.']},
 portugal:{home:['flug','Flughafen','Zum Flughafen gehen','Du gehst zum Flughafen. Die Möwen wünschen gute Reise.'],wild:['galo','Hahn von Barcelos','Den bunten Hahn streicheln','Der bunte Hahn kräht aus voller Brust. Das Kikeriki trägt dich fort.']},
 wuppertal:{home:['bahn','Hauptbahnhof','Zum Bahnhof gehen','Du gehst zum Bahnhof. Die Schwebebahn winkt von oben.'],wild:['waffel','Riesenwaffel','In die Waffel beißen','Du beißt in eine Bergische Waffel. Heiße Kirschen spritzen, und die Welt dreht sich weiter.']}
};
const ZWILD={strand:[42,23],vulkan:[43,25],berge:[42,8],hoehle:[39,21],rhein:[44,rheinY(44)+7],amsterdam:[43,16],wal:[40,15],maerchen:[38,23],schlaraff:[40,22],bayern:[44,22],portugal:[44,22],wuppertal:[44,25]};
const ZHOME={rhein:[3,rheinY(3)+7],amsterdam:[6,26],wal:[8,15],maerchen:[6,24],schlaraff:[6,24],bayern:[6,25],portugal:[12,24],wuppertal:[6,26]};
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
  const sc=['#3a4048','#444b54','#394450','#4a4640'];let hi=0;
  for(let x=3;x<=43;x+=4){zf(x,4,3,3,BL);z.BLD.push({x:x,y:4,w:3,h:3,c:sc[hi%4],n:'',k:'schiefer',hh:6});hi++;}
  for(let x=11;x<=35;x+=4){zf(x,20,3,3,BL);z.BLD.push({x:x,y:20,w:3,h:3,c:sc[hi%4],n:'',k:'schiefer',hh:6});hi++;}
  zf(16,8,7,4,BL);z.BLD.push({x:16,y:8,w:7,h:4,c:'#a8432f',n:'BRAUHAUS',k:'brau',hh:6});
  mk('brauhaus','buedchen',21,12,'Brauhaus','Brauhaus besuchen');
  {const m=mk('braum','sk',17,12,'Braumeister','Braumeister besuchen');m.sk='braum';m.col='#ffb347';}
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

 else if(t===GR&&(nm==='maerchen'||nm==='schlaraff'||nm==='bayern')){c.fillStyle=h<3?'#7cbf5c':h<6?'#74b755':'#82c563';c.fillRect(px,py,TS,TS);if(h===1){c.fillStyle='#fff';c.fillRect(px+7,py+9,3,3);c.fillStyle='#f4d03f';c.fillRect(px+8,py+10,1,1);}else if(h===3){c.fillStyle='#ff7fb0';c.fillRect(px+19,py+17,3,3);c.fillStyle='#fff3a0';c.fillRect(px+20,py+18,1,1);}else if(h===5){c.fillStyle='#b58cff';c.fillRect(px+12,py+22,3,3);}else if(h===2){c.fillStyle='rgba(255,255,255,.25)';c.fillRect(px+6,py+14,8,2);}}
 else if(t===GR){c.fillStyle=h<3?'#6fae56':h<6?'#68a64f':'#74b45c';c.fillRect(px,py,TS,TS);if(h===2){c.fillStyle='rgba(255,255,255,.35)';c.fillRect(px+8,py+10,2,2);c.fillStyle='#f4d03f';c.fillRect(px+20,py+18,2,2);}}
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
  const col=nm==='vulkan'?['#241d1c','#4a3a38']:nm==='berge'?['#7d8590','#a9b2bd']:nm==='bayern'?['#8b8478','#b5ad9c']:nm==='wal'?['#7a2a45','#a8456a']:['#14111b','#2e2840'];
  c.fillStyle=col[0];c.fillRect(px,py,TS,TS);
  if(g(x,y+1)!==RK){c.fillStyle=col[1];c.fillRect(px,py+TS-8,TS,8);}
  if(h<2){c.fillStyle='rgba(255,255,255,.07)';c.fillRect(px+6+h*6,py+6,10,8);}
  if((nm==='berge'||nm==='bayern')&&g(x,y-1)!==RK){c.fillStyle='#f4f8fb';c.fillRect(px,py,TS,8);}
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
   if(nm==='strand'||nm==='portugal'){
    c.strokeStyle='#7a5a32';c.lineWidth=4;c.beginPath();c.moveTo(px,py+8);c.lineTo(px+2,py-2);c.stroke();
    c.strokeStyle='#2f9a3f';c.lineWidth=3;
    for(let k=0;k<6;k++){const a=k/6*6.283;c.beginPath();c.moveTo(px+2,py-2);c.lineTo(px+2+Math.cos(a)*14,py-2+Math.sin(a)*10);c.stroke();}
    c.fillStyle='#6b4a1f';c.beginPath();c.arc(px+1,py-1,2.5,0,6.283);c.fill();c.lineWidth=1;
   }else if(nm==='maerchen'||nm==='schlaraff'){
    const hv=hash(x,y)%4,cc=(nm==='schlaraff'?[['#ff9ec7','#ffc2dc'],['#9ed8ff','#c4e8ff'],['#ffe08a','#fff0b8'],['#b9f0c0','#d8f8dc']]:[['#2f7a3f','#3f9a4f'],['#357f5a','#46a374'],['#4f8a2f','#6aae3f'],['#a8527a','#d4709f']])[hv];
    c.fillStyle='#5a3d22';c.fillRect(px-3,py+1,6,11);c.fillStyle='#2b1a0e';c.beginPath();c.ellipse(px,py+7,1.8,2.6,0,0,6.283);c.fill();
    c.fillStyle=cc[0];c.beginPath();c.arc(px,py-5,14,0,6.283);c.fill();c.fillStyle=cc[1];c.beginPath();c.arc(px-4,py-9,8,0,6.283);c.fill();c.beginPath();c.arc(px+6,py-4,6,0,6.283);c.fill();
    c.fillStyle='rgba(255,255,255,.45)';c.fillRect(px-6,py-10,2,2);c.fillRect(px+4,py-8,2,2);
   }else if(nm==='rhein'||nm==='amsterdam'||nm==='bayern'||nm==='wuppertal'){
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
 z.BLD.forEach(b=>drawBuilding(c,b));
 const mc=z.MM.getContext('2d'),S=6;
 mc.clearRect(0,0,304,192);
 for(let y=0;y<ZH;y++)for(let x=0;x<ZW;x++){
  const t=Tz[y*ZW+x];
  mc.fillStyle=t===GR?'#6fae56':t===SW?'#b9a58f':t===DK?'#a67c3a':t===FD?'#e0508a':t===SA?'#e2cd92':t===SH?'#5ec0d6':t===DP?'#2c80b4':t===AS?'#3a3231':t===LV?'#e8501a':t===SN?'#eef3f8':t===IC?'#b9dcf0':t===CF?'#352f40':t===RK?(nm==='berge'?'#7d8590':nm==='bayern'?'#8b8478':nm==='vulkan'?'#241d1c':'#14111b'):t===TR?'#2f7a3f':t===BL?'#8a6a5a':t===MU?'#3fe08f':t===CY?'#a58bff':'#c8b48a';
  if(nm==='hoehle'&&(t===SH||t===DP))mc.fillStyle='#25506f';
  if(nm==='wal'&&t===CF)mc.fillStyle='#d98aa0';
  if(nm==='wal'&&t===RK)mc.fillStyle='#7a2a45';
  if(nm==='wal'&&t===LC)mc.fillStyle='#8a5fb3';
  if((nm==='maerchen'||nm==='schlaraff')&&t===GR)mc.fillStyle='#7cbf5c';
  if(nm==='schlaraff'&&t===SH)mc.fillStyle='#f3efe6';
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
 else if(o==='waffel'){ctx.fillRect(x-12,y-10,26,24);ctx.fillStyle='#d8a050';ctx.fillRect(x-13,y-12,26,24);ctx.strokeStyle='#a8742e';for(let k=-8;k<=8;k+=8){ctx.beginPath();ctx.moveTo(x+k,y-12);ctx.lineTo(x+k,y+12);ctx.moveTo(x-13,y+k);ctx.lineTo(x+13,y+k);ctx.stroke();}ctx.fillStyle='#b01f2a';circle(x-4,y-3,3);circle(x+5,y+4,3);ctx.fillStyle='#fff';ctx.fillRect(x-1,y-12,5,3);}
 else if(o==='bahn'){ctx.fillRect(x-12,y-6,26,20);ctx.fillStyle='#2c3e50';ctx.fillRect(x-13,y-12,26,22);ctx.fillStyle='#f1c40f';ctx.fillRect(x-11,y-10,22,7);ctx.fillStyle='#ecf0f1';ctx.fillRect(x-9,y,18,4);ctx.fillStyle='#e5504d';ctx.fillRect(x-11,y+5,22,3);ctx.fillStyle='#888';circle(x-7,y+10,2.4);circle(x+7,y+10,2.4);ctx.fillStyle='#ffe08a';circle(x,y-6.5,1.6);}
 else if(o==='flug'){ctx.fillStyle='#f4f6f8';ctx.beginPath();ctx.ellipse(x,y,14,4.6,0,0,6.283);ctx.fill();ctx.beginPath();ctx.moveTo(x-2,y);ctx.lineTo(x-8,y-14);ctx.lineTo(x-3,y-14);ctx.lineTo(x+5,y);ctx.lineTo(x-3,y+14);ctx.lineTo(x-8,y+14);ctx.closePath();ctx.fill();ctx.fillStyle='#d8352f';ctx.beginPath();ctx.moveTo(x-12,y);ctx.lineTo(x-16,y-7);ctx.lineTo(x-12,y-7);ctx.closePath();ctx.fill();ctx.fillStyle='#2e86c1';circle(x+9,y-1,1.4);}
 else if(o==='kuckuck'){ctx.fillRect(x-10,y-6,24,22);ctx.fillStyle='#7a4a24';ctx.fillRect(x-11,y-8,22,22);ctx.fillStyle='#5a3416';ctx.beginPath();ctx.moveTo(x-13,y-8);ctx.lineTo(x,y-20);ctx.lineTo(x+13,y-8);ctx.closePath();ctx.fill();ctx.fillStyle='#f4ead0';circle(x,y+2,6.4);ctx.strokeStyle='#333';ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(x,y+2);ctx.lineTo(x,y-2);ctx.moveTo(x,y+2);ctx.lineTo(x+3,y+3);ctx.stroke();ctx.lineWidth=1;ctx.fillStyle='#ffd23f';ctx.fillRect(x-1,y+9,2,5);circle(x,y+16,2.4);}
 else if(o==='galo'){ctx.fillStyle='#d8352f';ctx.beginPath();ctx.ellipse(x,y+2,9,11,0,0,6.283);ctx.fill();ctx.fillStyle='#2f62b8';circle(x,y-9,5.4);ctx.fillStyle='#ffd23f';ctx.beginPath();ctx.moveTo(x+4,y-9);ctx.lineTo(x+11,y-7);ctx.lineTo(x+4,y-6);ctx.fill();ctx.fillStyle='#d8352f';ctx.fillRect(x-2,y-17,4,4);ctx.fillStyle='#fff';circle(x-1,y-10,1.2);ctx.fillStyle='#2e9d4f';ctx.fillRect(x-6,y+2,12,3);ctx.fillStyle='#ffd23f';ctx.fillRect(x-6,y+6,12,2);ctx.fillRect(x-4,y+12,2,4);ctx.fillRect(x+2,y+12,2,4);}
 else if(o==='brunnen'){ctx.beginPath();ctx.ellipse(x+2,y+4,15,12,0,0,6.283);ctx.fill();ctx.fillStyle='#9aa0a8';circle(x,y,14);ctx.fillStyle='#7d838c';circle(x,y,11);ctx.fillStyle='#2c80b4';circle(x,y,8.5);ctx.fillStyle='rgba(255,255,255,.4)';ctx.fillRect(x-5,y-3,6,2);ctx.strokeStyle='#5a3a1f';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x-12,y-14);ctx.lineTo(x-12,y+2);ctx.moveTo(x+12,y-14);ctx.lineTo(x+12,y+2);ctx.moveTo(x-13,y-14);ctx.lineTo(x+13,y-14);ctx.stroke();ctx.lineWidth=1;}
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
 ctx.fillText(m.kind==='hq'?'H':m.kind==='willi'?'W':m.kind==='buedchen'?'B':m.kind==='scream'?'!':m.kind==='sk'?'★':'€',m.x,m.y+1);
}
function drawPed(p){
 if(p.snow){drawSnowman(p);return;}
 if(p.st==='lie'){drawLie(p.x,p.y,p.tw||'#e5604d');return;}
 let y=p.y,a=p.a;
 if(p.st==='dance'){y+=Math.sin(timeNow*14)*2;a=timeNow*5;}
 else if(p.st==='dazed')a=timeNow*9;
 if(isDeep(p.x,p.y))drawSwim(p.x,y,a,p.col,p.walk);else drawPerson(p.x,y,a,p.col,'ped',p.walk,p.kid?.72:p.teen?.88:p.oma?.96:undefined);
 if(p.oma){ctx.fillStyle='#e2e2ea';circle(p.x,y-1,3.3);ctx.fillStyle='#b5503d';ctx.fillRect(p.x+Math.cos(a+1.57)*8-2,y+Math.sin(a+1.57)*8-2,5,4);}
 if(p.gun){ctx.save();ctx.translate(p.x,y);ctx.rotate(a);ctx.fillStyle=p.gc||'#3fd0ff';ctx.fillRect(5,-2,9,4);ctx.fillStyle='#222';ctx.fillRect(12,-1,3,2);ctx.restore();}
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
 const cx=clamp(Math.round(cam.x)+ox,0,MW*TS-VW),cy=clamp(Math.round(cam.y)+oy,0,MH*TS-VH);
 ctx.imageSmoothingEnabled=false;
 ctx.drawImage(WC,cx,cy,VW,VH,0,0,VW,VH);
 ctx.save();ctx.translate(-cx,-cy);
 const inView=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 const hl=new Set();
 if(G&&!ZONE){
  G.active.forEach(m=>{
   if(m.t==='kurier'&&!m.got)hl.add(m.from+'|p');
   else if(m.t==='kurier'||canHave(m))hl.add(m.to+'|d');
   else hl.add(m.to+'|w');
  });
 }
 MKS.forEach(m=>{if(inView(m.x,m.y,60))drawMarker(m,hl);});
 PICKS.forEach(k=>{if(inView(k.x,k.y,10))drawPick(k);});
 drawSeaLife(cx,cy);
 CAS.forEach(c=>{if(inView(c.x,c.y,40))drawCastle(c);});
 RIDES.forEach(R=>{if(inView(R.x,R.y,40))drawRide(R);});
 kids.forEach(k=>{if(inView(k.x,k.y,20))drawPerson(k.x,k.y,k.a,k.col,'ped',k.walk,.7);});
 peds.forEach(p=>{if(inView(p.x,p.y,24))drawPed(p);});
 drawSketch(cx,cy);
 cops.forEach(p=>{if(inView(p.x,p.y,20))drawPerson(p.x,p.y,p.a,'#2a4a8a','cop',p.walk);});
 thugs.forEach(u=>{if(inView(u.x,u.y,20)){if(u.ko>0){ctx.fillStyle='#7a1f1f';ctx.fillRect(u.x-8,u.y-4,16,8);ctx.fillStyle='#e8c39e';circle(u.x+9,u.y,3);}else{drawPerson(u.x,u.y,u.a,'#8a1f2a','thug',u.walk);if(u.loot)drawSack(u);}}});
 chasers.forEach(u=>{if(!inView(u.x,u.y,40))return;if(u.kind==='car')drawCar(u.x,u.y,u.a,'#f4f4f4','chase',timeNow);else drawPerson(u.x,u.y,u.a,'#2a4a8a','cop',timeNow*8);});
 traffic.forEach(c=>{if(inView(c.x,c.y,40))drawCar(c.x,c.y,c.a,c.col,c.cop?'cop':'civ',timeNow);});
 if(!ZONE)drawCar(V.x,V.y,V.a,'#e9e3d0','van',timeNow);
 if(!P.inCar&&!P.ride&&G){
  if(P.sit)drawSitter(P.x,P.y);
  else if(isDeep(P.x,P.y))drawSwim(P.x,P.y,P.a,'#d4a017',P.walk);
  else{const dn=P.dance>0;drawPerson(P.x,P.y+(dn?Math.sin(timeNow*14)*2:0),dn?timeNow*5:P.a,'#d4a017','me',P.walk);}
 }
 drawFishing();
 if(G&&P.build){const k=P.build.t/P.build.dur;ctx.strokeStyle='#ffd23f';ctx.lineWidth=3;ctx.beginPath();ctx.arc(P.x,P.y,16,-1.57,-1.57+6.283*k);ctx.stroke();ctx.lineWidth=1;}
 if(G&&G.wet>0&&!P.inCar){ctx.fillStyle='rgba(140,200,255,.85)';for(let i=0;i<4;i++){const q=timeNow*3+i*1.6;circle(P.x+Math.cos(q)*9,P.y+((timeNow*40+i*9)%16)-6,1.4);}}
 PR.forEach(b=>{
  const z=Math.sin(Math.PI*Math.min(1,b.t/.85))*12;
  ctx.fillStyle='rgba(0,0,0,.3)';circle(b.x,b.y+2,3);
  if(b.type==='dose'){ctx.fillStyle='#c9ced6';ctx.fillRect(b.x-2,b.y-z-4,5,8);}
  else if(b.type==='stein'){ctx.fillStyle='#8d8d92';circle(b.x,b.y-z,4);}
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
   const k=(m.t==='kurier'&&!m.got)?m.from:m.to;
   const mk=MKQ[k];const d=Math.hypot(mk.x-gx,mk.y-gy);if(d<td){td=d;tgt=mk;}
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
  drawWeather(wx);
  if(flash>0){ctx.fillStyle='rgba(255,255,255,'+flash*.6+')';ctx.fillRect(0,0,VW,VH);}
  if(hi>0){ctx.fillStyle='hsla('+Math.floor((timeNow*45)%360)+',85%,55%,'+(.12*hi)+')';ctx.fillRect(0,0,VW,VH);}
  if(G.drunk>=3){ctx.fillStyle='rgba(255,200,120,'+Math.min(.14,(G.drunk-2)*.04)+')';ctx.fillRect(0,0,VW,VH);}
 }
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
function mS(){return ZONE?6:4;}
function renderMini(){
 mctx.clearRect(0,0,mm.width,mm.height);
 mctx.drawImage(MM,0,0);
 const S=mS();
 MKS.forEach(m=>{mctx.fillStyle=m.kind==='hq'?'#6bcf63':m.kind==='willi'?'#e5604d':m.kind==='portal'?'#c06bff':m.kind==='buedchen'?'#46c2a0':m.kind==='scream'?'#ff5030':m.kind==='disco'?'#ff5fd0':'#f2b441';mctx.beginPath();mctx.arc(m.x/TS*S,m.y/TS*S,3,0,6.283);mctx.fill();});
 if(G){
  if(!ZONE)G.active.forEach(m=>{const k=(m.t==='kurier'&&!m.got)?m.from:m.to,mk=MKQ[k];mctx.strokeStyle='#fff';mctx.lineWidth=1.5;mctx.beginPath();mctx.arc(mk.x/TS*S,mk.y/TS*S,6,0,6.283);mctx.stroke();});
  thugs.forEach(u=>{if(u.loot&&u.ko<=0){mctx.fillStyle='#ff2d55';mctx.fillRect(u.x/TS*S-3,u.y/TS*S-3,6,6);mctx.strokeStyle='#fff';mctx.lineWidth=1;mctx.strokeRect(u.x/TS*S-3,u.y/TS*S-3,6,6);}});
  if(ZONE&&ZONE.whale){mctx.fillStyle='#8fc7ff';mctx.beginPath();mctx.ellipse(ZONE.whale.x/TS*S,ZONE.whale.y/TS*S,7,3,0,0,6.283);mctx.fill();}
  chasers.forEach(u=>{mctx.fillStyle=Math.floor(timeNow*4)%2?'#ff3030':'#3070ff';mctx.fillRect(u.x/TS*S-2,u.y/TS*S-2,4,4);});
  if(RACE){mctx.strokeStyle='#6bcf63';mctx.lineWidth=2;mctx.beginPath();mctx.arc(RACE.gx/TS*S,RACE.gy/TS*S,5,0,6.283);mctx.stroke();}
  mctx.fillStyle='#fff';mctx.beginPath();mctx.arc(P.x/TS*S,P.y/TS*S,3.5,0,6.283);mctx.fill();
  mctx.strokeStyle='#000';mctx.lineWidth=1;mctx.stroke();
 }
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
 bike:{mx:250,ac:260,br:420,dr:110,tn:3,r:8,g:0}
};
const RN={sled:'Rodelschlitten',chair:'Rollstuhl',boat:'Boot',bike:'Fahrrad'};
const RMSG={
 sled:['Rodeln! Der Hang gehört dir. Hoch beschleunigt, Links und Rechts lenkt.','Schlitten frei! Je steiler, desto lustiger.'],
 chair:['Der Rollstuhl hat Rückenwind. Und ein erstaunlich gutes Fahrwerk.','Vorsicht, Kurven! Der Rollstuhl hat ordentlich Dampf.'],
 boat:['Leinen los! Hoch fährt, Links und Rechts lenkt.','Ahoi! Das Boot schaukelt, die Laune auch.'],
 bike:['Aufs Rad! Klingeling.','Fahrrad geschnappt. Holland-Gefühl inklusive.']
};
let RIDES=[],CAS=[];
function mkRide(k,x,y,a){return{k:k,x:x,y:y,a:a||0,sp:0,snd:0,hx:false,hy:false,oma:null,stolen:false};}
function isWaterT(t){return t===SH||t===DP;}
function isDeep(x,y){return !!(ZONE&&ZONE.swim&&tget(Math.floor(x/TS),Math.floor(y/TS))===DP);}
function rideBlocked(R,x,y){
 const r=RP[R.k].r;
 if(R.k==='boat'){
  const x0=Math.floor((x-r)/TS),x1=Math.floor((x+r)/TS),y0=Math.floor((y-r)/TS),y1=Math.floor((y+r)/TS);
  for(let j=y0;j<=y1;j++)for(let i=x0;i<=x1;i++)if(!isWaterT(tget(i,j)))return true;
  return false;
 }
 return hit(x,y,r);
}
function rideMove(R,dx,dy){
 R.hx=false;R.hy=false;
 let nx=R.x+dx;if(rideBlocked(R,nx,R.y)){nx=R.x;R.hx=true;}R.x=nx;
 let ny=R.y+dy;if(rideBlocked(R,R.x,ny)){ny=R.y;R.hy=true;}R.y=ny;
 R.x=clamp(R.x,TS,MW*TS-TS);R.y=clamp(R.y,TS,MH*TS-TS);
}
function rideDrive(dt,ax,ay){
 const R=P.ride,p=RP[R.k];
 let mx=p.mx,dr=p.dr;
 const t=tget(Math.floor(R.x/TS),Math.floor(R.y/TS));
 if(R.k==='sled'){if(t===IC){mx*=1.35;dr*=.3;}else if(t!==SN){mx*=.5;dr*=4;}}
 if(R.k==='boat'&&ZONE&&ZONE.name==='rhein')mx=390;
 if(ay<0)R.sp=Math.min(mx,R.sp+p.ac*dt);
 else if(ay>0){if(R.sp>10)R.sp=Math.max(0,R.sp-p.br*dt);else R.sp=Math.max(-70,R.sp-p.ac*.5*dt);}
 else R.sp-=Math.sign(R.sp)*Math.min(Math.abs(R.sp),dr*dt);
 if(p.g)R.sp+=Math.sin(R.a)*p.g*dt;
 R.sp=clamp(R.sp,-80,mx*1.15);
 const steer=ax*p.tn*clamp(Math.abs(R.sp)/80,.25,1)*(R.sp<0?-1:1);
 R.a+=steer*dt;
 let dx=Math.cos(R.a)*R.sp*dt,dy=Math.sin(R.a)*R.sp*dt;
 if(R.k==='boat'&&ZONE&&ZONE.name==='rhein')dx+=26*dt;
 rideMove(R,dx,dy);
 if(R.hx||R.hy){
  if(Math.abs(R.sp)>120){
   addFx(R.x,R.y-16,pick(['Bonk!','Rums!','Hoppla!']),'#ffd23f');sfx('bonk');shake=.35;
   if(R.k==='sled'||R.k==='bike'||R.k==='chair')mood(1);
  }
  R.sp*=-.3;
 }
 P.x=R.x;P.y=R.y;
 R.snd-=dt;
 if(R.snd<=0&&Math.abs(R.sp)>90){R.snd=R.k==='boat'?.5:.38;sfx(R.k==='boat'?'wave':R.k==='sled'?'swish':'roll');}
 if(Math.abs(R.sp)>70&&chance(dt*18)){
  const bx=R.x-Math.cos(R.a)*14+rf(-4,4),by=R.y-Math.sin(R.a)*14+rf(-4,4);
  if(R.k==='boat')FX.push({x:bx,y:by,vx:rf(-6,6),vy:rf(-6,6),t:0,life:.6,dot:'rgba(255,255,255,.75)',r:rf(2,4)});
  else if(R.k==='sled'&&(t===SN||t===IC))FX.push({x:bx,y:by,vx:rf(-12,12),vy:rf(-14,-2),t:0,life:.5,dot:'#fff',r:rf(1.5,3)});
 }
 if(Math.abs(R.sp)>110){
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
 RIDES.forEach(R=>{const d=Math.hypot(R.x-P.x,R.y-P.y);if(d<bd){bd=d;b=R;}});
 return b;
}
function takeRide(R){
 if(R.oma&&!R.stolen)stealChair(R);
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
 ext6Update(dt);ext7Update(dt);ext8Update(dt);ext9Update(dt);ext10Update(dt);ext11Update(dt);
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
 }else{
  ctx.strokeStyle='#222';ctx.lineWidth=2.2;ctx.beginPath();ctx.arc(-9,0,5.5,0,6.283);ctx.stroke();ctx.beginPath();ctx.arc(9,0,5.5,0,6.283);ctx.stroke();
  ctx.strokeStyle='#e5604d';ctx.lineWidth=2.4;ctx.beginPath();ctx.moveTo(-9,0);ctx.lineTo(0,0);ctx.lineTo(9,0);ctx.moveTo(9,0);ctx.lineTo(8,-1);ctx.stroke();
  ctx.strokeStyle='#222';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(8,-6);ctx.lineTo(8,6);ctx.stroke();ctx.lineWidth=1;
  ctx.fillStyle='#222';ctx.fillRect(-3,-2,5,4);
 }
 ctx.restore();
 if(me){drawPerson(R.x,R.y,R.a,'#d4a017','me',0,.92);}
 else if(R.oma){
  drawPerson(R.x-Math.cos(R.a)*1,R.y-Math.sin(R.a)*1,R.a,'#9a7bbf','ped',0,.95);
  ctx.fillStyle='#e2e2ea';circle(R.x,R.y,3.5);ctx.fillStyle='#cfcfd8';circle(R.x-Math.cos(R.a)*2,R.y-Math.sin(R.a)*2,2.4);
  ctx.fillStyle='#b5503d';ctx.fillRect(R.x+Math.cos(R.a+1.57)*8-2,R.y+Math.sin(R.a+1.57)*8-2,5,4);
 }
}
function doGluehwein(){
 const w=noUse();if(w){toast(w);return false;}
 if(G.stock.gluehwein<1){toast('Kein Glühwein mehr. Die Hütten-Bar hat Nachschub.');return false;}
 G.stock.gluehwein--;G.drunk+=.7;
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
}
function rheinY(x){return Math.round(15+Math.sin(x*.21)*3+Math.sin(x*.07+1)*2);}


const TEENJ=['16 Jahre alt, schwört aber, er sei 18','Schülersprecher mit Skateboard','Hausaufgaben-Flüchtling','Hat noch ein Pausenbrot dabei','Sammelt Sticker und Meinungen'];
const TEENN=['Lukas','Mia','Emre','Lena','Jonas','Sophie'];
function heroRank(){const h=Math.floor(G.hero||0);return h<3?'Neuling mit Cape':h<8?'Nachbarschaftsheld':h<16?'Park-Retter':h<30?'Apotheken-Held':'Superheld';}
function addHeroE(n){G.heroE=Math.min(100,(G.heroE||0)+n);}
function minorNear(x,y,r){
 for(let i=0;i<kids.length;i++){if(Math.hypot(kids[i].x-x,kids[i].y-y)<r)return true;}
 for(let i=0;i<peds.length;i++){const p=peds[i];if((p.kid||p.teen)&&Math.hypot(p.x-x,p.y-y)<r)return true;}
 return false;
}
function addTeens(){
 for(let i=0;i<6;i++){
  const g=ZONES[i%ZONES.length];let x=g.x+rf(-70,70),y=g.y+rf(-70,70);
  for(let k=0;k<30&&hit(x,y,7);k++){x=g.x+rf(-90,90);y=g.y+rf(-90,90);}
  if(hit(x,y,7))continue;
  const q=mkPed(x,y);q.teen=true;q.nm=TEENN[i%TEENN.length];q.jb=pick(TEENJ);q.like=chance(.4);peds.push(q);
 }
}
function gangTH(){return ZONE&&CITYENT?CITYENT.thugs:thugs;}
function gangHeist(L,force){
 const TH=gangTH();
 TH.forEach(u=>{if(u.loot){u.loot.d++;if(u.loot.d>=2){L.push('Die Gang hat '+u.loot.q+' '+GOODS[u.loot.g].n+' im Park verkauft. Schade!');u.loot=null;}}});
 if(!force&&!chance(.75))return;
 const c=TH.filter(u=>!u.loot&&u.ko<=0);if(!c.length)return;
 const u=pick(c),o=G.prod.out;
 let g=o.gras>=o.bier?'gras':'bier',own=false,q;
 if(o[g]>0){q=Math.max(1,Math.ceil(o[g]*.5));o[g]-=q;own=true;}
 else{g=chance(.7)?'gras':'bier';q=rnd(4,8);}
 u.loot={g:g,q:q,own:own,d:0};u.deal=0;u.dealCool=0;
 const txt='Einbruch! Gangster haben '+q+' '+GOODS[g].n+(own?' aus dem Apotheken-Lager':' von einer Lieferung')+' geklaut und wollen es im Park verkaufen. Schnapp sie dir!';
 L.push(txt);
 setTimeout(()=>{try{msgCb(txt);}catch(e){}},force?400:3500);
}
function heroWin(u){
 let m='K.o.! Der Gangster sieht Sternchen.';
 G.hero=(G.hero||0)+.5;
 if(u.loot){
  const l=u.loot,r=l.q*20+(l.own?0:60);
  G.cash+=r;G.stats.earned+=r;if(l.own)G.prod.out[l.g]+=l.q;
  G.hero+=1+l.q/6;addHeroE(35);
  m='Beute zurück! '+l.q+' '+GOODS[l.g].n+(l.own?' liegen wieder im Apotheken-Lager.':' gehen zurück an die Kundschaft.')+' Belohnung '+eur(r)+'.';
  u.loot=null;sfx('win');
 }
 if(u.deal>0){G.hero+=1;G.cash+=50;m+=' Jugendschutz-Bonus: +50 €.';u.deal=0;u.dealT=null;u.dealCool=30;}
 else if(!/Belohnung/.test(m)){const c=rnd(15,40);G.cash+=c;m+=' Kopfgeld '+eur(c)+'.';}
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
  addFx(P.x,P.y-24,'SUPERSCHLAG!','#ffd23f',1.6);
  for(let i=0;i<14;i++)FX.push({x:P.x,y:P.y,vx:Math.cos(i/14*6.283)*150,vy:Math.sin(i/14*6.283)*150,g:0,t:0,life:.6,dot:'#ffd23f',r:3});
  thugs.forEach(u=>{if(u.ko>0)return;if(Math.hypot(u.x-P.x,u.y-P.y)<100){u.hp=0;u.ko=25;u.st='cool';G.stats.fights++;heroWin(u);}});
  return true;
 }
 best.hp--;best.stun=.5;G.stats.fights++;sfx('hit');
 const a=Math.atan2(best.y-P.y,best.x-P.x);moveE(best,Math.cos(a)*22,Math.sin(a)*22,8);P.a=a;
 addFx(best.x,best.y-16,pick(['BAMM!','PATSCH!','WUMMS!']),'#ffd23f',.8);
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
   msgCb('Der Jugendliche ist abgehauen. Verkauft wurde nichts, aber die Gang gibt nicht auf.');
  }
  return;
 }
 if(u.dealCool>0)return;
 const t=peds.find(p=>p.teen&&Math.hypot(p.x-u.x,p.y-u.y)<70);
 if(t){u.deal=.01;u.dealT=t;addFx(t.x,t.y-22,'!','#ff4040',2);addFx(u.x,u.y-22,'Psst ...','#ff8a65',2);msgCb('Ein Gangster bedrängt einen Jugendlichen im Park! Hilf ihm, Superheld!');}
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
 if(!c.nf&&G.fang===10){G.cash+=100;toast('Zehn Fische! Du bist jetzt der Angelkönig von Rheinhafen: +100 €.');}
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
 addFx(f.s.x+rf(-12,12),f.s.y-12,pick(['BAMM!','WUMMS!','PATSCH!','RUMMS!']),'#ffd23f',.8);
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
 G.teaT=40;
 mood(7+(G.high>0?5:0),G.high>0?'Tee & Joint!':'Ahh, Tee!');sfx('glug');
 toast(pick(['Kamillentee aus der Walwärme. Schmeckt nach Meer und Geborgenheit.','Du pustest in die Tasse. Der Wal brummt zufrieden vor sich hin.','Ein Schluck Tee, ein Zug Joint. Der Wal summt dazu.']));
}
function ext6Update(dt){
 if(!G)return;
 if(fade){P.fish=null;P.fight=null;}
 if(P.heroT>0)P.heroT-=dt;
 if(G.teaT>0)G.teaT-=dt;
 if(G.heroE===undefined)G.heroE=0;
 if(G.heroE<100){G.heroE=Math.min(100,G.heroE+dt*1.8);if(G.heroE>=100){toast('Heldenkraft aufgeladen! Der nächste Schlag ist ein SUPERSCHLAG.');sfx('power');}}
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
 const k=pick(['zwerge','musik','holle'].filter(q=>q!==SKL));
 if(k==='holle'){
  if(WXC.type==='snow')return;
  SKL=k;WXC.type='snow';WXC.t=rf(40,60);
  toast('Irgendwo schüttelt Frau Holle ihre Kissen aus. In Rheinhafen schneit es Federn!');
  mood(3,'+3 Schnee');sfx('magic');
  for(let i=0;i<10;i++)addFx(P.x+rf(-120,120),P.y+rf(-90,-20),'*','#ffffff',2.2,rf(12,30));
  return;
 }
 const sp=skSpawn();if(!sp)return;
 SKL=k;
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
 }else if(z.name==='wuppertal'){
  z.ska=[{k:'schweb',x:5*TS,y:wcy(5)*TS+16,dir:1,st:'go',t:0,cd:0,walk:0}];
 }else if(z.name==='portugal'){
  z.ska=[{k:'tram',x:10*TS,y:14*TS+26,dir:1,st:'go',t:0,cd:0,walk:0},{k:'fado',x:23*TS,y:23*TS,a:0,cd:0,walk:0}];
 }else if(z.name==='berge'){
  z.ska=[];
  z.ska.push({k:'wm',x:9.5*TS,y:17.6*TS,a:0,cd:0,ho:6});
  let gx=18,gy=0;while(gy<ZH&&z.T[gy*ZW+gx]===RK)gy++;
  z.ska.push({k:'gr',x:gx*TS+16,y:gy*TS+8,hx:gx*TS+16,hy:gy*TS+8,st:'hide',t:0,cd:0,gf:0,a:0});
  z.pcd=0;z.packs=0;
 }
}
function nearSk(){
 if(P.inCar||P.sit||P.ride||P.build||P.fish||P.fight)return null;
 let b=null,bd=99;
 skl().forEach(d=>{
  if(d.k==='ig')return;
  const r=d.k==='gr'?46:d.k==='mu'?40:(d.k==='tram'||d.k==='schweb')?72:34,dd=Math.hypot(d.x-P.x,d.y-P.y)-(r-34);
  if(dd<34&&dd<bd){bd=dd;b=d;}
 });
 return b;
}
function skPrompt(d){
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
 const k=mk.sk;
 if(k==='haus')hexeMenu();
 else if(k==='holle')holleMenu();
 else if(k==='werk')werkMenu();
 else if(k==='tisch')tischMenu();
 else if(k==='hase')hasenMenu();
 else if(k==='pudding')puddingMenu();
 else if(k==='burg')burgMenu();
 else if(k==='braum')braumeisterMenu();
 else if(k==='reise'){UI.euroFrom='';show('euro');}
}
function skOpen(d){
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
 else if(d.k==='mu'){
  if(d.cd>0){toast(d.v==='blas'?'Die Blaskapelle holt kurz Luft. Tuba braucht viel davon.':'Die Stadtmusikanten holen kurz Luft.');return;}
  d.cd=12;d.play=5;mood(6,'+6 Zugabe');sfx('musik');
  (d.v==='blas'?['Oans!','Zwoa!','Drei!','Humtata!']:['I-A!','Wuff!','Miau!','Kikeriki!']).forEach((s,i)=>addFx(d.x+(i-1.5)*10,d.y-36-i*3,s,'#ffe08a',1.8));
  peds.forEach(p=>{if(!p.snow&&p.st==='walk'&&Math.hypot(p.x-d.x,p.y-d.y)<220){p.st='dance';p.stT=6;}});
  skl().forEach(q=>{if(q.k==='zw')q.dn=5;});
  toast(d.v==='blas'?'Die Blaskapelle spielt einen zünftigen Marsch. Alle in Hörweite schunkeln mit.':'Die Stadtmusikanten spielen auf. Alle in Hörweite tanzen mit.');
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
 if(skAct2(p)||skAct3(p)||skAct4(p)||skAct5(p))return;
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
  if(SKT<=0){SKT=rf(80,150);if(!SKC.length&&wanted===0&&!P.inCar)skEvent();}
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
 const iv=(x,y,m)=>x>cx-m&&x<cx+VW+m&&y>cy-m&&y<cy+VH+m;
 if(ZONE){
  if(ZONE.candy)ZONE.candy.forEach(c=>{if(c.on&&iv(c.x,c.y,10))drawCandy(c);});
  if(ZONE.name==='maerchen'&&iv(19*TS,11*TS,60))drawTisch();
  if(ZONE.name==='maerchen'&&iv(23*TS,26*TS,520))drawAcker();
  if(ZONE.name==='berge'&&iv(12.5*TS,18*TS,120))drawSleigh(12.5*TS,18.3*TS);
  if(ZONE.name==='bayern')drawBayernDeko(cx,cy);
  if(ZONE.name==='portugal')drawRails(cx,cy);
  if(ZONE.name==='wuppertal')drawGirder(cx,cy);
 }
 skl().forEach(d=>{
  if(!iv(d.x,d.y,60))return;
  if(d.k==='zw')drawZwerg(d);
  else if(d.k==='hexe')drawHexe(d);
  else if(d.k==='holle')drawHolle(d);
  else if(d.k==='wm')drawWm(d);
  else if(d.k==='gr')drawGries(d);
  else if(d.k==='mu'){if(d.v==='blas')drawBlas(d);else drawMusik(d);}
  else if(d.k==='kap')drawKap(d);
  else if(d.k==='wolf')drawWolf(d);
  else if(d.k==='hase')drawHase(d);
  else if(d.k==='ig')drawIgel(d);
  else if(d.k==='huhn')drawHuhn(d);
  else if(d.k==='kuh')drawKuh(d);
  else if(d.k==='tram')drawTram(d);
  else if(d.k==='schweb')drawSchweb(d);
  else if(d.k==='tuffi')drawTuffi(d);
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
function startRace(bet){
 const h=skl().find(d=>d.k==='hase');if(!h||h.st!=='idle')return;
 if(bet){G.cash-=2;sfx('coin');}
 h.bet=bet;h.st='run';h.dir=1;h.round=0;h.x=13*TS+16;
 toast(bet==='hase'?'Du wettest auf den Hasen. Mutig.':bet==='igel'?'Du wettest auf den Igel. Klug.':'Auf die Plätze, fertig, los!');
 sfx('arrive');
}
function skAct3(p){
 if(p==='hr0'){startRace(null);return true;}
 if(p==='hrh'){startRace('hase');return true;}
 if(p==='hri'){startRace('igel');return true;}
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
 city:{n:'Rheinhafen',x:58,y:34,warp:'Du reist zurück nach Rheinhafen. Alles beim Alten, nur du bist besser drauf.'},
 amsterdam:{n:'Amsterdam',x:54,y:12,warp:'Du steigst in den Zug nach Westen. Grachten, Fahrräder, Tulpen: Willkommen in Amsterdam!'},
 wuppertal:{n:'Wuppertal',x:78,y:20,warp:'Der Zug rattert ins Bergische Land. Es geht bergauf, bergab und manchmal sogar in der Luft: Wuppertal!'},
 bayern:{n:'Bayern',x:88,y:39,warp:'Der Zug rollt nach Süden. Die Berge werden höher, die Hosen kürzer. Servus, Bayern!'},
 portugal:{n:'Portugal',x:13,y:68,warp:'Dein Flugzeug landet in Lissabon. Es riecht nach Meer, Zimt und Pastel de Nata. Olá, Portugal!'},
 oesterreich:{n:'Österreich',x:108,y:51,off:true,why:'Österreich ist noch in Planung. Dort wartet bald Kaffeehaus und Kaiserschmarrn.'}
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
  mood(3,'+3 Tram');cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);
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
 if(z.name==='bayern'){
  L.forEach(d=>{
   if(d.k==='kuh'){
    if(d.mu>0)d.mu-=dt;
    if(d.pause>0){d.pause-=dt;return;}
    d.steer-=dt;if(d.steer<=0){d.a+=rf(-1.2,1.2);d.steer=rf(2,5);if(chance(.4))d.pause=rf(2,5);}
    leash(d,9*TS,17*TS,300);
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
  mood(4,'+4 Schwebebahn');cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);
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

const H={
 G:()=>G,newGame,saveAll,hasSave,loadAll,GOODS,TRADE,DIST,MARKETS,UPS,BRAU_CAP,HAUS_CAP,eur,price,sellP,cap,used,worth,rank,clock,hour,
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
 const hc=g.heat>66?'var(--rd)':g.heat>33?'var(--am)':'var(--gr)';
 const night=hour()>=20||hour()<6;
 return '<div class="chip"><small>TAG '+g.day+(night&&!ZONE?' · NACHT':'')+(wxLabel()?' · '+wxLabel():'')+'</small><b class="am">'+H.clock()+'</b></div>'+
  '<div class="chip"><small>BARGELD</small><b class="gr">'+eur(g.cash)+'</b></div>'+
  '<div class="chip"><small>VORSCHUSS</small><b class="'+(g.debt>0?'rd':'mu')+'">'+eur(g.debt)+'</b></div>'+
  '<div class="chip"><small>'+(wanted?'POLIZEI':'HELD · '+Math.floor(g.hero||0)+' PKT')+'</small><b class="'+(wanted?'rd':'am')+'">'+(wanted?st:((g.heroE||0)>=100?'SUPERSCHLAG!':heroRank()))+'</b><div class="hb"><i style="width:'+Math.round(g.heroE||0)+'%;background:#ffd23f"></i></div></div>'+
  '<div class="chip"><small>LAUNE'+(g.high>0?' · BEKIFFT':g.drunk>=2?' · ANGEHEITERT':'')+'</small><b style="color:'+moodCol()+'">'+moodWord()+'</b><div class="hb"><i style="width:'+Math.round(g.mood)+'%;background:'+moodCol()+'"></i></div></div>'+
  '<div class="chip"><small>TRAGEN</small><b>'+used()+' / '+cap()+'</b></div>';
}
function promptText(){
 if(UI.screen||UI.modal||fade||P.sit||P.build)return '';
 if(P.fight)return 'OK: DRÜCKEN! Ringen!';
 if(P.fish)return P.fish.st==='bite'?'OK: JETZT ANZIEHEN!':'Warten ... (Richtung drücken: Leine einholen)';
 if(P.ride){if(nearWhale())return 'OK: Dem Wal Hallo sagen';return Math.abs(P.ride.sp)<110?'OK: Absteigen':'';}
 const mk=nearMarker();
 const lab=m=>'OK: '+(m.act||(m.kind==='hq'?'Apotheke':m.kind==='willi'?'Chefin Willi':m.n));
 if(P.inCar){
  if(mk&&Math.abs(V.sp)<80)return lab(mk);
  return Math.abs(V.sp)<60?'OK: Aussteigen':'';
 }
 if(nearThug())return G.heroE>=100?'OK: SUPERSCHLAG!':'OK: Zuschlagen';
 if(nearWhale())return 'OK: Dem Wal Hallo sagen';
 if(nearShark())return 'OK: Hai ringen!';
 if(mk)return lab(mk);
 if(nearSeat())return 'OK: Hinsetzen';
 const rd=nearRide();if(rd)return rd.oma&&!rd.stolen?'OK: Rollstuhl klauen':'OK: '+({sled:'Rodeln',chair:'Rollstuhl nehmen',boat:'Boot besteigen',bike:'Fahrrad nehmen'}[rd.k]);
 const sk=nearSk();if(sk)return skPrompt(sk);
 const pd=nearPed();if(pd)return 'OK: '+pd.nm+' ansprechen'+(pd.like?' ♥':'');
 if(nearSnowman())return 'OK: Schneemann umkicken';
 if(nearCastle())return 'OK: Sandburg kaputt treten';
 if(nearVan())return 'OK: Einsteigen';
 if(waterAhead()&&!aimBest(130,false))return 'OK: Angeln';
 const cb=ctxBuild();if(cb&&!aimBest(130,false))return cb==='castle'?'OK: Sandburg bauen':'OK: Schneemann bauen';
 const t=curAmmo();if(t)return 'OK: '+AMN[t]+(t==='wasser'?' spritzen ('+Math.floor(G.tank)+')':' werfen ('+G.ammo[t]+')');
 return '';
}
function hudUpdate(){
 const hudEl=$('#hud'),trk=$('#trk'),pr=$('#prompt'),mmEl=$('#mm');
 if(!G||UI.title){hudEl.style.display='none';trk.style.display='none';pr.style.display='none';mmEl.style.display='none';return;}
 hudEl.style.display='flex';trk.style.display='block';mmEl.style.display='block';
 const h=hudHtml();if(h!==UI.hudS){UI.hudS=h;hudEl.innerHTML=h;}
 let t='';
 G.active.forEach(m=>{
  const c=m.t==='kurier'?'k':m.t==='beschaffung'?'b':'';
  let s=m.t==='kurier'?(m.got?'Paket zu: '+DIST[m.to].n:'Paket holen: '+DIST[m.from].n):m.q+' '+GOODS[m.item].n+' → '+DIST[m.to].n;
  t+='<div class="'+c+'"><b>'+mTitle(m)+'</b> · '+s+' · Tag '+m.dl+'</div>';
 });
 thugs.forEach(u=>{if(u.loot&&u.ko<=0)t+='<div class="r"><b>Gangster</b> · hat '+u.loot.q+' '+GOODS[u.loot.g].n+' geklaut · rote Punkte auf der Karte</div>';});
 if(G.pistol&&curAmmo()==='wasser')t+='<div class="r"><b>Wasserpistole</b> · Tank '+Math.floor(G.tank)+' / 30</div>';
 if(RACE)t+='<div class="r"><b>Wettrennen</b> · gegen '+RACE.p.nm+' · noch '+Math.max(0,Math.ceil(RACE.max-RACE.t))+' s</div>';
 if(t!==UI.trkS){UI.trkS=t;trk.innerHTML=t;}
 let p=promptText();
 if(p!==UI.pS){UI.pS=p;pr.textContent=p;pr.style.display=p?'block':'none';}
}

const SCREENS={
 title(){
  return{hint:'Pfeiltasten: wählen · OK: bestätigen',cls:'t',html:'<div class="title"><h1>HOPFEN <span>&amp;</span> HANF</h1><p>Rheinhafen · Apotheke, Held &amp; Quatsch</p><div class="menu">'+
   btn('Neues Spiel','new',null,{def:1})+(H.hasSave()?btn('Spiel fortsetzen','cont'):'')+btn('Anleitung','help')+btn('Beenden','quit')+'</div></div>'};
 },
 help(){
  return{hint:'Zurück: schließen',html:'<div class="place" style="max-width:58rem"><h2>Anleitung</h2><div class="panel">'+
   '<p><b class="am">Steuerung:</b> Pfeiltasten laufen. OK: ansprechen, hinsetzen, einsteigen, werfen, bauen, angeln. Zurück: Menü. M: Ton an/aus. In Fahrzeugen: Hoch Gas, Runter Bremse, Links und Rechts lenken.</p>'+
   '<p><b class="am">Dein Job:</b> Du arbeitest in der Rhein-Apotheke. Alles wird legal bestellt, gebraut, angebaut, verkauft und geliefert. Alkohol und Cannabis gibt es nie für unter 18, und nie in ihrer Nähe.</p>'+
   '<p><b class="am">Superheld:</b> Gangster klauen Ware und verkaufen sie im Park. Rote Punkte auf der Karte zeigen sie. Schnapp sie mit OK, bring die Beute zurück und schütze Jugendliche. Ist die Heldenkraft voll, wird dein Schlag ein SUPERSCHLAG.</p>'+
   '<p><b class="am">Laune:</b> Bank, Bier, Tee, Joint, Tanzen, Strand und Rodeln heben sie. Regen und Hitze drücken sie. Auf Spielplätzen und bei der Kita sind Alkohol, Rauch und Werfen verboten.</p>'+
   '<p><b class="am">Leute:</b> Rote Herzen mögen dich. Abklatschen, Umarmen, Tanzen, Wettrennen. Niemand stirbt. Omas holen sich ihren Rollstuhl zurück, Kinder bespritzt du nur mit Wasser.</p>'+
   '<p><b class="am">Winter und Strand:</b> Schneemänner bauen, rodeln, Glühwein trinken. Sandburgen bauen oder kaputt treten, Wasserpistole, schwimmen, Boot fahren. Das Rhein-Schiff am Hafen bringt dich nach Amsterdam.</p>'+
   '<p><b class="am">Meer:</b> Am Wasser OK: Angeln, bei Zucken nochmal OK. Im tiefen Wasser OK: Hai ringen. Der Wal nimmt dich mit in seinen Bauch: Sofa, Tee, Joint.</p>'+
   '<p><b class="am">Märchen und Sketche:</b> Das Märchenbuch im Park bringt dich in den Märchenwald: Lebkuchenhaus zum Knabbern, liebe Hexe, Frau Holle, sieben Zwerge. In der Stadt laufen manchmal Zwerge oder Stadtmusikanten vorbei, und Frau Holle lässt es schneien. In den Bergen wartet die Weihnachtswerkstatt. Dort versteckt sich ein Berg-Griesgram, der Lebkuchen liebt. Im Märchenwald deckt dir das Tischlein Kuchen und Geschenke, und Rotkäppchen braucht Hilfe gegen den naschenden Wolf.</p>'+
   '<p><b class="am">Europa:</b> Im Reisebüro und im Menü öffnest du die Europa-Karte. Bayern hat Berge, Schloss, Blasmusik und Biergarten, Portugal Tram, Fado und Sardinen, Wuppertal Schwebebahn, Elefant Tuffi und ein Brauhaus. Wo es Bier gibt, gibt es nie welches für Kinder und Jugendliche. Österreich folgt.</p>'+
   '<p><b class="am">Skurrile Orte:</b> Gullydeckel, Telefonzelle, Dixi und Kühlschrank bringen dich an Strand, Vulkan, in die Berge, Höhle oder in den Märchenwald. Wer zu tief ins Glas schaut, wacht woanders auf.</p>'+
   '<p class="mu">Alles Fiktion, nur ein Spiel.</p></div>'+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 pause(){
  const g=G,w=H.worth();
  let ns='';g.events.forEach(e=>{ns+='<div class="news">'+e.t+'</div>';});
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: weiterspielen',html:'<div class="pmenu"><div class="hd"><h2>Menü</h2><div class="mu">Laune: '+moodWord()+' · Vermögen '+eur(w)+' · Respekt '+g.resp+' · Rang: '+H.rank(w)+'</div><div class="mu">Held: '+heroRank()+' ('+Math.floor(g.hero||0)+' Punkte) · Fänge '+(g.fang||0)+' · Haizähne '+(g.zahn||0)+'</div>'+ns+'</div>'+
   btn('Weiterspielen','back',null,{def:1})+btn('Handy: Aufträge ('+g.active.length+'/4)','missions')+btn('Rucksack','inv')+btn('Karte','map')+btn('Europa-Karte','euro')+btn('Van rufen (25 €)','vanCall')+btn('Ton: '+(SND.on?'an':'aus'),'snd')+btn('Touch-Tasten: '+({auto:'automatisch',off:'aus',on:'an'}[TPREF]),'tpref')+btn('Anleitung','help')+btn('Speichern und zum Titel','saveExit')+'</div>'};
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
  return{hint:'Zurück: schließen',html:'<div class="hd"><h2>Karte von Rheinhafen</h2><div class="mu">Gelb: Läden · Grün: Apotheke · Türkis: Büdchen · Lila: Portale · Weiße Ringe: Auftragsziele</div></div><canvas id="bigmap" width="304" height="192" style="width:100%;max-height:78%;border:2px solid var(--ln);border-radius:.4rem;image-rendering:pixelated"></canvas><div style="max-width:14rem">'+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 place(){
  const g=G,mk=UI.mk,d=DIST[mk.dist]||{n:mk.n,sub:'',d:''};let b='';
  if(d.mod)b+=btn('Zum Marktstand','market',null,{def:1});
  g.active.forEach(m=>{if(H.canPickup(m))b+=btn('Paket abholen: '+H.mTitle(m),'pickup',m.id,{cls:'m',note:'Übergabe: '+DIST[m.to].n});});
  g.active.forEach(m=>{if(m.to===g.loc){const ok=H.canDeliver(m);b+=btn('Abgeben: '+H.mTitle(m),'deliver',m.id,{cls:'d',off:!ok,why:ok?'':H.whyNot(m),note:H.mLine(m)+' Belohnung '+eur(m.rw)});}});
  if(mk.kind==='hq'){b+=btn('Labor: Brauen &amp; Anbauen','prod',null,{def:1});b+=btn('Ausbauten','ups');b+=btn('Schlafen bis zum Morgen','sleep');}
  b+=btn('Zurück zur Straße','back');
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: schließen',html:'<div class="place"><div class="hd"><h2>'+d.n+'</h2><div class="mu">'+d.sub+'</div><p>'+d.d+'</p></div>'+b+'</div>'};
 },
 market(){
  const k=G.loc;let rows='<div class="mrow h"><div>WARE</div><div class="num">KAUF</div><div class="num">VERKAUF</div><div class="num">DU HAST</div><div style="grid-column:span 3;text-align:center">KAUFEN</div><div style="grid-column:span 3;text-align:center">VERKAUFEN</div></div>';
  TRADE.forEach(t=>{
   const p=H.price(t,k),s=H.sellP(t,k),r=s/(GOODS[t].base*.85),kr=p/GOODS[t].base,n=G.inv[t];
   const kc=kr<.9?'gr':kr>1.15?'rd':'',ka=kr<.9?'▼ ':kr>1.15?'▲ ':'',vc=r>1.1?'gr':r<.9?'rd':'',va=r>1.1?'▲ ':r<.9?'▼ ':'';
   rows+='<div class="mrow"><div><b>'+GOODS[t].n+'</b></div><div class="num '+kc+'">'+ka+eur(p)+'</div><div class="num '+vc+'">'+va+eur(s)+'</div><div class="num own'+(n?' has':'')+'">'+n+'</div>'+
    btn('+1','buy',t+':1',{cls:'b'})+btn('+5','buy',t+':5',{cls:'b'})+btn('Max','buy',t+':max',{cls:'b'})+
    btn('-1','sell',t+':1',{cls:'s'})+btn('-5','sell',t+':5',{cls:'s'})+btn(n?'Alle ('+n+')':'Alle','sell',t+':all',{cls:'s'})+'</div>';
  });
  let news='';G.events.forEach(e=>{news+='<div class="news">'+e.t+'</div>';});
  return{hint:'Pfeiltasten: wählen · OK: kaufen/verkaufen · Zurück: zum Ort',html:'<div class="mk"><div class="mkh"><h2>Markt: '+DIST[k].n+'</h2><div class="mu">Bargeld <b class="gr">'+eur(G.cash)+'</b> · Tragen <b class="am">'+used()+' / '+cap()+'</b></div></div>'+news+rows+'<div class="leg"><span class="gr">▼ grün</span> Einkauf günstig · <span class="gr">▲ grün</span> Verkauf teuer = gutes Geschäft für dich &nbsp;|&nbsp; <span class="rd">rot</span> = schlechter Preis &nbsp;|&nbsp; weiß = normaler Preis. Verkauf immer 15 % unter dem Kaufpreis.</div><div style="margin-top:.4rem;max-width:14rem">'+btn('Fertig','back')+'</div></div>'};
 },
 missions(){
  const g=G;
  const tag=o=>'<span class="tg '+(o.t==='lieferung'?'l':o.t==='beschaffung'?'b':'k')+'">'+o.t.toUpperCase()+'</span>';
  let l='',r='';
  g.offers.forEach(o=>{l+='<div class="f card" data-a="accept" data-p="'+o.id+'">'+tag(o)+'<b>'+H.mTitle(o)+'</b><div>'+H.mLine(o)+'</div><div class="rw">Belohnung '+eur(o.rw)+' · bis Tag '+o.dl+'</div></div>';});
  g.active.forEach(m=>{
   const st=m.t==='kurier'?(m.got?'Paket dabei':'Noch abzuholen: '+DIST[m.from].n):'Dabei: '+Math.min(g.inv[m.item],m.q)+' / '+m.q;
   r+='<div class="f card" data-a="abandonAsk" data-p="'+m.id+'">'+tag(m)+'<b>'+H.mTitle(m)+'</b><div>'+H.mLine(m)+'</div><div class="rw">'+eur(m.rw)+' · bis Tag '+m.dl+' · '+st+'</div></div>';
  });
  if(!l)l='<div class="mu">Heute keine neuen Angebote.</div>';
  if(!r)r='<div class="mu">Du hast keine laufenden Aufträge.</div>';
  return{hint:'Links OK: annehmen · Rechts OK: abbrechen · Zurück: schließen',html:'<div class="two" style="height:calc(100% - 3.2rem)"><div class="panel"><h3>Angebote ('+g.offers.length+')</h3><div class="sc">'+l+'</div></div><div class="panel"><h3>Laufend ('+g.active.length+'/4)</h3><div class="sc">'+r+'</div></div></div><div style="max-width:14rem">'+btn('Zurück','back',null,{def:g.offers.length+g.active.length?0:1})+'</div>'};
 },
 prod(){
  const g=G,b=g.prod.brau,h=g.prod.haus,o=g.prod.out;
  const bm=Math.min(BRAU_CAP[g.up.brau],g.inv.hopfen,g.inv.malz),hm=Math.min(HAUS_CAP[g.up.haus],g.inv.samen);
  const bs=b.n>0?'Im Sud: <b>'+b.n+'</b> Ansätze, fertig in '+b.left+' Tag'+(b.left>1?'en':''):'Der Sud ist leer.';
  const hs=h.n>0?'Auf den Beeten: <b>'+h.n+'</b> Ansätze, Ernte in '+h.left+' Tag'+(h.left>1?'en':''):'Die Beete sind leer.';
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: zum Ort',html:'<div class="hd"><h2>Apotheke: Labor</h2><div class="mu">Ein Tag dauert 2,5 Minuten. Schlafen überspringt die Nacht.</div></div><div class="prodgrid">'+
   '<div class="panel"><h3>Kräuter-Brauerei (Stufe '+(g.up.brau+1)+')</h3><p>1 Hopfen + 1 Malz = 2 Fass Bier, 2 Tage. Kapazität: '+BRAU_CAP[g.up.brau]+' Ansätze.</p><p>'+bs+'</p>'+
    (b.n>0?'':btn('Brauen: 1 Ansatz','brew','1',{off:bm<1,why:'Du brauchst Hopfen und Malz dabei.'})+btn('Brauen: Maximum ('+bm+')','brew','max',{off:bm<1,why:'Du brauchst Hopfen und Malz dabei.'}))+'</div>'+
   '<div class="panel"><h3>Medizinal-Gewächshaus (Stufe '+(g.up.haus+1)+')</h3><p>1 Hanfsamen = 3 Gras, 3 Tage. Kapazität: '+HAUS_CAP[g.up.haus]+' Ansätze.</p><p>'+hs+'</p>'+
    (h.n>0?'':btn('Anbauen: 1 Ansatz','grow','1',{off:hm<1,why:'Du brauchst Hanfsamen dabei.'})+btn('Anbauen: Maximum ('+hm+')','grow','max',{off:hm<1,why:'Du brauchst Hanfsamen dabei.'}))+'</div></div>'+
   '<div class="panel" style="margin-top:.6rem"><h3>Lager</h3><p>Abholbereit: <b>'+o.bier+'</b> Fassbier, <b>'+o.gras+'</b> Cannabis.</p>'+btn('Alles einpacken','collect',null,{off:o.bier+o.gras<1,why:'Nichts abzuholen.',def:o.bier+o.gras>0?1:0})+'</div>'+
   '<div style="max-width:14rem">'+btn('Zurück','back',null,{def:o.bier+o.gras>0?0:1})+'</div>'};
 },
 ups(){
  let c='';
  Object.keys(UPS).forEach(k=>{
   const u=UPS[k],l=G.up[k],mx=l>=u.cost.length;
   c+='<div class="f card" data-a="up" data-p="'+k+'"><b>'+u.n+'</b> · Stufe '+l+' / '+u.cost.length+'<div>'+(mx?'<span class="gr">Höchststufe erreicht</span>':u.eff(l+1)+' <span class="am">für '+eur(u.cost[l])+'</span>')+'</div></div>';
  });
  return{hint:'Pfeiltasten: wählen · OK: kaufen · Zurück: zum Ort',html:'<div class="hd"><h2>Apotheke: Ausbauten</h2></div><div class="place" style="max-width:44rem;margin:0;height:calc(100% - 3rem)">'+c+btn('Zurück','back')+'</div>'};
 },
 willi(){
  return{hint:'Pfeiltasten: wählen · OK: bestätigen · Zurück: schließen',html:'<div class="place"><div class="hd"><h2>Chefin Dr. Willi</h2><p>"Ein Vorschuss ist wie Medizin: Nur die richtige Dosis hilft." Die Chefin verlangt 2% Zinsen pro Tag.</p><p>Vorschuss: <b class="rd">'+eur(G.debt)+'</b> · Bargeld: <b class="gr">'+eur(G.cash)+'</b></p></div>'+
   btn('100 € zurückzahlen','pay','100')+btn('500 € zurückzahlen','pay','500')+btn('Alles zurückzahlen, was geht','pay','all')+btn('Vorschuss: 500 €','loan','500',{note:'Limit 8.000 € insgesamt'})+btn('Zurück','back',null,{def:1})+'</div>'};
 },
 sit(){
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
  b+=btn('Umarmen','pHug',null,{off:m<35,why:'Du bist zu mies drauf für Umarmungen.'});
  b+=btn('Zusammen tanzen','pDance');
  b+=btn('Wettrennen!','pRace',null,{off:wanted>0||!!RACE,why:'Gerade nicht möglich.'});
  b+=btn('Zunge rausstrecken','pTongue');
  b+=btn('Schubsen','pPush',null,{off:m>=70||!!ng||!!(p.kid||p.teen),why:(p.kid||p.teen)?'Doch nicht bei Kindern und Jugendlichen!':ng?'Nicht auf dem Spielplatz!':'Du bist viel zu gut drauf zum Schubsen.'});
  b+=btn('Schlagen (Dampf ablassen)','pHit',null,{off:m>=45||!!ng||!!(p.kid||p.teen),why:(p.kid||p.teen)?'Doch nicht bei Kindern und Jugendlichen!':ng?'Nicht auf dem Spielplatz!':'Dafür bist du viel zu gut drauf.'});
  b+=btn('Weitergehen','back');
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+p.nm+(p.like?' <span class="rd">♥</span>':'')+'</h2><div class="mu">'+p.jb+'</div><div class="mu">'+(p.like?'Mag dich. Strahlt dich an.':'Guckt dich neutral an.')+'</div></div>'+b+'</div>'};
 },
 buedchen(){
  const mk=UI.mk,st=G.stock;
  let b=(ZONE&&ZONE.name==='wal')?btn('Tee trinken (gratis)','tea',null,{def:1})+btn('Joint kaufen: 6 €','shopB','joint'):btn('Bier kaufen: 3 €','shopB','bier',{def:1})+btn('Joint kaufen: 6 €','shopB','joint');
  if(ZONE&&ZONE.name==='bayern')b=btn('Maß Bier: 5 € (zwei Bier)','shopB','mass',{def:1})+btn('Brezn: 2 €','shopB','brezn');
  else if(ZONE&&ZONE.name==='portugal')b=btn('Pastel de Nata: 2 €','shopB','nata',{def:1})+btn('Sardine vom Grill: 3 €','shopB','sardine')+btn('Cerveja, kaltes Lagerbier: 3 €','shopB','cerveja');
  else if(ZONE&&ZONE.name==='wuppertal')b=btn('Hausbräu vom Fass: 4 €','shopB','hausbr',{def:1})+btn('Bergische Waffel mit Kirschen: 2 €','shopB','waffel')+btn('Panhas mit Apfelmus: 2 €','shopB','panhas');
  if(wxType()==='snow'||(ZONE&&ZONE.name==='berge'))b+=btn('Glühwein kaufen: 3 €','shopB','gluehwein');
  if(ZONE&&ZONE.name==='strand'&&!G.pistol)b+=btn('Wasserpistole kaufen: 5 €','shopB','pistol');
  b+=btn('Wasser kaufen: 1 € (macht nüchterner)','shopB','wasser')+btn('Plausch halten','chat')+btn('Tschüss','back');
  return{cls:'c',hint:'',html:'<div class="sitp"><div class="hd"><h2>'+mk.n+'</h2><div class="mu">Bargeld <b class="gr">'+eur(G.cash)+'</b> · Bier '+st.bier+' · Joints '+st.joint+((st.gluehwein>0)?' · Glühwein '+st.gluehwein:'')+'</div></div>'+b+'</div>'};
 },
 pack(){
  const L=[];TRADE.forEach(t=>{if(G.inv[t])L.push(GOODS[t].n+': <b>'+G.inv[t]+'</b>');});if(G.inv.koffer)L.push('Rezept-Paket: <b>'+G.inv.koffer+'</b>');
  const st=G.stock,am=G.ammo,cur=curAmmo(),why=noUse();
  const b=btn('Bier trinken ('+st.bier+')','drink',null,{off:!!why||st.bier<1,why:why||'Kein Bier mehr.'})+
   btn('Joint rauchen ('+st.joint+')','smoke',null,{off:!!why||st.joint<1,why:why||'Kein Joint mehr.'})+
   btn('Glühwein trinken ('+(st.gluehwein||0)+')','glue',null,{off:!!why||!(st.gluehwein>0),why:why||'Kein Glühwein mehr.'})+
   btn('Fass anzapfen: 1 Fassbier wird zu 8 Bier','tap',null,{off:G.inv.bier<1,why:'Du hast kein Fassbier dabei.'})+
   btn('Gras drehen: 1 Gras wird zu 6 Joints','roll',null,{off:G.inv.gras<1,why:'Du hast kein Gras dabei.'})+
   btn('Wurfobjekt: '+(cur?AMN[cur]+' ('+(cur==='wasser'?Math.floor(G.tank)+' Tank':am[cur])+')':'nichts'),'sel',null,{off:!(am.dose+am.stein+am.schnee+(G.pistol?1:0)),why:'Such erst Dosen, Steine oder Schneebälle.'})+
   btn('Zurück','back',null,{def:1});
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
  if(UI.screen==='map'){const bc=$('#bigmap');if(bc){const bx=bc.getContext('2d');bx.drawImage(MM,0,0);MKS.forEach(k=>{bx.fillStyle=k.kind==='hq'?'#6bcf63':k.kind==='willi'?'#e5604d':k.kind==='portal'?'#c06bff':k.kind==='buedchen'?'#46c2a0':k.kind==='scream'?'#ff5030':k.kind==='disco'?'#ff5fd0':'#f2b441';bx.beginPath();bx.arc(k.x/TS*mS(),k.y/TS*mS(),4,0,6.283);bx.fill();});if(!ZONE)G.active.forEach(a=>{const mk=MKQ[(a.t==='kurier'&&!a.got)?a.from:a.to];bx.strokeStyle='#fff';bx.lineWidth=2;bx.beginPath();bx.arc(mk.x/TS*mS(),mk.y/TS*mS(),7,0,6.283);bx.stroke();});bx.fillStyle='#fff';bx.beginPath();bx.arc(P.x/TS*mS(),P.y/TS*mS(),4,0,6.283);bx.fill();}}
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
 if(!cur||list.indexOf(cur)<0){setFocus(list[0]);return;}
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
 if(best)setFocus(best);
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
 if(P.fight){sharkPress();return;}
 if(P.fish){fishPull();return;}
 if(P.inCar){if(Math.abs(V.sp)<60){const mk=nearMarker();if(mk&&Math.hypot(mk.x-V.x,mk.y-V.y)<44){openMarker(mk);return;}if(!exitVan())toast('Hier ist kein Platz zum Aussteigen.');}return;}
 if(P.ride){if(nearWhale()){swallow();return;}leaveRide(false);return;}
 if(P.sit||P.build)return;
 if(nearThug()){punch();return;}
 if(nearWhale()){swallow();return;}
 const sk=nearShark();
 if(sk){startFight(sk);return;}
 const mk=nearMarker();
 if(mk){openMarker(mk);return;}
 const st=nearSeat();
 if(st){sitDown(st);return;}
 const rd=nearRide();
 if(rd){takeRide(rd);return;}
 const sk7=nearSk();
 if(sk7){skOpen(sk7);return;}
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
  toCity();H.newGame();UI.fkm={};UI.title=false;UI.hudS=null;UI.trkS=null;cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);
  UI.screen=null;
  showModal({title:'Willkommen in Rheinhafen',text:'Du arbeitest in der Rhein-Apotheke: Hier wird alles legal bestellt, verkauft und geliefert. Aber Gangster klauen Ware und verkaufen sie im Park. Zeit fürs Cape: Du bist der Superheld von Rheinhafen! Dazwischen darfst du einfach leben: Bank, Bier, Glühwein, Schneemänner, Sandburgen, Angeln, Haie, ein Wal, Märchenwald und Amsterdam. Alkohol und Cannabis gibt es nie für unter 18 und nie in ihrer Nähe.',choices:[{label:'Los geht\'s',a:'mclose'}]});
 },
 cont(){if(H.loadAll()){UI.fkm={};UI.title=false;UI.hudS=null;UI.trkS=null;cam.x=clamp(P.x-VW/2,0,MW*TS-VW);cam.y=clamp(P.y-VH/2,0,MH*TS-VH);closeAll();toast('Spielstand geladen.');}else toast('Kein Spielstand gefunden.');},
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
  if(G.inv.koffer)L.push('Rezept-Paket: '+G.inv.koffer);
  showModal({title:'Rucksack ('+used()+' / '+cap()+')',text:L.length?'':'Du hast nichts dabei.',lines:L,choices:[{label:'Schließen',a:'mclose'}]});
 },
 vanCall(){const r=H.callVan();closeAll();toast(r.msg);},
 saveExit(){H.saveAll();toCity();UI.title=true;UI.screen='title';UI.modal=null;render2();},
 buy(p){const x=p.split(':');res(H.buy(x[0],x[1]));},
 sell(p){
  const x=p.split(':');const r=H.sell(x[0],x[1]);
  if(r.ok&&r.witness){const near=cops.some(c=>Math.hypot(c.x-P.x,c.y-P.y)<260)||traffic.some(c=>c.cop&&Math.hypot(c.x-P.x,c.y-P.y)<260);if(near){closeAll();startWanted('Ein Polizist hat den Deal gesehen! Weg hier!');return;}}
  res(r);
 },
 brew(p){res(H.startBrew(p));},grow(p){res(H.startGrow(p));},collect(){res(H.collect());},
 up(k){res(H.buyUp(k));},pay(p){res(H.payDebt(p));},loan(p){res(H.loan(+p));},
 accept(id){res(H.accept(+id));},pickup(id){res(H.pickup(+id));},deliver(id){res(H.deliver(+id));checkWin();},
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
 tpref(){TPREF=TPREF==='auto'?'off':TPREF==='off'?'on':'auto';try{localStorage.setItem('hh_touch',TPREF);}catch(e){}setTouch(TPREF==='on');render2();toast(TPREF==='auto'?'Touch-Tasten erscheinen nur bei Berührung.':TPREF==='off'?'Touch-Tasten sind aus. Nur Fernbedienung und Tastatur.':'Touch-Tasten sind immer an.');},
 stand(){standUp();closeAll();},
 tap(){if(G.inv.bier<1)return;G.inv.bier--;G.stock.bier=Math.min(40,G.stock.bier+8);toast('Fass angezapft: +8 Bier.');render2();},
 roll(){if(G.inv.gras<1)return;G.inv.gras--;G.stock.joint=Math.min(40,G.stock.joint+6);toast('Gras gedreht: +6 Joints. Handwerk mit Liebe.');render2();},
 sel(){const o=['schnee','stein','dose'],have=o.filter(k=>G.ammo[k]>0);if(G.pistol)have.push('wasser');if(!have.length)return;const i=have.indexOf(curAmmo());G.sel=have[(i+1)%have.length];render2();},
 shopB(k){
  const pr={hausbr:4,waffel:2,panhas:2,bier:3,joint:6,wasser:1,gluehwein:3,pistol:5,mass:5,brezn:2,nata:2,sardine:3,cerveja:3}[k];
  if((k==='bier'||k==='joint'||k==='gluehwein'||k==='mass'||k==='cerveja'||k==='hausbr')&&minorNear(P.x,P.y,90)){toast('Ausweis bitte! Ein Kind oder Jugendlicher steht daneben: kein Verkauf von Alkohol und Cannabis.');return;}
  if(G.cash<pr){toast('Nicht genug Geld.');return;}
  if((k==='bier'&&G.stock.bier>=40)||(k==='joint'&&G.stock.joint>=40)||(k==='gluehwein'&&G.stock.gluehwein>=40)||(k==='mass'&&G.stock.bier>=39)||(k==='cerveja'&&G.stock.bier>=40)||(k==='hausbr'&&G.stock.bier>=40)){toast('Dein Rucksack ist randvoll.');return;}
  G.cash-=pr;sfx('coin');
  if(k==='bier'){G.stock.bier++;toast('Ein kaltes Bier für 3 €.');}
  else if(k==='joint'){G.stock.joint++;toast('Ein sauber gedrehter Joint für 6 €.');}
  else if(k==='gluehwein'){G.stock.gluehwein++;toast('Ein dampfender Glühwein für 3 €. Prost, Winter!');}
  else if(k==='mass'){G.stock.bier+=2;toast(pick(['Eine ordentliche Maß für 5 €. Zwei Bier im Rucksack, ein Lächeln im Gesicht. Ozapft is!','Die Kellnerin trägt sechs Maß gleichzeitig und stellt dir eine hin. Respekt, Prost!']));}
  else if(k==='brezn'){G.drunk=Math.max(0,G.drunk-1);mood(3,'+3 Brezn');toast('Eine riesige, knusprige Brezn mit viel Salz. Dein Magen sagt Danke.');}
  else if(k==='nata'){mood(3,'+3 Nata');toast('Ein Pastel de Nata, noch warm, mit Zimt obendrauf. Der Teig knistert wie ein Lagerfeuer.');}
  else if(k==='sardine'){mood(3,'+3 Sardine');toast('Eine Sardine frisch vom Grill, dazu Brot. So schmeckt das Meer, wenn es sich Mühe gibt.');}
  else if(k==='cerveja'){G.stock.bier++;toast('Eine Cerveja, eiskalt. Saúde!');}
  else if(k==='hausbr'){G.stock.bier++;toast('Hausbräu frisch vom Fass, goldgelb und mit perfekter Schaumkrone. Der Braumeister nickt stolz.');}
  else if(k==='waffel'){mood(3,'+3 Waffel');toast('Eine knusprige Bergische Waffel mit heißen Kirschen und Sahne. Die Kirschen sind heißer als dein Humor.');}
  else if(k==='panhas'){mood(3,'+3 Panhas');toast('Panhas mit Apfelmus. Rustikal, kräftig und überraschend lecker. Du fragst nicht, was drin ist.');}
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
 pPush(){const p=UI.ped;closeAll();if(!p||inNoGo(P.x,P.y))return;sfx('bonk');const a=Math.atan2(p.y-P.y,p.x-P.x);P.a=a;moveE(p,Math.cos(a)*26,Math.sin(a)*26,7);p.st='dazed';p.stT=2;mood(4,'+4');heat(2);addFx(p.x,p.y-18,'Hoppla!','#ffd23f');toast(pick(['Ups! '+p.nm+' sitzt auf dem Hosenboden.','Ein kleiner Schubser. '+p.nm+' dreht sich dreimal im Kreis.']));},
 pHit(){
  const p=UI.ped;closeAll();if(!p||inNoGo(P.x,P.y))return;sfx('hit');
  const a=Math.atan2(p.y-P.y,p.x-P.x);P.a=a;
  moveE(p,Math.cos(a)*34,Math.sin(a)*34,7);
  p.st='dazed';p.stT=3;G.stats.fights++;
  for(let i=0;i<4;i++)FX.push({x:p.x,y:p.y-8,vx:rf(-34,34),vy:rf(-46,-12),t:0,life:.9,txt:'★',col:'#ffd23f'});
  addFx(p.x,p.y-18,pick(['AUA!','Hey!','Uff!','Meine Brille!']),'#ffd23f');
  mood(10,'Dampf abgelassen');heat(6);
  if(copNear(P.x,P.y,230)){startWanted('Ein Polizist hat dich beim Prügeln gesehen! Lauf!');}
  else toast(pick(['Er rappelt sich beleidigt wieder auf. Niemand ist ernsthaft verletzt.','Peng! Das tat gut. '+p.nm+' sieht dich nur vorwurfsvoll an.','Dampf abgelassen. '+p.nm+' klopft sich den Staub ab und trollt sich.']));
 }
};
function back(){
 if(UI.modal){if(UI.modal.noBack)return;closeModal();return;}
 const s=UI.screen;
 if(s==='help'){if(UI.title)show('title');else if(UI.helpFrom==='pause')show('pause');else closeAll();return;}
 if(s==='sit'){standUp();closeAll();return;}
 if(s==='pack'){show('pause');return;}
 if(s==='market'||s==='prod'||s==='ups'){show('place');return;}
 if(s==='missions'||s==='map'){show('pause');return;}
 if(s==='euro'){if(UI.euroFrom==='pause')show('pause');else closeAll();return;}
 if(s==='title')return;
 closeAll();
}
H.setCb(function(m){
 if(m==='__win'){showModal({title:'Pate von Rheinhafen!',text:'Du hast 30.000 € Vermögen erreicht. Die ganze Stadt kennt deinen Namen. Du kannst weiterspielen.',choices:[{label:'Weiterspielen',a:'mclose'}]});return;}
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
function setTouch(on){
 if(TPREF==='off')on=false;else if(TPREF==='on')on=true;
 document.body.classList.toggle('touch',!!on);
}
setTouch(false);
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
  trafficUpdate(dt);pedsUpdate(dt);
 }else if(!menuActive()||(UI.screen==='sit'&&!UI.modal))update(dt);
 render();
 hudT+=dt;if(hudT>.1){hudT=0;hudUpdate();if(G&&!UI.title)renderMini();}
 requestAnimationFrame(frame);
}
resetEntities();
UI.screen='title';
render2();
requestAnimationFrame(frame);
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
