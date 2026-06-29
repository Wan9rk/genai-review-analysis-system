<template>
  <div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-tags c-cyan"></i>痛点/主题分布</span><span class="badge">分组柱状图</span></div><div ref="c1" class="cb"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-circle-exclamation c-cyan"></i>低分评论主题占比</span><span class="badge">⭐ 重点</span></div><div ref="c2" class="cb"></div></div>
    </div>
    <div class="insight"><i class="fa-solid fa-comment-dots c-cyan"></i><p><strong>汇报重点：</strong>低分评论主题分布是整场汇报中最有价值的图表——直接说明用户差评主要来自哪些产品体验问题。<strong>Accuracy/Logic Issues（回答质量）</strong>和<strong>Pricing/Subscription（付费订阅）</strong>是占比最高的差评原因。</p></div>
    <div class="glass-card tbl-wrap">
      <div class="thd"><h3><i class="fa-solid fa-list-check c-cyan"></i>各应用痛点主题明细</h3></div>
      <table><thead><tr><th>主题类别</th><th v-for="a in APPS" :key="a">{{ a }}</th></tr></thead>
        <tbody><tr v-for="t in themes" :key="t.t"><td><strong>{{ t.t }}</strong></td><td v-for="(v,i) in t.v" :key="i"><span class="badge-tag" :style="{color:v>20?'var(--accent-red)':v<10?'var(--accent-emerald)':'var(--accent-amber)'}">{{ v }}%</span></td></tr></tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { APPS, COLOR_ARR, themes, lowTheme } from '../data/mockData.js'
const c1=ref(null),c2=ref(null); let ch1=null,ch2=null
const tl=themes.map(t=>t.t.replace('/','/\n')), ltl=lowTheme.map(t=>t.t)

function draw(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);ch1.setOption({...dk,grid:{left:50,right:40,top:20,bottom:50},xAxis:{type:'category',data:tl,axisTick:{show:false},axisLabel:{fontSize:9}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v+'%'}},series:APPS.map((a,i)=>({name:a,type:'bar',data:themes.map(t=>t.v[i]),itemStyle:{color:COLOR_ARR[i],opacity:.53,borderRadius:3},barWidth:14})),legend:{top:'bottom',textStyle:{fontSize:10},icon:'roundRect'}})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:40,top:20,bottom:50},xAxis:{type:'category',data:ltl,axisTick:{show:false},axisLabel:{fontSize:10}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v+'%'}},series:[{type:'bar',data:lowTheme.map(t=>t.v),itemStyle:{color:p=>['#f87171','#fb923c','#fbbf24','#a78bfa','#38bdf8','#34d399','#94a3b8'][p.dataIndex],opacity:.53,borderRadius:[6,6,0,0]},barWidth:28,label:{show:true,position:'top',color:'#94a3b8',fontSize:11,formatter:p=>p.value+'%'}}]})}
}
onMounted(()=>nextTick(draw)); onUnmounted(()=>{ch1?.dispose();ch2?.dispose()})
</script>

<style scoped>
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:20px}
.chart-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px 20px;transition:all var(--transition-fast)}
.chart-card:hover{border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.ch{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;font-size:14px;font-weight:700}
.badge{font-size:10px;padding:3px 10px;border-radius:12px;background:rgba(167,139,250,.1);color:var(--accent-purple);font-weight:600}
.cb{width:100%;height:300px}
.insight{background:linear-gradient(135deg,rgba(56,189,248,.06) 0%,rgba(167,139,250,.06) 100%);border:1px solid var(--border-active);border-radius:var(--radius-lg);padding:18px 22px;display:flex;gap:14px;margin-bottom:20px}
.insight p{font-size:13px;color:var(--text-secondary);line-height:1.7}.insight strong{color:var(--accent-cyan)}
.tbl-wrap{overflow:hidden}.thd{padding:16px 20px;border-bottom:1px solid var(--border-subtle)}
.thd h3{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
table{width:100%;border-collapse:collapse;font-size:12px}
thead th{padding:12px 14px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);background:rgba(15,23,42,.5);border-bottom:1px solid var(--border-subtle)}
tbody td{padding:10px 14px;border-bottom:1px solid rgba(56,189,248,.04);color:var(--text-secondary)}
tbody tr:hover td{background:rgba(56,189,248,.03);color:var(--text-primary)}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
