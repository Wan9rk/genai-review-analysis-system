<template>
  <div>
    <div class="tab-bar"><span class="tab-label">选择应用：</span><div class="tab-grp"><button v-for="a in appOpts" :key="a" class="tab-btn" :class="{active:sel===a}" @click="sel=a;redraw()">{{ a }}</button></div></div>
    <div class="grid-2">
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-line c-cyan"></i>月度评论数量变化</span></div><div ref="c1" class="cb"></div></div>
      <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-line c-cyan"></i>月度平均评分变化</span></div><div ref="c2" class="cb"></div></div>
    </div>
    <div class="chart-card"><div class="ch"><span><i class="fa-solid fa-chart-line c-cyan"></i>月度差评率变化</span><span class="badge">趋势预警</span></div><div ref="c3" class="cb"></div></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import { months, trendCounts, trendRatings, trendBad } from '../data/mockData.js'
const c1=ref(null),c2=ref(null),c3=ref(null); let ch1=null,ch2=null,ch3=null
const sel=ref('ChatGPT'), appOpts=['ChatGPT','Claude','Gemini','Copilot','Perplexity','全部']
function redraw(){drawT()}
function drawT(){
  const dk={textStyle:{color:'#94a3b8'}}
  if(c1.value){ch1?.dispose();ch1=echarts.init(c1.value);ch1.setOption({...dk,grid:{left:50,right:10,top:10,bottom:10},xAxis:{type:'category',data:months,axisTick:{show:false},axisLabel:{fontSize:10}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v>=1000?(v/1000).toFixed(1)+'k':v}},series:[{type:'line',data:trendCounts,smooth:true,symbol:'circle',symbolSize:6,lineStyle:{color:'#38bdf8',width:2.5},itemStyle:{color:'#38bdf8'},areaStyle:{color:'rgba(56,189,248,.1)'}}]})}
  if(c2.value){ch2?.dispose();ch2=echarts.init(c2.value);ch2.setOption({...dk,grid:{left:50,right:10,top:10,bottom:10},xAxis:{type:'category',data:months,axisTick:{show:false},axisLabel:{fontSize:10}},yAxis:{type:'value',min:1,max:5,splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}}},series:[{type:'line',data:trendRatings,smooth:true,symbol:'circle',symbolSize:6,lineStyle:{color:'#a78bfa',width:2.5},itemStyle:{color:'#a78bfa'},areaStyle:{color:'rgba(167,139,250,.1)'}}]})}
  if(c3.value){ch3?.dispose();ch3=echarts.init(c3.value);ch3.setOption({...dk,grid:{left:50,right:10,top:10,bottom:10},xAxis:{type:'category',data:months,axisTick:{show:false},axisLabel:{fontSize:10}},yAxis:{type:'value',splitLine:{lineStyle:{color:'rgba(56,189,248,.06)'}},axisLabel:{formatter:v=>v+'%'}},series:[{type:'line',data:trendBad,smooth:true,symbol:'circle',symbolSize:6,lineStyle:{color:'#f472b6',width:2.5},itemStyle:{color:'#f472b6'},areaStyle:{color:'rgba(244,114,182,.1)'}}]})}
}
onMounted(()=>nextTick(drawT)); onUnmounted(()=>{ch1?.dispose();ch2?.dispose();ch3?.dispose()})
</script>

<style scoped>
.tab-bar{display:flex;align-items:center;gap:12px;margin-bottom:18px}
.tab-label{font-size:13px;color:var(--text-muted);font-weight:600}
.tab-grp{display:flex;gap:4px;background:var(--bg-card);border-radius:12px;padding:4px}
.tab-btn{padding:7px 16px;border-radius:10px;font-size:12px;font-weight:600;cursor:pointer;border:none;background:transparent;color:var(--text-muted);transition:all var(--transition-fast);font-family:var(--font-ui)}
.tab-btn.active{background:var(--gradient-card);color:var(--accent-cyan);box-shadow:0 0 12px rgba(56,189,248,.1)}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:16px}
.chart-card{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:16px 20px;transition:all var(--transition-fast);margin-bottom:16px}
.chart-card:hover{border-color:var(--border-active);box-shadow:var(--shadow-glow-cyan)}
.ch{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;font-size:14px;font-weight:700}
.badge{font-size:10px;padding:3px 10px;border-radius:12px;background:rgba(167,139,250,.1);color:var(--accent-purple);font-weight:600}
.cb{width:100%;height:240px}
.c-cyan{color:var(--accent-cyan);margin-right:6px}
</style>
