"""Inventory of temporary seismic networks archived at EarthScope (formerly IRIS) that could yield local
earthquake catalogues. Fetches the FDSN network list and keeps networks with a temporary code (first character a
digit or X/Y/Z), no sign of an active-source experiment in the description, at least 10 stations, and at least
360 days of operation. Writes candidates.csv.

Each candidate still needs a prior-work check: some have already been reprocessed for local seismicity."""
import csv, datetime, io, re, urllib.request
URL = 'https://service.earthscope.org/fdsnws/station/1/query?level=network&format=text&nodata=404'
ACTIVE = re.compile(r'active[- ]source|controlled[- ]source|explosi|shot|refraction|airgun|air gun|vibroseis|seismic source', re.I)
def parse(t): return datetime.datetime.fromisoformat(t[:19]) if t else None
txt = urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': 'foundation0-inventory'}), timeout=300).read().decode()
rows = [r for r in csv.reader(io.StringIO(txt), delimiter='|') if r and not r[0].startswith('#')]
temp = [r for r in rows if r[0][0].isdigit() or r[0][0] in 'XYZ']
passive = [r for r in temp if not ACTIVE.search(r[1])]
cand = []
for code, desc, start, end, nsta in passive:
    s, e = parse(start), parse(end)
    years = ((e or datetime.datetime.now()) - s).days / 365.25 if s else 0
    if int(nsta or 0) >= 10 and years >= 360 / 365.25:   # many deployments run 1 Jan to 31 Dec
        cand.append((code, s.date().isoformat() if s else '', e.date().isoformat() if e else '', f'{years:.1f}', int(nsta), desc.strip()))
cand.sort(key=lambda r: (r[1], r[0]))
with open('candidates.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['network', 'start', 'end', 'years', 'stations', 'description']); w.writerows(cand)
print(f'networks {len(rows)}, temporary codes {len(temp)}, no active-source keywords {len(passive)}, >=10 stations and >=360 days {len(cand)}')
