# GenAI Review ECharts Dashboard

Vue 3 + ECharts 5 大数据可视化大屏，基于 1920x1080 基准分辨率 scale 自适应。

## Start

```bash
npm install
npm run dev
```

Open `http://localhost:5173`.

## Stack

| Layer | Choice |
|-------|--------|
| Framework | Vue 3.4 (Composition API + SFC) |
| Charts | ECharts 5.5 |
| Build | Vite 5 |
| Screen Adapt | CSS transform:scale (1920x1080) |
| Theme | Dark glassmorphism + CSS custom properties |
| Icons | Font Awesome 6.5 CDN |
| Fonts | Inter + JetBrains Mono (Google Fonts) |

## Structure

```
src/
  main.js              # Vue entry
  App.vue              # Layout + sidebar + nav + page routing
  styles/global.css    # Design tokens & global styles
  utils/screenAdapter.js # Scale-based screen fit
  data/mockData.js     # Centralized mock data (matches project schema)
  views/
    OverviewPage.vue      # KPI cards + overview charts + product table
    ProjectPage.vue       # Positioning + questions + field schema
    ComparePage.vue       # Rating distribution + scatter + table
    SentimentPage.vue     # Sentiment stack + scores + cross table
    PainPointsPage.vue    # Theme groups + low-rating themes + detail table
    TrendPage.vue         # 3x line-area charts (count/rating/negative rate)
    KeywordsPage.vue      # Keyword bar chart + TF-IDF + review cards
    DesignPage.vue        # Requirements + architecture diagram + boundaries
```

## Charts (14 total)

| Page | Charts |
|------|--------|
| Overview | Horizontal bar (review count), Vertical bar (avg rating) |
| Compare | Grouped bar (rating dist 5x5), Scatter (good vs bad rate) |
| Sentiment | Stacked bar (sentiment %), Bar (polarity scores) |
| PainPoints | Grouped bar (theme x app), Bar (low-rating theme %) |
| Trend | 3x Line+area (count, rating, negative rate monthly) |
| Keywords | Horizontal bar (word freq), Grouped bar (TF-IDF) |

## Adaptation

- Baseline: 1920x1080
- `initScreenAdapter(rootEl)` computes `scale = min(w/1920, h/1080)`
- Applies `transform: translate(-50%, -50%) scale(X)` on root
- Recalculates on window resize
