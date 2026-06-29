<template>
  <div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-cloud c-cyan"></i>低分评论高频关键词</span><span class="badge">词频</span></div><div ref="c1" class="cb-tall"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-file-word c-cyan"></i>各应用差异化关键词 TF-IDF</span><span class="badge">差异分析</span></div><div ref="c2" class="cb-tall"></div></div>
    </div>
    <h3 class="st"><i class="fa-solid fa-quote-right c-cyan"></i> 典型评论<span class="acc">精选</span></h3>
    <div class="rv-grid">
      <div class="rv-card" v-for="(r,i) in reviews" :key="i">
        <div class="rv-h"><span class="rv-app"><i :class="ai(r.a)" :style="{color:AC[r.a]}"></i> {{ r.a }}</span><div class="rv-meta"><span class="badge-tag" :class="r.r>=4?'high':r.r>=3?'mid':'low'">{{ r.r }}⭐</span><span class="sentiment-tag" :class="r.s==='正面'?'positive':r.s==='中性'?'neutral':'negative'">{{ r.s }}</span></div></div>
        <p class="rv-tx">{{ r.tx }}</p>
        <div class="rv-ft"><span><i class="fa-solid fa-tag"></i>{{ r.t }}</span><span><i class="fa-solid fa-thumbs-up"></i>{{ r.th }}</span><span><i class="fa-regular fa-calendar"></i>{{ r.d }}</span></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { APP_COLORS as AC, APPS, keywords, tfidf, reviews } from '../data/mockData.js'
const c1=ref(null),c2=ref(null); let ch1=null,ch2=null
const ai=a=>({ChatGPT:'fa-brands fa-openai',Claude:'fa-solid fa-robot',Gemini:'fa-brands fa-google',Copilot:'fa-brands fa-microsoft',Perplexity:'fa-solid fa-magnifying-glass'}[a]||'')

function draw(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);const kw=[...keywords].reverse();ch1.setOption({...dk,grid:{left:100,right:20,top:10,bottom:10},xAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},yAxis:{type:'category',data:kw.map(k=>k.w),axisLine:{show:false},axisTick:{show:false}},series:[{type:'bar',data:kw.map(k=>k.c),itemStyle:{borderRadius:[0,6,6,0],color:p=>kw[p.dataIndex].c>1500?'#f87171':kw[p.dataIndex].c>800?'#fbbf24':'#94a3b8',opacity:.6},barWidth:16}]})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:10,top:20,bottom:10},xAxis:{type:'category',data:APPS,axisTick:{show:false},axisLabel:{fontSize:10}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v.toFixed(2)}},series:tfidf.map((k,i)=>({name:k.k,type:'bar',data:k.v,itemStyle:{color:['#f87171','#fbbf24','#fb923c','#34d399','#a78bfa'][i],opacity:.53,borderRadius:3},barWidth:14})),legend:{bottom:0,textStyle:{fontSize:9},icon:'roundRect',itemWidth:12}})}
}
onMounted(()=>nextTick(draw)); onUnmounted(()=>{ch1?.dispose();ch2?.dispose()})
</script>

<style scoped>
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:20px}
.chart-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px 20px;transition:all var(--transition-fast)}
.chart-card:hover{border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.ch{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;font-size:14px;font-weight:700}
.badge{font-size:10px;padding:3px 10px;border-radius:12px;background:rgba(167,139,250,.1);color:var(--accent-purple);font-weight:600}
.cb-tall{width:100%;height:380px}
.st{font-size:18px;font-weight:700;letter-spacing:-.3px;margin-bottom:16px;display:flex;align-items:center;gap:8px}.acc{color:var(--accent-purple)}
.rv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.rv-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px;transition:all var(--transition-fast)}
.rv-card:hover{border-color:var(--border-active);transform:translateY(-2px)}
.rv-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.rv-app{font-size:12px;font-weight:700;color:var(--accent-cyan)}.rv-meta{display:flex;gap:6px;align-items:center}
.rv-tx{font-size:12px;color:var(--text-secondary);line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.rv-ft{display:flex;align-items:center;justify-content:space-between;margin-top:10px;padding-top:10px;border-top:1px solid var(--border-subtle);font-size:11px;color:var(--text-muted)}
.rv-ft i{margin-right:3px}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
