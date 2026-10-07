import sys
S='stroke="#3b3b3b" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'
icons={
'puzzle':f'<rect x="18" y="30" width="32" height="32" rx="4" fill="#ffd166" {S}/><circle cx="34" cy="26" r="7" fill="#ffd166" {S}/><rect x="50" y="30" width="32" height="32" rx="4" fill="#06d6a0" {S}/><circle cx="86" cy="46" r="6" fill="#06d6a0" {S}/><rect x="34" y="62" width="32" height="26" rx="4" fill="#ef8354" {S}/><circle cx="50" cy="62" r="7" fill="#ef8354" {S}/>',
'adventure':f'<circle cx="75" cy="25" r="11" fill="#ffd166" {S}/><path d="M8 85 L40 35 L62 68 L74 52 L94 85Z" fill="#7bc67b" {S}/><path d="M40 35 L32 48 L40 45 L47 48Z" fill="#fff" {S}/><line x1="40" y1="35" x2="40" y2="18" {S}/><path d="M40 18 L54 23 L40 28Z" fill="#ef476f" {S}/>',
'build':f'<rect x="14" y="62" width="34" height="26" rx="3" fill="#ef476f" {S}/><rect x="52" y="62" width="34" height="26" rx="3" fill="#4cc9f0" {S}/><rect x="30" y="36" width="34" height="26" rx="3" fill="#ffd166" {S}/><path d="M36 36 L47 14 L58 36Z" fill="#06d6a0" {S}/>',
'character':f'<path d="M22 40 L26 14 L44 30Z" fill="#f4a261" {S}/><path d="M78 40 L74 14 L56 30Z" fill="#f4a261" {S}/><circle cx="50" cy="56" r="33" fill="#f9c784" {S}/><circle cx="38" cy="52" r="4" fill="#3b3b3b"/><circle cx="62" cy="52" r="4" fill="#3b3b3b"/><path d="M42 66 Q50 74 58 66" fill="none" {S}/><circle cx="30" cy="62" r="5" fill="#ffadad"/><circle cx="70" cy="62" r="5" fill="#ffadad"/><path d="M40 90 L50 82 L60 90 L50 94Z" fill="#ef476f" {S}/>',
'ondol':f'<rect x="8" y="62" width="84" height="28" rx="3" fill="#e9a35b" {S}/><line x1="36" y1="62" x2="36" y2="90" {S}/><line x1="64" y1="62" x2="64" y2="90" {S}/><path d="M24 54 Q18 44 24 34 Q30 24 24 14" fill="none" stroke="#ef476f" stroke-width="4" stroke-linecap="round"/><path d="M50 54 Q44 44 50 34 Q56 24 50 14" fill="none" stroke="#f77f00" stroke-width="4" stroke-linecap="round"/><path d="M76 54 Q70 44 76 34 Q82 24 76 14" fill="none" stroke="#ef476f" stroke-width="4" stroke-linecap="round"/>',
'giwa':f'<path d="M4 58 Q50 8 96 58 L88 66 Q50 26 12 66Z" fill="#5c6b7a" {S}/><path d="M14 66 Q50 30 86 66 L80 88 L20 88Z" fill="#8d99ae" {S}/><path d="M24 76 Q50 56 76 76M26 86 Q50 68 74 86" fill="none" stroke="#fff" stroke-width="2.5"/><path d="M4 58 Q-2 52 6 48M96 58 Q102 52 94 48" fill="none" {S}/>',
'tteok':f'<rect x="14" y="62" width="72" height="22" rx="11" fill="#ffffff" {S}/><rect x="20" y="42" width="60" height="22" rx="11" fill="#ffadc6" {S}/><rect x="26" y="22" width="48" height="22" rx="11" fill="#9be59b" {S}/>',
'kimchi':f'<rect x="22" y="38" width="56" height="50" rx="10" fill="#e8e8e8" {S}/><rect x="18" y="28" width="64" height="14" rx="5" fill="#ef476f" {S}/><path d="M30 28 Q34 14 42 22 Q50 8 58 22 Q66 14 70 28Z" fill="#f4511e" {S}/><path d="M32 56 Q50 48 68 56M32 70 Q50 62 68 70" fill="none" stroke="#ef476f" stroke-width="3"/>',
'tablet':f'<rect x="12" y="20" width="76" height="60" rx="8" fill="#4cc9f0" {S}/><rect x="19" y="27" width="62" height="46" rx="3" fill="#fff" {S}/><path d="M50 36 L54 46 L64 47 L56 54 L58 64 L50 59 L42 64 L44 54 L36 47 L46 46Z" fill="#ffd166" {S}/>',
'tv':f'<rect x="8" y="20" width="84" height="54" rx="5" fill="#8d99ae" {S}/><rect x="14" y="26" width="72" height="42" rx="3" fill="#bde0fe" {S}/><circle cx="36" cy="46" r="8" fill="#ffd166" {S}/><path d="M14 68 L40 52 L56 62 L70 50 L86 62 L86 68Z" fill="#7bc67b"/><line x1="36" y1="74" x2="30" y2="86" {S}/><line x1="64" y1="74" x2="70" y2="86" {S}/>',
'vr':f'<path d="M8 44 Q50 22 92 44" fill="none" stroke="#3b3b3b" stroke-width="5" stroke-linecap="round"/><rect x="14" y="40" width="72" height="38" rx="14" fill="#6c63ff" {S}/><circle cx="36" cy="59" r="9" fill="#fff" {S}/><circle cx="64" cy="59" r="9" fill="#fff" {S}/><circle cx="36" cy="59" r="4" fill="#3b3b3b"/><circle cx="64" cy="59" r="4" fill="#3b3b3b"/>',
'happy':f'<circle cx="50" cy="50" r="38" fill="#ffe066" {S}/><circle cx="37" cy="42" r="4.5" fill="#3b3b3b"/><circle cx="63" cy="42" r="4.5" fill="#3b3b3b"/><path d="M30 58 Q50 82 70 58Z" fill="#fff" {S}/>',
'okay':f'<circle cx="50" cy="50" r="38" fill="#bde0fe" {S}/><circle cx="37" cy="42" r="4.5" fill="#3b3b3b"/><circle cx="63" cy="42" r="4.5" fill="#3b3b3b"/><line x1="34" y1="65" x2="66" y2="65" {S}/>',
'scared':f'<circle cx="50" cy="50" r="38" fill="#d0c4f7" {S}/><circle cx="37" cy="42" r="6" fill="#fff" {S}/><circle cx="63" cy="42" r="6" fill="#fff" {S}/><circle cx="37" cy="43" r="2.5" fill="#3b3b3b"/><circle cx="63" cy="43" r="2.5" fill="#3b3b3b"/><path d="M30 38 L44 32M70 38 L56 32" fill="none" {S}/><path d="M36 70 Q43 60 50 70 Q57 60 64 70" fill="none" {S}/>',
'haetae':f'<path d="M20 40 Q16 14 34 20 L40 34Z" fill="#c9a66b" {S}/><path d="M80 40 Q84 14 66 20 L60 34Z" fill="#c9a66b" {S}/><circle cx="50" cy="56" r="34" fill="#e0c28a" {S}/><circle cx="37" cy="50" r="5" fill="#3b3b3b"/><circle cx="63" cy="50" r="5" fill="#3b3b3b"/><ellipse cx="50" cy="64" rx="9" ry="6" fill="#fff" {S}/><path d="M44 74 Q50 80 56 74" fill="none" {S}/><path d="M50 22 L46 12 L54 12Z" fill="#ffd166" {S}/>',
'gate':f'<rect x="10" y="48" width="80" height="40" fill="#b5651d" {S}/><path d="M34 88 L34 62 Q50 46 66 62 L66 88Z" fill="#3b2a1a" {S}/><path d="M2 48 Q50 14 98 48Z" fill="#5c6b7a" {S}/><path d="M16 38 Q50 14 84 38" fill="none" stroke="#fff" stroke-width="2"/>',
'book':f'<path d="M50 30 L50 84 Q30 74 10 80 L10 26 Q30 20 50 30Z" fill="#fff" {S}/><path d="M50 30 L50 84 Q70 74 90 80 L90 26 Q70 20 50 30Z" fill="#ffd166" {S}/><path d="M36 54 L50 36 L64 54Z" fill="#06d6a0" {S}/><path d="M42 54 L50 44 L58 54Z" fill="#ef476f"/>',
}
def svg(k,sz=100): return f'<svg viewBox="0 0 100 100" width="{sz}%" height="{sz}%">{icons[k]}</svg>'
CSS='''
@page{size:Letter;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:"Noto Sans CJK KR","Noto Sans CJK SC",sans-serif;color:#2b2b2b}
.page{width:8.5in;height:11in;padding:0.5in 0.62in;display:grid;grid-template-columns:repeat(3,63mm);grid-auto-rows:88mm;justify-content:center;align-content:center;page-break-after:always}
.card{width:63mm;height:88mm;border:1px dashed #999;border-radius:0;padding:5mm;display:flex;flex-direction:column;align-items:center;justify-content:space-between;text-align:center;outline:0}
.card .ic{width:44mm;height:44mm;margin-top:3mm}
.card .ko{font-size:15pt;font-weight:700}
.card .en{font-size:8pt;color:#666}
.tag{font-size:7pt;letter-spacing:.5px;color:#fff;background:var(--c);border-radius:4px;padding:1px 6px;align-self:flex-start}
.cut{position:absolute}
h1{font-size:12pt}
.pc .ko{font-size:13pt;margin:2mm 0}
.pc .desc{font-size:9pt;line-height:1.45;text-align:left;margin-top:2mm}
.pc .big{font-size:26pt;font-weight:800;color:var(--c)}
.pc{justify-content:flex-start}
.text-only .big{margin-top:6mm}
.warn{font-size:7pt;color:#a33;margin-top:auto}
.tl{width:11in;height:8.5in;padding:0.5in;page-break-after:always;display:flex;flex-direction:column}
.tl h1{font-size:16pt;margin:0 0 4mm}
.tl .row{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:3mm}
.tl .col{border:2px dashed #888;border-radius:10px;padding:4mm;display:flex;flex-direction:column;align-items:center}
.tl .col b{font-size:15pt}
.tl .col span{font-size:9pt;color:#666}
.tl .arrow{height:6mm;background:linear-gradient(90deg,#9be59b,#ffd166,#ef8354,#9b8cff);border-radius:3mm;margin:4mm 0}
.note{font-size:8pt;color:#555}
'''
def page(cards): return '<div class="page">'+''.join(cards)+'</div>'
def kid(k,ko,en,c,tag): return f'<div class="card" style="--c:{c}"><span class="tag">{tag}</span><div class="ic">{svg(k)}</div><div><div class="ko">{ko}</div><div class="en">{en}</div></div></div>'
kids=[]
play=[('puzzle','퍼즐 맞추기','Puzzle'),('adventure','모험·탐험','Adventure'),('build','만들기·쌓기','Build'),('character','캐릭터 돌보기·꾸미기','Care & dress up')]
obj=[('ondol','따뜻한 온돌 바닥','Warm ondol floor'),('giwa','지붕 위의 기와','Roof tiles (giwa)'),('tteok','떡','Rice cake (tteok)'),('kimchi','김치','Kimchi')]
dev=[('tablet','태블릿','Tablet'),('tv','TV','TV'),('vr','VR 헤드셋','VR headset')]
face=[('happy','기뻐요','Happy'),('okay','괜찮아요','Okay'),('scared','무서워요','Scared')]
kc=[kid(k,a,b,'#ef8354','놀이') for k,a,b in play]+[kid(k,a,b,'#06a77d','한국 물건·음식') for k,a,b in obj]+[kid(k,a,b,'#4361ee','기기') for k,a,b in dev]+[kid(k,a,b,'#9b5de5','내 마음') for k,a,b in face]
# faces twice (spare) -> fill page 2
kc+= [kid(k,a,b,'#9b5de5','내 마음') for k,a,b in face]
pages=[page(kc[:9]),page(kc[9:18])]
kidhtml=f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open('kids.html','w').write(kidhtml)
def pc(label,ko,desc,c,icon=None,warn=None):
    ic=f'<div style="width:26mm;height:26mm;margin-top:2mm">{svg(icon)}</div>' if icon else f'<div class="big">{label}</div>'
    w=f'<div class="warn">{warn}</div>' if warn else ''
    return f'<div class="card pc" style="--c:{c}"><span class="tag">{"컨셉 카드" if label in "ABC" and len(label)==1 else "시기 정하기"}</span>{ic}<div class="ko">{ko}</div><div class="desc">{desc}</div>{w}</div>'
concept=[pc('A','사라진 조각 찾기','해태와 함께 광화문의 사라진 조각을 찾아 주는 밝고 짧은 게임. 무서운 장면이 없고, 놀고 나면 부모님이 이야기를 나눌 수 있도록 짧은 안내가 있어요.','#ef8354','haetae'),
 pc('B','물건으로 만나는 한국 역사','온돌, 기와, 음식 같은 물건에 담긴 이야기를 놀이로 만나요.','#06a77d','ondol'),
 pc('C','입체 이야기책','펼치고 당기면 움직이는 입체 이야기책 (종이 또는 디지털).','#4361ee','book')]
for c in concept: pass
timing=[('온돌·기와 같은 옛 물건','집과 생활 속 물건에 담긴 이야기','#06a77d','giwa',None),
('한국 음식','떡, 김치 같은 음식에 담긴 이야기','#06a77d','tteok',None),
('명절과 풍습','설날, 추석 같은 명절의 유래','#06a77d','book',None),
('궁궐과 왕 이야기','광화문 같은 궁궐과 그곳의 이야기','#ef8354','gate',None),
('일제강점기','아픈 역사','#6b6b6b',None,'글자 카드 · 아이에게 보여 주지 않음'),
('한국전쟁','아픈 역사','#6b6b6b',None,'글자 카드 · 아이에게 보여 주지 않음')]
tc=[]
for ko,d,c,ic,w in timing:
    if ic: tc.append(pc('T',ko,d,c,ic))
    else:
        h=pc('T',ko,d,c,None,w).replace('<div class="big">T</div>','<div style="height:26mm;margin-top:2mm;display:flex;align-items:center;font-size:30pt;color:#6b6b6b">·  ·  ·</div>')
        tc.append(h)
blank=lambda:'<div class="card pc" style="--c:#999"><span class="tag">빈 카드</span><div class="ko" style="margin-top:20mm">부모님이 추가하는 카드</div><div class="desc" style="text-align:center;color:#888">직접 쓰거나 그려 주세요</div></div>'
tc+= [blank(),blank(),blank()]
parent=page(concept+tc[:6])+page(tc[6:])
cols=[('6세 전후','지금 바로'),('8~9세',''),('10~12세',''),('13세 이상',''),('아직 모르겠다','더 생각해 볼래요')]
tl='<div class="tl"><h1>시기 정하기 시간선 &nbsp;<span class="note">카드를 알맞은 칸에 놓고, 놓을 때마다 "왜 그 시기인가요?"</span></h1><div class="arrow"></div><div class="row">'+''.join(f'<div class="col"><b>{a}</b><span>{b}</span></div>' for a,b in cols)+'</div></div>'
open('timeline.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}@page{{size:11in 8.5in}}</style></head><body>{tl}</body></html>')
open('parents.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{parent}</body></html>')
