# === 自動生成フィールド（編集不要）===
TITLE = '会議コスト計算ツール【無料】簡単・無料計算'
DESCRIPTION = '参加者数・平均時給・時間から会議の機会コストをリアルタイム計算。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '参加者数・平均時給・時間から会議の機会コストをリアルタイム計算。'
COLOR1 = '#E0E7FF'
COLOR2 = '#EEF2FF'
COLOR_BTN = '#4338CA'
FOOTER_LINKS = [('https://appadaycreator.github.io/taskflow-timer/', 'TaskFlow Timer'), ('https://appadaycreator.github.io/okr-tracker/', 'OKRトラッカー'), ('https://appadaycreator.github.io/saas-tool-advisor/', 'Saas Tool Advisor')]

# ================================================================
# 以下の3フィールドを実装してください
# ================================================================
# ヒント:
#   - MAIN_HTML: class="card" を使ったUI、class="result" で結果を隠す
#   - JS_CODE: DOMContentLoadedで初期化、onclick or addEventListener を使う
#   - 結果表示: document.getElementById('result').classList.add('show')
#   - 色参照: CSS変数 var(--btn, #4338CA) または直接 #4338CA を使用
#
# === MAIN_HTML サンプル ===
# MAIN_HTML = """
# <div class="card">
#   <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">⚡ タイトル</h2>
#   <label>入力項目</label>
#   <input type="number" id="val1" placeholder="数値を入力" min="0">
#   <button class="btn" style="margin-top:20px;" onclick="calc()">計算する</button>
#   <div class="result" id="result" style="margin-top:16px;">
#     <div class="card" style="text-align:center;">
#       <div id="output" style="font-size:2rem;font-weight:700;color:#4338CA;"></div>
#       <p id="msg" style="color:#666;font-size:14px;margin-top:8px;"></p>
#     </div>
#   </div>
# </div>
# """
# === JS_CODE サンプル ===
# JS_CODE = """
# document.addEventListener('DOMContentLoaded', () => {
#   document.getElementById('val1').addEventListener('keydown', e => {
#     if (e.key === 'Enter') calc();
#   });
# });
# function calc() {
#   const v = parseFloat(document.getElementById('val1').value);
#   if (isNaN(v) || v <= 0) { alert('正しい値を入力してください'); return; }
#   const result = v * 2; // 実際のロジックに置き換える
#   document.getElementById('output').textContent = result.toFixed(0);
#   document.getElementById('msg').textContent = '計算完了';
#   document.getElementById('result').classList.add('show');
# }
# """

CUSTOM_CSS = """"""

# ↓ スケルトンを参考に、サービス固有のUI・ロジックを実装してください
MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">💼 会議コスト計算ツール</h2>
  <!-- 入力フィールドをここに追加 -->

  <button class="btn" style="margin-top:20px;" onclick="calculate()">計算する</button>
  <div class="result" id="result" style="margin-top:16px;">
    <div class="card" style="text-align:center;">
      <div id="output" style="font-size:2.2rem;font-weight:700;color:#4338CA;padding:12px 0;"></div>
      <p id="detail" style="color:#666;font-size:14px;margin-top:4px;"></p>
    </div>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """// ★ここだけ実装（約10行）★
const CFG = {{
  inputs: ['val1'],         // 変更: ['val1','val2',...] など input の id
  error: '値を入力してください', // 変更: バリデーションエラー文
}};
function calcLogic(vals) {{
  const [v1] = vals;  // 変更: vals[0],vals[1]... で各入力値を取得
  const result = v1;  // 変更: 実際の計算式
  const detail = '';  // 変更: 補足説明（単位など）
  return {{ result, detail }};
}}
// ★以下変更不要★
document.addEventListener('DOMContentLoaded',()=>{{
  CFG.inputs.forEach(id=>{{ const el=document.getElementById(id); if(el) el.addEventListener('keydown',e=>{{ if(e.key==='Enter') calculate(); }}); }});
}});
function calculate(){{
  const vals=CFG.inputs.map(id=>parseFloat(document.getElementById(id)?.value)||0);
  if(!vals[0]){{ alert(CFG.error); return; }}
  const {{result,detail}}=calcLogic(vals);
  document.getElementById('output').textContent=typeof result==='number'?result.toLocaleString():result;
  const d=document.getElementById('detail'); if(d) d.textContent=detail||'';
  document.getElementById('result').classList.add('show');
}}"""
