"""Inventory of NOAA Central Library's Foreign Climate Data scans (climate data rescue), from the public S3 bucket.
Lists every PDF under docs.lib/htdocs/rescue/cd*, with its folder and size. Writes scans.csv and prints totals.
Which station-years are already in ISPD or ICOADS must still be checked before transcribing anything."""
import csv, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
B = 'https://s3.amazonaws.com/library.oarcloud.noaa.gov'
NS = {'s': 'http://s3.amazonaws.com/doc/2006-03-01/'}
keys, token = [], None
while True:
    q = {'list-type': '2', 'prefix': 'docs.lib/htdocs/rescue/cd'}
    if token: q['continuation-token'] = token
    x = ET.fromstring(urllib.request.urlopen(f"{B}?{urllib.parse.urlencode(q)}", timeout=120).read())
    for c in x.findall('s:Contents', NS):
        keys.append((c.find('s:Key', NS).text, int(c.find('s:Size', NS).text), c.find('s:LastModified', NS).text[:10]))
    if x.find('s:IsTruncated', NS).text != 'true': break
    token = x.find('s:NextContinuationToken', NS).text
pdf = [k for k in keys if k[0].lower().endswith('.pdf')]
with open('scans.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['folder', 'file', 'bytes', 'url'])
    for k, size, _ in pdf:
        folder, name = k.rsplit('/', 1)
        w.writerow([folder.rsplit('/', 1)[-1], name, size, f'{B}/{urllib.parse.quote(k)}'])
print(f"objects {len(keys)}, PDFs {len(pdf)}, folders {len({k.rsplit('/', 1)[0] for k, _, _ in pdf})}, {sum(s for _, s, _ in pdf) / 1e9:.1f} GB")
