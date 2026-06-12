import os
import json
import requests
from datetime import date

MATOMO_URL = os.environ.get("MATOMO_URL", "https://matomo.research.software/")
SITE_ID    = os.environ.get("MATOMO_SITE_ID", "7")
TOKEN      = os.environ.get("MATOMO_TOKEN", "")

USE_DUMMY  = not TOKEN  # if no token, fall back to dummy data

DUMMY_DATA = {
    "generated_at": date.today().isoformat(),
    "total_visits": 18472,
    "total_unique_visitors": 11823,
    "top_countries": [
        { "name": "United Kingdom", "visits": 3241 },
        { "name": "Germany",        "visits": 2187 },
        { "name": "United States",  "visits": 1943 },
        { "name": "Netherlands",    "visits": 1502 },
        { "name": "France",         "visits": 987  },
        { "name": "Italy",          "visits": 834  },
        { "name": "Spain",          "visits": 721  },
        { "name": "Sweden",         "visits": 614  },
        { "name": "Switzerland",    "visits": 589  },
        { "name": "Australia",      "visits": 412  }
    ],
    "referrers": [
        { "type": "Direct Entry",   "visits": 6823 },
        { "type": "Search Engines", "visits": 5341 },
        { "type": "Websites",       "visits": 4102 },
        { "type": "Social Networks","visits": 1876 },
        { "type": "Campaigns",      "visits": 330  }
    ]
}


def api(method, extra=""):
    url = (
        f"{MATOMO_URL}?module=API&method={method}"
        f"&idSite={SITE_ID}&format=JSON&token_auth={TOKEN}{extra}"
    )
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict) and data.get("result") == "error":
        raise RuntimeError(f"Matomo API error: {data.get('message')}")
    return data


def fetch_live():
    print("Fetching live data from Matomo...")

    summary = api(
        "VisitsSummary.get",
        "&period=range&date=2000-01-01,today"
    )

    countries = api(
        "UserCountry.getCountry",
        "&period=range&date=last365&filter_limit=15"
    )

    referrers = api(
        "Referrers.getReferrerType",
        "&period=range&date=last365"
    )

    return {
        "generated_at":          date.today().isoformat(),
        "total_visits":          summary.get("nb_visits", 0),
        "total_unique_visitors": summary.get("nb_uniq_visitors", 0),
        "top_countries": [
            {"name": c["label"], "visits": c["nb_visits"]}
            for c in (countries if isinstance(countries, list) else [])
        ],
        "referrers": [
            {"type": r["label"], "visits": r["nb_visits"]}
            for r in (referrers if isinstance(referrers, list) else [])
        ]
    }


def main():
    if USE_DUMMY:
        print("No MATOMO_TOKEN set — using dummy data.")
        output = DUMMY_DATA
    else:
        try:
            output = fetch_live()
            print(f"Live data fetched. Total visits: {output['total_visits']}")
        except Exception as e:
            print(f"WARNING: Matomo fetch failed ({e}). Falling back to dummy data.")
            output = DUMMY_DATA

    out_path = os.path.join(
        os.path.dirname(__file__), "../../_data/matomo_stats.json"
    )
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Written to {out_path}")


if __name__ == "__main__":
    main()
