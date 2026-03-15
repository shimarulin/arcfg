#!/usr/bin/env python3
"""
Create VS Code profile if it doesn't exist.
Writes to VS Code's globalStorage/storage.json file.

Usage:
    python3 create_profile.py <config_dir> <profile_name> [icon]

Arguments:
    config_dir   - VS Code config directory (e.g., ~/.config/Code/User)
    profile_name - Name of the profile to create
    icon         - Optional icon name (e.g., 'terminal', 'code', 'server')

Output:
    Prints "CREATED:<location>" if profile was created,
    "EXISTS:<location>" if already exists, or "ERROR:<message>" on failure.
"""

import json
import os
import random
import sys


def generate_location() -> str:
    """Generate a profile location ID in VS Code format (signed 32-bit hex)."""
    # VS Code uses signed 32-bit integers represented as hex strings without 0x prefix
    value = random.randint(-2147483648, 2147483647)
    if value < 0:
        return hex(value)[3:]  # Remove '0x' and keep the '-' sign
    else:
        return hex(value)[2:]  # Remove '0x' prefix


def create_profile(config_dir: str, profile_name: str, icon: str = None) -> str:
    """
    Create VS Code profile if it doesn't exist.

    Args:
        config_dir: VS Code config directory path
        profile_name: Name of the profile to create
        icon: Optional icon name

    Returns:
        "CREATED:<location>", "EXISTS:<location>", or "ERROR:<message>"
    """
    storage_path = os.path.join(config_dir, "globalStorage", "storage.json")

    # Ensure globalStorage directory exists
    global_storage_dir = os.path.join(config_dir, "globalStorage")
    os.makedirs(global_storage_dir, exist_ok=True)

    # Read existing storage.json or create new
    storage_data = {}
    if os.path.exists(storage_path):
        try:
            with open(storage_path, 'r', encoding='utf-8') as f:
                storage_data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            return f"ERROR: Failed to read storage.json: {e}"

    # Get existing profiles
    profiles = storage_data.get('userDataProfiles', [])

    # Check if profile already exists
    for profile in profiles:
        if profile.get('name') == profile_name:
            return f"EXISTS:{profile.get('location')}"

    # Generate new location
    location = generate_location()

    # Create new profile entry
    new_profile = {
        "location": location,
        "name": profile_name
    }
    if icon:
        new_profile["icon"] = icon

    profiles.append(new_profile)
    storage_data['userDataProfiles'] = profiles

    # Save storage.json
    try:
        with open(storage_path, 'w', encoding='utf-8') as f:
            json.dump(storage_data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        return f"ERROR: Failed to write storage.json: {e}"

    # Create profile directory
    profile_dir = os.path.join(config_dir, "profiles", location)
    try:
        os.makedirs(profile_dir, exist_ok=True)
    except OSError as e:
        return f"ERROR: Failed to create profile directory: {e}"

    return f"CREATED:{location}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR: Missing arguments")
        sys.exit(1)

    vscode_config_dir = sys.argv[1]
    profile_name_arg = sys.argv[2]
    icon_arg = sys.argv[3] if len(sys.argv) > 3 else None

    result = create_profile(vscode_config_dir, profile_name_arg, icon_arg)
    print(result)
