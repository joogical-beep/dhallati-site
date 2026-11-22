# Live homepage pieces: multilingual hero, real search over found items, journey, trust
PHRASES = ["ضاع منك شيء؟","Lost something?","کچھ گم ہو گیا؟","कुछ खो गया?","কিছু হারিয়েছেন?","എന്തെങ്കിലും നഷ്ടപ്പെട്ടോ?","ஏதாவது தொலைந்ததா?","ఏదైనా పోగొట్టుకున్నారా?","May nawala ka ba?","Kehilangan sesuatu?","केही हरायो?","යමක් නැති වුණාද?","የጠፋብዎት ነገር አለ?","څه مو ورک شوي؟"]
CSS = """
.live{position:relative;padding:40px 0 10px;overflow:hidden}
.ask{text-align:right;unicode-bidi:isolate;font-size:clamp(2.3rem,7vw,4.4rem);line-height:1.15;color:var(--butter);margin:0;min-height:1.3em;font-weight:700;transition:opacity .45s,transform .45s}
.ask.out{opacity:0;transform:translateY(10px)}
.sub{color:var(--cream);font-size:1.15rem;max-width:46ch;margin:12px 0 22px}
.finder{background:var(--cream);color:#2F2924;border-radius:24px;padding:14px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6);max-width:720px}
.frow{display:flex;gap:8px;flex-wrap:wrap}
.frow input{flex:1 1 240px;min-width:0;font:inherit;font-size:1.1rem;padding:14px 16px;border-radius:16px;border:1px solid #d8c9ae;background:#fff;color:#2F2924}
.frow select{font:inherit;padding:14px;border-radius:16px;border:1px solid #d8c9ae;background:#fff;color:#2F2924}
.frow button{font:inherit;font-weight:700;padding:14px 22px;border:0;border-radius:16px;background:#2F2924;color:var(--butter);cursor:pointer}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chips button{font:inherit;font-size:.9rem;padding:6px 12px;border-radius:99px;border:1px solid #d8c9ae;background:transparent;color:#5a4c3f;cursor:pointer}
.chips button[aria-pressed=true]{background:#2F2924;color:var(--butter);border-color:#2F2924}
.res{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px;margin-top:12px}
.res a{display:block;background:#fff;border-radius:16px;overflow:hidden;text-decoration:none;color:#2F2924;border:1px solid #eadfca}
.res img,.res .ph{width:100%;aspect-ratio:4/3;object-fit:cover;background:#efe4cf;display:grid;place-items:center;font-size:2rem}
.res div.t{padding:8px 10px;font-weight:600}.res small{display:block;color:#7a6b5c;font-weight:400}
.none{margin-top:12px;padding:14px;border-radius:16px;background:#fff;color:#2F2924}
.none a{color:#2F2924;font-weight:700}
.journey{position:relative;margin:56px 0 10px}
.track{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;position:relative}
.track::before{content:"";position:absolute;top:34px;inset-inline:8%;height:2px;background:repeating-linear-gradient(90deg,var(--line) 0 8px,transparent 8px 14px)}
.st{position:relative;text-align:center;padding:0 4px}
.st i{display:grid;place-items:center;width:68px;height:68px;margin:0 auto 10px;border-radius:50%;background:var(--card);border:1px solid var(--line);font-style:normal;font-size:1.7rem;position:relative;z-index:1}
.st b{display:block;color:var(--cream)}.st span{color:var(--soft);font-size:.92rem}
.tag{position:absolute;top:14px;inset-inline-start:8%;width:40px;height:40px;border-radius:12px;background:var(--butter);display:grid;place-items:center;z-index:2;animation:travel 9s ease-in-out infinite}
@keyframes travel{0%,8%{inset-inline-start:8%}30%,38%{inset-inline-start:33%}60%,68%{inset-inline-start:58%}90%,100%{inset-inline-start:84%}}
@media (max-width:640px){.track{grid-template-columns:1fr 1fr;row-gap:22px}.track::before,.tag{display:none}}
@media (prefers-reduced-motion:reduce){.tag{animation:none}.ask{transition:none}}
.trust{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:14px}
.trust div{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px}
.trust b{display:block;color:var(--butter);margin-bottom:4px}
.badges{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.badges span{border:1px solid var(--line);border-radius:99px;padding:6px 14px;color:var(--soft);font-size:.92rem}
.langs{display:flex;gap:16px;overflow:hidden;white-space:nowrap;color:var(--soft);margin-top:10px;mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
"""
def hero(APP, WEBAPP):
    import json
    return f"""<section class="live"><h1 class="ask" id="ask" aria-live="polite">ضاع منك شيء؟</h1>
<p class="sub">ابحث الحين بين الأغراض اللي سجّلتها الجهات والمنشآت. وإذا ما لقيته، بلّغ عنه وننبهك أول ما ينلقى.</p>
<form class="finder" id="finder" role="search"><div class="frow">
<input id="fq" placeholder="اكتب وش ضاع منك: جوال أسود، محفظة بنية…" aria-label="وش ضاع منك">
<select id="fc" aria-label="المدينة"><option value="riyadh">الرياض</option><option value="jeddah">جدة</option><option value="makkah">مكة</option><option value="dammam">الدمام</option><option value="abha">أبها</option></select>
<button type="submit">ابحث</button></div>
<div class="chips" id="chips"></div><div id="out"></div></form>
<div class="badges"><span>14 لغة</span><span>سؤال تحقق قبل التسليم</span><span>رقمك مخفي</span><span>تطبيق سعودي</span></div>
</section>
<script>window.__PH={json.dumps(PHRASES, ensure_ascii=False)};window.__APP="{APP}";window.__WEB="{WEBAPP}";</script>"""

JOURNEY = """<section class="journey" id="how"><h2>رحلة الغرض من الضياع إلى صاحبه</h2>
<div class="track"><div class="tag" aria-hidden="true">🏷️</div>
<div class="st"><i>📸</i><b>يُسجَّل</b><span>الموظف يصوّره ويكتب وصفه في ثوانٍ</span></div>
<div class="st"><i>🔎</i><b>يُطابَق</b><span>صاحبه يبحث من جواله ويلقاه</span></div>
<div class="st"><i>🔐</i><b>يُتحقَّق</b><span>سؤال ما يعرفه إلا صاحبه</span></div>
<div class="st"><i>🤝</i><b>يُسلَّم</b><span>ويرجع لصاحبه، والتسليم موثّق</span></div></div></section>
<h2>ليش الناس تثق في ضالّتي</h2>
<div class="trust"><div><b>ما يستلمه إلا صاحبه</b>سؤال تحقق عن تفصيلة ما يعرفها غيره.</div>
<div><b>رقمك ما يظهر</b>التواصل داخل التطبيق، بدون أرقام جوالات.</div>
<div><b>بلغة كل زائر</b>14 لغة تخدم الزوار والعمالة والسياح.</div>
<div><b>للجهة سجل موحّد</b>بدل الدفتر الورقي والاتصالات المتكررة.</div></div>
<div class="langs" aria-hidden="true">""" + "".join(f"<span>{p}</span>" for p in PHRASES) + "</div>"

JS = """<script type="module">
const PH=window.__PH;let i=0;const ask=document.getElementById("ask");
if(!matchMedia("(prefers-reduced-motion: reduce)").matches)setInterval(()=>{ask.classList.add("out");setTimeout(()=>{i=(i+1)%PH.length;ask.textContent=PH[i];ask.classList.remove("out")},450)},2600);
const U="https://efhmdxoqjbwkyxhievyv.supabase.co",K="sb_publishable_IE1VnqygsApInZcMhZ4oeA_Ntygg89E";
const CATS={phone:"جوال",wallet:"محفظة",bag:"حقيبة",keys:"مفاتيح",docs:"أوراق ووثائق",glasses:"نظارة",watch:"ساعة",kids:"أغراض أطفال",other:"أخرى"};
const ICO={phone:"📱",wallet:"👛",bag:"👜",keys:"🔑",docs:"📄",glasses:"👓",watch:"⌚",kids:"🧸",other:"📦"};
let cat="";const chips=document.getElementById("chips");
for(const [k,v] of Object.entries(CATS)){const b=document.createElement("button");b.type="button";b.textContent=ICO[k]+" "+v;b.setAttribute("aria-pressed","false");
 b.onclick=()=>{cat=cat===k?"":k;[...chips.children].forEach(c=>c.setAttribute("aria-pressed","false"));if(cat)b.setAttribute("aria-pressed","true");run()};chips.append(b)}
const out=document.getElementById("out");const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const norm=s=>String(s||"").toLowerCase().replace(/[ً-ْـ]/g,"").replace(/[أإآ]/g,"ا").replace(/ة/g,"ه").replace(/ى/g,"ي");
async function run(){const q=document.getElementById("fq").value.trim(),city=document.getElementById("fc").value;
 out.innerHTML='<div class="none">جاري البحث…</div>';
 let url=U+"/rest/v1/items?select=code,category,title,spot,photo_path,found_on,venues(name_ar)&status=neq.done&city=eq."+city+"&order=created_at.desc&limit=60";
 if(cat)url+="&category=eq."+cat;
 try{const r=await fetch(url,{headers:{apikey:K,Authorization:"Bearer "+K}});let d=await r.json();if(!Array.isArray(d))d=[];
  if(q){const w=norm(q).split(/\\s+/).filter(x=>x.length>1);d=d.filter(it=>{const t=norm(it.title+" "+(CATS[it.category]||"")+" "+(it.spot||""));return w.some(x=>t.includes(x))})}
  if(!d.length){out.innerHTML='<div class="none">ما لقيناه بين الموجودات للحين. <a href="'+window.__WEB+'">بلّغ عنه</a> وننبهك أول ما ينلقى.</div>';return}
  out.innerHTML='<div class="res">'+d.slice(0,12).map(it=>{const img=it.photo_path?'<img loading="lazy" alt="" src="'+U+'/storage/v1/object/public/found/'+esc(it.photo_path)+'">':'<div class="ph">'+(ICO[it.category]||"📦")+'</div>';
   return '<a href="'+window.__WEB+'">'+img+'<div class="t">'+esc(it.title)+'<small>'+esc(it.venues?.name_ar||it.spot||"")+'</small><small>'+esc(it.found_on||"")+'</small></div></a>'}).join("")+'</div>';
 }catch(e){out.innerHTML='<div class="none">تعذّر البحث الحين، جرّب مرة ثانية.</div>'}}
document.getElementById("finder").addEventListener("submit",e=>{e.preventDefault();run()});
document.getElementById("fc").addEventListener("change",run);
</script>"""
