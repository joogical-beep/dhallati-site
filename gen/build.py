import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://dhallati.com"
APP = "https://apps.apple.com/app/id6831172490"
SOCIAL = []  # filled after accounts are created

CSS = """
:root{--bg:#2F2924;--ink:#F1E7D6;--soft:#C9BBA6;--card:#3A322B;--line:#4E433A;--butter:#F2E2A0;--cream:#ECDFC8;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Readex Pro",system-ui,Tahoma,sans-serif;line-height:1.8}
a{color:var(--butter)}
.w{max-width:960px;margin:0 auto;padding-block:24px 64px;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}
.brand img{width:44px;height:44px;border-radius:12px}
.brand b{font-size:1.25rem}
nav{display:flex;gap:16px;flex-wrap:wrap}
nav a{color:var(--soft);text-decoration:none}
nav a:hover,nav a:focus-visible{color:var(--butter)}
.hero{padding:56px 0 24px}
h1{font-size:clamp(1.9rem,5vw,3.2rem);line-height:1.25;margin:0;color:var(--butter);text-wrap:balance}
.lead{font-size:1.15rem;color:var(--cream);max-width:56ch;margin:16px 0 0}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.btn{display:inline-block;background:var(--butter);color:#2F2924;padding:12px 22px;border-radius:14px;font-weight:600;text-decoration:none}
.btn.o{background:transparent;color:var(--butter);border:1px solid var(--butter)}
.quote{border-inline-start:6px solid var(--butter);padding:4px 18px;margin:36px 0;font-size:1.3rem;color:var(--cream);max-width:60ch}
h2{font-size:1.5rem;margin:44px 0 10px;text-wrap:balance}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;padding:0;list-style:none;counter-reset:s}
.steps li{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px;counter-increment:s}
.steps li::before{content:counter(s);display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--butter);color:#2F2924;font-weight:700;margin-bottom:8px}
.feat{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;padding:0;list-style:none}
.feat li{border-bottom:1px solid var(--line);padding:10px 0;color:var(--cream)}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.p{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px}
.p h3{margin:0;font-size:1.1rem;color:var(--cream)}
.price{font-size:2.2rem;font-weight:700;color:var(--butter);margin:6px 0 0}
.price span{font-size:1rem;font-weight:400;color:var(--soft)}
.soft{color:var(--soft)}
.posts{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;padding:0;list-style:none}
.posts a{display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;text-decoration:none;color:var(--ink);height:100%}
.posts a:hover,.posts a:focus-visible{border-color:var(--butter)}
.posts b{display:block;color:var(--butter);margin-bottom:4px}
details{border-bottom:1px solid var(--line);padding:12px 0}
summary{cursor:pointer;font-weight:600}
.contact{margin-top:44px;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px}
.ltr{direction:ltr;unicode-bidi:isolate}
footer{margin-top:48px;color:var(--soft);font-size:.9rem;border-top:1px solid var(--line);padding-top:18px}
article{max-width:68ch}
article h2{font-size:1.3rem}
article li{margin:6px 0}
.tip{background:var(--card);border-inline-start:4px solid var(--butter);border-radius:10px;padding:12px 16px;margin:20px 0}
.meta{color:var(--soft);font-size:.9rem;margin-top:8px}
:focus-visible{outline:2px solid var(--butter);outline-offset:3px}
"""

def head(title, desc, path, extra_ld):
    url = SITE + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in extra_ld)
    return f"""<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="ضالّتي">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.jpg"><meta property="og:locale" content="ar_SA">
<meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id=6831172490">
<meta name="theme-color" content="#2F2924">
<link rel="icon" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;600;700&display=swap">
<style>{CSS}</style>{ld}</head><body><div class="w">
<header><a class="brand" href="/"><img src="/icon.png" alt="" width="44" height="44"><b>ضالّتي</b></a>
<nav><a href="/#how">كيف يعمل</a><a href="/#prices">الأسعار</a><a href="/blog/">المقالات</a><a href="{APP}">حمّل التطبيق</a></nav></header>
"""

FOOT = f"""<footer>ضالّتي، تطبيق سعودي لإدارة المفقودات والموجودات في المنشآت.<br>
<span class="ltr">info@dhallati.com</span><br><span class="ltr">0545510045</span></footer></div></body></html>"""

ORG = {"@context":"https://schema.org","@type":"Organization","name":"ضالّتي","alternateName":"Dallati","url":SITE,
       "logo":SITE+"/icon.png","email":"info@dhallati.com","telephone":"+966545510045","areaServed":"SA"}

def write(path, text):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)

def home():
    faq = [("ما هو ضالّتي؟","تطبيق سعودي على iPhone لإدارة المفقودات والموجودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية."),
           ("كم الاشتراك؟","299 ريال شهريًا للجهات الخاصة، و999 ريال شهريًا للجهات الحكومية، ويمكن الإلغاء في أي وقت."),
           ("هل نحتاج أجهزة أو تركيب؟","لا، يكفي جوال iPhone، وكل شيء يتم عن بُعد، ونجهّز حسابكم خلال يوم عمل."),
           ("كيف نضمن أن الغرض يرجع لصاحبه؟","بسؤال تحقق قبل التسليم، والتواصل داخل التطبيق ورقم الموظف مخفي."),
           ("كم لغة يدعم؟","14 لغة لخدمة جميع الزوار.")]
    app = {"@context":"https://schema.org","@type":"MobileApplication","name":"ضالّتي","alternateName":"Dallati",
           "operatingSystem":"iOS","applicationCategory":"BusinessApplication","url":SITE,"downloadUrl":APP,
           "offers":[{"@type":"Offer","price":"299","priceCurrency":"SAR","description":"اشتراك شهري للجهات الخاصة"},
                     {"@type":"Offer","price":"999","priceCurrency":"SAR","description":"اشتراك شهري للجهات الحكومية"}]}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    if SOCIAL: ORG["sameAs"] = SOCIAL
    posts = "".join(f'<li><a href="/blog/{a["slug"]}.html"><b>{html.escape(a["h1"])}</b><span class="soft">{html.escape(a["desc"][:90])}…</span></a></li>' for a in ARTICLES[:6])
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
    t = head("ضالّتي | تطبيق إدارة المفقودات والموجودات للمنشآت في السعودية",
             "ضالّتي تطبيق سعودي لإدارة المفقودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية: تسجيل بالصور، بحث ومطابقة، وتسليم آمن.",
             "/", [ORG, app, fq])
    t += f"""<main><section class="hero"><h1>المفقودات في منشأتك، ترجع لأصحابها بأمان</h1>
<p class="lead">«ضالّتي» تطبيق سعودي على iPhone لإدارة المفقودات والموجودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية.</p>
<div class="btns"><a class="btn" href="{APP}">حمّل من App Store</a><a class="btn o" href="mailto:info@dhallati.com">اطلب حساب لمنشأتك</a></div></section>
<p class="quote">الناس لا تنسى أبدًا المكان الذي صنع لها ذكرى سعيدة.</p>
<h2 id="how">كيف يعمل</h2>
<ol class="steps"><li>الموظف يسجّل الغرض الموجود بصورة ووصف خلال ثوانٍ.</li>
<li>صاحب الغرض يبحث من جواله، والتطبيق يطابقه مع موجوداتكم.</li>
<li>سؤال تحقق، ثم تسليم الغرض لصاحبه الحقيقي.</li></ol>
<h2>لماذا ضالّتي</h2>
<ul class="feat"><li>تواصل داخل التطبيق، ورقم الموظف يبقى مخفيًا.</li><li>متاح بـ14 لغة تخدم جميع الزوار.</li>
<li>بدون أجهزة ولا تركيب، كل شيء عن بُعد.</li><li>نجهّز حسابكم خلال يوم عمل واحد.</li></ul>
<h2 id="prices">الأسعار</h2>
<div class="plans"><div class="p"><h3>الجهات الخاصة</h3><p class="price">299 <span>ريال شهريًا</span></p>
<p class="soft">المولات، المستشفيات والعيادات، المطاعم والمقاهي، الفنادق، الشركات، الجامعات والمدارس الخاصة.</p></div>
<div class="p"><h3>الجهات الحكومية</h3><p class="price">999 <span>ريال شهريًا</span></p>
<p class="soft">الأمانات والبلديات، الحدائق العامة، المطارات، المستشفيات والجامعات الحكومية، وكل جهة حكومية.</p></div></div>
<p class="soft">يمكن إلغاء الاشتراك في أي وقت.</p>
<h2>من المقالات</h2><ul class="posts">{posts}</ul>
<p><a href="/blog/">كل المقالات</a></p>
<h2>أسئلة شائعة</h2>{faqh}
<div class="contact"><h2 style="margin-top:0">ابدأ اليوم</h2>
<p>راسلنا على <span class="ltr">info@dhallati.com</span> أو اتصل على <span class="ltr">0545510045</span>، ونجهّز حساب منشأتك خلال يوم عمل.</p>
<a class="btn" href="{APP}">حمّل ضالّتي</a></div></main>{FOOT}"""
    write("/index.html", t)

def article(a):
    path = f"/blog/{a['slug']}.html"
    art = {"@context":"https://schema.org","@type":"Article","headline":a["h1"],"description":a["desc"],
           "datePublished":a["date"],"dateModified":a["date"],"inLanguage":"ar","mainEntityOfPage":SITE+path,
           "image":SITE+"/og.jpg","author":{"@type":"Organization","name":"ضالّتي"},"publisher":ORG}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":x}} for q,x in a["faq"]]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"ضالّتي","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"المقالات","item":SITE+"/blog/"},
        {"@type":"ListItem","position":3,"name":a["h1"],"item":SITE+path}]}
    faqh = "".join(f"<details><summary>{q}</summary><p>{x}</p></details>" for q,x in a["faq"])
    others = [o for o in ARTICLES if o["slug"]!=a["slug"]][:3]
    rel = "".join(f'<li><a href="/blog/{o["slug"]}.html"><b>{html.escape(o["h1"])}</b></a></li>' for o in others)
    t = head(a["title"]+" | ضالّتي", a["desc"], path, [art, fq, bc])
    t += f"""<main><article><p class="meta"><a href="/blog/">المقالات</a></p><h1>{html.escape(a['h1'])}</h1>
{a['body']}<h2>أسئلة شائعة</h2>{faqh}
<div class="btns"><a class="btn" href="{APP}">حمّل ضالّتي</a><a class="btn o" href="/#prices">الأسعار</a></div></article>
<h2>مقالات أخرى</h2><ul class="posts">{rel}</ul></main>{FOOT}"""
    write(path, t)

def blog_index():
    posts = "".join(f'<li><a href="/blog/{a["slug"]}.html"><b>{html.escape(a["h1"])}</b><span class="soft">{html.escape(a["desc"])}</span></a></li>' for a in reversed(ARTICLES))
    t = head("مقالات عن إدارة المفقودات | ضالّتي", "مقالات عملية عن إدارة المفقودات والموجودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية.", "/blog/", [ORG])
    t += f"<main><h1>مقالات ضالّتي</h1><p class='lead'>كل ما يخص إدارة المفقودات في المنشآت.</p><ul class='posts' style='margin-top:24px'>{posts}</ul></main>{FOOT}"
    write("/blog/index.html", t)

def extras():
    urls = [("/","1.0"),("/blog/","0.8")] + [(f"/blog/{a['slug']}.html","0.7") for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"<url><loc>{SITE}{u}</loc><priority>{p}</priority></url>\n" for u,p in urls) + "</urlset>\n"
    write("/sitemap.xml", sm)
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write("/CNAME", "dhallati.com\n")
    write("/.nojekyll", "")
    t = head("الصفحة غير موجودة | ضالّتي", "الصفحة غير موجودة.", "/404.html", [])
    t += f"<main><h1>الصفحة غير موجودة</h1><p><a href='/'>الرجوع للرئيسية</a></p></main>{FOOT}"
    write("/404.html", t)

home(); blog_index(); [article(a) for a in ARTICLES]; extras()
print("ok", len(ARTICLES))
