# NOAA Foreign Climate Data scans

Supporting data for [AREAS.md](../../AREAS.md) §9. It lists the scans in the NOAA Central Library's public S3 bucket
(`library.oarcloud.noaa.gov`, prefix `docs.lib/htdocs/rescue/cd`), taken on 18 Oct 2026.

| File | What |
|---|---|
| `inventory.py` | Lists the bucket and writes one row per PDF. |
| `scans.csv` | 5,424 PDFs, 192.9 GB in total, in 526 folders. Each has a matching TIFF in a `cd###_tif` folder. Columns: folder, file, bytes, URL. |

**First task.** The PDF names are opaque, so map them to country, title and years first, for example
`cd001_pdf/000CE50D.pdf` is Argentina's *Resumen Mensual del Tiempo* for July 1942. The titles are not in the
bucket. Then check each station-year against ISPD before transcribing anything.
