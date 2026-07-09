import json

import gradio as gr
import lightgbm as lgb
import pandas as pd

MODEL_PATH = "m5_lgb_model.txt"
META_PATH = "feature_meta.json"

model = lgb.Booster(model_file=MODEL_PATH)

with open(META_PATH) as f:
    meta = json.load(f)

FEATURES = meta["features"]
CAT_FEATURES = meta["cat_features"]
FEATURE_META = meta["meta"]


def build_inputs():
    """Create one Gradio input component per model feature."""
    components = []
    for col in FEATURES:
        info = FEATURE_META[col]
        if info["type"] == "categorical":
            components.append(
                gr.Dropdown(
                    choices=info["categories"],
                    value=info["categories"][0],
                    label=col,
                )
            )
        else:
            components.append(
                gr.Number(value=round(info["default"], 4), label=col)
            )
    return components


def predict(*values):
    row = dict(zip(FEATURES, values))
    df = pd.DataFrame([row])

    # Re-apply the exact categorical encoding used at training time
    for c in CAT_FEATURES:
        df[c] = pd.Categorical(df[c], categories=FEATURE_META[c]["categories"])

    # Numeric columns should be numeric dtype
    for c in FEATURES:
        if c not in CAT_FEATURES:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    pred = model.predict(df)[0]
    pred = max(0.0, float(pred))
    return f"Predicted sales: {pred:.2f}"


with gr.Blocks(title="M5 Sales Forecast — LightGBM") as demo:
    gr.Markdown(
        "# M5 Sales Forecasting (LightGBM)\n"
        "Enter feature values and click **Predict** to get the forecasted "
        "sales quantity for that item/store/day combination."
    )
    with gr.Row():
        with gr.Column(scale=2):
            inputs = build_inputs()
        with gr.Column(scale=1):
            output = gr.Textbox(label="Prediction", lines=2)
            btn = gr.Button("Predict", variant="primary")

    btn.click(predict, inputs=inputs, outputs=output)

if __name__ == "__main__":
    demo.launch()
