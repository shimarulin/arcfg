#!/usr/bin/env python3
"""
Find VS Code profile directory by name.
Reads the profiles from VS Code's globalStorage/state.vscdb SQLite database.

Usage:
    python3 find_profile_dir.py <config_dir> <profile_name>

Arguments:
    config_dir   - VS Code config directory (e.g., ~/.config/Code/User)
    profile_name - Name of the profile to find

Output:
    Prints the profile directory path if found, or "NOT_FOUND" if not found.
"""

import sqlite3
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
    db_path = os.path.join(config_dir, "globalStorage", "state.vscdb")

    if not os.path.exists(db_path):
        return "NOT_FOUND"

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.execute(
            "SELECT value FROM ItemTable WHERE key='userDataProfiles'"
        )
        row = cursor.fetchone()

        if row:
            profiles = json.loads(row[0])
            for profile in profiles:
                if profile.get('name') == profile_name:
                    location = profile.get('location', '')
                    return os.path.join(config_dir, "profiles", location)

        return "NOT_FOUND"
    except (sqlite3.Error, json.JSONDecodeError):
        return "NOT_FOUND"
    finally:
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("NOT_FOUND")
        sys.exit(0)

    vscode_config_dir = sys.argv[1]
    profile_name_arg = sys.argv[2]

    result = find_profile_directory(vscode_config_dir, profile_name_arg)
    print(result)
