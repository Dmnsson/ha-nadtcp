# ha-nadtcp

Home Assistant custom integration for the **NAD C338** amplifier, controlled via TCP/IP.

This is a fork of [Sjoerdfc/ha-nadtcp](https://github.com/Sjoerdfc/ha-nadtcp), which itself originates from [martonperei/ha-nadtcp](https://github.com/martonperei/ha-nadtcp).

Tested on Home Assistant Core **2026.6.3**.

---

## Changes in this fork

- **`unique_id` support** — entities are now properly registered in the HA entity registry, so they persist across restarts and can be renamed/customized in the UI.
- **Removed deprecated `hass.loop` usage** — the event loop is now resolved internally in `nadtcpv10.py` rather than passed in from outside.
- **`async_dispatcher_send`** replaces the sync `dispatcher_send` for correct async behavior.
- **Removed duplicate `state` property** that was silently shadowing the correct implementation.

---

## Requirements

- NAD C338 amplifier connected to your network
- Home Assistant with support for custom components

---

## Installation

1. Copy the `custom_components/nadtcp2` folder into your HA `config/custom_components/` directory.
2. Restart Home Assistant.

---

## Configuration

Add the following to your `configuration.yaml`:

```yaml
media_player:
  - platform: nadtcp2
    name: NAD C338
    host: 192.168.1.x        # IP address of your amplifier
    min_volume: -70           # Minimum volume in dB
    max_volume: -20           # Maximum volume in dB
    volume_step: 2            # Step size in dB for volume up/down
    reconnect_interval: 10    # Seconds between reconnection attempts
```

Only `host` is required. All other options have defaults:

| Option | Default | Description |
|---|---|---|
| `name` | `NAD amplifier` | Entity display name |
| `min_volume` | `-80` | Minimum volume (dB) |
| `max_volume` | `10` | Maximum volume (dB) |
| `volume_step` | `4` | Volume step size (dB) |
| `reconnect_interval` | `10` | Reconnect delay (seconds) |

---

## Supported features

- Power on/off
- Volume set, step up/down
- Mute/unmute
- Source selection

Available sources: `Stream`, `Wireless`, `TV`, `Phono`, `Coax1`, `Coax2`, `Opt1`, `Opt2`
