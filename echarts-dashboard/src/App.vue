<template>
  <div class="dashboard-root">
    <div class="dashboard-bg">
      <div class="bg-grid"></div>
      <div class="bg-orb"></div>
    </div>

    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo-box">
          <div class="logo-icon"><i class="fa-solid fa-chart-line"></i></div>
          <div class="logo-text"><h2>GenAI Review</h2><span>Analytics Platform</span></div>
        </div>
      </div>
      <div class="sidebar-section">
        <div class="upload-zone" @click="simUpload">
          <i :class="upIcon"></i><p>{{ upText }}</p><small>{{ upSub }}</small>
        </div>
        <div class="file-loaded" v-if="upDone"><i class="fa-solid fa-circle-check"></i><span>已加载 2 个数据集 · 99,988 条</span></div>
      </div>
      <div class="sidebar-section toggles">
        <div class="t-row"><span><i class="fa-solid fa-folder-open c-cyan"></i>读取 data/ 目录</span><label class="t-sw"><input type="checkbox" checked><span class="t-knob"></span></label></div>
        <div class="t-row"><span><i class="fa-solid fa-flask c-purple"></i>使用示例数据</span><label class="t-sw"><input type="checkbox"><span class="t-knob"></span></label></div>
      </div>
      <nav class="sidebar-nav scrollbar-thin">
        <template v-for="g in navGroups" :key="g.label">
          <div class="nav-label">{{ g.label }}</div>
          <div v-for="it in g.items" :key="it.id" class="nav-item" :class="{active:page===it.id}" @click="page=it.id">
            <i :class="it.icon"></i>{{ it.name }}<span class="nav-badge" v-if="it.badge">{{ it.badge }}</span>
          </div>
        </template>
      </nav>
      <div class="sidebar-footer"><span class="s-dot"></span><span class="s-text">系统就绪 · <strong>99,988</strong> 条</span></div>
    </aside>

    <main class="main-area">
      <header class="topbar">
        <div class="topbar-left"><h1>{{ meta[page]?.[0] }}</h1><p>{{ meta[page]?.[1] }}</p></div>
        <div class="topbar-right">
          <div class="search-box"><i class="fa-solid fa-magnifying-glass"></i><input placeholder="搜索应用或关键词..."></div>
          <button class="btn-ghost"><i class="fa-solid fa-sliders"></i>筛选器</button>
          <button class="btn-primary"><i class="fa-solid fa-download"></i>导出报告</button>
        </div>
      </header>
      <div class="filter-bar">
        <span class="f-label"><i class="fa-solid fa-filter"></i>应用：</span>
        <span v-for="a in filterApps" :key="a.key" class="f-chip" :class="{active:selApps.includes(a.key)}" @click="toggleApp(a.key)">
          <i v-if="a.icon" :class="a.icon"></i>{{ a.label }}
        </span>
        <span class="f-sep"></span><span class="f-label">评分：1-5⭐</span>
      </div>
      <div class="page-container scrollbar-thin">
        <transition name="fade" mode="out-in">
          <OverviewPage   v-if="page==='overview'"   key="overview"   :apps="selApps" />
          <ProjectPage    v-else-if="page==='project'"   key="project" />
          <ComparePage    v-else-if="page==='compare'"   key="compare"   :apps="selApps" />
          <SentimentPage  v-else-if="page==='sentiment'" key="sentiment" :apps="selApps" />
          <PainPointsPage v-else-if="page==='painpoints'" key="painpoints" :apps="selApps" />
          <TrendPage      v-else-if="page==='trend'"     key="trend"     :apps="selApps" />
          <KeywordsPage   v-else-if="page==='keywords'"  key="keywords"  :apps="selApps" />
          <DesignPage     v-else-if="page==='design'"    key="design" />
        </transition>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import OverviewPage   from './views/OverviewPage.vue'
import ProjectPage    from './views/ProjectPage.vue'
import ComparePage    from './views/ComparePage.vue'
import SentimentPage  from './views/SentimentPage.vue'
import PainPointsPage from './views/PainPointsPage.vue'
import TrendPage      from './views/TrendPage.vue'
import KeywordsPage   from './views/KeywordsPage.vue'
import DesignPage     from './views/DesignPage.vue'

const upDone = ref(false); const upIcon = ref('fa-solid fa-cloud-arrow-up'); const upText = ref('上传 CSV 数据集'); const upSub = ref('支持 Kaggle 评论数据')
function simUpload() {
  upDone.value = true; upIcon.value = 'fa-solid fa-circle-check c-emerald'; upText.value = '数据加载成功!'; upSub.value = '已识别 2 个 Kaggle 数据集'
  setTimeout(() => { upDone.value = false; upIcon.value = 'fa-solid fa-cloud-arrow-up'; upText.value = '上传 CSV 数据集'; upSub.value = '支持 Kaggle 评论数据' }, 2500)
}

const page = ref('overview')
const navGroups = [
  { label:'数据与总览', items:[
    {id:'overview', name:'总览看板', icon:'fa-solid fa-gauge-high'},
    {id:'project', name:'项目与字段说明', icon:'fa-solid fa-circle-info'},
  ]},
  { label:'核心分析', items:[
    {id:'compare', name:'产品口碑对比', icon:'fa-solid fa-chart-bar'},
    {id:'sentiment', name:'情感分析', icon:'fa-solid fa-face-smile'},
    {id:'painpoints', name:'痛点主题分析', icon:'fa-solid fa-magnifying-glass-chart', badge:'核心'},
  ]},
  { label:'深度挖掘', items:[
    {id:'trend', name:'时间趋势分析', icon:'fa-solid fa-chart-line'},
    {id:'keywords', name:'关键词与典型评论', icon:'fa-solid fa-key'},
  ]},
  { label:'关于系统', items:[
    {id:'design', name:'系统设计说明', icon:'fa-solid fa-sitemap'},
  ]},
]
const meta = {
  overview:['总览看板','生成式 AI 应用用户体验数据全景视图'],
  project:['项目与字段说明','系统定位、数据来源与标准字段定义'],
  compare:['产品口碑对比','不同 AI 应用的评分分布与口碑画像'],
  sentiment:['情感分析','多维度情感倾向与评分交叉分析'],
  painpoints:['痛点主题分析','用户投诉热点与各产品差异对比'],
  trend:['时间趋势分析','评论量、评分与差评率的月度变化'],
  keywords:['关键词与典型评论','高频词提取、差异化分析与代表性评论'],
  design:['系统设计说明','需求分析、系统架构与项目边界'],
}

const filterApps = [
  {key:'all',label:'全部'},{key:'ChatGPT',label:'ChatGPT',icon:'fa-brands fa-openai'},
  {key:'Claude',label:'Claude',icon:'fa-solid fa-robot'},{key:'Gemini',label:'Gemini',icon:'fa-brands fa-google'},
  {key:'Copilot',label:'Copilot',icon:'fa-brands fa-microsoft'},{key:'Perplexity',label:'Perplexity',icon:'fa-solid fa-magnifying-glass'},
]
const selApps = ref(['all'])
function toggleApp(k) {
  if (k==='all') { selApps.value=['all']; return }
  selApps.value = selApps.value.filter(f=>f!=='all')
  const i = selApps.value.indexOf(k)
  if (i>=0) selApps.value.splice(i,1); else selApps.value.push(k)
  if (!selApps.value.length) selApps.value=['all']
}
</script>

<style scoped>
.dashboard-root { width:1920px; height:1080px; background:var(--bg-deep); display:flex; font-family:var(--font-ui); color:var(--text-primary); overflow:hidden; }
.dashboard-bg { position:absolute; inset:0; pointer-events:none; z-index:0; }
.bg-grid { position:absolute; inset:0; background:linear-gradient(rgba(56,189,248,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(56,189,248,.03) 1px,transparent 1px); background-size:60px 60px; animation:gS 20s linear infinite; }
@keyframes gS { 0%{background-position:0 0} 100%{background-position:60px 60px} }
.bg-orb { position:absolute; width:600px; height:600px; border-radius:50%; background:radial-gradient(circle,rgba(56,189,248,.06) 0%,transparent 70%); top:-200px; right:-200px; animation:oF 12s ease-in-out infinite; }
@keyframes oF { 0%,100%{transform:translate(0,0) scale(1)} 33%{transform:translate(-80px,60px) scale(1.1)} 66%{transform:translate(40px,-30px) scale(.95)} }

.sidebar { width:280px; min-width:280px; background:linear-gradient(180deg,#0d1321 0%,#111827 50%,#0a0e17 100%); border-right:1px solid var(--border-subtle); display:flex; flex-direction:column; z-index:10; backdrop-filter:blur(20px); }
.sidebar-header { padding:24px 20px 16px; border-bottom:1px solid var(--border-subtle); }
.logo-box { display:flex; align-items:center; gap:12px; }
.logo-icon { width:40px; height:40px; border-radius:14px; background:var(--gradient-hero); display:flex; align-items:center; justify-content:center; font-size:18px; color:#fff; box-shadow:var(--shadow-glow-cyan); animation:lG 3s ease-in-out infinite; }
@keyframes lG { 0%,100%{box-shadow:0 0 20px rgba(56,189,248,.2)} 50%{box-shadow:0 0 40px rgba(167,139,250,.35)} }
.logo-text h2 { font-size:15px; font-weight:700; background:var(--gradient-hero); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
.logo-text span { font-size:10px; color:var(--text-muted); text-transform:uppercase; letter-spacing:.5px; }
.sidebar-section { padding:16px 20px; border-bottom:1px solid var(--border-subtle); }
.upload-zone { border:2px dashed var(--border-active); border-radius:14px; padding:14px; text-align:center; cursor:pointer; background:rgba(56,189,248,.03); transition:all var(--transition-fast); }
.upload-zone:hover { border-color:var(--accent-purple); box-shadow:var(--shadow-glow-purple); transform:translateY(-1px); }
.upload-zone i { font-size:24px; color:var(--accent-cyan); margin-bottom:6px; display:block; transition:transform var(--transition-spring); }
.upload-zone:hover i { transform:scale(1.15); }
.upload-zone p { font-size:13px; color:var(--text-secondary); }
.upload-zone small { font-size:11px; color:var(--text-muted); }
.file-loaded { display:flex; align-items:center; gap:8px; margin-top:10px; padding:8px 12px; background:rgba(52,211,153,.08); border-radius:8px; font-size:12px; color:var(--accent-emerald); }
.toggles { display:flex; flex-direction:column; gap:10px; }
.t-row { display:flex; align-items:center; justify-content:space-between; font-size:13px; color:var(--text-secondary); }
.t-sw { position:relative; width:44px; height:24px; }
.t-sw input { opacity:0; width:0; height:0; }
.t-knob { position:absolute; inset:0; background:var(--bg-card); border-radius:24px; cursor:pointer; transition:var(--transition-fast); border:1px solid var(--border-subtle); }
.t-knob::before { content:''; position:absolute; width:18px; height:18px; left:2px; bottom:2px; background:var(--text-muted); border-radius:50%; transition:var(--transition-fast); }
.t-sw input:checked+.t-knob { background:linear-gradient(135deg,var(--accent-cyan),var(--accent-purple)); border-color:transparent; }
.t-sw input:checked+.t-knob::before { transform:translateX(20px); background:#fff; }
.sidebar-nav { flex:1; padding:12px; overflow-y:auto; }
.nav-label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-muted); padding:8px 10px 4px; }
.nav-item { display:flex; align-items:center; gap:10px; padding:10px 12px; border-radius:12px; cursor:pointer; font-size:13px; font-weight:500; color:var(--text-secondary); transition:all var(--transition-fast); margin-bottom:2px; }
.nav-item i { width:18px; text-align:center; font-size:14px; transition:transform var(--transition-spring); }
.nav-item:hover { background:var(--bg-card); color:var(--text-primary); }
.nav-item:hover i { transform:translateX(2px); }
.nav-item.active { background:var(--gradient-card); color:var(--accent-cyan); box-shadow:inset 0 0 0 1px var(--border-active); }
.nav-badge { margin-left:auto; font-size:10px; padding:2px 8px; border-radius:12px; background:rgba(248,113,113,.15); color:var(--accent-red); font-weight:600; }
.sidebar-footer { padding:14px 20px; border-top:1px solid var(--border-subtle); display:flex; align-items:center; gap:8px; }
.s-dot { width:8px; height:8px; border-radius:50%; background:var(--accent-emerald); box-shadow:0 0 8px var(--accent-emerald); animation:dP 2s ease-in-out infinite; }
@keyframes dP { 0%,100%{opacity:1} 50%{opacity:.4} }
.s-text { font-size:12px; color:var(--text-muted); }
.s-text strong { color:var(--accent-emerald); }

.main-area { flex:1; display:grid; grid-template-rows:auto auto 1fr; z-index:1; min-width:0; min-height:0; overflow:hidden; }
.topbar { display:flex; align-items:center; justify-content:space-between; padding:28px 32px 0; }
.topbar-left h1 { font-size:26px; font-weight:800; letter-spacing:-.6px; background:linear-gradient(135deg,#e2e8f0 0%,#a78bfa 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
.topbar-left p { font-size:13px; color:var(--text-muted); margin-top:4px; }
.topbar-right { display:flex; gap:12px; align-items:center; }
.search-box { position:relative; display:inline-flex; align-items:center; }
.search-box i { position:absolute; left:12px; color:var(--text-muted); font-size:14px; }
.search-box input { background:var(--bg-card); border:1px solid var(--border-subtle); border-radius:12px; padding:9px 16px 9px 36px; font-size:13px; color:var(--text-primary); font-family:var(--font-ui); width:240px; transition:all var(--transition-fast); }
.search-box input:focus { outline:none; border-color:var(--border-active); box-shadow:var(--shadow-glow-cyan); }
.btn-ghost { padding:9px 18px; border-radius:12px; font-size:13px; font-weight:600; background:transparent; color:var(--text-secondary); border:1px solid var(--border-subtle); cursor:pointer; font-family:var(--font-ui); display:flex; align-items:center; gap:6px; transition:all var(--transition-fast); }
.btn-ghost:hover { background:var(--bg-card); border-color:var(--border-active); }
.btn-primary { padding:9px 18px; border-radius:12px; font-size:13px; font-weight:600; background:var(--gradient-hero); color:#fff; border:none; cursor:pointer; font-family:var(--font-ui); display:flex; align-items:center; gap:6px; box-shadow:var(--shadow-glow-cyan); transition:all var(--transition-fast); }
.btn-primary:hover { transform:translateY(-2px); box-shadow:0 0 30px rgba(56,189,248,.3); }
.filter-bar { display:flex; gap:10px; align-items:center; flex-wrap:wrap; padding:20px 32px 0; }
.f-label { font-size:12px; color:var(--text-muted); font-weight:600; display:flex; align-items:center; gap:5px; }
.f-chip { padding:7px 16px; border-radius:20px; font-size:12px; font-weight:600; cursor:pointer; background:var(--bg-card); color:var(--text-secondary); border:1px solid var(--border-subtle); display:flex; align-items:center; gap:5px; transition:all var(--transition-fast); user-select:none; }
.f-chip:hover { background:var(--bg-card-hover); border-color:var(--border-active); }
.f-chip.active { background:var(--gradient-card); color:var(--accent-cyan); border-color:var(--border-active); box-shadow:var(--shadow-glow-cyan); }
.f-sep { width:1px; background:var(--border-subtle); align-self:stretch; margin:0 4px; }
.page-container { height:100%; overflow-y:auto; overflow-x:hidden; padding:24px 32px 40px; }
.c-cyan { color:var(--accent-cyan); margin-right:6px; }
.c-purple { color:var(--accent-purple); margin-right:6px; }
.c-emerald { color:var(--accent-emerald); }
</style>
