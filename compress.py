import joblib
import os

# Load existing model
model = joblib.load("model.pkl")

print("Model type:", type(model))
print("Original size:", os.path.getsize("model.pkl") / (1024 * 1024), "MB")

# Save compressed model
joblib.dump(
    model,
    "model_compressed.pkl",
    compress=3
)

print(
    "Compressed size:",
    os.path.getsize("model_compressed.pkl") / (1024 * 1024),
    "MB"
)

print("Done!")