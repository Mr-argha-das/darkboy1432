#!/usr/bin/env python3
"""
THE BIRTH OF CREATION - ULTRA-CINEMATIC INSTAGRAM REEL EDITION (9:16, 1080x1920, 24 FPS, 90.00s)
Enhanced feature-film anime VFX pipeline:
  - True vertical 9:16 camera choreography (vertical cranes, dramatic tilts, heroic push-ins, cosmic pullbacks)
  - Genuine golden film halation / specular highlight bloom
  - Rotating volumetric crepuscular god-rays (light shafts)
  - Multi-layer parallax bokeh orbs + golden celestial sparks + stardust
  - Beat-synced rhythmic camera impact pulses (Scene 04 heartbeats, Scene 07 Creation Boom, Scene 09 3 Temple Bells)
  - Dramatic luminous golden optical flare transitions
  - Rich cinematic indigo/violet/burnished-gold S-curve color grading + 35mm cinema grain
  - Instagram Reels safe-zone Cinzel titles & HarfBuzz-shaped Noto Sans Devanagari subtitles
"""

import math
import os
import subprocess
import time
import numpy as np
from PIL import Image, ImageFilter
import imageio_ffmpeg

W, H = 1080, 1920
FPS = 24
DURATION = 90.0
TOTAL_FRAMES = int(FPS * DURATION)  # Exact 2,160 frames
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REEL_SCENES_DIR = os.path.join(ROOT, "assets", "reel_scenes")
AUDIO_PATH = os.path.join(ROOT, "assets", "audio", "master_audio_48khz.m4a")
ASS_PATH = os.path.join(ROOT, "subtitles_reel_hi.ass")
FONTS_DIR = "/tmp/video_tools/ttf"
OUT_MP4 = os.path.join(ROOT, "THE_BIRTH_OF_CREATION_REEL_9x16.mp4")

# Purpose-built 9:16 vertical cinematography for all 9 scenes
REEL_SPECS = [
    {
        "id": 1, "file": "reel_01_void.png", "start": 0.0, "end": 10.0,
        "z0": 1.00, "z1": 1.28, "x0": 0.50, "x1": 0.50, "y0": 0.50, "y1": 0.50,
        "glow_xy": (0.50, 0.50), "glow_color": (255, 200, 95), "glow_amp": (0.05, 0.30),
        "rays": 0.22, "p_mode": "drift_in", "p_density": 1.0, "flare_out": 0.35,
    },
    {
        "id": 2, "file": "reel_02_ksheer_sagar.png", "start": 10.0, "end": 20.0,
        "z0": 1.24, "z1": 1.04, "x0": 0.50, "x1": 0.50, "y0": 0.36, "y1": 0.56,
        "glow_xy": (0.50, 0.62), "glow_color": (255, 228, 160), "glow_amp": (0.08, 0.18),
        "rays": 0.18, "p_mode": "mist_drift", "p_density": 0.90, "flare_out": 0.20,
    },
    {
        "id": 3, "file": "reel_03_vishnu.png", "start": 20.0, "end": 31.0,
        "z0": 1.26, "z1": 1.04, "x0": 0.48, "x1": 0.51, "y0": 0.36, "y1": 0.55,
        "glow_xy": (0.42, 0.65), "glow_color": (255, 208, 110), "glow_amp": (0.08, 0.18),
        "rays": 0.24, "p_mode": "rise_gentle", "p_density": 1.0, "flare_out": 0.25,
    },
    {
        "id": 4, "file": "reel_04_lotus.png", "start": 31.0, "end": 41.0,
        # Iconic vertical crane-up: tight on Vishnu's glowing navel -> sweep all the way up to the golden lotus!
        "z0": 1.56, "z1": 1.08, "x0": 0.50, "x1": 0.50, "y0": 0.78, "y1": 0.32,
        "glow_xy": (0.50, 0.25), "glow_color": (255, 212, 95), "glow_amp": (0.12, 0.32),
        "rays": 0.36, "p_mode": "rise_fast", "p_density": 1.35, "flare_out": 0.75,
    },
    {
        "id": 5, "file": "reel_05_brahma.png", "start": 41.0, "end": 51.0,
        "z0": 1.02, "z1": 1.20, "x0": 0.50, "x1": 0.50, "y0": 0.55, "y1": 0.44,
        "glow_xy": (0.50, 0.40), "glow_color": (255, 208, 105), "glow_amp": (0.14, 0.25),
        "rays": 0.34, "p_mode": "radiate", "p_density": 1.20, "flare_out": 0.25,
    },
    {
        "id": 6, "file": "reel_06_who_am_i.png", "start": 51.0, "end": 61.0,
        # Majestic vertical descent revealing infinite dark ocean abyss below the lotus stem
        "z0": 1.24, "z1": 1.02, "x0": 0.48, "x1": 0.52, "y0": 0.35, "y1": 0.54,
        "glow_xy": (0.50, 0.53), "glow_color": (248, 198, 115), "glow_amp": (0.07, 0.16),
        "rays": 0.16, "p_mode": "swirl_slow", "p_density": 0.95, "flare_out": 0.65,
    },
    {
        "id": 7, "file": "reel_07_first_creation.png", "start": 61.0, "end": 72.0,
        # Explosive cosmic pull-back from Brahma's creation aura to full swirling galaxies
        "z0": 1.48, "z1": 1.00, "x0": 0.50, "x1": 0.50, "y0": 0.52, "y1": 0.48,
        "glow_xy": (0.50, 0.46), "glow_color": (255, 218, 118), "glow_amp": (0.14, 0.28),
        "rays": 0.38, "p_mode": "radiate_fast", "p_density": 1.45, "flare_out": 0.45,
    },
    {
        "id": 8, "file": "reel_08_seven_sages.png", "start": 72.0, "end": 82.0,
        # Graceful tilt downward from Brahma across all 7 Saptarishis
        "z0": 1.22, "z1": 1.02, "x0": 0.50, "x1": 0.50, "y0": 0.34, "y1": 0.54,
        "glow_xy": (0.50, 0.22), "glow_color": (255, 224, 138), "glow_amp": (0.10, 0.18),
        "rays": 0.28, "p_mode": "rise_gentle", "p_density": 1.05, "flare_out": 0.65,
    },
    {
        "id": 9, "file": "reel_09_cosmic_cycle.png", "start": 82.0, "end": 90.0,
        # Monumental Trimurti vertical pullback + climax golden illumination
        "z0": 1.24, "z1": 1.00, "x0": 0.50, "x1": 0.50, "y0": 0.44, "y1": 0.50,
        "glow_xy": (0.50, 0.38), "glow_color": (255, 218, 128), "glow_amp": (0.12, 0.32),
        "rays": 0.40, "p_mode": "cosmic_flow", "p_density": 1.40, "flare_out": 0.0,
    },
]

# Beat-synced audio impact timestamps (exact sync with master_audio_48khz)
IMPACTS = [
    (31.4, 0.016, 0.38),  # Heartbeat 1
    (33.4, 0.018, 0.38),  # Heartbeat 2
    (35.4, 0.015, 0.38),  # Heartbeat 3
    (41.3, 0.022, 0.65),  # Brahma Reveal Bell
    (61.5, 0.032, 0.85),  # Creation Cosmic Boom
    (82.2, 0.024, 0.65),  # Trimurti Bell 1
    (84.8, 0.024, 0.65),  # Trimurti Bell 2
    (87.1, 0.028, 0.75),  # Trimurti Bell 3
]

XFADE_DUR = 0.85


def smoothstep(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3.0 - 2.0 * u)


def load_reel_scenes():
    """Load and upscale all 9 vertical 9:16 artworks to 1440x2560 master canvas for sub-pixel cinema camera headroom."""
    imgs = {}
    MW, MH = 1440, 2560
    for sc in REEL_SPECS:
        p = os.path.join(REEL_SCENES_DIR, sc["file"])
        im = Image.open(p).convert("RGB")
        iw, ih = im.size
        scale = max(MW / iw, MH / ih)
        nw, nh = int(round(iw * scale)), int(round(ih * scale))
        im = im.resize((nw, nh), Image.Resampling.LANCZOS)
        left = (nw - MW) // 2
        top = (nh - MH) // 2
        im = im.crop((left, top, left + MW, top + MH))
        imgs[sc["id"]] = im
    return imgs


def render_camera_crop(im, z, cx, cy):
    mw, mh = im.size
    crop_w = mw / z
    crop_h = mh / z
    x0 = max(0.0, min(mw - crop_w, cx * mw - crop_w * 0.5))
    y0 = max(0.0, min(mh - crop_h, cy * mh - crop_h * 0.5))
    cropped = im.resize((W, H), resample=Image.Resampling.BILINEAR, box=(x0, y0, x0 + crop_w, y0 + crop_h))
    return np.asarray(cropped, dtype=np.float32)


def build_static_masks():
    """Precompute vertical cinema vignette, subtle top/bottom safe-zone framing gradient, and 1/4-res ray grid."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    xn = (xx / W - 0.5) * 2.0
    yn = (yy / H - 0.5) * 2.0

    # Deep dramatic vertical cinema vignette
    r2 = xn * xn * 0.85 + yn * yn * 0.65
    vignette = np.clip(1.0 - 0.34 * np.power(np.clip(r2 - 0.22, 0.0, 2.5), 1.35), 0.56, 1.0)

    # Subtle bottom-third subtitle readability band (centered around y=0.76..0.90) + soft top shadow
    y_frac = yy / H
    sub_band = 1.0 - 0.30 * np.exp(-((y_frac - 0.82) / 0.11) ** 2)
    top_grad = 1.0 - 0.20 * np.clip((0.12 - y_frac) / 0.12, 0.0, 1.0) ** 1.4
    combined_mult = (vignette * sub_band * top_grad)[:, :, None].astype(np.float32)

    # Quarter-res coordinate grid for ultra-fast volumetric god-rays & radial glow
    gh, gw = H // 4, W // 4
    gy, gx = np.mgrid[0:gh, 0:gw].astype(np.float32)
    gx /= gw
    gy /= gh
    return combined_mult, gx, gy


def make_particle_bank(n_particles=180):
    rng = np.random.default_rng(1008)
    return {
        "x0": rng.uniform(0.0, 1.0, n_particles).astype(np.float32),
        "y0": rng.uniform(0.0, 1.0, n_particles).astype(np.float32),
        "vx": rng.uniform(-0.015, 0.015, n_particles).astype(np.float32),
        "vy": rng.uniform(-0.036, -0.008, n_particles).astype(np.float32),
        # Includes large soft out-of-focus foreground bokeh orbs (rad=16, 24) for true cinema depth!
        "rad": rng.choice([2, 3, 5, 8, 16, 24], size=n_particles, p=[0.30, 0.28, 0.18, 0.12, 0.08, 0.04]),
        "phase": rng.uniform(0, 2 * np.pi, n_particles).astype(np.float32),
        "twinkle_f": rng.uniform(0.6, 2.4, n_particles).astype(np.float32),
        "alpha": rng.uniform(0.25, 0.85, n_particles).astype(np.float32),
        "warm": rng.uniform(0.0, 1.0, n_particles).astype(np.float32),
    }


def make_sprite_cache():
    sprites = {}
    for rad in [2, 3, 5, 8, 16, 24]:
        sz = rad * 4 + 1
        c = sz // 2
        yy, xx = np.mgrid[0:sz, 0:sz].astype(np.float32)
        d2 = ((xx - c) ** 2 + (yy - c) ** 2) / (rad * rad * 1.15)
        if rad >= 16:
            # Soft cinema bokeh disc with luminous ring edge
            r = np.sqrt(d2)
            spr = np.exp(-d2 * 0.85) * 0.42 + np.exp(-((r - 0.85) ** 2) * 8.0) * 0.14
        else:
            spr = np.exp(-d2 * 1.6) + 0.55 * np.exp(-d2 * 6.0)
        sprites[rad] = np.clip(spr, 0.0, 1.0).astype(np.float32)
    return sprites


def impact_pulse_at(t):
    """Return beat-synced (zoom_bump, light_flash, shake_x, shake_y) from audio impact map."""
    zb, lf, sx, sy = 0.0, 0.0, 0.0, 0.0
    for t_hit, amp, dur in IMPACTS:
        dt = t - t_hit
        if 0.0 <= dt < dur:
            env = (1.0 - math.exp(-dt / 0.025)) * math.exp(-dt / (dur * 0.38))
            zb += amp * env
            lf += amp * 750.0 * env
            sx += amp * 0.18 * math.sin(dt * 42.0) * env
            sy += amp * 0.18 * math.cos(dt * 37.0) * env
    return zb, lf, sx, sy


def apply_cinema_effects(frame, t, sc, local_u, particles, sprites, gx, gy, light_flash):
    """Apply volumetric rotating god-rays, golden halation bloom, and 3-layer parallax bokeh/sparks."""
    # 1. Volumetric radial glow + rotating crepuscular god-rays (quarter-res -> smooth upsample)
    g0, g1 = sc["glow_amp"]
    pulse = 1.0 + 0.15 * math.sin(2.0 * math.pi * 0.38 * t + sc["id"])
    g_amp = (g0 + (g1 - g0) * smoothstep(local_u)) * pulse
    cx, cy = sc["glow_xy"]
    cx += 0.015 * math.sin(t * 0.35)
    cy += 0.012 * math.cos(t * 0.28)

    dx = (gx - cx) * (W / H)
    dy = (gy - cy)
    d2 = dx * dx + dy * dy
    radial = np.exp(-d2 * 4.2) * g_amp

    # Rotating volumetric light shafts (crepuscular rays)
    ray_amp = sc["rays"]
    if ray_amp > 0:
        ang = np.arctan2(dy, dx)
        rays = (
            0.5 + 0.30 * np.sin(ang * 7.0 + t * 0.22)
            + 0.20 * np.sin(ang * 13.0 - t * 0.16)
        )
        rays = np.clip(rays, 0.0, 1.0) ** 2.2
        ray_mask = rays * np.exp(-d2 * 1.6) * (1.0 - np.exp(-d2 * 28.0)) * ray_amp * (0.75 + 0.25 * math.sin(t * 0.7))
        light_field = radial + ray_mask
    else:
        light_field = radial

    lf_img = Image.fromarray((np.clip(light_field, 0.0, 1.0) * 255).astype(np.uint8), mode="L")
    lf_full = np.asarray(lf_img.resize((W, H), Image.Resampling.BILINEAR), dtype=np.float32) / 255.0
    col = np.array(sc["glow_color"], dtype=np.float32)
    frame += lf_full[:, :, None] * col[None, None, :] * (1.0 - frame / 285.0)

    # 2. Genuine Anime Cinema Halation / Specular Highlight Bloom (makes gold & stars glow like celluloid film!)
    # Downsample bright highlights to 1/6 res -> Gaussian blur -> warm additive screen blend
    lum = frame[:, :, 0] * 0.35 + frame[:, :, 1] * 0.50 + frame[:, :, 2] * 0.15
    bright = np.clip((lum - 185.0) / 70.0, 0.0, 1.0)
    b_small = Image.fromarray((bright[::6, ::6] * 255).astype(np.uint8), mode="L").filter(ImageFilter.GaussianBlur(radius=6))
    b_full = np.asarray(b_small.resize((W, H), Image.Resampling.BILINEAR), dtype=np.float32) / 255.0
    frame[:, :, 0] += b_full * 42.0 * (1.0 - frame[:, :, 0] / 270.0)
    frame[:, :, 1] += b_full * 31.0 * (1.0 - frame[:, :, 1] / 270.0)
    frame[:, :, 2] += b_full * 16.0 * (1.0 - frame[:, :, 2] / 270.0)

    # 3. Beat-synced golden impact flash (heartbeats / creation boom / finale bells)
    if light_flash > 0.5:
        frame[:, :, 0] += light_flash * 1.00 * (1.0 - frame[:, :, 0] / 275.0)
        frame[:, :, 1] += light_flash * 0.84 * (1.0 - frame[:, :, 1] / 275.0)
        frame[:, :, 2] += light_flash * 0.45 * (1.0 - frame[:, :, 2] / 275.0)

    # 4. Multi-depth Parallax Bokeh Orbs + Golden Celestial Sparks
    mode = sc["p_mode"]
    n_use = min(len(particles["x0"]), int(125 * sc["p_density"]))
    for i in range(n_use):
        x0 = particles["x0"][i]
        y0 = particles["y0"][i]
        vx = particles["vx"][i]
        vy = particles["vy"][i]
        ph = particles["phase"][i]
        rad = int(particles["rad"][i])
        depth_mul = 1.65 if rad >= 16 else (1.2 if rad >= 8 else 1.0)

        if mode == "drift_in":
            dx_p, dy_p = x0 - 0.5, y0 - 0.5
            sc_p = 1.0 + 0.07 * ((t * depth_mul + ph) % 10.0)
            px = (0.5 + dx_p * sc_p + 0.01 * math.sin(t * 0.5 + ph)) % 1.0
            py = (0.5 + dy_p * sc_p + 0.01 * math.cos(t * 0.4 + ph)) % 1.0
        elif mode == "mist_drift":
            px = (x0 + (0.020 + abs(vx)) * t * depth_mul) % 1.0
            py = (y0 + 0.008 * math.sin(t * 0.7 + ph)) % 1.0
        elif mode == "rise_fast":
            px = (x0 + vx * t + 0.014 * math.sin(t * 1.2 + ph)) % 1.0
            py = (y0 + vy * 2.1 * t * depth_mul) % 1.0
        elif mode in ("radiate", "radiate_fast"):
            spd = (0.055 if mode == "radiate_fast" else 0.028) * depth_mul
            r = 0.06 + ((x0 + t * spd) % 0.65)
            px = 0.5 + r * math.cos(ph) * 0.92
            py = 0.46 + r * math.sin(ph) * 0.75
            if not (0.01 < px < 0.99 and 0.01 < py < 0.99):
                continue
        elif mode == "swirl_slow":
            px = (x0 + vx * 0.9 * t + 0.025 * math.sin(t * 0.45 + ph)) % 1.0
            py = (y0 + vy * 0.6 * t + 0.018 * math.cos(t * 0.35 + ph)) % 1.0
        elif mode == "cosmic_flow":
            px = (x0 + (0.028 + vx) * t * depth_mul) % 1.0
            py = (y0 + vy * 0.9 * t + 0.018 * math.sin(t * 0.6 + ph)) % 1.0
        else:
            px = (x0 + vx * t + 0.012 * math.sin(t * 0.6 + ph)) % 1.0
            py = (y0 + vy * t * depth_mul) % 1.0

        tw = 0.52 + 0.48 * math.sin(t * particles["twinkle_f"][i] + ph)
        amp = particles["alpha"][i] * tw * (120.0 if rad >= 16 else 185.0)
        if sc["id"] == 1:
            amp *= smoothstep(t / 3.2)

        spr = sprites[rad]
        sh, sw = spr.shape
        cx_i, cy_i = int(px * W), int(py * H)
        y1, y2 = cy_i - sh // 2, cy_i - sh // 2 + sh
        x1, x2 = cx_i - sw // 2, cx_i - sw // 2 + sw
        if x1 < 0 or y1 < 0 or x2 > W or y2 > H:
            continue

        w_warm = particles["warm"][i]
        patch = spr * (amp / 255.0)
        frame[y1:y2, x1:x2, 0] += patch * 255.0
        frame[y1:y2, x1:x2, 1] += patch * (246.0 - 48.0 * w_warm)
        frame[y1:y2, x1:x2, 2] += patch * (230.0 - 140.0 * w_warm)


def get_scene_frame(sc, im, t, particles, sprites, gx, gy, zb, lf, sx, sy):
    dur = sc["end"] - sc["start"]
    u = max(0.0, min(1.0, (t - sc["start"]) / dur))
    su = smoothstep(u)

    z = sc["z0"] + (sc["z1"] - sc["z0"]) * su + zb
    cx = sc["x0"] + (sc["x1"] - sc["x0"]) * su + 0.004 * math.sin(t * 0.45 + sc["id"]) + sx
    cy = sc["y0"] + (sc["y1"] - sc["y0"]) * su + 0.003 * math.cos(t * 0.35 + sc["id"] * 1.7) + sy

    frame = render_camera_crop(im, z, cx, cy)
    apply_cinema_effects(frame, t, sc, u, particles, sprites, gx, gy, lf)
    return frame


def render():
    t0_wall = time.time()
    print("=== Loading 9 Vertical 9:16 Anime Cinema Scenes ===")
    imgs = load_reel_scenes()
    vignette_mult, gx, gy = build_static_masks()
    particles = make_particle_bank(180)
    sprites = make_sprite_cache()

    rng_g = np.random.default_rng(2026)
    grain_bank = [rng_g.normal(0.0, 2.0, (H // 2, W // 2, 1)).astype(np.float32) for _ in range(24)]

    ass_escaped = ASS_PATH.replace("\\", "/").replace(":", "\\:")
    vf_chain = f"ass='{ass_escaped}':fontsdir='{FONTS_DIR}'"

    # Mobile-optimized high-cinema H.264 encode (CRF 20, max 5.5 Mbps -> crisp 1080x1920 Reel ~45-55 MB!)
    # Boost punchy mobile cinema audio subtly (+1.5dB sub warmth @ 75Hz, +1.5dB clarity @ 3kHz)
    cmd = [
        FFMPEG, "-y", "-v", "warning",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{W}x{H}", "-pix_fmt", "rgb24", "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_PATH,
        "-vf", vf_chain,
        "-af", "equalizer=f=75:t=q:w=1.2:g=1.6,equalizer=f=3000:t=q:w=1.4:g=1.4,alimiter=limit=0.93",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-maxrate", "5500k", "-bufsize", "11000k",
        "-profile:v", "high", "-level", "4.1",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
        "-t", f"{DURATION:.3f}",
        "-movflags", "+faststart",
        OUT_MP4,
    ]
    print("=== Starting Ultra-Cinematic 9:16 Instagram Reel Render (1080x1920, 24fps, 2,160 frames) ===")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for f_idx in range(TOTAL_FRAMES):
        t = f_idx / float(FPS)
        zb, lf, sx, sy = impact_pulse_at(t)

        active_i = 0
        for i, sc in enumerate(REEL_SPECS):
            if sc["start"] <= t < sc["end"]:
                active_i = i
                break
        else:
            active_i = len(REEL_SPECS) - 1

        sc = REEL_SPECS[active_i]
        frame = get_scene_frame(sc, imgs[sc["id"]], t, particles, sprites, gx, gy, zb, lf, sx, sy)

        # Smooth crossfade + luminous golden optical flare transition
        if active_i < len(REEL_SPECS) - 1:
            time_to_end = sc["end"] - t
            if time_to_end < XFADE_DUR:
                next_sc = REEL_SPECS[active_i + 1]
                alpha = smoothstep(1.0 - time_to_end / XFADE_DUR)
                next_frame = get_scene_frame(next_sc, imgs[next_sc["id"]], t, particles, sprites, gx, gy, zb, lf, sx, sy)
                frame = frame * (1.0 - alpha) + next_frame * alpha

                # Optical golden light flare wipe on emotional scene transitions
                flare_strength = sc["flare_out"]
                if flare_strength > 0:
                    flare = math.sin(alpha * math.pi) ** 1.3 * 68.0 * flare_strength
                    frame[:, :, 0] += flare * 1.00
                    frame[:, :, 1] += flare * 0.84
                    frame[:, :, 2] += flare * 0.44

        # Dramatic Cinema Color Grade: rich S-curve contrast + deep indigo shadows + warm gold highlights
        frame = np.clip(frame, 0.0, 255.0)
        nrm = frame / 255.0
        # Gentle cinematic S-curve contrast boost
        scurve = nrm * 0.80 + (nrm * nrm * (3.0 - 2.0 * nrm)) * 0.20
        frame = scurve * 255.0
        # Subtle shadow-indigo / highlight-gold split tone
        frame[:, :, 0] *= 1.025
        frame[:, :, 1] *= 1.005
        frame[:, :, 2] *= 1.030

        # Apply vertical cinema vignette + safe-zone readability framing
        frame *= vignette_mult

        # Opening darkness reveal (0.0s - 2.2s)
        if t < 2.2:
            frame *= smoothstep(t / 2.2)

        # Finale golden cosmic climax swell (85.2s-87.3s) + dignified fade to complete black (87.0s-89.8s)
        if t > 85.2:
            if t < 87.3:
                swell = smoothstep((t - 85.2) / 2.1) * 48.0
                frame[:, :, 0] += swell * 1.00
                frame[:, :, 1] += swell * 0.86
                frame[:, :, 2] += swell * 0.48
            if t >= 86.9:
                frame *= (1.0 - smoothstep((t - 86.9) / 2.85))

        # Organic 35mm cinema film grain
        g_tile = grain_bank[f_idx % 24]
        grain_full = np.repeat(np.repeat(g_tile, 2, axis=0), 2, axis=1)
        frame += grain_full

        proc.stdin.write(np.clip(frame, 0.0, 255.0).astype(np.uint8).tobytes())

        if (f_idx + 1) % 240 == 0 or f_idx == TOTAL_FRAMES - 1:
            elapsed = time.time() - t0_wall
            pct = 100.0 * (f_idx + 1) / TOTAL_FRAMES
            print(f"Reel Frame {f_idx + 1:4d}/{TOTAL_FRAMES} ({pct:5.1f}%) | t={t:5.2f}s | elapsed={elapsed:5.1f}s", flush=True)

    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"FFmpeg exited with code {rc}")
    sz_mb = os.path.getsize(OUT_MP4) / (1024 * 1024)
    print(f"=== COMPLETE! Saved {OUT_MP4} ({sz_mb:.2f} MB) in {time.time() - t0_wall:.1f}s ===")


if __name__ == "__main__":
    render()
