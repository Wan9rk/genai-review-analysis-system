<template>
  <div>
    <div class="kpi-row">
      <div class="kpi-card" v-for="(k,i) in kpis" :key="i" :style="{'--accent':k.color}">
        <div class="kpi-icon"><i :class="k.icon"></i></div>
        <div class="kpi-value">{{ k.value }}</div>
        <div class="kpi-label">{{ k.label }}</div>
        <div class="kpi-delta" :class="k.deltaClass">{{ k.delta }}</div>
      </div>
    </div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-pie c-cyan"></i>各应用评论数量</span><span class="badge">评论量</span></div><div ref="c1" class="cb"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-simple c-cyan"></i>各应用平均评分</span><span class="badge">评分</span></div><div ref="c2" class="cb"></div></div>
    </div>
    <div class="glass-card tbl-wrap">
      <div class="thd"><h3><i class="fa-solid fa-table-list c-cyan"></i>各产品核心指标一览</h3></div>
      <table>
        <thead><tr><th>应用</th><th>评论数</th><th>平均评分</th><th>好评率</th><th>差评率</th><th>平均情感分</th><th>平均点赞数</th></tr></thead>
        <tbody>
          <tr v-for="p in profiles" :key="p.App">
            <td><i :class="ai(p.App)" :style="{color:AC[p.App]}"></i> <strong>{{ p.App }}</strong></td>
            <td>{{ p.count.toLocaleString() }}</td>
            <td><span class="badge-tag" :class="p.rating>=4?'high':p.rating>=3?'mid':'low'">{{ p.rating }}</span></td>
            <td>{{ p.good }}%</td><td>{{ p.bad }}%</td><td>{{ p.sentiment }}</td><td>{{ p.thumbs }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { APP_COLORS as AC, APPS, COLOR_ARR, profiles } from '../data/mockData.js'

const c1=ref(null),c2=ref(null); let ch1=null,ch2=null
const ai=a=>({ChatGPT:'fa-brands fa-openai',Claude:'fa-solid fa-robot',Gemini:'fa-brands fa-google',Copilot:'fa-brands fa-microsoft',Perplexity:'fa-solid fa-magnifying-glass'}[a]||'')
const kpis=[
  {icon:'fa-solid fa-comments',value:'99,988',label:'评论总数',delta:'↑ +12.5% 较上月',deltaClass:'up',color:'#38bdf8'},
  {icon:'fa-solid fa-layer-group',value:'5',label:'AI 应用数量',delta:'✓ 覆盖主流产品',deltaClass:'up',color:'#a78bfa'},
  {icon:'fa-solid fa-star',value:'3.95',label:'平均评分',delta:'↑ +0.14 vs 上月',deltaClass:'up',color:'#34d399'},
  {icon:'fa-solid fa-percent',value:'17.6%',label:'差评率',delta:'↓ -1.9% 较上月',deltaClass:'down',color:'#f472b6'},
]

function draw(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);ch1.setOption({...dk,grid:{left:110,right:50,top:10,bottom:10,containLabel:true},xAxis:{type:'value',axisLabel:{formatter:v=>v>=1000?(v/1000).toFixed(1)+'k':v},splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},yAxis:{type:'category',data:[...APPS].reverse(),axisLine:{show:false},axisTick:{show:false}},series:[{type:'bar',data:[10000,10000,10000,10000,10000],itemStyle:{borderRadius:[0,8,8,0],color:p=>COLOR_ARR[4-p.dataIndex],opacity:.6},barWidth:22,label:{show:true,position:'right',color:'#94a3b8',fontSize:12}}]})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:10,top:10,bottom:30},xAxis:{type:'category',data:APPS,axisLabel:{fontSize:11},axisTick:{show:false}},yAxis:{type:'value',min:0,max:5,splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},series:[{type:'bar',data:[3.81,4.11,3.74,3.96,4.15],itemStyle:{borderRadius:[8,8,0,0],color:p=>COLOR_ARR[p.dataIndex],opacity:.6},barWidth:28}]})}
}
onMounted(()=>nextTick(draw))
onUnmounted(()=>{ch1?.dispose();ch2?.dispose()})
</script>

<style scoped>
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}
.kpi-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:18px 20px;position:relative;overflow:hidden;transition:all var(--transition-fast)}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--accent);border-radius:3px 3px 0 0}
.kpi-card:hover{transform:translateY(-3px);border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.kpi-icon{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;margin-bottom:10px;background:rgba(255,255,255,.04);color:var(--accent)}
.kpi-value{font-size:28px;font-weight:800;font-family:var(--font-mono);color:var(--accent);letter-spacing:-1px}
.kpi-label{font-size:12px;color:var(--text-muted);margin-top:2px}
.kpi-delta{font-size:11px;margin-top:4px}
.kpi-delta.up{color:var(--accent-emerald)}.kpi-delta.down{color:var(--accent-red)}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:20px}
.chart-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px 20px;transition:all var(--transition-fast)}
.chart-card:hover{border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.ch{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;font-size:14px;font-weight:700}
.badge{font-size:10px;padding:3px 10px;border-radius:12px;background:rgba(167,139,250,.1);color:var(--accent-purple);font-weight:600}
.cb{width:100%;height:280px}
.tbl-wrap{overflow:hidden}.thd{padding:16px 20px;border-bottom:1px solid var(--border-subtle)}
.thd h3{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{padding:12px 16px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);background:rgba(15,23,42,.5);border-bottom:1px solid var(--border-subtle)}
tbody td{padding:10px 16px;border-bottom:1px solid rgba(56,189,248,.04);color:var(--text-secondary)}
tbody tr:hover td{background:rgba(56,189,248,.03);color:var(--text-primary)}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
