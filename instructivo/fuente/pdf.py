"""Imprime los cuatro PDF de los instructivos de Ratio Milpa con Chrome sin interfaz.
Requiere el servidor local (python -m http.server 8775 --directory D:/CLAUDE/RatioMilpa).
Uso:  python pdf.py"""
import os, random, re, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, '..')
NAV = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PERFIL = os.path.join(os.environ.get('TEMP', AQUI), 'milpa_pdf_perfil')
TRABAJOS = [('productor', 'es', 'RatioMilpa-Instructivo-Productor.pdf'), ('productor', 'en', 'RatioMilpa-Producer-Guide.pdf'),
            ('cientifico', 'es', 'RatioMilpa-Instructivo-Cientifico.pdf'), ('cientifico', 'en', 'RatioMilpa-Scientist-Guide.pdf')]
for guia, lang, nombre in TRABAJOS:
    f = os.path.join(OUT, nombre)
    url = f'http://localhost:8774/instructivo-{guia}.html?lang={lang}&eager&v={random.randint(1, 10**9)}'
    subprocess.run([NAV, '--headless=new', '--disable-gpu', f'--user-data-dir={PERFIL}', '--no-pdf-header-footer', '--virtual-time-budget=20000',
                    f'--print-to-pdf={f}', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    b = open(f, 'rb').read()
    n = len(re.findall(rb'/Type\s*/Page[^s]', b))
    print(f'{nombre}: {n} p, {len(b) / 1048576:.1f} MB')
