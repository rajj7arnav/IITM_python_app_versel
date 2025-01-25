from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# Initialize the app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# The data
data=[{"name":"ghYw6","marks":56},{"name":"g5","marks":12},{"name":"qpXySaerV1","marks":7},{"name":"aj6s","marks":41},{"name":"Pyulr0L18","marks":81},{"name":"fBwIIiLzpu","marks":29},{"name":"5","marks":97},{"name":"mX","marks":29},{"name":"wfO4kgCGI","marks":1},{"name":"1QAUPQ3n","marks":40},{"name":"83MWs55rsy","marks":87},{"name":"qg3XUPfodl","marks":64},{"name":"r0ywNcH","marks":19},{"name":"XnDpmD","marks":66},{"name":"5Mkfyx","marks":14},{"name":"BuhTZwlInK","marks":25},{"name":"G","marks":92},{"name":"N","marks":72},{"name":"80m9iUtiY","marks":20},{"name":"sAvyJ43","marks":10},{"name":"GZ","marks":94},{"name":"s","marks":28},{"name":"ayZ50IYv","marks":97},{"name":"61SYwIpQ","marks":38},{"name":"i2aIion","marks":39},{"name":"yhN2jmMyi","marks":91},{"name":"qdZESXu","marks":79},{"name":"u","marks":25},{"name":"SWcWN","marks":13},{"name":"FMsFT68x","marks":66},{"name":"KT","marks":18},{"name":"aNH","marks":8},{"name":"TSy6U","marks":82},{"name":"xLqO4ag","marks":16},{"name":"wKcPP4","marks":39},{"name":"q","marks":28},{"name":"GhcFVx","marks":88},{"name":"wCv","marks":67},{"name":"Lei9","marks":75},{"name":"ToIECQ","marks":2},{"name":"cR9SabY","marks":17},{"name":"kD1d","marks":95},{"name":"YW6B9RKgq7","marks":31},{"name":"NIMF2S9","marks":34},{"name":"czxKX","marks":25},{"name":"C0qmP7CB","marks":69},{"name":"mYZ2Kap","marks":2},{"name":"1","marks":15},{"name":"CnKB","marks":72},{"name":"XAvBfUgUWT","marks":53},{"name":"AI","marks":75},{"name":"1h9H5jXh","marks":73},{"name":"27jI05HL","marks":56},{"name":"281v","marks":7},{"name":"VV7EfTkUG","marks":71},{"name":"grqBiursyD","marks":37},{"name":"5w2awxU6Ne","marks":42},{"name":"1","marks":86},{"name":"z","marks":50},{"name":"TSFox","marks":29},{"name":"UQZ","marks":14},{"name":"rrgQw","marks":22},{"name":"Z0","marks":87},{"name":"Qn","marks":59},{"name":"3r","marks":27},{"name":"UgIbjsfX","marks":59},{"name":"Ina7","marks":35},{"name":"afA","marks":25},{"name":"8","marks":53},{"name":"JC","marks":89},{"name":"vwg","marks":93},{"name":"RL8rjP13o","marks":6},{"name":"u2gmdRzA","marks":58},{"name":"6d1Vfqn","marks":72},{"name":"N","marks":80},{"name":"zpY1I","marks":56},{"name":"XrXO","marks":23},{"name":"Ld","marks":4},{"name":"DXq","marks":24},{"name":"NAZzn3xju","marks":51},{"name":"slUQKMbr","marks":30},{"name":"u3tB","marks":48},{"name":"45Oo","marks":4},{"name":"yFBJNgH0","marks":37},{"name":"cK","marks":15},{"name":"PwhhcYOkxJ","marks":47},{"name":"J5D","marks":84},{"name":"X","marks":24},{"name":"qUnG","marks":84},{"name":"xQapH","marks":95},{"name":"Mb73","marks":18},{"name":"D5XqiZcz","marks":25},{"name":"VnKz","marks":83},{"name":"j3","marks":78},{"name":"93p9","marks":8},{"name":"tjJCo","marks":25},{"name":"pDuyQ","marks":63},{"name":"wtvv0","marks":37},{"name":"yuq8na","marks":55},{"name":"N1RUoJRz9s","marks":12}]

data_dict = {item["name"]: item["marks"] for item in data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    marks = [data_dict.get(n, "Name not found") for n in name]
    return {"marks": marks}
