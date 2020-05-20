def flex(kanji,meanings,jlpt,kun_reading,on_reading):

  meaning_sub = "-"
  kun_sub = "-"
  on_sub = "-"
  for i in range (3):
      if i == 0 :
        try:
          meaning_sub = meanings[i]
        except Exception:
          pass
      else:
        try:
          meaning_sub = meaning_sub + ", " +meanings[i]
        except Exception:
          pass
      if i == 0 :
        try:
          kun_sub = kun_reading[i]
        except Exception:
          pass
      else:
        try:
          kun_sub = kun_sub + ", " +kun_reading[i]
        except Exception:
          pass
      if i == 0 :
        try:
          on_sub = on_reading[i]
        except Exception:
          pass
      else:
        try:
          on_sub = on_sub + ", " +on_reading[i]
        except Exception:
          pass
  return {
  "type": "flex",
  "altText": kanji,
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "spacer",
              "size": "xs"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "horizontal",
          "spacing": "md",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 1,
              "contents": [
                {
                  "type": "spacer",
                  "size": "sm"
                },
                {
                  "type": "text",
                  "text": kanji,
                  "margin": "xxl",
                  "size": "5xl",
                  "align": "center",
                  "color": "#000000",
                  "wrap": True
                },
                {
                  "type": "spacer",
                  "size": "md"
                }
              ]
            }
          ]
        },
        "styles": {
          "header": {
            "backgroundColor": "#FFFFFF"
          }
        }
      },
      {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": kanji,
              "size": "3xl",
              "align": "start"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "Meanings :",
              "margin": "md",
              "wrap": True
            },
            {
              "type": "text",
              "text": meaning_sub,
              "margin": "sm",
              "size": "sm",
              "align": "start"
            },
            {
              "type": "text",
              "text": "Kun-Readings :",
              "margin": "md",
              "wrap": False
            },
            {
              "type": "text",
              "text": kun_sub,
              "margin": "sm",
              "size": "sm"
            },
            {
              "type": "text",
              "text": "On-readings :",
              "margin": "md",
              "wrap": True
            },
            {
              "type": "text",
              "text": on_sub,
              "margin": "sm",
              "size": "sm"
            },
            {
              "type": "text",
              "text": "JLPT Level : N"+str(jlpt),
              "margin": "md",
              "wrap": True
            }
          ]
        }
      }
    ]
  }
}