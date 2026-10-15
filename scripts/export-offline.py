"""Build a single-file game with its lazy-loaded neural voice assets embedded."""
from pathlib import Path
import base64,json,sys
root=Path(__file__).resolve().parent.parent
voice=root/'dist/voice'
source=(root/'dist/index.html').read_text()
b64=lambda data:base64.b64encode(data).decode('ascii')
worker=b'\n'.join((voice/name).read_bytes() for name in ['ort.wasm.min.js','phonemes.js','character.js','worker.js'])
wasm=b''.join((voice/('ort-wasm-simd-threaded.wasm.part'+str(i))).read_bytes() for i in range(1,4))
assets={'worker':b64(worker),'glue':b64((voice/'ort-wasm-simd-threaded.mjs').read_bytes()),'wasm':b64(wasm),'model':b64((voice/'house.onnx').read_bytes())}
notice=(voice/'LICENSES.txt').read_text().replace('--','—')
output=source.replace('<script>', '<!-- Embedded voice third-party notices:\n'+notice+'\n-->\n<script>globalThis.HOUSE_OFFLINE_ENGINE='+json.dumps(assets,separators=(',',':'))+';</script>\n<script>',1)
path=Path(sys.argv[1]);path.write_text(output);print(str(path),path.stat().st_size,'bytes')
