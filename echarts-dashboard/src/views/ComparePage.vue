<template>
  <div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-bar c-cyan"></i>评分分布对比</span><span class="badge">分组柱状图</span></div><div ref="c1" class="cb"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-scatter c-cyan"></i>好评率 vs 差评率</span><span class="badge">散点图</span></div><div ref="c2" class="cb"></div></div>
    </div>
    <div class="insight"><i class="fa-solid fa-circle-exclamation c-cyan"></i><p><strong>汇报提示：</strong>这里比较的是<strong>用户评论中的体验口碑</strong>，不等同于模型客观能力排名。Perplexity 和 Claude 的好评率较高，背后可能是用户群体和使用场景的差异。</p></div>
    <div class="glass-card tbl-wrap">
      <div class="thd"><h3><i class="fa-solid fa-table c-cyan"></i>口碑指标明细</h3></div>
      <table><thead><tr><th>应用</th><th>评论数</th><th>平均评分</th><th>好评率</th><th>差评率</th><th>平均情感分</th><th>平均点赞数</th></tr></thead>
        <tbody><tr v-for="p in profiles" :key="p.App"><td><strong>{{ p.App }}</strong></td><td>{{ p.count.toLocaleString() }}</td><td><span class="badge-tag" :class="p.rating>=4?'high':p.rating>=3?'mid':'low'">{{ p.rating }}</span></td><td>{{ p.good }}%</td><td>{{ p.bad }}%</td><td>{{ p.sentiment }}</td><td>{{ p.thumbs }}</td></tr></tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { APPS, COLOR_ARR, profiles } from '../data/mockData.js'
const c1=ref(null),c2=ref(null); let ch1=null,ch2=null
const D={ChatGPT:[1000,1482,750,1900,4868],Claude:[450,780,1050,2650,5070],Gemini:[980,1340,1180,2350,4150],Copilot:[660,1000,1050,2650,4640],Perplexity:[430,700,950,2750,5170]}
function draw(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);ch1.setOption({...dk,grid:{left:50,right:15,top:15,bottom:50},xAxis:{type:'category',data:['1星','2星','3星','4星','5星'],axisTick:{show:false}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v>=1000?(v/1000).toFixed(1)+'k':v}},series:APPS.map((a,i)=>({name:a,type:'bar',data:D[a],itemStyle:{color:COLOR_ARR[i],opacity:.53,borderRadius:4},barWidth:16})),legend:{top:'bottom',textStyle:{fontSize:11},icon:'roundRect'}})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:15,top:15,bottom:50},xAxis:{type:'value',name:'差评率 (%)',nameTextStyle:{color:'#94a3b8',fontSize:11},splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},yAxis:{type:'value',name:'好评率 (%)',nameTextStyle:{color:'#94a3b8',fontSize:11},splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},series:[{type:'scatter',data:[22.1,11.3,18.9,14.7,8.5].map((x,i)=>[x,[48.2,68.5,54.1,61.2,72.8][i]]),symbolSize:[28,22,18,16,14],itemStyle:{color:p=>COLOR_ARR[p.dataIndex],opacity:.53},label:{show:true,formatter:p=>APPS[p.dataIndex],position:'top',fontSize:11,color:'#94a3b8'}}]})}
}
onMounted(()=>nextTick(draw))
onUnmounted(()=>{ch1?.dispose();ch2?.dispose()})
</script>
<style scoped>
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:20px}
.chart-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px 20px;transition:all var(--transition-fast)}
.chart-card:hover{border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.ch{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;font-size:14px;font-weight:700}
.badge{font-size:10px;padding:3px 10px;border-radius:12px;background:rgba(167,139,250,.1);color:var(--accent-purple);font-weight:600}
.cb{width:100%;height:280px}
.insight{background:linear-gradient(135deg,rgba(56,189,248,.06) 0%,rgba(167,139,250,.06) 100%);border:1px solid var(--border-active);border-radius:var(--radius-lg);padding:18px 22px;display:flex;gap:14px;margin-bottom:20px}
.insight p{font-size:13px;color:var(--text-secondary);line-height:1.7}.insight strong{color:var(--accent-cyan)}
.tbl-wrap{overflow:hidden}.thd{padding:16px 20px;border-bottom:1px solid var(--border-subtle)}
.thd h3{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{padding:12px 16px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);background:rgba(15,23,42,.5);border-bottom:1px solid var(--border-subtle)}
tbody td{padding:10px 16px;border-bottom:1px solid rgba(56,189,248,.04);color:var(--text-secondary)}
tbody tr:hover td{background:rgba(56,189,248,.03);color:var(--text-primary)}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
