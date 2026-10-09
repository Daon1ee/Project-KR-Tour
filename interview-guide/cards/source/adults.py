import gen
from gen import icons,S,svg,CSS
icons['story']=f'<path d="M50 90 L50 54" {S}/><path d="M50 54 Q50 40 30 30" fill="none" {S}/><path d="M50 54 Q50 40 70 30" fill="none" {S}/><rect x="12" y="14" width="34" height="18" rx="4" fill="#cfe3ef" {S}/><rect x="54" y="14" width="34" height="18" rx="4" fill="#f3d9b1" {S}/><line x1="19" y1="23" x2="39" y2="23" {S}/><line x1="61" y1="23" x2="81" y2="23" {S}/><circle cx="50" cy="90" r="5" fill="#6b8e9e" {S}/>'
icons['detective']=f'<rect x="14" y="16" width="46" height="60" rx="4" fill="#f4ecd8" {S}/><line x1="22" y1="30" x2="52" y2="30" {S}/><line x1="22" y1="42" x2="52" y2="42" {S}/><line x1="22" y1="54" x2="40" y2="54" {S}/><circle cx="64" cy="58" r="16" fill="#dff1f7" {S}/><line x1="76" y1="70" x2="90" y2="86" stroke="#3b3b3b" stroke-width="6" stroke-linecap="round"/>'
icons['strategy']=f'<rect x="10" y="20" width="80" height="60" rx="5" fill="#e8efe4" {S}/><path d="M10 50 L90 50 M50 20 L50 80" fill="none" stroke="#3b3b3b" stroke-width="1.8"/><circle cx="30" cy="35" r="8" fill="#6b8e9e" {S}/><rect x="60" y="58" width="16" height="16" rx="2" fill="#c98b5b" {S}/><path d="M64 30 L74 40 M74 30 L64 40" {S}/>'
cards=[('story','A. 이야기 선택형','그 시대를 살던 평범한 사람의 하루를 따라가며 선택을 하는 게임','예: 아침에 무엇을 챙기고 누구에게 말을 건넬지 고르는 하루','#4a7c8f'),
('giwa','B. 복원·수집형','사라진 유물이나 장소를 찾아 하나씩 복원하는 게임','예: 흩어진 조각을 모아 옛 건물을 다시 세움 (6세용 컨셉과 이어짐)','#5b8c5a'),
('detective','C. 퍼즐·추리형','기록과 단서를 모아 사건의 전말을 추리하는 게임','예: 옛 편지와 사진을 맞춰 보며 무슨 일이 있었는지 알아 감','#8a6bb0'),
('vr','D. 몰입 체험형 (VR)','그 시대의 장소를 직접 걷고 둘러보는 체험','예: 복원된 거리를 걸으며 안내를 듣는 시간 여행','#3d5a98'),
('strategy','E. 전략·시뮬레이션형','결정과 자원 관리를 통해 그 시대의 선택을 이해하는 게임','논란이 가장 클 수 있어 선을 확인하는 용도로 보여 줌','#b0654a')]
def card(i,t,d,e,c):
    return f'<div class="card pc" style="--c:{c}"><span class="tag">성인용 방식 카드</span><div style="width:24mm;height:24mm;margin-top:2mm">{svg(i)}</div><div class="ko">{t}</div><div class="desc">{d}</div><div class="desc" style="color:#666;font-size:8pt;margin-top:1mm">{e}</div></div>'
blank='<div class="card pc" style="--c:#999"><span class="tag">빈 카드</span><div class="ko" style="margin-top:20mm">참가자가 말한 방식</div><div class="desc" style="text-align:center;color:#888">직접 쓰거나 그려 주세요</div></div>'
html=f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'+gen.page([card(*c) for c in cards]+[blank]*4)+'</body></html>'
open('adult_cards.html','w').write(html)
rows=''.join(f'<tr><td><b>{c[1]}</b></td><td></td><td></td><td></td><td></td></tr>' for c in cards)+'<tr><td><b>참가자가 말한 방식</b></td><td></td><td></td><td></td><td></td></tr>'
sheet=f'''<html><head><meta charset="utf-8"><style>{CSS}@page{{size:11in 8.5in}}
table{{border-collapse:collapse;width:100%}}td,th{{border:1.5px solid #888;padding:8px;font-size:11pt}}th{{background:#f0f0f0}}td{{height:16mm}}
.w{{padding:0.5in}}</style></head><body><div class="w"><h1>성인용 방식 카드 반응 기록 · 참가자 ____________ (집단: 한국인 / 교포 2세 / 일반)</h1>
<p class="note">카드를 한 장씩 보여 주고 "어떤 게 가장 의미 있고, 어떤 게 불편할 것 같나요?"라고 묻습니다. 말한 대로 체크하고 이유를 한 줄로 적으세요. 전투나 폭력 중심 방식은 참가자가 먼저 말할 때만 적습니다.</p>
<table><tr><th style="width:24%">카드</th><th style="width:11%">의미 있음</th><th style="width:11%">불편함</th><th style="width:11%">잘 모르겠음</th><th>이유 · 한 줄 메모</th></tr>{rows}</table>
<p class="note" style="margin-top:6mm">가장 의미 있는 1장: __________ &nbsp; 선을 넘는다고 한 지점: ______________________________</p></div></body></html>'''
open('adult_sheet.html','w').write(sheet)
from playwright.sync_api import sync_playwright
import os
d=os.getcwd()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for n in ['adult_cards','adult_sheet']:
        pg=b.new_page(); pg.goto(f'file://{d}/{n}.html'); pg.pdf(path=f'{n}.pdf',prefer_css_page_size=True,print_background=True)
    b.close()
