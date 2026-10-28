# Project Chandana V5 — Floating Rose Universe 🌹

A birthday experience for Sreya Chandana (“My Bangaram”), turning 20 on October 28, 2026.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. The app has independent routes for the home, cake, memories, individual photo details, letter, hug, gifts, Paris and finale.

## Deploy to Render

Upload the project to a Git repository and create a Render web service using `render.yaml` (or set build command `pip install -r requirements.txt`, start command `gunicorn app:app`).

## Notes

- Includes 14 locally stored optimized photos of Sreya. Keep the project private if desired.
- Pink-and-white editorial homepage, floating 3D parallax photo collage, mixed heart/round/arched frames, rose motifs and glass navigation.
- Three.js / GSAP load from public CDNs, so network access is needed for enhanced 3D effects; CSS layout still works offline.
- Audio is a user-activated synthesized ambient tone; no licensed songs included.
- Photo details use cinematic entrance and rose reveal, and can be browsed in sequence.
- Respect reduced-motion settings; mobile touch navigation is supported.
