import os
import maps4fs as mfs

# Check if templates directory exists
if os.path.exists("templates"):
    print("✅ Templates directory found")

    # Check for required files
    fs25_template = "templates/fs25-map-template.zip"
    fs25_schema = "templates/fs25/texture_schemas/fs25-texture-schema.json"

    if os.path.exists(fs25_template):
        print("✅ FS25 map template found")
    else:
        print("❌ FS25 map template missing")

    if os.path.exists(fs25_schema):
        print("✅ FS25 texture schema found")
    else:
        print("❌ FS25 texture schema missing")

    print("🎉 Setup appears to be working!")
else:
    print("❌ Templates directory not found")
    print("Please download the templates folder from the repository")
