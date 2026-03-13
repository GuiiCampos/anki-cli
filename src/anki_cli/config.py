from .paths import CONFIG_FILE, DEFAULT_CONFIG


def load_config():
    config = DEFAULT_CONFIG.copy()

    if not CONFIG_FILE.exists():
        return config

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config


def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        for key in DEFAULT_CONFIG:
            value = config.get(key, DEFAULT_CONFIG[key])
            f.write(f"{key}={value}\n")