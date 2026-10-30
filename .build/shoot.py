import asyncio, json
from playwright.async_api import async_playwright
BASE="file:///workspace/tax-site/"
PAGES=["index","services","about","faq","contact"]
async def main():
    async with async_playwright() as p:
        try: b=await p.chromium.launch()
        except Exception: b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        report={}
        for vpname,vp,mobile in [("mobile",{"width":390,"height":844},True),("desktop",{"width":1440,"height":900},False)]:
            for scheme in ["light","dark"]:
                ctx=await b.new_context(viewport=vp,device_scale_factor=2 if mobile else 1,color_scheme=scheme,is_mobile=mobile,has_touch=mobile)
                pg=await ctx.new_page()
                errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
                for name in PAGES:
                    await pg.goto(BASE+name+".html"); await pg.wait_for_timeout(150)
                    ov=await pg.evaluate("""()=>{const w=document.documentElement.clientWidth;const bad=[];
                      document.querySelectorAll('body *').forEach(el=>{const r=el.getBoundingClientRect(); if(r.width&&(r.right>w+1||r.left<-1)&&getComputedStyle(el).visibility!=='hidden'&&!el.closest('.nav__menu')&&!el.classList.contains('visually-hidden')&&!el.classList.contains('skip-link')) bad.push(el.tagName+'.'+el.className+' '+Math.round(r.right))});
                      return {sw:document.documentElement.scrollWidth,w,bad:bad.slice(0,5)}}""")
                    small=await pg.evaluate("""()=>{const out=[];document.querySelectorAll('a,button,summary,input,select,textarea').forEach(el=>{const r=el.getBoundingClientRect();const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden'||!r.width)return; if(el.closest('.visually-hidden')||el.classList.contains('skip-link'))return; if(r.height<44-0.5) out.push(el.tagName+' "'+(el.textContent||el.name).trim().slice(0,30)+'" '+Math.round(r.width)+'x'+Math.round(r.height))});return out}""")
                    report[f"{name}-{vpname}-{scheme}"]={"overflow":ov,"small_targets":small}
                    if name=="index" or (scheme=="light") :
                        await pg.screenshot(path=f"screenshots/{name}-{vpname}-{scheme}-full.png",full_page=True)
                    if name=="index":
                        await pg.screenshot(path=f"screenshots/{name}-{vpname}-{scheme}.png")
                if mobile:
                    await pg.goto(BASE+"index.html")
                    await pg.click(".menu-btn"); await pg.wait_for_timeout(400)
                    st=await pg.evaluate("""()=>({exp:document.querySelector('.menu-btn').getAttribute('aria-expanded'),vis:getComputedStyle(document.getElementById('site-menu')).visibility,focus:document.activeElement.textContent.trim(),inert:document.getElementById('site-menu').hasAttribute('inert')})""")
                    await pg.screenshot(path=f"screenshots/index-mobile-{scheme}-menu-open.png")
                    await pg.keyboard.press("Escape"); await pg.wait_for_timeout(400)
                    st2=await pg.evaluate("""()=>({exp:document.querySelector('.menu-btn').getAttribute('aria-expanded'),vis:getComputedStyle(document.getElementById('site-menu')).visibility,focus:document.activeElement.className,inert:document.getElementById('site-menu').hasAttribute('inert')})""")
                    # tap a link closes and navigates
                    await pg.click(".menu-btn"); await pg.wait_for_timeout(300)
                    await pg.click("#site-menu a[href='faq.html']"); await pg.wait_for_load_state()
                    report[f"menu-{scheme}"]={"open":st,"after_esc":st2,"nav_to":pg.url}
                    if scheme=="light":
                        await pg.goto(BASE+"faq.html"); await pg.click(".faq summary >> nth=0"); await pg.wait_for_timeout(300)
                        await pg.screenshot(path="screenshots/faq-mobile-light-open.png")
                        await pg.goto(BASE+"contact.html"); await pg.click("button[type=submit]"); await pg.wait_for_timeout(200)
                        await pg.screenshot(path="screenshots/contact-mobile-light-errors.png",full_page=True)
                        await pg.fill("#name","Test"); await pg.fill("#email","t@example.com"); await pg.fill("#message","My SSN is 123-45-6789")
                        await pg.click("button[type=submit]"); await pg.wait_for_timeout(200)
                        ssn=await pg.text_content("#message-error span")
                        await pg.fill("#message","Need help with a notice"); await pg.click("button[type=submit]"); await pg.wait_for_timeout(900)
                        ok=await pg.text_content("#form-status p")
                        report["form"]={"ssn_msg":ssn,"success":ok}
                report[f"errors-{vpname}-{scheme}"]=errs
                await ctx.close()
        # reduced motion check
        ctx=await b.new_context(viewport={"width":390,"height":844},reduced_motion="reduce"); pg=await ctx.new_page()
        await pg.goto(BASE+"index.html")
        report["reduced_motion_btn_transition"]=await pg.evaluate("getComputedStyle(document.querySelector('.btn')).transitionDuration")
        await b.close()
        json.dump(report,open(".build/report.json","w"),indent=1)
asyncio.run(main())
