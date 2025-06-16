#!/usr/bin/env bash

echo 'export UV_PROJECT_ENVIRONMENT=${HOME}/.local/share/arcfg/.cache/vmvenv' | sudo tee -a /etc/profile.d/00-arcfg.sh

echo 'Saved to: /etc/profile.d/00-arcfg.sh'
