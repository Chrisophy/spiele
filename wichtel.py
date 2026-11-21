# -*- coding: utf-8 -*-
# Wichtel-Rettung
# IT('s) Possible
# 2026.11.20

EXT_ID = 'wichtel'
EXT_NAME = 'Wichtel-Rettung'
EXT_DESCRIPTION = '🧙 Knobelspaß: Kleine Wichtel laufen von allein. Gib ihnen Aufgaben (graben, bauen, klettern, Schirm ...) und nutze Konfetti-Bomben, Trampoline, Balken und Portale. 100 Level, leuchtender Hintergrund, Fernbedienung und Touch.'
EXT_LINKS = [('Wichtel-Rettung', 'index')]
EXT_SETTINGS = []


def register(api):
    api.route('index', lambda req: PAGE)
    api.widget('Wichtel-Rettung', lambda: {'text': 'Wichtel', 'sub': '100 Level, Knobelspaß', 'icon': '🧙'}, ttl=3600, icon='🧙')


PAGE = r"""<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Wichtel-Rettung</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}
html,body{height:100%;background:#120d1f;color:#f1eefc;font-family:system-ui,sans-serif;overflow:hidden}
#app{height:100dvh;display:flex;flex-direction:column}
#hud{flex:none;display:flex;gap:14px;align-items:center;justify-content:space-between;padding:6px 76px 6px 12px;background:#1c1431;border-bottom:1px solid #3a2c63;font-size:clamp(13px,2.2vmin,22px);font-weight:700;min-height:34px}
#hud b{color:#ffd45a}
#stage{flex:1;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;background:#0b0816}
canvas{image-rendering:pixelated;image-rendering:crisp-edges;display:block;background:#0b0816;border-radius:6px;touch-action:none}
#hint{position:absolute;left:50%;top:8px;transform:translateX(-50%);max-width:92%;background:rgba(18,13,31,.88);border:1px solid #5a47a0;border-radius:10px;padding:6px 12px;font-size:clamp(12px,2.1vmin,20px);text-align:center;pointer-events:none;opacity:0;transition:opacity .3s}
#hint.on{opacity:1}
#bar{flex:none;display:flex;gap:6px;justify-content:center;flex-wrap:wrap;padding:6px 8px 8px;background:#1c1431;border-top:1px solid #3a2c63}
#bar button{min-width:58px;padding:4px 8px 3px;border-radius:12px;border:3px solid transparent;background:#2b2150;color:#fff;font-size:12px;display:flex;flex-direction:column;align-items:center;gap:1px;cursor:pointer;position:relative}
#bar button i{font-style:normal;font-size:clamp(20px,3.6vmin,32px);line-height:1.1}
#bar button b{font-weight:600;font-size:clamp(10px,1.7vmin,15px)}
#bar button u{text-decoration:none;position:absolute;right:3px;top:1px;font-weight:800;color:#ffd45a;font-size:clamp(11px,1.9vmin,16px)}
#bar button.sel{background:#4b3a96;border-color:#ffd45a}
#bar button.off{opacity:.35}
#bar button.f{border-color:#5ec2ff;box-shadow:0 0 0 2px #5ec2ff55}
#bar .sep{width:10px}
#ov>:first-child{margin-top:auto}
#ov>:last-child{margin-bottom:auto}
#ov{position:absolute;inset:0;background:rgba(14,9,26,.82);display:none;flex-direction:column;align-items:center;justify-content:flex-start;gap:12px;padding:14px;text-align:center;overflow:auto}
#ov h1{font-size:clamp(24px,5vmin,44px);color:#ffd45a}
#ov p{max-width:640px;font-size:clamp(13px,2.4vmin,20px);color:#d8d2f2;line-height:1.35}
#ov .row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
#ov .grid{display:grid;grid-template-columns:repeat(10,minmax(40px,62px));gap:clamp(4px,.9vmin,8px)}
#ov .grid .mb,#ov .grid .lock{padding:clamp(2px,.6vmin,6px) 2px;border-radius:10px;font-size:clamp(11px,2.1vmin,18px);line-height:1.15}
#ov .grid .mb small{font-size:.62em}
.mb{background:#2f2560;color:#fff;border:3px solid transparent;border-radius:12px;padding:10px 16px;font-size:clamp(14px,2.6vmin,22px);font-weight:700;cursor:pointer}
.mb small{display:block;font-size:.7em;color:#ffd45a;font-weight:600}
.mb.f{border-color:#5ec2ff;background:#40318a}
.lock{background:#241c40;color:#6f6694;border-radius:12px;padding:10px 16px;font-size:clamp(14px,2.6vmin,22px);font-weight:700}
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
const W=320,H=160;
const SKN={climb:['🧗','Klettern'],float:['☂️','Schirm'],block:['✋','Stopper'],build:['🧱','Bauen'],bash:['👊','Hauen'],dig:['⬇️','Graben'],mine:['⛏️','Bergbau'],boom:['🎉','Knall'],plank:['🌉','Balken'],tramp:['🦘','Sprung']};
const ORDER=['climb','float','block','build','bash','dig','mine','boom','plank','tramp'];
const TOOLS={boom:1,plank:1,tramp:1};
const LV=[
{n:'Spaziergang',h:'Die Wichtel laufen von allein. Bring sie zur Tür! Mit dem Fadenkreuz kannst du schon üben.',cnt:10,need:10,rate:30,E:[50,20],X:[270,89],sk:{block:2,float:2},r:[[0,50,220,10],[200,90,120,10]]},
{n:'Graben',h:'Wähle ⬇️ Graben und gib es einem Wichtel. Er gräbt ein Loch nach unten.',cnt:10,need:8,rate:30,E:[60,25],X:[240,99],sk:{dig:2},r:[[0,50,320,25],[0,100,320,60]]},
{n:'Haudrauf',h:'Eine dicke Wand! 👊 Hauen schlägt einen Gang waagerecht hindurch.',cnt:10,need:8,rate:30,E:[40,62],X:[270,109],sk:{bash:2},r:[[0,110,320,10],[150,50,20,60]]},
{n:'Brückenbau',h:'Eine Lücke! 🧱 Bauen legt eine Treppe, bevor der erste hinunterfällt.',cnt:10,need:8,rate:30,E:[40,50],X:[290,79],sk:{build:2},r:[[0,90,140,10],[164,80,156,10]]},
{n:'Hoch hinaus',h:'Nur Kletterer kommen die Wand hoch. Gib sie vielen Wichteln.',cnt:8,need:4,rate:30,E:[40,62],X:[270,109],sk:{climb:5},r:[[0,110,320,10],[150,60,10,50]]},
{n:'Schirmchen',h:'Zu tief zum Springen! ☂️ Mit Schirm landen sie sanft. Sei schnell!',cnt:8,need:6,rate:36,E:[40,20],X:[250,139],sk:{float:8},r:[[0,50,110,10],[0,140,320,20]]},
{n:'Stopper',h:'Rechts ist ein Abgrund. ✋ Ein Stopper dreht alle um. Tippe ihn später an, dann läuft er zurück.',cnt:10,need:9,rate:30,E:[140,60],X:[40,99],sk:{block:2},r:[[0,100,200,10]]},
{n:'Bergbau',h:'⛏️ Bergbau gräbt schräg nach unten, zur Tür in der Höhle.',cnt:10,need:8,rate:30,E:[50,30],X:[230,118],sk:{mine:2},r:[[0,60,320,60],[200,100,60,19,0]]},
{n:'Erst bauen, dann hauen',h:'Zwei Hindernisse, zwei Fähigkeiten.',cnt:10,need:8,rate:30,E:[40,60],X:[280,99],sk:{build:2,bash:2},r:[[0,100,320,10],[100,100,24,10,0],[180,50,20,50]]},
{n:'Zwischenspiel',h:'Du hast alles zur Verfügung. Viel Spaß!',cnt:10,need:7,rate:30,E:[40,22],X:[285,139],sk:{float:10,climb:6,bash:3,build:2,mine:2,dig:2,block:2},r:[[0,50,120,10],[0,140,320,20],[200,100,15,40]]},
{n:'Party-Knall',h:'Eine Mauer! 🎉 Die Konfetti-Bombe sprengt sie weg. Setze sie mitten in die Mauer, nahe am Boden. Der Kreis zeigt, was verschwindet.',cnt:10,need:8,rate:30,E:[30,62],X:[280,109],sk:{boom:1},r:[[0,110,320,50],[150,50,14,60]]},
{n:'Trampolin',h:'Eine hohe Kante! 🦘 Stelle ein Trampolin auf den Boden vor der Kante, dann hüpfen alle hinauf.',cnt:10,need:8,rate:30,E:[30,100],X:[290,59],sk:{tramp:1},r:[[0,110,150,50],[150,60,170,100]]},
{n:'Balken legen',h:'Zwei Lücken! 🌉 Ein Balken ist 34 breit. Lege ihn quer über die Lücke.',cnt:10,need:9,rate:30,E:[30,60],X:[290,99],sk:{plank:2},r:[[0,100,90,60],[112,100,60,60],[194,100,126,60]]},
{n:'Portal-Reise',h:'Blaue Tür rein, orange Tür raus! Erst die Mauer wegschlagen.',cnt:10,need:8,rate:30,E:[30,30],X:[300,129],sk:{bash:1},r:[[0,60,230,100],[120,20,14,40],[240,130,80,30]],P:[[200,59,262,129]]},
{n:'Schluchtsprung',h:'Zu breit zum Bauen? 🦘 Ein Trampolin am Rand schleudert sie weit hinüber.',cnt:10,need:9,rate:30,E:[30,60],X:[290,99],sk:{tramp:1},r:[[0,100,110,60],[170,100,150,60]]},
{n:'Pappboden',h:'Der Boden ist dünn wie Pappe. 🎉 Eine Bombe macht ein Loch, durch das alle nach unten fallen.',cnt:10,need:8,rate:30,E:[40,20],X:[290,99],sk:{boom:1},r:[[0,50,320,2],[0,100,320,60]]},
{n:'Zickzack',h:'Von Etage zu Etage! Die letzte Stufe ist tief: ☂️ Schirme brauchst du fast alle.',cnt:12,need:9,rate:24,E:[30,5],X:[150,149],sk:{float:10},r:[[0,25,280,4],[40,55,280,4],[0,85,280,4],[0,150,320,10]]},
{n:'Portal-Salat',h:'Zwei Portale hintereinander, das letzte wirft sie hoch in die Luft. ☂️ Schirm nicht vergessen.',cnt:10,need:8,rate:30,E:[30,30],X:[290,139],sk:{float:9},r:[[0,60,120,100],[130,110,90,50],[230,140,90,20]],P:[[100,59,145,109],[200,109,250,30]]},
{n:'Hochhaus',h:'Erst hoch hüpfen, dann hoch klettern. 🦘 plus 🧗. Wer nicht klettern kann, läuft zurück und hüpft nochmal.',cnt:10,need:6,rate:30,E:[30,100],X:[295,34],sk:{tramp:1,climb:6},r:[[0,130,150,30],[150,85,170,75],[230,35,90,50]]},
{n:'Sprengbrücke',h:'Mauer und Lücke. 🎉 Knall für die Mauer, 🌉 Balken für die Lücke.',cnt:10,need:8,rate:30,E:[30,60],X:[290,99],sk:{boom:1,plank:1},r:[[0,100,170,60],[110,50,14,50],[196,100,124,60]]},
{n:'Stahlsperre',h:'Die Stahlplatte hält jeden Spaten auf, nur das Fenster nicht. ⬇️ Grabe genau über dem Fenster.',cnt:10,need:8,rate:30,E:[40,30],X:[290,109],sk:{dig:1},r:[[0,60,320,30],[150,90,24,6],[0,90,150,6,2],[174,90,146,6,2],[0,110,320,50]]},
{n:'Dreifach-Hürde',h:'Mauer, Lücke, Abgrund: 👊 🌉 ☂️ Alles hintereinander!',cnt:10,need:8,rate:30,E:[30,40],X:[295,144],sk:{bash:1,plank:1,float:9},r:[[0,70,150,90],[174,70,76,90],[100,20,14,50],[250,145,70,15]]},
{n:'Doppelsprung',h:'Zwei Schluchten, zwei Trampoline. 🦘🦘 Stelle das zweite auf die kleine Insel.',cnt:10,need:8,rate:30,E:[30,60],X:[305,99],sk:{tramp:2},r:[[0,100,100,60],[170,100,40,60],[280,100,40,60]]},
{n:'Wichtel-Parcours',h:'Das große Finale! Hauen, Balken, Trampolin und Konfetti: jedes Werkzeug hat seinen Platz.',cnt:10,need:8,rate:30,E:[15,60],X:[305,99],sk:{bash:1,plank:1,tramp:1,boom:1},r:[[0,100,110,60],[60,50,14,50],[134,100,36,60],[230,100,90,60],[270,50,14,50]]},
{"n":"Wackelpfad","h":"Hier warten: dicke Mauer, Lücke, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,80],"X":[300,109],"sk":{"boom":2,"plank":1,"tramp":1},"r":[[0,110,134,50],[156,110,164,50],[76,70,28,40],[211,75,44,35]]},
{"n":"Zappelhof","h":"Hier warten: Mauer, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,80],"X":[164,109],"sk":{"bash":2},"r":[[0,110,320,50],[76,70,14,40],[120,70,14,40]]},
{"n":"Purzelweg","h":"Hier warten: Schlucht, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,80],"X":[280,109],"sk":{"plank":2,"boom":1},"r":[[0,110,101,50],[161,110,159,50],[236,70,14,40]]},
{"n":"Kringelschlucht","h":"Hier warten: Schlucht, dicke Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,80],"X":[294,109],"sk":{"tramp":1,"boom":2},"r":[[0,110,101,50],[161,110,159,50],[236,70,28,40]]},
{"n":"Schnattermühle","h":"Hier warten: Mauer, Schlucht. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,80],"X":[280,109],"sk":{"boom":1,"tramp":1},"r":[[0,110,145,50],[205,110,115,50],[76,70,14,40]]},
{"n":"Brummturm","h":"Hier warten: Lücke, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":11,"rate":30,"E":[15,80],"X":[247,109],"sk":{"build":1,"tramp":1,"plank":2},"r":[[0,110,76,50],[98,110,222,50],[153,75,44,35]]},
{"n":"Hopsadach","h":"Hier warten: Mauer, Schlucht. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,80],"X":[280,109],"sk":{"boom":1,"plank":2,"float":2},"r":[[0,110,145,50],[205,110,115,50],[76,70,14,40]]},
{"n":"Tüftelgarten","h":"Hier warten: Lücke, Lücke, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[224,109],"sk":{"build":2,"boom":1,"tramp":1},"r":[[0,110,76,50],[98,110,30,50],[150,110,170,50],[180,70,14,40]]},
{"n":"Knobelkeller","h":"Hier warten: Mauer, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,80],"X":[239,109],"sk":{"boom":1,"climb":9},"r":[[0,110,320,50],[76,70,14,40],[145,75,44,35]]},
{"n":"Zipfelbrücke","h":"Hier warten: Mauer, Lücke, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,80],"X":[216,109],"sk":{"boom":1,"plank":1,"bash":1,"build":1},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,40],[172,70,14,28,2],[172,98,14,12]]},
{"n":"Flitztreppe","h":"Hier warten: Mauer, dicke Mauer, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[230,109],"sk":{"bash":2,"build":1},"r":[[0,110,178,50],[200,110,120,50],[76,70,14,40],[120,70,28,40]]},
{"n":"Bummeltal","h":"Hier warten: Kante, dicke Mauer, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[297,109],"sk":{"tramp":1,"bash":2,"dig":1},"r":[[0,110,320,50],[101,75,44,35],[195,70,28,40],[253,70,14,40]]},
{"n":"Kullerertunnel","h":"Hier warten: Lücke, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":11,"rate":30,"E":[15,80],"X":[247,109],"sk":{"build":1,"tramp":1,"mine":1},"r":[[0,110,76,50],[98,110,222,50],[153,75,44,35]]},
{"n":"Plumpsberg","h":"Hier warten: dicke Mauer, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,80],"X":[186,109],"sk":{"bash":1,"plank":1,"climb":1},"r":[[0,110,134,50],[156,110,164,50],[76,70,28,40]]},
{"n":"Tippelwald","h":"Hier warten: dicke Mauer, Kante, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[297,109],"sk":{"bash":2,"tramp":1},"r":[[0,110,320,50],[76,70,28,40],[159,75,44,35],[253,70,14,28,2],[253,98,14,12]]},
{"n":"Mümmelpfad","h":"Hier warten: Lücke, Lücke, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[224,109],"sk":{"plank":1,"build":1,"boom":1},"r":[[0,110,76,50],[98,110,30,50],[150,110,170,50],[180,70,14,28,2],[180,98,14,12]]},
{"n":"Schlafhof","h":"Hier warten: Stahlmauer, Kante, dicke Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,80],"X":[297,109],"sk":{"bash":1,"tramp":1,"boom":2,"block":2},"r":[[0,110,320,50],[76,70,14,28,2],[76,98,14,12],[145,75,44,35],[239,70,28,40]]},
{"n":"Rübezahlweg","h":"Hier warten: Stahlmauer, Lücke, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[216,109],"sk":{"boom":2,"build":1,"block":1},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,28,2],[76,98,14,12],[172,70,14,28,2],[172,98,14,12]]},
{"n":"Pfiffigschlucht","h":"Hier warten: Mauer, Lücke, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[291,109],"sk":{"bash":1,"build":1,"climb":11,"plank":2},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,40],[197,75,44,35]]},
{"n":"Zaubermühle","h":"Hier warten: Kante, Lücke, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[299,109],"sk":{"climb":11,"plank":2,"float":2},"r":[[0,110,195,50],[217,110,30,50],[269,110,51,50],[101,75,44,35]]},
{"n":"Wackelschlucht","h":"Hier warten: Mauer, Lücke, Lücke, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[268,109],"sk":{"boom":2,"plank":2},"r":[[0,110,120,50],[142,110,30,50],[194,110,126,50],[76,70,14,40],[224,70,14,28,2],[224,98,14,12]]},
{"n":"Zappelmühle","h":"Hier warten: Stahlmauer, Stahlmauer, Mauer, dicke Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[266,109],"sk":{"boom":3,"bash":1},"r":[[0,110,320,50],[76,70,14,28,2],[76,98,14,12],[120,70,14,28,2],[120,98,14,12],[164,70,14,40],[208,70,28,40]]},
{"n":"Purzelturm","h":"Hier warten: Mauer, Stahlmauer, Mauer, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[260,109],"sk":{"boom":2,"bash":1,"plank":1},"r":[[0,110,208,50],[230,110,90,50],[76,70,14,40],[120,70,14,28,2],[120,98,14,12],[164,70,14,40]]},
{"n":"Kringeldach","h":"Hier warten: Stahlmauer, Mauer, Mauer, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,80],"X":[252,109],"sk":{"boom":2,"bash":2},"r":[[0,110,320,50],[76,70,14,28,2],[76,98,14,12],[120,70,14,40],[164,70,14,40],[208,70,14,40]]},
{"n":"Schnattergarten","h":"Hier warten: dicke Mauer, Stahlmauer, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[147,139],"sk":{"bash":1,"boom":1,"build":1,"float":8,"tramp":1},"r":[[0,60,290,10],[76,20,28,40],[200,140,120,20],[0,140,178,20],[230,100,14,28,2],[230,128,14,12]]},
{"n":"Brummkeller","h":"Hier warten: Stahlmauer, Lücke, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[216,109],"sk":{"bash":2,"plank":1,"boom":1},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,28,2],[76,98,14,12],[172,70,14,40]]},
{"n":"Hopsabrücke","h":"Hier warten: Mauer, Kante, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[124,139],"sk":{"bash":1,"tramp":1,"float":12,"dig":1},"r":[[0,60,290,10],[76,20,14,40],[0,140,320,20],[175,105,44,35]]},
{"n":"Tüfteltreppe","h":"Hier warten: Lücke, Stahlmauer, Mauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[216,109],"sk":{"plank":1,"bash":1,"boom":1},"r":[[0,110,76,50],[98,110,222,50],[128,70,14,28,2],[128,98,14,12],[172,70,14,40]]},
{"n":"Knobeltal","h":"Hier warten: Mauer, Lücke, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[291,109],"sk":{"bash":1,"plank":1,"climb":11,"tramp":1},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,40],[197,75,44,35]]},
{"n":"Zipfeltunnel","h":"Hier warten: Lücke, Stahlmauer, Kante. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,80],"X":[291,109],"sk":{"build":1,"boom":1,"climb":8,"block":2},"r":[[0,110,76,50],[98,110,222,50],[128,70,14,28,2],[128,98,14,12],[197,75,44,35]]},
{"n":"Flitzberg","h":"Hier warten: Mauer, Lücke, Mauer, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[260,109],"sk":{"boom":2,"build":1,"bash":1,"plank":2},"r":[[0,110,120,50],[142,110,178,50],[76,70,14,40],[172,70,14,40],[216,70,14,28,2],[216,98,14,12]]},
{"n":"Bummelwald","h":"Hier warten: dicke Mauer, Stahlmauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[199,139],"sk":{"bash":1,"boom":2,"float":10,"block":1},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,28,2],[134,48,14,12],[0,140,320,20],[230,100,14,40]]},
{"n":"Kullererpfad","h":"Hier warten: Lücke, Stahlmauer, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[224,109],"sk":{"build":2,"bash":1},"r":[[0,110,76,50],[98,110,74,50],[194,110,126,50],[128,70,14,28,2],[128,98,14,12]]},
{"n":"Plumpshof","h":"Hier warten: Stahlmauer, Mauer, Lücke. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,80],"X":[216,109],"sk":{"boom":2,"build":1,"bash":2,"tramp":1},"r":[[0,110,164,50],[186,110,134,50],[76,70,14,28,2],[76,98,14,12],[120,70,14,40]]},
{"n":"Tippelweg","h":"Hier warten: Lücke, Stahlmauer, Stahlmauer, Stahlmauer. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,80],"X":[260,109],"sk":{"build":1,"bash":1,"boom":2,"plank":1},"r":[[0,110,76,50],[98,110,222,50],[128,70,14,28,2],[128,98,14,12],[172,70,14,28,2],[172,98,14,12],[216,70,14,28,2],[216,98,14,12]]},
{"n":"Mümmelschlucht","h":"Hier warten: Stahlmauer, Schlucht, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[39,139],"sk":{"boom":1,"tramp":1,"bash":1,"float":10},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[219,140,101,20],[0,140,159,20],[70,100,14,40]]},
{"n":"Schlafmühle","h":"Hier warten: Kante, dicke Mauer, Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":13,"rate":30,"E":[15,30],"X":[155,139],"sk":{"tramp":1,"bash":2,"boom":1,"float":13,"build":1},"r":[[0,60,290,10],[101,25,44,35],[195,20,28,40],[0,140,320,20],[230,100,14,40],[186,100,14,28,2],[186,128,14,12]]},
{"n":"Rübezahlturm","h":"Hier warten: Kante, Stahlmauer, Kante, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[80,139],"sk":{"tramp":2,"bash":1,"boom":1,"float":8,"mine":1,"dig":1},"r":[[0,60,290,10],[101,25,44,35],[195,20,14,28,2],[195,48,14,12],[0,140,320,20],[175,105,44,35],[111,100,14,40]]},
{"n":"Pfiffigdach","h":"Hier warten: Stahlmauer, Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[199,139],"sk":{"boom":1,"bash":2,"float":10},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,14,40],[0,140,320,20],[230,100,14,28,2],[230,128,14,12]]},
{"n":"Zaubergarten","h":"Hier warten: dicke Mauer, Mauer, Kante, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[80,139],"sk":{"bash":1,"boom":2,"tramp":1,"float":8,"mine":1,"plank":1},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,40],[0,140,320,20],[175,105,44,35],[111,100,14,28,2],[111,128,14,12]]},
{"n":"Wackeldach","h":"Hier warten: Stahlmauer, dicke Mauer, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[191,139],"sk":{"boom":3,"plank":1,"float":9,"block":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,28,40],[244,140,76,20],[0,140,222,20]]},
{"n":"Zappelgarten","h":"Hier warten: Stahlmauer, Stahlmauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[185,139],"sk":{"bash":3,"float":10,"build":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,14,28,2],[120,48,14,12],[0,140,320,20],[216,100,28,40]]},
{"n":"Purzelkeller","h":"Hier warten: Kante, Mauer, Mauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[199,139],"sk":{"tramp":1,"boom":2,"bash":1,"float":10,"build":1},"r":[[0,60,290,10],[101,25,44,35],[195,20,14,40],[239,20,14,40],[0,140,320,20],[230,100,14,40]]},
{"n":"Kringelbrücke","h":"Hier warten: Stahlmauer, Mauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":7,"rate":30,"E":[15,30],"X":[141,139],"sk":{"boom":1,"bash":2,"float":7},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[0,140,320,20],[230,100,14,40],[172,100,28,40]]},
{"n":"Schnattertreppe","h":"Hier warten: dicke Mauer, Stahlmauer, Stahlmauer, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[302,139],"sk":{"bash":1,"boom":2,"dig":1,"float":8,"block":1},"r":[[0,60,123,10],[123,60,52,24],[175,60,145,10],[123,84,14,6,2],[137,84,24,6],[161,84,14,6,2],[76,20,28,40],[0,140,320,20],[227,100,14,28,2],[227,128,14,12],[271,100,14,28,2],[271,128,14,12]]},
{"n":"Brummtal","h":"Hier warten: Mauer, Kante, Schlucht, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[27,139],"sk":{"bash":1,"tramp":2,"boom":2,"float":10,"climb":2},"r":[[0,60,290,10],[76,20,14,40],[145,25,44,35],[219,140,101,20],[0,140,159,20],[56,100,28,40]]},
{"n":"Hopsatunnel","h":"Hier warten: dicke Mauer, Lücke, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[147,139],"sk":{"bash":1,"build":1,"boom":1,"float":8,"tramp":1},"r":[[0,60,290,10],[76,20,28,40],[244,140,76,20],[0,140,222,20],[178,100,14,28,2],[178,128,14,12]]},
{"n":"Tüftelberg","h":"Hier warten: Stahlmauer, Mauer, Mauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[185,139],"sk":{"boom":3,"bash":1,"float":8},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,14,40],[164,20,14,40],[0,140,320,20],[216,100,28,40]]},
{"n":"Knobelwald","h":"Hier warten: Stahlmauer, Stahlmauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[155,139],"sk":{"bash":1,"boom":2,"float":12,"block":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[0,140,320,20],[230,100,14,28,2],[230,128,14,12],[186,100,14,40]]},
{"n":"Zipfelpfad","h":"Hier warten: dicke Mauer, Mauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[155,139],"sk":{"bash":3,"float":9,"boom":2},"r":[[0,60,290,10],[76,20,28,40],[0,140,320,20],[230,100,14,40],[186,100,14,40]]},
{"n":"Flitzhof","h":"Hier warten: dicke Mauer, Mauer, Mauer, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[302,139],"sk":{"boom":3,"bash":1,"dig":1,"float":9,"plank":2},"r":[[0,60,125,10],[125,60,52,24],[177,60,143,10],[125,84,14,6,2],[139,84,24,6],[163,84,14,6,2],[76,20,28,40],[0,140,320,20],[229,100,14,40],[273,100,14,40]]},
{"n":"Bummelweg","h":"Hier warten: Mauer, Mauer, Kante, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[80,139],"sk":{"boom":1,"bash":1,"tramp":1,"float":8},"r":[[0,60,290,10],[76,20,14,40],[0,140,320,20],[230,100,14,40],[131,105,44,35]]},
{"n":"Kullererschlucht","h":"Hier warten: Stahlmauer, Stahlmauer, Lücke, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[302,139],"sk":{"boom":1,"bash":1,"build":1,"dig":1,"float":12},"r":[[0,60,126,10],[126,60,52,24],[178,60,142,10],[126,84,14,6,2],[140,84,24,6],[164,84,14,6,2],[76,20,14,28,2],[76,48,14,12],[0,140,274,20],[296,140,24,20],[230,100,14,28,2],[230,128,14,12]]},
{"n":"Plumpsmühle","h":"Hier warten: Stahlmauer, dicke Mauer, dicke Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[141,139],"sk":{"bash":3,"boom":2,"float":8,"plank":2,"tramp":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,28,40],[0,140,320,20],[216,100,28,40],[172,100,14,28,2],[172,128,14,12]]},
{"n":"Tippelturm","h":"Hier warten: Mauer, Mauer, Stahlmauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,30],"X":[141,139],"sk":{"bash":3,"boom":1,"float":9,"tramp":1,"block":1},"r":[[0,60,290,10],[76,20,14,40],[120,20,14,40],[0,140,320,20],[230,100,14,28,2],[230,128,14,12],[172,100,28,40]]},
{"n":"Mümmeldach","h":"Hier warten: Mauer, Stahlmauer, Kante, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[80,139],"sk":{"boom":2,"tramp":1,"bash":1,"float":10,"mine":2,"dig":1},"r":[[0,60,290,10],[76,20,14,40],[120,20,14,28,2],[120,48,14,12],[0,140,320,20],[175,105,44,35],[111,100,14,40]]},
{"n":"Schlafgarten","h":"Hier warten: Kante, dicke Mauer, Lücke, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[139,139],"sk":{"tramp":1,"bash":1,"plank":1,"build":1,"float":8},"r":[[0,60,290,10],[101,25,44,35],[195,20,28,40],[244,140,76,20],[192,140,30,20],[0,140,170,20]]},
{"n":"Rübezahlkeller","h":"Hier warten: Stahlmauer, dicke Mauer, Stahlmauer, Lücke, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[147,139],"sk":{"bash":2,"boom":3,"plank":1,"float":8},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,28,40],[178,20,14,28,2],[178,48,14,12],[244,140,76,20],[0,140,222,20],[178,100,14,40]]},
{"n":"Pfiffigbrücke","h":"Hier warten: dicke Mauer, Mauer, dicke Mauer, Lücke, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[89,139],"sk":{"bash":4,"build":1,"float":10,"climb":1,"block":2},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,40],[186,140,134,20],[0,140,164,20],[216,100,28,40],[120,100,14,40]]},
{"n":"Zaubertreppe","h":"Hier warten: Stahlmauer, dicke Mauer, dicke Mauer, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[302,139],"sk":{"boom":3,"bash":1,"dig":1,"float":8,"mine":1,"build":1},"r":[[0,60,168,10],[168,60,52,24],[220,60,100,10],[168,84,14,6,2],[182,84,24,6],[206,84,14,6,2],[76,20,14,28,2],[76,48,14,12],[120,20,28,40],[0,140,320,20],[272,100,28,40]]},
{"n":"Wackelbrücke","h":"Hier warten: dicke Mauer, Stahlmauer, Stahlmauer, Stahlmauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[155,139],"sk":{"bash":3,"boom":2,"float":10},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,28,2],[134,48,14,12],[178,20,14,28,2],[178,48,14,12],[0,140,320,20],[230,100,14,28,2],[230,128,14,12],[186,100,14,40]]},
{"n":"Zappeltreppe","h":"Hier warten: Mauer, Stahlmauer, Mauer, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":11,"rate":30,"E":[15,30],"X":[299,139],"sk":{"bash":2,"boom":1,"dig":1,"float":11},"r":[[0,60,151,10],[151,60,52,24],[203,60,117,10],[151,84,14,6,2],[165,84,24,6],[189,84,14,6,2],[76,20,14,40],[120,20,14,28,2],[120,48,14,12],[0,140,320,20],[255,100,14,40]]},
{"n":"Purzeltal","h":"Hier warten: Stahlmauer, dicke Mauer, Lücke, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[302,139],"sk":{"bash":1,"boom":2,"plank":1,"dig":1,"float":10},"r":[[0,60,170,10],[170,60,52,24],[222,60,98,10],[170,84,14,6,2],[184,84,24,6],[208,84,14,6,2],[76,20,14,28,2],[76,48,14,12],[120,20,28,40],[0,140,274,20],[296,140,24,20]]},
{"n":"Kringeltunnel","h":"Hier warten: Stahlmauer, Kante, Schlucht, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[31,139],"sk":{"bash":1,"tramp":2,"plank":1,"float":12,"mine":1,"dig":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[145,25,44,35],[219,140,101,20],[84,140,75,20],[0,140,62,20]]},
{"n":"Schnatterberg","h":"Hier warten: Mauer, Kante, Kante, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[72,139],"sk":{"boom":1,"tramp":2,"build":1,"float":12,"dig":2},"r":[[0,60,290,10],[76,20,14,40],[145,25,44,35],[125,140,195,20],[0,140,103,20],[175,105,44,35]]},
{"n":"Brummwald","h":"Hier warten: Mauer, Mauer, dicke Mauer, Lücke, dicke Mauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[89,139],"sk":{"boom":2,"bash":3,"plank":1,"float":12,"climb":2,"build":1},"r":[[0,60,290,10],[76,20,14,40],[120,20,14,40],[164,20,28,40],[244,140,76,20],[0,140,222,20],[164,100,28,40],[120,100,14,40]]},
{"n":"Hopsapfad","h":"Hier warten: dicke Mauer, Mauer, Mauer, Lücke, dicke Mauer, Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[45,139],"sk":{"boom":4,"bash":2,"plank":1,"float":9},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,40],[200,140,120,20],[0,140,178,20],[230,100,14,40],[120,100,28,40],[76,100,14,40]]},
{"n":"Tüftelhof","h":"Hier warten: Mauer, dicke Mauer, Mauer, Mauer, Lücke, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[103,139],"sk":{"boom":1,"bash":4,"build":1,"float":12,"plank":1,"block":1},"r":[[0,60,290,10],[76,20,14,40],[120,20,28,40],[178,20,14,40],[200,140,120,20],[0,140,178,20],[230,100,14,40],[134,100,14,28,2],[134,128,14,12]]},
{"n":"Knobelweg","h":"Hier warten: dicke Mauer, Mauer, Stahlmauer, Stahlmauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":7,"rate":30,"E":[15,30],"X":[97,139],"sk":{"bash":2,"boom":4,"float":7,"plank":1,"dig":2},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,40],[0,140,320,20],[230,100,14,28,2],[230,128,14,12],[186,100,14,28,2],[186,128,14,12],[128,100,28,40]]},
{"n":"Zipfelschlucht","h":"Hier warten: Mauer, dicke Mauer, Stahlmauer, Stahlmauer, Stahlmauer, dicke Mauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":9,"rate":30,"E":[15,30],"X":[97,139],"sk":{"boom":5,"bash":2,"float":9,"mine":2},"r":[[0,60,290,10],[76,20,14,40],[120,20,28,40],[178,20,14,28,2],[178,48,14,12],[0,140,320,20],[230,100,14,28,2],[230,128,14,12],[186,100,14,28,2],[186,128,14,12],[128,100,28,40]]},
{"n":"Flitzmühle","h":"Hier warten: dicke Mauer, Stahlmauer, Mauer, dicke Mauer, Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[53,139],"sk":{"bash":4,"boom":2,"float":9,"mine":2,"block":1},"r":[[0,60,290,10],[76,20,28,40],[134,20,14,28,2],[134,48,14,12],[0,140,320,20],[230,100,14,40],[172,100,28,40],[128,100,14,40],[84,100,14,28,2],[84,128,14,12]]},
{"n":"Bummelturm","h":"Hier warten: Stahlmauer, Stahlmauer, Stahlmauer, Stahlplatte. Überlege, welches Werkzeug wohin gehört.","cnt":12,"need":10,"rate":30,"E":[15,30],"X":[302,139],"sk":{"boom":2,"bash":1,"dig":1,"float":10},"r":[[0,60,169,10],[169,60,52,24],[221,60,99,10],[169,84,14,6,2],[183,84,24,6],[207,84,14,6,2],[76,20,14,28,2],[76,48,14,12],[120,20,14,28,2],[120,48,14,12],[0,140,320,20],[273,100,14,28,2],[273,128,14,12]]},
{"n":"Kullererdach","h":"Hier warten: Stahlmauer, Kante, Lücke, Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[103,139],"sk":{"boom":1,"tramp":1,"build":1,"bash":2,"float":8,"climb":1},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[145,25,44,35],[244,140,76,20],[0,140,222,20],[178,100,14,40],[134,100,14,28,2],[134,128,14,12]]},
{"n":"Plumpsgarten","h":"Hier warten: Stahlmauer, Stahlmauer, dicke Mauer, Mauer, Lücke, Lücke, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":8,"rate":30,"E":[15,30],"X":[95,139],"sk":{"boom":1,"bash":3,"plank":1,"build":1,"float":8},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,14,28,2],[120,48,14,12],[164,20,28,40],[200,140,120,20],[148,140,30,20],[0,140,126,20],[230,100,14,40]]},
{"n":"Tippelkeller","h":"Hier warten: Mauer, Mauer, Mauer, Kante, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":10,"need":9,"rate":30,"E":[15,30],"X":[80,139],"sk":{"bash":4,"tramp":1,"float":9},"r":[[0,60,290,10],[76,20,14,40],[120,20,14,40],[164,20,14,40],[0,140,320,20],[175,105,44,35],[111,100,14,28,2],[111,128,14,12]]},
{"n":"Mümmelbrücke","h":"Hier warten: Stahlmauer, Stahlmauer, Mauer, Stahlmauer, Abgrund. Überlege, welches Werkzeug wohin gehört.","cnt":14,"need":12,"rate":30,"E":[15,30],"X":[155,139],"sk":{"boom":2,"bash":2,"float":12},"r":[[0,60,290,10],[76,20,14,28,2],[76,48,14,12],[120,20,14,28,2],[120,48,14,12],[0,140,320,20],[230,100,14,40],[186,100,14,28,2],[186,128,14,12]]}
];
const cv=$('#cv'),ctx=cv.getContext('2d'),lcv=document.createElement('canvas');lcv.width=W;lcv.height=H;const lx=lcv.getContext('2d');
const tcv=document.createElement('canvas');tcv.width=W;tcv.height=H;const tctx=tcv.getContext('2d');
const id=tctx.createImageData(W,H);
const TH=[
{a:'#0b1030',b:'#2b2f7a',g:'#7fe3ff',f:'#fff3b0',h:'#171b4d',s:'#ffe27a'},
{a:'#3a1450',b:'#e0603a',g:'#ffd45a',f:'#ffb347',h:'#2a0f3a',s:'#ffd0a0'},
{a:'#08201f',b:'#146a5e',g:'#6bffb8',f:'#b6ff7a',h:'#0a2b2a',s:'#8fffd0'},
{a:'#1b0a33',b:'#6a1b90',g:'#ff6bf0',f:'#dcdcff',h:'#2a0f4a',s:'#ff9bf6',d:1},
{a:'#0a1c33',b:'#2f78b0',g:'#b6f3ff',f:'#f0fcff',h:'#123a5e',s:'#ffffff'},
{a:'#14081f',b:'#7a1f3f',g:'#ff9a6b',f:'#ffdf6b',h:'#2a0a1a',s:'#ffcf6b'}];
const bgc=document.createElement('canvas');bgc.width=640;bgc.height=320;
const gt=document.createElement('canvas');gt.width=640;gt.height=90;
let th=TH[0],bits=[];
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
let bombs=[],tramps=[],bub=[],sh=0,idle=0,sig=0,T=new Uint8Array(W*H),L=null,lv=0,ws=[],tick=0,spawned=0,saved=0,lost=0,cnt={},sel='dig',paused=false,speed=1,over=null,ptc=[],cx=160,cy=80,zone='menu',barIdx=0,btns=[],mbs=[],mbi=0,hintT=0,mode='main';
let dx0=0,dy0=0,dx1=-1,dy1=-1,dirty=false,snd=true,allOn=false,prog=[],AC=null,mouseMode=false;
try{prog=JSON.parse(localStorage.getItem('wr_prog')||'[]');allOn=localStorage.getItem('wr_all')==='1';snd=localStorage.getItem('wr_snd')!=='0'}catch(e){}
if(!Array.isArray(prog))prog=[];
function save(){try{localStorage.setItem('wr_prog',JSON.stringify(prog));localStorage.setItem('wr_all',allOn?'1':'0');localStorage.setItem('wr_snd',snd?'1':'0')}catch(e){}}
function beep(f,d,t,v,when,f2){if(!snd)return;try{if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();if(AC.state==='suspended')AC.resume();const n=AC.currentTime+(when||0),o=AC.createOscillator(),g=AC.createGain();o.type=t||'square';o.frequency.setValueAtTime(f,n);if(f2)o.frequency.linearRampToValueAtTime(f2,n+d);g.gain.setValueAtTime(v||.04,n);g.gain.exponentialRampToValueAtTime(.0001,n+d);o.connect(g);g.connect(AC.destination);o.start(n);o.stop(n+d+.03)}catch(e){}}
const SFX={ok:()=>beep(420,.12,'triangle',.05,0,700),no:()=>beep(160,.14,'sawtooth',.03),save:()=>beep(760,.12,'triangle',.05,0,1200),lose:()=>beep(380,.25,'triangle',.04,0,120),win:()=>[523,659,784,1047].forEach((f,i)=>beep(f,.22,'triangle',.06,i*.14)),move:()=>beep(300,.04,'square',.02),boing:()=>beep(200,.3,'sine',.08,0,700),boom:()=>{beep(120,.4,'sawtooth',.09,0,35);beep(70,.5,'square',.05,0,30)},fuse:()=>beep(1100,.25,'sawtooth',.015,0,500),port:()=>beep(500,.2,'sine',.05,0,1100)};
function sol(x,y){if(x<0||x>=W)return true;if(y<0||y>=H)return false;return T[y*W+x]!==0}
function colFree(c,fy){for(let k=0;k<8;k++)if(sol(c,fy-k))return false;return true}
function mark(x,y){if(!dirty){dx0=dx1=x;dy0=dy1=y;dirty=true}else{if(x<dx0)dx0=x;if(x>dx1)dx1=x;if(y<dy0)dy0=y;if(y>dy1)dy1=y}}
function setT(x,y,t){if(x<0||x>=W||y<0||y>=H)return;T[y*W+x]=t;mark(x,y)}
function info(x0,y0,x1,y1){let s=0,st=false;for(let y=Math.max(0,y0);y<=Math.min(H-1,y1);y++)for(let x=Math.max(0,x0);x<=Math.min(W-1,x1);x++){const t=T[y*W+x];if(t){s++;if(t===2)st=true}}return{s,st}}
function erase(x0,y0,x1,y1){for(let y=Math.max(0,y0);y<=Math.min(H-1,y1);y++)for(let x=Math.max(0,x0);x<=Math.min(W-1,x1);x++){const t=T[y*W+x];if(t===1||t===3){T[y*W+x]=0;mark(x,y)}}}
function px(x,y){const i=(y*W+x)*4,t=T[y*W+x],d=id.data;if(!t){d[i+3]=0;return}let r,g,b;
 if(t===2){const c=((x>>2)+(y>>2))&1;r=c?150:128;g=r;b=r+18;if((x&7)===0&&(y&7)===0){r=g=b=205}}
 else if(t===3){const s=y%3===0;r=s?150:198;g=s?98:142;b=s?48:82}
 else{const top=y===0||T[(y-1)*W+x]===0;
  if(top){r=72;g=176;b=60}
  else if(y>1&&T[(y-2)*W+x]===0){r=58;g=140;b=50}
  else{const h=((x*31+y*17)^(x*7))&7;r=124+h*3;g=82+h*2;b=44+h}}
 d[i]=r;d[i+1]=g;d[i+2]=b;d[i+3]=255}
function paintAll(){for(let y=0;y<H;y++)for(let x=0;x<W;x++)px(x,y);tctx.putImageData(id,0,0);dirty=false}
function flush(){if(!dirty)return;const y0=Math.max(0,dy0-2),y1=Math.min(H-1,dy1+2),x0=Math.max(0,dx0),x1=Math.min(W-1,dx1);for(let y=y0;y<=y1;y++)for(let x=x0;x<=x1;x++)px(x,y);tctx.putImageData(id,0,0,x0,y0,x1-x0+1,y1-y0+1);dirty=false}
const PAL={H:'#e03a3a',S:'#f2c496',W:'#ffffff',T:'#f0b429',L:'#5b3a1e',E:'#222222',K:'#c98a46',B:'#8a5a1a'};
const BASE=['....H...','...HHH..','..HHHHH.','..SSESS.','..WWWWW.','...WWW..','..TTTTT.','..TBBBT.','...T.T..'];
function fr(legs,mods){const r=BASE.concat([legs]).map(s=>s.split(''));(mods||[]).forEach(m=>{r[m[0]][m[1]]=m[2]});return r.map(x=>x.join(''))}
function mkS(rows,flip,hc){const c=document.createElement('canvas');c.width=8;c.height=rows.length;const x=c.getContext('2d');if(flip){x.translate(8,0);x.scale(-1,1)}rows.forEach((row,y)=>{for(let i=0;i<8;i++){const ch=row[i];if(ch!=='.'){x.fillStyle=ch==='H'?hc:PAL[ch];x.fillRect(i,y,1,1)}}});return c}
const LA='..LL.L..',LB='...L.LL.';
const HATS=['#e03a3a','#3a7ae0','#35b84a','#b43ae0','#f08a2a'];
const SDEF=[['walk',[fr(LA),fr(LB)]],['fall',[fr('..L..L..',[[5,1,'S'],[5,7,'S']])]],['climb',[fr(LA,[[3,7,'S'],[5,7,'S']]),fr(LB,[[2,7,'S'],[4,7,'S']])]],['block',[fr(LA,[[6,0,'T'],[6,1,'T'],[6,7,'T']])]],['build',[fr(LA,[[6,7,'K'],[7,7,'K']]),fr(LB,[[6,7,'K'],[7,7,'K']])]],['bash',[fr(LA,[[6,7,'S'],[7,7,'S']]),fr(LB,[[6,7,'S'],[7,7,'S']])]],['dig',[fr('.LL..LL.'),fr(LA)]],['exit',[fr('..L..L..',[[4,7,'S'],[3,7,'S']])]]];
const SPR=HATS.map(hc=>{const o={};SDEF.forEach(([k,a])=>{o[k]=[a.map(r=>mkS(r,true,hc)),a.map(r=>mkS(r,false,hc))]});return o});
const WJ=['Hui!','Wheee!','Boing!','Hoppla!'],WS=['Juhu!','Hurra!','Tschüss!','Geschafft!'],WL=['Autsch!','Huch!','Oje!'],WB=['Wumm!','Konfetti!','Huch!'],WP=['Zack!','Hui!','Wo bin ich?'],CONF=['#ff5a5a','#ffd45a','#5ad2ff','#9be37a','#ff8ae6','#ffffff'];
function chat(w,arr,p){if(bub.length>=3||Math.random()>p)return;const s=arr[(Math.random()*arr.length)|0];ctx.font='bold 13px system-ui,sans-serif';bub.push({x:w.x,y:w.y-12,t:0,s,w:ctx.measureText(s).width})}
function canApply(w,s){if(w.st==='dead'||w.st==='gone'||w.st==='exit')return false;if(w.st==='block')return true;if(s==='climb')return !w.climber;if(s==='float')return !w.floater;return w.st==='walk'}
function doApply(w,s){if(!w||w.st==='dead'||w.st==='gone'||w.st==='exit')return false;
 if(w.st==='block'){w.st='walk';w.dir=-w.dir;return true}
 if(!canApply(w,s)||!(cnt[s]>0))return false;cnt[s]--;
 if(s==='climb')w.climber=true;else if(s==='float')w.floater=true;else{w.t=0;w.nw=0;w.n=0;w.st=s}
 idle=0;updBar();return true}
function spawn(){ws.push({id:spawned,hat:spawned%5,x:L.E[0],y:L.E[1],dir:1,st:'fall',fd:0,climber:false,floater:false,floating:false,t:0,nw:0,n:0});spawned++}
function lose(w){w.st='dead';lost++;chat(w,WL,.5);for(let i=0;i<7;i++)ptc.push({x:w.x,y:Math.min(H-3,w.y-4),vx:(Math.random()-.5)*1.6,vy:-Math.random()*1.4-.4,l:16,c:i%2?'#ffe27a':'#fff'});SFX.lose()}
function slope(w){if(sol(w.x,w.y+1))return true;for(let j=1;j<=3;j++)if(sol(w.x,w.y+1+j)){w.y+=j;return true}return false}
function goFall(w){w.st='fall';w.fd=0;w.floating=false}
function walkStep(w){const nx=w.x+w.dir;
 for(const b of ws){if((b.st==='build'||b.st==='bash'||b.st==='mine')&&b.dir===w.dir&&(b.x-w.x)*w.dir>0&&Math.abs(b.x-nx)<=3&&Math.abs(b.y-w.y)<=8)return}
 for(const b of ws){if(b.st==='block'&&(b.x-w.x)*w.dir>0&&Math.abs(b.x-nx)<=2&&Math.abs(b.y-w.y)<=6){w.dir=-w.dir;return}}
 for(let h=0;h<=3;h++){if(colFree(nx,w.y-h)){w.x=nx;w.y-=h;return}}
 if(w.climber){w.st='climb';w.t=0}else w.dir=-w.dir}
function act(w){
 if(w.st==='dead'||w.st==='gone')return;
 if(w.st==='exit'){w.t++;if(w.t>=14){w.st='gone';saved++;SFX.save();chat(w,WS,.6);for(let i=0;i<8;i++)ptc.push({x:w.x,y:w.y-8,vx:(Math.random()-.5)*2,vy:-Math.random()*1.8-.4,l:22,c:CONF[i%CONF.length]})}return}
 if((w.st==='walk'||w.st==='fall'||w.st==='fly')&&Math.abs(w.x-L.X[0])<=3&&Math.abs(w.y-L.X[1])<=4){w.st='exit';w.t=0;return}
 if(w.st==='walk'||w.st==='fall'){
  if(L.P&&(w.pc||0)<=tick)for(const p of L.P){if(Math.abs(w.x-p[0])<=2&&Math.abs(w.y-p[1])<=5){w.x=p[2];w.y=p[3];w.pc=tick+20;w.fd=0;pburst(p[0],p[1]);pburst(p[2],p[3]);SFX.port();chat(w,WP,.5);if(!sol(w.x,w.y+1))goFall(w);return}}
  for(const t of tramps){if(t.cd<=tick&&Math.abs(w.x-t.x)<=5&&w.y>=t.y-3&&w.y<=t.y+1){t.cd=tick+14;w.st='fly';w.fx=w.x;w.fy=w.y-1;w.vx=w.dir*1.5;w.vy=-3.8;w.fd=0;w.floating=false;SFX.boing();chat(w,WJ,.7);return}}}
 w.t++;const d=w.dir;
 switch(w.st){
 case 'fall':{const sp=w.floating?1:2;for(let i=0;i<sp;i++){
   if(sol(w.x,w.y+1)){if(w.fd>58&&!w.floating){lose(w);return}w.fd=0;w.floating=false;w.st='walk';return}
   w.y++;w.fd++;if(w.y>=H+8){lose(w);return}}
  if(w.floater&&w.fd>16&&!w.floating)w.floating=true;break}
 case 'fly':{w.vy=Math.min(5,w.vy+.13);let nx=w.fx+w.vx;if(!colFree(Math.round(nx),Math.round(w.fy))){w.vx=-w.vx*.5;nx=w.fx}w.fx=nx;const xi=Math.round(nx);let ny=w.fy+w.vy;
  if(w.vy<0){if(sol(xi,Math.round(ny)-8)){w.vy=0;ny=w.fy}}
  else{const y0=Math.round(w.fy),y1=Math.round(ny);for(let yy=y0+1;yy<=y1+1;yy++){if(sol(xi,yy)){ny=yy-1;w.fy=ny;w.x=xi;w.y=ny;w.fd=0;w.st='walk';if(Math.abs(w.vx)>.3)w.dir=w.vx>0?1:-1;return}}}
  w.fy=ny;w.x=xi;w.y=Math.round(ny);if(w.y>=H+8)lose(w);break}
 case 'walk':if(!slope(w)){goFall(w);break}walkStep(w);break;
 case 'block':if(!sol(w.x,w.y+1))goFall(w);break;
 case 'dig':{if(w.t%3)break;
  const r=info(w.x-3,w.y+1,w.x+3,w.y+1);if(r.st){w.st='walk';break}
  erase(w.x-3,w.y+1,w.x+3,w.y+1);w.y++;
  for(let k=0;k<4;k++)if(Math.random()<.6)ptc.push({x:w.x+(Math.random()*6-3),y:w.y,vx:(Math.random()-.5)*.8,vy:-Math.random()*.8,l:8,c:'#a8743a'});
  if(w.y>=H-1||!sol(w.x,w.y+1))goFall(w);break}
 case 'bash':{if(!slope(w)){goFall(w);break}if(w.t%4)break;
  const a=Math.min(w.x+d,w.x+d*4),b=Math.max(w.x+d,w.x+d*4),r=info(a,w.y-8,b,w.y);
  if(r.st){w.st='walk';w.dir=-d;break}
  if(r.s){w.nw=0;erase(a,w.y-8,b,w.y);for(let k=0;k<3;k++)ptc.push({x:w.x+d*4,y:w.y-Math.random()*8,vx:d*Math.random()*.8,vy:-Math.random()*.6,l:8,c:'#a8743a'})}else w.nw++;
  if(w.nw>=3){w.st='walk';break}
  w.x+=d*2;break}
 case 'mine':{if(w.t%4)break;
  const a=Math.min(w.x+d,w.x+d*5),b=Math.max(w.x+d,w.x+d*5),r=info(a,w.y-7,b,w.y+1);
  if(r.st){w.st='walk';break}
  if(r.s){w.nw=0;erase(a,w.y-7,b,w.y+1)}else w.nw++;
  if(w.nw>=3){w.st='walk';break}
  w.x+=d;w.y++;if(!sol(w.x,w.y+1)){let f=false;for(let j=2;j<=4;j++)if(sol(w.x,w.y+j)){f=true;break}if(!f)goFall(w)}break}
 case 'build':{if(w.t%5)break;
  if(w.n>=12){w.st='walk';break}
  for(let i=1;i<=5;i++)if(!sol(w.x+d*i,w.y))setT(w.x+d*i,w.y,3);
  w.n++;
  if(!colFree(w.x+d*2,w.y-1)){w.st='walk';w.dir=-d;break}
  w.x+=d*2;w.y--;break}
 case 'climb':{if(w.t%2)break;
  if(sol(w.x,w.y-8)){w.dir=-d;goFall(w);break}
  const nx=w.x+d;for(let h=0;h<=3;h++){if(colFree(nx,w.y-h)){w.x=nx;w.y-=h;w.st='walk';return}}
  w.y--;break}
 }}
function step(){if(over||!L)return;tick++;idle++;
 if(spawned<L.cnt&&(tick-1)%L.rate===0)spawn();
 for(const b of bombs){if(b.f>0){if(!sol(b.x,b.y)){for(let i=0;i<2;i++)if(b.y<H&&!sol(b.x,b.y+1))b.y++}b.f--;if(b.f===0)blast(b.x,b.y)}}
 bombs=bombs.filter(b=>b.f>0&&b.y<H);
 for(const w of ws)act(w);
 fx();hud();
 if(saved*1000+lost!==sig){sig=saved*1000+lost;idle=0}
 if(spawned>=L.cnt){if(idle===1200)say('Hängt es? Mit 🏁 Ende oder 🔄 Neu geht es weiter.');if(idle>=600&&saved>=L.need){endLv(true);return}let live=0,blk=0;for(const w of ws){if(w.st==='block')blk++;else if(w.st!=='dead'&&w.st!=='gone')live++}
  if(live===0){if(saved>=L.need)endLv(true);else if(saved+blk>=L.need)say('Tippe den Stopper an, damit er mitkommt.');else endLv(false)}}}
function fx(){for(const p of ptc){p.x+=p.vx;p.y+=p.vy;p.vy+=.08;p.l--}ptc=ptc.filter(p=>p.l>0);for(const b of bub){b.t++}bub=bub.filter(b=>b.t<46);sh*=.82}
function pburst(x,y){for(let i=0;i<8;i++){const a=Math.random()*6.283;ptc.push({x,y:y-6,vx:Math.cos(a)*1.1,vy:Math.sin(a)*1.1,l:14,c:i%2?'#5ec2ff':'#ffa24a'})}}
function blast(bx,by){const r=13;for(let y=Math.max(0,by-r);y<=Math.min(H-1,by+3);y++)for(let x=Math.max(0,bx-r);x<=Math.min(W-1,bx+r);x++){if((x-bx)*(x-bx)+(y-by)*(y-by)<=r*r){const t=T[y*W+x];if(t===1||t===3){T[y*W+x]=0;mark(x,y)}}}
 sh=8;SFX.boom();for(let i=0;i<46;i++){const a=Math.random()*6.283,sp=.5+Math.random()*2;ptc.push({x:bx,y:by,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp-.8,l:26+(Math.random()*14|0),c:CONF[i%CONF.length]})}
 for(const w of ws){if(w.st==='dead'||w.st==='gone'||w.st==='exit')continue;const dx=w.x-bx,dy=w.y-4-by,d=Math.sqrt(dx*dx+dy*dy);
  if(d<=r+4){w.st='fly';w.fx=w.x;w.fy=w.y;w.vx=(Math.abs(dx)<1?(w.id%2?1:-1):dx/(d||1))*1.5;w.vy=-2.4;w.fd=0;w.floating=false;chat(w,WB,.7)}}}
function snapT(x,y){x=Math.round(x);y=Math.round(y);if(y<0||y>=H-1)return -1;let k=0;while(sol(x,y)&&k<30){y--;k++}if(sol(x,y))return -1;k=0;while(!sol(x,y+1)&&k<70){y++;k++}return sol(x,y+1)&&y<H-1?y:-1}
function useTool(s,x,y){x=Math.round(x);y=Math.round(y);if(!L||over||!(cnt[s]>0)){SFX.no();return false}
 if(s==='boom')bombs.push({x,y:Math.min(y,H-1),f:24});
 else if(s==='plank'){let n=0;for(let yy=y;yy<y+3;yy++)for(let xx=x-17;xx<x+17;xx++)if(xx>=0&&xx<W&&yy>=0&&yy<H&&!T[yy*W+xx]){setT(xx,yy,3);n++}if(!n){SFX.no();return false}}
 else if(s==='tramp'){const ty=snapT(x,y);if(ty<0){SFX.no();say('Das Trampolin braucht festen Boden darunter.');return false}tramps.push({x,y:ty,cd:0})}
 else return false;
 cnt[s]--;idle=0;updBar();SFX.ok();if(s==='boom')SFX.fuse();return true}
function say(t){const h=$('#hint');h.textContent=t;h.classList.add('on');hintT=Date.now()+6500}
function hud(){$('#ht').innerHTML='Level '+(lv+1)+' · <b>'+L.n+'</b>';$('#hs').innerHTML='Draußen '+(L.cnt-spawned)+' · Unterwegs '+ws.filter(w=>w.st!=='dead'&&w.st!=='gone').length+' · Gerettet <b>'+saved+'/'+L.cnt+'</b> (Ziel '+L.need+')'}
function loadLevel(n){lv=n;L=LV[n];T.fill(0);for(const r of L.r){const t=r[4]===undefined?1:r[4];for(let y=r[1];y<r[1]+r[3];y++)for(let x=r[0];x<r[0]+r[2];x++)if(x>=0&&x<W&&y>=0&&y<H)T[y*W+x]=t}
 paintAll();setTheme(Math.floor(n/4));bombs=[];tramps=(L.T||[]).map(p=>({x:p[0],y:p[1],cd:0}));bub=[];sh=0;ws=[];ptc=[];tick=0;spawned=0;saved=0;lost=0;over=null;paused=false;speed=1;idle=0;sig=0;cnt=Object.assign({},L.sk);sel=ORDER.find(s=>L.sk[s])||'dig';
 cx=Math.min(W-1,Math.max(0,L.E[0]+30));cy=Math.max(10,L.E[1]+30);ov.style.display='none';zone='field';mode='play';pushTrap();mkBar();hud();say(L.h)}
const ov=$('#ov');
function focusMb(i){mbs.forEach(x=>x.classList.remove('f'));mbi=Math.max(0,Math.min(mbs.length-1,i));if(mbs[mbi]){const b=mbs[mbi];b.classList.add('f');const r=b.getBoundingClientRect(),o=ov.getBoundingClientRect();if(r.top<o.top+70)ov.scrollTop-=o.top+70-r.top;else if(r.bottom>o.bottom-24)ov.scrollTop+=r.bottom-o.bottom+24}}
function showOv(title,msg,items,extra,focusIdx){mode=mode==='play'||mode==='pause'?'pause':'main';ov.innerHTML='';const h=el('h1');h.textContent=title;ov.append(h);
 if(msg){const p=el('p');p.textContent=msg;ov.append(p)}if(extra)ov.append(extra);
 const row=el('div','row');for(const it of items){const b=el('button','mb');b.textContent=it[0];b.onclick=()=>{ui();it[1]()};row.append(b)}ov.append(row);
 ov.style.display='flex';zone='menu';mbs=[...ov.querySelectorAll('.mb')];focusMb(focusIdx||0)}
function ui(){if(AC&&AC.state==='suspended')try{AC.resume()}catch(e){}}
function stars(n){const s=prog[n]||0;return '★'.repeat(s)+'☆'.repeat(3-s)}
function nextSp(){return speed===1?2:speed===2?3:speed===3?.5:1}
function unlocked(n){return allOn||n===0||(prog[n-1]||0)>0||(n>1&&(prog[n-2]||0)>0)}
function mainMenu(){mode='main';L=null;bar.innerHTML='';btns=[];$('#ht').textContent='Wichtel-Rettung';$('#hs').textContent='';const g=el('div','grid');let first=0,fi=0;
 for(let i=0;i<LV.length;i++){if(unlocked(i)){const b=el('button','mb');b.innerHTML=(i+1)+'<small>'+stars(i)+'</small>';b.onclick=()=>{ui();loadLevel(i)};g.append(b);if((prog[i]||0)===0&&!first){first=1;fi=g.children.length-1}}else{const d=el('div','lock');d.textContent='🔒 '+(i+1);g.append(d)}}
 if(!first)fi=0;
 showOv('🧙 Wichtel-Rettung','Die Wichtel laufen von allein. Gib dem richtigen Wichtel eine Fähigkeit oder setze Bombe, Balken und Trampolin, damit alle zur Tür kommen. Fernbedienung: Pfeile bewegen das Fadenkreuz, OK wirkt, am unteren Rand erreichst du die Leiste. Touch: einfach antippen.',
  [['Ton: '+(snd?'an':'aus'),()=>{snd=!snd;save();mainMenu()}],['Alle Level: '+(allOn?'an':'aus'),()=>{allOn=!allOn;save();mainMenu()}],['🚪 Beenden',quit]],g,fi)}
let trap=0,bk=0,quitting=0;
function quit(){quitting=1;if(trap)history.back();else closeGame()}
function pushTrap(){if(trap)return;try{history.pushState({wr:1},'');trap=1}catch(e){}}
function closeGame(){try{if(window.parent!==window){window.parent.history.back();return}}catch(e){}if(history.length>1)history.back();else location.href='/ui/'}
function resume(){ov.style.display='none';zone='field';mode='play';paused=false}
addEventListener('popstate',()=>{if(!trap)return;trap=0;
 if(quitting){closeGame();return}
 if(L&&mode!=='main'){pushTrap();if(Date.now()-bk<350)return;
  if(zone==='menu'){if(over)mainMenu();else if(mode==='pause')resume()}
  else if(zone==='bar'){zone='field';updBar()}
  else pauseMenu()}
 else closeGame()});
function pauseMenu(){paused=true;showOv('Pause',L.n,[['▶ Weiter',resume],['🔄 Neu starten',()=>loadLevel(lv)],['☰ Level wählen',mainMenu],['Ton: '+(snd?'an':'aus'),()=>{snd=!snd;save();pauseMenu()}],['🚪 Beenden',quit]])}
function endLv(win){over=win?'win':'lose';updBar();
 if(win){const k=saved===L.cnt?3:(saved>=Math.ceil(L.cnt*.8)?2:1);if(k>(prog[lv]||0)){prog[lv]=k;save()}SFX.win();for(let i=0;i<70;i++)ptc.push({x:Math.random()*W,y:-4-Math.random()*30,vx:(Math.random()-.5)*.8,vy:.3+Math.random()*.9,l:110,c:CONF[i%CONF.length]});
  const items=[];if(lv+1<LV.length)items.push(['▶ Nächstes Level',()=>loadLevel(lv+1)]);items.push(['🔄 Nochmal',()=>loadLevel(lv)],['☰ Level wählen',mainMenu]);
  showOv('Geschafft! '+'★'.repeat(k)+'☆'.repeat(3-k),saved+' von '+L.cnt+' Wichteln gerettet.'+(lv+1>=LV.length?' Du hast alle Level gemeistert!':''),items)}
 else{SFX.lose();showOv('Leider nicht genug',saved+' von '+L.cnt+' gerettet, nötig sind '+L.need+'.',[['🔄 Nochmal',()=>loadLevel(lv)],['☰ Level wählen',mainMenu]])}}
const bar=$('#bar');
function mkBar(){bar.innerHTML='';btns=[];
 for(const s of ORDER){if(!L.sk[s])continue;const b=el('button');b.dataset.s=s;b.innerHTML='<i>'+SKN[s][0]+'</i><b>'+SKN[s][1]+'</b><u></u>';b.onclick=()=>{ui();sel=s;zone='field';updBar()};bar.append(b);btns.push({b,f:()=>{sel=s;zone='field';updBar()}})}
 const sp=el('span','sep');bar.append(sp);
 const ctl=[['⏸','Pause',()=>{if(!over)pauseMenu()}],['⏩','Tempo',()=>{speed=nextSp();updBar();say('Tempo ×'+speed)}],['🏁','Ende',()=>{if(!over&&L){if(saved>=L.need)endLv(true);else say('Noch nicht genug gerettet: Ziel '+L.need)}}],['🔄','Neu',()=>loadLevel(lv)],['☰','Menü',mainMenu]];
 for(const c of ctl){const b=el('button');b.innerHTML='<i>'+c[0]+'</i><b>'+c[1]+'</b>';b.onclick=()=>{ui();c[2]()};bar.append(b);btns.push({b,f:c[2],ctl:1})}
 barIdx=Math.max(0,btns.findIndex(x=>x.b.dataset.s===sel));updBar();fit()}
function updBar(){for(const x of btns){const s=x.b.dataset.s;if(s){x.b.classList.toggle('sel',s===sel);x.b.classList.toggle('off',!(cnt[s]>0));x.b.querySelector('u').textContent=cnt[s]||0}x.b.classList.remove('f')}
 if(zone==='bar'&&btns[barIdx])btns[barIdx].b.classList.add('f')}
function pick(px_,py_,r,s){let best=null,bs=1e9;for(const w of ws){if(w.st==='dead'||w.st==='gone'||w.st==='exit')continue;const dx=w.x-px_,dy=(w.y-5)-py_,d=dx*dx+dy*dy;if(d>r*r)continue;const sc=d+((canApply(w,s)&&(w.st==='block'||cnt[s]>0))?0:1000);if(sc<bs){bs=sc;best=w}}return best}
function applyAt(x,y,r){if(!L||over||zone==='menu')return;if(TOOLS[sel]){useTool(sel,x,y);return}const w=pick(x,y,r,sel);if(w&&doApply(w,sel)){SFX.ok();return}SFX.no()}
const held={};
function goBar(){zone='bar';barIdx=Math.max(0,Math.min(barIdx,btns.length-1));updBar()}
function cycle(d){const av=ORDER.filter(s=>L&&L.sk[s]);if(!av.length)return;sel=av[(av.indexOf(sel)+d+av.length)%av.length];updBar()}
function navMenu(dir){if(!mbs.length)return;const cur=mbs[mbi].getBoundingClientRect(),cxm=cur.left+cur.width/2,cym=cur.top+cur.height/2;let best=-1,bd=1e9;
 mbs.forEach((b,i)=>{if(i===mbi)return;const r=b.getBoundingClientRect(),x=r.left+r.width/2-cxm,y=r.top+r.height/2-cym;let pr,pe;
  if(dir==='ArrowRight'){pr=x;pe=Math.abs(y)}else if(dir==='ArrowLeft'){pr=-x;pe=Math.abs(y)}else if(dir==='ArrowDown'){pr=y;pe=Math.abs(x)}else{pr=-y;pe=Math.abs(x)}
  if(pr<=2)return;const d=pr+pe*2.2;if(d<bd){bd=d;best=i}});
 if(best>=0)focusMb(best)}
addEventListener('keydown',e=>{if(e.ctrlKey||e.altKey||e.metaKey)return;const k=e.key;ui();let used=true;if(k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack')bk=Date.now();
 if(zone==='menu'){
  if(k.startsWith('Arrow'))navMenu(k);
  else if(k==='Enter'||k===' ')mbs[mbi]&&mbs[mbi].click();
  else if((k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack')&&mode==='pause'&&!over){resume()}
  else used=false}
 else if(zone==='bar'){
  if(k==='ArrowLeft'){barIdx=Math.max(0,barIdx-1);updBar()}else if(k==='ArrowRight'){barIdx=Math.min(btns.length-1,barIdx+1);updBar()}
  else if(k==='ArrowUp'||k==='Escape'||k==='Backspace'){zone='field';updBar()}
  else if(k==='Enter'||k===' '){const x=btns[barIdx];if(x){x.f();if(!x.ctl){zone='field';updBar()}}}
  else used=false}
 else{
  if(k==='ArrowDown'||k==='s'){if(cy>=H-3){goBar()}else{if(!held[k])nudge(0,1);held[k]=held[k]||Date.now()}}
  else if(['ArrowLeft','ArrowRight','ArrowUp','a','d','w'].includes(k)){if(!held[k])nudge(k==='ArrowRight'||k==='d'?1:k==='ArrowLeft'||k==='a'?-1:0,k==='ArrowUp'||k==='w'?-1:0);held[k]=held[k]||Date.now()}
  else if(k==='Enter'){applyAt(cx,cy,11)}
  else if(k===' '||k==='p'){paused=!paused;say(paused?'Pause':'Weiter')}
  else if(k==='Escape'||k==='Backspace'||k==='GoBack'||k==='BrowserBack'){if(L&&!over)pauseMenu()}
  else if(/^[0-9]$/.test(k)){const av=ORDER.filter(s=>L&&L.sk[s]),ix=k==='0'?9:+k-1;if(av[ix]){sel=av[ix];updBar()}}
  else if(k==='PageDown'||k==='ChannelDown'||k==='MediaTrackNext'||k===']'){cycle(1)}
  else if(k==='PageUp'||k==='ChannelUp'||k==='MediaTrackPrevious'||k==='['){cycle(-1)}
  else if(k==='f'||k==='MediaFastForward'){speed=nextSp();say('Tempo ×'+speed)}
  else if(k==='r'){if(L)loadLevel(lv)}
  else used=false}
 if(used){e.preventDefault();e.stopPropagation()}},true);
addEventListener('keyup',e=>{delete held[e.key]},true);
function toLog(e){const r=cv.getBoundingClientRect();return[(e.clientX-r.left)/r.width*W,(e.clientY-r.top)/r.height*H]}
cv.addEventListener('pointerdown',e=>{ui();const[x,y]=toLog(e);cx=x;cy=y;if(zone==='bar')zone='field';mouseMode=true;applyAt(x,y,e.pointerType==='touch'?13:10);e.preventDefault()});
cv.addEventListener('pointermove',e=>{if(e.pointerType==='mouse'){const[x,y]=toLog(e);cx=x;cy=y;mouseMode=true}});
let last=0,acc=0,hold0={};
function nudge(a,b){mouseMode=false;cx=Math.max(0,Math.min(W-1,cx+a));cy=Math.max(0,Math.min(H-1,cy+b))}
function moveCur(dt){let dx=0,dy=0,now=Date.now();
 const sp=k=>{const t=held[k];if(!t)return 0;const e=now-t;return e<300?30:e<800?75:e<1500?130:190};
 dx+=sp('ArrowRight')+sp('d')-sp('ArrowLeft')-sp('a');dy+=sp('ArrowDown')+sp('s')-sp('ArrowUp')-sp('w');
 if(zone==='field'&&(held.ArrowDown||held.s)&&cy>=H-2&&Date.now()-(held.ArrowDown||held.s)>250){delete held.ArrowDown;delete held.s;goBar();return}
 if(dx||dy){mouseMode=false;cx=Math.max(0,Math.min(W-1,cx+dx*dt/1000));cy=Math.max(0,Math.min(H-1,cy+dy*dt/1000))}}
function sprFor(w){let k='walk',f=0;const t=w.t;
 if(w.st==='fall'||w.st==='fly')k='fall';else if(w.st==='climb'){k='climb';f=(t>>2)&1}else if(w.st==='block')k='block';else if(w.st==='build'){k='build';f=(t>>2)&1}else if(w.st==='bash'){k='bash';f=(t>>1)&1}else if(w.st==='dig'){k='dig';f=(t>>2)&1}else if(w.st==='exit')k='exit';
 else f=(t>>2)&1;
 const a=SPR[(w.hat||0)%5][k][w.dir<0?0:1];return a[Math.min(f,a.length-1)]}
function deco(){const E=L.E,X=L.X;lx.fillStyle='#6b4423';lx.fillRect(E[0]-9,E[1]-7,18,3);lx.fillStyle='#3d2812';lx.fillRect(E[0]-9,E[1]-4,18,1);lx.fillRect(E[0]-9,E[1]-8,2,4);lx.fillRect(E[0]+7,E[1]-8,2,4);
 lx.fillStyle='#4b2e14';lx.fillRect(X[0]-8,X[1]-18,16,18);lx.fillStyle='#c0392b';lx.fillRect(X[0]-9,X[1]-21,18,3);lx.fillRect(X[0]-7,X[1]-23,14,2);lx.fillRect(X[0]-5,X[1]-25,10,2);
 lx.fillStyle='#1b1020';lx.fillRect(X[0]-5,X[1]-15,10,15);lx.fillStyle=(tick>>3)&1?'#ffd45a':'#ff9a3c';lx.fillRect(X[0]-8,X[1]-12,2,3);lx.fillRect(X[0]+6,X[1]-12,2,3);
 lx.fillStyle='#ffd45a';lx.fillRect(X[0]-1,X[1]-22,2,1)}
function drawPortals(){for(const p of L.P||[]){[[p[0],p[1],'#5ec2ff'],[p[2],p[3],'#ffa24a']].forEach(([x,y,c],i)=>{const ph=tick/6+i*3;lx.fillStyle=c;lx.globalAlpha=.35;lx.fillRect(x-4,y-13,8,14);lx.globalAlpha=1;for(let k=0;k<6;k++){const a=ph+k*1.047;lx.fillRect(Math.round(x+Math.cos(a)*3.2),Math.round(y-6+Math.sin(a)*6),1,1)}lx.fillStyle='#fff';lx.fillRect(x,y-6+Math.round(Math.sin(ph)*2),1,1)})}}
function prevTool(){const ok=cnt[sel]>0,X=Math.round(cx)*2,Y=Math.round(cy)*2;ctx.lineWidth=2;ctx.strokeStyle=ok?'#ffe14a':'#ff8a8a';
 if(sel==='boom'){ctx.save();ctx.beginPath();ctx.rect(0,0,640,Y+8);ctx.clip();ctx.beginPath();ctx.arc(X,Y,26,0,6.2832);ctx.stroke();ctx.restore();ctx.beginPath();ctx.moveTo(X-25,Y+8);ctx.lineTo(X+25,Y+8);ctx.stroke()}
 else if(sel==='plank'){ctx.strokeRect(X-34,Y,68,6)}
 else{const ty=snapT(cx,cy);if(ty>=0){ctx.strokeStyle=ok?'#7dffb0':'#ff8a8a';ctx.strokeRect(X-14,(ty-3)*2,28,6);ctx.beginPath();ctx.moveTo(X,Y);ctx.lineTo(X,(ty-3)*2);ctx.stroke()}}}
function render(t){ctx.imageSmoothingEnabled=false;
 drawBg(t||0);
 if(!L)return;
 flush();lx.clearRect(0,0,W,H);lx.drawImage(tcv,0,0);deco();drawPortals();
 for(const q of tramps){const sq=q.cd>tick+8?1:0;lx.fillStyle='#444';lx.fillRect(q.x-7,q.y-1,2,2);lx.fillRect(q.x+5,q.y-1,2,2);lx.fillStyle='#ff4d6d';lx.fillRect(q.x-7,q.y-3+sq,14,2);lx.fillStyle='#ffe14a';for(let i=-6;i<7;i+=4)lx.fillRect(q.x+i,q.y-3+sq,2,1)}
 for(const b of bombs){lx.fillStyle=b.f<8&&(tick&1)?'#ffffff':'#ff5aa5';lx.fillRect(b.x-2,b.y-4,5,5);lx.fillStyle='#ffe14a';lx.fillRect(b.x-1,b.y-3,1,1);lx.fillStyle=(tick&2)?'#ffe14a':'#ff7a2a';lx.fillRect(b.x,b.y-6,1,2)}
 for(const w of ws){if(w.st==='dead'||w.st==='gone')continue;const c=sprFor(w);
  if(w.st==='exit'){const hop=Math.round(Math.sin(w.t/14*Math.PI)*5);lx.globalAlpha=Math.max(.15,1-w.t/16);lx.drawImage(c,w.x-4,w.y-9-hop);lx.globalAlpha=1;continue}
  lx.drawImage(c,w.x-4,w.y-9);
  if(w.floating){lx.fillStyle='#ff6b6b';lx.fillRect(w.x-5,w.y-14,10,1);lx.fillRect(w.x-4,w.y-15,8,1);lx.fillRect(w.x-2,w.y-16,4,1);lx.fillStyle='#fff';lx.fillRect(w.x,w.y-13,1,4)}
  if(w.climber||w.floater){lx.fillStyle=w.climber&&w.floater?'#8fe3ff':w.climber?'#9be37a':'#ff9aa8';lx.fillRect(w.x-1,w.y-11,2,1)}}
 for(const p of ptc){lx.fillStyle=p.c;lx.fillRect(Math.round(p.x),Math.round(p.y),1,1)}
 if(sh>.6){ctx.save();ctx.translate((Math.random()-.5)*sh,(Math.random()-.5)*sh)}
 ctx.drawImage(lcv,0,0,640,320);
 if(sh>.6)ctx.restore();
 ctx.font='bold 13px system-ui,sans-serif';ctx.textAlign='center';
 for(const b of bub){const bw=b.w+12,X=Math.max(bw/2,Math.min(640-bw/2,b.x*2)),Y=Math.max(20,b.y*2-b.t*.5);ctx.fillStyle='rgba(255,255,255,.96)';ctx.fillRect(X-bw/2,Y-18,bw,18);ctx.fillRect(X-3,Y,6,4);ctx.fillStyle='#2a1c40';ctx.fillText(b.s,X,Y-5)}
 if(zone==='field'&&!over){
  if(TOOLS[sel])prevTool();
  else{const w=pick(cx,cy,11,sel);if(w){const ok=canApply(w,sel)&&(w.st==='block'||cnt[sel]>0);ctx.strokeStyle=ok?'#ffe14a':'#ff8a8a';ctx.lineWidth=2;ctx.strokeRect((w.x-6)*2,(w.y-12)*2,24,26)}}
  const X=cx*2,Y=cy*2;ctx.strokeStyle='#fff';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(X-11,Y);ctx.lineTo(X-4,Y);ctx.moveTo(X+4,Y);ctx.lineTo(X+11,Y);ctx.moveTo(X,Y-11);ctx.lineTo(X,Y-4);ctx.moveTo(X,Y+4);ctx.lineTo(X,Y+11);ctx.stroke();ctx.strokeStyle='#000';ctx.lineWidth=1;ctx.strokeRect(X-1,Y-1,2,2)}
 if(paused&&zone!=='menu'){ctx.fillStyle='rgba(0,0,0,.18)';ctx.fillRect(0,0,640,320);ctx.fillStyle='#fff';ctx.font='bold 22px system-ui';ctx.textAlign='center';ctx.fillText('⏸ Pause – du kannst trotzdem Fähigkeiten geben',320,306)}}
function frame(t){const dt=Math.min(100,t-last);last=t;moveCur(dt);
 if(L&&!paused&&(zone!=='menu'||over)){acc+=dt*speed;while(acc>=33.3){acc-=33.3;if(over)fx();else step()}}else acc=0;
 if(hintT&&Date.now()>hintT){$('#hint').classList.remove('on');hintT=0}
 render(t);requestAnimationFrame(frame)}
function fit(){const st=$('#stage'),w=st.clientWidth,h=st.clientHeight;let cw=w,ch=w/2;if(ch>h){ch=h;cw=h*2}cv.style.width=Math.floor(cw)+'px';cv.style.height=Math.floor(ch)+'px'}
addEventListener('resize',fit);fit();try{new ResizeObserver(fit).observe($('#stage'))}catch(e){}
window.WG={add:l=>{LV.push(l);return LV.length-1},tool:(s,x,y)=>useTool(s,x,y),step:n=>{for(let i=0;i<(n||1);i++)step()},load:loadLevel,apply:(s,i)=>doApply(ws[i],s),ws:()=>ws.map(w=>({id:w.id,hat:w.hat,x:w.x,y:w.y,st:w.st,dir:w.dir,fd:w.fd,climber:w.climber,floater:w.floater})),st:()=>({cx:Math.round(cx*10)/10,cy:Math.round(cy*10)/10,bombs:bombs.length,tramps:tramps.length,tick,spawned,saved,lost,over,cnt:Object.assign({},cnt),zone,sel,lv}),n:LV.length,menu:mainMenu};
setTheme(0);mainMenu();requestAnimationFrame(frame);
</script></body></html>
"""
