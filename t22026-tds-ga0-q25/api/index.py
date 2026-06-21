from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

# ✏️  PASTE YOUR OWN TELEMETRY JSON HERE (downloaded from exam portal)
TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 208.86,
    "uptime_pct": 98.103,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 177.35,
    "uptime_pct": 99.007,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 234.49,
    "uptime_pct": 98.596,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 115.66,
    "uptime_pct": 97.673,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 225.94,
    "uptime_pct": 97.432,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 129.73,
    "uptime_pct": 97.594,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 134.94,
    "uptime_pct": 98.898,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 128.86,
    "uptime_pct": 99.442,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 165.75,
    "uptime_pct": 98.387,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 141.39,
    "uptime_pct": 97.289,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 176.78,
    "uptime_pct": 97.632,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 166.09,
    "uptime_pct": 97.405,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 124.72,
    "uptime_pct": 97.785,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 137.3,
    "uptime_pct": 97.324,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 122.64,
    "uptime_pct": 97.105,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 139.21,
    "uptime_pct": 97.856,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 175.76,
    "uptime_pct": 97.398,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 170.75,
    "uptime_pct": 97.689,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 174.41,
    "uptime_pct": 97.893,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 184.52,
    "uptime_pct": 98.404,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 230.72,
    "uptime_pct": 98.272,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 192.68,
    "uptime_pct": 98.224,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 149.24,
    "uptime_pct": 98.717,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 204.04,
    "uptime_pct": 99.039,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 129.59,
    "uptime_pct": 97.368,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 115.52,
    "uptime_pct": 98.39,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 115.56,
    "uptime_pct": 98.033,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 165.79,
    "uptime_pct": 98.974,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 155.8,
    "uptime_pct": 97.426,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 186.84,
    "uptime_pct": 99.383,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 140.65,
    "uptime_pct": 97.461,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 152.77,
    "uptime_pct": 98.186,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 174.93,
    "uptime_pct": 97.995,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 136.43,
    "uptime_pct": 97.577,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 129.05,
    "uptime_pct": 99.412,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 152.22,
    "uptime_pct": 99.476,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}