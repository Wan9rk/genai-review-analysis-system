<template>
  <div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-bar c-cyan"></i>各应用情感占比</span><span class="badge">堆叠柱状图</span></div><div ref="c1" class="cb"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-box c-cyan"></i>情感分数分布</span><span class="badge">柱状图</span></div><div ref="c2" class="cb"></div></div>
    </div>
    <h3 class="st"><i class="fa-solid fa-table-cells c-cyan"></i> 评分与情感<span class="acc">交叉分析</span></h3>
    <div class="glass-card tbl-wrap">
      <table>
        <thead><tr><th>评分区间</th><th>正面情感</th><th>中性情感</th><th>负面情感</th></tr></thead>
        <tbody><tr v-for="r in cross" :key="r.g"><td><strong>{{ r.g }}</strong></td><td :style="{color:r.p>50?'var(--accent-emerald)':'',fontWeight:r.p>50?'700':''}">{{ r.p }}%</td><td :style="{color:r.n>40?'var(--accent-amber)':'',fontWeight:r.n>40?'700':''}">{{ r.n }}%</td><td :style="{color:r.x>50?'var(--accent-red)':'',fontWeight:r.x>50?'700':''}">{{ r.x }}%</td></tr></tbody>
      </table>
    </div>
    <div class="insight"><i class="fa-solid fa-lightbulb c-cyan"></i><p><strong>分析洞察：</strong>好评中有 2.4% 的评论文本仍带负面情绪——这些通常是对产品总体满意但指出具体缺点的用户。单看星级评分不够，文本情感可以补充解释。</p></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { APPS, COLOR_ARR, ratingCross as cross } from '../data/mockData.js'
const c1=ref(null),c2=ref(null); let ch1=null,ch2=null
function draw(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);ch1.setOption({...dk,grid:{left:50,right:40,top:20,bottom:35},xAxis:{type:'category',data:APPS,axisTick:{show:false}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v+'%'}},series:[{name:'正面',type:'bar',stack:'s',data:[48,65,52,58,70],itemStyle:{color:'#34d399',opacity:.53},barWidth:28},{name:'中性',type:'bar',stack:'s',data:[28,22,27,25,20],itemStyle:{color:'#94a3b8',opacity:.53}},{name:'负面',type:'bar',stack:'s',data:[24,13,21,17,10],itemStyle:{color:'#f87171',opacity:.53}}],legend:{bottom:0,textStyle:{fontSize:11},icon:'roundRect'}})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:40,top:20,bottom:35},xAxis:{type:'category',data:APPS,axisTick:{show:false},axisLabel:{fontSize:11}},yAxis:{type:'value',min:-1,max:1,splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},series:[{type:'bar',data:[0.15,0.44,0.20,0.33,0.49],itemStyle:{color:p=>COLOR_ARR[p.dataIndex],opacity:.53,borderRadius:[8,8,0,0]},barWidth:28}]})}
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
.st{font-size:18px;font-weight:700;letter-spacing:-.3px;margin-bottom:16px;display:flex;align-items:center;gap:8px}.acc{color:var(--accent-purple)}
.tbl-wrap{overflow:hidden;margin-bottom:20px}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{padding:12px 16px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);background:rgba(15,23,42,.5);border-bottom:1px solid var(--border-subtle)}
tbody td{padding:10px 16px;border-bottom:1px solid rgba(56,189,248,.04);color:var(--text-secondary)}
tbody tr:hover td{background:rgba(56,189,248,.03);color:var(--text-primary)}
.insight{background:linear-gradient(135deg,rgba(56,189,248,.06) 0%,rgba(167,139,250,.06) 100%);border:1px solid var(--border-active);border-radius:var(--radius-lg);padding:18px 22px;display:flex;gap:14px}
.insight p{font-size:13px;color:var(--text-secondary);line-height:1.7}.insight strong{color:var(--accent-cyan)}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
