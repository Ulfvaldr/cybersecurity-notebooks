from pyattck import Attck

try:
    # Initialize MITRE ATT&CK framework
    attack = Attck()
    print("MITRE ATT&CK framework initialized successfully!")

    # Accessing tactics from the enterprise ATT&CK framework
    print("List of Tactics:")
    for tactic in attack.enterprise.tactics:
        print(tactic.name)
except Exception as e:
    print(f"Error initializing ATT&CK framework: {e}")
