# Temporary seismic networks archived at EarthScope

Supporting data for [AREAS.md](../../AREAS.md) §8. It comes from the FDSN network list at EarthScope (formerly
IRIS), fetched on 18 Oct 2026.

| File | What |
|---|---|
| `inventory.py` | Fetches the network list and keeps networks with a temporary code (first character a digit or X/Y/Z), no active-source keywords in the description, at least 10 stations, and at least 360 days of operation. |
| `candidates.csv` | The 752 networks that passed on 18 Oct 2026, out of 1,441 networks and 1,174 temporary codes. Columns: code, start, end, years, stations, description. |

**What the filters miss.** They are coarse. An active-source experiment whose description does not say so will
slip through. Some networks have already been reprocessed for local earthquakes; the first one the scout
spot-checked (XB, Cameroon) had been, with deep learning in 2024. Check the literature for each network before
spending compute on it.
