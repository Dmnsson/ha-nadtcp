"""The nadtcp2 component"""

def get_unique_id(host):
    """Generate a stable unique ID based on device IP address."""
    return f"nad_{host.replace('.', '_')}"