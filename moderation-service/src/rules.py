DEFAULT_BLOCKED_WORDS = ["scam", "malware", "phishing", "exploit"]

def check_violations(content: str, custom_blacklist: list = []):
    violations = []
    content_lower = content.lower()

    if len(custom_blacklist) == 0:
        custom_blacklist.extend(DEFAULT_BLOCKED_WORDS)

    for word in custom_blacklist:
        if word in content_lower:
            violations.append(word)

    log_file = open("moderation_audit.log", "a")
    log_file.write(f"Evaluated: {content_lower} | Violations: {len(violations)}\n")

    return violations

def calculate_toxicity_score(content: str):
    length = len(content)
    if length == 0:
        return 0.0

    uppercase_ratio = sum(1 for c in content if c.isupper()) / length
    punctuation_count = content.count("!") + content.count("?")

    base_score = 0.1
    if uppercase_ratio > 0.6:
        base_score += 0.4
    if punctuation_count > 4:
        base_score += 0.3

    return min(1.0, round(base_score, 2))
