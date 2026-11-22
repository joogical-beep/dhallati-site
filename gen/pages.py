# Extra pages: how it works, support, privacy, account deletion, city pages
CITIES = [
 ("riyadh","الرياض","المولات الكبيرة، المستشفيات، البوليفارد ومواسم الرياض، الحدائق والممشى، المطار"),
 ("jeddah","جدة","الكورنيش والواجهة البحرية، المولات، جدة التاريخية، الفعاليات الموسمية، المطار"),
 ("makkah","مكة المكرمة","الفنادق المحيطة بالمسجد الحرام، مراكز الخدمة، المستشفيات، مواسم الحج والعمرة"),
 ("madinah","المدينة المنورة","الفنادق المحيطة بالمسجد النبوي، المولات، المستشفيات، مواسم الزيارة"),
 ("dammam","الدمام والخبر","الواجهة البحرية، المولات، المستشفيات، الجامعات، المطار"),
]

def page_shell(head, FOOT, title, desc, path, ld, body):
    return head(title, desc, path, ld) + f"<main>{body}</main>" + FOOT

def build_pages(head, FOOT, ORG, SITE, APP, write, html, DL):
    def faqld(faq):
        return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    def faqh(faq):
        return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)

    # How it works
    how = {"@context":"https://schema.org","@type":"HowTo","name":"كيف يعمل ضالّتي","step":[
        {"@type":"HowToStep","name":"تسجيل الغرض","text":"الموظف يصوّر الغرض الموجود ويكتب وصفه ومكان العثور عليه."},
        {"@type":"HowToStep","name":"البحث والمطابقة","text":"صاحب الغرض يبحث من جواله، والتطبيق يطابق وصفه مع الموجودات."},
        {"@type":"HowToStep","name":"التواصل","text":"التواصل داخل التطبيق، ورقم الموظف يبقى مخفيًا."},
        {"@type":"HowToStep","name":"التحقق والتسليم","text":"سؤال تحقق لا يعرفه إلا صاحب الغرض، ثم التسليم وتوثيقه."}]}
    body = f"""<section class="hero"><h1>كيف يعمل ضالّتي</h1>
<p class="lead">من لحظة العثور على الغرض إلى لحظة تسليمه لصاحبه، في أربع خطوات.</p></section>
<ol class="steps"><li><b>تسجيل الغرض:</b> الموظف يصوّر الغرض ويكتب وصفه ومكان العثور عليه خلال ثوانٍ.</li>
<li><b>البحث والمطابقة:</b> صاحب الغرض يبحث من جواله، والتطبيق يطابقه مع الموجودات.</li>
<li><b>التواصل:</b> داخل التطبيق، ورقم الموظف يبقى مخفيًا.</li>
<li><b>التحقق والتسليم:</b> سؤال لا يعرفه إلا صاحب الغرض، ثم التسليم وتوثيقه.</li></ol>
<h2>للمنشأة</h2><ul class="feat"><li>سجل موحد لكل الموجودات بدل الدفتر الورقي.</li><li>اتصالات أقل على الاستقبال وخدمة العملاء.</li><li>كل تسليم موثق.</li><li>بدون أجهزة ولا تركيب.</li></ul>
<h2>لصاحب الغرض</h2><ul class="feat"><li>يبحث بنفسه من جواله.</li><li>بلغته، من 14 لغة.</li><li>يستلم غرضه بأمان بعد التحقق.</li></ul>
<div class="btns">{DL}</div><p><a href="/support.html">تواصل معنا</a></p>"""
    write("/how-it-works.html", page_shell(head, FOOT, "كيف يعمل ضالّتي | تطبيق مفقودات بالخطوات",
        "شرح خطوات ضالّتي: تسجيل الغرض بالصورة، البحث والمطابقة، التواصل الآمن، ثم التحقق والتسليم لصاحبه.", "/how-it-works.html", [ORG, how], body))

    # Support
    sfaq = [("كيف أطلب حساب لمنشأتي؟","راسلنا على info@dhallati.com باسم المنشأة والمدينة، ونجهّز الحساب خلال يوم عمل."),
            ("فقدت غرضًا، كيف أبحث عنه؟","حمّل التطبيق وابحث بوصف الغرض. إذا كانت المنشأة تستخدم ضالّتي سيظهر لك ما يطابقه."),
            ("كيف ألغي الاشتراك؟","راسلنا من بريد المنشأة المسجّل، ويُلغى الاشتراك من الشهر التالي."),
            ("كيف أحذف حسابي؟","من صفحة حذف الحساب في هذا الموقع."),
            ("كم وقت الرد؟","نرد على الرسائل خلال يوم عمل.")]
    body = f"""<section class="hero"><h1>الدعم والمساعدة</h1><p class="lead">نرد خلال يوم عمل.</p></section>
<div class="contact"><h2 style="margin-top:0">تواصل معنا</h2>
<p>البريد: <span class="ltr">info@dhallati.com</span><br>الجوال: <span class="ltr">0545510045</span></p>
<a class="btn" href="mailto:info@dhallati.com?subject=%D8%AF%D8%B9%D9%85%20%D8%B6%D8%A7%D9%84%D9%91%D8%AA%D9%8A">راسلنا</a></div>
<h2>أسئلة شائعة</h2>{faqh(sfaq)}
<p><a href="/privacy.html">سياسة الخصوصية</a> <a href="/delete-account.html">حذف الحساب</a></p>"""
    write("/support.html", page_shell(head, FOOT, "الدعم | ضالّتي", "تواصل مع فريق ضالّتي: البريد والجوال والأسئلة الشائعة عن التطبيق والاشتراك وحذف الحساب.", "/support.html", [ORG, faqld(sfaq)], body))

    # Privacy
    body = """<article><h1>سياسة الخصوصية</h1><p class="meta">آخر تحديث: 22 نوفمبر 2026</p>
<p>توضح هذه السياسة كيف يجمع تطبيق «ضالّتي» وموقع dhallati.com البيانات ويستخدمها ويحميها. نلتزم بنظام حماية البيانات الشخصية في المملكة العربية السعودية.</p>
<h2>البيانات التي نجمعها</h2><ul>
<li>بيانات حساب المنشأة: اسم المنشأة، اسم الموظف، البريد الإلكتروني، رقم التواصل.</li>
<li>بيانات الموجودات: صور الأغراض ووصفها ومكان ووقت العثور عليها.</li>
<li>بيانات من يبحث عن غرضه: الوصف الذي يكتبه، ووسيلة التواصل التي يختارها لاستلام الغرض.</li>
<li>الرسائل المتبادلة داخل التطبيق لغرض التسليم.</li>
<li>في الموقع فقط: بيانات زيارة عامة عبر Google Analytics لقياس عدد الزوار.</li></ul>
<h2>كيف نستخدمها</h2><ul><li>تشغيل خدمة تسجيل الموجودات ومطابقتها وتسليمها.</li><li>التحقق من صاحب الغرض قبل التسليم.</li><li>الدعم الفني والتواصل بخصوص الحساب.</li></ul>
<h2>المشاركة</h2><p>لا نبيع البيانات ولا نؤجرها. لا تظهر أرقام الموظفين لمن يبحث عن غرضه. نشارك البيانات فقط مع مزودي الاستضافة والخدمات التقنية اللازمين لتشغيل التطبيق، أو إذا طلبتها جهة رسمية مختصة نظامًا.</p>
<h2>الحفظ والحذف</h2><p>نحتفظ بالبيانات طوال مدة الحساب. يمكنك طلب حذف حسابك وبياناته في أي وقت من <a href="/delete-account.html">صفحة حذف الحساب</a>، ونحذفها خلال 30 يومًا من الطلب.</p>
<h2>الحماية</h2><p>نستخدم اتصالًا مشفّرًا وصلاحيات وصول محدودة لحماية البيانات.</p>
<h2>تواصل معنا</h2><p>لأي سؤال عن الخصوصية: <span class="ltr">info@dhallati.com</span></p></article>"""
    write("/privacy.html", page_shell(head, FOOT, "سياسة الخصوصية | ضالّتي", "سياسة الخصوصية لتطبيق ضالّتي وموقع dhallati.com: البيانات التي نجمعها وكيف نستخدمها ونحميها وكيف تحذفها.", "/privacy.html", [ORG], body))

    # Account deletion
    body = """<article><h1>حذف الحساب</h1>
<p class="lead">تقدر تحذف حسابك في ضالّتي وكل بياناته في أي وقت.</p>
<h2>طريقة الحذف</h2><ol>
<li>أرسل رسالة إلى <span class="ltr">info@dhallati.com</span> من البريد المسجّل في حسابك.</li>
<li>اكتب في العنوان: «طلب حذف حساب».</li>
<li>نؤكد استلام الطلب خلال يوم عمل، ونحذف الحساب وبياناته خلال 30 يومًا.</li></ol>
<h2>ما الذي يُحذف</h2><ul><li>بيانات الحساب ومعلومات التواصل.</li><li>صور ووصف الموجودات التي سجّلها الحساب.</li><li>الرسائل داخل التطبيق.</li></ul>
<p>قد نحتفظ بسجلات مالية للاشتراكات المدة التي يلزمها النظام فقط.</p>
<div class="btns"><a class="btn" href="mailto:info@dhallati.com?subject=%D8%B7%D9%84%D8%A8%20%D8%AD%D8%B0%D9%81%20%D8%AD%D8%B3%D8%A7%D8%A8">أرسل طلب الحذف</a></div></article>"""
    write("/delete-account.html", page_shell(head, FOOT, "حذف الحساب | ضالّتي", "طريقة حذف حسابك في تطبيق ضالّتي وكل بياناته، ومدة تنفيذ الطلب.", "/delete-account.html", [ORG], body))

    # City pages
    links = []
    for slug, name, places in CITIES:
        path = f"/cities/{slug}.html"
        links.append((path, name))
        cfaq = [(f"فقدت شيئًا في {name}، وش أسوي؟", "تواصل مع المكان اللي فقدت فيه الغرض بأسرع وقت، وإذا كان يستخدم ضالّتي ابحث بوصف الغرض من التطبيق. لفقدان الوثائق الرسمية بلّغ عبر أبشر."),
                (f"هل ضالّتي متاح للمنشآت في {name}؟", "نعم، الخدمة تعمل عن بُعد في كل مدن المملكة، والحساب يجهز خلال يوم عمل.")]
        body = f"""<section class="hero"><h1>تطبيق مفقودات في {name}</h1>
<p class="lead">«ضالّتي» ينظم المفقودات والموجودات في منشآت {name}: {places}.</p>
<div class="btns">{DL}</div><p><a href="/support.html">اطلب حساب لمنشأتك</a></p></section>
<h2>فقدت غرضًا في {name}؟</h2><ol class="steps"><li>تواصل مع المكان اللي فقدت فيه الغرض بأسرع وقت.</li><li>إذا كان المكان يستخدم ضالّتي، ابحث بوصف الغرض من جوالك.</li><li>جاوب سؤال التحقق واستلم غرضك.</li></ol>
<p class="soft">فقدان الهوية أو الجواز أو الرخصة: بلّغ عنه عبر أبشر.</p>
<h2>للمنشآت والجهات في {name}</h2><ul class="feat"><li>تسجيل الموجودات بالصورة خلال ثوانٍ.</li><li>14 لغة للزوار والسياح.</li><li>تواصل آمن ورقم الموظف مخفي.</li><li>299 ريال شهريًا للخاص، 999 ريال شهريًا للحكومي.</li></ul>
<h2>أسئلة شائعة</h2>{faqh(cfaq)}"""
        write(path, page_shell(head, FOOT, f"تطبيق مفقودات في {name} | ضالّتي",
            f"البحث عن المفقودات في {name}: ضالّتي ينظم المفقودات في المولات والمستشفيات والفنادق والجهات الحكومية، ويساعد صاحب الغرض يلقاه من جواله.", path, [ORG, faqld(cfaq)], body))
    return ["/how-it-works.html","/support.html","/privacy.html","/delete-account.html"] + [p for p,_ in links], links

PK = "pk_live_HfyJvNhYsJAvK3q7XuDheGEUekSBrwiNZcyX4BCd"  # Moyasar publishable key (public by design)

def build_pay(head, FOOT, ORG, write):
    FN = "https://gtgnekbrkczlszrwwuaz.supabase.co/functions/v1/dallati-subs"
    body = """<section class="hero" style="padding-bottom:8px"><h1>اشتراك ضالّتي للجهات</h1><p class="lead">اختر نوع الجهة، اكتب بياناتها، وادفع. يتجدد الاشتراك تلقائيًا كل شهر، ويمكن إلغاؤه في أي وقت.</p></section>
<link rel="stylesheet" href="https://cdn.moyasar.com/mpf/1.14.0/moyasar.css">
<style>.pick{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;max-width:520px;margin:18px 0}
.pick label{display:block;background:var(--card);border:2px solid var(--line);border-radius:16px;padding:14px;cursor:pointer}
.pick input{position:absolute;opacity:0}.pick label:has(input:checked){border-color:var(--butter)}
.pick b{display:block;color:var(--cream)}.pick span{font-size:1.6rem;font-weight:700;color:var(--butter)}
.f{display:grid;gap:12px;max-width:520px}.f label{display:grid;gap:6px;color:var(--cream)}
.f input{font:inherit;padding:12px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--ink)}
.card{max-width:520px;margin-top:18px;background:#fff;border-radius:16px;padding:16px;color:#222}
#wait{color:#555;text-align:center;padding:18px 0}</style>
<div class="pick" role="radiogroup">
<label><input type="radio" name="plan" value="private" checked><b>جهة خاصة</b><span>299</span> ريال شهريًا</label>
<label><input type="radio" name="plan" value="gov"><b>جهة حكومية</b><span>999</span> ريال شهريًا</label></div>
<div class="f"><label>اسم الجهة<input id="org" autocomplete="organization"></label>
<label>البريد الإلكتروني<input id="em" type="email" dir="ltr" autocomplete="email"></label>
<label>الجوال<input id="ph" type="tel" dir="ltr" autocomplete="tel"></label></div>
<div class="card"><p id="wait">اكتب اسم الجهة والبريد والجوال، وتظهر هنا خانة البطاقة.</p><div class="mysr-form"></div></div>
<p class="soft">الدفع آمن عبر ميسّر. بعد الدفع نجهّز حساب جهتكم خلال يوم عمل. للإلغاء راسلنا على <span class="ltr">info@dhallati.com</span></p>
<script src="https://cdn.moyasar.com/mpf/1.14.0/moyasar.js"></script>
<script>
const P={private:{a:29900,n:"جهة خاصة"},gov:{a:99900,n:"جهة حكومية"}};
const q=new URLSearchParams(location.search);if(q.get("plan")==="gov")document.querySelector('input[value=gov]').checked=true;
const $=id=>document.getElementById(id);let last="",t;
function render(){const k=document.querySelector('input[name=plan]:checked').value,org=$("org").value.trim(),em=$("em").value.trim(),ph=$("ph").value.trim();
 const ok=org.length>1&&/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)&&ph.replace(/\D/g,"").length>=9;
 const box=document.querySelector(".mysr-form");const sig=[k,org,em,ph].join("|");
 if(!ok){$("wait").hidden=false;box.innerHTML="";last="";return}
 if(sig===last)return;last=sig;$("wait").hidden=true;box.innerHTML="";
 Moyasar.init({element:".mysr-form",amount:P[k].a,currency:"SAR",language:"ar",
  description:"اشتراك ضالّتي الشهري - "+P[k].n+" - "+org,publishable_api_key:"%PK%",
  callback_url:location.origin+"/thanks.html",methods:["applepay","creditcard"],credit_card:{save_card:true},apple_pay:{country:"SA",label:"ضالّتي",validate_merchant_url:"https://api.moyasar.com/v1/applepay/initiate"},
  metadata:{app:"dallati",plan:k,org:org,email:em,phone:ph}});}
document.querySelectorAll("input").forEach(i=>i.addEventListener("input",()=>{clearTimeout(t);t=setTimeout(render,500)}));
document.querySelectorAll('input[name=plan]').forEach(i=>i.addEventListener("change",render));
</script>""".replace("%PK%", PK)
    write("/subscribe.html", head("اشتراك ضالّتي للجهات | الدفع", "اشترك في ضالّتي لإدارة المفقودات في جهتك: 299 ريال شهريًا للجهات الخاصة و999 ريال للحكومية، يتجدد تلقائيًا، والدفع آمن عبر ميسّر.", "/subscribe.html", [ORG]) + f"<main>{body}</main>" + FOOT)
    body = """<section class="hero"><h1 id="h">جاري التأكد من الدفع…</h1><p class="lead" id="m"></p></section>
<div class="btns"><a class="btn" href="/">الرئيسية</a><a class="btn o" href="/support.html">الدعم</a></div>
<script>const q=new URLSearchParams(location.search),id=q.get("id");const h=document.getElementById("h"),m=document.getElementById("m");
function fail(x){h.textContent="لم يكتمل الدفع";m.textContent=(x?x+". ":"")+"حاول مرة ثانية من صفحة الاشتراك، أو راسلنا على info@dhallati.com"}
if(!id||q.get("status")!=="paid"){fail(q.get("message")||"")}else{
fetch("%FN%",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({verify:id})}).then(r=>r.json()).then(j=>{
 if(!j.ok){fail(j.message||"");return}
 h.textContent="تم الاشتراك، شكرًا لكم";
 const d=j.next?new Date(j.next).toLocaleDateString("ar-SA-u-nu-latn",{year:"numeric",month:"long",day:"numeric"}):"";
 m.textContent="نجهّز حساب "+(j.org||"جهتكم")+" خلال يوم عمل ونرسل التفاصيل على بريدكم."+(j.auto&&d?" التجديد القادم تلقائيًا في "+d+".":"");
}).catch(()=>{h.textContent="تم استلام الدفع";m.textContent="نجهّز حسابكم خلال يوم عمل ونرسل التفاصيل على بريدكم."})}
</script>""".replace("%FN%", FN)
    write("/thanks.html", head("حالة الدفع | ضالّتي", "حالة الدفع لاشتراك ضالّتي.", "/thanks.html", []).replace('content="index,follow,max-image-preview:large"','content="noindex"') + f"<main>{body}</main>" + FOOT)
