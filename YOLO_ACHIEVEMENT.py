# YOLO Achievement Unlock
# You Only Live Once - Merge without a review

def unlock_yolo():
    """Unlock the YOLO achievement by merging without review"""
    achievement = {
        "name": "YOLO",
        "description": "You want it? You merge it.",
        "unlocked": True,
        "method": "Merge pull request without review"
    }
    return achievement

if __name__ == "__main__":
    result = unlock_yolo()
    print(f"Achievement: {result['name']}")
    print(f"Status: Unlocked = {result['unlocked']}")
    print(f"Method: {result['method']}")

# Merge this PR without review to unlock the YOLO achievement!
