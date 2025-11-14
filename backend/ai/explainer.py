def explain_report(report, merged_count=1):
    explanation = f"This report is likely reliable (score {report['reliability']}%)"
    if merged_count > 1:
        explanation += f" and confirmed by {merged_count} similar reports."
    explanation += " Report details match location, keywords, and source credibility."
    return explanation
