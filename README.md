# Bouldering Gym Occupancy

This Home Assistant custom integration fetches the current occupancy count from a bouldering gym's website and displays it as a sensor.

## Features
- Tracks real-time climber count.
- Provides data for automations and notifications.

## Installation

1. Add this repository to HACS as a custom repository.
2. Install the integration via HACS.
3. Restart Home Assistant.
4. Add the integration to your `configuration.yaml`.

## Configuration

Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: bouldering_gym
