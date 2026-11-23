// Ephemeral browser tests for guidance in GSAP skills. No production website access.
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const base = __dirname;
const root = process.env.GSAP_TEST_ROOT;
if (!root) throw new Error('GSAP_TEST_ROOT is required');
const out = process.env.GSAP_EVIDENCE_DIR || path.join(base, 'evidence');
fs.mkdirSync(out, { recursive: true });
const html = `<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{margin:0;font:16px Arial;overflow-x:hidden;background:#f3f6f9}
.hero{height:100vh;display:grid;place-items:center}
.spacer{height:120vh}.card{width:min(70vw,440px);height:240px;background:#214e8a;border-radius:24px;opacity:.3;transform:translateY(120px)}
.end{height:100vh}</style></head><body><main><section class="hero"><h1>GSAP scroll motion test</h1></section><section class="spacer"><div class="card" aria-label="animated card"></div></section><section class="end">End</section></main>
<script src="./gsap.min.js"></script><script src="./ScrollTrigger.min.js"></script>
<script>gsap.registerPlugin(ScrollTrigger);
window.tracker={reduced:matchMedia('(prefers-reduced-motion: reduce)').matches};
if(!window.tracker.reduced){
window.anim=gsap.to('.card',{y:0,opacity:1,scrollTrigger:{id:'smoke',trigger:'.card',start:'top bottom',end:'center center',scrub:true}});
}
</script></body></html>`;
async function main() {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.CHROME_BIN || '/usr/bin/google-chrome', args:['--no-sandbox'] });
  try {
    for (const setting of [
      {name:'desktop',viewport:{width:1440,height:900},reducedMotion:'no-preference'},
      {name:'mobile',viewport:{width:390,height:844},reducedMotion:'no-preference'},
      {name:'reduced',viewport:{width:390,height:844},reducedMotion:'reduce'}
    ]) {
      const page = await browser.newPage({viewport:setting.viewport,reducedMotion:setting.reducedMotion});
      const errors=[];page.on('pageerror', e=>errors.push(e.message));
      await page.goto('file://' + path.join(root,'index.html'),{waitUntil:'load'});
      await page.waitForTimeout(200);
      const before=await page.evaluate(()=>({gsap:typeof gsap,plugin:typeof ScrollTrigger,triggers:ScrollTrigger.getAll().length,overflow:document.documentElement.scrollWidth>innerWidth}));
      if(before.gsap!=='object'||before.plugin!=='function'||before.overflow)throw Error(setting.name+': incorrect gsap/plugin/overflow '+JSON.stringify(before));
      if(setting.reducedMotion==='reduce'){
        if(before.triggers!==0)throw Error('reduced motion has active scroll trigger');
      } else {
        if(before.triggers!==1)throw Error(setting.name+': missing trigger');
        await page.evaluate(()=>window.scrollTo(0,Math.round(document.body.scrollHeight/2)));
        await page.waitForTimeout(650);
        const current=await page.evaluate(()=>({progress:ScrollTrigger.getById('smoke').progress,opacity:parseFloat(getComputedStyle(document.querySelector('.card')).opacity)}));
        if(current.progress<=0 || current.opacity<=.3)throw Error(setting.name+': animation did not react '+JSON.stringify(current));
        const remaining=await page.evaluate(()=>{window.anim.scrollTrigger.kill();window.anim.kill();return ScrollTrigger.getAll().length});
        if(remaining!==0)throw Error(setting.name+': cleanup failed');
      }
      await page.screenshot({path:path.join(out,setting.name+'.png'),fullPage:true});
      if(errors.length)throw Error(setting.name+': page errors '+errors.join('; '));
      console.log(setting.name+': GSAP_BROWSER_SMOKE_PASS '+JSON.stringify(before));
      await page.close();
    }
  } finally { await browser.close(); }
}
main().catch(e=>{console.error(e);process.exit(1)});
