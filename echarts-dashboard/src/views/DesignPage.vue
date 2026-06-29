<template>
  <div>
    <h3 class="st"><i class="fa-solid fa-clipboard-list c-cyan"></i> 需求<span class="acc">分析</span></h3>
    <div class="grid-2">
      <div class="qc"><div class="qc-h"><i class="fa-solid fa-users c-purple"></i>用户需求</div><p>学生、普通用户和产品分析人员希望了解不同生成式 AI 应用的真实用户体验，尤其是用户为什么给好评或差评。</p></div>
      <div class="qc"><div class="qc-h"><i class="fa-solid fa-list-check c-purple"></i>功能需求</div><ul><li>导入 Kaggle 评论 CSV 数据</li><li>字段自动识别、去重、缺失值处理</li><li>评分分布、好评率、差评率统计</li><li>评论情感分析</li><li>用户痛点主题识别</li><li>多产品横向对比 + 时间趋势</li><li>典型评论展示</li></ul></div>
    </div>

    <h3 class="st"><i class="fa-solid fa-diagram-project c-cyan"></i> 系统<span class="acc">架构</span></h3>
    <div class="arch-row">
      <div v-for="(l,i) in layers" :key="i" class="arch-item">
        <div class="arch-box glass-card"><i :class="l.icon"></i><h4>{{ l.title }}</h4><p>{{ l.desc }}</p></div>
        <div v-if="i<layers.length-1" class="arch-arr"><i class="fa-solid fa-arrow-right"></i></div>
      </div>
    </div>

    <h3 class="st"><i class="fa-solid fa-triangle-exclamation c-cyan"></i> 项目<span class="acc">边界</span></h3>
    <div class="insight warn"><i class="fa-solid fa-shield-halved" style="color:var(--accent-red)"></i><p><strong style="color:var(--accent-red)">重要声明：</strong>本系统分析的是<strong>应用商店评论中的用户体验口碑</strong>，不能直接推出哪个大模型能力最强；汇报时应避免夸大结论。</p></div>
  </div>
</template>

<script setup>
const layers=[
  {icon:'fa-solid fa-database',title:'Kaggle 公开数据',desc:'评论数据集'},
  {icon:'fa-solid fa-upload',title:'数据接入层',desc:'CSV 上传/目录读取'},
  {icon:'fa-solid fa-broom',title:'数据预处理层',desc:'字段统一·去重·清洗'},
  {icon:'fa-solid fa-brain',title:'文本分析层',desc:'情感·主题·关键词'},
  {icon:'fa-solid fa-chart-pie',title:'统计分析层',desc:'评分·对比·趋势'},
  {icon:'fa-solid fa-display',title:'可视化展示层',desc:'Vue 3 + ECharts'},
]
</script>

<style scoped>
.st{font-size:18px;font-weight:700;letter-spacing:-.3px;margin-bottom:16px;display:flex;align-items:center;gap:8px}.acc{color:var(--accent-purple)}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:24px}
.qc{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:18px 20px}
.qc-h{font-size:14px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.qc p{font-size:13px;color:var(--text-secondary);line-height:1.7}
.qc ul{font-size:13px;color:var(--text-secondary);line-height:2;padding-left:18px}
.arch-row{display:flex;align-items:center;gap:14px;padding:20px 10px;margin-bottom:24px;overflow-x:auto}
.arch-item{display:flex;align-items:center;gap:14px;flex-shrink:0}
.arch-box{text-align:center;padding:20px 18px;min-width:140px}
.arch-box i{font-size:26px;margin-bottom:8px;background:var(--gradient-hero);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;display:block}
.arch-box h4{font-size:13px;font-weight:700;margin-bottom:2px}
.arch-box p{font-size:11px;color:var(--text-muted)}
.arch-arr{font-size:18px;color:var(--accent-cyan);animation:ap 2s ease-in-out infinite}
@keyframes ap{0%,100%{opacity:.3;transform:translateX(0)}50%{opacity:1;transform:translateX(3px)}}
.insight{background:linear-gradient(135deg,rgba(56,189,248,.06) 0%,rgba(167,139,250,.06) 100%);border:1px solid var(--border-active);border-radius:var(--radius-lg);padding:18px 22px;display:flex;gap:14px}
.insight p{font-size:13px;color:var(--text-secondary);line-height:1.7}
.warn{border-color:rgba(248,113,113,.3);background:rgba(248,113,113,.04)}
.c-cyan{color:var(--accent-cyan);margin-right:6px}.c-purple{color:var(--accent-purple);margin-right:6px}
</style>
