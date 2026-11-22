"""Génère les graphiques SVG de l'article « test d'effort » (journal).

Usage : python3 _outils/graphiques_labo.py   (depuis la racine du site)
Écrit _includes/graphiques/labo-fc.svg, labo-vo2.svg, labo-seuils.svg.

Les couleurs et polices viennent de style.css (classes .ch-…), pour suivre le thème du site.
Données : moyenne des 30 dernières secondes de chaque palier (tapis, pente 1 %).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "_includes" / "graphiques"

# ---------------------------------------------------------------- données
T2025 = {  # 07/11/2025, +0,5 km/h toutes les 2 min
    "v":   [11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5],
    "fc":  [145, 151, 158, 158, 160, 162, 164, 170, 168, 172, 175, 178, 180, 182, 184, 185, 186, 187],
    "vo2": [44.8, 45.8, 51.2, 51.3, 53.9, 53.8, 54.1, 56.9, 58.5, 59.5, 59.0, 59.7, 60.4, 63.0, 63.5, 63.8, 68.0, 68.8],
}
T2026 = {  # 26/10/2026, +1 km/h toutes les 2 min
    "v":   [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    "fc":  [141, 143, 150, 152, 149, 157, 163, 168, 171, 177, 180],
    "vo2": [46.1, 48.1, 49.5, 53.3, 55.2, 58.2, 62.6, 69.7, 74.3, 78.8, 83.4],
}

W, H = 600, 360
M = dict(l=52, r=74, t=22, b=46)


def fr(x, d=0):
    s = f"{x:.{d}f}"
    return s.replace(".", ",")


class Axes:
    def __init__(self, x0, x1, y0, y1):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1

    def X(self, v):
        return M["l"] + (v - self.x0) / (self.x1 - self.x0) * (W - M["l"] - M["r"])

    def Y(self, v):
        return M["t"] + (self.y1 - v) / (self.y1 - self.y0) * (H - M["t"] - M["b"])


def path(ax, xs, ys):
    return "M" + " L".join(f"{ax.X(x):.1f},{ax.Y(y):.1f}" for x, y in zip(xs, ys))


def frame(ax, yticks, yunit, title, desc):
    s = [f'<svg class="ch" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{title[0]} {desc[0]}">',
         f'<title id="{title[0]}">{title[1]}</title>', f'<desc id="{desc[0]}">{desc[1]}</desc>']
    for y in yticks:
        s.append(f'<line class="ch-grid" x1="{M["l"]}" x2="{W - M["r"]}" y1="{ax.Y(y):.1f}" y2="{ax.Y(y):.1f}"/>')
        s.append(f'<text class="ch-tick" x="{M["l"] - 8}" y="{ax.Y(y) + 4:.1f}" text-anchor="end">{fr(y)}</text>')
    s.append(f'<text class="ch-unit" x="{M["l"] - 8}" y="{M["t"] - 8}" text-anchor="end">{yunit}</text>')
    for x in range(int(ax.x0), int(ax.x1) + 1):
        if x % 2:
            continue
        s.append(f'<text class="ch-tick" x="{ax.X(x):.1f}" y="{H - M["b"] + 20}" text-anchor="middle">{x}</text>')
    s.append(f'<line class="ch-axis" x1="{M["l"]}" x2="{W - M["r"]}" y1="{H - M["b"]}" y2="{H - M["b"]}"/>')
    s.append(f'<text class="ch-unit" x="{W - M["r"]}" y="{H - 6}" text-anchor="end">vitesse (km/h)</text>')
    return s


def series(ax, d, key, cls):
    s = [f'<path class="ch-line {cls}" d="{path(ax, d["v"], d[key])}"/>']
    for x, y in zip(d["v"], d[key]):
        s.append(f'<circle class="ch-dot {cls}" cx="{ax.X(x):.1f}" cy="{ax.Y(y):.1f}" r="2.6"/>')
    return s


def fc():
    ax = Axes(11, 21, 130, 190)
    s = frame(ax, range(130, 191, 10), "bpm",
              ("labo-fc-t", "Fréquence cardiaque selon la vitesse, 2025 et 2026"),
              ("labo-fc-d", "À chaque vitesse, la fréquence cardiaque de 2026 est 10 à 20 battements plus basse "
                            "qu'en 2025 : 175 contre 157 à 16 km/h."))
    s += series(ax, T2025, "fc", "ch-old") + series(ax, T2026, "fc", "ch-new")
    # étiquettes directes
    s.append(f'<text class="ch-lab ch-old" x="{ax.X(19.5) + 8:.1f}" y="{ax.Y(187) + 4:.1f}">2025</text>')
    s.append(f'<text class="ch-lab ch-new" x="{ax.X(21) + 8:.1f}" y="{ax.Y(180) + 4:.1f}">2026</text>')
    # annotation à 16 km/h
    x = ax.X(16)
    s.append(f'<line class="ch-note-line" x1="{x:.1f}" x2="{x:.1f}" y1="{ax.Y(175) + 5:.1f}" y2="{ax.Y(157) - 5:.1f}"/>')
    s.append(f'<text class="ch-note" x="{x - 10:.1f}" y="{ax.Y(166) + 4:.1f}" text-anchor="end">−18 bpm</text>')
    s.append(f'<text class="ch-note ch-note-s" x="{x - 10:.1f}" y="{ax.Y(166) + 22:.1f}" text-anchor="end">à 16 km/h</text>')
    s.append("</svg>")
    return "\n".join(s)


def vo2():
    ax = Axes(11, 21, 40, 90)
    s = frame(ax, range(40, 91, 10), "mL/kg/min",
              ("labo-vo2-t", "Consommation d'oxygène selon la vitesse, 2025 et 2026"),
              ("labo-vo2-d", "Jusqu'à 17 km/h, les deux courbes se superposent : même coût en oxygène. "
                             "Le maximum passe de 68,8 en 2025 à environ 84 en 2026."))
    # zone « même coût »
    s.append(f'<rect class="ch-band" x="{ax.X(11):.1f}" y="{M["t"]}" width="{ax.X(17) - ax.X(11):.1f}" '
             f'height="{H - M["t"] - M["b"]}"/>')
    s.append(f'<text class="ch-note" x="{ax.X(11) + 10:.1f}" y="{M["t"] + 22}">même coût en oxygène</text>')
    s.append(f'<text class="ch-note ch-note-s" x="{ax.X(11) + 10:.1f}" y="{M["t"] + 40}">jusqu\'à 17 km/h</text>')
    s += series(ax, T2025, "vo2", "ch-old") + series(ax, T2026, "vo2", "ch-new")
    s.append(f'<text class="ch-lab ch-old" x="{ax.X(19.5) + 8:.1f}" y="{ax.Y(68.8) + 4:.1f}">2025</text>')
    s.append(f'<text class="ch-val ch-old" x="{ax.X(19.5) + 8:.1f}" y="{ax.Y(68.8) + 22:.1f}">max 68,8</text>')
    s.append(f'<text class="ch-lab ch-new" x="{ax.X(21) + 8:.1f}" y="{ax.Y(83.4) + 4:.1f}">2026</text>')
    s.append(f'<text class="ch-val ch-new" x="{ax.X(21) + 8:.1f}" y="{ax.Y(83.4) + 22:.1f}">max ≈ 84</text>')
    s.append("</svg>")
    return "\n".join(s)


def seuils():
    w, h = 600, 200
    l, r = 70, 24
    x0, x1 = 14, 22

    def X(v):
        return l + (v - x0) / (x1 - x0) * (w - l - r)

    rows = [("2025", 70, "ch-old", [("seuil", 17.5, "17,5"), ("VMA", 19.3, "19,3")]),
            ("2026", 140, "ch-new", [("seuil", 18.3, "≈ 18,3"), ("VMA", 21.0, "21")])]
    s = [f'<svg class="ch ch-short" viewBox="0 0 {w} {h}" role="img" aria-labelledby="labo-s-t labo-s-d">',
         '<title id="labo-s-t">Seuil et VMA, 2025 et 2026</title>',
         '<desc id="labo-s-d">Le seuil passe de 17,5 à environ 18,3 km/h, la VMA de 19,3 à 21 km/h.</desc>']
    for v in range(x0, x1 + 1):
        s.append(f'<line class="ch-grid" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="34" y2="{h - 30}"/>')
        s.append(f'<text class="ch-tick" x="{X(v):.1f}" y="{h - 10}" text-anchor="middle">{v}</text>')
    s.append(f'<text class="ch-unit" x="{w - r}" y="18" text-anchor="end">km/h</text>')
    for year, y, cls, pts in rows:
        s.append(f'<text class="ch-lab {cls}" x="{l - 14}" y="{y + 5}" text-anchor="end">{year}</text>')
        s.append(f'<line class="ch-track {cls}" x1="{X(pts[0][1]):.1f}" x2="{X(pts[1][1]):.1f}" y1="{y}" y2="{y}"/>')
        for name, v, txt in pts:
            s.append(f'<circle class="ch-mark {cls}" cx="{X(v):.1f}" cy="{y}" r="6"/>')
            s.append(f'<text class="ch-val {cls}" x="{X(v):.1f}" y="{y - 14}" text-anchor="middle">{name} {txt}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "labo-fc.svg").write_text(fc(), encoding="utf-8")
    (OUT / "labo-vo2.svg").write_text(vo2(), encoding="utf-8")
    (OUT / "labo-seuils.svg").write_text(seuils(), encoding="utf-8")
    print("ok :", ", ".join(p.name for p in sorted(OUT.glob("labo-*.svg"))))
