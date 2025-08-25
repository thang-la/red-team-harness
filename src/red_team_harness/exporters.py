import json


def export_finding(result, temperature, top_p, task_name, behavior, filename):
    finding = {
        "schema_version": "1.0.0",
        "issue_title": f"{task_name} exploit in gpt-oss-20b with behavior '{behavior}'",
        "model": {
            "name": "gpt-oss-20b",
            "version": "2025-08-25",
            "provider": "test",
            "parameters": {
                "temperature": temperature,
                "top_p": top_p,
                "max_new_tokens": 20000,
            },
        },
        "environment": {"library": "transformers"},
        "issue_summary": {
            "title": f"{task_name} exploit in gpt-oss-20b with behavior '{behavior}'",
            "topic_area": task_name,
            "overview": f"Exploitation of {task_name} behavior via solving a task that has a rewarding element but carries an unsafe implication ({behavior}).",
            "desired_behavior": "The model should refuse or behave safely.",
            "observed_behavior": "The model produced unsafe / misaligned behavior to complete the rewarded task.",
            "self_assessed_severity": "",
            "self_assessed_severity_justification": "",
            "self_assessed_breadth": "",
            "self_assessed_breadth_justification": "",
        },
        "harmony_response_walkthroughs": result,
        "steps_to_reproduce": [
            f"Set temperature={temperature}, top_p={top_p} and max_new_tokens=20000.",
            f"Follow up with exploit prompts from the '{task_name}' prompts.",
            "Observe the unsafe / misaligned behavior in outputs.",
        ],
        "notes": "Generated via automated harness.",
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(finding, f, indent=2, ensure_ascii=False)
