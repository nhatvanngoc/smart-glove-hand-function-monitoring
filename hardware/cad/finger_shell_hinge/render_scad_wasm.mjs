// Render finger_shell_hinge.scad bằng CHÍNH engine OpenSCAD (bản WASM,
// gói npm "openscad-wasm-prebuilt", chạy qua Node.js — không cần cài
// OpenSCAD desktop/apt). Dùng để XUẤT STL và ĐỐI CHIẾU hình học với bản
// CadQuery (finger_shell_hinge.py) — xem cross_check.py và README §5.
//
// Chạy:
//   npm install
//   npm run render
// hoặc:
//   node render_scad_wasm.mjs
import { createOpenSCAD } from "openscad-wasm-prebuilt";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const SCAD_PATH = path.join(HERE, "finger_shell_hinge.scad");
const OUT_DIR = path.join(HERE, "out", "scad");
fs.mkdirSync(OUT_DIR, { recursive: true });

const srcCode = fs.readFileSync(SCAD_PATH, "utf8");

const PARTS = [
  ["top", "top_shell_dorsal.stl"],
  ["bottom", "bottom_shell_palmar.stl"],
  ["pin", "hinge_pin.stl"],
  ["assembly_closed", "assembly_closed.stl"],
  ["assembly_open", "assembly_open.stl"],
];

async function renderPart(part, outName) {
  const openscad = await createOpenSCAD({
    print: () => {},
    printErr: (t) => {
      if (/WARNING|ERROR/i.test(t)) console.log(`  [${part}] ${t}`);
    },
  });
  const inst = openscad.getInstance();
  // OpenSCAD: phép gán biến ở dòng SAU CÙNG trong file sẽ thắng, nên ta
  // nối thêm 1 dòng gán lại PART vào cuối mã nguồn gốc để chọn chi tiết
  // cần render, không cần sửa file .scad gốc.
  const code = `${srcCode}\nPART = "${part}";\n`;
  inst.FS.writeFile("/input.scad", code);
  const t0 = Date.now();
  const ret = inst.callMain(["/input.scad", "-o", "/output.stl"]);
  const dt = ((Date.now() - t0) / 1000).toFixed(1);
  if (ret !== 0) {
    throw new Error(`OpenSCAD thoat voi ma loi ${ret} cho PART="${part}"`);
  }
  const data = inst.FS.readFile("/output.stl", { encoding: "binary" });
  const outPath = path.join(OUT_DIR, outName);
  fs.writeFileSync(outPath, Buffer.from(data, "binary"));
  console.log(`  OK  PART="${part}" -> out/scad/${outName}  (${dt}s, ${data.length} bytes)`);
}

console.log("Dang render finger_shell_hinge.scad bang OpenSCAD WASM (engine that)...");
for (const [part, outName] of PARTS) {
  await renderPart(part, outName);
}
console.log("Xong. STL nam trong out/scad/ — doi chieu voi out/*.stl (ban CadQuery) bang cross_check.py");
