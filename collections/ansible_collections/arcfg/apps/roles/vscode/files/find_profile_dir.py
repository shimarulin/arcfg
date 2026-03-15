#!/usr/bin/env python3
"""
Find VS Code profile directory by name.
Reads the profiles from VS Code's globalStorage/storage.json file.

Usage:
    python3 find_profile_dir.py <config_dir> <profile_name>

Arguments:
    config_dir   - VS Code config directory (e.g., ~/.config/Code/User)
    profile_name - Name of the profile to find

Output:
    Prints the profile directory path if found, or "NOT_FOUND" if not found.
"""

import json
import os
import sys


def find_profile_directory(config_dir: str, profile_name: str) -> str:
    """
    Find VS Code profile directory by name.

    Args:
        config_dir: VS Code config directory path
        profile_name: Name of the profile to find

    Returns:
        Profile directory path or "NOT_FOUND"
    """
    storage_path = os.path.join(config_dir, "globalStorage", "storage.json")

    if not os.path.exists(storage_path):
        return "NOT_FOUND"

    try:
        with open(storage_path, 'r', encoding='utf-8') as f:
            storage_data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return "NOT_FOUND"

    profiles = storage_data.get('userDataProfiles', [])

    for profile in profiles:
        if profile.get('name') == profile_name:
            location = profile.get('location', '')
            return os.path.join(config_dir, "profiles", location)

    return "NOT_FOUND"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("NOT_FOUND")
        sys.exit(0)

    vscode_config_dir = sys.argv[1]
    profile_name_arg = sys.argv[2]

    result = find_profile_directory(vscode_config_dir, profile_name_arg)
    print(result)
