export const APP_COLORS = {
  "ChatGPT": "#38bdf8",
  "Claude": "#a78bfa",
  "Perplexity": "#f472b6",
  "Microsoft_Copilot": "#c084fc",
  "Google_Gemini": "#f97316"
}

export const APPS = Object.keys(APP_COLORS)

export const COLOR_ARR = Object.values(APP_COLORS)


export const kpi = {
  "totalReviews": 99988,
  "appCount": 5,
  "avgRating": 4.12,
  "negativeRate": 17.6
}

export const profiles = [
  {
    "App": "ChatGPT",
    "count": 10000,
    "rating": 3.81,
    "good": 69.2,
    "bad": 24.8,
    "sentiment": 0.37,
    "thumbs": 0.52
  },
  {
    "App": "Claude",
    "count": 10000,
    "rating": 3.78,
    "good": 67.3,
    "bad": 25.5,
    "sentiment": 0.37,
    "thumbs": 1.59
  },
  {
    "App": "Perplexity",
    "count": 10000,
    "rating": 3.46,
    "good": 59.7,
    "bad": 35.7,
    "sentiment": 0.31,
    "thumbs": 2.87
  },
  {
    "App": "Microsoft_Copilot",
    "count": 10000,
    "rating": 4.23,
    "good": 80.4,
    "bad": 14.1,
    "sentiment": 0.49,
    "thumbs": 3.36
  },
  {
    "App": "Google_Gemini",
    "count": 10000,
    "rating": 3.5,
    "good": 60.4,
    "bad": 32.6,
    "sentiment": 0.29,
    "thumbs": 1.65
  }
]

export const rateDist = [
  [
    2085,
    1980,
    3137,
    1127,
    2739
  ],
  [
    397,
    570,
    436,
    280,
    524
  ],
  [
    599,
    724,
    454,
    556,
    697
  ],
  [
    1210,
    1114,
    683,
    1235,
    1039
  ],
  [
    5709,
    5612,
    5290,
    6802,
    5001
  ]
]

export const sentiment = {
  "pos": [
    69.5,
    70.9,
    66.1,
    78.2,
    61.8
  ],
  "neu": [
    11.6,
    8.7,
    11.1,
    9.0,
    15.5
  ],
  "neg": [
    18.9,
    20.4,
    22.7,
    12.8,
    22.7
  ]
}

export const sentimentAvg = [
  0.37,
  0.37,
  0.31,
  0.49,
  0.29
]

export const ratingCross = [
  {
    "g": "好评 (4-5星)",
    "p": 93.7,
    "n": 3.9,
    "x": 2.4
  },
  {
    "g": "中评 (3星)",
    "p": 34.2,
    "n": 49.0,
    "x": 16.7
  },
  {
    "g": "差评 (1-2星)",
    "p": 23.2,
    "n": 12.4,
    "x": 64.4
  }
]

export const themes = [
  {
    "t": "Accuracy/Logic Issues",
    "v": [
      5.4,
      4.3,
      6.4,
      4.5,
      4.9
    ]
  },
  {
    "t": "Pricing/Subscription",
    "v": [
      5.8,
      8.2,
      7.7,
      2.2,
      3.4
    ]
  },
  {
    "t": "Bugs/Performance",
    "v": [
      2.1,
      5.7,
      1.9,
      2.9,
      5.3
    ]
  },
  {
    "t": "Learning/Work Value",
    "v": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ]
  },
  {
    "t": "Feature Experience",
    "v": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ]
  },
  {
    "t": "Login/Account",
    "v": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ]
  },
  {
    "t": "Usage Limits",
    "v": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ]
  }
]

export const lowTheme = [
  {
    "t": "General",
    "v": 67.3
  },
  {
    "t": "Accuracy/Logic",
    "v": 10.5
  },
  {
    "t": "Pricing/Sub",
    "v": 10.3
  },
  {
    "t": "Bugs/Performance",
    "v": 8.4
  },
  {
    "t": "Feature Experience",
    "v": 1.3
  },
  {
    "t": "Login/Account",
    "v": 0.9
  },
  {
    "t": "Learning/Work Value",
    "v": 0.7
  }
]

export const months = [
  "2025-09",
  "2025-10",
  "2025-11",
  "2025-12",
  "2026-01",
  "2026-02",
  "2026-03",
  "2026-04",
  "2026-05",
  "2026-06"
]

export const trendCounts = [
  4671,
  8416,
  5679,
  3936,
  4378,
  6000,
  25699,
  818,
  2165,
  1112
]

export const trendRatings = [
  4.31,
  3.71,
  4.2,
  3.98,
  3.97,
  3.95,
  3.72,
  4.41,
  4.5,
  4.51
]

export const trendBad = [
  12.5,
  28.6,
  15.8,
  20.6,
  21.2,
  22.0,
  27.2,
  10.8,
  8.1,
  8.5
]

export const keywords = [
  {
    "w": "it's",
    "c": 2895
  },
  {
    "w": "time",
    "c": 1944
  },
  {
    "w": "don't",
    "c": 1784
  },
  {
    "w": "can't",
    "c": 1677
  },
  {
    "w": "all",
    "c": 1556
  },
  {
    "w": "gemini",
    "c": 1532
  },
  {
    "w": "now",
    "c": 1441
  },
  {
    "w": "wrong",
    "c": 1231
  },
  {
    "w": "pro",
    "c": 1219
  },
  {
    "w": "doesn't",
    "c": 1174
  },
  {
    "w": "answer",
    "c": 1165
  },
  {
    "w": "better",
    "c": 1158
  },
  {
    "w": "give",
    "c": 1098
  },
  {
    "w": "because",
    "c": 1095
  },
  {
    "w": "only",
    "c": 1088
  },
  {
    "w": "google",
    "c": 1073
  },
  {
    "w": "free",
    "c": 1068
  },
  {
    "w": "want",
    "c": 1052
  },
  {
    "w": "hai",
    "c": 1041
  },
  {
    "w": "gpt",
    "c": 1033
  }
]

export const tfidf = [
  {
    "k": "it's",
    "v": [
      156.0,
      169.7,
      119.9,
      204.7,
      145.8
    ]
  },
  {
    "k": "love",
    "v": [
      82.6,
      73.4,
      54.6,
      116.4,
      63.0
    ]
  },
  {
    "k": "all",
    "v": [
      82.1,
      89.8,
      89.4,
      88.5,
      80.5
    ]
  },
  {
    "k": "helpful",
    "v": [
      74.8,
      39.4,
      29.6,
      59.9,
      50.4
    ]
  },
  {
    "k": "time",
    "v": [
      70.3,
      77.6,
      81.3,
      66.1,
      74.9
    ]
  }
]

export const reviews = [
  {
    "a": "Google_Gemini",
    "r": 3,
    "s": "负面",
    "t": "General",
    "th": 5447,
    "d": "2026-03-01",
    "tx": "There is way too much lag! it's not exactly seamless if it lags for a solid 30 seconds every time I come back to the app. Also when I try to use the mic within the app, it clears the entire conversation. the \"compatibili"
  },
  {
    "a": "Perplexity",
    "r": 1,
    "s": "负面",
    "t": "Bugs/Performance",
    "th": 3567,
    "d": "2026-01-11",
    "tx": "No voice activation, and the app doesn't preserve any voice settings (like custom speed or accent) between sessions. It also doesn't matter how many times you tell it to speak more slowly, it gradually speeds up again. T"
  },
  {
    "a": "Microsoft_Copilot",
    "r": 4,
    "s": "正面",
    "t": "General",
    "th": 2672,
    "d": "2025-08-30",
    "tx": "it's a good app for anything that isn't image generation. I get the disclaimer that it might make mistakes. but for an AI generated by one of the biggest companies in the world those mistakes shouldn't be as frequent if "
  },
  {
    "a": "Claude",
    "r": 4,
    "s": "正面",
    "t": "General",
    "th": 1532,
    "d": "2025-08-27",
    "tx": "This app is very convenient and smooth, with tolerable time limits, 3 or 4 hours. There's only this problem that sometimes even after the time limit (Like when the app says you can't send messages until 8am) I am still u"
  },
  {
    "a": "ChatGPT",
    "r": 5,
    "s": "正面",
    "t": "General",
    "th": 835,
    "d": "2026-03-30",
    "tx": "I like this app cause can be adaptation and more like friend. but why I always got ’n ?"
  },
  {
    "a": NaN,
    "r": 4,
    "s": "正面",
    "t": "Accuracy/Logic Issues",
    "th": 744,
    "d": "2023-12-07",
    "tx": "Love ChatGPT; love having an app instead of relying on a browser. However, there are two basic functions that are missing from the app which are sometimes essential: the ability change your input without starting a new c"
  },
  {
    "a": "Google_Gemini",
    "r": 4,
    "s": "正面",
    "t": "Bugs/Performance",
    "th": 724,
    "d": "2026-03-18",
    "tx": "Please stop the Personal Context glitches. The feature forces it to interconnect topics in chats that are not meant to be related. Even someone on Reddit complained that the feature caused Gemini to bring up an irrelevan"
  },
  {
    "a": "Google_Gemini",
    "r": 1,
    "s": "负面",
    "t": "General",
    "th": 718,
    "d": "2026-03-02",
    "tx": "The gemini app used to be amazing. Recently, my chars have not been loading leading to frustration, and sone chats even disappeared and I have lost lots of history of important stuff. In addition there is no swipe from t"
  }
]

export const fields = [
  [
    "App",
    "应用名称",
    "区分 ChatGPT、Claude、Gemini、Copilot、Perplexity 等产品"
  ],
  [
    "Review_Date",
    "评论时间",
    "用于月度/日度趋势分析"
  ],
  [
    "Star_Rating",
    "用户评分",
    "计算平均评分、好评率、差评率"
  ],
  [
    "Review_Text",
    "评论正文",
    "用于情感分析、关键词提取、痛点主题识别"
  ],
  [
    "Word_Count",
    "评论词数",
    "衡量评论长度"
  ],
  [
    "Review_Length_Chars",
    "评论字符数",
    "辅助选择典型评论"
  ],
  [
    "Thumbs_Up_Count",
    "评论点赞数",
    "衡量评论代表性"
  ],
  [
    "App_Version",
    "应用版本",
    "版本维度分析"
  ],
  [
    "Sentiment_Polarity",
    "情感极性分数",
    "判断文本正负倾向"
  ],
  [
    "Sentiment_Label",
    "情感标签",
    "正面/中性/负面"
  ],
  [
    "Review_Theme",
    "评论主题/痛点",
    "分析用户关注点和产品问题"
  ],
  [
    "Source",
    "数据来源",
    "标记来自哪个 CSV/数据集"
  ]
]
