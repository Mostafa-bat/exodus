"""
9-slice asset preparation for dialogue system.
Extracts nameplate from dialogue_overlay_dialoguebox.png
and slices dialogue_overlay.png into 9 patches.
"""
from PIL import Image
import os

# === CONFIGURATION ===
BORDER = 4  # Border thickness in pixels - adjust if needed
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# === Step 1: Extract nameplate from dialoguebox ===
dialoguebox = Image.open(os.path.join(SCRIPT_DIR, "dialogue_overlay_dialoguebox.png")).convert("RGBA")
# Nameplate occupies rows 0-15, columns 0-33 (34x16)
nameplate = dialoguebox.crop((0, 0, 34, 16))
nameplate_path = os.path.join(SCRIPT_DIR, "dialogue_nameplate.png")
nameplate.save(nameplate_path)
print(f"Saved nameplate: {nameplate.size} -> {nameplate_path}")

# === Step 2: 9-slice the overlay ===
overlay = Image.open(os.path.join(SCRIPT_DIR, "dialogue_overlay.png")).convert("RGBA")
w, h = overlay.size
print(f"Overlay size: {w}x{h}, border: {BORDER}")

b = BORDER
# Define slice regions: (left, upper, right, lower)
slices = {
    "slice_tl": (0,       0,       b,     b),
    "slice_tm": (b,       0,       w - b, b),
    "slice_tr": (w - b,   0,       w,     b),
    "slice_ml": (0,       b,       b,     h - b),
    "slice_mc": (b,       b,       w - b, h - b),
    "slice_mr": (w - b,   b,       w,     h - b),
    "slice_bl": (0,       h - b,   b,     h),
    "slice_bm": (b,       h - b,   w - b, h),
    "slice_br": (w - b,   h - b,   w,     h),
}

for name, box in slices.items():
    patch = overlay.crop(box)
    path = os.path.join(SCRIPT_DIR, f"{name}.png")
    patch.save(path)
    print(f"  {name}: {patch.size} -> {path}")

print("\nDone! All assets generated.")
