export const APP_COLORS = {
  'ChatGPT':'#38bdf8','Claude':'#a78bfa','Gemini':'#fbbf24','Copilot':'#34d399','Perplexity':'#f472b6',
}
export const APPS = Object.keys(APP_COLORS)
export const COLOR_ARR = Object.values(APP_COLORS)

export const kpi = { totalReviews:99988, appCount:5, avgRating:3.95, negativeRate:17.6 }

export const profiles = [
  { App:'ChatGPT', count:10000, rating:3.81, good:67.7, bad:24.8, sentiment:0.15, thumbs:10.5 },
  { App:'Claude', count:10000, rating:4.11, good:77.2, bad:12.3, sentiment:0.44, thumbs:19.2 },
  { App:'Gemini', count:10000, rating:3.74, good:65.0, bad:23.2, sentiment:0.20, thumbs:8.5 },
  { App:'Copilot', count:10000, rating:3.96, good:72.9, bad:16.6, sentiment:0.33, thumbs:11.8 },
  { App:'Perplexity', count:10000, rating:4.15, good:79.2, bad:11.3, sentiment:0.49, thumbs:21.4 },
]

// [ChatGPT, Claude, Gemini, Copilot, Perplexity] per rating level 1-star .. 5-star
export const rateDist = [
  [1000, 450, 980, 660, 430],
  [1482, 780, 1340, 1000, 700],
  [750, 1050, 1180, 1050, 950],
  [1900, 2650, 2350, 2650, 2750],
  [4868, 5070, 4150, 4640, 5170],
]

export const sentiment = {
  pos:[47,68,50,60,72], neu:[28,20,27,23,18], neg:[25,12,23,17,10],
}

export const sentimentAvg = [0.15,0.44,0.20,0.33,0.49]

export const ratingCross = [
  { g:'好评 (4-5星)', p:93.7, n:3.9, x:2.4 },
  { g:'中评 (3星)', p:34.2, n:49.0, x:16.7 },
  { g:'差评 (1-2星)', p:23.2, n:12.4, x:64.4 },
]

export const themes = [
  { t:'General', v:[28.4,22.6,30.1,26.8,24.5] },
  { t:'Accuracy/Logic Issues', v:[21.2,11.8,18.7,20.5,19.4] },
  { t:'Bugs/Performance', v:[10.8,16.4,14.2,13.1,8.8] },
  { t:'Pricing/Subscription', v:[18.1,20.5,10.6,12.2,17.8] },
  { t:'Usage Limits', v:[7.2,10.8,8.5,6.4,9.2] },
  { t:'Login/Account', v:[8.5,6.2,15.1,13.8,10.5] },
  { t:'Feature Experience', v:[5.8,11.7,8.5,11.2,13.6] },
  { t:'Learning/Work Value', v:[8.8,12.0,7.8,8.2,11.2] },
]

export const lowTheme = [
  { t:'General', v:67.3 },
  { t:'Accuracy/Logic Issues', v:10.5 },
  { t:'Pricing/Subscription', v:10.3 },
  { t:'Bugs/Performance', v:8.4 },
  { t:'Feature Experience', v:1.3 },
  { t:'Login/Account', v:0.9 },
  { t:'Learning/Work Value', v:0.7 },
  { t:'Usage Limits', v:0.5 },
]

export const months = ['2025-09','2025-10','2025-11','2025-12','2026-01','2026-02','2026-03','2026-04','2026-05','2026-06']
export const trendCounts = [7500,8000,8500,9000,9500,10200,10000,10800,11200,10500]
export const trendRatings = [3.72,3.70,3.68,3.74,3.76,3.78,3.81,3.83,3.82,3.84]
export const trendBad = [26.5,26.8,27.2,25.8,25.0,24.5,24.8,23.5,23.0,22.5]

export const keywords = [
  {w:'app',c:6311},{w:'ai',c:3214},{w:'like',c:2237},
  {w:'use',c:2153},{w:'just',c:2075},{w:'time',c:1943},
  {w:"don't",c:1847},{w:'good',c:1804},{w:'chat',c:1766},
  {w:'chatgpt',c:1657},{w:'gemini',c:1548},{w:'bad',c:1284},
  {w:'wrong',c:1234},{w:"doesn't",c:1220},{w:'pro',c:1220},
]

export const tfidf = [
  {k:'app', v:[0.88,0.72,0.91,0.85,0.78]},
  {k:'good', v:[0.76,0.65,0.72,0.70,0.68]},
  {k:'best', v:[0.82,0.58,0.48,0.52,0.45]},
  {k:'like', v:[0.68,0.52,0.64,0.60,0.62]},
  {k:'ai', v:[0.42,0.86,0.75,0.78,0.73]},
]

export const reviews = [
  {a:'ChatGPT',r:1,s:'负面',t:'Accuracy/Logic Issues',th:184,d:'2026-03-31',tx:'consistently gives false information and will argue it is true even when verified to be false'},
  {a:'Claude',r:5,s:'正面',t:'Learning/Work Value',th:35,d:'2026-03-20',tx:'excellent writing assistant and the long text conversation is very smooth'},
  {a:'Gemini',r:2,s:'负面',t:'Bugs/Performance',th:11,d:'2026-03-19',tx:'login verification keeps failing and the app gets stuck at the loading screen'},
  {a:'Perplexity',r:5,s:'正面',t:'Learning/Work Value',th:27,d:'2026-03-25',tx:'great for search and citations, answers are clear and well-sourced'},
  {a:'Copilot',r:2,s:'负面',t:'Pricing/Subscription',th:42,d:'2026-03-16',tx:'the subscription pricing is confusing and the free tier keeps pushing upgrade prompts'},
  {a:'ChatGPT',r:3,s:'中性',t:'Bugs/Performance',th:0,d:'2026-03-31',tx:'the free version is slow performance and paid is good performance'},
]

export const fields = [
  ['App','应用名称','区分 ChatGPT、Claude、Gemini、Copilot、Perplexity 等产品'],
  ['Review_Date','评论时间','用于月度/日度趋势分析'],
  ['Star_Rating','用户评分','计算平均评分、好评率、差评率'],
  ['Review_Text','评论正文','用于情感分析、关键词提取、痛点主题识别'],
  ['Word_Count','评论词数','衡量评论长度'],
  ['Review_Length_Chars','评论字符数','辅助选择典型评论'],
  ['Thumbs_Up_Count','评论点赞数','衡量评论代表性'],
  ['App_Version','应用版本','版本维度分析'],
  ['Sentiment_Polarity','情感极性分数','判断文本正负倾向'],
  ['Sentiment_Label','情感标签','正面/中性/负面'],
  ['Review_Theme','评论主题/痛点','分析用户关注点和产品问题'],
  ['Source','数据来源','标记来自哪个 CSV/数据集'],
]
