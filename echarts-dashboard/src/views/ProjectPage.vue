<template>
  <div>
    <div class="insight"><i class="fa-solid fa-bullseye c-cyan"></i><p><strong>核心定位：</strong>本系统面向"大数据技术与应用"课程期末项目，核心目标不是判断哪个大模型能力最强，而是基于<strong>真实用户评论数据</strong>，分析生成式 AI 应用在<strong>用户体验层面</strong>的口碑差异与主要痛点。</p></div>
    <h3 class="st"><i class="fa-solid fa-circle-question c-cyan"></i> 系统要回答的<span class="acc">核心问题</span></h3>
    <div class="grid-3">
      <div class="qc"><div class="qc-h"><i class="fa-solid fa-scale-balanced c-purple"></i>口碑差异</div><p>不同生成式 AI 应用的评分和评论情感有什么差异？哪些产品用户体验口碑更好？</p></div>
      <div class="qc"><div class="qc-h"><i class="fa-solid fa-thumbs-up c-purple"></i>满意/不满</div><p>用户对生成式 AI 应用主要满意在哪里？不满意又集中在哪些方面？</p></div>
      <div class="qc"><div class="qc-h"><i class="fa-solid fa-clock-rotate-left c-purple"></i>时间变化</div><p>ChatGPT 的评论数量、评分和负面反馈是否随时间变化？趋势如何？</p></div>
    </div>
    <h3 class="st"><i class="fa-solid fa-database c-cyan"></i> 统一数据<span class="acc">字段说明</span></h3>
    <div class="glass-card tbl-wrap">
      <table>
        <thead><tr><th>字段名</th><th>含义</th><th>系统用途</th></tr></thead>
        <tbody><tr v-for="f in fields" :key="f[0]"><td><strong>{{ f[0] }}</strong></td><td>{{ f[1] }}</td><td>{{ f[2] }}</td></tr></tbody>
      </table>
    </div>
  </div>
</template>
<script setup>import { fields } from '../data/mockData.js'</script>
<style scoped>
.insight{background:linear-gradient(135deg,rgba(56,189,248,.06) 0%,rgba(167,139,250,.06) 100%);border:1px solid var(--border-active);border-radius:var(--radius-lg);padding:18px 22px;display:flex;gap:14px;margin-bottom:20px}
.insight p{font-size:13px;color:var(--text-secondary);line-height:1.7}.insight strong{color:var(--accent-cyan)}
.st{font-size:18px;font-weight:700;letter-spacing:-.3px;margin-bottom:16px;display:flex;align-items:center;gap:8px}.acc{color:var(--accent-purple)}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}
.qc{background:var(--bg-glass);backdrop-filter:blur(12px);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:18px 20px}
.qc-h{font-size:14px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.qc p{font-size:13px;color:var(--text-secondary);line-height:1.7}
.tbl-wrap{overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{padding:12px 16px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-muted);background:rgba(15,23,42,.5);border-bottom:1px solid var(--border-subtle)}
tbody td{padding:10px 16px;border-bottom:1px solid rgba(56,189,248,.04);color:var(--text-secondary)}
tbody tr:hover td{background:rgba(56,189,248,.03);color:var(--text-primary)}
.c-cyan{color:var(--accent-cyan);margin-right:8px}.c-purple{color:var(--accent-purple);margin-right:8px}
</style>
