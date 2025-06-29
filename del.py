import os

def delete_mp3_files(root_dir):
    deleted = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".mp3"):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    print(f"🗑️ Deleted: {file_path}")
                    deleted += 1
                except Exception as e:
                    print(f"❌ Failed to delete {file_path}: {e}")
    print(f"\n✅ Deleted {deleted} .mp3 files from: {root_dir}")

# Example usage
if __name__ == "__main__":
    delete_mp3_files("src/pinet_project/data/preprocessed")
