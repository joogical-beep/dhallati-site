import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES
from pages import build_pages, CITIES, build_pay
import home_live as HL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://dhallati.com"
APP = "https://apps.apple.com/app/id6831172490"
WEBAPP = "/app/"
PAY_PRIVATE = "/subscribe.html?plan=private"
PAY_GOV = "/subscribe.html?plan=gov"
SUB_PRIVATE = f'<a class="btn" href="{PAY_PRIVATE}">اشترك: جهة خاصة 299 ريال شهريًا</a>'
SUB_GOV = f'<a class="btn o" href="{PAY_GOV}">اشترك: جهة حكومية 999 ريال شهريًا</a>'
DL = f'<a class="btn" href="{APP}">للآيفون: حمّل من App Store</a><a class="btn o" href="{WEBAPP}">لغير الآيفون: افتح ضالّتي من المتصفح</a>'
SOCIAL = ["https://www.instagram.com/dhallati.sa/", "https://x.com/dhallati", "https://www.facebook.com/profile.php?id=61596629137000"]  # filled after accounts are created

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
footer p a{margin-inline-end:14px}
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
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><script async src="https://www.googletagmanager.com/gtm.js?id=GTM-5FMDV5HQ"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());</script>
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
<style>{CSS}{HL.CSS}</style>{ld}</head><body><div class="w">
<header><a class="brand" href="/"><img src="/icon-88.webp" alt="" width="44" height="44"><b>ضالّتي</b></a>
<nav><a href="/how-it-works.html">كيف يعمل</a><a href="/#prices">الأسعار</a><a href="/blog/">المقالات</a><a href="/gov.html">للجهات الحكومية</a><a href="/support.html">الدعم</a><a href="{APP}">حمّل التطبيق</a></nav></header>
"""

CITY_LINKS = " ".join(f'<a href="/cities/{c[0]}.html">مفقودات {c[1]}</a>' for c in CITIES)
FOOT = f"""<footer>ضالّتي، تطبيق سعودي لإدارة المفقودات والموجودات في المنشآت.<br>
<span class="ltr">info@dhallati.com</span>
<p>حساباتنا: <a href="https://www.instagram.com/dhallati.sa/">انستقرام</a> <a href="https://www.facebook.com/profile.php?id=61596629137000">فيسبوك</a> <a href="https://x.com/dhallati">إكس</a></p>
<p><a href="/how-it-works.html">كيف يعمل</a> <a href="/support.html">الدعم</a> <a href="/privacy.html">سياسة الخصوصية</a> <a href="/delete-account.html">حذف الحساب</a></p>
<p>{CITY_LINKS}</p></footer></div></body></html>"""

ORG = {"@context":"https://schema.org","@type":"Organization","name":"ضالّتي","alternateName":["Dallati","Dalati","ضالتي"],"url":SITE,
       "logo":SITE+"/icon.png","email":"info@dhallati.com","areaServed":"SA"}

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
    app = {"@context":"https://schema.org","@type":"MobileApplication","name":"ضالّتي","alternateName":["Dallati","Dalati","ضالتي"],
           "operatingSystem":"iOS","applicationCategory":"BusinessApplication","url":SITE,"downloadUrl":APP,
           "offers":[{"@type":"Offer","price":"299","priceCurrency":"SAR","description":"اشتراك شهري للجهات الخاصة"},
                     {"@type":"Offer","price":"999","priceCurrency":"SAR","description":"اشتراك شهري للجهات الحكومية"}]}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    if SOCIAL: ORG["sameAs"] = SOCIAL
    posts = "".join(f'<li><a href="/blog/{a["slug"]}.html"><b>{html.escape(a["h1"])}</b><span class="soft">{html.escape(a["desc"][:90])}…</span></a></li>' for a in ARTICLES[:6])
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
    t = head("ضالّتي (ضالتي) Dallati | تطبيق مفقودات للمنشآت في السعودية",
             "ضالّتي (Dallati) تطبيق مفقودات سعودي لإدارة المفقودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية: تسجيل بالصور، بحث ومطابقة، وتسليم آمن.",
             "/", [ORG, {"@context":"https://schema.org","@type":"WebSite","name":"ضالّتي","alternateName":["Dallati","ضالتي"],"url":SITE,"inLanguage":"ar"}, app, fq])
    t += HL.hero(APP, WEBAPP) + HL.JOURNEY + f"""<main>
<div class="plans" style="margin-top:36px">
<div class="p"><h3>للأفراد: ضاع منك شيء؟</h3><p class="soft">مجانًا. ابحث وبلّغ من جوالك.</p><div class="btns">{DL}</div></div>
<div class="p"><h3>للجهات والمنشآت</h3><p class="soft">اشتراك شهري، ونجهّز حسابكم خلال يوم عمل.</p><div class="btns">{SUB_PRIVATE}{SUB_GOV}</div></div>
</div>
<h2 id="prices">الأسعار</h2>
<div class="plans"><div class="p"><h3>الجهات الخاصة</h3><p class="price">299 <span>ريال شهريًا</span></p>
<p class="soft">المولات، المستشفيات والعيادات، المطاعم والمقاهي، الفنادق، الشركات، الجامعات والمدارس الخاصة.</p><div class="btns">{SUB_PRIVATE}</div></div>
<div class="p"><h3>الجهات الحكومية</h3><p class="price">999 <span>ريال شهريًا</span></p>
<p class="soft">الأمانات والبلديات، الحدائق العامة، المطارات، المستشفيات والجامعات الحكومية، وكل جهة حكومية.</p><div class="btns">{SUB_GOV}</div></div></div>
<p class="soft">يمكن إلغاء الاشتراك في أي وقت.</p>
<h2>من المقالات</h2><ul class="posts">{posts}</ul>
<p><a href="/blog/">كل المقالات</a></p>
<h2>أسئلة شائعة</h2>{faqh}
<div class="contact"><h2 style="margin-top:0">ابدأ اليوم</h2>
<p>راسلنا على <span class="ltr">info@dhallati.com</span>، ونجهّز حساب منشأتك خلال يوم عمل.</p>
<div class="btns">{DL}</div></div></main>{FOOT}"""
    write("/index.html", t.replace("</body>", HL.JS+"</body>"))

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
<div class="btns">{DL}</div></article>
<h2>مقالات أخرى</h2><ul class="posts">{rel}</ul></main>{FOOT}"""
    write(path, t)

def blog_index():
    posts = "".join(f'<li><a href="/blog/{a["slug"]}.html"><b>{html.escape(a["h1"])}</b><span class="soft">{html.escape(a["desc"])}</span></a></li>' for a in reversed(ARTICLES))
    t = head("مقالات عن إدارة المفقودات | ضالّتي", "مقالات عملية عن إدارة المفقودات والموجودات في المولات والمستشفيات والمطاعم والفنادق والجهات الحكومية.", "/blog/", [ORG])
    t += f"<main><h1>مقالات ضالّتي</h1><p class='lead'>كل ما يخص إدارة المفقودات في المنشآت.</p><ul class='posts' style='margin-top:24px'>{posts}</ul></main>{FOOT}"
    write("/blog/index.html", t)

def gov():
    faq=[("هل يناسب الوزارات والأمانات والبلديات؟","نعم، يناسب الوزارات والهيئات والأمانات والبلديات والحدائق العامة والمطارات ومراكز خدمة المستفيدين."),
         ("كم اشتراك الجهات الحكومية؟","999 ريال شهريًا للجهة، ويمكن الإلغاء في أي وقت."),
         ("هل يحتاج أجهزة أو ربط أنظمة؟","لا، يعمل على iPhone وكل شيء يتم عن بُعد، والحساب يجهز خلال يوم عمل.")]
    fq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    svc={"@context":"https://schema.org","@type":"Service","name":"ضالّتي للجهات الحكومية","provider":ORG,"areaServed":"SA",
         "audience":{"@type":"Audience","audienceType":"الوزارات والهيئات والأمانات والبلديات"},
         "offers":{"@type":"Offer","price":"999","priceCurrency":"SAR"}}
    faqh="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
    rel=[a for a in ARTICLES if a["slug"] in ("amanat-baladiyat-lost-and-found","ministries-service-centers-lost-and-found","government-lost-and-found-office")]
    posts="".join(f'<li><a href="/blog/{a["slug"]}.html"><b>{html.escape(a["h1"])}</b></a></li>' for a in rel)
    t=head("نظام إدارة المفقودات للجهات الحكومية | ضالّتي",
           "نظام سعودي لإدارة المفقودات في الوزارات والأمانات والبلديات والمطارات والمستشفيات: سجل موحّد، بحث ذاتي للمستفيد، وتسليم موثّق. اطلب عرضًا للجهة.",
           "/gov.html",[ORG,svc,fq])
    t+=f"""<main><section class="hero"><h1>نظام إدارة المفقودات للوزارات والأمانات والبلديات</h1>
<p class="lead">سجل موحّد لكل مواقع الجهة، والمستفيد يبحث بنفسه من جواله، والتسليم بعد تحقق وموثّق. بدون أجهزة ولا ربط أنظمة.</p>
<div class="btns"><a class="btn" href="#req">اطلب عرضًا للجهة</a>{SUB_GOV}</div></section>
<h2>التحدي في الجهات اليوم</h2>
<ul class="feat"><li>سجلات ورقية متفرقة بين المواقع والفروع.</li><li>اتصالات واستفسارات متكررة من المراجعين.</li><li>صعوبة مطابقة وصف المراجع مع الغرض الموجود.</li><li>تسليم بدون تحقق ولا توثيق.</li></ul>
<h2>كيف يحلّها ضالّتي</h2>
<ol class="steps"><li>الموظف يسجّل الغرض بصورة ووصف خلال ثوانٍ، من أي موقع.</li><li>المستفيد يبحث من جواله، والتطبيق يطابقه مع الموجودات.</li><li>سؤال تحقق، ثم تسليم موثّق لصاحب الغرض.</li></ol>
<h2>ما تكسبه الجهة</h2>
<ul class="feat"><li>سجل واحد لكل المواقع بدل الدفاتر.</li><li>ضغط أقل على الاستقبال وخدمة المستفيدين.</li><li>كل تسليم موثّق ويمكن الرجوع له.</li><li>تجربة مستفيد أفضل بـ14 لغة.</li><li>تواصل آمن ورقم الموظف مخفي.</li><li>تشغيل عن بُعد خلال يوم عمل.</li></ul>
<h2>لمن؟</h2>
<ul class="feat"><li>الوزارات والهيئات ومراكز خدمة المستفيدين</li><li>الأمانات والبلديات</li><li>الحدائق العامة والممشى والواجهات البحرية</li><li>المطارات والمستشفيات والجامعات</li></ul>
<h2>خطوات التعاون</h2>
<ol class="steps"><li>طلب من النموذج أدناه أو بالبريد الرسمي.</li><li>عرض للجهة وتجهيز الحساب خلال يوم عمل.</li><li>التشغيل: الموظفون يسجّلون من جوالاتهم مباشرة.</li></ol>
<h2>الاشتراك</h2><div class="plans"><div class="p"><h3>الجهات الحكومية</h3><p class="price">999 <span>ريال شهريًا</span></p><p class="soft">يمكن الإلغاء في أي وقت.</p><div class="btns">{SUB_GOV}</div></div></div>
<div class="contact" id="req"><h2 style="margin-top:0">طلب عرض للجهة</h2>
<p class="soft">اكتب بيانات الجهة، ونرسل لكم العرض ونتواصل خلال يوم عمل. وبعد الإرسال تقدر تنزّل ورقة التعريف بضالّتي.</p>
<form id="lf" class="lf"><input name="org" required placeholder="اسم الجهة"><input name="sector" placeholder="القطاع (أمانة، وزارة، مستشفى…)">
<input name="contact" placeholder="اسم المسؤول"><input name="email" type="email" required dir="ltr" placeholder="البريد الرسمي">
<input name="phone" type="tel" dir="ltr" placeholder="رقم التواصل"><button class="btn" type="submit">أرسل الطلب</button></form>
<p id="lr" class="soft"></p></div>
<h2>مقالات للجهات الحكومية</h2><ul class="posts">{posts}</ul>
<h2>أسئلة شائعة</h2>{faqh}</main>{{FOOT}}
<style>.lf{{display:grid;gap:10px;max-width:520px}}.lf input{{font:inherit;padding:12px;border-radius:12px;border:1px solid var(--line);background:var(--bg);color:var(--ink)}}</style>
<script>document.getElementById("lf").addEventListener("submit",async e=>{{e.preventDefault();const f=Object.fromEntries(new FormData(e.target));const r=document.getElementById("lr");r.textContent="جاري الإرسال…";
try{{const x=await fetch("https://gtgnekbrkczlszrwwuaz.supabase.co/functions/v1/dallati-subs",{{method:"POST",headers:{{"content-type":"application/json"}},body:JSON.stringify({{lead:f}})}});const j=await x.json();
if(!j.ok)throw 0;e.target.hidden=true;r.innerHTML='وصل طلبكم، ونتواصل معكم خلال يوم عمل. <a href="/dallati-gov.pdf" download>نزّل ورقة التعريف بضالّتي (PDF)</a>';}}catch(_){{r.textContent="ما وصل الطلب، راسلونا على info@dhallati.com"}}}});</script>"""
    write("/gov.html",t.replace("{FOOT}",FOOT))

def extras():
    urls = [("/","1.0"),("/gov.html","0.9"),("/blog/","0.8")] + [(u,"0.8") for u in EXTRA] + [(f"/blog/{a['slug']}.html","0.7") for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"<url><loc>{SITE}{u}</loc><priority>{p}</priority></url>\n" for u,p in urls) + "</urlset>\n"
    write("/sitemap.xml", sm)
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write("/CNAME", "dhallati.com\n")
    write("/.nojekyll", "")
    write("/12a18a2853cf688f29707202dac6a65f.txt", "12a18a2853cf688f29707202dac6a65f")
    t = head("الصفحة غير موجودة | ضالّتي", "الصفحة غير موجودة.", "/404.html", [])
    t += f"<main><h1>الصفحة غير موجودة</h1><p><a href='/'>الرجوع للرئيسية</a></p></main>{FOOT}"
    write("/404.html", t)

EXTRA, _ = build_pages(head, FOOT, ORG, SITE, APP, write, html, DL)
build_pay(head, FOOT, ORG, write)
home(); gov(); blog_index(); [article(a) for a in ARTICLES]; extras()
print("ok", len(ARTICLES))
