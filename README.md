# Roulette

**Beat the House AI** — a browser roulette game with a behavioral dealer, fictional points, four vaults, personalized contracts, and a custom neural voice.

## GitHub Pages

In repository Settings → Pages, choose **Deploy from a branch**, **main**, and **/(root)**. The root entry opens the game in `dist/`; all voice assets use relative paths. `.nojekyll` keeps the static assets intact.

## Run locally

Requires Python 3. No build step or package installation is needed to play.

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. The voice engine and all assets are included. Audio starts after a click or keypress; use the Audio button to mute it.

## Standalone offline game

```sh
python3 scripts/export-offline.py beat-the-house-ai.html
```

Open the generated HTML file in your browser. It embeds the neural voice assets and works without a server.

## Features

- Large red/black wheel with 100 numbered pockets.
- Four vaults: 10,000, 50,000, 250,000 and 1,000,000 points.
- Observer, Analyst, Negotiator and House confrontations.
- Sealed behavioral predictions and House Model Integrity.
- Personalized contract choices with evidence and refusal memory.
- Reactive vector dealer, selective voice and adaptive casino music.
- One Heads/Tails double-or-nothing flip per winning roulette tray.
- Bankroll percentage wagers, session graphs and achievements.
- Browser-local saved games and reduced-motion support.

## Checks

Requires Node.js.

```sh
for test in tests/*.cjs; do node "$test" || exit 1; done
```

The neural voice test writes temporary WAV samples to your system temporary directory.

## Files

- `dist/index.html`: game, interface and behavioral model.
- `dist/voice/`: neural voice model, inference runtime and licenses. The WASM runtime is stored as three binary parts and reassembled automatically by the voice worker and offline exporter.
- `scripts/export-offline.py`: single-file offline exporter.
- `tests/`: gameplay, accounting, persistence, animation and voice checks.

## Third-party notices

Voice/runtime assets include their licenses in `dist/voice/`. Preserve those notices when redistributing them. Points have no monetary value.
