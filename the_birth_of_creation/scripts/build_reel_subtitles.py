#!/usr/bin/env python3
"""
Generate Instagram Reel (1080x1920, 9:16) theatrical ASS subtitles & Cinzel titles
respecting Instagram Reels UI safe zones (top 14% and bottom 20% clear).
"""

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TIMINGS_PATH = os.path.join(ROOT, "assets", "audio", "vo_timings.json")
OUT_ASS = os.path.join(ROOT, "subtitles_reel_hi.ass")

# Tight, punchy 2-3 line vertical Reel subtitles (max ~24-28 chars per line so they never hit side icons!)
REEL_SUBS = {
    1: [
        (0.00, 0.56, "जब न समय था… न आकाश।\nन धरती थी, न जीवन।\nन कोई दिशा… न कोई सीमा।"),
        (0.56, 1.00, "तब क्या था?\nक्या सच में कुछ भी नहीं था?"),
    ],
    2: [
        (0.00, 0.50, "हिंदू पौराणिक परंपरा में,\nउस अनंत जलराशि के बीच था क्षीर सागर…"),
        (0.50, 1.00, "जहाँ अनंत शेषनाग पर\nयोग-निद्रा में विराजमान थे भगवान विष्णु।"),
    ],
    3: [
        (0.00, 0.42, "वो थे नारायण…\nअनंत, शांत और समय से परे।"),
        (0.42, 1.00, "उनकी योग-निद्रा में छुपी थी\nएक ऐसी संभावना… जो पूरी सृष्टि का आधार बनी।"),
    ],
    4: [
        (0.00, 0.55, "फिर एक दिव्य कमल प्रकट हुआ…\nनारायण की नाभि से निकलता हुआ,\nअनंत जल के ऊपर उठता हुआ।"),
        (0.55, 1.00, "जैसे शून्यता के बीच जन्म ले रही हो…\nएक नई संभावना।"),
    ],
    5: [
        (0.00, 0.52, "और उस कमल पर प्रकट हुए ब्रह्मा…\nचार मुखों वाले सृष्टि के रचयिता।"),
        (0.52, 1.00, "उनके सामने था एक अनंत प्रश्न…\nऔर एक अनंत ज़िम्मेदारी।"),
    ],
    6: [
        (0.00, 0.55, "लेकिन ब्रह्मा के मन में सवाल उठा…\nमैं कौन हूँ? मुझे किसने जन्म दिया?"),
        (0.55, 1.00, "मेरी उत्पत्ति का रहस्य क्या है?\nउन्होंने उत्तर खोजना शुरू किया।"),
    ],
    7: [
        (0.00, 0.62, "पौराणिक वर्णन के अनुसार,\nब्रह्मा ने सृष्टि की रचना आरंभ की…\nलोकों, प्रकृति और जीवन का विस्तार हुआ।"),
        (0.62, 1.00, "अंधकार में अब रोशनी थी।"),
    ],
    8: [
        (0.00, 0.54, "उनसे प्रकट हुई ऋषियों\nऔर प्रजापतियों की परंपरा…\nसृष्टि की कहानी आगे बढ़ने लगी।"),
        (0.54, 1.00, "ज्ञान, जीवन और चेतना के\nअनेक रूप सामने आए।"),
    ],
    9: [
        (0.00, 0.48, "और यही है सृष्टि, स्थिति\nऔर प्रलय का अनंत चक्र…"),
        (0.48, 1.00, "क्योंकि हिंदू दर्शन में क्रिएशन\nसिर्फ़ एक शुरुआत नहीं… एक अनंत यात्रा है।"),
    ],
}


def fmt_ass(sec):
    cs = int(round(sec * 100))
    h = cs // 360000
    m = (cs % 360000) // 6000
    s = (cs % 6000) // 100
    rem = cs % 100
    return f"{h}:{m:02d}:{s:02d}.{rem:02d}"


def build():
    with open(TIMINGS_PATH, "r", encoding="utf-8") as f:
        timings = json.load(f)

    events = [
        # Cinematic opening title card (vertical stacked for dramatic 9:16 Reel impact)
        r"Dialogue: 1,0:00:00.70,0:00:05.70,TitleTop,,0,0,0,,{\pos(540,775)\fad(850,1100)}THE BIRTH OF",
        r"Dialogue: 1,0:00:00.90,0:00:05.70,TitleMain,,0,0,0,,{\pos(540,870)\fad(900,1100)}CREATION",
        r"Dialogue: 1,0:00:01.60,0:00:05.70,TitleSub,,0,0,0,,{\pos(540,965)\fad(900,1100)}BEFORE TIME  ·  BEFORE SPACE  ·  BEFORE LIFE",
        # Cinematic closing title card during golden fade to black
        r"Dialogue: 1,0:01:26.40,0:01:29.60,EndTop,,0,0,0,,{\pos(540,835)\fad(750,900)}THE BIRTH OF",
        r"Dialogue: 1,0:01:26.55,0:01:29.60,EndMain,,0,0,0,,{\pos(540,920)\fad(750,900)}CREATION",
        r"Dialogue: 1,0:01:26.95,0:01:29.60,EndSub,,0,0,0,,{\pos(540,1005)\fad(700,900)}BEFORE TIME  ·  BEFORE SPACE  ·  BEFORE LIFE",
    ]

    for item in timings:
        sid = item["scene"]
        t0 = item["vo_start"]
        t1 = item["vo_end"]
        dur = t1 - t0
        for f0, f1, txt in REEL_SUBS[sid]:
            cs = t0 + dur * f0
            ce = min(89.65, t0 + dur * f1)
            ass_txt = txt.replace("\n", "\\N")
            events.append(f"Dialogue: 0,{fmt_ass(cs)},{fmt_ass(ce)},ReelHindi,,0,0,0,,{{\\fad(180,180)}}{ass_txt}")

    header = """[Script Info]
Title: THE BIRTH OF CREATION - INSTAGRAM REEL (9:16)
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ReelHindi,Noto Sans Devanagari,46,&H00F2F7FF,&H000000FF,&H00120906,&HA805040E,-1,0,0,0,100,100,0,0,1,3.2,2.8,2,88,128,315,1
Style: TitleTop,Cinzel,52,&H00C8ECFF,&H000000FF,&H00120905,&H88000000,-1,0,0,0,100,100,11,0,1,2.0,3.2,5,40,40,40,1
Style: TitleMain,Cinzel,108,&H00A8E0FF,&H000000FF,&H00120905,&H90000000,-1,0,0,0,100,100,12,0,1,2.8,4.2,5,40,40,40,1
Style: TitleSub,Cinzel,24,&H00E4F1FF,&H000000FF,&H000D0805,&H88000000,0,0,0,0,100,100,3.5,0,1,1.6,2.2,5,40,40,40,1
Style: EndTop,Cinzel,46,&H00C8ECFF,&H000000FF,&H00120905,&H88000000,-1,0,0,0,100,100,10,0,1,1.8,3.0,5,40,40,40,1
Style: EndMain,Cinzel,96,&H00A8E0FF,&H000000FF,&H00120905,&H90000000,-1,0,0,0,100,100,11,0,1,2.4,3.8,5,40,40,40,1
Style: EndSub,Cinzel,22,&H00E4F1FF,&H000000FF,&H000D0805,&H88000000,0,0,0,0,100,100,3.0,0,1,1.4,2.0,5,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(OUT_ASS, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"Generated {OUT_ASS} successfully!")


if __name__ == "__main__":
    build()
